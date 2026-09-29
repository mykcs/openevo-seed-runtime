# CI Passport

Status: **active required CI — public GHCR identity qualification**

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

## Required gate

- Required context: `GHCR manifest identity` (GitHub Actions App ID `15368`).
- Main ruleset: `CI: required runtime manifest identity` (ruleset ID `24133655`), strict required checks enabled.
- The workflow runs for pull requests and manual `workflow_dispatch` only. It checks out the exact PR head SHA, has `contents: read`, uses no secrets, and cancels a superseded run in the same PR/ref group. It has no push trigger, path filter, deployment, or registry-write step.
- Do not infer a passing qualification from a green outer status alone: inspect the owning `Runtime identity CI / qualify` job and confirm the exact-candidate checkout and remote manifest validator both ran successfully.

## Verified execution evidence

- PR #2 candidate `44c56434fdb96ce2d925a0b289a50c64293f8628` passed the `GHCR manifest identity` job in [run 36464917576](https://github.com/mykcs/openevo-seed-runtime/actions/runs/36464917576/job/109072470821). The job checked out that candidate and completed `Validate README identity and public GHCR manifest` successfully; the active main ruleset made this context required before the PR was merged.
- Merged main `d26d9eb590ce6a47d2e0ba871f42fed94f3fe183` passed the manual main smoke in [run 36465515040](https://github.com/mykcs/openevo-seed-runtime/actions/runs/36465515040/job/109074490571), including the same checkout and validator steps.
- These observations establish current gate behavior for the recorded heads. Refresh ruleset, workflow, and run evidence when the owner or contract changes; do not treat these SHAs as permanent current state.

This repository has no website Production role. Keep the check limited to README/runtime identity and the public GHCR manifest; never pull image layers, publish packages, run scientific work, or add live-server authority. The current workflow evidence reveals no reason for further CI optimization or provider migration; resource cost and quota were not assessed here.
