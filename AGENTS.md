# Agent operating rules

This root `AGENTS.md` is the **unique repository-root Agent bootstrap authority** and the first repository file an Agent reads.

This repository is a small runtime artifact. [`README.md`](README.md) describes the runtime/package contract; it is product documentation, not a second Agent policy source. If a `docs/` tree is added later, its README files are navigation-only.

Keep changes narrow and reproducible. Do not add secrets, live server state, model/checkpoint payloads, or mutable experiment authority here. Scientific experiment authority remains in `mykcs/openevo-experiment`; shared-host authority remains in `mykcs/zju-server`.

This repository has no website Production role. Changes to `AGENTS.md` or repository documentation must not be wired to Vercel, Cloudflare, GitHub Pages, or another website Production trigger.


## Development direction

For repository development and CI work, read [`docs/dev/README.md`](docs/dev/README.md) and [`docs/dev/LATEST.md`](docs/dev/LATEST.md). For artifact-identity or provider changes, also read [`docs/dev/DESIGN.md`](docs/dev/DESIGN.md) and [`docs/dev/CI_PASSPORT.md`](docs/dev/CI_PASSPORT.md).

CI mode is `SPECIALIZED_CI`: hosted checks may inspect the public GHCR manifest identity but must not pull large layers, publish packages, run scientific tasks, or gain live-server authority.
