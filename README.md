# OpenEvo SEED Runtime / 运行环境镜像

> 中文在前，English follows.

## 中文说明

这是 OpenEvo + WebShop + SEED 的**实验运行环境镜像**，用于复现依赖、Python
环境和工具链。它**不包含基础模型权重、LoRA checkpoint、WebShop 数据集、轨迹、
W&B 日志或任何密钥**；模型与 checkpoint 应在运行时从各自的公开来源下载或挂载。

当前公开版本是探索性实验快照，并不代表方法已经取得成功。对应的 H1.36 LoRA
checkpoint 和完整实验说明在
[Hugging Face](https://huggingface.co/miyuki17/openevo-h136-qwen25-7b-webshop-lora)。

### 什么时候用

- 需要与该实验一致的运行环境时拉取；不要把它当作模型 checkpoint。
- 本镜像约 10.29 GB，最大单层约 6.82 GB；服务器上已有同层时不会重复占用整份空间。
- 需要稳定复现时请固定到 digest，而不是只使用可变 tag。

### 拉取

```bash
# 可读版本号（适合日常使用）
docker pull ghcr.io/mykcs/openevo-seed-runtime:2026.08.18-h136

# 固定内容（适合复现）
docker pull ghcr.io/mykcs/openevo-seed-runtime@sha256:0144b2a3b5856a08f7e2d92fc9ab937580549d78c6d8bdd46705edf45fc4412a
```

### 维护约定

新版本使用日期和实验标识作为 tag；只在运行环境有实质变化时发布。模型权重和
checkpoint 放 Hugging Face，代码保留在受控 GitHub 仓库，服务器只保留正在使用或
短期验证所需的版本。

## English

This is an **experimental runtime image** for OpenEvo, WebShop, and SEED. It
packages the dependency, Python, and tooling environment; it does **not**
contain base-model weights, LoRA checkpoints, WebShop data, trajectories,
W&B logs, or credentials. Fetch or mount model assets at runtime.

The current public tag is an exploratory research snapshot, not a claim of
method success. The H1.36 LoRA checkpoint and experiment notes are available
on [Hugging Face](https://huggingface.co/miyuki17/openevo-h136-qwen25-7b-webshop-lora).

For reproducibility, pin the digest shown above. New tags are published only
when the runtime changes materially; checkpoints belong on Hugging Face and
source code remains in its controlled GitHub repository.

## Metadata

| Field | Value |
| --- | --- |
| Image | `ghcr.io/mykcs/openevo-seed-runtime` |
| Tag | `2026.08.18-h136` |
| Digest | `sha256:0144b2a3b5856a08f7e2d92fc9ab937580549d78c6d8bdd46705edf45fc4412a` |
| Visibility | Public |
| Published | 2026-08-18 |
