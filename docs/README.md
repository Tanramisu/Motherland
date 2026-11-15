# 规范

这套规范按顺序用：先判这个仓库属于哪种原型，再定目录结构，再逐篇定类型，再拿判据逐句判该留该改，再落笔，最后处理旧文档的改与删。另外四份是参照：蓝图决定目标形态，实例给出真实的好与坏，语言决定一个模块用什么写，出版决定一个自用仓库公开时要改成什么样。

| 层 | 文件 | 解决的问题 |
|---|---|---|
| 判据 | [`what-good-means.md`](what-good-means.md) | 什么算好，哪些句子一定有问题 |
| 类型 | [`doc-types.md`](doc-types.md) | 十种文档各写什么、写多长、放哪 |
| 结构 | [`structure.md`](structure.md) | 目录骨架、命名、什么时候拆、索引 |
| 原型 | [`archetypes.md`](archetypes.md) | 这个仓库该建哪些板块 |
| 落笔 | [`writing.md`](writing.md) | 句子怎么写，路径怎么写成链接 |
| 蓝图 | [`blueprint.md`](blueprint.md) | 目标形态、验收判据、差距表 |
| 生死 | [`lifecycle.md`](lifecycle.md) | 旧文档什么时候改、什么时候删 |
| 实例 | [`examples.md`](examples.md) | 真实仓库里的好与坏 |
| 编程语言 | [`language-rules.md`](language-rules.md) | agent 写代码用哪种语言、怎么写；只约束 agent，不约束人 |
| 出版 | [`open-source.md`](open-source.md) | 自用仓库公开给陌生人时，内容、历史、元数据和文档要改成什么样 |

## 用法

改一个仓库的文档，顺序是：

1. 读那个仓库的根 `README.md` 和 `AGENTS.md`，确认它自己的规则。
2. 用 [`archetypes.md`](archetypes.md) 判定它属于哪种原型，确定要建哪些目录。
3. 用 [`structure.md`](structure.md) 的「读者怎么到」定三层：哪些进定向层、每个板块的 hub 收什么、哪些只是细节。
4. 用 [`doc-types.md`](doc-types.md) 逐篇判定类型：放错目录的先搬，类型混在一起先拆。
5. 用 [`what-good-means.md`](what-good-means.md) 逐句判：删掉这句读者会失去什么。
6. 用 [`writing.md`](writing.md) 落笔，用 [`lifecycle.md`](lifecycle.md) 处理旧文档。
7. 改完扫一遍链接，跑一次真实命令。

## 这套规范自己的维护规则

- 判据要能当场判定。「文档应当清晰」没法执行，「每个目录的 README 列出其中每个文件的一句话定位」可以。
- 例子来自真实仓库，带路径。编出来的例子会被当成规矩套用，然后套错。
- 同一条规范只写在一个文件里，其余位置只放链接（判据见 [`what-good-means.md`](what-good-means.md) 系统级第 4 条）。
- 加文件前先确认现有文件装不下（硬规则见 [`AGENTS.md`](../AGENTS.md)）。这套规范已经十份，没人读得完，别轻易写第十一份。两个例外：`language-rules.md` 回答的不是写文档的问题，是「这个模块该用什么写、agent 怎么写法」；`open-source.md` 回答的是把仓库公开给陌生人的问题。两个都装不进任何一份文档规范。
- 规范只定义形状，不定义任何具体仓库的内容。
