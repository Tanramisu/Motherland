# 仓库

维护者名下所有 GitHub 仓库在这张表里各出现一次。本地有没有 checkout 是独立的事：没有 checkout 的仓库照样属于这张表，走 GitHub 读。

本文件同时是格式示例：仓库名与路径均为虚构。采用者用自己的真实清单替换本表。真实清单是本机拓扑，公开仓库里只放示例，真实表在本地维护、不进公开版本。

## DESKTOP 本地 checkout

| 仓库 | 原型 | 路径 | origin |
|---|---|---|---|
| atlas | A 平台 / harness | `D:\Projects\atlas` | example/atlas |
| ops | B 部署与运维 | `D:\ops` | example/ops |
| shop | C 产品 / SaaS | `D:\Projects\shop` | example/shop |
| ledger | D 业务台账 | `D:\Projects\ledger` | example/ledger |
| sketches | F 设计 / 创作 | `D:\Projects\sketches` | example/sketches |
| mirror-styles | H 上游镜像 | `D:\Projects\mirror-styles` | example/mirror-styles |

原型的定义与对应骨架在 [`docs/archetypes.md`](docs/archetypes.md)。判定结果写进该仓库 `docs/README.md` 第一段。

顶层目录若是指向真身的 junction，表里写成「链接 → 真身」。改代码去真身，不要在链接目录和真身各改一份。

部署根（放各系统启动脚本与任务入口的目录）不放任何仓库的 checkout，只在表外注明它的路径与用途。

第二台机器只有哪几个 checkout，单独一段写清，并注明核对日期与核对方式；在另一台机器上没法复核的，照实写「未复核」。

## 改这张表

加仓库或挪 checkout 时，先验证真实 worktree 和 `origin`，再改表。验证过的路径和猜出来的路径长得一样，只有验证过才能写进来。

## 归档

已归档的仓库在本节列名即可。只作历史，不算活跃 owner，文档不更新。
