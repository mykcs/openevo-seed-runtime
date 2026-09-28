# Current development direction

CI mode: **SPECIALIZED_CI**

The repository publishes the identity of a reproducible OpenEvo/WebShop/SEED runtime already stored in public GHCR.

The repository-owned offline check is:

```bash
python3 scripts/validate_runtime_identity.py
```

Hosted CI adds one external fact:

```bash
python3 scripts/validate_runtime_identity.py --remote
```

That command queries only the remote GHCR manifest and verifies that the readable tag still resolves to the exact digest pinned in README. It does not pull image layers, run the container, publish anything or execute scientific tasks.

Scientific claims remain owned by `mykcs/openevo-experiment`; server/runtime execution authority remains in `mykcs/zju-server`.
