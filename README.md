<div align="center">

![AgentSeed](./pic/image.png)

# AgentSeed —— 从零开始的Agent开发教程

> 播下一颗种子，期待它长成参天大树的那天。

</div>

AgentSeed 是一个从零开始构建 AI Agent 的渐进式教学项目。

项目以 Python 为主，不直接依赖 LangChain 等 Agent Framework，而是从一次最基础的 LLM 调用出发，逐步实现上下文、工具调用、Agent Loop、存储、检索、Skill、MCP、可观测性与评测。

## 为什么做 AgentSeed

AI 正在从单纯的聊天工具，转向能够理解目标、使用工具并完成任务的智能助手。

一个 Agent 可以简单理解为：

```text
Agent = 大语言模型（LLM）+ 上下文（Context）+ 工具（Tools）
```

- **LLM** 负责理解问题、推理并作出决策；
- **Context** 为模型提供完成当前任务所需的信息；
- **Tools** 让模型能够搜索、计算、读写文件并调用外部服务。

但在实际学习中，LLM、Tool Use、Agent Loop、RAG、Skill 和 MCP 等概念经常同时出现，让人难以看清它们之间的关系。

AgentSeed 希望提供一条清晰的学习路径：不从庞大的框架开始，而是从可以运行的最小代码开始。每次只引入一个主要概念，观察它解决了什么问题，再让这些能力逐步生长为一个完整的 Agent。

## 项目特点

- **从底层机制开始**：直接理解 HTTP、JSON、Message、Tool Call 和 Agent Loop。
- **渐进式实现**：项目能力通过连续的 Git commit 逐步演进。
- **每步都可运行**：切换到关键提交后，可以观察该阶段新增的能力。
- **先实践，再抽象**：抽象从已经运行的代码中产生，而不是提前设计复杂框架。
- **覆盖完整链路**：从命令行模型调用，逐步扩展到 Web、RAG、Skill、MCP 和 Eval。
- **使用 Anthropic 示例**：当前代码和教程统一以 Anthropic Messages API 为例。

## 如何学习

本项目以 Git commit 作为学习和推进单位。每个关键提交都会回答四个问题：

1. 这一阶段要解决什么问题？
2. 为什么需要引入这个概念？
3. 它在代码中是如何实现的？
4. 运行后可以观察到什么新能力？

你可以跟随主分支持续阅读，也可以切换到某个提交，查看 Agent 是如何一步步构建出来的。

### 第一章：LLM 对话 （Doing）

从一次普通的 HTTP 请求开始，理解应用如何与大语言模型通信。

主要内容：

- 调用 Anthropic Messages API 兼容接口；
- 理解 System、User、Assistant 消息角色；
- 保存消息并实现上下文记忆；
- 抽象模型客户端；
- 实现流式输出；
- 使用 FastAPI 和 React 构建 Web ChatBox。

本章的目标是建立完整的模型通信基础，并理解：

> LLM 的输入是一组有角色、有顺序的消息；所谓对话记忆，本质上是应用对上下文的保存与再次发送。

### 第二章：Agent 核心能力（TODO）

在模型对话的基础上，引入 Agent 的三类核心能力：执行、存储与检索。

#### 执行（Action）

- 定义并调用 Tool；
- 实现“模型决策 → 工具执行 → 结果反馈”的 Agent Loop；
- 使用 Human-in-the-loop 审批关键操作。

#### 存储（Storage）

- 持久化保存会话和运行数据；
- 使用检查点恢复被暂停或中断的 Agent。

#### 检索（Retrieval）

- 从线性遍历和关键词检索开始；
- 逐步引入全文索引与向量索引；
- 使用 RAG 将外部知识注入模型上下文。

本章的目标是让模型从“生成回答”走向“采取行动并使用外部知识”。

### 第三章：格式转换与可观测性（TODO）

让 Agent 的输入、输出和执行过程更加可靠、清晰和可追踪。

主要内容：

- 使用 Schema 约束结构化输出；
- 记录模型调用、工具执行和停止原因；
- 保存并查看完整的 Agent 运行轨迹。

本章的目标是解决两个问题：Agent 输出能否被程序稳定使用，以及一次任务失败后能否看清发生了什么。

### 第四章：Skill 技能系统（TODO）

让 Agent 根据任务按需发现和使用可复用的技能说明。

主要内容：

- 从文件系统发现并激活 Skill；
- 按需加载 Skill 指令和资源；
- 使用 Skill 编排多步骤任务；
- 复用已有的 Agent Loop、Tools 和结构化输出能力。

本章的目标是让 Agent 从通用执行器进一步发展为能够按任务加载专业工作方法的系统。

### 第五章：MCP 协议接入（TODO）

通过 Model Context Protocol 将 Agent 与外部能力连接起来。

主要内容：

- 管理 MCP Server 的生命周期；
- 发现并调用 MCP Tool；
- 连接多个受信任的 MCP Server；
- 将 MCP Resource 和 Prompt 加入上下文。

本章的目标是理解 MCP 如何为模型与外部工具、资源和提示词提供统一的连接方式。


## 阶段产物

| 阶段 | 主题 | 阶段产物 |
| --- | --- | --- |
| 1 | LLM 对话 | 支持消息角色、上下文和流式响应的 CLI 与 Web ChatBox |
| 2 | Agent 核心能力 | 支持 Tool、人工审批、持久化、恢复和 RAG 的 Agent |
| 3 | 格式与可观测性 | 结构化输出与可查看的 Agent Trace |
| 4 | Skill 技能系统 | 支持技能发现与多步骤任务的 Skill Agent |
| 5 | MCP 协议 | 支持 Tools、Resources、Prompts 和多服务路由的 MCP Agent |
## 项目原则

- 使用渐进式单项目，让能力在前一个提交的基础上自然演进；
- 每个关键提交聚焦一个主要概念和一项可观察的新能力；
- 不使用大型 Agent Framework 隐藏关键机制；
- 先理解模型通信和 Agent 原理，再逐步完成工程抽象；
- 不为尚未出现的问题提前引入复杂设计；
- 不提交 API Key 或其他敏感信息。

## 最终目标

AgentSeed 最终会形成一个完整但最小的 AI Agent 参考实现：它能够与模型对话、维护上下文、调用工具、等待人工审批、保存与恢复状态、检索外部知识、加载 Skill、连接 MCP Server，并通过 Trace 和 Eval 观察与验证自己的执行过程。

更重要的是，项目会完整保留它从一颗种子逐步生长起来的过程。


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Nick-Hogo/AgentSeed&type=date&legend=top-left)](https://www.star-history.com/#Nick-Hogo/AgentSeed&type=date&legend=top-left)


## 相关链接

- [Linux.do](https://linux.do/)：连接开发者与 AI 爱好者的社区。
- [AgentSeed GitHub](https://github.com/Nick-Hogo/AgentSeed)：项目源码与教程。