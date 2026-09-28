# Development and CI design

## Why this is SPECIALIZED_CI

The important invariant is artifact identity, not generic linting and not website deployment.

README exposes three linked facts:
- public GHCR image name;
- human-readable tag;
- immutable digest.

The useful failure mode is tag drift or documentation disagreement. CI therefore verifies those identities directly.

## Why CI does not rebuild

The published runtime is roughly 10 GB. Rebuilding or pulling it on every documentation PR would waste bandwidth and compute while proving a different claim.

`docker buildx imagetools inspect` reads the public registry manifest metadata without downloading image layers. That is sufficient to prove the tag-to-digest mapping.

## Authority boundary

CI must not:
- publish or mutate GHCR;
- require `packages: write`;
- download model weights or checkpoints;
- consume WebShop tasks;
- contact `lyg2171` or use GPU capacity;
- reinterpret experiment results.

The repository has no website Production role.
