#!/usr/bin/env python3
import argparse, math, re, sys

K = 2*math.pi/(8*math.log((1+5**0.5)/2))

def parse_qty(s):
    m = re.match(r"^\s*([0-9.eE+-]+)\s*(.*)\s*$", s)
    if not m: raise ValueError(f"Bad quantity: {s}")
    return float(m.group(1)), m.group(2)

parser = argparse.ArgumentParser()
parser.add_argument('--units', required=True)
parser.add_argument('--print', action='store_true')
args = parser.parse_args()

# super-minimal TOML-ish parser
vals = {}
for line in open(args.units):
    line=line.strip()
    if not line or line.startswith('#'): continue
    k,v = line.split('=',1)
    vals[k.strip()] = v.strip().strip('"')

if 'tau0' not in vals or 'ell0' not in vals:
    print('units.toml must define tau0 and ell0', file=sys.stderr)
    sys.exit(2)

_tau0,_ = parse_qty(vals['tau0'])
_ell0,_ = parse_qty(vals['ell0'])

# Invariants
ratio_tau = K
ratio_len = K

tau_rec = K*_tau0
lambda_kin = K*_ell0

if args.__dict__['print']:
    print(f"2pi/(8 ln phi) = {K:.12g}")
    print(f"tau_rec/tau0 = {ratio_tau:.12g}")
    print(f"lambda_kin/ell0 = {ratio_len:.12g}")
    print(f"tau_rec = {tau_rec:.12g} s (display)")
    print(f"lambda_kin = {lambda_kin:.12g} m (display)")

if 'lambda_rec' in vals:
    lam_rec,_ = parse_qty(vals['lambda_rec'])
    u_lam = float(vals.get('u_lambda_rec','0'))
    u_ell = 0.0
    # Combine (rho=0 default)
    u_comb = (u_lam**2 + u_ell**2)**0.5
    Z = abs(lambda_kin - lam_rec)/(u_comb*lam_rec) if u_comb>0 else float('inf')
    print(f"u_comb = {u_comb:.3g}")
    print(f"Z = {Z:.3g}")
    k = float(vals.get('k','2'))
    print(f"pass(TEST-1) = {Z <= k}")
