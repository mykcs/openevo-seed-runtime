# Agent documentation router

This repository owns the portable OpenEvo + WebShop + SEED runtime-image contract. It does not own model/checkpoint payloads, live-server policy, or scientific campaign authority.

## Read order

1. [`AGENTS.md`](../../AGENTS.md) — repository boundaries.
2. [`README.md`](../../README.md) — runtime/package identity and public usage contract.
3. [`../dev/README.md`](../dev/README.md) + [`../dev/LATEST.md`](../dev/LATEST.md) — current development and CI direction.
4. Executable runtime/CI configuration plus live GHCR/GitHub state for identity or release claims.

## Cross-repository boundaries

- `mykcs/openevo-experiment` owns experiment science, results, and claims.
- `mykcs/zju-server` owns shared-host/live-server policy.
- This repository owns reproducible runtime definitions and their specialized validation.

Use the project CI passport and executable validator for exact commands; do not turn this router into a second CI contract. Read Dev archive only for replaced directions.

Shared development lifecycle: [`DEV_PROTOCOL.md`](https://github.com/mykcs/.agents/blob/main/docs/agents/DEV_PROTOCOL.md).
