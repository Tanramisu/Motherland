# 编程语言规则

**这是给 agent 写代码用的标准，服务对象是 vibe coding：人定方向、看结果，代码由 agent 写。** 所以这里没有「照顾人的习惯」的条款：团队熟悉度、代码审查方便、按人力算的重构成本，全部不进账。判据只有一个——agent 用哪种语言更快写出对的代码。

## 一、先问这个对象现在存不存在

**新写的东西**：按第二节和第三节选。
**已经在的东西**：第三方库、上游拷贝、厂商 SDK、别人维护的仓库——**继承原语言，不改写**。判据只有一个：这段代码将来要不要跟着上游走。要跟，换语言等于放弃合并，省下的阅读方便不值这个价。

这条优先于下面所有条款。

## 二、先看这东西在哪跑

不是先选语言，是先看它要在哪活。

**要进主进程**——跟着现有代码一起跑、被别的模块 import、挂在 Web 前端——就是主进程现有的语言（本文的基线是 TypeScript）。理由不是 TS 更好，是环境已经是 TS：跨进程要多付三份代价（数据序列化、错误跨边界翻译、启动顺序协调），为了一点语法方便付这三份不值。

**不在进程里、跑完就走的东西**，走第三节。

## 三、跑完就走的东西，Python

小脚本、数据处理、调现成的库、试一个想法——这些用 Python。

三件事它赢：

- 库现成。数值、图像、音频、文档解析、模型调用，装一个包就有。
- 改一行就能跑。不用编译、不用配工程、不用等类型检查。
- 出错直接指到那一行。

**判据是这东西的寿命和归属**：寿命短、不进生产链路、不跟别人共享接口的，用 Python。要长期留在主系统里、被别人调用、跟现有代码同一个进程的，用 TypeScript。

## 四、判据是「方便 agent 写代码」，不是别的

同一个选择，agent 和人算的账不一样。按这个排：

- **错误暴露得早不早。** 编译器当场能报的，胜过测试跑一遍才报，胜过运行时才炸。
- **形状能不能写下来。** 类型、schema、dataclass——能把「长什么样」写成机器可检查的东西，agent 就不用记住它。
- **改一次要跑几步。** 改完直接能跑最好；省一步就少一次「我改完了但其实没生效」。
- **别人踩过的坑写没写下来。** 报错信息清不清楚、文档全不全，直接决定 agent 要试几轮。

按人头算的重构成本、语言统一带来的阅读方便、团队熟悉度、代码审查的成本——**这些都不进账**。这个仓库的代码只给 agent 写、agent 读，唯一要算的是 agent 的效率和出错率。

## 五、TypeScript 怎么写

一半的规则不该写成句子，该写成开关。写在提示词里的规则要和其他所有东西争注意力，模型还会在压力下绕过去——**每条规则先问一句：这句能不能变成配置？** 能就别写。

### 配置

| 想说的 | 收到的位置 |
|---|---|
| 数组下标可能是 undefined | `noUncheckedIndexedAccess: true` |
| 不用 `any` | `@typescript-eslint/no-explicit-any` |
| 不用非空断言 | `no-non-null-assertion` |
| promise 必须等 | `no-floating-promises`（需要类型信息） |
| 用 `@ts-expect-error` 不用 `@ts-ignore` | `ban-ts-comment` |
| 别乱 cast | `consistent-type-assertions: { assertionStyle: "never" }` |
| switch 要穷尽 | `noFallthroughCasesInSwitch` + `assertNever` |
| 类型导入写 `import type` | `verbatimModuleSyntax: true` |

tsconfig 基线：

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "verbatimModuleSyntax": true,
    "erasableSyntaxOnly": true,
    "target": "ES2023",
    "module": "nodenext",
    "moduleResolution": "nodenext"
  }
}
```

把 `tsc --noEmit` 挂到每次编辑之后。改完到报错之间隔几秒，和隔一个回合，修复成本差一个量级。

### 提示词里只剩形状判断

**类型就是规格。** 外部数据（`fetch`、`JSON.parse`、数据库）是 `unknown`，用 schema 解析成类型，不写 `as`。多个可能不存在的字段换成判别联合——一个 `kind` 加几个成员，非法状态构造不出来。id 和金额用品牌类型。穷尽的 switch 以 `assertNever` 结尾。`as const` 代替 `enum`，`satisfies` 代替 `as`。

**每个禁用词后面跟一句替代动作。** 不用 `any` 用 `unknown` 再收窄；不用 `@ts-ignore` 用 `@ts-expect-error` 加理由；不用 `!` 先处理 null 分支；不写空 catch，catch 里点名错误是什么、为什么可以不管。

**收工前跑一次 typecheck，把输出贴出来。** 没跑就是没跑，不写成通过。

## 六、别的语言

- **设备固件**：C/C++。微控制器的运行时只有这个。
- **系统调用、进程隔离、性能热点**：C 或 Rust，通过原生扩展接回主进程。
- **一次性脚本**：哪个装好了用哪个，不值得为它引一个运行时。

## 七、跨语言怎么接

用接口接，不合并语言。三样里选一样并写清是哪样：**HTTP**（两边都能说、容易观察、代价是端口和进程管理）、**命令行**（最简单，但参数和输出格式要写成约定）、**消息队列**（只在真有异步解耦需求时用）。

一个仓库有两种语言是正常的。分工写进各自的 `AGENTS.md`，不在一份文件里混着解释。

## 八、每个仓库写什么

每个仓库的 `AGENTS.md` 有一节 Languages，四句话，不重复本文：

1. 主体语言是什么。
2. 这个仓库里什么东西用 Python、什么东西用 TypeScript。
3. 跑什么命令做检查和格式化。
4. 本仓库特有的坑。

**四句之后不再解释为什么**——理由在这里，`AGENTS.md` 只留结论和命令。**指引文件每一轮都进上下文，写长了只涨成本不涨表现**（数据见 [`what-good-means.md`](what-good-means.md#agentsmd-最容易写坏)）。同理不要在指引文件里重复 README 的技术栈、目录树、安装步骤。

## 一句话判据

**加一条规则之前先问：它是「能检查的」还是「要判断的」。** 能检查的进配置，要判断的进提示词，两样都不是的删掉。
