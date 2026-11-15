# Motherland

[English](README.md)｜中文

全部仓库的文档与工程基准。管五件事：文档怎么建、怎么写、怎么改和删、怎么判断齐不齐，以及一个模块用什么语言写。

读者主要是 agent（动笔改文档的那个），其次是半年后回来的人。这决定了几件事：agent 按文件名和关键词检索，不顺着目录走；它只读抓到的那一段，读不到你没写的那句；它会原样复制文档里的端口号、路径和默认值，而且不会核验。所以每条判据都要能当场判定，每份模板都要能直接抄。

## 把这段话发给你的 AI

让你的 AI 按这套规范整理你的仓库文档，把下面这段话发给它就行：

```text
请阅读 Motherland 仓库：https://github.com/Tanramisu/Motherland ，用它的判据检查我名下所有仓库的文档：缺的补上、过时的改掉、重复的合并，需要改的直接改，不用先出方案等我批准。改完逐个仓库向我汇报改了什么。

最后问我：要不要设一个每 24 小时运行一次的定时任务，按 Motherland 的标准自动整理这些仓库的文档？
```

## 多个仓库怎么共用这一份

**登记。** 采用本规范的仓库在自己的 `docs/README.md` 顶部写一行指向这里，并列出本仓偏离的地方和原因。没有登记就不算例外，算漂移。

**传播。** 改判据的人负责把改动推到已登记的仓库。没登记的仓库不在这一轮的范围内。一次改动只推自己那一层：判据、模板、示例分开走，不顺手重构别人的文档。

**优先级。** 判据 > 模板 > 示例。判据改了，模板同批跟上；示例可以晚一步，因为它只是示意。

这一节是按几个仓库的实际运行写的判断，没有对照实验支撑。

## 七条主判据

- **只写代码和提交历史重建不出来的东西**——为什么这样设计、否决了什么、哪些操作会静默出错、行业里的真实约束；会被代码证伪的字面量（端口、默认值、版本号、路径清单）换成指向真源的一跳，除非这一页就是它的 owner，因为文档里的值过期时，agent 会抄走过期那个并且很自信（预注册实验，[surface-bench](https://github.com/Connorrmcd6/surface-bench/blob/main/PAPER.md)）。判法是 [`docs/what-good-means.md`](docs/what-good-means.md) 开头的删句测试。
- **一个事实只有一个家。** 全文见 [`docs/what-good-means.md`](docs/what-good-means.md#系统级九条) 系统级第 4 条。
- **类型不混。** 全文见 [`docs/what-good-means.md`](docs/what-good-means.md#系统级九条) 系统级第 3 条。
- **先说它是什么。** 全文见 [`docs/what-good-means.md`](docs/what-good-means.md#否定不能当定义)。
- **过时的直接改，被取代的直接删。** 全文见 [`docs/lifecycle.md`](docs/lifecycle.md#三条规则)。
- **齐不齐，拿清单对账。** 全文见 [`docs/what-good-means.md`](docs/what-good-means.md#系统级九条) 系统级第 8 条。
- **读者能到。** 全文见 [`docs/what-good-means.md`](docs/what-good-means.md#系统级九条) 系统级第 1、9 条。

完整判据与坏味道清单在 [`docs/what-good-means.md`](docs/what-good-means.md)。

## 从头建一个仓库的文档

1. 判定原型：[`docs/archetypes.md`](docs/archetypes.md) 的八种，决定这个仓库要建哪些目录。
2. 建骨架：[`docs/structure.md`](docs/structure.md) 的默认骨架，删掉用不上的板块。入口随骨架一起写：根 `README.md` 一条链接指向 `docs/README.md`；`docs/README.md` 分定向层与板块，每个板块一个 hub，给路径不给全量清单。
3. 逐篇定类型：[`docs/doc-types.md`](docs/doc-types.md) 的十种，每篇只做一件事。
4. 逐句判：按 [`docs/what-good-means.md`](docs/what-good-means.md) 的删句测试逐句过——删掉这句，读者会失去什么。再对账：按第 8 条列应有清单，逐项标已覆盖、半覆盖、缺失，按第 9 条查有没有零入链的页。
5. 落笔：[`docs/writing.md`](docs/writing.md)。系统还没建成时先写蓝图，按 [`docs/blueprint.md`](docs/blueprint.md) 的四段加法写。
6. 处理旧文档：按 [`docs/lifecycle.md`](docs/lifecycle.md)，过时的改，被取代的删。机械能查的先跑一遍：`python scripts/check-doc-links.py` 按 `REPOS.md` 的本地 checkout 扫各仓根入口文件与 `docs/`，报出指向空处的相对链接，以及写成 `D:/...` 本机绝对路径的链接目标——后者在本机打得开，克隆之后必然落空。这个脚本查的是登记表里各仓的本地 checkout，本仓不在登记表内，自己的链接不在它的检查范围内。

## 模板

| 要写什么 | 抄哪份 |
|---|---|
| 仓库首页 | [`README.template.md`](templates/README.template.md) |
| 给 agent 的运行约定 | [`AGENTS.template.md`](templates/AGENTS.template.md) |
| `docs/` 的索引页 | [`index.template.md`](templates/index.template.md) |
| 一块不熟悉的代码从哪读起 | [`CODEMAP.template.md`](templates/CODEMAP.template.md) |
| 系统最终要长成什么样 | [`blueprint.template.md`](templates/blueprint.template.md) |
| 系统或模块现在是什么样（类型 4 当前实现） | [`reference.template.md`](templates/reference.template.md) |
| 一件事怎么操作 | [`how-to.template.md`](templates/how-to.template.md) |
| 一个故障怎么恢复 | [`runbook.template.md`](templates/runbook.template.md) |
| 一个决定为什么这么定 | [`decision.template.md`](templates/decision.template.md) |
| 一个行业的规则与术语 | [`domain.template.md`](templates/domain.template.md) |
| 一次复盘、事故、里程碑 | [`record.template.md`](templates/record.template.md) |

每份模板开头的注释写了读者是谁、什么该有、什么该删。抄的时候把注释一起删掉，只留骨架。

## 规范

| 遇到的问题 | 读哪份 |
|---|---|
| 这内容该不该写成文档、写成哪一种 | [`docs/doc-types.md`](docs/doc-types.md) |
| 目录怎么分、文件怎么命名、多长该拆 | [`docs/structure.md`](docs/structure.md) |
| 我这个仓库要用哪套骨架 | [`docs/archetypes.md`](docs/archetypes.md) |
| 这套文档齐不齐、缺什么 | [`docs/what-good-means.md`](docs/what-good-means.md) 系统级第 8、9 条 |
| 该不该写蓝图、蓝图里放什么 | [`docs/blueprint.md`](docs/blueprint.md) |
| 这句该怎么写、路径怎么写 | [`docs/writing.md`](docs/writing.md) |
| 哪句该删、哪条信息不能删 | [`docs/what-good-means.md`](docs/what-good-means.md) |
| 旧文档该留该删 | [`docs/lifecycle.md`](docs/lifecycle.md) |
| 想看真实的好和坏 | [`docs/examples.md`](docs/examples.md) |
| agent 写代码用哪种语言、怎么写 | [`docs/language-rules.md`](docs/language-rules.md) |
| 把自用仓库公开发布 | [`docs/open-source.md`](docs/open-source.md) |

## 不管什么

- **不管各仓库文档具体写什么。** 这里给形状，内容归那个仓库。
- **不管代码结构、符号、调用关系。** 那是 `codebase-memory-mcp` 的实时状态，抄进文档第二天就过期。CODEMAP 给的是「从哪读起」，不是符号索引。
- **不做仓库索引。** 哪个仓库在哪、本地有没有 checkout，查 [`REPOS.md`](REPOS.md)。
- **不往别的仓库塞规则。** 这里的规矩只管这里。

## 凭据

发现疑似泄露的凭据，报告，不处置。改、删、移动、脱敏、轮换都不该由 agent 替人决定。
