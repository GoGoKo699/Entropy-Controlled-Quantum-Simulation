"""Finite checks of controlled Hermitian noise and its explicit witnesses.

Run from the repository root: python3 verification/checks.py
These checks validate finite identities and residuals, not general theorem proofs.
"""
from pathlib import Path
from itertools import product
import argparse
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm, expm_frechet, logm

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '--output',
    type=Path,
    help='Optionally save the complete numerical result to this JSON path.',
)
args = parser.parse_args()

if not __debug__:
    raise RuntimeError('Run without Python -O: scientific checks use assertions.')

rng = np.random.default_rng(41018)
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1., -1.]).astype(complex)

def herm(d):
    a = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d))
    a = (a+a.conj().T)/2
    return a/np.linalg.norm(a, 2)

def vec(a): return a.reshape(-1, order='F')
def mat(a, d): return a.reshape((d, d), order='F')
def comm(a, b): return a@b-b@a
def norm1(a): return float(np.linalg.svd(a, compute_uv=False).sum())

def entropy(r):
    vals = np.linalg.eigvalsh((r+r.conj().T)/2)
    vals = vals[vals > 1e-14]
    return float(-np.dot(vals, np.log(vals)))

def binary_entropy(x):
    return sum(-v*np.log(v) for v in [x, 1-x] if v > 0)

def dissipator(h):
    d = len(h)
    return np.kron(h.conj(), h)-.5*(np.kron(np.eye(d), h@h)+np.kron((h@h).T, np.eye(d)))

def derivative(h, e):
    d = len(h)
    a = h@e+e@h
    return np.kron(e.conj(), h)+np.kron(h.conj(), e)-.5*(np.kron(np.eye(d), a)+np.kron(a.T, np.eye(d)))

def reset_super(b, reference=1):
    tau = (I+b*Z)/2
    ks = []
    for a, c in product(range(2), repeat=2):
        k = np.zeros((2, 2), complex)
        k[a, c] = np.sqrt(tau[a, a].real)
        ks.append(np.kron(k, np.eye(reference)))
    return sum(np.kron(k.conj(), k) for k in ks)

out = {'description': 'Finite consistency checks; analytical proofs are in science/.',
       'controlled_variance': [], 'mixed_reset': [], 'local_spin': []}

# Two noise intervals and a nonunital common reset, with an untouched reference.
for b in [.65, .98]:
    d, ref, dim = 2, 2, 4
    weights = np.array([.2, .3, .5])
    durations = [.4, .7]
    hs = [[np.kron(herm(d), I) for _ in weights] for _ in durations]
    es = [[np.kron(herm(d), I) for _ in weights] for _ in durations]
    ell, dell = [], []
    for hlist, elist in zip(hs, es):
        k = np.kron(.31*herm(d), I)
        ell.append(sum(w*dissipator(h) for w, h in zip(weights, hlist))
                   -1j*(np.kron(np.eye(dim), k)-np.kron(k.T, np.eye(dim))))
        dell.append(sum(w*derivative(h, e) for w, h, e in zip(weights, hlist, elist)))
    evolution = [expm(t*l) for t, l in zip(durations, ell)]
    devolution = [expm_frechet(t*l, t*dl, compute_expm=False)
                  for t, l, dl in zip(durations, ell, dell)]
    control = reset_super(b, ref)
    total = evolution[1]@control@evolution[0]
    dtotal = devolution[1]@control@evolution[0]+evolution[1]@control@devolution[0]
    a = rng.normal(size=(dim, dim))+1j*rng.normal(size=(dim, dim))
    rho = a@a.conj().T+2*np.eye(dim)
    rho /= np.trace(rho)
    obs = herm(dim)
    before = mat(evolution[0]@vec(rho), dim)
    after = mat(control@vec(before), dim)
    final = mat(evolution[1]@vec(after), dim)
    obs_after = mat(evolution[1].conj().T@vec(obs), dim)
    obs_before = mat(control.conj().T@vec(obs_after), dim)
    obs_initial = mat(total.conj().T@vec(obs), dim)
    variance_jump = float((np.trace(after@obs_after@obs_after)-np.trace(before@obs_before@obs_before)).real)
    variance_total = float((np.trace(final@obs@obs)-np.trace(rho@obs_initial@obs_initial)).real)
    entropy_noise = entropy(before)-entropy(rho)+entropy(final)-entropy(after)
    entropy_control = entropy(before)-entropy(after)
    capacity = np.log(2)-binary_entropy((1+b)/2)
    sums = np.zeros(5)
    nodes, qweights = leggauss(80)
    for index, (t, l, hlist, elist) in enumerate(zip(durations, ell, hs, es)):
        start = rho if index == 0 else after
        last_obs = obs_before if index == 0 else obs
        for z, wq in zip(nodes, qweights):
            s = t*(z+1)/2
            rs = mat(expm(s*l)@vec(start), dim)
            os = mat(expm((t-s)*l.conj().T)@vec(last_obs), dim)
            logs = logm(rs)
            first = second = energy = sigma = comm_sq = 0.
            for w, h, e in zip(weights, hlist, elist):
                hr, er, ho = comm(h, rs), comm(e, rs), comm(h, os)
                first += float((-.5*w*np.trace(os@comm(e, hr))).real)
                second += float((-.5*w*np.trace(os@comm(h, er))).real)
                energy += float((w*np.trace(rs@ho.conj().T@ho)).real)
                sig = float((-np.trace(mat(dissipator(h)@vec(rs), dim)@logs)).real)
                sigma += w*sig
                comm_sq += w*norm1(hr)**2
                assert norm1(hr)**2 <= 2*sig+1e-10
            sums += wq*t/2*np.array([first+second, energy, sigma, comm_sq, abs(first)+abs(second)])
    exact_deriv = float(np.trace(obs@mat(dtotal@vec(rho), dim)).real)
    lam_sq = sum(t*sum(w*np.linalg.norm(e, 2)**2 for w, e in zip(weights, elist))
                 for t, elist in zip(durations, es))
    bound = np.sqrt(lam_sq)*(1+np.sqrt(4*np.log(d)+2*capacity))
    assert variance_jump >= -1e-10
    assert entropy_control <= capacity+1e-10
    assert entropy_noise <= 2*np.log(d)+capacity+1e-10
    assert abs(sums[0]-exact_deriv) < 1e-8
    assert abs(sums[1]+variance_jump-variance_total) < 1e-8
    assert abs(sums[2]-entropy_noise) < 1e-8
    assert sums[3] <= 2*entropy_noise+1e-8
    assert sums[4] <= bound+1e-8
    out['controlled_variance'].append({
        'reset_polarization': b, 'reference_dimension': ref,
        'duhamel_error': abs(sums[0]-exact_deriv),
        'variance_identity_error': abs(sums[1]+variance_jump-variance_total),
        'variance_control_jump': variance_jump,
        'entropy_identity_error': abs(sums[2]-entropy_noise),
        'actual_entropy_decrease': entropy_control, 'control_capacity': capacity})

# Verify the actual two-qubit circuit, including a mixed replacement channel.
p = (1-np.exp(-2))/2
plus = np.array([1, 1], complex)/np.sqrt(2)
plus_rho = np.outer(plus, plus.conj())
cnot = np.zeros((4, 4), complex)
for s, l in product(range(2), repeat=2): cnot[2*(s^l)+l, 2*s+l] = 1
max_circuit_error = 0.
for b, count, theta in product([0., .15, .6, 1.], [1, 3, 7], [0., .09, .5]):
    tau = (I+b*Z)/2
    u = np.cos(theta)*np.kron(X, I)-np.sin(theta)*np.kron(Y, Z)
    assert np.linalg.norm(u.conj().T-u) < 1e-12
    assert np.linalg.norm(u@u-np.eye(4)) < 1e-12
    local = np.kron(np.cos(theta)*X-np.sin(theta)*Y, I)
    assert np.linalg.norm(cnot@local@cnot-u) < 1e-12
    rho = np.kron(tau, plus_rho)
    reset = reset_super(b, 2)
    for _ in range(count): rho = mat(reset@vec((1-p)*rho+p*u@rho@u), 4)
    f = 1-p+p*np.cos(2*theta)-1j*p*b*np.sin(2*theta)
    logical = np.array([[1, f**count], [np.conj(f)**count, 1]], complex)/2
    err = np.linalg.norm(rho-np.kron(tau, logical))
    max_circuit_error = max(max_circuit_error, float(err))
    assert err < 1e-10
out['mixed_reset_circuit_max_error'] = max_circuit_error
for count in [1, 4, 16, 64, 1000]:
    for b in sorted(set([1/np.sqrt(count), .5, 1.])):
        if count*b*b < 1-1e-12: continue
        theta = 1/(2*count*b)
        f = 1-p+p*np.cos(2*theta)-1j*p*b*np.sin(2*theta)
        distance = abs(f**count-1)
        e = np.log(2)-binary_entropy((1+b)/2)
        e_after = np.log(2)-binary_entropy((1+np.exp(-2)*b)/2)
        removed = count*(e-e_after)
        assert distance > .084
        assert b*b/2-1e-12 <= e <= np.log(2)*b*b+1e-12
        assert (1-np.exp(-4))*count*e-1e-10 <= removed <= count*e+1e-10
        out['mixed_reset'].append({'cycles': count, 'polarization': b, 'angle': theta,
                                   'trace_distance': float(distance), 'budget': count*e,
                                   'actual_entropy_removed_at_zero': removed})

# Direct finite local-spin mixtures verify the GHZ formula and entropy equality.
yp = np.array([1, 1j], complex)/np.sqrt(2)
ym = np.array([1, -1j], complex)/np.sqrt(2)
def tensor(factors):
    value = np.array([1.], complex)
    for f in factors: value = np.kron(value, f)
    return value
for n in range(1, 7):
    psi = (tensor([yp]*n)+1j*tensor([ym]*n))/np.sqrt(2)
    obs = tensor([Z]*n)
    for tau in [.3, 1.]:
        r = (1-np.exp(-2*tau))/2
        theta = 1/(2*n)
        rho, rho_zero = np.zeros((2**n, 2**n), complex), np.zeros((2**n, 2**n), complex)
        for bits in product([0, 1], repeat=n):
            k = sum(bits)
            prob = r**k*(1-r)**(n-k)
            v = tensor([np.cos(theta)*Z+np.sin(theta)*X if bit else I for bit in bits])@psi
            v0 = tensor([Z if bit else I for bit in bits])@psi
            rho += prob*np.outer(v, v.conj())
            rho_zero += prob*np.outer(v0, v0.conj())
        exact = np.imag((1-r+r*np.exp(2j*theta))**n)
        measured = float(np.trace(obs@rho).real)
        ent = entropy(rho_zero)
        assert abs(measured-exact) < 1e-10
        assert abs(ent-n*binary_entropy(r)) < 1e-10
        if tau == 1: assert measured > .36
        out['local_spin'].append({'qubits': n, 'local_time': tau,
                                 'readout_error': abs(measured-exact),
                                 'entropy_error': abs(ent-n*binary_entropy(r)),
                                 'readout': measured})

if args.output is not None:
    args.output.write_text(json.dumps(out, indent=2)+'\n')

print('PASS: controlled entropy/Duhamel/variance with reference, exact two-qubit mixed resets, and local-spin GHZ/entropy identities.')
print(f"Controlled protocols: {len(out['controlled_variance'])}; mixed-reset parameter points: {len(out['mixed_reset'])}; local-spin points: {len(out['local_spin'])}.")
print(f"Maximum two-qubit circuit residual: {out['mixed_reset_circuit_max_error']:.3e}.")
print('These finite calculations do not replace the analytical proofs.')
if args.output is not None:
    print(f'Saved numerical results to {args.output}.')
