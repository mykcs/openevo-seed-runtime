# Agent operating rules

This root `AGENTS.md` is the **unique repository-root Agent bootstrap authority** and the first repository file an Agent reads.

This repository is a small runtime artifact. [`README.md`](README.md) describes the runtime/package contract; it is product documentation, not a second Agent policy source. If a `docs/` tree is added later, its README files are navigation-only.

Keep changes narrow and reproducible. Do not add secrets, live server state, model/checkpoint payloads, or mutable experiment authority here. Scientific experiment authority remains in `mykcs/openevo-experiment`; shared-host authority remains in `mykcs/zju-server`.

This repository has no website Production role. Changes to `AGENTS.md` or repository documentation must not be wired to Vercel, Cloudflare, GitHub Pages, or another website Production trigger.
