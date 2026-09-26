# CI Passport

Status: **candidate — public GHCR identity qualification**

Repository: `mykcs/openevo-seed-runtime`  
Integration branch: `main`  
CI mode: `SPECIALIZED_CI`

## Contract

- offline: `python3 scripts/validate_runtime_identity.py`
- hosted: `python3 scripts/validate_runtime_identity.py --remote`
- provider: public GitHub Actions
- remote operation: manifest inspection only
- image-layer pull: forbidden/not required
- registry write: none
- secrets: none
- scientific work: none

Before making the check required, obtain an exact-head successful hosted run proving the public GHCR tag resolves to the README digest.
