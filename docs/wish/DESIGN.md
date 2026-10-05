# Wish design — OpenEvo SEED Runtime

This repository is intentionally narrow.

- runtime/package/image definitions live here;
- scientific task/seed/budget/result authority lives in `mykcs/openevo-experiment`;
- host/GPU/storage policy lives in `mykcs/zju-server`;
- portable environment/recovery material may be coordinated with `mykcs/wangrui-server-environment`.

A good change improves reproducibility or portability without importing live host state or scientific decisions.
