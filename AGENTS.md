# AGENTS.md

这个仓库定义文档怎么建、怎么写、怎么改。动手之前读 [`README.md`](README.md)，再按下面顺序读对应规范。

## 语言

这个仓库是文档仓库，没有主体代码。语言规则本身在这里：[`docs/language-rules.md`](docs/language-rules.md)。

## 顺序

1. 判目标仓库属于哪种原型、要建哪些目录：[`docs/archetypes.md`](docs/archetypes.md)。
2. 定目录结构：[`docs/structure.md`](docs/structure.md)。
3. 判每篇东西属于哪种类型：[`docs/doc-types.md`](docs/doc-types.md) 的十种。
4. 逐句判该留该改：[`docs/what-good-means.md`](docs/what-good-means.md)。
5. 落笔：[`docs/writing.md`](docs/writing.md)。
6. 处理旧内容：[`docs/lifecycle.md`](docs/lifecycle.md)。

判据全文只在 [`docs/what-good-means.md`](docs/what-good-means.md)，这里不重复。

## 硬规则

- 本仓库是公开仓库。写进来的任何内容都会公开：不写个人或敏感信息（真实仓库清单、本机路径、凭据、私有项目的内部细节），例子保持通用化。真实登记表只留本地 `REPOS.local.md`，不进仓库。
- 直接改 `main`，不开分支。
- 加文件前先确认现有文件装不下。

## 改与删

改完检查三样，见 [`docs/what-good-means.md`](docs/what-good-means.md#改完检查三样)；删文档之前检查两件事，见 [`docs/lifecycle.md`](docs/lifecycle.md#删之前检查两件事)。
