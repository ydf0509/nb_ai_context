
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **此文档生成时间**：2026-06-05 20:18:37
> **系统指令**：你正在解析一份由工具 **`nb_ai_context`** 自动生成的**结构化项目快照**。
> **文档性质**：这**不是**一份普通的面向人类的文档，而是专为 AI 大模型（LLM）设计的上下文数据流。它将项目文档、源代码和 AST 架构元数据进行了特殊的结构化合并，请开启"代码解析器"的心智模式。


## 🧠 AI 认知与解析准则

这份由 `nb_ai_context` 生成的文档是你的核心知识库。其中的内容是动态的——它可能包含完整的底层源码，也可能仅包含使用教程，或者是两者的混合。请严格遵循以下自适应阅读策略：

### 1. 信息的层级与冲突处理
*   **文档即意图**：将 `README`、教程文档和 Docstrings 视为项目设计的**最高意图**。如果生成器省略了对应源码，请完全信任文档逻辑，以此为基础推理。
*   **源码即事实**：遇到 `.py` 源码或 AST 元数据（类/函数签名）时，以此作为实现细节、类型约束和语法准确性的**最终事实标准**。
*   **冲突处理**：若文档与源码/AST 存在矛盾，请以源码为准，并在回答中向用户简要指出该差异。
*   **测试代码的忽略**：为优化 Token 长度，集成/单元测试及非核心 API 源码通常被隐藏。**绝对不要**因此推断或提醒用户“项目缺乏测试”或“代码未实现”。

### 2. 文件边界与架构感知
*   **上下文定界**：工具使用 `--- **start of file: <路径>** ---` 等标记严格界定文件。**在你的回复中，请使用标准 Markdown 代码块，切勿模仿使用此类系统定界符。**
*   **结构可视化**：利用“文件树 (File Tree)”章节建立项目的宏观架构认知。
*   **依赖关系**：利用“文件依赖分析”章节理清模块间的 import 数据流向。

### 3. 严格的代码生成与交互边界
*   **事实锚定 (Fact Anchoring)**：你生成的代码必须严格锚定在本文档范围内！API 调用必须基于**源码中的 AST 签名**或**文档中的演示示例**。
*   **严禁臆造 (Zero Fabrication)**：绝对禁止编造文档中未定义或未提及的类名、方法名或参数。
*   **越界拒绝**：如果用户询问的功能在当前提供的上下文中完全不存在，请明确告知“当前上下文中未包含该信息”，而不是试图凭空生成。

---
# markdown content namespace: nb_agent project summary 



- `nb_agent` 是一个可 import 使用的 TUI Agent 框架，让用户快速开发自己的 AI Agent 项目。
- 三种扩展机制：Tools（@tool 装饰器）、MCP（外部 MCP Server）、Skills（SKILL.md 文档注入）
- 核心模块：
  - `nb_agent/core/agent.py`: AgentCore — 对话循环、工具调用、模型切换、分组管理
  - `nb_agent/tools/base.py`: @tool 装饰器 — 自动生成 OpenAI Function Calling schema，支持 group 参数
  - `nb_agent/mcp/manager.py`: MCP 管理器 — 动态连接 MCP Server、工具发现
  - `nb_agent/skills/manager.py`: SkillManager — SKILL.md 发现、加载、匹配
  - `nb_agent/tui/app.py`: TUI 界面 — 基于 Textual 的终端交互（F2 Skills / F3 工具组 / @ 补全）
  - `nb_agent/session/store.py`: 会话持久化 — SQLModel + SQLite
  - `nb_agent/approval/`: 危险操作审批机制
  - `nb_agent/config/`: 配置管理（JSONC 格式）
- 用户用法：`from nb_agent.core import AgentCore` + `from nb_agent.tools import tool`
- 支持工具分组（tool_group）：`@tool(group="file")` → `file__read_file`，TUI 中可禁用整组


## 📋 nb_agent most core source files metadata (Entry Points)


以下是项目 nb_agent 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nb_agent most core source code files as follows: 
- `nb_agent/core/agent.py`
- `nb_agent/tools/base.py`


### 📄 Python File Metadata: `nb_agent/core/agent.py`

#### 📝 Module Docstring

`````
AgentCore — ReAct 循环核心

核心循环：
  用户输入 → LLM(messages + tools) → 判断:
    有 tool_calls → 执行工具 → 结果回传 LLM → 再次判断（可能多轮）
    无 tool_calls → 返回文本回复
`````

#### 📦 Imports

- `import asyncio`
- `import functools`
- `import json`
- `import time`
- `import uuid`
- `from typing import AsyncIterator`
- `from typing import List`
- `from typing import Dict`
- `from typing import Optional`
- `from typing import Callable`
- `from openai import AsyncOpenAI`
- `from nb_agent.core.models import ModelInfo`
- `from nb_agent.core.models import ToolCallRecord`
- `from nb_agent.core.models import AgentResponse`
- `from nb_agent.core.models import load_models_from_config`
- `from nb_agent.core.context import trim_context`
- `from nb_agent.core.retry import call_llm_with_retry`
- `from nb_agent.core.retry import RETRYABLE_ERRORS`
- `from nb_agent.core.retry import MAX_RETRIES`
- `from nb_agent.session import SessionStore`
- `from nb_agent.mcp import MCPManager`
- `from nb_agent.approval import ApprovalEngine`
- `from nb_agent.tools import TOOL_REGISTRY`
- `from nb_agent.skills import SkillManager`
- `from nb_agent.utils.loggers import logger_llm_call`
- `from nb_agent.utils.loggers import logger_llm_call_raw`
- `import datetime as _dt`

#### 🏛️ Classes (1)

##### 📌 `class AgentCore`
*Line: 32*

**Docstring:**
`````
Agent 核心：
- Function Calling：LLM 自主决定是否调用工具
- 多轮工具调用：一次对话中可调用多个工具、多轮
- 通过回调实时通知 TUI 工具调用状态
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, config: dict)`
  - **Parameters:**
    - `self`
    - `config: dict`

**Public Methods (23):**
- `async def chat(self, user_input: str) -> AgentResponse`
- `async def chat_stream(self, user_input: str) -> AsyncIterator[str]`
  - *工具调用阶段用非流式（需要完整 tool_calls），最终回复用流式输出*
- `async def connect_mcp(self)`
- `async def disconnect_mcp(self)`
- `def switch_model(self, model_id: str) -> bool`
- `def get_models_grouped(self) -> Dict[str, List[ModelInfo]]`
- `async def generate_smart_title(self)`
- `def clear_history(self)`
- `def get_session_list(self, limit: int = 50) -> list`
- `def get_tools(self) -> list`
- `def get_tool_groups(self) -> list`
  - *返回所有工具分组及其状态*
- `def toggle_tool_group(self, group: str) -> bool`
  - *切换工具分组的启用/禁用状态，返回 True=已启用*
- `def get_mcp_status(self) -> list`
- `def toggle_mcp_server(self, name: str) -> bool`
- `def get_model_name(self) -> str`
- `def get_model_display_name(self) -> str`
- `def get_token_usage(self) -> dict`
- `def register_tool(self, name: str, func: Callable, description: str, parameters: dict, group: str = '')`
- `def get_agents(self) -> list`
  - *返回所有 Agent（含默认），当前使用的标记 is_current*
- `def save_agent(self, name: str, system_prompt: str, default_model: str = '', allowed_tool_groups: list = None, allowed_mcp_servers: list = None, allowed_skills: list = None) -> str`
- `def update_agent(self, agent_id: str, name: str, system_prompt: str, default_model: str = '', allowed_tool_groups: list = None, allowed_mcp_servers: list = None, allowed_skills: list = None)`
- `def delete_agent(self, agent_id: str) -> bool`
- `def apply_agent(self, agent_id: str)`
  - *应用 Agent 配置：替换 system prompt + 工具/MCP/Skills 开关 + 默认模型，新建会话*

**Class Variables (2):**
- `MAX_TOOL_ROUNDS = 30`
- `DEFAULT_AGENT_ID = '__default__'`


---




### 📄 Python File Metadata: `nb_agent/tools/base.py`

#### 📝 Module Docstring

`````
工具注册框架 — 基于 Pydantic + 装饰器自动生成 OpenAI Function Calling Schema

用法:
    from nb_agent.tools import tool

    class MyParams(BaseModel):
        query: str = Field(description="搜索关键词")

    # 无分组
    @tool
    def search(params: MyParams) -> str:
        """搜索互联网"""
        ...

    # 有分组 — 注册名变为 file__read_file
    @tool(group="file")
    def read_file(params: ReadParams) -> str:
        """读取文件"""
        ...
`````

#### 📦 Imports

- `import inspect`
- `from typing import Dict`
- `from typing import Callable`
- `from typing import Optional`
- `from typing import Type`
- `from typing import get_type_hints`
- `from pydantic import BaseModel`

#### 🔧 Public Functions (2)

- `def tool(func = None)`
  - *Line: 131*
  - **Docstring:**
  `````
  装饰器：自动注册工具函数到 TOOL_REGISTRY
  
  用法:
      @tool                          # 无分组，注册名 = func_name
      @tool(group="file")            # 有分组，注册名 = file__func_name
  `````

- `def decorator(fn)`
  - *Line: 140*


---



## 🔗 nb_agent Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ nb_agent/core/agent.py
  ★ nb_agent/tools/base.py

`````

### 📋 Detailed Dependencies

### 📦 Third-party Dependencies

项目使用的第三方库：

- `nb_agent`
- `openai`
- `pydantic`
- ......以及更多的第三方库......


---
# markdown content namespace: nb_agent Project Root Dir Some Files 


## nb_agent File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## nb_agent (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: nb_agent) --- 

`````markdown
# nb_agent

nb_agent 是一个用户能基于此快速开发agent应用的框架，能快速扩展tools mcp skills，创建agents，自带tui终端。

**手写 ReAct Agent 框架 + 赛博朋克 TUI** — 不依赖 LangChain，用纯 Python 实现 LLM ↔ Tool 循环。

nb_agent tui截图：
截图是nb-agent接入serena这个mcp，变身为ai coding工具。
自己吃自己的狗粮：自己打造nb-agent的终端 + ai coding智能体，使用deepseek-v4-flash 模型，修改nb-agent项目自身的源码，验证效果完美，一次即可改对代码。
![alt text](1c93130f53f4cca8d290198dd426926a.png)

截图是nb-agent创建的新闻agent，通过接入了open web search 这个mcp，用于搜索互联网娱乐八卦新闻：
在tui终端提问:特朗普这个月做了什么呀？效果如下图
![alt text](image.png)

## 特性

- **手写 ReAct 循环**：LLM → tool_calls → execute → feedback，无框架黑魔法
- **三种扩展方式**：Tools（Python 函数）+ MCP（外部工具协议）+ Skills（Markdown 指导手册）
- **Agent 配置**：创建多个 Agent 预设，每个可独立配置 system prompt、工具组、MCP Server、Skills 的启用范围
- **MCP 多 Server 管理**：stdio / SSE / HTTP 三种传输方式，运行时启禁，工具命名空间防冲突
- **生产级特性**：上下文裁剪、指数退避重试、危险操作审批、SQLite 会话持久化
- **赛博朋克 TUI**：流式输出 + 思考链 + 模型切换 + Token 统计 + 右侧工具面板

## 快速开始

```bash
pip install very_nb_agent   # 这里要注意是very_nb_agent，不是nb_agent，因为nb_agent 和别人的已有 nbagent名字太相似，被pypi拒绝了。
```

或者在你的项目中集成：

```python
import tools                          # 导入即注册你的自定义工具
from nb_agent import load_config, AgentApp

config = load_config()
app = AgentApp(config)
app.run()
```

## 配置

复制 `config.example.jsonc` 到工作目录，重命名为 `config.jsonc`：

```bash
cp config.example.jsonc config.jsonc
# 编辑 config.jsonc，填入你的 API Key
nb_agent
```

配置优先级：`CLI 参数 > 环境变量 > 项目级 ./config.jsonc > 全局 ~/.nb_agent/config.jsonc > 默认值`

API Key 支持 `{env:DEEPSEEK_API_KEY}` 语法从环境变量读取。

**raw_model** — 当配置的模型 key 与 API 实际要求的模型名不一致时，可通过 `raw_model` 指定真实模型名：

```jsonc
"models": {
    "ds-deepseek-v4-flash-200k": {
        "name": "DeepSeek V4 Flash (官方直连)",
        "raw_model": "deepseek-chat",
        "limit": { "context": 200000, "output": 64000 }
    }
}
```

若未设置 `raw_model`，则直接使用 key（如 `ds-deepseek-v4-flash-200k`）作为模型名请求接口。

## 三种扩展方式

### 1. Tools — Python 函数工具

用 `@tool` 装饰器 + Pydantic 参数模型，导入即自动注册：

```python
from nb_agent.tools import tool
from pydantic import BaseModel, Field

class SearchParams(BaseModel):
    query: str = Field(description="搜索关键词")

@tool(group="search")  # group 可选，用于分组管理
def web_search(params: SearchParams) -> str:
    """搜索互联网，返回相关结果"""
    # ... 你的逻辑
    return "搜索结果"
```

工具名自动生成为 `{group}__{函数名}`（如 `search__web_search`），无 group 时直接用函数名。

### 2. MCP — 外部工具协议

在 `config.jsonc` 中配置 MCP Server：

```jsonc
"mcp": {
    // 本地 stdio 方式启动自定义 MCP Server（FastMCP 编写）
    "bookmark": {
        "type": "local",
        "command": ["python", "mcp_servers/bookmark_server.py"],
        "enabled": true
    },
    // SSE 方式连接远程 MCP Server
    "web-search": {
        "type": "sse",
        "url": "http://localhost:3000/sse",
        "enabled": true
    },
    // HTTP 方式连接远程 MCP Server（streamableHttp 协议，http 是别名）
    "nbrag": {
        "type": "http",
        "url": "http://localhost:9101/mcp"
    }
}
```

支持四种传输方式：

| type | 说明 |
|------|------|
| `local`（默认） | stdio 子进程，配置 `command` + `args` |
| `sse` | SSE 协议远程连接，配置 `url` |
| `streamableHttp` | Streamable HTTP 远程连接，配置 `url` |
| `http` | `streamableHttp` 的别名，方便记忆 |

不传 `type` 默认走 `local`（stdio）。MCP 工具名自动加 `mcp__{server}__{tool}` 前缀。

### 3. Skills — Markdown 指导手册

Skills 教 AI "怎么做"某类任务。不是可执行代码，而是 Markdown 格式的操作指南。

遵循 **[Agent Skills 开放规范](https://agentskills.io)**（Anthropic 创建，Claude / OpenAI Codex / Gemini CLI / Cursor / VS Code 等 26+ 平台采用）。

**渐进式披露（Progressive Disclosure）**：
1. **Discovery** — 启动时 system prompt 只注入 name + description 清单，不浪费 token
2. **Activation** — AI 判断需要某 Skill 时，调用 `view_skill("name")` 加载完整指南
3. **Execution** — 按指南执行任务

**目录扫描**（后者覆盖前者）：

```
内置:     nb_agent/skills/builtin/ (code-review, explain-code, refactor)
全局级:   ~/.nb_agent/skills/my-skill/SKILL.md
跨平台:   ~/.agents/skills/my-skill/SKILL.md     ← 与 Codex/Gemini CLI 共享
项目级:   .nb_agent/skills/my-skill/SKILL.md
跨平台:   .agents/skills/my-skill/SKILL.md        ← 与 Codex/Gemini CLI 共享
```

**SKILL.md 格式**：

```markdown
---
name: deploy-checklist
description: >-
  部署前检查清单。当用户提到部署、发布、上线时使用。
---

# 部署检查

## 检查项
1. 所有测试通过
2. 环境变量已配置
3. 数据库迁移已执行
...
```

> 文件夹名必须与 `name` 字段一致。完整的 frontmatter 字段说明见 [agentskills.io/specification](https://agentskills.io/specification)。

## Agent 管理

Agent 是一组 "system prompt + 工具/MCP/Skills 启用范围" 的配置预设。通过 TUI 中的 **F4** 快捷键管理：

- **新建 Agent**：为不同任务创建专用预设（如 "代码审查专家"、"翻译助手"）
- **勾选控制**：每个 Agent 可独立选择启用哪些工具组、MCP Server、Skills
- **切换应用**：随时切换当前使用的 Agent，自动重置会话

启用范围采用三值语义：
- 不设置 → 全部允许（默认）
- 选择部分 → 只允许选中的
- 全部取消 → 全部禁用

## 审批引擎

可插拔的工具审批机制，防止 AI 执行危险操作：

```jsonc
// config.jsonc
{
  "approval": {
    "dangerous_tools": ["note__delete_note"],
    "auto_approve": false
  }
}
```

也可用代码注入自定义规则：

```python
def rule_redis_write(tool_name: str, tool_kwargs: dict) -> bool:
    """Redis 写命令弹窗确认，只读命令直接放行"""
    if tool_name != "mcp__redis-tools__redis_execute":
        return False
    cmd = tool_kwargs.get("command", "").strip().split()
    return cmd[0].upper() in {"SET", "DEL", "HSET"} if cmd else False

app.agent.approval_engine.add_rule(rule_redis_write)
```

## nb_log 配置

nb_agent 使用 [nb_log](https://github.com/ydf0509/nb_log) 作为日志库。TUI 模式下需要在项目根目录的 `nb_log_config.py` 中设置以下 3 项，否则 **TUI 会黑屏**：

```python
PRINT_WRTIE_FILE_NAME = None   # 禁止 nb_log 劫持 sys.stdout
SYS_STD_FILE_NAME = None       # 禁止 nb_log 劫持 sys.stdout
AUTO_PATCH_PRINT = False       # 禁止 monkey patch print
```

> Textual TUI 独占终端的 alternate screen buffer 渲染，上述三项配置会破坏渲染通道。

## CLI

```bash
nb_agent                              # 启动 TUI
nb_agent --config ./my_config.jsonc   # 指定配置
nb_agent run "帮我分析代码性能"        # 非交互模式
nb_agent sessions list                # 查看历史会话
```


## Agent 管理功能

支持创建多个 **Agent 预设**，每个 Agent 是独立的一套配置组合（System Prompt + 工具组开关 + MCP 开关 + Skills 开关 + 默认模型），让 AI 在不同场景下拥有不同的身份和能力边界。按 **F4** 管理。
从不同的agent创建会话，适应不同的场景。
例如你可以通过接入serena mcp后，专门创建一个agent，用于ai coding。
通过接入 web search mcp后，专门创建一个agent，用于搜索互联网娱乐八卦新闻。
通过接入 nbrag mcp后，专门创建一个agent，用于rag知识库检索。
不同的agent绑定不同的System Prompt + 工具组开关 + MCP 开关 + Skills 开关，可以减少无关工具暴露给ai，节约很多tokens，提高ai的决策效率。

## TUI 快捷键

| 快捷键 | 功能 |
|--------|------|
| Ctrl+J / Ctrl+Enter | 发送消息 |
| Enter | 输入框内换行 |
| Tab | 切换模型 |
| Ctrl+N | 新建会话 |
| Ctrl+R | 恢复历史会话 |
| Ctrl+K | 终止 AI 回答 |
| Ctrl+↑ | 编辑上一轮提问 |
| Ctrl+E | 展开/收起输入框 |
| Ctrl+L | 清空屏幕 |
| Ctrl+P | 命令面板 |
| F1 | 帮助 |
| F2 | Skills 列表（查看/应用） |
| F4 | Agent 管理（创建/编辑/切换） |
| Ctrl+Q | 退出 |

## 架构总览

```
用户输入 → AgentCore (ReAct Loop, max 30 轮)
             ├── Tools (@tool 装饰器注册的 Python 函数)
             ├── MCP Server (外部进程，stdio/SSE/HTTP)
             ├── Skills (view_skill → SKILL.md 指导手册)
             └── ApprovalEngine (危险操作审批)
                    ↕
              LLM API (OpenAI 兼容，按 provider 分组)
                    ↕
              流式/非流式回复 → TUI 渲染
                    ↕
              SessionStore (SQLite 会话持久化)
```

**三种扩展方式完全正交**：
- **Tools** = 可执行的 Python 函数
- **MCP** = 外部进程提供的工具（通过 stdio/SSE/HTTP 通信）
- **Skills** = Markdown 格式的指导手册（渐进式披露，省 token）

## 项目结构

```
nb_agent/
├── config/          — 配置加载 (JSONC + 环境变量)
├── core/            — ReAct 核心
│   ├── agent.py     — AgentCore 核心类
│   ├── models.py    — ModelInfo, AgentResponse 等
│   ├── context.py   — Token 估算 & 上下文裁剪
│   └── retry.py     — 指数退避重试
├── tools/           — @tool 装饰器 + 内置工具
├── mcp/             — MCP 多 Server 管理
├── skills/          — Skills 渐进式披露系统
│   ├── manager.py   — SkillManager
│   └── builtin/     — 内置 Skills (code-review, explain-code, refactor)
├── session/         — SQLModel 会话 + Agent 配置持久化
├── approval/        — 可插拔工具审批引擎
├── tui/             — Textual 赛博朋克 TUI
│   ├── app.py       — AgentApp 主类
│   ├── styles.tcss  — 样式
│   └── widgets/     — UI 组件 (输入框、工具面板、弹窗、命令面板)
└── utils/           — 日志工具
```

## 问答章节

### 1. 什么是nb_agent

ReAct Agent 框架 + 赛博朋克 TUI。不依赖 LangChain，纯 Python 实现 LLM ↔ Tool 循环，支持三种扩展方式：Python 函数工具（@tool 装饰器）、MCP 外部工具协议、Skills Markdown 指导手册(严格按照agentskills.io 规范)。`pip install very_nb_agent` 一条命令就能跑。

### 2. 用 nb_agent 有什么好处

- **零框架依赖**：没有 LangChain 黑魔法，ReAct 循环完全手写，行为可控、调试透明
- **三种正交扩展**：Tools（写代码）、MCP（接外部工具）、Skills（写 Markdown 指南），各司其职
- **生产级特性**：上下文裁剪、指数退避重试、危险操作审批引擎、SqlModel 会话持久化
- **TUI 开箱即用**：流式输出 + 思考链可视 + 模型热切换 + Token 统计 
- tool  mcp  skills 热启用(无需改配置文件或代码)
- 多agents管理(每个agent独立配置 提示词+ 工具组+ MCP Server+ Skills ，快速从不同的agent创建会话应对不同的场景)
- **接入门槛极低**：`pip install very_nb_agent && nb_agent` 即可，集成到项目只需几行代码

### 3 nb_agent 能不能作为编程助手呀？（类似claude-code opencode cline 这种终端工具）

**能。** 通过接入第三方编程 MCP，nb_agent 可以化身为终端编程助手。

**Serena** — 当前最流行的开源编程 MCP。接入后用户不需要写任何 tools 函数、不需要写任何 skills、不需要再接 filesystem / codegraph 等杂七杂八的 MCP，零代码即可让 nb_agent 拥有类似 opencode / cline / claude-code 的编程能力。

**nbrag / context7** — 文档与代码知识库 MCP，可把任意第三方框架的最新教程和源码向量化，编程时精确查找 API 用法。

在 `config.jsonc` 的 `mcp` 节配置即可：

```jsonc
"mcp": {
    // Serena（语义级编程 MCP：代码索引、符号导航、跨文件重构、智能编辑）
    // 安装: uv tool install -p 3.12 serena-agent@latest --prerelease=allow
    "serena": {
        "type": "local",
        "command": ["serena", "start-mcp-server", "--project", "D:/codes/my_project"],
        "enabled": true
    },
    // nbrag（Agentic RAG MCP：文档/代码向量化导入、多轮智能检索）
    // 安装: uv tool install nbrag  或  pip install nbrag
    // 支持 http（单独启动服务）和 local（子进程启动）两种方式
    "nbrag": {
        "type": "http",
        "url": "http://localhost:9101/mcp"
    },
    // context7（实时文档查询 MCP：查任意库的官方文档和代码示例）
    "context7": {
        "type": "local",
        "command": ["npx", "-y", "@upstash/context7-mcp@latest"],
        "enabled": false
    }
}
```

### nb_agent 支不支持 RAG 知识库 呀？

**支持。** nbrag 是一个独立的 Agentic RAG MCP Server（12 个工具），可导入代码、文档等任意文本，尤其对 Python 项目有奇效（AST 自动解析 class/function 作用域）。在 nb_agent 的 config.jsonc 中配置为 MCP Server 即可使用——MCP 暴露了工具描述和入参，AI 直接就能理解怎么用。如果想更进一步，把 `skills/nbrag-workflow/SKILL.md` 复制到 `.nb_agent/skills/nbrag-workflow/SKILL.md`，AI 会按最佳检索策略打组合拳。

nbrag作为知识库，吊打传统native知识库， 所以nb_agent支持mcp，nbrag是rag mcp，所以nb_agent 支持知识库


## License

MIT

`````

--- **end of file: README.md** (project: nb_agent) --- 

---


--- **start of file: pyproject.toml** (project: nb_agent) --- 

`````text
[project]
name = "very_nb_agent"
version = "0.2.2"
description = "Handwritten ReAct Agent with TUI — Tools + MCP + Skills，agent frame"
readme = "README.md"
license = "MIT"
requires-python = ">=3.11"
keywords = ["ai-agent", "react-agent", "function-calling", "mcp", "tui", "skills"]

dependencies = [
    "textual>=0.50.0",
    "rich>=13.0.0",
    "json5>=0.9.0",
    "openai>=1.0.0",
    "httpx>=0.24.0",
    "pydantic>=2.0.0",
    "python-dotenv>=1.0.0",
    "mcp>=1.0.0",
    "pyyaml>=6.0",
    "sqlmodel>=0.0.16",
    "nb_log",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "pytest-asyncio>=0.20"]

[project.scripts]
nb_agent = "nb_agent.main:main"

#[build-system]
#requires = ["hatchling"]
#build-backend = "hatchling.build"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project.urls]
Homepage = "https://github.com/ydf0509/nb_agent"
Repository = "https://github.com/ydf0509/nb_agent"

[tool.setuptools.packages.find]
include = ["nb_agent*"]

[tool.setuptools.package-data]
nb_agent = ["*.tcss", "**/*.tcss"]  
`````

--- **end of file: pyproject.toml** (project: nb_agent) --- 

---

# markdown content namespace: nb_agent codes 


## nb_agent File Tree (relative dir: `nb_agent`)


`````

└── nb_agent
    ├── __init__.py
    ├── __main__.py
    ├── approval
    │   ├── __init__.py
    │   └── engine.py
    ├── config
    │   ├── __init__.py
    │   └── loader.py
    ├── core
    │   ├── __init__.py
    │   ├── agent.py
    │   ├── context.py
    │   ├── models.py
    │   └── retry.py
    ├── main.py
    ├── mcp
    │   ├── __init__.py
    │   └── client.py
    ├── session
    │   ├── __init__.py
    │   ├── models.py
    │   └── store.py
    ├── skills
    │   ├── README.md
    │   ├── __init__.py
    │   └── manager.py
    ├── tools
    │   ├── __init__.py
    │   ├── base.py
    │   └── builtin.py
    ├── tui
    │   ├── __init__.py
    │   ├── app.py
    │   ├── styles.tcss
    │   └── widgets
    │       ├── __init__.py
    │       ├── commands.py
    │       ├── inputs.py
    │       ├── screens.py
    │       └── tool_panel.py
    └── utils
        └── loggers.py

`````

---


## nb_agent (relative dir: `nb_agent`)  Included Files (total: 32 files)


- `nb_agent/main.py`

- `nb_agent/__init__.py`

- `nb_agent/__main__.py`

- `nb_agent/approval/engine.py`

- `nb_agent/approval/__init__.py`

- `nb_agent/config/loader.py`

- `nb_agent/config/__init__.py`

- `nb_agent/core/agent.py`

- `nb_agent/core/context.py`

- `nb_agent/core/models.py`

- `nb_agent/core/retry.py`

- `nb_agent/core/__init__.py`

- `nb_agent/mcp/client.py`

- `nb_agent/mcp/__init__.py`

- `nb_agent/session/models.py`

- `nb_agent/session/store.py`

- `nb_agent/session/__init__.py`

- `nb_agent/skills/manager.py`

- `nb_agent/skills/README.md`

- `nb_agent/skills/__init__.py`

- `nb_agent/tools/base.py`

- `nb_agent/tools/builtin.py`

- `nb_agent/tools/__init__.py`

- `nb_agent/tui/app.py`

- `nb_agent/tui/styles.tcss`

- `nb_agent/tui/__init__.py`

- `nb_agent/tui/widgets/commands.py`

- `nb_agent/tui/widgets/inputs.py`

- `nb_agent/tui/widgets/screens.py`

- `nb_agent/tui/widgets/tool_panel.py`

- `nb_agent/tui/widgets/__init__.py`

- `nb_agent/utils/loggers.py`


---


--- **start of file: nb_agent/main.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/main.py`

#### 📝 Module Docstring

`````
nb_agent CLI 入口
`````

#### 📦 Imports

- `import argparse`
- `import os`
- `import sys`
- `from nb_agent.config import load_config`
- `import asyncio`
- `from nb_agent.core import AgentCore`
- `from nb_agent.session import SessionStore`
- `from nb_agent.tui.app import AgentApp`

#### 🔧 Public Functions (1)

- `def main()`
  - *Line: 8*


---

`````python
"""nb_agent CLI 入口"""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="nb_agent — Handwritten ReAct Agent with TUI")
    parser.add_argument("--config", "-c", help="配置文件路径 (JSONC)")
    parser.add_argument("--dotenv", help=".env 文件路径")

    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="非交互模式：执行一次对话")
    run_parser.add_argument("prompt", nargs="?", help="用户提问")
    run_parser.add_argument("-f", "--file", help="从文件读取 prompt")

    subparsers.add_parser("sessions", help="会话管理")

    args = parser.parse_args()

    from nb_agent.config import load_config
    config = load_config(
        cli_config_path=args.config or "",
        dotenv_path=args.dotenv or "",
    )
    config["_project_root"] = os.getcwd()

    if args.command == "run":
        _run_once(config, args)
    elif args.command == "sessions":
        _list_sessions(config)
    else:
        _run_tui(config)


def _run_tui(config: dict):
    try:
        from nb_agent.tui.app import AgentApp
    except ImportError:
        print("TUI 依赖未安装，请运行: pip install nb_agent[tui]")
        sys.exit(1)
    app = AgentApp(config)
    app.run()


def _run_once(config: dict, args):
    import asyncio

    prompt = args.prompt or ""
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            prompt = f.read()
    if not prompt:
        print("错误：请提供 prompt 或 -f 文件")
        sys.exit(1)

    from nb_agent.core import AgentCore

    async def _run():
        agent = AgentCore(config)
        await agent.connect_mcp()
        try:
            async for chunk in agent.chat_stream(prompt):
                print(chunk, end="", flush=True)
            print()
        finally:
            await agent.disconnect_mcp()

    asyncio.run(_run())


def _list_sessions(config: dict):
    from nb_agent.session import SessionStore
    db_path = config.get("session", {}).get("db_path", "")
    store = SessionStore(db_path)
    sessions = store.list_sessions(limit=20)
    if not sessions:
        print("暂无历史会话")
        return
    for s in sessions:
        print(f"  {s['id']}  {s['title'][:40]:<40}  {s['updated_at'][:19]}")


if __name__ == "__main__":
    main()

`````

--- **end of file: nb_agent/main.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/__init__.py`

#### 📝 Module Docstring

`````
nb_agent — Handwritten ReAct Agent with TUI
`````

#### 📦 Imports

- `from nb_agent.config import load_config`
- `from nb_agent.tui.app import AgentApp`


---

`````python
"""nb_agent — Handwritten ReAct Agent with TUI"""

__version__ = "0.1.0"

from nb_agent.config import load_config
from nb_agent.tui.app import AgentApp

__all__ = ["load_config", "AgentApp", "__version__"]

`````

--- **end of file: nb_agent/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/__main__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/__main__.py`

#### 📝 Module Docstring

`````
python -m nb_agent 入口
`````

#### 📦 Imports

- `from nb_agent.main import main`


---

`````python
"""python -m nb_agent 入口"""

from nb_agent.main import main

main()

`````

--- **end of file: nb_agent/__main__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/approval/engine.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/approval/engine.py`

#### 📝 Module Docstring

`````
工具审批规则引擎 — 判断工具调用是否需要用户确认

使用方式:
    engine = ApprovalEngine()
    engine.add_rule(my_rule_func)  # 添加自定义规则

    if engine.needs_approval("tool_name", {"arg": "value"}):
        # 弹窗让用户确认
        ...

规则函数签名: (tool_name: str, tool_kwargs: dict) -> bool
    返回 True 表示需要审批，False 表示放行。
`````

#### 📦 Imports

- `from typing import Callable`
- `from typing import List`
- `from typing import Optional`

#### 🏛️ Classes (1)

##### 📌 `class ApprovalEngine`
*Line: 18*

**Docstring:**
`````
工具审批规则引擎：可插拔规则列表，任一命中即触发审批弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, rules: Optional[List[Callable]] = None, extra_dangerous: Optional[List[str]] = None)`
  - **Parameters:**
    - `self`
    - `rules: Optional[List[Callable]] = None`
    - `extra_dangerous: Optional[List[str]] = None`

**Public Methods (3):**
- `def needs_approval(self, tool_name: str, tool_kwargs: dict) -> bool`
- `def add_rule(self, rule: Callable)`
- `def remove_rule(self, rule: Callable)`


---

`````python
"""工具审批规则引擎 — 判断工具调用是否需要用户确认

使用方式:
    engine = ApprovalEngine()
    engine.add_rule(my_rule_func)  # 添加自定义规则

    if engine.needs_approval("tool_name", {"arg": "value"}):
        # 弹窗让用户确认
        ...

规则函数签名: (tool_name: str, tool_kwargs: dict) -> bool
    返回 True 表示需要审批，False 表示放行。
"""

from typing import Callable, List, Optional


class ApprovalEngine:
    """工具审批规则引擎：可插拔规则列表，任一命中即触发审批弹窗"""

    def __init__(self, rules: Optional[List[Callable]] = None,
                 extra_dangerous: Optional[List[str]] = None):
        self.rules: List[Callable] = list(rules or [])
        if extra_dangerous:
            extra_set = set(extra_dangerous)
            self.rules.append(lambda name, kwargs: name in extra_set)

    def needs_approval(self, tool_name: str, tool_kwargs: dict) -> bool:
        return any(rule(tool_name, tool_kwargs) for rule in self.rules)

    def add_rule(self, rule: Callable):
        self.rules.append(rule)

    def remove_rule(self, rule: Callable):
        self.rules = [r for r in self.rules if r is not rule]

`````

--- **end of file: nb_agent/approval/engine.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/approval/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/approval/__init__.py`

#### 📦 Imports

- `from engine import ApprovalEngine`


---

`````python
from .engine import ApprovalEngine  # noqa: F401

`````

--- **end of file: nb_agent/approval/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/config/loader.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/config/loader.py`

#### 📝 Module Docstring

`````
配置加载器 — JSONC 格式，支持环境变量替换

加载优先级: CLI 参数 > 环境变量 > 项目级 ./config.jsonc > 全局 ~/.nb_agent/config.jsonc > 默认值

支持 {env:VARIABLE_NAME} 语法从环境变量读取值。
缺失的环境变量替换为空字符串。
`````

#### 📦 Imports

- `import copy`
- `import os`
- `import re`
- `from pathlib import Path`
- `import json5`
- `from dotenv import load_dotenv`
- `from nb_agent.utils.loggers import logger_config`

#### 🔧 Public Functions (1)

- `def load_config(cli_config_path: str = '', dotenv_path: str = '') -> dict`
  - *Line: 76*
  - *加载配置，返回合并后的配置字典*


---

`````python
"""
配置加载器 — JSONC 格式，支持环境变量替换

加载优先级: CLI 参数 > 环境变量 > 项目级 ./config.jsonc > 全局 ~/.nb_agent/config.jsonc > 默认值

支持 {env:VARIABLE_NAME} 语法从环境变量读取值。
缺失的环境变量替换为空字符串。
"""

import copy
import os
import re
from pathlib import Path

import json5
from dotenv import load_dotenv
from nb_agent.utils.loggers import logger_config


DEFAULT_CONFIG = {
    "agent": {
        "system_prompt": "你是一个智能助手。",
        "default_model": "",
        "max_context_tokens": 0,
        "streaming": True,
    },
    "provider": {},
    "mcp": {},
    "approval": {
        "dangerous_tools": [],
        "auto_approve": False,
    },
    "session": {
        "db_path": "",
    },
    "ui": {
        "theme": "dark",
        "show_tool_panel": True,
        "show_token_usage": True,
    },
}


def _substitute_env(text: str) -> str:
    """将 {env:VAR_NAME} 替换为对应环境变量值，缺失则替换为空字符串"""
    return re.sub(r"\{env:([^}]+)\}", lambda m: os.environ.get(m.group(1), ""), text)


def _find_config_file(cli_path: str = "") -> str:
    """按优先级查找配置文件"""
    if cli_path:
        return cli_path

    cwd_config = os.path.join(os.getcwd(), "config.jsonc")
    if os.path.isfile(cwd_config):
        return cwd_config

    home_config = os.path.join(Path.home(), ".nb_agent", "config.jsonc")
    if os.path.isfile(home_config):
        return home_config

    return ""


def _deep_merge(base: dict, override: dict) -> dict:
    """深度合并字典，override 覆盖 base"""
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config(cli_config_path: str = "", dotenv_path: str = "") -> dict:
    """加载配置，返回合并后的配置字典"""
    if dotenv_path:
        load_dotenv(dotenv_path, override=False)
    else:
        load_dotenv(override=False)

    config_path = _find_config_file(cli_config_path)
    if not config_path:
        return copy.deepcopy(DEFAULT_CONFIG)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            raw = f.read()
    except (FileNotFoundError, PermissionError) as e:
        logger_config.warning(f"配置文件读取失败: {e}，使用默认配置")
        return copy.deepcopy(DEFAULT_CONFIG)

    raw = _substitute_env(raw)
    try:
        user_config = json5.loads(raw)
    except ValueError as e:
        logger_config.warning(f"配置文件解析失败: {e}，使用默认配置")
        return copy.deepcopy(DEFAULT_CONFIG)

    merged = _deep_merge(copy.deepcopy(DEFAULT_CONFIG), user_config)
    merged["_config_path"] = config_path
    merged["_project_root"] = os.path.dirname(os.path.abspath(config_path))

    return merged

`````

--- **end of file: nb_agent/config/loader.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/config/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/config/__init__.py`

#### 📦 Imports

- `from loader import load_config`


---

`````python
from .loader import load_config  # noqa: F401

`````

--- **end of file: nb_agent/config/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/core/agent.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/core/agent.py`

#### 📝 Module Docstring

`````
AgentCore — ReAct 循环核心

核心循环：
  用户输入 → LLM(messages + tools) → 判断:
    有 tool_calls → 执行工具 → 结果回传 LLM → 再次判断（可能多轮）
    无 tool_calls → 返回文本回复
`````

#### 📦 Imports

- `import asyncio`
- `import functools`
- `import json`
- `import time`
- `import uuid`
- `from typing import AsyncIterator`
- `from typing import List`
- `from typing import Dict`
- `from typing import Optional`
- `from typing import Callable`
- `from openai import AsyncOpenAI`
- `from nb_agent.core.models import ModelInfo`
- `from nb_agent.core.models import ToolCallRecord`
- `from nb_agent.core.models import AgentResponse`
- `from nb_agent.core.models import load_models_from_config`
- `from nb_agent.core.context import trim_context`
- `from nb_agent.core.retry import call_llm_with_retry`
- `from nb_agent.core.retry import RETRYABLE_ERRORS`
- `from nb_agent.core.retry import MAX_RETRIES`
- `from nb_agent.session import SessionStore`
- `from nb_agent.mcp import MCPManager`
- `from nb_agent.approval import ApprovalEngine`
- `from nb_agent.tools import TOOL_REGISTRY`
- `from nb_agent.skills import SkillManager`
- `from nb_agent.utils.loggers import logger_llm_call`
- `from nb_agent.utils.loggers import logger_llm_call_raw`
- `import datetime as _dt`

#### 🏛️ Classes (1)

##### 📌 `class AgentCore`
*Line: 32*

**Docstring:**
`````
Agent 核心：
- Function Calling：LLM 自主决定是否调用工具
- 多轮工具调用：一次对话中可调用多个工具、多轮
- 通过回调实时通知 TUI 工具调用状态
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, config: dict)`
  - **Parameters:**
    - `self`
    - `config: dict`

**Public Methods (23):**
- `async def chat(self, user_input: str) -> AgentResponse`
- `async def chat_stream(self, user_input: str) -> AsyncIterator[str]`
  - *工具调用阶段用非流式（需要完整 tool_calls），最终回复用流式输出*
- `async def connect_mcp(self)`
- `async def disconnect_mcp(self)`
- `def switch_model(self, model_id: str) -> bool`
- `def get_models_grouped(self) -> Dict[str, List[ModelInfo]]`
- `async def generate_smart_title(self)`
- `def clear_history(self)`
- `def get_session_list(self, limit: int = 50) -> list`
- `def get_tools(self) -> list`
- `def get_tool_groups(self) -> list`
  - *返回所有工具分组及其状态*
- `def toggle_tool_group(self, group: str) -> bool`
  - *切换工具分组的启用/禁用状态，返回 True=已启用*
- `def get_mcp_status(self) -> list`
- `def toggle_mcp_server(self, name: str) -> bool`
- `def get_model_name(self) -> str`
- `def get_model_display_name(self) -> str`
- `def get_token_usage(self) -> dict`
- `def register_tool(self, name: str, func: Callable, description: str, parameters: dict, group: str = '')`
- `def get_agents(self) -> list`
  - *返回所有 Agent（含默认），当前使用的标记 is_current*
- `def save_agent(self, name: str, system_prompt: str, default_model: str = '', allowed_tool_groups: list = None, allowed_mcp_servers: list = None, allowed_skills: list = None) -> str`
- `def update_agent(self, agent_id: str, name: str, system_prompt: str, default_model: str = '', allowed_tool_groups: list = None, allowed_mcp_servers: list = None, allowed_skills: list = None)`
- `def delete_agent(self, agent_id: str) -> bool`
- `def apply_agent(self, agent_id: str)`
  - *应用 Agent 配置：替换 system prompt + 工具/MCP/Skills 开关 + 默认模型，新建会话*

**Class Variables (2):**
- `MAX_TOOL_ROUNDS = 30`
- `DEFAULT_AGENT_ID = '__default__'`


---

`````python
"""
AgentCore — ReAct 循环核心

核心循环：
  用户输入 → LLM(messages + tools) → 判断:
    有 tool_calls → 执行工具 → 结果回传 LLM → 再次判断（可能多轮）
    无 tool_calls → 返回文本回复
"""

import asyncio
import functools
import json
import time
import uuid
from typing import AsyncIterator, List, Dict, Optional, Callable

from openai import AsyncOpenAI

from nb_agent.core.models import (
    ModelInfo, ToolCallRecord, AgentResponse, load_models_from_config,
)
from nb_agent.core.context import trim_context
from nb_agent.core.retry import call_llm_with_retry, RETRYABLE_ERRORS, MAX_RETRIES
from nb_agent.session import SessionStore
from nb_agent.mcp import MCPManager
from nb_agent.approval import ApprovalEngine
from nb_agent.tools import TOOL_REGISTRY
from nb_agent.skills import SkillManager
from nb_agent.utils.loggers import logger_llm_call, logger_llm_call_raw


class AgentCore:
    """
    Agent 核心：
    - Function Calling：LLM 自主决定是否调用工具
    - 多轮工具调用：一次对话中可调用多个工具、多轮
    - 通过回调实时通知 TUI 工具调用状态
    """

    MAX_TOOL_ROUNDS = 30

    DEFAULT_AGENT_ID = "__default__"

    def __init__(self, config: dict):
        self.config = config
        self._base_prompt = config.get("agent", {}).get("system_prompt", "你是一个智能助手。")
        self.current_agent_id = self.DEFAULT_AGENT_ID
        self.current_agent_name = "默认助手"
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0
        self.last_turn_rounds = 0

        self.tool_registry: Dict[str, dict] = dict(TOOL_REGISTRY)

        project_root = config.get("_project_root", "")
        self.skill_manager = SkillManager(
            project_root=__import__("pathlib").Path(project_root) if project_root else None
        )
        self.skill_manager.discover()
        self.allowed_tool_groups: set = None
        self.allowed_skills: set = None
        self.system_prompt = self._build_system_prompt(self._base_prompt)
        self.messages: List[dict] = [{"role": "system", "content": self.system_prompt}]

        self.available_models: List[ModelInfo] = load_models_from_config(config)
        self.current_model: Optional[ModelInfo] = None
        self._llm_clients: Dict[str, AsyncOpenAI] = {}
        self._select_default_model()

        self.on_tool_call: Optional[Callable] = None
        self.approval_callback: Optional[Callable] = None

        extra_dangerous = config.get("approval", {}).get("dangerous_tools", [])
        self.approval_engine = ApprovalEngine(extra_dangerous=extra_dangerous or None)

        self.mcp_manager = MCPManager()

        db_path = config.get("session", {}).get("db_path", "")
        self.session_store = SessionStore(db_path)
        self.session_id = str(uuid.uuid4())[:8]
        model_id = self.current_model.id if self.current_model else ""
        self.session_store.create_session(
            self.session_id, title="新会话", model_id=model_id,
            agent_id=self.current_agent_id,
        )

    def _build_system_prompt(self, base_prompt: str) -> str:
        """在用户 system_prompt 末尾追加当前日期 + Skills 清单"""
        import datetime as _dt
        now = _dt.datetime.now()
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        date_str = f"{now.strftime('%Y-%m-%d')} {weekdays[now.weekday()]}"
        parts = [base_prompt, "", f"当前日期: {date_str}"]

        manifest = self.skill_manager.get_manifest(allowed_skills=self.allowed_skills)
        if manifest:
            parts.append("")
            parts.append("## 可用 Skills")
            parts.append("以下是你可以使用的技能指南。当任务匹配某个 Skill 时，先调用 `view_skill` 工具获取完整指南再执行。")
            parts.append("")
            for s in manifest:
                parts.append(f"- **{s['name']}**: {s['description']}")
            parts.append("")
            parts.append("调用方式: `view_skill(skill_name=\"<name>\")` 获取完整指南内容。")
        return "\n".join(parts)

    def _select_default_model(self):
        default = self.config.get("agent", {}).get("default_model", "")
        if default:
            for m in self.available_models:
                if m.id == default:
                    self.current_model = m
                    break
        if not self.current_model and self.available_models:
            self.current_model = self.available_models[0]

    def _get_client(self, model: ModelInfo) -> AsyncOpenAI:
        key = model.provider
        if key not in self._llm_clients:
            self._llm_clients[key] = AsyncOpenAI(
                base_url=model.base_url,
                api_key=model.api_key,
            )
        return self._llm_clients[key]

    def _get_openai_tools(self) -> list:
        """合并内置 tools + MCP tools + Skills view_skill，按 allowed 过滤"""
        tools = []
        for t in self.tool_registry.values():
            group = t.get("group", "")
            if group and self.allowed_tool_groups is not None and group not in self.allowed_tool_groups:
                continue
            tools.append(t["schema"])
        tools.extend(self.mcp_manager.get_all_tools_openai_format())
        if self.skill_manager.get_manifest(allowed_skills=self.allowed_skills):
            tools.append(self.skill_manager.get_view_skill_schema())
        return tools

    async def _execute_with_approval(self, name: str, args: dict) -> str:
        if self.approval_engine.needs_approval(name, args):
            if not self.approval_callback:
                return "[已拦截] 此操作需要审批但无审批通道，已自动拒绝"
            approved = await self.approval_callback(name, args)
            if not approved:
                return "[用户已拒绝执行此操作]"
        return await self._execute_tool(name, args)

    async def _execute_tool(self, name: str, args: dict) -> str:
        if name == "view_skill":
            skill_name = args.get("skill_name", "")
            result = self.skill_manager.view_skill(skill_name)
            if result["success"]:
                return result["content"]
            return json.dumps(result, ensure_ascii=False)

        if self.mcp_manager.is_mcp_tool(name):
            return await self.mcp_manager.call_tool(name, args)
        tool_info = self.tool_registry.get(name)
        if not tool_info:
            return f"错误: 未知工具 '{name}'"

        func = tool_info["function"]
        model_cls = tool_info.get("model_cls")
        try:
            if model_cls:
                params = model_cls(**args)
                if asyncio.iscoroutinefunction(func):
                    result = await func(params)
                else:
                    result = await asyncio.get_running_loop().run_in_executor(
                        None, functools.partial(func, params)
                    )
            else:
                if asyncio.iscoroutinefunction(func):
                    result = await func(**args)
                else:
                    result = await asyncio.get_running_loop().run_in_executor(
                        None, functools.partial(func, **args)
                    )
            return str(result)
        except Exception as e:
            return f"工具执行失败: {type(e).__name__}: {e}"

    async def _execute_tool_calls_batch(
        self, parsed_calls: list,
    ) -> dict:
        """批量执行工具调用：无需审批的并发执行，需审批的串行执行。

        Args:
            parsed_calls: [(tc_id, func_name, func_args, record_or_None), ...]
        Returns:
            dict: {tc_id: result_str, ...}
        """
        if len(parsed_calls) <= 1:
            results = {}
            for tc_id, func_name, func_args, _ in parsed_calls:
                results[tc_id] = await self._execute_with_approval(func_name, func_args)
            return results

        approval_calls = []
        concurrent_calls = []
        for item in parsed_calls:
            tc_id, func_name, func_args, _ = item
            if self.approval_engine.needs_approval(func_name, func_args):
                approval_calls.append(item)
            else:
                concurrent_calls.append(item)

        results: dict = {}

        if concurrent_calls:
            gather_results = await asyncio.gather(
                *[self._execute_tool(fn, fa) for _, fn, fa, _ in concurrent_calls],
                return_exceptions=True,
            )
            for (tc_id, _fn, _fa, _), result in zip(concurrent_calls, gather_results):
                if isinstance(result, BaseException):
                    result = f"工具执行失败: {type(result).__name__}: {result}"
                results[tc_id] = result

        for tc_id, func_name, func_args, _ in approval_calls:
            results[tc_id] = await self._execute_with_approval(func_name, func_args)

        return results

    def _clean_messages_for_api(self) -> list:
        return [
            {k: v for k, v in m.items() if not k.startswith('_')}
            for m in self.messages
        ]

    def _build_assistant_msg(self, resp_msg) -> dict:
        msg = {"role": "assistant", "content": resp_msg.content or ""}
        msg["_model"] = self.current_model.id if self.current_model else ""

        if resp_msg.tool_calls:
            msg["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in resp_msg.tool_calls
            ]
            if not msg["content"]:
                msg["content"] = None

        reasoning = getattr(resp_msg, "reasoning_content", None)
        if reasoning:
            msg["reasoning_content"] = reasoning

        return msg

    # ==================== 非流式 ====================

    async def chat(self, user_input: str) -> AgentResponse:
        self.messages.append({"role": "user", "content": user_input})
        self.messages = trim_context(
            self.messages,
            self.current_model.context_limit if self.current_model else 0,
        )
        self.session_store.save_message(self.session_id, "user", user_input)
        self._auto_update_title(user_input)

        if not self.current_model:
            return AgentResponse(text="[错误] 没有配置任何模型")

        client = self._get_client(self.current_model)
        openai_tools = self._get_openai_tools()
        all_tool_calls: list = []
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0
        self.last_turn_rounds = 0

        for round_idx in range(self.MAX_TOOL_ROUNDS):
            self.last_turn_rounds = round_idx + 1
            try:
                kwargs = {
                    "model": self.current_model.raw_id or self.current_model.id,
                    "messages": self._clean_messages_for_api(),
                }
                if openai_tools:
                    kwargs["tools"] = openai_tools

                resp = await call_llm_with_retry(client, **kwargs)
                resp_msg = resp.choices[0].message

                if resp.usage:
                    p = resp.usage.prompt_tokens or 0
                    c = resp.usage.completion_tokens or 0
                    self.last_turn_prompt += p
                    self.last_turn_completion += c
                    self.total_prompt_tokens += p
                    self.total_completion_tokens += c

                if not resp_msg.tool_calls:
                    reply = resp_msg.content or ""
                    reasoning = getattr(resp_msg, "reasoning_content", "") or ""
                    self.messages.append(self._build_assistant_msg(resp_msg))
                    tc_dicts = [{"name": t.name, "args": t.args, "result": t.result} for t in all_tool_calls]
                    self.session_store.save_message(
                        self.session_id, "assistant", reply,
                        reasoning=reasoning, tool_calls=tc_dicts,
                    )
                    return AgentResponse(
                        text=reply, reasoning=reasoning,
                        tool_calls=all_tool_calls, token_usage=self.get_token_usage(),
                    )

                self.messages.append(self._build_assistant_msg(resp_msg))

                parsed_calls = []
                for tc in resp_msg.tool_calls:
                    func_name = tc.function.name
                    try:
                        func_args = json.loads(tc.function.arguments)
                    except json.JSONDecodeError:
                        func_args = {}
                    record = ToolCallRecord(name=func_name, args=func_args, status="running")
                    all_tool_calls.append(record)
                    self.last_turn_tool_calls += 1
                    if self.on_tool_call:
                        self.on_tool_call(record)
                    parsed_calls.append((tc.id, func_name, func_args, record))

                results_map = await self._execute_tool_calls_batch(parsed_calls)

                for tc_id, func_name, func_args, record in parsed_calls:
                    result = results_map[tc_id]
                    record.result = result
                    record.status = "error" if result.startswith(
                        ("[已拦截]", "[用户已拒绝", "错误:", "工具执行失败")
                    ) else "done"
                    if self.on_tool_call:
                        self.on_tool_call(record)
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tc_id,
                        "content": result,
                    })

            except RETRYABLE_ERRORS as e:
                error_text = f"[网络/超时错误（已重试 {MAX_RETRIES} 次）] {type(e).__name__}: {e}"
                self.messages.append({"role": "assistant", "content": error_text})
                return AgentResponse(text=error_text, tool_calls=all_tool_calls, token_usage=self.get_token_usage())
            except Exception as e:
                error_text = f"[LLM 调用失败] {type(e).__name__}: {e}"
                self.messages.append({"role": "assistant", "content": error_text})
                return AgentResponse(text=error_text, tool_calls=all_tool_calls, token_usage=self.get_token_usage())

        return AgentResponse(
            text="[警告] 工具调用轮次超限，已强制停止",
            tool_calls=all_tool_calls, token_usage=self.get_token_usage(),
        )

    # ==================== 流式 ====================

    async def chat_stream(self, user_input: str) -> AsyncIterator[str]:
        """工具调用阶段用非流式（需要完整 tool_calls），最终回复用流式输出"""
        self.messages.append({"role": "user", "content": user_input})
        self.messages = trim_context(
            self.messages,
            self.current_model.context_limit if self.current_model else 0,
        )
        self.session_store.save_message(self.session_id, "user", user_input)
        self._auto_update_title(user_input)

        if not self.current_model:
            yield "[错误] 没有配置任何模型"
            return

        client = self._get_client(self.current_model)
        openai_tools = self._get_openai_tools()
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0
        self.last_turn_rounds = 0

        for round_idx in range(self.MAX_TOOL_ROUNDS):
            self.last_turn_rounds = round_idx + 1
            try:
                kwargs = {
                    "model": self.current_model.raw_id or self.current_model.id,
                    "messages": self._clean_messages_for_api(),
                    "stream": True,
                }
                kwargs["stream_options"] = {"include_usage": True}
                if openai_tools:
                    kwargs["tools"] = openai_tools

                stream_resp = await call_llm_with_retry(client, **kwargs)
                stream_t0 = time.monotonic()

                full_content = ""
                full_reasoning = ""
                tool_calls_map: Dict[int, dict] = {}
                in_thinking = False
                has_tool_calls = False
                chunk = None

                async for chunk in stream_resp:
                    delta = chunk.choices[0].delta if chunk.choices else None
                    if not delta:
                        continue

                    reasoning_chunk = getattr(delta, "reasoning_content", None) or ""
                    if reasoning_chunk:
                        if not in_thinking:
                            in_thinking = True
                            yield "<think>"
                        full_reasoning += reasoning_chunk
                        yield reasoning_chunk

                    content_chunk = delta.content or ""
                    if content_chunk:
                        if in_thinking:
                            in_thinking = False
                            yield "</think>"
                        full_content += content_chunk
                        yield content_chunk

                    if delta.tool_calls:
                        has_tool_calls = True
                        for tc_delta in delta.tool_calls:
                            idx = tc_delta.index
                            if idx not in tool_calls_map:
                                tool_calls_map[idx] = {"id": tc_delta.id or "", "name": "", "arguments": ""}
                            if tc_delta.function:
                                if tc_delta.function.name:
                                    tool_calls_map[idx]["name"] = tc_delta.function.name
                                if tc_delta.function.arguments:
                                    tool_calls_map[idx]["arguments"] += tc_delta.function.arguments

                if in_thinking:
                    yield "</think>"

                if chunk and hasattr(chunk, 'usage') and chunk.usage:
                    p = chunk.usage.prompt_tokens or 0
                    c = chunk.usage.completion_tokens or 0
                    self.last_turn_prompt += p
                    self.last_turn_completion += c
                    self.total_prompt_tokens += p
                    self.total_completion_tokens += c

                stream_elapsed = time.monotonic() - stream_t0
                stream_summary = {
                    "content_length": len(full_content),
                    "reasoning_length": len(full_reasoning),
                    "has_tool_calls": has_tool_calls,
                    "tool_calls": [
                        {"name": tc["name"], "args": tc["arguments"][:200]}
                        for tc in tool_calls_map.values()
                    ] if has_tool_calls else [],
                    "usage": {"prompt": self.last_turn_prompt, "completion": self.last_turn_completion},
                }
                logger_llm_call.info(
                    f"[LLM流式完成] round={round_idx + 1} elapsed={stream_elapsed:.2f}s | "
                    f"{json.dumps(stream_summary, ensure_ascii=False, default=str)}\n\n"
                )
                raw_resp = {
                    "content": full_content,
                    "reasoning_content": full_reasoning,
                    "tool_calls": [tool_calls_map[k] for k in sorted(tool_calls_map.keys())] if has_tool_calls else [],
                    "usage": {"prompt": self.last_turn_prompt, "completion": self.last_turn_completion},
                }
                logger_llm_call_raw.info(
                    f"[LLM流式完成-RAW] round={round_idx + 1} elapsed={stream_elapsed:.2f}s\n"
                    f"{json.dumps(raw_resp, ensure_ascii=False, default=str, indent=2)}\n\n"
                )

                if not has_tool_calls:
                    msg = {"role": "assistant", "content": full_content}
                    msg["_model"] = self.current_model.id if self.current_model else ""
                    if full_reasoning:
                        msg["reasoning_content"] = full_reasoning
                    self.messages.append(msg)
                    self.session_store.save_message(
                        self.session_id, "assistant", full_content, reasoning=full_reasoning,
                    )
                    return

                assembled_tool_calls = []
                for idx in sorted(tool_calls_map.keys()):
                    tc = tool_calls_map[idx]
                    assembled_tool_calls.append({
                        "id": tc["id"],
                        "type": "function",
                        "function": {"name": tc["name"], "arguments": tc["arguments"]},
                    })

                msg = {
                    "role": "assistant",
                    "content": full_content or None,
                    "tool_calls": assembled_tool_calls,
                    "_model": self.current_model.id if self.current_model else "",
                }
                if full_reasoning:
                    msg["reasoning_content"] = full_reasoning
                self.messages.append(msg)

                parsed_stream = []
                for tc in assembled_tool_calls:
                    func_name = tc["function"]["name"]
                    try:
                        func_args = json.loads(tc["function"]["arguments"])
                    except json.JSONDecodeError:
                        func_args = {}
                    self.last_turn_tool_calls += 1
                    yield f"\n🔧 调用工具: {func_name}({json.dumps(func_args, ensure_ascii=False)})\n"
                    parsed_stream.append((tc["id"], func_name, func_args, None))

                results_map = await self._execute_tool_calls_batch(parsed_stream)

                stream_tool_records = []
                for tc_id, func_name, func_args, _ in parsed_stream:
                    result = results_map[tc_id]
                    stream_tool_records.append({"name": func_name, "args": func_args, "result": result})
                    yield f"📋 结果: {result}\n"
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tc_id,
                        "content": result,
                    })

                self.session_store.save_message(
                    self.session_id, "assistant", full_content,
                    reasoning=full_reasoning, tool_calls=stream_tool_records,
                )

            except RETRYABLE_ERRORS as e:
                error_text = f"[网络/超时错误（已重试 {MAX_RETRIES} 次）] {type(e).__name__}: {e}"
                self.messages.append({"role": "assistant", "content": error_text, "_model": self.current_model.id if self.current_model else ""})
                self.session_store.save_message(self.session_id, "assistant", error_text)
                yield f"\n{error_text}"
                return
            except Exception as e:
                error_text = f"[LLM 调用失败] {type(e).__name__}: {e}"
                self.messages.append({"role": "assistant", "content": error_text, "_model": self.current_model.id if self.current_model else ""})
                self.session_store.save_message(self.session_id, "assistant", error_text)
                yield f"\n{error_text}"
                return

        yield "\n[警告] 工具调用轮次超限"

    # ==================== MCP ====================

    async def connect_mcp(self):
        mcp_config = self.config.get("mcp", {})
        project_root = self.config.get("_project_root", "")
        if mcp_config:
            await self.mcp_manager.connect_all(mcp_config, project_root=project_root)

    async def disconnect_mcp(self):
        await self.mcp_manager.disconnect_all()

    # ==================== 查询接口 ====================

    def switch_model(self, model_id: str) -> bool:
        for m in self.available_models:
            if m.id == model_id:
                self.current_model = m
                return True
        return False

    def get_models_grouped(self) -> Dict[str, List[ModelInfo]]:
        groups: Dict[str, List[ModelInfo]] = {}
        for m in self.available_models:
            groups.setdefault(m.provider_name, []).append(m)
        return groups

    def _auto_update_title(self, user_input: str):
        current_title = self.session_store.get_session_title(self.session_id)
        if current_title == "新会话":
            title = user_input[:30].replace("\n", " ").strip()
            if title:
                self.session_store.update_session_title(self.session_id, title)

    async def generate_smart_title(self):
        current_title = self.session_store.get_session_title(self.session_id)
        if not current_title or current_title == "新会话":
            return
        user_msgs = [m["content"] for m in self.messages if m.get("role") == "user"]
        if not user_msgs:
            return
        first_msg = user_msgs[0][:200]
        try:
            if not self.current_model:
                return
            client = self._get_client(self.current_model)
            resp = await client.chat.completions.create(
                model=self.current_model.raw_id or self.current_model.id,
                messages=[
                    {"role": "system", "content": "你是一个标题生成器。根据用户的问题，生成一个不超过10个字的简短标题。只输出标题文字，不加引号或标点。"},
                    {"role": "user", "content": first_msg},
                ],
                max_tokens=20,
                temperature=0.3,
            )
            title = (resp.choices[0].message.content or "").strip().strip('"\'')
            if title and len(title) <= 30:
                self.session_store.update_session_title(self.session_id, title)
        except Exception:
            pass

    def clear_history(self):
        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0
        self.session_id = str(uuid.uuid4())[:8]
        model_id = self.current_model.id if self.current_model else ""
        self.session_store.create_session(
            self.session_id, title="新会话", model_id=model_id,
            agent_id=self.current_agent_id,
        )

    def get_session_list(self, limit: int = 50) -> list:
        return self.session_store.list_sessions(limit)

    def get_tools(self) -> list:
        builtin = []
        for name, t in self.tool_registry.items():
            group = t.get("group", "")
            func = t.get("function")
            module = getattr(func, "__module__", "") if func else ""
            is_builtin = module.startswith("nb_agent.tools.")
            source = "内置" if is_builtin else "第三方"
            builtin.append({
                "name": name,
                "func_name": t.get("func_name", name),
                "group": group,
                "description": t["schema"]["function"]["description"],
                "source": source,
                "disabled": (self.allowed_tool_groups is not None and group not in self.allowed_tool_groups) if group else False,
            })
        if self.skill_manager.get_manifest(allowed_skills=self.allowed_skills):
            builtin.append({
                "name": "view_skill",
                "func_name": "view_skill",
                "group": "nb_agent_builtin",
                "description": "查看 Skill 完整指南",
                "source": "Skills",
                "disabled": self.allowed_tool_groups is not None and "nb_agent_builtin" not in self.allowed_tool_groups,
            })
        mcp_tools = []
        for t in self.mcp_manager.get_tool_info_list():
            server = t["server"]
            mcp_tools.append({
                "name": f"mcp__{server}__{t['name']}",
                "func_name": t["name"],
                "group": f"mcp__{server}",
                "description": t["description"],
                "source": f"MCP:{server}",
                "disabled": not self.mcp_manager.is_server_enabled(server),
            })
        return builtin + mcp_tools

    def get_tool_groups(self) -> list:
        """返回所有工具分组及其状态"""
        groups = {}
        for t in self.get_tools():
            group = t.get("group", "")
            if not group:
                group = "(无分组)"
            if group not in groups:
                groups[group] = {"name": group, "count": 0, "disabled": False, "source": t["source"]}
            groups[group]["count"] += 1
            groups[group]["disabled"] = t.get("disabled", False)
        return sorted(groups.values(), key=lambda g: g["name"])

    def toggle_tool_group(self, group: str) -> bool:
        """切换工具分组的启用/禁用状态，返回 True=已启用"""
        if group.startswith("mcp__"):
            server_name = group[5:]
            return self.mcp_manager.toggle_server(server_name)
        if self.allowed_tool_groups is None:
            all_groups = {t.get("group", "") for t in self.tool_registry.values() if t.get("group")}
            self.allowed_tool_groups = all_groups - {group}
            return False
        if group in self.allowed_tool_groups:
            self.allowed_tool_groups.discard(group)
            return False
        self.allowed_tool_groups.add(group)
        return True

    def get_mcp_status(self) -> list:
        return self.mcp_manager.get_server_status()

    def toggle_mcp_server(self, name: str) -> bool:
        return self.mcp_manager.toggle_server(name)

    def get_model_name(self) -> str:
        return self.current_model.id if self.current_model else "未配置"

    def get_model_display_name(self) -> str:
        return self.current_model.name if self.current_model else "未配置"

    def get_token_usage(self) -> dict:
        return {
            "last_prompt": self.last_turn_prompt,
            "last_completion": self.last_turn_completion,
            "last_total": self.last_turn_prompt + self.last_turn_completion,
            "last_tool_calls": self.last_turn_tool_calls,
            "last_rounds": self.last_turn_rounds,
            "total_prompt": self.total_prompt_tokens,
            "total_completion": self.total_completion_tokens,
            "total": self.total_prompt_tokens + self.total_completion_tokens,
        }

    def register_tool(self, name: str, func: Callable, description: str,
                      parameters: dict, group: str = ""):
        tool_name = f"{group}__{name}" if group else name
        self.tool_registry[tool_name] = {
            "function": func,
            "group": group,
            "func_name": name,
            "schema": {
                "type": "function",
                "function": {
                    "name": tool_name,
                    "description": description,
                    "parameters": parameters,
                },
            },
        }

    # ==================== Agent ====================

    def get_agents(self) -> list:
        """返回所有 Agent（含默认），当前使用的标记 is_current"""
        default = {
            "id": self.DEFAULT_AGENT_ID,
            "name": "默认助手",
            "system_prompt": self._base_prompt,
            "default_model": self.current_model.id if self.current_model else "",
            "allowed_tool_groups": None,
            "allowed_mcp_servers": None,
            "allowed_skills": None,
            "is_builtin": True,
        }
        saved = self.session_store.list_agents()
        result = [default] + saved
        return result

    def save_agent(self, name: str, system_prompt: str,
                   default_model: str = "",
                   allowed_tool_groups: list = None,
                   allowed_mcp_servers: list = None,
                   allowed_skills: list = None) -> str:
        agent_id = str(uuid.uuid4())[:8]
        self.session_store.create_agent(
            agent_id, name, system_prompt,
            default_model=default_model,
            allowed_tool_groups=allowed_tool_groups,
            allowed_mcp_servers=allowed_mcp_servers,
            allowed_skills=allowed_skills,
        )
        return agent_id

    def update_agent(self, agent_id: str, name: str, system_prompt: str,
                     default_model: str = "",
                     allowed_tool_groups: list = None,
                     allowed_mcp_servers: list = None,
                     allowed_skills: list = None):
        self.session_store.update_agent(
            agent_id, name, system_prompt,
            default_model=default_model,
            allowed_tool_groups=allowed_tool_groups,
            allowed_mcp_servers=allowed_mcp_servers,
            allowed_skills=allowed_skills,
        )
        if self.current_agent_id == agent_id:
            self.current_agent_name = name
            if default_model:
                self.switch_model(default_model)
            self.allowed_skills = set(allowed_skills) if allowed_skills is not None else None
            self.system_prompt = self._build_system_prompt(system_prompt)
            self.messages[0] = {"role": "system", "content": self.system_prompt}
            self.allowed_tool_groups = set(allowed_tool_groups) if allowed_tool_groups is not None else None
            self.mcp_manager.set_allowed_servers(allowed_mcp_servers)

    def delete_agent(self, agent_id: str) -> bool:
        if agent_id == self.DEFAULT_AGENT_ID:
            return False
        self.session_store.delete_agent(agent_id)
        if self.current_agent_id == agent_id:
            self.apply_agent(self.DEFAULT_AGENT_ID)
        return True

    def apply_agent(self, agent_id: str):
        """应用 Agent 配置：替换 system prompt + 工具/MCP/Skills 开关 + 默认模型，新建会话"""
        if agent_id == self.DEFAULT_AGENT_ID:
            agent_data = {
                "name": "默认助手",
                "system_prompt": self._base_prompt,
                "default_model": "",
                "allowed_tool_groups": None,
                "allowed_mcp_servers": None,
                "allowed_skills": None,
            }
        else:
            agent_data = self.session_store.get_agent(agent_id)
            if not agent_data:
                return

        self.current_agent_id = agent_id
        self.current_agent_name = agent_data["name"]
        raw_skills = agent_data.get("allowed_skills")
        self.allowed_skills = set(raw_skills) if raw_skills is not None else None
        self.system_prompt = self._build_system_prompt(agent_data["system_prompt"])
        raw_groups = agent_data.get("allowed_tool_groups")
        self.allowed_tool_groups = set(raw_groups) if raw_groups is not None else None
        self.mcp_manager.set_allowed_servers(agent_data.get("allowed_mcp_servers"))

        default_model = agent_data.get("default_model", "")
        if default_model:
            self.switch_model(default_model)

        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0
        self.session_id = str(uuid.uuid4())[:8]
        model_id = self.current_model.id if self.current_model else ""
        self.session_store.create_session(
            self.session_id, title="新会话", model_id=model_id,
            agent_id=agent_id,
        )

`````

--- **end of file: nb_agent/core/agent.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/core/context.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/core/context.py`

#### 📝 Module Docstring

`````
上下文窗口管理 — token 估算 + 自动裁剪
`````

#### 📦 Imports

- `from typing import List`

#### 🔧 Public Functions (2)

- `def estimate_tokens(text: str) -> int`
  - *Line: 6*
  - *粗略估算 token 数（中文约 1.5 字/token，英文约 4 字符/token）*

- `def trim_context(messages: List[dict], context_limit: int) -> List[dict]`
  - *Line: 26*
  - **Docstring:**
  `````
  当消息总 token 超出模型限制时，从最早的非 system 消息开始移除
  
  注意：此函数会原地修改传入的 messages 列表。
  `````


---

`````python
"""上下文窗口管理 — token 估算 + 自动裁剪"""

from typing import List


def estimate_tokens(text: str) -> int:
    """粗略估算 token 数（中文约 1.5 字/token，英文约 4 字符/token）"""
    if not text:
        return 0
    cn_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    en_chars = len(text) - cn_chars
    return int(cn_chars / 1.5 + en_chars / 4)


def _estimate_message_tokens(msg: dict) -> int:
    """估算单条消息的总 token（包括 content、reasoning、tool_calls）"""
    total = estimate_tokens(msg.get("content", "") or "")
    total += estimate_tokens(msg.get("reasoning_content", "") or "")
    for tc in msg.get("tool_calls", []):
        func = tc.get("function", {})
        total += estimate_tokens(func.get("name", ""))
        total += estimate_tokens(func.get("arguments", ""))
    return total


def trim_context(messages: List[dict], context_limit: int) -> List[dict]:
    """当消息总 token 超出模型限制时，从最早的非 system 消息开始移除

    注意：此函数会原地修改传入的 messages 列表。
    """
    if not context_limit:
        return messages

    max_tokens = int(context_limit * 0.85)

    total = sum(_estimate_message_tokens(m) for m in messages)

    while total > max_tokens and len(messages) > 2:
        removed = messages.pop(1)
        total -= _estimate_message_tokens(removed)

    return messages

`````

--- **end of file: nb_agent/core/context.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/core/models.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/core/models.py`

#### 📝 Module Docstring

`````
数据结构 — AgentCore 使用的 dataclass
`````

#### 📦 Imports

- `from dataclasses import dataclass`
- `from dataclasses import field`
- `from typing import List`

#### 🏛️ Classes (3)

##### 📌 `class ToolCallRecord`
*Line: 8*

**Docstring:**
`````
工具调用记录（给 TUI 展示用）
`````

**Class Variables (4):**
- `name: str`
- `args: dict`
- `result: str = ''`
- `status: str = 'pending'`

##### 📌 `class AgentResponse`
*Line: 17*

**Docstring:**
`````
Agent 的回复
`````

**Class Variables (4):**
- `text: str`
- `reasoning: str = ''`
- `tool_calls: list = field(default_factory=list)`
- `token_usage: dict = field(default_factory=dict)`

##### 📌 `class ModelInfo`
*Line: 26*

**Docstring:**
`````
模型信息
`````

**Class Variables (9):**
- `id: str`
- `name: str`
- `provider: str`
- `provider_name: str`
- `base_url: str`
- `api_key: str`
- `context_limit: int = 0`
- `output_limit: int = 0`
- `raw_id: str = ''`

#### 🔧 Public Functions (1)

- `def load_models_from_config(config: dict) -> List[ModelInfo]`
  - *Line: 39*
  - *从 config.jsonc 的 provider 节解析所有模型*


---

`````python
"""数据结构 — AgentCore 使用的 dataclass"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ToolCallRecord:
    """工具调用记录（给 TUI 展示用）"""
    name: str
    args: dict
    result: str = ""
    status: str = "pending"  # pending / running / done / error


@dataclass
class AgentResponse:
    """Agent 的回复"""
    text: str
    reasoning: str = ""
    tool_calls: list = field(default_factory=list)
    token_usage: dict = field(default_factory=dict)


@dataclass
class ModelInfo:
    """模型信息"""
    id: str
    name: str
    provider: str
    provider_name: str
    base_url: str
    api_key: str
    context_limit: int = 0
    output_limit: int = 0
    raw_id: str = ""


def load_models_from_config(config: dict) -> List[ModelInfo]:
    """从 config.jsonc 的 provider 节解析所有模型"""
    models = []
    for provider_id, provider_cfg in config.get("provider", {}).items():
        provider_name = provider_cfg.get("name", provider_id)
        base_url = provider_cfg.get("base_url", "")
        api_key = provider_cfg.get("api_key", "")

        for model_id, model_cfg in provider_cfg.get("models", {}).items():
            limit = model_cfg.get("limit", {})
            models.append(ModelInfo(
                id=model_id,
                name=model_cfg.get("name", model_id),
                provider=provider_id,
                provider_name=provider_name,
                base_url=base_url,
                api_key=api_key,
                context_limit=limit.get("context", 0),
                output_limit=limit.get("output", 0),
                raw_id=model_cfg.get("raw_model", ""),
            ))
    return models

`````

--- **end of file: nb_agent/core/models.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/core/retry.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/core/retry.py`

#### 📝 Module Docstring

`````
LLM 调用重试 — 指数退避 + 双日志（摘要 + 原始）
`````

#### 📦 Imports

- `import asyncio`
- `import json`
- `import time`
- `from openai import APITimeoutError`
- `from openai import RateLimitError`
- `from openai import APIConnectionError`
- `from nb_agent.utils.loggers import logger_llm_call`
- `from nb_agent.utils.loggers import logger_llm_call_raw`

#### 🔧 Public Functions (1)

- `async def call_llm_with_retry(client, **kwargs)`
  - *Line: 88*
  - *带重试的 LLM 调用（超时/限流/网络错误自动重试），双日志*


---

`````python
"""LLM 调用重试 — 指数退避 + 双日志（摘要 + 原始）"""

import asyncio
import json
import time
from openai import APITimeoutError, RateLimitError, APIConnectionError

from nb_agent.utils.loggers import logger_llm_call, logger_llm_call_raw

MAX_RETRIES = 3
RETRY_DELAYS = [1, 3, 5]
RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, APIConnectionError, ConnectionError, TimeoutError)


def _safe_serialize(obj, max_len=5000):
    """安全序列化，截断过长内容"""
    try:
        s = json.dumps(obj, ensure_ascii=False, default=str)
        if len(s) > max_len:
            return s[:max_len] + f"...(截断，原始长度 {len(s)})"
        return s
    except Exception:
        return str(obj)[:max_len]


def _full_serialize(obj):
    """完整序列化，不截断"""
    try:
        return json.dumps(obj, ensure_ascii=False, default=str, indent=2)
    except Exception:
        return str(obj)


def _extract_request_summary(kwargs: dict) -> dict:
    """提取请求摘要（不含完整 messages 以免日志过大）"""
    summary = {"model": kwargs.get("model", "?")}

    messages = kwargs.get("messages", [])
    summary["message_count"] = len(messages)
    if messages:
        summary["last_message_role"] = messages[-1].get("role", "?")
        last_content = messages[-1].get("content", "")
        if isinstance(last_content, str) and len(last_content) > 200:
            last_content = last_content[:200] + "..."
        summary["last_message_preview"] = last_content

    tools = kwargs.get("tools", [])
    if tools:
        summary["tool_count"] = len(tools)
        summary["tool_names"] = [t.get("function", {}).get("name", "?") for t in tools[:20]]

    summary["stream"] = kwargs.get("stream", False)
    return summary


def _extract_response_summary(resp) -> dict:
    """提取响应摘要"""
    summary = {}
    try:
        choice = resp.choices[0] if resp.choices else None
        if choice:
            msg = choice.message
            summary["finish_reason"] = choice.finish_reason
            if msg.content:
                content = msg.content
                summary["content_length"] = len(content)
                summary["content_preview"] = content[:300] + "..." if len(content) > 300 else content
            if msg.tool_calls:
                summary["tool_calls"] = [
                    {"name": tc.function.name, "args_preview": tc.function.arguments[:200]}
                    for tc in msg.tool_calls
                ]
            reasoning = getattr(msg, "reasoning_content", None)
            if reasoning:
                summary["reasoning_length"] = len(reasoning)

        if resp.usage:
            summary["usage"] = {
                "prompt": resp.usage.prompt_tokens,
                "completion": resp.usage.completion_tokens,
                "total": (resp.usage.prompt_tokens or 0) + (resp.usage.completion_tokens or 0),
            }
    except Exception as e:
        summary["parse_error"] = str(e)
    return summary


async def call_llm_with_retry(client, **kwargs):
    """带重试的 LLM 调用（超时/限流/网络错误自动重试），双日志"""
    last_error: Exception = RuntimeError("LLM 调用失败（未知错误）")
    req_summary = _extract_request_summary(kwargs)

    for attempt in range(MAX_RETRIES):
        t0 = time.monotonic()
        try:
            # 摘要日志
            logger_llm_call.info(f"[LLM请求] attempt={attempt + 1} | {_safe_serialize(req_summary)}\n\n")
            # 原始日志：完整请求体
            logger_llm_call_raw.info(f"[LLM请求-RAW] attempt={attempt + 1}\n{_full_serialize(kwargs)}\n\n")

            result = await client.chat.completions.create(**kwargs)
            elapsed = time.monotonic() - t0

            if not kwargs.get("stream"):
                # 摘要日志
                resp_summary = _extract_response_summary(result)
                logger_llm_call.info(
                    f"[LLM响应] elapsed={elapsed:.2f}s | {_safe_serialize(resp_summary)}\n\n"
                )
                # 原始日志：完整响应
                try:
                    raw_resp = result.model_dump_json(indent=2)
                except Exception:
                    raw_resp = str(result)
                logger_llm_call_raw.info(f"[LLM响应-RAW] elapsed={elapsed:.2f}s\n{raw_resp}\n\n")
            else:
                logger_llm_call.info(f"[LLM流式] stream opened, elapsed={elapsed:.2f}s\n\n")
                logger_llm_call_raw.info(f"[LLM流式-RAW] stream opened, elapsed={elapsed:.2f}s\n\n")

            return result

        except RETRYABLE_ERRORS as e:
            elapsed = time.monotonic() - t0
            last_error = e
            msg = (f"[LLM重试] attempt={attempt + 1} elapsed={elapsed:.2f}s | "
                   f"{type(e).__name__}: {e}\n\n")
            logger_llm_call.warning(msg)
            logger_llm_call_raw.warning(msg)
            if attempt < MAX_RETRIES - 1:
                delay = RETRY_DELAYS[min(attempt, len(RETRY_DELAYS) - 1)]
                await asyncio.sleep(delay)

    fail_msg = f"[LLM失败] 已重试{MAX_RETRIES}次 | {type(last_error).__name__}: {last_error}\n\n"
    logger_llm_call.error(fail_msg)
    logger_llm_call_raw.error(fail_msg)
    raise last_error

`````

--- **end of file: nb_agent/core/retry.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/core/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/core/__init__.py`

#### 📦 Imports

- `from agent import AgentCore`
- `from models import ModelInfo`
- `from models import ToolCallRecord`
- `from models import AgentResponse`


---

`````python
from .agent import AgentCore  # noqa: F401
from .models import ModelInfo, ToolCallRecord, AgentResponse  # noqa: F401

`````

--- **end of file: nb_agent/core/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/mcp/client.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/mcp/client.py`

#### 📝 Module Docstring

`````
MCP 客户端管理器 — 连接多个 MCP Server，统一管理工具

支持四种传输方式:
  - local (stdio): 启动子进程，通过 stdin/stdout 通信
  - sse: 通过 SSE 连接远程 MCP Server
  - streamableHttp / http: 通过 Streamable HTTP 连接远程 MCP Server（http 是 streamableHttp 的别名）
`````

#### 📦 Imports

- `import asyncio`
- `import contextlib`
- `import json`
- `import os`
- `import sys`
- `from typing import Dict`
- `from typing import List`
- `from typing import Optional`
- `from typing import Any`
- `from typing import TextIO`
- `from nb_agent.utils.loggers import logger_mcp`
- `from mcp import ClientSession`
- `from mcp.client.stdio import stdio_client`
- `from mcp.client.stdio import StdioServerParameters`
- `from mcp.client.sse import sse_client`
- `from mcp.client.streamable_http import streamablehttp_client`

#### 🏛️ Classes (2)

##### 📌 `class MCPServerInfo`
*Line: 40*

**Docstring:**
`````
单个 MCP Server 的连接信息
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, name: str, session = None)`
  - **Parameters:**
    - `self`
    - `name: str`
    - `session = None`

**Public Methods (1):**
- `async def reconnect(self, manager: 'MCPManager', cfg: dict)`
  - *断线后重连，复用旧的 exit_stack*

##### 📌 `class MCPManager`
*Line: 57*

**Docstring:**
`````
管理多个 MCP Server 的连接和工具调用
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self)`
  - **Parameters:**
    - `self`

**Public Methods (11):**
- `async def connect_all(self, mcp_config: dict, project_root: str = '')`
  - **Docstring:**
  `````
  根据配置连接所有 MCP Server
  
  SSE/HTTP 连接必须在调用者任务中初始化（anyio cancel scope 要求），
  因此只有 stdio 类型才能用 asyncio.gather 并发启动。
  `````
- `async def connect_server(self, name: str, cfg: dict)`
  - *连接单个 MCP Server*
- `async def disconnect_all(self)`
- `def toggle_server(self, name: str) -> bool`
  - *切换 MCP Server 启用/禁用，返回 True=已启用*
- `def is_server_enabled(self, name: str) -> bool`
- `def set_allowed_servers(self, names: list)`
- `def get_all_tools_openai_format(self) -> List[dict]`
- `def get_tool_info_list(self) -> List[dict]`
  - *返回所有已连接 server 的工具（含禁用的，用于 UI 显示）*
- `def get_server_status(self) -> List[dict]`
- `async def call_tool(self, full_tool_name: str, arguments: dict) -> str`
  - *调用 MCP 工具。full_tool_name 格式: mcp__{server}__{tool}*
- `def is_mcp_tool(self, tool_name: str) -> bool`


---

`````python
"""
MCP 客户端管理器 — 连接多个 MCP Server，统一管理工具

支持四种传输方式:
  - local (stdio): 启动子进程，通过 stdin/stdout 通信
  - sse: 通过 SSE 连接远程 MCP Server
  - streamableHttp / http: 通过 Streamable HTTP 连接远程 MCP Server（http 是 streamableHttp 的别名）
"""

import asyncio
import contextlib
import json
import os
import sys
from typing import Dict, List, Optional, Any, TextIO

from nb_agent.utils.loggers import logger_mcp

try:
    from mcp import ClientSession
    from mcp.client.stdio import stdio_client, StdioServerParameters
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False
    logger_mcp.warning("MCP SDK 未安装，请运行: pip install mcp")

try:
    from mcp.client.sse import sse_client
    SSE_AVAILABLE = True
except ImportError:
    SSE_AVAILABLE = False

try:
    from mcp.client.streamable_http import streamablehttp_client
    STREAMABLE_HTTP_AVAILABLE = True
except ImportError:
    STREAMABLE_HTTP_AVAILABLE = False


class MCPServerInfo:
    """单个 MCP Server 的连接信息"""

    def __init__(self, name: str, session=None):
        self.name = name
        self.session = session
        self.tools: list = []
        self.connected = False
        self.error = ""
        self._exit_stack: Optional[contextlib.AsyncExitStack] = None

    async def reconnect(self, manager: "MCPManager", cfg: dict):
        """断线后重连，复用旧的 exit_stack"""
        await manager._cleanup_remote(self)
        await manager.connect_server(self.name, cfg)


class MCPManager:
    """管理多个 MCP Server 的连接和工具调用"""

    def __init__(self):
        self.servers: Dict[str, MCPServerInfo] = {}
        self._stdio_exit_stack = contextlib.AsyncExitStack()
        self._project_root = ""
        self._all_configs: Dict[str, dict] = {}
        self._allowed_servers: set = None
        self.errlog: Optional[TextIO] = None

    async def connect_all(self, mcp_config: dict, project_root: str = ""):
        """根据配置连接所有 MCP Server

        SSE/HTTP 连接必须在调用者任务中初始化（anyio cancel scope 要求），
        因此只有 stdio 类型才能用 asyncio.gather 并发启动。
        """
        self._project_root = project_root
        self._all_configs = dict(mcp_config)

        if not MCP_AVAILABLE:
            logger_mcp.error("MCP SDK 未安装，跳过所有 MCP 连接")
            return

        stdio_tasks = []
        remote_servers = []

        for name, cfg in mcp_config.items():
            if not cfg.get("enabled", True):
                continue
            server_type = cfg.get("type", "local")
            if server_type in ("sse", "streamableHttp", "streamable_http", "http"):
                remote_servers.append((name, cfg))
            else:
                stdio_tasks.append(self.connect_server(name, cfg))

        if stdio_tasks:
            await asyncio.gather(*stdio_tasks, return_exceptions=True)

        for name, cfg in remote_servers:
            await self.connect_server(name, cfg)

    async def connect_server(self, name: str, cfg: dict):
        """连接单个 MCP Server"""
        if not MCP_AVAILABLE:
            return

        info = MCPServerInfo(name)
        self.servers[name] = info
        server_type = cfg.get("type", "local")

        try:
            if server_type in ("sse",):
                await self._connect_sse(name, cfg, info)
            elif server_type in ("streamableHttp", "streamable_http", "http"):
                await self._connect_streamable_http(name, cfg, info)
            else:
                await self._connect_stdio(name, cfg, info)

            logger_mcp.info(f"MCP [{name}] 已连接 ({server_type})，{len(info.tools)} 个工具")

        except asyncio.TimeoutError:
            info.error = "连接超时"
            logger_mcp.error(f"MCP [{name}] 连接超时")
            await self._cleanup_remote(info)
        except FileNotFoundError as e:
            info.error = f"命令未找到: {e}"
            logger_mcp.error(f"MCP [{name}] {info.error}")
        except BaseException as e:
            if isinstance(e, BaseExceptionGroup):
                msgs = [f"{type(se).__name__}: {se}" for se in e.exceptions]
                info.error = "; ".join(msgs)
            else:
                info.error = f"{type(e).__name__}: {e}"
            logger_mcp.error(f"MCP [{name}] 连接失败: {info.error}")
            await self._cleanup_remote(info)

    @staticmethod
    async def _cleanup_remote(info: MCPServerInfo):
        if info._exit_stack is not None:
            try:
                await info._exit_stack.aclose()
            except (Exception, BaseException):
                pass
            info._exit_stack = None

    async def _connect_stdio(self, name: str, cfg: dict, info: MCPServerInfo):
        command = cfg.get("command", [])
        if isinstance(command, str):
            command = [command]
        args = cfg.get("args", [])
        full_command = command + args
        if not full_command:
            info.error = "未配置 command"
            return

        custom_env = cfg.get("environment", {})
        merged_env = {**os.environ, **custom_env} if custom_env else None
        cwd = cfg.get("cwd", self._project_root or None)

        server_params = StdioServerParameters(
            command=full_command[0],
            args=full_command[1:] if len(full_command) > 1 else [],
            env=merged_env,
            cwd=cwd,
        )

        errlog = self.errlog if self.errlog and not self.errlog.closed else sys.stderr
        transport = stdio_client(server_params, errlog=errlog)
        streams = await self._stdio_exit_stack.enter_async_context(transport)
        session = ClientSession(*streams)
        await self._stdio_exit_stack.enter_async_context(session)

        init_timeout = cfg.get("init_timeout", 60)
        await asyncio.wait_for(session.initialize(), timeout=init_timeout)

        tools_result = await asyncio.wait_for(session.list_tools(), timeout=30)
        info.session = session
        info.tools = tools_result.tools if tools_result.tools else []
        info.connected = True

    async def _connect_sse(self, name: str, cfg: dict, info: MCPServerInfo):
        if not SSE_AVAILABLE:
            info.error = "mcp SSE 客户端不可用，请升级: pip install mcp[sse]"
            return

        url = cfg.get("url", "")
        if not url:
            info.error = "SSE 类型需要配置 url"
            return

        headers = cfg.get("headers", {})
        exit_stack = contextlib.AsyncExitStack()
        info._exit_stack = exit_stack

        transport = sse_client(url=url, headers=headers)
        streams = await exit_stack.enter_async_context(transport)
        session = ClientSession(*streams)
        await exit_stack.enter_async_context(session)

        init_timeout = cfg.get("init_timeout", 30)
        await asyncio.wait_for(session.initialize(), timeout=init_timeout)

        tools_result = await asyncio.wait_for(session.list_tools(), timeout=30)
        info.session = session
        info.tools = tools_result.tools if tools_result.tools else []
        info.connected = True

    async def _connect_streamable_http(self, name: str, cfg: dict, info: MCPServerInfo):
        if not STREAMABLE_HTTP_AVAILABLE:
            info.error = "mcp Streamable HTTP 客户端不可用，请升级: pip install mcp"
            return

        url = cfg.get("url", "") or cfg.get("baseUrl", "")
        if not url:
            info.error = "streamableHttp 类型需要配置 url 或 baseUrl"
            return

        headers = cfg.get("headers", {})
        exit_stack = contextlib.AsyncExitStack()
        info._exit_stack = exit_stack

        transport = streamablehttp_client(url=url, headers=headers)
        streams = await exit_stack.enter_async_context(transport)
        read_stream, write_stream = streams[0], streams[1]
        session = ClientSession(read_stream, write_stream)
        await exit_stack.enter_async_context(session)

        init_timeout = cfg.get("init_timeout", 30)
        await asyncio.wait_for(session.initialize(), timeout=init_timeout)

        tools_result = await asyncio.wait_for(session.list_tools(), timeout=30)
        info.session = session
        info.tools = tools_result.tools if tools_result.tools else []
        info.connected = True

    async def disconnect_all(self):
        try:
            await self._stdio_exit_stack.aclose()
        except (Exception, BaseException):
            pass
        self._stdio_exit_stack = contextlib.AsyncExitStack()

        for info in self.servers.values():
            if info._exit_stack is not None:
                try:
                    await info._exit_stack.aclose()
                except (Exception, BaseException):
                    pass
                info._exit_stack = None

        self.servers.clear()

    def toggle_server(self, name: str) -> bool:
        """切换 MCP Server 启用/禁用，返回 True=已启用"""
        if self._allowed_servers is None:
            all_names = set(self.servers.keys())
            self._allowed_servers = all_names - {name}
            return False
        if name in self._allowed_servers:
            self._allowed_servers.discard(name)
            return False
        self._allowed_servers.add(name)
        return True

    def is_server_enabled(self, name: str) -> bool:
        return self._allowed_servers is None or name in self._allowed_servers

    def set_allowed_servers(self, names: list):
        self._allowed_servers = set(names) if names is not None else None

    def get_all_tools_openai_format(self) -> List[dict]:
        tools = []
        for server_name, info in self.servers.items():
            if not info.connected or (self._allowed_servers is not None and server_name not in self._allowed_servers):
                continue
            for t in info.tools:
                input_schema = {}
                if hasattr(t, 'inputSchema') and t.inputSchema:
                    input_schema = t.inputSchema
                elif hasattr(t, 'input_schema') and t.input_schema:
                    input_schema = t.input_schema

                tools.append({
                    "type": "function",
                    "function": {
                        "name": f"mcp__{server_name}__{t.name}",
                        "description": f"[MCP:{server_name}] {t.description or t.name}",
                        "parameters": input_schema,
                    },
                })
        return tools

    def get_tool_info_list(self) -> List[dict]:
        """返回所有已连接 server 的工具（含禁用的，用于 UI 显示）"""
        result = []
        for server_name, info in self.servers.items():
            if not info.connected:
                continue
            for t in info.tools:
                result.append({
                    "name": t.name,
                    "server": server_name,
                    "description": t.description or "",
                })
        return result

    def get_server_status(self) -> List[dict]:
        result = []
        seen = set()
        for name, info in self.servers.items():
            seen.add(name)
            result.append({
                "name": name,
                "connected": info.connected,
                "tools_count": len(info.tools),
                "error": info.error,
                "disabled": self._allowed_servers is not None and name not in self._allowed_servers,
                "config_disabled": False,
            })
        for name, cfg in self._all_configs.items():
            if name not in seen and not cfg.get("enabled", True):
                result.append({
                    "name": name,
                    "connected": False,
                    "tools_count": 0,
                    "error": "",
                    "disabled": False,
                    "config_disabled": True,
                })
        return result

    async def call_tool(self, full_tool_name: str, arguments: dict) -> str:
        """调用 MCP 工具。full_tool_name 格式: mcp__{server}__{tool}"""
        parts = full_tool_name.split("__", 2)
        if len(parts) != 3 or parts[0] != "mcp":
            return f"[错误] 无效的 MCP 工具名: {full_tool_name}"

        server_name = parts[1]
        tool_name = parts[2]

        if self._allowed_servers is not None and server_name not in self._allowed_servers:
            return f"[已拦截] MCP Server '{server_name}' 不在允许列表中"

        info = self.servers.get(server_name)
        if not info:
            return f"[错误] MCP Server '{server_name}' 未找到"

        cfg = self._all_configs.get(server_name, {})
        server_type = cfg.get("type", "local")
        is_remote = server_type in ("sse", "streamableHttp", "streamable_http", "http")

        for attempt in range(2):
            if not info.connected or not info.session:
                if attempt > 0:
                    return f"[错误] MCP Server '{server_name}' 未连接"
                if is_remote:
                    logger_mcp.info(f"MCP [{server_name}] 断线重连...")
                    await info.reconnect(self, cfg)
                    info = self.servers.get(server_name) or info
                    if not info.connected:
                        return f"[错误] MCP Server '{server_name}' 重连失败: {info.error}"
                else:
                    return f"[错误] MCP Server '{server_name}' 未连接"

            try:
                result = await asyncio.wait_for(
                    info.session.call_tool(tool_name, arguments=arguments),
                    timeout=60,
                )

                texts = []
                for item in result.content:
                    if hasattr(item, 'text'):
                        texts.append(item.text)
                    elif hasattr(item, 'data'):
                        texts.append(str(item.data))
                    else:
                        texts.append(str(item))

                return "\n".join(texts) if texts else "(空结果)"

            except asyncio.TimeoutError:
                return f"[超时] MCP 工具 {tool_name} 执行超时(60s)"
            except Exception as e:
                if attempt == 0 and is_remote:
                    info.connected = False
                    logger_mcp.warning(f"MCP [{server_name}] 连接断开 ({type(e).__name__})，尝试重连")
                    continue
                return f"[错误] MCP 工具调用失败: {type(e).__name__}: {e}"

        return f"[错误] MCP 工具 {tool_name} 调用失败（重连后仍失败）"

    def is_mcp_tool(self, tool_name: str) -> bool:
        return tool_name.startswith("mcp__")

`````

--- **end of file: nb_agent/mcp/client.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/mcp/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/mcp/__init__.py`

#### 📦 Imports

- `from client import MCPManager`


---

`````python
from .client import MCPManager  # noqa: F401

`````

--- **end of file: nb_agent/mcp/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/session/models.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/session/models.py`

#### 📝 Module Docstring

`````
SQLModel 数据模型 — 会话、消息、Agent 配置
`````

#### 📦 Imports

- `from typing import Optional`
- `from sqlmodel import SQLModel`
- `from sqlmodel import Field`

#### 🏛️ Classes (3)

##### 📌 `class ChatSession(SQLModel)`
*Line: 7*

**Class Variables (7):**
- `__tablename__ = 'sessions'`
- `id: str = Field(primary_key=True)`
- `title: str = Field(default='')`
- `model_id: str = Field(default='')`
- `agent_id: str = Field(default='__default__')`
- `created_at: str = Field(default='')`
- `updated_at: str = Field(default='')`

##### 📌 `class Message(SQLModel)`
*Line: 18*

**Class Variables (8):**
- `__tablename__ = 'messages'`
- `id: Optional[int] = Field(default=None, primary_key=True)`
- `session_id: str = Field(index=True)`
- `role: str = Field(default='')`
- `content: str = Field(default='')`
- `reasoning: str = Field(default='')`
- `tool_calls_json: str = Field(default='[]')`
- `created_at: str = Field(default='')`

##### 📌 `class AgentConfig(SQLModel)`
*Line: 30*

**Class Variables (11):**
- `__tablename__ = 'agent_configs'`
- `id: str = Field(primary_key=True)`
- `name: str = Field(default='')`
- `system_prompt: str = Field(default='')`
- `default_model: str = Field(default='')`
- `allowed_tool_groups_json: str = Field(default='null')`
- `allowed_mcp_servers_json: str = Field(default='null')`
- `allowed_skills_json: str = Field(default='null')`
- `is_builtin: bool = Field(default=False)`
- `created_at: str = Field(default='')`
- `updated_at: str = Field(default='')`


---

`````python
"""SQLModel 数据模型 — 会话、消息、Agent 配置"""

from typing import Optional
from sqlmodel import SQLModel, Field


class ChatSession(SQLModel, table=True):
    __tablename__ = "sessions"

    id: str = Field(primary_key=True)
    title: str = Field(default="")
    model_id: str = Field(default="")
    agent_id: str = Field(default="__default__")
    created_at: str = Field(default="")
    updated_at: str = Field(default="")


class Message(SQLModel, table=True):
    __tablename__ = "messages"

    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: str = Field(index=True)
    role: str = Field(default="")
    content: str = Field(default="")
    reasoning: str = Field(default="")
    tool_calls_json: str = Field(default="[]")
    created_at: str = Field(default="")


class AgentConfig(SQLModel, table=True):
    __tablename__ = "agent_configs"

    id: str = Field(primary_key=True)
    name: str = Field(default="")
    system_prompt: str = Field(default="")
    default_model: str = Field(default="")
    allowed_tool_groups_json: str = Field(default="null")
    allowed_mcp_servers_json: str = Field(default="null")
    allowed_skills_json: str = Field(default="null")
    is_builtin: bool = Field(default=False)
    created_at: str = Field(default="")
    updated_at: str = Field(default="")

`````

--- **end of file: nb_agent/session/models.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/session/store.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/session/store.py`

#### 📝 Module Docstring

`````
会话持久化 — SQLModel ORM，默认 SQLite，可切换 PostgreSQL
`````

#### 📦 Imports

- `import json`
- `import os`
- `import datetime`
- `from pathlib import Path`
- `from typing import List`
- `from typing import Dict`
- `from typing import Optional`
- `from sqlmodel import SQLModel`
- `from sqlmodel import Session`
- `from sqlmodel import create_engine`
- `from sqlmodel import select`
- `from sqlmodel import text`
- `from models import ChatSession`
- `from models import Message`
- `from models import AgentConfig`

#### 🏛️ Classes (1)

##### 📌 `class SessionStore`
*Line: 14*

**🔧 Constructor (`__init__`):**
- `def __init__(self, db_path: str = '')`
  - **Parameters:**
    - `self`
    - `db_path: str = ''`

**Public Methods (13):**
- `def create_session(self, session_id: str, title: str = '', model_id: str = '', agent_id: str = '__default__') -> str`
- `def get_session_title(self, session_id: str) -> str`
- `def get_session(self, session_id: str) -> Optional[dict]`
- `def update_session_title(self, session_id: str, title: str)`
- `def list_sessions(self, limit: int = 50) -> List[dict]`
- `def save_message(self, session_id: str, role: str, content: str, reasoning: str = '', tool_calls: Optional[list] = None)`
- `def get_messages(self, session_id: str) -> List[Dict]`
- `def delete_session(self, session_id: str)`
- `def create_agent(self, agent_id: str, name: str, system_prompt: str, default_model: str = '', allowed_tool_groups: list = None, allowed_mcp_servers: list = None, allowed_skills: list = None, is_builtin: bool = False) -> str`
- `def list_agents(self) -> List[dict]`
- `def get_agent(self, agent_id: str) -> Optional[dict]`
- `def update_agent(self, agent_id: str, name: str, system_prompt: str, default_model: str = '', allowed_tool_groups: list = None, allowed_mcp_servers: list = None, allowed_skills: list = None)`
- `def delete_agent(self, agent_id: str)`


---

`````python
"""会话持久化 — SQLModel ORM，默认 SQLite，可切换 PostgreSQL"""

import json
import os
import datetime
from pathlib import Path
from typing import List, Dict, Optional

from sqlmodel import SQLModel, Session, create_engine, select, text

from .models import ChatSession, Message, AgentConfig


class SessionStore:

    def __init__(self, db_path: str = ""):
        if not db_path:
            db_dir = os.path.join(Path.home(), ".nb_agent")
            os.makedirs(db_dir, exist_ok=True)
            db_path = os.path.join(db_dir, "sessions.db")

        db_path = os.path.expanduser(db_path)
        parent = os.path.dirname(db_path)
        if parent:
            os.makedirs(parent, exist_ok=True)

        if db_path.startswith("postgresql"):
            self._url = db_path
        else:
            self._url = f"sqlite:///{db_path}"

        connect_args = {}
        if self._url.startswith("sqlite"):
            connect_args["check_same_thread"] = False

        self._engine = create_engine(self._url, connect_args=connect_args)
        SQLModel.metadata.create_all(self._engine)
        self._run_migrations()

    def _run_migrations(self):
        """数据库迁移：新增字段等，防止旧数据库 schema 不匹配报错"""
        try:
            with self._engine.connect() as conn:
                conn.execute(text("ALTER TABLE agent_configs ADD COLUMN default_model VARCHAR NOT NULL DEFAULT ''"))
                conn.commit()
        except Exception:
            pass

    def _session(self) -> Session:
        return Session(self._engine)

    # ==================== Session ====================

    def create_session(self, session_id: str, title: str = "",
                       model_id: str = "", agent_id: str = "__default__") -> str:
        now = datetime.datetime.now().isoformat()
        with self._session() as s:
            s.add(ChatSession(
                id=session_id, title=title, model_id=model_id,
                agent_id=agent_id, created_at=now, updated_at=now,
            ))
            s.commit()
        return session_id

    def get_session_title(self, session_id: str) -> str:
        with self._session() as s:
            row = s.get(ChatSession, session_id)
            return row.title if row else ""

    def get_session(self, session_id: str) -> Optional[dict]:
        with self._session() as s:
            row = s.get(ChatSession, session_id)
            return row.model_dump() if row else None

    def update_session_title(self, session_id: str, title: str):
        now = datetime.datetime.now().isoformat()
        with self._session() as s:
            row = s.get(ChatSession, session_id)
            if row:
                row.title = title
                row.updated_at = now
                s.add(row)
                s.commit()

    def list_sessions(self, limit: int = 50) -> List[dict]:
        with self._session() as s:
            stmt = select(ChatSession).order_by(ChatSession.updated_at.desc()).limit(limit)
            rows = s.exec(stmt).all()
            return [r.model_dump() for r in rows]

    def save_message(self, session_id: str, role: str, content: str,
                     reasoning: str = "", tool_calls: Optional[list] = None):
        now = datetime.datetime.now().isoformat()
        tc_json = json.dumps(tool_calls or [], ensure_ascii=False)
        with self._session() as s:
            s.add(Message(
                session_id=session_id, role=role, content=content,
                reasoning=reasoning, tool_calls_json=tc_json, created_at=now,
            ))
            row = s.get(ChatSession, session_id)
            if row:
                row.updated_at = now
                s.add(row)
            s.commit()

    def get_messages(self, session_id: str) -> List[Dict]:
        with self._session() as s:
            stmt = (
                select(Message)
                .where(Message.session_id == session_id)
                .order_by(Message.id)
            )
            rows = s.exec(stmt).all()
            return [
                {
                    "role": r.role,
                    "content": r.content,
                    "reasoning": r.reasoning,
                    "tool_calls_json": r.tool_calls_json,
                }
                for r in rows
            ]

    def delete_session(self, session_id: str):
        with self._session() as s:
            stmt = select(Message).where(Message.session_id == session_id)
            for msg in s.exec(stmt).all():
                s.delete(msg)
            row = s.get(ChatSession, session_id)
            if row:
                s.delete(row)
            s.commit()

    # ==================== Agent ====================

    def create_agent(self, agent_id: str, name: str, system_prompt: str,
                     default_model: str = "",
                     allowed_tool_groups: list = None,
                     allowed_mcp_servers: list = None,
                     allowed_skills: list = None,
                     is_builtin: bool = False) -> str:
        now = datetime.datetime.now().isoformat()
        with self._session() as s:
            s.add(AgentConfig(
                id=agent_id, name=name, system_prompt=system_prompt,
                default_model=default_model,
                allowed_tool_groups_json=json.dumps(allowed_tool_groups),
                allowed_mcp_servers_json=json.dumps(allowed_mcp_servers),
                allowed_skills_json=json.dumps(allowed_skills),
                is_builtin=is_builtin,
                created_at=now, updated_at=now,
            ))
            s.commit()
        return agent_id

    @staticmethod
    def _deserialize_agent(d: dict) -> dict:
        for src, dst in [("allowed_tool_groups_json", "allowed_tool_groups"),
                         ("allowed_mcp_servers_json", "allowed_mcp_servers"),
                         ("allowed_skills_json", "allowed_skills")]:
            raw = d.pop(src, "null")
            d[dst] = json.loads(raw) if raw else None
        return d

    def list_agents(self) -> List[dict]:
        with self._session() as s:
            stmt = select(AgentConfig).order_by(AgentConfig.created_at)
            rows = s.exec(stmt).all()
            return [self._deserialize_agent(r.model_dump()) for r in rows]

    def get_agent(self, agent_id: str) -> Optional[dict]:
        with self._session() as s:
            row = s.get(AgentConfig, agent_id)
            if not row:
                return None
            return self._deserialize_agent(row.model_dump())

    def update_agent(self, agent_id: str, name: str, system_prompt: str,
                     default_model: str = "",
                     allowed_tool_groups: list = None,
                     allowed_mcp_servers: list = None,
                     allowed_skills: list = None):
        now = datetime.datetime.now().isoformat()
        with self._session() as s:
            row = s.get(AgentConfig, agent_id)
            if row:
                row.name = name
                row.system_prompt = system_prompt
                row.default_model = default_model
                row.allowed_tool_groups_json = json.dumps(allowed_tool_groups)
                row.allowed_mcp_servers_json = json.dumps(allowed_mcp_servers)
                row.allowed_skills_json = json.dumps(allowed_skills)
                row.updated_at = now
                s.add(row)
                s.commit()

    def delete_agent(self, agent_id: str):
        with self._session() as s:
            row = s.get(AgentConfig, agent_id)
            if row:
                s.delete(row)
                s.commit()

`````

--- **end of file: nb_agent/session/store.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/session/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/session/__init__.py`

#### 📦 Imports

- `from store import SessionStore`


---

`````python
from .store import SessionStore  # noqa: F401

`````

--- **end of file: nb_agent/session/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/skills/manager.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/skills/manager.py`

#### 📝 Module Docstring

`````
SkillManager — 发现、加载与匹配 SKILL.md 技能文档。
`````

#### 📦 Imports

- `from __future__ import annotations`
- `import fnmatch`
- `import re`
- `from dataclasses import dataclass`
- `from pathlib import Path`
- `from typing import Any`
- `import yaml`

#### 🏛️ Classes (2)

##### 📌 `class SkillRecord`
*Line: 27*

**Class Variables (6):**
- `name: str`
- `description: str`
- `paths: tuple[str, ...]`
- `skill_path: Path`
- `source: str`
- `disable_model_invocation: bool = False`

##### 📌 `class SkillManager`
*Line: 128*

**Docstring:**
`````
Manage progressive disclosure of SKILL.md instructions.
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, project_root: Path | None = None)`
  - **Parameters:**
    - `self`
    - `project_root: Path | None = None`

**Public Methods (6):**
- `def discover(self) -> None`
  - *Scan builtin, global, cross-platform, and project skill directories.*
- `def get_manifest(self, allowed_skills: set | None = None) -> list[dict[str, str]]`
  - *Return auto-invocable skills. None=全部允许, set()=全部禁用, {'a','b'}=只允许a和b。*
- `def get_all_skills(self) -> list[dict[str, str]]`
  - *Return all skills including manual-only ones.*
- `def view_skill(self, skill_name: str) -> dict[str, Any]`
  - *Load the full SKILL.md content for a skill.*
- `def match_skills(self, file_paths: list[str]) -> list[str]`
  - *Return skill names whose ``paths`` globs match any given file path.*
- `def get_view_skill_schema(self) -> dict[str, Any]`
  - *Return the OpenAI function schema for the ``view_skill`` tool.*


---

`````python
"""SkillManager — 发现、加载与匹配 SKILL.md 技能文档。"""

from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

_BUILTIN_DIR = Path(__file__).resolve().parent / "builtin"

_GLOBAL_DIRS = [
    Path.home() / ".nb_agent" / "skills",
    Path.home() / ".agents" / "skills",
]

_PROJECT_DIR_NAMES = [
    Path(".nb_agent") / "skills",
    Path(".agents") / "skills",
]


@dataclass(frozen=True)
class SkillRecord:
    name: str
    description: str
    paths: tuple[str, ...]
    skill_path: Path
    source: str
    disable_model_invocation: bool = False


def _split_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Parse YAML frontmatter separated by ``---`` from markdown body."""
    text = content.lstrip("\ufeff")
    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    metadata = yaml.safe_load(parts[1]) or {}
    if not isinstance(metadata, dict):
        metadata = {}
    body = parts[2].lstrip("\n")
    return metadata, body


def _read_frontmatter(skill_path: Path) -> dict[str, Any]:
    try:
        content = skill_path.read_text(encoding="utf-8")
    except OSError:
        return {}
    metadata, _ = _split_frontmatter(content)
    return metadata


def _normalize_paths(raw_paths: Any) -> tuple[str, ...]:
    if raw_paths is None:
        return ()
    if isinstance(raw_paths, str):
        items = [part.strip() for part in raw_paths.split(",")]
    elif isinstance(raw_paths, list):
        items = [str(part).strip() for part in raw_paths]
    else:
        return ()
    return tuple(item for item in items if item)


def _glob_to_regex(pattern: str) -> re.Pattern[str]:
    normalized = pattern.replace("\\", "/")
    parts: list[str] = []
    i = 0
    while i < len(normalized):
        char = normalized[i]
        if char == "*":
            if i + 1 < len(normalized) and normalized[i + 1] == "*":
                parts.append(".*")
                i += 2
                if i < len(normalized) and normalized[i] == "/":
                    i += 1
                continue
            parts.append("[^/]*")
            i += 1
            continue
        if char == "?":
            parts.append("[^/]")
        else:
            parts.append(re.escape(char))
        i += 1
    return re.compile(f"^{''.join(parts)}$")


def _path_matches_glob(file_path: str, pattern: str) -> bool:
    normalized_path = file_path.replace("\\", "/").lstrip("./")
    normalized_pattern = pattern.replace("\\", "/").lstrip("./")
    if not normalized_path or not normalized_pattern:
        return False

    path = Path(normalized_path)
    if path.match(normalized_pattern):
        return True

    if normalized_pattern.startswith("**/"):
        suffix = normalized_pattern[3:]
        if fnmatch.fnmatch(path.name, suffix):
            return True

    if "**" in normalized_pattern or "/" in normalized_pattern:
        return bool(_glob_to_regex(normalized_pattern).fullmatch(normalized_path))

    return fnmatch.fnmatch(path.name, normalized_pattern) or fnmatch.fnmatch(
        normalized_path,
        normalized_pattern,
    )


def _iter_skill_files(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted(path for path in root.glob("*/SKILL.md") if path.is_file())


class SkillManager:
    """Manage progressive disclosure of SKILL.md instructions."""

    def __init__(self, project_root: Path | None = None) -> None:
        self._project_root = project_root or Path.cwd()
        self._skills: dict[str, SkillRecord] = {}

    def discover(self) -> None:
        """Scan builtin, global, cross-platform, and project skill directories."""
        discovered: dict[str, SkillRecord] = {}

        scan_targets: list[tuple[str, Path]] = [("builtin", _BUILTIN_DIR)]
        for gdir in _GLOBAL_DIRS:
            scan_targets.append(("global", gdir))
        for pdir_name in _PROJECT_DIR_NAMES:
            scan_targets.append(("project", self._project_root / pdir_name))

        for source, root in scan_targets:
            for skill_path in _iter_skill_files(root):
                metadata = _read_frontmatter(skill_path)
                name = metadata.get("name")
                if not isinstance(name, str) or not name.strip():
                    continue

                description = metadata.get("description", "")
                if not isinstance(description, str):
                    description = str(description)

                dmi = metadata.get("disable-model-invocation", False)
                if not isinstance(dmi, bool):
                    dmi = str(dmi).lower() in ("true", "1", "yes")

                record = SkillRecord(
                    name=name.strip(),
                    description=description.strip(),
                    paths=_normalize_paths(metadata.get("paths")),
                    skill_path=skill_path,
                    source=source,
                    disable_model_invocation=dmi,
                )
                discovered[record.name] = record

        self._skills = discovered

    def get_manifest(self, allowed_skills: set | None = None) -> list[dict[str, str]]:
        """Return auto-invocable skills. None=全部允许, set()=全部禁用, {'a','b'}=只允许a和b。"""
        return [
            {"name": record.name, "description": record.description}
            for record in sorted(self._skills.values(), key=lambda item: item.name)
            if not record.disable_model_invocation
            and (allowed_skills is None or record.name in allowed_skills)
        ]

    def get_all_skills(self) -> list[dict[str, str]]:
        """Return all skills including manual-only ones."""
        return [
            {
                "name": record.name,
                "description": record.description,
                "manual_only": record.disable_model_invocation,
            }
            for record in sorted(self._skills.values(), key=lambda item: item.name)
        ]

    def view_skill(self, skill_name: str) -> dict[str, Any]:
        """Load the full SKILL.md content for a skill."""
        record = self._skills.get(skill_name)
        if record is None:
            return {
                "success": False,
                "error": f"Skill '{skill_name}' not found.",
                "available_skills": sorted(self._skills),
            }

        try:
            raw_content = record.skill_path.read_text(encoding="utf-8")
        except OSError as exc:
            return {
                "success": False,
                "error": f"Failed to read skill '{skill_name}': {exc}",
            }

        metadata, body = _split_frontmatter(raw_content)
        return {
            "success": True,
            "name": record.name,
            "description": record.description,
            "paths": list(record.paths),
            "source": record.source,
            "skill_path": str(record.skill_path),
            "content": body.strip(),
            "raw_content": raw_content,
            "metadata": metadata,
        }

    def match_skills(self, file_paths: list[str]) -> list[str]:
        """Return skill names whose ``paths`` globs match any given file path."""
        if not file_paths:
            return []

        matched: list[str] = []
        for record in sorted(self._skills.values(), key=lambda item: item.name):
            if not record.paths:
                continue
            if any(
                _path_matches_glob(file_path, pattern)
                for file_path in file_paths
                for pattern in record.paths
            ):
                matched.append(record.name)
        return matched

    def get_view_skill_schema(self) -> dict[str, Any]:
        """Return the OpenAI function schema for the ``view_skill`` tool."""
        return {
            "type": "function",
            "function": {
                "name": "view_skill",
                "description": (
                    "Load the full instructions for a skill by name. "
                    "Use this when a task matches a skill listed in the manifest."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "skill_name": {
                            "type": "string",
                            "description": "The skill name from the manifest.",
                        }
                    },
                    "required": ["skill_name"],
                },
            },
        }

`````

--- **end of file: nb_agent/skills/manager.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/skills/README.md** (project: nb_agent) --- 

`````markdown
# Skills 系统

nb_agent 的 Skills 系统遵循 **[Agent Skills 开放规范](https://agentskills.io)**。

该规范由 Anthropic 创建并发布为开放标准，已被 26+ 平台采用（Claude、OpenAI Codex、Gemini CLI、GitHub Copilot、Cursor、VS Code 等）。

## 什么是 Skill？

Skill 是一份 Markdown 格式的操作指南，告诉 AI 在特定任务中如何一步步执行。每个 Skill 是一个包含 `SKILL.md` 文件的文件夹。

## SKILL.md 格式

文件使用 YAML Front Matter 定义元数据，后接 Markdown 正文：

```markdown
---
name: my-skill
description: 简短描述这个 Skill 的用途和触发时机
---

# Skill 标题

具体的操作步骤和指南...
```

### Front Matter 字段（agentskills.io 规范）

| 字段 | 必填 | 说明 |
|---|---|---|
| `name` | 是 | 1-64 字符，小写字母+数字+连字符，不能以连字符开头或结尾，不能有连续连字符，**必须与文件夹名一致** |
| `description` | 是 | 1-1024 字符，描述 Skill 做什么 + 什么时候用，应包含触发关键词 |
| `license` | 否 | 许可证名称或引用打包的许可证文件（如 `Apache-2.0`） |
| `compatibility` | 否 | 1-500 字符，环境要求（目标产品、系统依赖、网络访问等） |
| `metadata` | 否 | 任意键值对映射，用于自定义扩展属性（如 `author`、`version`） |
| `allowed-tools` | 否 | 空格分隔的预授权工具列表（实验性，如 `Bash(git:*) Read`） |

以下为 nb_agent 扩展字段（非 agentskills.io 规范）：

| 字段 | 必填 | 说明 |
|---|---|---|
| `paths` | 否 | 文件路径 glob 匹配模式，限定 Skill 的作用域 |
| `disable-model-invocation` | 否 | 设为 `true` 则 AI 不会自动触发，只能手动调用 |

### 完整示例

```markdown
---
name: pdf-processing
description: >-
  提取 PDF 文本、填写 PDF 表单、合并多个 PDF。
  当用户提到 PDF、表单、文档提取时使用。
license: Apache-2.0
compatibility: Requires Python 3.10+ and poppler-utils
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(python3:*) Read Write
---

# PDF 处理 Skill

具体的操作步骤...
```

## 渐进式披露（Progressive Disclosure）

Agent Skills 规范的核心设计模式：

1. **Discovery（发现）**：启动时只加载 `name` + `description`，注入到 system prompt 的 Skills 清单中
2. **Activation（激活）**：当任务匹配某个 Skill 时，AI 调用 `view_skill()` 工具加载完整 SKILL.md 内容
3. **Execution（执行）**：AI 按照指南步骤执行任务，按需加载 scripts/、references/ 等资源

这样既节省 Context Window（token），又不丢失功能。

## Skill 存放位置

| 来源 | 路径 | 说明 |
|---|---|---|
| 内置 | `nb_agent/skills/builtin/` | 随 nb_agent 安装 |
| 全局 | `~/.nb_agent/skills/` 或 `~/.agents/skills/` | 用户级，所有项目共享 |
| 项目 | `<project>/.nb_agent/skills/` 或 `<project>/.agents/skills/` | 项目级，跟随项目 |

## 创建 Skill

```
my-skill/                 ← 文件夹名
├── SKILL.md              # 必需：元数据 + 操作指南
├── scripts/              # 可选：可执行脚本
├── references/           # 可选：参考文档
└── assets/               # 可选：模板、资源文件
```

1. 在上述任一目录下创建子文件夹（如 `my-skill/`）
2. 在子文件夹中创建 `SKILL.md` 文件
3. **`name` 字段必须与文件夹名一致**（如文件夹叫 `my-skill`，则 `name: my-skill`）
4. 重启 nb_agent 即可发现新 Skill

## 相关链接

- [Agent Skills 官网](https://agentskills.io)
- [Agent Skills 规范](https://agentskills.io/specification)
- [GitHub 仓库](https://github.com/agentskills/agentskills)
- [示例 Skills](https://github.com/anthropics/skills)

`````

--- **end of file: nb_agent/skills/README.md** (project: nb_agent) --- 

---


--- **start of file: nb_agent/skills/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/skills/__init__.py`

#### 📝 Module Docstring

`````
Skills 系统 — 渐进式披露 SKILL.md 指令。
`````

#### 📦 Imports

- `from manager import SkillManager`


---

`````python
"""Skills 系统 — 渐进式披露 SKILL.md 指令。"""

from .manager import SkillManager

__all__ = ["SkillManager"]

`````

--- **end of file: nb_agent/skills/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tools/base.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tools/base.py`

#### 📝 Module Docstring

`````
工具注册框架 — 基于 Pydantic + 装饰器自动生成 OpenAI Function Calling Schema

用法:
    from nb_agent.tools import tool

    class MyParams(BaseModel):
        query: str = Field(description="搜索关键词")

    # 无分组
    @tool
    def search(params: MyParams) -> str:
        """搜索互联网"""
        ...

    # 有分组 — 注册名变为 file__read_file
    @tool(group="file")
    def read_file(params: ReadParams) -> str:
        """读取文件"""
        ...
`````

#### 📦 Imports

- `import inspect`
- `from typing import Dict`
- `from typing import Callable`
- `from typing import Optional`
- `from typing import Type`
- `from typing import get_type_hints`
- `from pydantic import BaseModel`

#### 🔧 Public Functions (2)

- `def tool(func = None)`
  - *Line: 131*
  - **Docstring:**
  `````
  装饰器：自动注册工具函数到 TOOL_REGISTRY
  
  用法:
      @tool                          # 无分组，注册名 = func_name
      @tool(group="file")            # 有分组，注册名 = file__func_name
  `````

- `def decorator(fn)`
  - *Line: 140*


---

`````python
"""
工具注册框架 — 基于 Pydantic + 装饰器自动生成 OpenAI Function Calling Schema

用法:
    from nb_agent.tools import tool

    class MyParams(BaseModel):
        query: str = Field(description="搜索关键词")

    # 无分组
    @tool
    def search(params: MyParams) -> str:
        \"\"\"搜索互联网\"\"\"
        ...

    # 有分组 — 注册名变为 file__read_file
    @tool(group="file")
    def read_file(params: ReadParams) -> str:
        \"\"\"读取文件\"\"\"
        ...
"""

import inspect
from typing import Dict, Callable, Optional, Type, get_type_hints

from pydantic import BaseModel


TOOL_REGISTRY: Dict[str, dict] = {}


def _pydantic_schema_to_openai_params(model_cls: Type[BaseModel]) -> dict:
    """将 Pydantic model 的 JSON Schema 转换为 OpenAI function parameters 格式"""
    raw_schema = model_cls.model_json_schema()

    properties = {}
    required = []

    for name, field_schema in raw_schema.get("properties", {}).items():
        prop = {}
        field_type = field_schema.get("type")
        if field_type:
            prop["type"] = field_type
            if field_type == "array" and "items" in field_schema:
                prop["items"] = field_schema["items"]
        else:
            prop["type"] = "string"

        if "description" in field_schema:
            prop["description"] = field_schema["description"]

        if "anyOf" in field_schema:
            for variant in field_schema["anyOf"]:
                vtype = variant.get("type")
                if vtype and vtype != "null":
                    prop["type"] = vtype
                    if vtype == "array" and "items" in variant:
                        prop["items"] = variant["items"]
                    break

        if "enum" in field_schema:
            prop["enum"] = field_schema["enum"]

        if "default" in field_schema:
            prop["default"] = field_schema["default"]

        properties[name] = prop

    for name in raw_schema.get("required", []):
        required.append(name)

    return {
        "type": "object",
        "properties": properties,
        "required": required,
    }


def _find_model_cls(func: Callable) -> Optional[Type[BaseModel]]:
    """从函数签名中查找 Pydantic BaseModel 参数类型"""
    try:
        hints = get_type_hints(func)
    except Exception:
        hints = {}

    sig = inspect.signature(func)
    for param_name, param in sig.parameters.items():
        annotation = hints.get(param_name, param.annotation)
        if annotation is inspect.Parameter.empty:
            continue
        if isinstance(annotation, type) and issubclass(annotation, BaseModel):
            return annotation
    return None


def _register_tool(func: Callable, group: Optional[str] = None) -> Callable:
    """核心注册逻辑：解析函数签名，生成 schema，写入 TOOL_REGISTRY"""
    model_cls = _find_model_cls(func)
    if model_cls is None:
        raise TypeError(
            f"工具函数 '{func.__name__}' 必须有一个 Pydantic BaseModel 参数。"
            f"示例: def my_tool(params: MyParams) -> str: ..."
        )

    description = (func.__doc__ or "").strip()
    if not description:
        raise ValueError(f"工具函数 '{func.__name__}' 必须有 docstring 作为工具描述")

    openai_params = _pydantic_schema_to_openai_params(model_cls)
    func_name = func.__name__
    tool_name = f"{group}__{func_name}" if group else func_name

    TOOL_REGISTRY[tool_name] = {
        "function": func,
        "model_cls": model_cls,
        "group": group or "",
        "func_name": func_name,
        "schema": {
            "type": "function",
            "function": {
                "name": tool_name,
                "description": description,
                "parameters": openai_params,
            },
        },
    }

    return func


def tool(func=None, *, group=None):
    """装饰器：自动注册工具函数到 TOOL_REGISTRY

    用法:
        @tool                          # 无分组，注册名 = func_name
        @tool(group="file")            # 有分组，注册名 = file__func_name
    """
    if func is not None:
        return _register_tool(func)
    def decorator(fn):
        return _register_tool(fn, group=group)
    return decorator

`````

--- **end of file: nb_agent/tools/base.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tools/builtin.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tools/builtin.py`

#### 📝 Module Docstring

`````
内置工具 — 框架必需的核心工具
`````

#### 📦 Imports

- `import datetime`
- `from pydantic import BaseModel`
- `from pydantic import Field`
- `from base import tool`
- `from zoneinfo import ZoneInfo`

#### 🏛️ Classes (1)

##### 📌 `class GetCurrentTimeParams(BaseModel)`
*Line: 12*

**Class Variables (1):**
- `timezone: str = Field(default='Asia/Shanghai', description='时区，默认 Asia/Shanghai')`

#### 🔧 Public Functions (1)

- `def get_current_time(params: GetCurrentTimeParams) -> str` `tool(group='nb_agent_builtin')`
  - *Line: 17*
  - *获取当前日期和时间*


---

`````python
"""内置工具 — 框架必需的核心工具"""

import datetime

from pydantic import BaseModel, Field

from .base import tool

from zoneinfo import ZoneInfo


class GetCurrentTimeParams(BaseModel):
    timezone: str = Field(default="Asia/Shanghai", description="时区，默认 Asia/Shanghai")


@tool(group="nb_agent_builtin")
def get_current_time(params: GetCurrentTimeParams) -> str:
    """获取当前日期和时间"""
    try:
        tz = ZoneInfo(params.timezone)
    except (KeyError, Exception):
        tz = ZoneInfo("Asia/Shanghai")
    now = datetime.datetime.now(tz)
    return now.strftime(f"%Y-%m-%d %H:%M:%S ({now.strftime('%A')}) [{params.timezone}]")

`````

--- **end of file: nb_agent/tools/builtin.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tools/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tools/__init__.py`

#### 📝 Module Docstring

`````
工具模块 — 导入所有工具以触发 @tool 注册，导出 TOOL_REGISTRY
`````

#### 📦 Imports

- `from base import TOOL_REGISTRY`
- `from base import tool`
- `import nb_agent.tools.builtin`


---

`````python
"""工具模块 — 导入所有工具以触发 @tool 注册，导出 TOOL_REGISTRY"""

from .base import TOOL_REGISTRY, tool  # noqa: F401

import nb_agent.tools.builtin  # noqa: F401

`````

--- **end of file: nb_agent/tools/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/app.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/app.py`

#### 📝 Module Docstring

`````
TUI 界面 —— 用 Textual 框架构建

布局:
┌─────────────────────────────────────────────────┐
│  nb_agent | deepseek-v4-flash | Tokens: 0       │  ← Header
├──────────────────────────────┬──────────────────-┤
│                              │  已注册工具:      │
│  对话区域（滚动）             │  - get_time      │  ← Main
│                              │  - calculate     │
│  user: 你好                  │                  │
│  model: [流式输出中...]       │  MCP: 未连接      │
│                              │                  │
├──────────────────────────────┴──────────────────-┤
│  > 输入消息...                          [发送]   │  ← Input
│  (Enter=发送, Shift+Enter=换行)                  │
├─────────────────────────────────────────────────┤
│  Tab=模型 | Ctrl+Q=退出 | Ctrl+L=清屏            │  ← Footer
└─────────────────────────────────────────────────┘
`````

#### 📦 Imports

- `import asyncio`
- `import os`
- `import re`
- `import sys`
- `import time`
- `from datetime import datetime`
- `from pathlib import Path`
- `from typing import Optional`
- `from textual.app import App`
- `from textual.app import ComposeResult`
- `from textual.containers import Horizontal`
- `from textual.widgets import Footer`
- `from textual.widgets import Header`
- `from textual.widgets import RichLog`
- `from textual.widgets import Static`
- `from textual.binding import Binding`
- `from textual.screen import ModalScreen`
- `from rich.text import Text`
- `from rich.markdown import Markdown as RichMarkdown`
- `from rich.panel import Panel`
- `from nb_agent.core import AgentCore`
- `from widgets import ChatInput`
- `from widgets import ToolPanel`
- `from widgets import ModelSelectScreen`
- `from widgets import HelpScreen`
- `from widgets import SessionSelectScreen`
- `from widgets import ToolDetailScreen`
- `from widgets import RoundsInputScreen`
- `from widgets import ToolApprovalScreen`
- `from widgets import SkillListScreen`
- `from widgets import SkillContentScreen`
- `from widgets import MentionSelectScreen`
- `from widgets import AgentSelectScreen`
- `from widgets import AgentEditScreen`
- `from widgets import AgentCommands`
- `from widgets.tool_panel import _fmt_tokens`
- `import logging`
- `import json as _json`
- `import nb_log.monkey_sys_std as _std_mod`
- `import nb_log`
- `import nb_log.monkey_print as _print_mod`

#### 🏛️ Classes (1)

##### 📌 `class AgentApp(App)`
*Line: 71*

**Docstring:**
`````
nb_agent TUI 主应用
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, config: dict)`
  - **Parameters:**
    - `self`
    - `config: dict`

**Public Methods (15):**
- `def compose(self) -> ComposeResult`
- `async def on_mount(self)`
- `def action_stop_ai(self)`
- `def action_edit_last(self)`
- `async def action_send_msg(self)`
- `def action_new_session(self)`
- `def action_resume_session(self)`
- `def action_show_help(self)`
- `def action_toggle_input(self)`
- `def action_show_skills(self)`
- `def action_show_agents(self)`
- `def on_chat_input_mention_triggered(self, event: ChatInput.MentionTriggered) -> None`
- `def action_clear_chat(self)`
- `def action_select_model(self)`
- `async def on_unmount(self)`

**Class Variables (4):**
- `TITLE = 'nb_agent'`
- `CSS_PATH = 'styles.tcss'`
- `COMMANDS = App.COMMANDS | {AgentCommands}`
- `BINDINGS = [Binding('ctrl+j', 'send_msg', '发送', show=True, priority=True), Binding('ctrl+k', 'stop_ai', '终止', show=True, priority=True), Binding('ctrl+up', 'edit_last', '编辑上轮', show=True, priority=True), Binding('tab', 'select_model', '模型', show=True, priority=True), Binding('ctrl+n', 'new_session', '新建', show=True, priority=True), Binding('ctrl+r', 'resume_session', '恢复', show=True, priority=True), Binding('ctrl+e', 'toggle_input', '展开', show=True, priority=True), Binding('ctrl+l', 'clear_chat', '清屏', show=True), Binding('f1', 'show_help', '帮助', show=True), Binding('f2', 'show_skills', 'Skills', show=True), Binding('f4', 'show_agents', 'Agents', show=True), Binding('ctrl+q', 'quit', '退出', show=True, priority=True)]`


---

`````python
"""
TUI 界面 —— 用 Textual 框架构建

布局:
┌─────────────────────────────────────────────────┐
│  nb_agent | deepseek-v4-flash | Tokens: 0       │  ← Header
├──────────────────────────────┬──────────────────-┤
│                              │  已注册工具:      │
│  对话区域（滚动）             │  - get_time      │  ← Main
│                              │  - calculate     │
│  user: 你好                  │                  │
│  model: [流式输出中...]       │  MCP: 未连接      │
│                              │                  │
├──────────────────────────────┴──────────────────-┤
│  > 输入消息...                          [发送]   │  ← Input
│  (Enter=发送, Shift+Enter=换行)                  │
├─────────────────────────────────────────────────┤
│  Tab=模型 | Ctrl+Q=退出 | Ctrl+L=清屏            │  ← Footer
└─────────────────────────────────────────────────┘
"""

import asyncio
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Footer, Header, RichLog, Static
from textual.binding import Binding
from textual.screen import ModalScreen
from rich.text import Text
from rich.markdown import Markdown as RichMarkdown
from rich.panel import Panel

from nb_agent.core import AgentCore
from .widgets import (
    ChatInput,
    ToolPanel,
    ModelSelectScreen,
    HelpScreen,
    SessionSelectScreen,
    ToolDetailScreen,
    RoundsInputScreen,
    ToolApprovalScreen,
    SkillListScreen,
    SkillContentScreen,
    MentionSelectScreen,
    AgentSelectScreen,
    AgentEditScreen,
    AgentCommands,
)
from .widgets.tool_panel import _fmt_tokens


_SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
_SPINNER_BIG = ["◐", "◓", "◑", "◒"]
_MARQUEE_BASE = "  ◐  AI 正在回答中，请稍候...  按 Ctrl+K 停止  ✦  "
_RAINBOW_COLORS = [
    "#ff0080", "#ff2060", "#ff4040", "#ff6020",
    "#ff8000", "#ffb000", "#ffff00", "#80ff00",
    "#00ff80", "#00ffff", "#0080ff", "#4040ff",
    "#8000ff", "#c000ff", "#ff00ff", "#ff0080",
]


class AgentApp(App):
    """nb_agent TUI 主应用"""

    TITLE = "nb_agent"
    CSS_PATH = "styles.tcss"

    COMMANDS = App.COMMANDS | {AgentCommands}

    BINDINGS = [
        Binding("ctrl+j", "send_msg", "发送", show=True, priority=True),
        Binding("ctrl+k", "stop_ai", "终止", show=True, priority=True),
        Binding("ctrl+up", "edit_last", "编辑上轮", show=True, priority=True),
        Binding("tab", "select_model", "模型", show=True, priority=True),
        Binding("ctrl+n", "new_session", "新建", show=True, priority=True),
        Binding("ctrl+r", "resume_session", "恢复", show=True, priority=True),
        Binding("ctrl+e", "toggle_input", "展开", show=True, priority=True),
        Binding("ctrl+l", "clear_chat", "清屏", show=True),
        Binding("f1", "show_help", "帮助", show=True),
        Binding("f2", "show_skills", "Skills", show=True),
        Binding("f4", "show_agents", "Agents", show=True),
        Binding("ctrl+q", "quit", "退出", show=True, priority=True),
    ]

    def __init__(self, config: dict):
        super().__init__()
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        self._tui_log_file = self._open_tui_log()

        self.agent = AgentCore(config)
        self.agent.mcp_manager.errlog = self._tui_log_file
        self.config = config
        self._sending = False
        self._cancel_requested = False
        self._last_ai_reply = ""
        self._show_thinking = True
        self._spinner_idx = 0
        self._marquee_pos = 0
        self._spinner_timer = None
        self._send_start_time: float = 0.0
        self._last_elapsed: float = 0.0

        self.agent.approval_callback = self._request_tool_approval

    @staticmethod
    def _open_tui_log():
        log_dir = Path.home() / ".nb_agent" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        return open(log_dir / "tui_stdout.log", "a", encoding="utf-8")

    def _redirect_all_handlers(self):
        """将所有指向终端的 logging handler 和 nb_log 缓存引用重定向到 TUI 日志文件。

        不动 sys.stdout（Textual 需要它来渲染界面），
        只在 handler 和 nb_log 内部引用层面拦截。
        """
        import logging
        log_file = self._tui_log_file
        log_write = log_file.write

        for logger_obj in [logging.getLogger()] + list(logging.Logger.manager.loggerDict.values()):
            if not isinstance(logger_obj, logging.Logger):
                continue
            for h in logger_obj.handlers:
                if hasattr(h, 'stream') and h.stream in (self._original_stdout, self._original_stderr):
                    h.stream = log_file

        try:
            import nb_log.monkey_sys_std as _std_mod
            _std_mod.stdout_raw = log_write
            _std_mod.stderr_raw = log_write
            import nb_log
            nb_log.stdout_raw = log_write
            nb_log.stderr_raw = log_write
        except (ImportError, AttributeError):
            pass

        try:
            import nb_log.monkey_print as _print_mod
            _print_mod.print_raw = lambda *a, **kw: print(*a, **kw, file=log_file)
        except (ImportError, AttributeError):
            pass

    def _restore_stdio(self):
        if self._tui_log_file and not self._tui_log_file.closed:
            self._tui_log_file.close()

    async def _request_tool_approval(self, tool_name: str, tool_args: dict) -> bool:
        future: asyncio.Future[bool] = asyncio.get_running_loop().create_future()

        def on_result(approved: Optional[bool]) -> None:
            if not future.done():
                future.set_result(bool(approved))

        self.push_screen(ToolApprovalScreen(tool_name, tool_args), on_result)
        return await future

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with Horizontal(id="main-area"):
            yield RichLog(id="chat-panel", wrap=True, markup=True, highlight=True, auto_scroll=True)
            yield ToolPanel(self.agent, id="tool-panel")
        yield ChatInput(id="user-input")
        with Horizontal(id="ai-status-row"):
            yield Static("", id="ai-status-bar")
            yield Static("", id="ai-timer")
        yield Footer()

    async def on_mount(self):
        self._redirect_all_handlers()

        chat = self.query_one("#chat-panel", RichLog)
        model = self.agent.get_model_name()
        total = len(self.agent.available_models)
        chat.write(f"[bold #00d4aa]nb_agent[/bold #00d4aa] | 模型: [bold #4d96ff]{model}[/bold #4d96ff] | 共 [#ffd93d]{total}[/#ffd93d] 个可用模型")
        chat.write("[#6b7394]Enter=换行 | Ctrl+J/Ctrl+Enter=发送 | Tab=切换模型 | @=补全 | Ctrl+P=命令面板 | F1=帮助[/#6b7394]\n")
        self._update_subtitle()
        self.query_one("#user-input", ChatInput).focus()

        mcp_config = self.config.get("mcp", {})
        enabled_count = sum(1 for v in mcp_config.values() if v.get("enabled", True))
        if enabled_count > 0:
            chat.write(f"[#ff922b]⟳ {enabled_count} 个 MCP Server 后台连接中...[/#ff922b]")
            self.run_worker(self._connect_mcp_background(), exclusive=False)

    async def _connect_mcp_background(self):
        await self.agent.connect_mcp()
        chat = self.query_one("#chat-panel", RichLog)
        status = self.agent.get_mcp_status()
        ok = sum(1 for s in status if s["connected"])
        fail = len(status) - ok
        if ok > 0:
            chat.write(f"[#6bcb77]✓ {ok} 个 MCP Server 已连接[/#6bcb77]")
        if fail > 0:
            for s in status:
                if not s["connected"]:
                    chat.write(f"[#ff6b6b]✗ {s['name']}: {s['error']}[/#ff6b6b]")
        self.query_one("#tool-panel", ToolPanel).update_content()

    def _update_subtitle(self):
        agent_name = self.agent.current_agent_name or "默认助手"
        session_title = self.agent.session_store.get_session_title(self.agent.session_id)
        if session_title and session_title != "新会话":
            self.sub_title = f"Agent: {agent_name} | {session_title}"
            self._set_terminal_title(f"nb_agent - {agent_name} - {session_title}")
        else:
            self.sub_title = f"Agent: {agent_name}"
            self._set_terminal_title(f"nb_agent - {agent_name}")

    @staticmethod
    def _set_terminal_title(title: str):
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

    # ─── 思考动画 ───────────────────────────────────────

    def _start_thinking_animation(self) -> None:
        self._spinner_idx = 0
        self._marquee_pos = 0
        if self._spinner_timer is not None:
            self._spinner_timer.stop()
        self._spinner_timer = self.set_interval(0.12, self._tick_spinner)

    def _stop_thinking_animation(self) -> None:
        if self._spinner_timer is not None:
            self._spinner_timer.stop()
            self._spinner_timer = None
        try:
            self.query_one("#ai-status-bar", Static).update("")
            self.query_one("#ai-timer", Static).update("")
        except Exception:
            pass

    def _tick_spinner(self) -> None:
        if not self._sending:
            self._stop_thinking_animation()
            return

        frame = _SPINNER_BIG[self._spinner_idx % len(_SPINNER_BIG)]
        base = f"  {frame}  AI is thinking...  Ctrl+K stop  *  "
        pos = self._marquee_pos % len(base)
        shifted = base[pos:] + base[:pos]
        full = (shifted * 6)[:120]

        marquee = Text()
        color_step = self._spinner_idx * 2
        for i, char in enumerate(full):
            color = _RAINBOW_COLORS[(i + color_step) % len(_RAINBOW_COLORS)]
            marquee.append(char, style=f"bold {color} on #0a0015")

        elapsed = time.monotonic() - self._send_start_time
        if elapsed < 60:
            time_val = f"{elapsed:.1f}s"
        elif elapsed < 3600:
            time_val = f"{int(elapsed // 60)}m{elapsed % 60:.0f}s"
        else:
            time_val = f"{int(elapsed // 3600)}h{int(elapsed % 3600 // 60)}m"

        spin_chars = _SPINNER_FRAMES
        spin = spin_chars[self._spinner_idx % len(spin_chars)]
        pulse = ["#ffd700", "#ff6b00", "#ff0080", "#a855f7", "#00d4ff", "#00ff88", "#ffd700"]
        tc = pulse[self._spinner_idx % len(pulse)]
        timer = Text()
        timer.append(f" {spin} ", style=f"bold {tc} on #0d0020")
        timer.append(f"{time_val} ", style=f"bold {tc} on #0d0020")

        self._spinner_idx += 1
        self._marquee_pos += 2
        try:
            self.query_one("#ai-status-bar", Static).update(marquee)
            self.query_one("#ai-timer", Static).update(timer)
        except Exception:
            pass

    # ─── 消息发送 ───────────────────────────────────────

    async def _do_send(self, user_text: str):
        chat = self.query_one("#chat-panel", RichLog)
        is_first_msg = len([m for m in self.agent.messages if m.get("role") == "user"]) == 0
        self._cancel_requested = False
        self._send_start_time = time.monotonic()
        self._start_thinking_animation()

        chat.write(Panel(
            Text(user_text, style="bold #f0f0f0 on #1a2744", overflow="fold"),
            border_style="bold #00d4ff",
            title="[bold #00d4ff]💎 user[/bold #00d4ff]",
            title_align="left",
            subtitle="[dim #00d4ff]━━━[/dim #00d4ff]",
            subtitle_align="right",
            padding=(0, 1),
        ))
        chat.write(f"[#7c3aed]({self.agent.get_model_name()}) 思考中...[/#7c3aed]")

        skill_context = self._extract_skill_mentions(user_text)
        if skill_context:
            self.agent.messages.append({"role": "system", "content": skill_context})

        try:
            use_stream = self.config.get("agent", {}).get("streaming", True)
            if use_stream:
                await self._handle_stream(user_text, chat)
            else:
                await self._handle_non_stream(user_text, chat)
        except Exception as e:
            chat.write(f"[#ff6b6b]发送失败: {type(e).__name__}: {e}[/#ff6b6b]")
        finally:
            self._stop_thinking_animation()
            self._sending = False
            try:
                self.query_one("#tool-panel", ToolPanel).update_content(last_elapsed=self._last_elapsed)
                self.query_one("#user-input", ChatInput).focus()
            except Exception:
                pass

        if is_first_msg:
            self._update_subtitle()
            self.run_worker(self._generate_title(), exclusive=False)

    async def _generate_title(self):
        try:
            await self.agent.generate_smart_title()
            self._update_subtitle()
        except Exception:
            pass

    def _is_at_bottom(self, chat: RichLog) -> bool:
        return chat.scroll_y >= chat.max_scroll_y - 2

    def _smart_scroll(self, chat: RichLog):
        if self._is_at_bottom(chat):
            chat.scroll_end(animate=False)

    async def _handle_stream(self, user_text: str, chat: RichLog):
        chat.auto_scroll = False
        model_label = self.agent.get_model_name()
        chat.write(f"[bold #4d96ff]🤖 {model_label}[/bold #4d96ff]")
        self._smart_scroll(chat)
        line_buffer = ""
        in_thinking = False
        full_reply_lines = []

        cancelled = False
        async for chunk in self.agent.chat_stream(user_text):
            if self._cancel_requested:
                cancelled = True
                break
            line_buffer += chunk
            await asyncio.sleep(0)

            if "<think>" in line_buffer and not in_thinking:
                in_thinking = True
                line_buffer = line_buffer.replace("<think>", "")
                if self._show_thinking:
                    chat.write("[italic #a78bfa]💭 思考过程:[/italic #a78bfa]")
                    self._smart_scroll(chat)

            if "</think>" in line_buffer and in_thinking:
                in_thinking = False
                before = line_buffer.split("</think>")[0]
                after = line_buffer.split("</think>", 1)[1]
                if self._show_thinking:
                    for line in before.split("\n"):
                        if line.strip():
                            chat.write(Text(line, style="#a78bfa"))
                    chat.write("[italic #7c3aed]── 思考结束 ──[/italic #7c3aed]")
                    self._smart_scroll(chat)
                line_buffer = after.lstrip("\n")
                continue

            while "\n" in line_buffer:
                line, line_buffer = line_buffer.split("\n", 1)
                if in_thinking and not self._show_thinking:
                    continue
                if not line.strip() and in_thinking:
                    continue
                if in_thinking:
                    chat.write(Text(line, style="#a78bfa"))
                elif line.strip():
                    chat.write(Text(line))
                    full_reply_lines.append(line)
                self._smart_scroll(chat)

        if cancelled:
            chat.write("[#ff6b6b]⏹ 已终止回答[/#ff6b6b]")
            self._cancel_requested = False
        else:
            if line_buffer:
                if in_thinking and self._show_thinking:
                    chat.write(Text(line_buffer, style="#a78bfa"))
                elif not in_thinking:
                    chat.write(Text(line_buffer))
                    full_reply_lines.append(line_buffer)

        self._last_ai_reply = "\n".join(full_reply_lines)

        if not cancelled:
            self._redraw_chat()
            chat = self.query_one("#chat-panel", RichLog)

        elapsed = time.monotonic() - self._send_start_time
        self._last_elapsed = elapsed
        t = self.agent.get_token_usage()
        rounds_str = f" | 交互{t['last_rounds']}轮" if t['last_rounds'] > 1 else ""
        tc_str = f" | 工具{t['last_tool_calls']}次" if t['last_tool_calls'] > 0 else ""
        chat.write(f"[#6b7394](本次 入{_fmt_tokens(t['last_prompt'])}+出{_fmt_tokens(t['last_completion'])}={_fmt_tokens(t['last_total'])} | 耗时{elapsed:.1f}s{rounds_str}{tc_str} | 累计 {_fmt_tokens(t['total'])})[/#6b7394]")
        chat.auto_scroll = True
        chat.scroll_end(animate=False)

    async def _handle_non_stream(self, user_text: str, chat: RichLog):
        response = await self.agent.chat(user_text)

        for tc in response.tool_calls:
            chat.write(Panel(
                Text(tc.args, style="#fbbf24", overflow="fold"),
                border_style="#d97706",
                title=f"[bold #fbbf24]🔧 {tc.name}[/bold #fbbf24]",
                title_align="left",
                padding=(0, 1),
            ))
            result = tc.result[:5000] if len(tc.result) > 5000 else tc.result
            chat.write(Panel(
                Text(result, style="#86efac", overflow="fold"),
                border_style="#22c55e",
                title="[bold #86efac]📋 返回结果[/bold #86efac]",
                title_align="left",
                padding=(0, 1),
            ))

        if response.reasoning and self._show_thinking:
            chat.write(Panel(
                Text(response.reasoning, style="italic #a78bfa", overflow="fold"),
                border_style="#7c3aed",
                title="[bold #a78bfa]💭 思考过程[/bold #a78bfa]",
                title_align="left",
                padding=(0, 1),
            ))

        model_label = self.agent.get_model_name()
        chat.write(f"[bold #4d96ff]🤖 {model_label}[/bold #4d96ff]")
        chat.write(RichMarkdown(response.text))
        self._last_ai_reply = response.text
        elapsed = time.monotonic() - self._send_start_time
        self._last_elapsed = elapsed
        t = self.agent.get_token_usage()
        rounds_str = f" | 交互{t['last_rounds']}轮" if t['last_rounds'] > 1 else ""
        tc_str = f" | 工具{t['last_tool_calls']}次" if t['last_tool_calls'] > 0 else ""
        chat.write(f"[#6b7394](本次 入{_fmt_tokens(t['last_prompt'])}+出{_fmt_tokens(t['last_completion'])}={_fmt_tokens(t['last_total'])} | 耗时{elapsed:.1f}s{rounds_str}{tc_str} | 累计 {_fmt_tokens(t['total'])})[/#6b7394]")

    # ─── 快捷键 Actions ────────────────────────────────

    def action_stop_ai(self):
        if isinstance(self.screen, ModalScreen):
            self.screen.dismiss()
            return
        if self._sending:
            self._cancel_requested = True
            self.notify("正在终止 AI 回答...", timeout=2)

    def action_edit_last(self):
        if self._sending:
            self.notify("请等待 AI 回答完成", severity="warning", timeout=2)
            return
        self._edit_last_message()

    async def action_send_msg(self):
        if self._sending:
            return
        input_widget = self.query_one("#user-input", ChatInput)
        user_text = input_widget.text.strip()
        if not user_text:
            return
        input_widget.clear()
        self._sending = True
        self.run_worker(self._do_send(user_text), exclusive=False)

    def action_new_session(self):
        if self._sending:
            self.notify("请等待 AI 回答完成", severity="warning", timeout=2)
            return
        self._cmd_new_session()

    def action_resume_session(self):
        self.push_screen(SessionSelectScreen(self.agent), self._on_session_selected)

    def action_show_help(self):
        self.push_screen(HelpScreen())

    def action_toggle_input(self):
        input_widget = self.query_one("#user-input", ChatInput)
        input_widget.toggle_class("expanded")
        input_widget.focus()

    def action_show_skills(self):
        self.push_screen(SkillListScreen(self.agent), self._on_skill_selected)

    def action_show_agents(self):
        self.push_screen(AgentSelectScreen(self.agent), self._on_agent_selected)

    def _on_agent_selected(self, result: str):
        if not result:
            self.query_one("#user-input", ChatInput).focus()
            return
        if result == "__new__":
            self._cmd_new_agent()
            return
        if result.startswith("__edit__:"):
            self._cmd_edit_agent(result[9:])
            return
        if result.startswith("__copy__:"):
            self._cmd_copy_agent(result[9:])
            return
        if result == self.agent.current_agent_id:
            self.notify("已是当前 Agent", timeout=2)
            self.query_one("#user-input", ChatInput).focus()
            return
        self.agent.apply_agent(result)
        chat = self.query_one("#chat-panel", RichLog)
        chat.clear()
        chat.write(f"[bold #a78bfa]✦ 已应用 Agent: {self.agent.current_agent_name}[/bold #a78bfa]")
        chat.write(f"[#6b7394]System prompt + 工具配置已更新，新会话已创建[/#6b7394]\n")
        self.query_one("#tool-panel", ToolPanel).update_content()
        self._update_subtitle()
        self.query_one("#user-input", ChatInput).focus()

    def _cmd_new_agent(self):
        self.push_screen(
            AgentEditScreen(self.agent),
            self._on_agent_saved,
        )

    def _cmd_edit_agent(self, agent_id: str):
        agents = self.agent.get_agents()
        for a in agents:
            if a["id"] == agent_id:
                self.push_screen(
                    AgentEditScreen(self.agent, edit_agent=a),
                    self._on_agent_saved,
                )
                return

    def _cmd_copy_agent(self, agent_id: str):
        agents = self.agent.get_agents()
        for a in agents:
            if a["id"] == agent_id:
                copy_data = dict(a)
                copy_data["id"] = ""
                copy_data["name"] = f"{a['name']} (副本)"
                copy_data["is_builtin"] = False
                self.push_screen(
                    AgentEditScreen(self.agent, edit_agent=copy_data),
                    self._on_agent_saved,
                )
                return

    def _on_agent_saved(self, result: str):
        if not result:
            self.query_one("#user-input", ChatInput).focus()
            return
        import json as _json
        try:
            data = _json.loads(result)
        except Exception:
            return
        edit_id = data.get("edit_id", "")
        name = data["name"]
        prompt = data["system_prompt"]
        default_model = data.get("default_model", "")
        atg = data.get("allowed_tool_groups")
        ams = data.get("allowed_mcp_servers")
        ask = data.get("allowed_skills")
        if edit_id:
            self.agent.update_agent(edit_id, name, prompt, default_model, atg, ams, ask)
            self.notify(f"已更新 Agent: {name}", timeout=3)
        else:
            self.agent.save_agent(name, prompt, default_model, atg, ams, ask)
            self.notify(f"已创建 Agent: {name}", timeout=3)
        self.query_one("#user-input", ChatInput).focus()

    def on_chat_input_mention_triggered(self, event: ChatInput.MentionTriggered) -> None:
        candidates = self._build_mention_candidates()
        if candidates:
            self.push_screen(MentionSelectScreen(candidates), self._on_mention_selected)

    def _build_mention_candidates(self) -> list:
        candidates = []
        for t in self.agent.get_tools():
            if t["name"] == "view_skill" or t.get("disabled"):
                continue
            candidates.append({
                "name": t["name"],
                "func_name": t.get("func_name", t["name"]),
                "group": t.get("group", ""),
                "description": t["description"],
                "type": "tool",
                "source": t["source"],
            })
        for s in self.agent.skill_manager.get_all_skills():
            candidates.append({
                "name": s["name"],
                "description": s["description"],
                "type": "skill",
                "source": "Skill",
                "manual_only": s.get("manual_only", False),
            })
        return candidates

    def _on_mention_selected(self, prefixed_name: str) -> None:
        input_widget = self.query_one("#user-input", ChatInput)
        if prefixed_name:
            input_widget.insert(prefixed_name + " ")
        input_widget.focus()

    def action_clear_chat(self):
        if self._sending:
            self.notify("请等待 AI 回答完成", severity="warning", timeout=2)
            return
        chat = self.query_one("#chat-panel", RichLog)
        chat.clear()
        self.agent.clear_history()
        chat.write("[#6b7394]对话已清空，上下文已重置[/#6b7394]\n")

    def action_select_model(self):
        self.push_screen(ModelSelectScreen(self.agent), self._on_model_selected)

    async def on_unmount(self):
        await self.agent.disconnect_mcp()
        self._restore_stdio()

    # ─── 命令面板回调 ──────────────────────────────────

    def _cmd_new_session(self):
        chat = self.query_one("#chat-panel", RichLog)
        self.agent.clear_history()
        chat.clear()
        chat.write("[#6b7394]✦ 新会话已创建，上下文已重置[/#6b7394]\n")
        self.query_one("#tool-panel", ToolPanel).update_content()
        self._update_subtitle()

    def _cmd_toggle_thinking(self):
        self._show_thinking = not self._show_thinking
        state = "显示" if self._show_thinking else "隐藏"
        self._redraw_chat()
        self.notify(f"思考过程已{state}", timeout=2)

    def _cmd_export_markdown(self):
        self.push_screen(RoundsInputScreen("导出 Markdown 文件"), self._on_export_rounds)

    def _cmd_copy_markdown(self):
        self.push_screen(RoundsInputScreen("复制为 Markdown"), self._on_copy_rounds)

    # ─── 弹窗回调 ──────────────────────────────────────

    def _on_model_selected(self, model_name):
        if not model_name:
            self.query_one("#user-input", ChatInput).focus()
            return
        old = self.agent.get_model_name()
        if self.agent.switch_model(model_name):
            new = self.agent.get_model_name()
            chat = self.query_one("#chat-panel", RichLog)
            chat.write(f"\n[bold #ffd93d]✦ 模型已切换:[/bold #ffd93d] [#6b7394]{old}[/#6b7394] → [bold #00d4aa]{new}[/bold #00d4aa]")
            self._update_subtitle()
            self.query_one("#tool-panel", ToolPanel).update_content()
        self.query_one("#user-input", ChatInput).focus()

    def _on_skill_selected(self, skill_name):
        if not skill_name:
            self.query_one("#user-input", ChatInput).focus()
            return
        if skill_name.startswith("__apply__:"):
            real_name = skill_name[10:]
            input_widget = self.query_one("#user-input", ChatInput)
            input_widget.insert(f"@skill:{real_name} ")
            input_widget.focus()
            self.notify(f"已插入 @skill:{real_name}，输入消息后发送即可", timeout=3)
            return
        skill_data = self.agent.skill_manager.view_skill(skill_name)
        if skill_data.get("success"):
            self.push_screen(SkillContentScreen(skill_data))
        else:
            self.notify(skill_data.get("error", "加载失败"), severity="warning", timeout=3)
        self.query_one("#user-input", ChatInput).focus()

    def _on_session_selected(self, session_id):
        if not session_id:
            self.query_one("#user-input", ChatInput).focus()
            return
        if session_id == self.agent.session_id:
            self.notify("已是当前会话", timeout=2)
            self.query_one("#user-input", ChatInput).focus()
            return
        sessions = self.agent.get_session_list(20)
        title = ""
        for s in sessions:
            if s["id"] == session_id:
                title = s["title"]
                break
        self.run_worker(self._cmd_resume_session(session_id, title), exclusive=False)
        self.query_one("#user-input", ChatInput).focus()

    async def _cmd_resume_session(self, session_id: str, title: str):
        chat = self.query_one("#chat-panel", RichLog)
        msgs = self.agent.session_store.get_messages(session_id)
        self.agent.session_id = session_id
        self.agent.messages = [{"role": "system", "content": self.agent.system_prompt}]
        for m in msgs:
            self.agent.messages.append({"role": m["role"], "content": m["content"]})
        chat.clear()
        chat.write(f"[#6bcb77]✦ 已恢复会话: {title}[/#6bcb77]")
        for m in msgs:
            if m["role"] == "user":
                chat.write(Panel(
                    Text(m["content"], style="bold #f0f0f0 on #1a2744", overflow="fold"),
                    border_style="bold #00d4ff",
                    title="[bold #00d4ff]💎 user[/bold #00d4ff]",
                    title_align="left",
                    subtitle="[dim #00d4ff]━━━[/dim #00d4ff]",
                    subtitle_align="right",
                    padding=(0, 1),
                ))
            elif m["role"] == "assistant" and m["content"]:
                chat.write("[bold #4d96ff]🤖 AI[/bold #4d96ff]")
                chat.write(RichMarkdown(m["content"]))
        self._update_subtitle()

    def _on_export_rounds(self, rounds):
        if rounds is None or rounds < 0:
            return
        self._export_markdown(rounds)

    def _on_copy_rounds(self, rounds):
        if rounds is None or rounds < 0:
            return
        self._copy_markdown(rounds)

    # ─── 编辑 / 导出 / 复制 ────────────────────────────

    def _edit_last_message(self):
        msgs = self.agent.messages
        last_user_idx = -1
        for i in range(len(msgs) - 1, -1, -1):
            if msgs[i].get("role") == "user":
                last_user_idx = i
                break
        if last_user_idx < 0:
            self.notify("没有可编辑的消息", severity="warning", timeout=2)
            return
        last_user_text = msgs[last_user_idx].get("content", "")
        self.agent.messages = msgs[:last_user_idx]
        input_widget = self.query_one("#user-input", ChatInput)
        input_widget.clear()
        input_widget.insert(last_user_text)
        input_widget.focus()
        self._redraw_chat()
        self.notify("已撤回上轮对话，可编辑后重新发送", timeout=3)

    def _show_tool_details(self):
        self.push_screen(ToolDetailScreen(self.agent))

    def _get_round_messages(self, rounds: int = 0) -> list:
        """获取最近 N 轮对话的消息列表，rounds=0 返回全部"""
        messages = self.agent.messages
        if rounds <= 0:
            return messages
        user_count = 0
        start_idx = 0
        for i in range(len(messages) - 1, -1, -1):
            if messages[i].get("role") == "user":
                user_count += 1
                if user_count == rounds:
                    start_idx = i
                    break
        if user_count < rounds:
            start_idx = 0
        result = [m for m in messages if m.get("role") == "system"]
        result.extend(m for i, m in enumerate(messages) if m.get("role") != "system" and i >= start_idx)
        return result

    def _export_markdown(self, rounds: int = 0):
        messages = self._get_round_messages(rounds)
        session_title = self.agent.session_store.get_session_title(self.agent.session_id) or ""
        display_title = session_title if session_title and session_title != "新会话" else f"会话 {self.agent.session_id[:8]}"
        lines = [f"# {display_title}\n"]
        for msg in messages:
            role = msg.get("role", "")
            content = msg.get("content", "") or ""
            if role == "system":
                continue
            elif role == "user":
                lines.append(f"## 用户\n\n{content}\n")
            elif role == "assistant":
                reasoning = msg.get("reasoning_content", "")
                if reasoning:
                    lines.append(f"<details><summary>💭 思考过程</summary>\n\n{reasoning}\n\n</details>\n")
                tool_calls = msg.get("tool_calls", [])
                for tc in tool_calls:
                    func = tc.get("function", {})
                    name = func.get("name", "?")
                    args = func.get("arguments", "{}")
                    lines.append(f"### 🔧 调用工具: {name}\n\n```json\n{args}\n```\n")
                if content:
                    lines.append(f"## AI\n\n{content}\n")
            elif role == "tool":
                tool_name = msg.get("name", "tool")
                lines.append(f"> 📋 **{tool_name} 返回**: {content}\n")

        if len(lines) <= 1:
            self.notify("没有对话内容", severity="warning", timeout=2)
            return

        save_dir = os.path.join(Path.home(), ".nb_agent", "exports")
        os.makedirs(save_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if session_title and session_title != "新会话":
            safe_title = re.sub(r'[\\/:*?"<>|\s]+', '_', session_title)[:50].strip('_')
            filename = f"chat_{timestamp}_{safe_title}.md"
        else:
            filename = f"chat_{timestamp}_{self.agent.session_id[:8]}.md"
        filepath = os.path.join(save_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        self.notify(f"已导出: {filepath}", timeout=4)

    def _copy_markdown(self, rounds: int = 0):
        messages = self._get_round_messages(rounds)
        lines = []
        for msg in messages:
            role = msg.get("role", "")
            content = msg.get("content", "") or ""
            if role == "system":
                continue
            elif role == "user":
                lines.append(f"## 用户\n\n{content}\n")
            elif role == "assistant":
                reasoning = msg.get("reasoning_content", "")
                if reasoning:
                    lines.append(f"<details><summary>💭 思考过程</summary>\n\n{reasoning}\n\n</details>\n")
                tool_calls = msg.get("tool_calls", [])
                for tc in tool_calls:
                    func = tc.get("function", {})
                    name = func.get("name", "?")
                    args = func.get("arguments", "{}")
                    lines.append(f"### 🔧 调用工具: {name}\n\n```json\n{args}\n```\n")
                if content:
                    lines.append(f"## AI\n\n{content}\n")
            elif role == "tool":
                tool_name = msg.get("name", "tool")
                lines.append(f"> 📋 **{tool_name} 返回**: {content}\n")

        if not lines:
            self.notify("没有对话内容", severity="warning", timeout=2)
            return
        self.copy_to_clipboard("\n".join(lines))
        rounds_hint = f"最近 {rounds} 轮" if rounds > 0 else "全部"
        self.notify(f"{rounds_hint}对话 Markdown 已复制到剪贴板", timeout=3)

    # ─── @ mention 预处理 ──────────────────────────────

    def _extract_skill_mentions(self, text: str) -> str:
        """从消息中提取 @skill:name 引用，加载 SKILL.md 内容作为临时系统指令。"""
        skill_mentions = re.findall(r'@skill:([\w-]+)', text)
        if not skill_mentions:
            return ""

        injected = []
        for name in skill_mentions:
            skill_data = self.agent.skill_manager.view_skill(name)
            if skill_data.get("success"):
                injected.append(
                    f"[Skill: {name}]\n"
                    f"以下是 Skill '{name}' 的指导文档，请据此完成任务：\n\n"
                    f"{skill_data['content']}"
                )
        return "\n\n---\n".join(injected) if injected else ""

    # ─── 聊天重绘 ──────────────────────────────────────

    def _redraw_chat(self):
        chat = self.query_one("#chat-panel", RichLog)
        chat.clear()
        total = len(self.agent.available_models)
        chat.write(f"[bold #00d4aa]nb_agent[/bold #00d4aa] | 共 [#ffd93d]{total}[/#ffd93d] 个可用模型")
        chat.write("[#6b7394]Enter=换行 | Ctrl+J/Ctrl+Enter=发送 | Ctrl+↑=编辑上条 | F1=帮助[/#6b7394]\n")

        last_assistant_idx = -1
        for i in range(len(self.agent.messages) - 1, -1, -1):
            if self.agent.messages[i].get("role") == "assistant" and self.agent.messages[i].get("reasoning_content"):
                last_assistant_idx = i
                break

        for idx, msg in enumerate(self.agent.messages):
            role = msg.get("role", "")
            content = msg.get("content", "") or ""
            if role == "system":
                continue
            elif role == "user":
                chat.write(Panel(
                    Text(content, style="bold #f0f0f0 on #1a2744", overflow="fold"),
                    border_style="bold #00d4ff",
                    title="[bold #00d4ff]💎 user[/bold #00d4ff]",
                    title_align="left",
                    subtitle="[dim #00d4ff]━━━[/dim #00d4ff]",
                    subtitle_align="right",
                    padding=(0, 1),
                ))
            elif role == "assistant":
                tool_calls = msg.get("tool_calls", [])
                reasoning = msg.get("reasoning_content", "")
                if tool_calls or content or reasoning:
                    model_label = msg.get("_model") or "AI"
                    chat.write(f"[bold #4d96ff]🤖 {model_label}[/bold #4d96ff]")
                if reasoning and self._show_thinking:
                    is_last = (idx == last_assistant_idx)
                    if is_last:
                        chat.write(Panel(
                            Text(reasoning, style="italic #a78bfa", overflow="fold"),
                            border_style="#7c3aed",
                            title="[bold #a78bfa]💭 思考过程[/bold #a78bfa]",
                            title_align="left",
                            padding=(0, 1),
                        ))
                    else:
                        char_count = len(reasoning)
                        chat.write(f"  [italic #7c3aed]💭 思考了 {char_count} 字 (Ctrl+P→切换思考显示 可查看全部)[/italic #7c3aed]")
                if tool_calls:
                    for tc in tool_calls:
                        func = tc.get("function", {})
                        name = func.get("name", "?")
                        args = func.get("arguments", "{}")
                        chat.write(Panel(
                            Text(args, style="#fbbf24", overflow="fold"),
                            border_style="#d97706",
                            title=f"[bold #fbbf24]🔧 {name}[/bold #fbbf24]",
                            title_align="left",
                            padding=(0, 1),
                        ))
                if content:
                    chat.write(RichMarkdown(content))
            elif role == "tool":
                result = content[:5000] if len(content) > 5000 else content
                tool_name = msg.get("name", "tool")
                chat.write(Panel(
                    Text(result, style="#86efac", overflow="fold"),
                    border_style="#22c55e",
                    title=f"[bold #86efac]📋 {tool_name} 返回[/bold #86efac]",
                    title_align="left",
                    padding=(0, 1),
                ))

`````

--- **end of file: nb_agent/tui/app.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/styles.tcss** (project: nb_agent) --- 

`````text
/* nb_agent TUI — Modern Dark Theme */

Screen {
    background: #1a1b2e;
    layout: vertical;
}

Header {
    background: #0d0e1a;
    color: #00d4aa;
}

Footer {
    background: #0d0e1a;
    color: #6b7394;
}

Footer > .footer--key {
    background: #252742;
    color: #00d4aa;
}

/* ====== 主内容区 ====== */
#main-area {
    layout: horizontal;
    height: 1fr;
}

#chat-panel {
    width: 1fr;
    border: solid #2a2d4a;
    padding: 0 1;
    scrollbar-size-vertical: 1;
    scrollbar-color: #00d4aa;
    scrollbar-color-hover: #00ffc8;
    background: #12132a;
}

/* ====== 右侧信息面板 ====== */
#tool-panel {
    width: 38;
    border: solid #2a2d4a;
    padding: 0 1;
    background: #0f1025;
}

#section-tokens {
    height: auto;
    max-height: 5;
    padding: 0 0 1 0;
    color: #ffd93d;
}

#section-models-title {
    height: auto;
    max-height: 2;
    color: #4d96ff;
}

#section-models-list {
    height: 1fr;
    min-height: 5;
    border-bottom: solid #252742;
    scrollbar-size-vertical: 1;
    scrollbar-color: #4d96ff;
    background: #0f1025;
}

#section-models-list > .option-list--option-highlighted {
    background: #00897b;
    color: #e0f7fa;
}

#section-models-list > .option-list--option-hover {
    background: #1a3a4a;
}

#section-mcp-title {
    height: auto;
    max-height: 2;
    color: #ff922b;
    padding: 1 0 0 0;
}

#section-mcp-list {
    height: auto;
    max-height: 8;
    border-bottom: solid #252742;
    scrollbar-size-vertical: 1;
    scrollbar-color: #ff922b;
    background: #0f1025;
}

#section-mcp-list > .option-list--option-highlighted {
    background: #3a2a1a;
    color: #ffd93d;
}

#section-mcp-list > .option-list--option-hover {
    background: #2a1f14;
}

#section-tools-title {
    height: auto;
    max-height: 2;
    color: #6bcb77;
    padding: 1 0 0 0;
}

#section-tools-scroll {
    height: 1fr;
    min-height: 5;
    scrollbar-size-vertical: 1;
}

/* ====== 底部输入区 ====== */
#user-input {
    height: 4;
    margin: 0 1;
    border: round #3a3d5a;
    background: #12132a;
    color: #e0e0e0;
    scrollbar-size-vertical: 1;
    scrollbar-color: #00d4aa;
}

#user-input:focus {
    border: round #00d4aa;
}

#user-input.expanded {
    height: 14;
}

/* ====== 模型选择弹窗 ====== */
ModelSelectScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#model-dialog {
    width: 70;
    max-height: 80%;
    border: thick #00d4aa;
    background: #1a1b2e;
    padding: 1 2;
}

#model-title {
    text-align: center;
    width: 100%;
    height: 3;
    color: #00d4aa;
}

#model-list {
    height: 1fr;
    width: 100%;
    background: #12132a;
}

#model-list > .option-list--option-highlighted {
    background: #00897b;
    color: #e0f7fa;
}

/* ====== 会话选择弹窗 ====== */
SessionSelectScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#session-dialog {
    width: 70;
    max-height: 80%;
    border: thick #ff922b;
    background: #1a1b2e;
    padding: 1 2;
}

#session-title {
    text-align: center;
    width: 100%;
    height: 3;
    color: #ff922b;
}

#session-list {
    height: 1fr;
    width: 100%;
    background: #12132a;
}

#session-list > .option-list--option-highlighted {
    background: #00897b;
    color: #e0f7fa;
}

/* ====== 工具详情弹窗 ====== */
ToolDetailScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#tool-detail-dialog {
    width: 90%;
    max-width: 120;
    max-height: 80%;
    border: thick #6bcb77;
    background: #1a1b2e;
    padding: 1 2;
}

#tool-detail-content {
    width: 100%;
}

/* ====== 帮助弹窗 ====== */
HelpScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#help-dialog {
    width: 80%;
    max-width: 100;
    max-height: 80%;
    border: thick #4d96ff;
    background: #1a1b2e;
    padding: 1 2;
}

#help-content {
    width: 100%;
}

/* ====== 工具审批弹窗 ====== */
ToolApprovalScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#approval-dialog {
    width: 70%;
    max-width: 90;
    max-height: 60%;
    border: thick #ff6b6b;
    background: #1a1b2e;
    padding: 1 2;
}

#approval-title {
    text-align: center;
    width: 100%;
    height: 2;
}

#approval-tool {
    text-align: center;
    width: 100%;
    height: 2;
}

#approval-args-label {
    height: 1;
}

#approval-args-scroll {
    height: 1fr;
    min-height: 3;
    max-height: 15;
    border: solid #2a2d4a;
    background: #12132a;
    padding: 0 1;
    scrollbar-size-vertical: 1;
}

#approval-footer {
    text-align: center;
    height: 2;
    margin-top: 1;
}

/* ====== AI 回答跑马灯 + 计时器 ====== */
#ai-status-row {
    height: 1;
    width: 100%;
}

#ai-status-bar {
    width: 1fr;
    height: 1;
    background: #0a0015;
    text-align: left;
    overflow: hidden;
}

#ai-timer {
    width: auto;
    min-width: 10;
    height: 1;
    background: #1a0030;
    text-align: center;
    overflow: hidden;
}

/* ====== Skills 列表弹窗 ====== */
SkillListScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#skill-dialog {
    width: 80;
    max-height: 80%;
    border: thick #a78bfa;
    background: #1a1b2e;
    padding: 1 2;
}

#skill-title {
    text-align: center;
    width: 100%;
    height: 3;
    color: #a78bfa;
}

#skill-list {
    height: 1fr;
    width: 100%;
    background: #12132a;
}

#skill-list > .option-list--option-highlighted {
    background: #1b5e20;
    color: #e8f5e9;
    text-style: bold;
}

#skill-list > .option-list--option-hover {
    background: #2e7d32;
    color: #c8e6c9;
}

#skill-buttons {
    height: auto;
    width: 100%;
    align: center middle;
    padding-top: 1;
}

#skill-buttons Button {
    margin: 0 1;
    min-width: 12;
}

#btn-skill-view {
    background: #2a3a5a;
    color: #8ab4f8;
    border: tall #4a6a9a;
}
#btn-skill-view:hover {
    background: #3a4a6a;
}

#btn-skill-help {
    background: #3a3020;
    color: #ffa726;
    border: tall #6a5a30;
}
#btn-skill-help:hover {
    background: #4a4030;
}

#btn-skill-back {
    background: #2a2a3a;
    color: #9e9e9e;
    border: tall #4a4a5a;
}
#btn-skill-back:hover {
    background: #3a3a4a;
}

/* ====== 右侧面板 — 工具分组 ====== */
#section-groups-title {
    height: auto;
    max-height: 2;
    color: #ffd93d;
    padding: 1 0 0 0;
}

#section-groups-list {
    height: auto;
    max-height: 8;
    border-bottom: solid #252742;
    scrollbar-size-vertical: 1;
    scrollbar-color: #ffd93d;
    background: #0f1025;
}

#section-groups-list > .option-list--option-highlighted {
    background: #3a3520;
    color: #ffd93d;
}

#section-groups-list > .option-list--option-hover {
    background: #2a2515;
}

/* ====== @ 补全弹窗 ====== */
MentionSelectScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#mention-dialog {
    width: 80;
    max-height: 70%;
    border: thick #ffd93d;
    background: #1a1b2e;
    padding: 1 2;
}

#mention-title {
    text-align: center;
    width: 100%;
    height: 2;
    color: #ffd93d;
}

#mention-filter {
    margin-bottom: 1;
}

#mention-list {
    height: 1fr;
    width: 100%;
    background: #12132a;
}

#mention-list > .option-list--option-highlighted {
    background: #3a3520;
    color: #ffd93d;
}

#mention-list > .option-list--option-hover {
    background: #2a2515;
}

/* ====== Skill 内容弹窗 ====== */
SkillContentScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#skill-content-dialog {
    width: 90%;
    max-width: 120;
    max-height: 85%;
    border: thick #a78bfa;
    background: #1a1b2e;
    padding: 1 2;
}

#skill-content-text {
    width: 100%;
}

/* ====== 轮次输入弹窗 ====== */
RoundsInputScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#rounds-dialog {
    width: 60%;
    max-width: 60;
    max-height: 30%;
    border: thick #ffd93d;
    background: #1a1b2e;
    padding: 1 2;
}

#rounds-title {
    text-align: center;
    margin-bottom: 1;
}

#rounds-hint {
    text-align: center;
    margin-bottom: 1;
}

#rounds-input {
    margin-bottom: 1;
}

#rounds-footer {
    text-align: center;
}

/* ====== Agent 管理弹窗 ====== */
AgentSelectScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#preset-dialog {
    width: 100;
    max-height: 70%;
    border: thick #a78bfa;
    background: #1a1b2e;
    padding: 1 2;
}

#preset-title {
    text-align: center;
    width: 100%;
    height: 2;
    color: #a78bfa;
}

#preset-list {
    height: 1fr;
    width: 100%;
    background: #12132a;
}

#preset-list > .option-list--option-highlighted {
    background: #00bcd4;
    color: #0a0a1a;
    text-style: bold;
}

#preset-list > .option-list--option-hover {
    background: #00838f;
    color: #e0f7fa;
}

#preset-buttons {
    height: auto;
    width: 100%;
    align: center middle;
    padding-top: 1;
}

#preset-buttons Button {
    margin: 0 1;
    min-width: 10;
}

#btn-agent-view {
    background: #2a3a5a;
    color: #8ab4f8;
    border: tall #4a6a9a;
}
#btn-agent-view:hover {
    background: #3a4a6a;
}

#btn-agent-edit {
    background: #3a3020;
    color: #ffc107;
    border: tall #6a5a30;
}
#btn-agent-edit:hover {
    background: #4a4030;
}

#btn-agent-apply {
    background: #1a3a2a;
    color: #00e676;
    border: tall #2a6a4a;
}
#btn-agent-apply:hover {
    background: #2a4a3a;
}

#btn-agent-copy {
    background: #2a2a4a;
    color: #b39ddb;
    border: tall #4a4a7a;
}
#btn-agent-copy:hover {
    background: #3a3a5a;
}

#btn-agent-new {
    background: #1a3a4a;
    color: #00bcd4;
    border: tall #2a5a6a;
}
#btn-agent-new:hover {
    background: #2a4a5a;
}

#btn-agent-delete {
    background: #3a1a1a;
    color: #ff5252;
    border: tall #6a2a2a;
}
#btn-agent-delete:hover {
    background: #4a2a2a;
}

/* ====== Agent 详情弹窗 ====== */
AgentContentScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#preset-content-dialog {
    width: 85%;
    max-width: 110;
    max-height: 80%;
    border: thick #a78bfa;
    background: #1a1b2e;
    padding: 1 2;
}

/* ====== Agent 编辑弹窗 ====== */
AgentEditScreen {
    align: center middle;
    background: rgba(0, 0, 0, 0.7);
}

#preset-save-dialog {
    width: 85%;
    max-width: 110;
    max-height: 85%;
    border: thick #ffd93d;
    background: #1a1b2e;
    padding: 1 2;
}

#agent-prompt-input {
    min-height: 10;
    height: auto;
    max-height: 20;
    margin-bottom: 1;
}

#preset-save-title {
    text-align: center;
    margin-bottom: 1;
}

#preset-name-input {
    margin-bottom: 1;
}

#preset-content-input {
    height: 1fr;
    min-height: 5;
    margin-bottom: 1;
}

#preset-save-buttons {
    height: auto;
    width: 100%;
    align: center middle;
    padding-top: 1;
}

#preset-save-buttons Button {
    margin: 0 1;
    min-width: 12;
}

.agent-toggle-buttons {
    height: auto;
    width: 100%;
    padding: 0 0 1 0;
}

.agent-toggle-buttons Button {
    margin: 0 1;
    min-width: 10;
    height: 1;
    background: #1a2a3a;
    color: #6b9bc0;
    border: none;
}
.agent-toggle-buttons Button:hover {
    background: #2a3a4a;
}

`````

--- **end of file: nb_agent/tui/styles.tcss** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/__init__.py`


---

`````python


`````

--- **end of file: nb_agent/tui/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/widgets/commands.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/widgets/commands.py`

#### 📝 Module Docstring

`````
TUI 命令面板 Provider
`````

#### 📦 Imports

- `from textual.command import Hit`
- `from textual.command import Hits`
- `from textual.command import Provider`
- `from textual.command import DiscoveryHit`

#### 🏛️ Classes (1)

##### 📌 `class AgentCommands(Provider)`
*Line: 6*

**Docstring:**
`````
命令面板: 提供会话管理、导出、设置等操作
`````

**Public Methods (2):**
- `async def discover(self) -> Hits`
- `async def search(self, query: str) -> Hits`


---

`````python
"""TUI 命令面板 Provider"""

from textual.command import Hit, Hits, Provider, DiscoveryHit


class AgentCommands(Provider):
    """命令面板: 提供会话管理、导出、设置等操作"""

    async def discover(self) -> Hits:
        app = self.app
        commands = [
            ("编辑上轮提问", "撤回最后一轮对话，重新编辑", app._edit_last_message),
            ("切换思考显示", "显示或隐藏 AI 的思考过程", app._cmd_toggle_thinking),
            ("查看工具详情", "查看所有工具的完整描述", app._show_tool_details),
            ("复制为 Markdown", "复制对话为 Markdown 到剪贴板", app._cmd_copy_markdown),
            ("导出 Markdown 文件", "将对话导出为 .md 文件", app._cmd_export_markdown),
        ]
        for name, help_text, callback in commands:
            yield DiscoveryHit(name, callback, help=help_text)

    async def search(self, query: str) -> Hits:
        matcher = self.matcher(query)
        app = self.app
        commands = [
            ("编辑上轮提问", "撤回最后一轮，重新编辑", app._edit_last_message),
            ("切换思考显示", "显示或隐藏思考过程", app._cmd_toggle_thinking),
            ("查看工具详情", "查看所有工具的完整描述", app._show_tool_details),
            ("复制为 Markdown", "复制对话为 Markdown 到剪贴板", app._cmd_copy_markdown),
            ("导出 Markdown 文件", "导出为 .md 文件", app._cmd_export_markdown),
        ]
        for name, help_text, callback in commands:
            score = matcher.match(name)
            if score > 0:
                yield Hit(score, matcher.highlight(name), callback, help=help_text)

`````

--- **end of file: nb_agent/tui/widgets/commands.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/widgets/inputs.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/widgets/inputs.py`

#### 📝 Module Docstring

`````
聊天输入组件
`````

#### 📦 Imports

- `from textual import events`
- `from textual.message import Message`
- `from textual.widgets import Static`
- `from textual.widgets import TextArea`

#### 🏛️ Classes (2)

##### 📌 `class ChatInput(TextArea)`
*Line: 8*

**Docstring:**
`````
聊天输入框：Enter=换行，Ctrl+J=发送，@=触发补全
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, **kwargs)`
  - **Parameters:**
    - `self`
    - `**kwargs`

**Public Methods (1):**
- `def on_key(self, event: events.Key) -> None`

##### 📌 `class ClickableStatic(Static)`
*Line: 26*

**Docstring:**
`````
可点击的 Static 组件 — 点击时打开工具详情
`````

**Public Methods (1):**
- `def on_click(self, event)`


---

`````python
"""聊天输入组件"""

from textual import events
from textual.message import Message
from textual.widgets import Static, TextArea


class ChatInput(TextArea):
    """聊天输入框：Enter=换行，Ctrl+J=发送，@=触发补全"""

    class MentionTriggered(Message):
        """输入 @ 时触发，通知 App 打开补全弹窗"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_line_numbers = False

    def on_key(self, event: events.Key) -> None:
        if event.character == "@":
            self.set_timer(0.05, self._emit_mention)

    def _emit_mention(self) -> None:
        self.post_message(self.MentionTriggered())


class ClickableStatic(Static):
    """可点击的 Static 组件 — 点击时打开工具详情"""

    def on_click(self, event):
        app = self.app
        if hasattr(app, '_show_tool_details'):
            app._show_tool_details()

`````

--- **end of file: nb_agent/tui/widgets/inputs.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/widgets/screens.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/widgets/screens.py`

#### 📝 Module Docstring

`````
TUI 弹窗：模型选择、帮助、会话恢复、工具详情、轮次输入、工具审批
`````

#### 📦 Imports

- `import json`
- `from typing import Optional`
- `from textual.app import ComposeResult`
- `from textual.containers import Horizontal`
- `from textual.containers import Vertical`
- `from textual.containers import VerticalScroll`
- `from textual.widgets import Button`
- `from textual.widgets import Input`
- `from textual.widgets import OptionList`
- `from textual.widgets import Static`
- `from textual.widgets.option_list import Option`
- `from textual.binding import Binding`
- `from textual.screen import ModalScreen`
- `from rich.text import Text`
- `from nb_agent.core import AgentCore`
- `from textual.widgets._toggle_button import ToggleButton`
- `from textual.widgets import SelectionList`
- `from textual.widgets.selection_list import Selection`
- `from textual.widgets import SelectionList`
- `from textual.widgets.selection_list import Selection`
- `from textual.widgets import SelectionList`
- `from textual.widgets.selection_list import Selection`
- `from textual.widgets import SelectionList`
- `import json as _json`
- `from textual.widgets import TextArea`
- `from textual.widgets import SelectionList`
- `from textual.widgets import TextArea`

#### 🏛️ Classes (13)

##### 📌 `class ModelSelectScreen(ModalScreen[str])`
*Line: 17*

**Docstring:**
`````
模型选择弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent: AgentCore, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent: AgentCore`
    - `**kwargs`

**Public Methods (4):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_option_list_option_selected(self, event: OptionList.OptionSelected)`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回')]`

##### 📌 `class HelpScreen(ModalScreen)`
*Line: 59*

**Docstring:**
`````
帮助弹窗
`````

**Public Methods (2):**
- `def compose(self) -> ComposeResult`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回'), Binding('f1', 'dismiss_modal', '返回'), Binding('enter', 'dismiss_modal', '返回')]`

##### 📌 `class SessionSelectScreen(ModalScreen[str])`
*Line: 130*

**Docstring:**
`````
会话选择弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent: AgentCore, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent: AgentCore`
    - `**kwargs`

**Public Methods (4):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_option_list_option_selected(self, event: OptionList.OptionSelected)`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回')]`

##### 📌 `class ToolDetailScreen(ModalScreen)`
*Line: 180*

**Docstring:**
`````
工具详情弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent: AgentCore, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent: AgentCore`
    - `**kwargs`

**Public Methods (2):**
- `def compose(self) -> ComposeResult`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回'), Binding('enter', 'dismiss_modal', '返回')]`

##### 📌 `class RoundsInputScreen(ModalScreen[int])`
*Line: 229*

**Docstring:**
`````
轮次输入弹窗：用户输入要导出/复制的对话轮次，0=全部
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, action_name: str, **kwargs)`
  - **Parameters:**
    - `self`
    - `action_name: str`
    - `**kwargs`

**Public Methods (5):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_input_submitted(self, event: Input.Submitted)`
- `def action_confirm(self)`
- `def action_cancel(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'cancel', '取消')]`

##### 📌 `class SkillListScreen(ModalScreen[str])`
*Line: 270*

**Docstring:**
`````
Skills 列表弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent: AgentCore, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent: AgentCore`
    - `**kwargs`

**Public Methods (4):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_button_pressed(self, event: Button.Pressed)`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回')]`

##### 📌 `class _SkillHelpScreen(ModalScreen)`
*Line: 348*

**Docstring:**
`````
Skills 使用说明弹窗
`````

**Public Methods (2):**
- `def compose(self) -> ComposeResult`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回'), Binding('enter', 'dismiss_modal', '返回')]`

##### 📌 `class SkillContentScreen(ModalScreen)`
*Line: 410*

**Docstring:**
`````
Skill 内容详情弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, skill_data: dict, **kwargs)`
  - **Parameters:**
    - `self`
    - `skill_data: dict`
    - `**kwargs`

**Public Methods (2):**
- `def compose(self) -> ComposeResult`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回'), Binding('enter', 'dismiss_modal', '返回')]`

##### 📌 `class MentionSelectScreen(ModalScreen[str])`
*Line: 451*

**Docstring:**
`````
@ 补全弹窗：搜索并选择工具或 Skill
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, candidates: list, **kwargs)`
  - **Parameters:**
    - `self`
    - `candidates: list`
    - `**kwargs`

**Public Methods (5):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_input_changed(self, event: Input.Changed)`
- `def on_option_list_option_selected(self, event: OptionList.OptionSelected)`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回')]`

##### 📌 `class AgentSelectScreen(ModalScreen[str])`
*Line: 543*

**Docstring:**
`````
Agent 管理弹窗
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent: AgentCore, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent: AgentCore`
    - `**kwargs`

**Public Methods (4):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_button_pressed(self, event: Button.Pressed)`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回')]`

##### 📌 `class AgentContentScreen(ModalScreen)`
*Line: 671*

**Docstring:**
`````
Agent 详情查看弹窗 — 含 system prompt + 工具 + MCP + Skills
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent_data: dict, agent_core: AgentCore = None, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent_data: dict`
    - `agent_core: AgentCore = None`
    - `**kwargs`

**Public Methods (2):**
- `def compose(self) -> ComposeResult`
- `def action_dismiss_modal(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'dismiss_modal', '返回'), Binding('enter', 'dismiss_modal', '返回')]`

##### 📌 `class AgentEditScreen(ModalScreen[str])`
*Line: 765*

**Docstring:**
`````
新建/编辑 Agent 弹窗（含工具组和 MCP 勾选 + 默认模型选择）
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent_core: AgentCore, edit_agent: dict = None, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent_core: AgentCore`
    - `edit_agent: dict = None`
    - `**kwargs`

**Public Methods (5):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def on_button_pressed(self, event: Button.Pressed)`
- `def on_option_list_option_selected(self, event: OptionList.OptionSelected)`
- `def action_cancel(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'cancel', '取消')]`

##### 📌 `class ToolApprovalScreen(ModalScreen[bool])`
*Line: 972*

**Docstring:**
`````
工具审批弹窗：危险操作需要用户确认后才执行
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, tool_name: str, tool_args: dict, **kwargs)`
  - **Parameters:**
    - `self`
    - `tool_name: str`
    - `tool_args: dict`
    - `**kwargs`

**Public Methods (3):**
- `def compose(self) -> ComposeResult`
- `def action_approve(self)`
- `def action_reject(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('enter', 'approve', '确认执行', priority=True), Binding('escape', 'reject', '拒绝', priority=True)]`


---

`````python
"""TUI 弹窗：模型选择、帮助、会话恢复、工具详情、轮次输入、工具审批"""

import json
from typing import Optional

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Button, Input, OptionList, Static
from textual.widgets.option_list import Option
from textual.binding import Binding
from textual.screen import ModalScreen
from rich.text import Text

from nb_agent.core import AgentCore


class ModelSelectScreen(ModalScreen[str]):
    """模型选择弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
    ]

    def __init__(self, agent: AgentCore, **kwargs):
        super().__init__(**kwargs)
        self.agent = agent

    def compose(self) -> ComposeResult:
        with Vertical(id="model-dialog"):
            yield Static("[bold]选择模型[/bold]  (↑↓选择, Enter确认, Esc返回)\n", id="model-title")
            yield OptionList(id="model-list")

    def on_mount(self):
        option_list = self.query_one("#model-list", OptionList)
        grouped = self.agent.get_models_grouped()
        current = self.agent.get_model_name()

        for provider_name, models in grouped.items():
            option_list.add_option(Option(
                Text(f"── {provider_name} ──", style="dim #6b7394"), disabled=True
            ))
            for m in models:
                if m.id == current:
                    label = Text(f"  ▶ {m.id} ({m.name})", style="bold #00d4aa")
                else:
                    label = Text(f"    {m.id} ({m.name})", style="#c0c0c0")
                option_list.add_option(Option(label, id=m.id))

        option_list.focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        if event.option.id:
            self.dismiss(event.option.id)

    def action_dismiss_modal(self):
        self.dismiss("")


class HelpScreen(ModalScreen):
    """帮助弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
        Binding("f1", "dismiss_modal", "返回"),
        Binding("enter", "dismiss_modal", "返回"),
    ]

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="help-dialog"):
            yield Static(self._build_help(), id="help-content")

    def _build_help(self) -> str:
        lines = []
        lines.append("[bold #00d4aa]═══ nb_agent 帮助 ═══[/bold #00d4aa]\n")

        lines.append("[bold #ffd93d]⌨ 快捷键[/bold #ffd93d]")
        keys = [
            ("Ctrl+J / Ctrl+Enter", "发送消息"),
            ("Enter", "输入框内换行"),
            ("Tab", "打开模型选择弹窗"),
            ("Ctrl+N", "新建会话"),
            ("Ctrl+K", "终止当前 AI 回答"),
            ("Ctrl+↑", "编辑上一轮提问"),
            ("Ctrl+R", "恢复历史会话"),
            ("Ctrl+E", "展开/收起输入框"),
            ("Ctrl+L", "清空屏幕"),
            ("Ctrl+P", "打开命令面板"),
            ("F1", "显示此帮助"),
            ("F2", "查看 Skills 列表"),
            ("F4", "Agent 管理（提示词+工具配置）"),
            ("Ctrl+Q", "退出程序"),
        ]
        for key, desc in keys:
            lines.append(f"  [#ffd93d]{key:<20}[/#ffd93d] [#c0c0c0]{desc}[/#c0c0c0]")

        lines.append("")
        lines.append("[bold #4d96ff]📋 命令面板 (Ctrl+P)[/bold #4d96ff]")
        cmds = [
            ("编辑上轮提问", "撤回最后一轮，重新编辑"),
            ("切换思考显示", "显示或隐藏 AI 思考过程"),
            ("查看工具详情", "查看所有工具完整描述"),
            ("复制完整对话", "复制 Markdown 到剪贴板"),
            ("复制最后回复", "复制到剪贴板"),
            ("导出/保存", "导出 .md 或保存 .txt"),
        ]
        for name, desc in cmds:
            lines.append(f"  [#4d96ff]{name:<18}[/#4d96ff] [#c0c0c0]{desc}[/#c0c0c0]")

        lines.append("")
        lines.append("[bold #ff922b]📋 复制文本[/bold #ff922b]")
        lines.append("  [#c0c0c0]• Shift+鼠标左键拖选 → 选中文本，然后 Ctrl+C 复制[/#c0c0c0]")
        lines.append("  [#c0c0c0]• Alt+Shift+鼠标拖选  → 矩形区域选择[/#c0c0c0]")
        lines.append("  [#c0c0c0]• Ctrl+P → 复制完整对话 / 复制最后回复 (Markdown 格式)[/#c0c0c0]")

        lines.append("")
        lines.append("[bold #6bcb77]💡 提示[/bold #6bcb77]")
        lines.append("  [#c0c0c0]• 输入 @ 自动弹出工具/Skill 补全[/#c0c0c0]")
        lines.append("  [#c0c0c0]• @skill:name 注入 Skill 指南，@tool:name 提示 AI 用该工具[/#c0c0c0]")
        lines.append("  [#c0c0c0]• 右侧面板可点击切换：模型 / MCP Server / 工具分组[/#c0c0c0]")
        lines.append("  [#c0c0c0]• MCP 工具在后台自动连接[/#c0c0c0]")
        lines.append("  [#c0c0c0]• 对话超长时自动截断早期消息[/#c0c0c0]")

        lines.append("\n[dim #6b7394]按 Esc / Enter / F1 关闭[/dim #6b7394]")
        return "\n".join(lines)

    def action_dismiss_modal(self):
        self.dismiss()


class SessionSelectScreen(ModalScreen[str]):
    """会话选择弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
    ]

    def __init__(self, agent: AgentCore, **kwargs):
        super().__init__(**kwargs)
        self.agent = agent
        self._session_ids = []

    def compose(self) -> ComposeResult:
        with Vertical(id="session-dialog"):
            yield Static("[bold]恢复会话[/bold]  (↑↓选择, Enter确认, Esc返回)\n", id="session-title")
            yield OptionList(id="session-list")

    def on_mount(self):
        option_list = self.query_one("#session-list", OptionList)
        sessions = self.agent.get_session_list(20)
        current_id = self.agent.session_id

        if not sessions:
            option_list.add_option(Option(
                Text("没有历史会话", style="dim #6b7394"), disabled=True
            ))
            return

        for s in sessions:
            title = s["title"]
            date = s["updated_at"][:16]
            sid = s["id"]
            self._session_ids.append(sid)

            if sid == current_id:
                label = Text(f"  ▶ {title}  ({date})", style="bold #00d4aa")
            else:
                label = Text(f"    {title}  ({date})", style="#c0c0c0")
            option_list.add_option(Option(label, id=sid))

        option_list.focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        if event.option.id:
            self.dismiss(event.option.id)

    def action_dismiss_modal(self):
        self.dismiss("")


class ToolDetailScreen(ModalScreen):
    """工具详情弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
        Binding("enter", "dismiss_modal", "返回"),
    ]

    def __init__(self, agent: AgentCore, **kwargs):
        super().__init__(**kwargs)
        self.agent = agent

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="tool-detail-dialog"):
            yield Static(self._build_content(), id="tool-detail-content")

    def _build_content(self) -> str:
        tools = self.agent.get_tools()
        enabled_count = sum(1 for t in tools if not t.get("disabled"))
        lines = [f"[bold #6bcb77]函数详情 ({enabled_count}/{len(tools)})[/bold #6bcb77]\n"]
        for t in tools:
            source = t.get("source", "")
            disabled = t.get("disabled", False)
            if disabled:
                icon = "[#ffd93d]○[/#ffd93d]"
                src_label = f"[#ffd93d]{source} [已禁用][/#ffd93d]"
                name_style = "#8890a8"
            elif source.startswith("MCP:"):
                icon = "[#b39ddb]◆[/#b39ddb]"
                src_label = f"[#b39ddb]{source}[/#b39ddb]"
                name_style = "#c0c0c0"
            elif source == "第三方":
                icon = "[#4d96ff]●[/#4d96ff]"
                src_label = f"[#4d96ff]{source}[/#4d96ff]"
                name_style = "#c0c0c0"
            else:
                icon = "[#6bcb77]●[/#6bcb77]"
                src_label = f"[#6bcb77]{source}[/#6bcb77]"
                name_style = "#c0c0c0"
            lines.append(f"{icon} [bold {name_style}]{t['name']}[/bold {name_style}]  {src_label}")
            lines.append(f"  [#8890a8]{t['description']}[/#8890a8]")
            lines.append("")
        lines.append("[dim #6b7394]按 Esc / Enter 关闭[/dim #6b7394]")
        return "\n".join(lines)

    def action_dismiss_modal(self):
        self.dismiss()


class RoundsInputScreen(ModalScreen[int]):
    """轮次输入弹窗：用户输入要导出/复制的对话轮次，0=全部"""

    BINDINGS = [
        Binding("escape", "cancel", "取消"),
    ]

    def __init__(self, action_name: str, **kwargs):
        super().__init__(**kwargs)
        self.action_name = action_name

    def compose(self) -> ComposeResult:
        with Vertical(id="rounds-dialog"):
            yield Static(f"[bold #ffd93d]{self.action_name}[/bold #ffd93d]", id="rounds-title")
            yield Static("[#c0c0c0]导出/复制最近 N 轮对话 (0 = 全部)[/#c0c0c0]", id="rounds-hint")
            yield Input(value="0", id="rounds-input")
            yield Static("[dim #6b7394]Enter 确认 | Esc 取消[/dim #6b7394]", id="rounds-footer")

    def on_mount(self):
        self.query_one("#rounds-input", Input).focus()

    def on_input_submitted(self, event: Input.Submitted):
        self._do_confirm(event.value)

    def action_confirm(self):
        text = self.query_one("#rounds-input", Input).value.strip()
        self._do_confirm(text)

    def _do_confirm(self, text: str):
        try:
            n = int(text.strip())
            if n < 0:
                n = 0
        except ValueError:
            n = 0
        self.dismiss(n)

    def action_cancel(self):
        self.dismiss(-1)


class SkillListScreen(ModalScreen[str]):
    """Skills 列表弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
    ]

    def __init__(self, agent: AgentCore, **kwargs):
        super().__init__(**kwargs)
        self.agent = agent

    def compose(self) -> ComposeResult:
        with Vertical(id="skill-dialog"):
            yield Static(
                "[bold #ffa726]✦ Skills 列表[/bold #ffa726]  [dim #6b7394]↑↓ 选择 · 按钮操作 · Esc 返回[/dim #6b7394]",
                id="skill-title",
            )
            yield OptionList(id="skill-list")
            with Horizontal(id="skill-buttons"):
                yield Button("应用", id="btn-skill-apply", variant="success")
                yield Button("查看详情", id="btn-skill-view", variant="default")
                yield Button("使用说明", id="btn-skill-help", variant="default")
                yield Button("返回", id="btn-skill-back", variant="default")

    def on_mount(self):
        option_list = self.query_one("#skill-list", OptionList)
        all_skills = self.agent.skill_manager.get_all_skills()

        if not all_skills:
            option_list.add_option(Option(
                Text("没有发现 Skills", style="dim #6b7394"), disabled=True
            ))
            return

        for s in all_skills:
            name = s["name"]
            desc = s["description"]
            if len(desc) > 60:
                desc = desc[:60] + "..."
            manual = "  [仅手动]" if s.get("manual_only") else ""
            icon = "○" if s.get("manual_only") else "●"
            label = Text(f"  {icon} {name}{manual}  — {desc}", style="#c0c0c0")
            option_list.add_option(Option(label, id=name))

        option_list.focus()

    def _get_selected_skill_id(self) -> str:
        option_list = self.query_one("#skill-list", OptionList)
        idx = option_list.highlighted
        if idx is not None:
            opt = option_list.get_option_at_index(idx)
            if opt.id:
                return opt.id
        return ""

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn-skill-apply":
            skill_id = self._get_selected_skill_id()
            if skill_id:
                self.dismiss(f"__apply__:{skill_id}")
                return
            self.app.notify("请先选中一个 Skill", severity="warning", timeout=2)
        elif event.button.id == "btn-skill-view":
            skill_id = self._get_selected_skill_id()
            if skill_id:
                self.dismiss(skill_id)
                return
            self.app.notify("请先选中一个 Skill", severity="warning", timeout=2)
        elif event.button.id == "btn-skill-help":
            self.app.push_screen(_SkillHelpScreen())
        elif event.button.id == "btn-skill-back":
            self.dismiss("")
        self.query_one("#skill-list", OptionList).focus()

    def action_dismiss_modal(self):
        self.dismiss("")


class _SkillHelpScreen(ModalScreen):
    """Skills 使用说明弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
        Binding("enter", "dismiss_modal", "返回"),
    ]

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="skill-content-dialog"):
            yield Static(self._build(), id="skill-help-text")

    def _build(self) -> str:
        lines = [
            "[bold #ffa726]═══ Skills 使用说明 ═══[/bold #ffa726]\n",
            "[bold #4d96ff]什么是 Skill？[/bold #4d96ff]",
            "  Skill 是一份 SKILL.md 格式的操作指南，告诉 AI 在特定",
            "  任务中如何一步步执行。AI 在需要时通过 view_skill 工具",
            "  主动查阅，实现渐进式披露（Progressive Disclosure）。\n",
            "[bold #4d96ff]开放标准[/bold #4d96ff]",
            "  遵循 Agent Skills 开放规范（agentskills.io）",
            "  由 Anthropic 创建，已被 26+ 平台采用：",
            "  Claude / OpenAI Codex / Gemini CLI / GitHub Copilot /",
            "  Cursor / VS Code / Microsoft Agent Framework 等\n",
            "[bold #4d96ff]渐进式披露（Progressive Disclosure）[/bold #4d96ff]",
            "  1. [#ffa726]Discovery[/#ffa726]：启动时仅加载 name + description",
            "  2. [#ffa726]Activation[/#ffa726]：任务匹配时加载完整 SKILL.md",
            "  3. [#ffa726]Execution[/#ffa726]：按需加载 scripts / references\n",
            "[bold #4d96ff]如何创建 Skill？[/bold #4d96ff]",
            "  1. 在 .nb_agent/skills/ 下新建文件夹",
            "  2. 在文件夹中创建 SKILL.md，格式如下：",
            "  [bold #ff5252]⚠ 文件夹名必须和 name 字段相同[/bold #ff5252]\n",
            "  [#c0c0c0]my-skill/[/#c0c0c0]",
            "  [#c0c0c0]└── SKILL.md[/#c0c0c0]\n",
            "  [#c0c0c0]---[/#c0c0c0]",
            "  [#c0c0c0]name: my-skill    ← 必须与文件夹名一致[/#c0c0c0]",
            "  [#c0c0c0]description: 描述用途和触发时机[/#c0c0c0]",
            "  [#c0c0c0]---[/#c0c0c0]",
            "  [#c0c0c0]具体的操作步骤和指南...[/#c0c0c0]\n",
            "[bold #4d96ff]Front Matter 字段（agentskills.io 规范）[/bold #4d96ff]",
            "  [#ffd93d]name[/#ffd93d]（必填）小写+连字符，最多 64 字符",
            "  [#ffd93d]description[/#ffd93d]（必填）用途+触发时机，最多 1024 字符",
            "  [#ffd93d]license[/#ffd93d]（可选）许可证（如 Apache-2.0）",
            "  [#ffd93d]compatibility[/#ffd93d]（可选）环境要求，最多 500 字符",
            "  [#ffd93d]metadata[/#ffd93d]（可选）自定义键值对（author/version 等）",
            "  [#ffd93d]allowed-tools[/#ffd93d]（可选）预授权工具列表（实验性）",
            "  [dim #6b7394]nb_agent 扩展字段:[/dim #6b7394]",
            "  [#ffd93d]paths[/#ffd93d]（可选）文件路径 glob 匹配模式",
            "  [#ffd93d]disable-model-invocation[/#ffd93d]（可选）true = 仅手动\n",
            "[bold #4d96ff]Skill 来源[/bold #4d96ff]",
            "  [#6bcb77]●[/#6bcb77] 内置：nb_agent/skills/builtin/",
            "  [#4d96ff]●[/#4d96ff] 全局：~/.nb_agent/skills/ 或 ~/.agents/skills/",
            "  [#b39ddb]●[/#b39ddb] 项目：<项目>/.nb_agent/skills/\n",
            "[dim #6b7394]规范详情: agentskills.io/specification[/dim #6b7394]",
            "[dim #6b7394]按 Esc / Enter 返回[/dim #6b7394]",
        ]
        return "\n".join(lines)

    def action_dismiss_modal(self):
        self.dismiss()


class SkillContentScreen(ModalScreen):
    """Skill 内容详情弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
        Binding("enter", "dismiss_modal", "返回"),
    ]

    def __init__(self, skill_data: dict, **kwargs):
        super().__init__(**kwargs)
        self.skill_data = skill_data

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="skill-content-dialog"):
            yield Static(self._build_content(), id="skill-content-text")

    def _build_content(self) -> str:
        d = self.skill_data
        lines = []
        lines.append(f"[bold #a78bfa]═══ Skill: {d.get('name', '?')} ═══[/bold #a78bfa]\n")
        lines.append(f"  [#ffd93d]来源:[/#ffd93d] {d.get('source', '?')}")
        lines.append(f"  [#ffd93d]路径:[/#ffd93d] {d.get('skill_path', '?')}")

        paths = d.get("paths", [])
        if paths:
            lines.append(f"  [#ffd93d]匹配:[/#ffd93d] {', '.join(paths)}")

        lines.append("")
        lines.append("[bold #4d96ff]── 内容 ──[/bold #4d96ff]\n")
        content = d.get("content", "无内容")
        for line in content.split("\n"):
            safe = line.replace("[", "\\[")
            lines.append(f"[#c0c0c0]{safe}[/#c0c0c0]")

        lines.append("\n[dim #6b7394]按 Esc / Enter 关闭[/dim #6b7394]")
        return "\n".join(lines)

    def action_dismiss_modal(self):
        self.dismiss()


class MentionSelectScreen(ModalScreen[str]):
    """@ 补全弹窗：搜索并选择工具或 Skill"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
    ]

    def __init__(self, candidates: list, **kwargs):
        super().__init__(**kwargs)
        self.candidates = candidates

    def compose(self) -> ComposeResult:
        with Vertical(id="mention-dialog"):
            yield Static("[bold]@ 引用工具或 Skill[/bold]  (输入过滤, Enter 选择, Esc 返回)", id="mention-title")
            yield Input(placeholder="搜索...", id="mention-filter")
            yield OptionList(id="mention-list")

    def on_mount(self):
        self._render_list("")
        self.query_one("#mention-filter", Input).focus()

    def on_input_changed(self, event: Input.Changed):
        if event.input.id == "mention-filter":
            self._render_list(event.value)

    def _render_list(self, query: str):
        option_list = self.query_one("#mention-list", OptionList)
        option_list.clear_options()
        q = query.lower()

        tools = [c for c in self.candidates if c.get("type") != "skill"]
        skills = [c for c in self.candidates if c.get("type") == "skill"]

        filtered_tools = [c for c in tools if not q or q in c["name"].lower() or q in c.get("description", "").lower()]
        filtered_skills = [c for c in skills if not q or q in c["name"].lower() or q in c.get("description", "").lower()]

        if filtered_tools:
            last_group = None
            for c in filtered_tools:
                group = c.get("group", "")
                if group != last_group:
                    src = c.get("source", "")
                    if src.startswith("MCP:"):
                        option_list.add_option(Option(Text(f"── {group} ──", style="dim #b39ddb"), disabled=True))
                    elif src == "第三方" and group:
                        option_list.add_option(Option(Text(f"── {group} ──", style="dim #4d96ff"), disabled=True))
                    elif group:
                        option_list.add_option(Option(Text(f"── {group} ──", style="dim #6bcb77"), disabled=True))
                    else:
                        option_list.add_option(Option(Text("── 工具 ──", style="dim #6bcb77"), disabled=True))
                    last_group = group

                name = c["name"]
                func_name = c.get("func_name", name)
                desc = c.get("description", "")
                if len(desc) > 50:
                    desc = desc[:50] + "..."
                source = c.get("source", "")

                if source.startswith("MCP:"):
                    icon, style = "◆", "#b39ddb"
                elif source == "第三方":
                    icon, style = "●", "#4d96ff"
                else:
                    icon, style = "●", "#6bcb77"

                label = Text(f"  {icon} {func_name}  ", style=f"bold {style}")
                label.append(desc, style="#8890a8")
                option_list.add_option(Option(label, id=f"tool:{name}"))

        if filtered_skills:
            if filtered_tools:
                option_list.add_option(Option(Text("", style="dim"), disabled=True))
            option_list.add_option(Option(Text("── Skills ──", style="dim #a78bfa"), disabled=True))
            for c in filtered_skills:
                name = c["name"]
                desc = c.get("description", "")
                if len(desc) > 50:
                    desc = desc[:50] + "..."
                manual = " [仅手动]" if c.get("manual_only") else ""
                label = Text(f"  ★ {name}{manual}  ", style="bold #a78bfa")
                label.append(desc, style="#8890a8")
                option_list.add_option(Option(label, id=f"skill:{name}"))

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        if event.option.id:
            self.dismiss(event.option.id)

    def action_dismiss_modal(self):
        self.dismiss("")


class AgentSelectScreen(ModalScreen[str]):
    """Agent 管理弹窗"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
    ]

    def __init__(self, agent: AgentCore, **kwargs):
        super().__init__(**kwargs)
        self.agent = agent

    def compose(self) -> ComposeResult:
        with Vertical(id="preset-dialog"):
            yield Static(
                "[bold #a78bfa]✦ Agent 管理[/bold #a78bfa]  [dim #6b7394]↑↓ 选择 · 按钮操作 · Esc 返回[/dim #6b7394]",
                id="preset-title",
            )
            yield OptionList(id="preset-list")
            with Horizontal(id="preset-buttons"):
                yield Button("查看详情", id="btn-agent-view", variant="default")
                yield Button("编辑", id="btn-agent-edit", variant="warning")
                yield Button("应用", id="btn-agent-apply", variant="success")
                yield Button("复制", id="btn-agent-copy", variant="primary")
                yield Button("新建", id="btn-agent-new", variant="primary")
                yield Button("删除", id="btn-agent-delete", variant="error")

    def on_mount(self):
        self._render_list()
        self.query_one("#preset-list", OptionList).focus()

    def _render_list(self):
        option_list = self.query_one("#preset-list", OptionList)
        option_list.clear_options()
        agents = self.agent.get_agents()
        current_id = self.agent.current_agent_id
        for a in agents:
            aid = a["id"]
            name = a["name"]
            prompt_preview = a.get("system_prompt", "")[:40].replace("\n", " ")
            if len(a.get("system_prompt", "")) > 40:
                prompt_preview += "..."
            builtin_tag = " ⚙" if a.get("is_builtin") else ""
            if aid == current_id:
                label = Text(f"  ✦ ", style="bold #00ff88")
                label.append(name, style="bold #00ff88")
                label.append(f"{builtin_tag}  ", style="bold #00ff88")
                label.append("(当前) ", style="bold #00ff88")
                label.append(prompt_preview, style="#5a8a6a")
            else:
                label = Text(f"    ", style="#e0e0e0")
                label.append(name, style="#e0e0e0")
                label.append(f"{builtin_tag}  ", style="#888888")
                label.append(prompt_preview, style="#6b7394")
            option_list.add_option(Option(label, id=aid))

    def _get_highlighted_agent(self):
        option_list = self.query_one("#preset-list", OptionList)
        idx = option_list.highlighted
        if idx is None:
            return None
        opt = option_list.get_option_at_index(idx)
        if not opt.id:
            return None
        for a in self.agent.get_agents():
            if a["id"] == opt.id:
                return a
        return None

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn-agent-view":
            agent_data = self._get_highlighted_agent()
            if agent_data:
                self.app.push_screen(AgentContentScreen(agent_data, self.agent))
            else:
                self.app.notify("请先选中一个 Agent", severity="warning", timeout=2)

        elif event.button.id == "btn-agent-edit":
            agent_data = self._get_highlighted_agent()
            if not agent_data:
                self.app.notify("请先选中一个 Agent", severity="warning", timeout=2)
            elif agent_data.get("is_builtin"):
                self.app.notify("内置 Agent 不可编辑，请先复制", severity="warning", timeout=2)
            else:
                self.dismiss(f"__edit__:{agent_data['id']}")

        elif event.button.id == "btn-agent-apply":
            agent_data = self._get_highlighted_agent()
            if agent_data:
                self.dismiss(agent_data["id"])
            else:
                self.app.notify("请先选中一个 Agent", severity="warning", timeout=2)

        elif event.button.id == "btn-agent-copy":
            agent_data = self._get_highlighted_agent()
            if agent_data:
                self.dismiss(f"__copy__:{agent_data['id']}")
            else:
                self.app.notify("请先选中一个 Agent", severity="warning", timeout=2)

        elif event.button.id == "btn-agent-new":
            self.dismiss("__new__")

        elif event.button.id == "btn-agent-delete":
            self._do_delete()

        self.query_one("#preset-list", OptionList).focus()

    def _do_delete(self):
        option_list = self.query_one("#preset-list", OptionList)
        idx = option_list.highlighted
        if idx is None:
            return
        opt = option_list.get_option_at_index(idx)
        if not opt.id or opt.id == self.agent.DEFAULT_AGENT_ID:
            self.app.notify("默认 Agent 不可删除", severity="warning", timeout=2)
            return
        agent_data = self._get_highlighted_agent()
        if agent_data and agent_data.get("is_builtin"):
            self.app.notify("内置 Agent 不可删除", severity="warning", timeout=2)
            return
        self.agent.delete_agent(opt.id)
        self._render_list()
        self.app.notify("已删除 Agent", timeout=2)

    def action_dismiss_modal(self):
        self.dismiss("")


class AgentContentScreen(ModalScreen):
    """Agent 详情查看弹窗 — 含 system prompt + 工具 + MCP + Skills"""

    BINDINGS = [
        Binding("escape", "dismiss_modal", "返回"),
        Binding("enter", "dismiss_modal", "返回"),
    ]

    def __init__(self, agent_data: dict, agent_core: AgentCore = None, **kwargs):
        super().__init__(**kwargs)
        self.agent_data = agent_data
        self.agent_core = agent_core

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="preset-content-dialog"):
            yield Static(self._build_content(), id="preset-content-text")

    def _build_content(self) -> str:
        a = self.agent_data
        lines = []
        lines.append(f"[bold #a78bfa]═══ Agent: {a.get('name', '?')} ═══[/bold #a78bfa]\n")
        if a.get("is_builtin"):
            lines.append("  [#ffd93d]类型:[/#ffd93d] 内置（不可编辑/删除，可复制）")
        else:
            lines.append(f"  [#ffd93d]ID:[/#ffd93d] {a.get('id', '?')}")

        raw_ag = a.get("allowed_tool_groups")
        ag = set(raw_ag) if raw_ag is not None else None
        raw_as = a.get("allowed_mcp_servers")
        as_ = set(raw_as) if raw_as is not None else None

        lines.append("")
        lines.append("[bold #4d96ff]── System Prompt ──[/bold #4d96ff]\n")
        content = a.get("system_prompt", "无内容")
        for line in content.split("\n"):
            safe = line.replace("[", "\\[")
            lines.append(f"[#c0c0c0]{safe}[/#c0c0c0]")

        default_model = a.get("default_model", "")
        if default_model:
            lines.append("")
            lines.append(f"[bold #4d96ff]── 默认模型 ──[/bold #4d96ff]\n")
            lines.append(f"  [bold #00d4aa]{default_model}[/bold #00d4aa]")

        if self.agent_core:
            lines.append("")
            lines.append("[bold #6bcb77]── 工具/函数 ──[/bold #6bcb77]\n")
            groups = self.agent_core.get_tool_groups()
            non_mcp = [g for g in groups if not g["name"].startswith("mcp__") and g["name"] != "(无分组)"]
            if non_mcp:
                for g in non_mcp:
                    is_allowed = ag is None or g["name"] in ag
                    dot = "[#6bcb77]●[/#6bcb77]" if is_allowed else "[#ffd93d]○[/#ffd93d]"
                    state = "[#6bcb77]启用[/#6bcb77]" if is_allowed else "[#ffd93d]未选中[/#ffd93d]"
                    safe_name = g["name"].replace("[", "\\[")
                    lines.append(f"  {dot} {safe_name} ({g['count']} 个函数) — {state}")
            else:
                lines.append("  [dim #6b7394]无工具组[/dim #6b7394]")

            lines.append("")
            lines.append("[bold #b39ddb]── MCP 服务 ──[/bold #b39ddb]\n")
            servers = self.agent_core.get_mcp_status()
            if servers:
                for s in servers:
                    is_allowed = as_ is None or s["name"] in as_
                    dot = "[#b39ddb]◆[/#b39ddb]" if is_allowed else "[#ffd93d]○[/#ffd93d]"
                    state = "[#b39ddb]启用[/#b39ddb]" if is_allowed else "[#ffd93d]未选中[/#ffd93d]"
                    tc = f" ({s.get('tool_count', 0)} 个工具)" if s.get("tool_count") else ""
                    lines.append(f"  {dot} {s['name']}{tc} — {state}")
            else:
                lines.append("  [dim #6b7394]无 MCP 服务[/dim #6b7394]")

            all_skills = self.agent_core.skill_manager.get_all_skills()
            if all_skills:
                raw_sk = a.get("allowed_skills")
                sk_set = set(raw_sk) if raw_sk is not None else None
                lines.append("")
                lines.append("[bold #ffa726]── Skills ──[/bold #ffa726]\n")
                for sk in all_skills:
                    safe_name = sk["name"].replace("[", "\\[")
                    safe_desc = sk.get("description", "").replace("[", "\\[")
                    is_allowed = sk_set is None or sk["name"] in sk_set
                    if is_allowed:
                        lines.append(f"  [#ffa726]★[/#ffa726] {safe_name} — [dim]{safe_desc}[/dim]")
                    else:
                        lines.append(f"  [#ffd93d]☆[/#ffd93d] [#8890a8]{safe_name} — {safe_desc}[/#8890a8]  [#ffd93d]未选中[/#ffd93d]")

        lines.append("\n[dim #6b7394]按 Esc / Enter 返回[/dim #6b7394]")
        return "\n".join(lines)

    def action_dismiss_modal(self):
        self.dismiss()


class AgentEditScreen(ModalScreen[str]):
    """新建/编辑 Agent 弹窗（含工具组和 MCP 勾选 + 默认模型选择）"""

    BINDINGS = [
        Binding("escape", "cancel", "取消"),
    ]

    def __init__(self, agent_core: AgentCore, edit_agent: dict = None, **kwargs):
        super().__init__(**kwargs)
        self.agent_core = agent_core
        self.edit_agent = edit_agent
        self._all_group_names: list = []
        self._all_server_names: list = []
        self._all_skill_names: list = []
        self._selected_model = ""

    def compose(self) -> ComposeResult:
        from textual.widgets._toggle_button import ToggleButton
        ToggleButton.BUTTON_INNER = "✓"

        title = f"编辑 Agent: {self.edit_agent['name']}" if self.edit_agent else "新建 Agent"
        with VerticalScroll(id="preset-save-dialog"):
            yield Static(f"[bold #ffd93d]{title}[/bold #ffd93d]", id="preset-save-title")
            yield Static("[#c0c0c0]Agent 名称:[/#c0c0c0]")
            yield Input(
                value=self.edit_agent["name"] if self.edit_agent else "",
                placeholder="如：代码审查专家",
                id="agent-name-input",
            )
            yield Static("[#c0c0c0]默认模型 [dim](↑↓ 选择)[/dim]:[/#c0c0c0]")
            yield OptionList(id="agent-model-select")
            yield Static("[#c0c0c0]System Prompt:[/#c0c0c0]")
            from textual.widgets import TextArea
            prompt = self.edit_agent["system_prompt"] if self.edit_agent else ""
            yield TextArea(prompt, id="agent-prompt-input")
            yield Static("[#c0c0c0]工具组 [dim](✓ 启用)[/dim]:[/#c0c0c0]")
            yield self._build_groups_list()
            with Horizontal(classes="agent-toggle-buttons"):
                yield Button("全部启用", id="btn-groups-all", variant="default")
                yield Button("全部禁用", id="btn-groups-none", variant="default")
            yield Static("[#c0c0c0]MCP 服务 [dim](✓ 启用)[/dim]:[/#c0c0c0]")
            yield self._build_servers_list()
            with Horizontal(classes="agent-toggle-buttons"):
                yield Button("全部启用", id="btn-servers-all", variant="default")
                yield Button("全部禁用", id="btn-servers-none", variant="default")
            yield Static("[#c0c0c0]Skills [dim](✓ 注入到 AI 上下文)[/dim]:[/#c0c0c0]")
            yield self._build_skills_list()
            with Horizontal(classes="agent-toggle-buttons"):
                yield Button("全部启用", id="btn-skills-all", variant="default")
                yield Button("全部禁用", id="btn-skills-none", variant="default")
            with Horizontal(id="preset-save-buttons"):
                yield Button("保存", id="btn-save-agent", variant="success")
                yield Button("取消", id="btn-cancel-agent", variant="default")

    def _build_groups_list(self):
        from textual.widgets import SelectionList
        from textual.widgets.selection_list import Selection
        raw = self.edit_agent.get("allowed_tool_groups") if self.edit_agent else None
        allowed = set(raw) if raw is not None else (set() if not self.edit_agent else None)
        groups = self.agent_core.get_tool_groups()
        non_mcp = [g for g in groups if not g["name"].startswith("mcp__") and g["name"] != "(无分组)"]
        selections = []
        for g in non_mcp:
            self._all_group_names.append(g["name"])
            checked = allowed is None or g["name"] in allowed
            selections.append(Selection(f"{g['name']} ({g['count']} 个函数)", g["name"], checked))
        if not selections:
            return Static("[dim #6b7394]无可用工具组[/dim #6b7394]", id="agent-groups-select")
        return SelectionList(*selections, id="agent-groups-select")

    def _build_servers_list(self):
        from textual.widgets import SelectionList
        from textual.widgets.selection_list import Selection
        raw = self.edit_agent.get("allowed_mcp_servers") if self.edit_agent else None
        allowed = set(raw) if raw is not None else (set() if not self.edit_agent else None)
        servers = self.agent_core.get_mcp_status()
        selections = []
        for s in servers:
            self._all_server_names.append(s["name"])
            checked = allowed is None or s["name"] in allowed
            label = f"{s['name']}" + (f" ({s['tool_count']} 个工具)" if s.get("tool_count") else "")
            selections.append(Selection(label, s["name"], checked))
        if not selections:
            return Static("[dim #6b7394]无 MCP 服务[/dim #6b7394]", id="agent-servers-select")
        return SelectionList(*selections, id="agent-servers-select")

    def _build_skills_list(self):
        from textual.widgets import SelectionList
        from textual.widgets.selection_list import Selection
        raw = self.edit_agent.get("allowed_skills") if self.edit_agent else None
        allowed = set(raw) if raw is not None else (set() if not self.edit_agent else None)
        all_skills = self.agent_core.skill_manager.get_all_skills()
        selections = []
        for s in all_skills:
            name = s["name"]
            self._all_skill_names.append(name)
            checked = allowed is None or name in allowed
            suffix = " [仅手动]" if s.get("manual_only") else ""
            selections.append(Selection(f"{name}{suffix} — {s['description'][:40]}", name, checked))
        if not selections:
            return Static("[dim #6b7394]无可用 Skills[/dim #6b7394]", id="agent-skills-select")
        return SelectionList(*selections, id="agent-skills-select")

    def on_mount(self):
        self.query_one("#agent-name-input", Input).focus()
        self._refresh_model_list()

    def _refresh_model_list(self):
        """刷新模型列表，选中当前 Agent 的 default_model 或当前模型"""
        option_list = self.query_one("#agent-model-select", OptionList)
        option_list.clear_options()
        grouped = self.agent_core.get_models_grouped()
        edit_model = self.edit_agent.get("default_model", "") if self.edit_agent else ""
        current = edit_model or self.agent_core.get_model_name()
        self._selected_model = current

        for provider_name, models in grouped.items():
            option_list.add_option(Option(
                Text(f"── {provider_name} ──", style="dim #6b7394"), disabled=True
            ))
            for m in models:
                if m.id == current:
                    label = Text(f"  ▶ {m.id} ({m.name})", style="bold #00d4aa")
                else:
                    label = Text(f"    {m.id} ({m.name})", style="#c0c0c0")
                option_list.add_option(Option(label, id=m.id))

    def _toggle_all(self, widget_id: str, all_names: list, select: bool):
        from textual.widgets import SelectionList
        try:
            sl = self.query_one(f"#{widget_id}", SelectionList)
            for name in all_names:
                if select:
                    sl.select(name)
                else:
                    sl.deselect(name)
        except Exception:
            pass

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "btn-save-agent":
            self._do_save()
        elif event.button.id == "btn-cancel-agent":
            self.dismiss("")
        elif event.button.id == "btn-groups-all":
            self._toggle_all("agent-groups-select", self._all_group_names, True)
        elif event.button.id == "btn-groups-none":
            self._toggle_all("agent-groups-select", self._all_group_names, False)
        elif event.button.id == "btn-servers-all":
            self._toggle_all("agent-servers-select", self._all_server_names, True)
        elif event.button.id == "btn-servers-none":
            self._toggle_all("agent-servers-select", self._all_server_names, False)
        elif event.button.id == "btn-skills-all":
            self._toggle_all("agent-skills-select", self._all_skill_names, True)
        elif event.button.id == "btn-skills-none":
            self._toggle_all("agent-skills-select", self._all_skill_names, False)

    def _do_save(self):
        import json as _json
        name = self.query_one("#agent-name-input", Input).value.strip()
        if not name:
            self.app.notify("请输入 Agent 名称", severity="warning", timeout=2)
            return
        from textual.widgets import TextArea, SelectionList
        prompt = self.query_one("#agent-prompt-input", TextArea).text.strip()
        if not prompt:
            self.app.notify("请输入 System Prompt", severity="warning", timeout=2)
            return

        allowed_tool_groups = []
        allowed_mcp_servers = []
        allowed_skills = []
        try:
            groups_select = self.query_one("#agent-groups-select", SelectionList)
            allowed_tool_groups = list(groups_select.selected)
        except Exception:
            pass
        try:
            servers_select = self.query_one("#agent-servers-select", SelectionList)
            allowed_mcp_servers = list(servers_select.selected)
        except Exception:
            pass
        try:
            skills_select = self.query_one("#agent-skills-select", SelectionList)
            allowed_skills = list(skills_select.selected)
        except Exception:
            pass

        result = _json.dumps({
            "edit_id": self.edit_agent["id"] if self.edit_agent else "",
            "name": name,
            "system_prompt": prompt,
            "default_model": self._selected_model,
            "allowed_tool_groups": allowed_tool_groups,
            "allowed_mcp_servers": allowed_mcp_servers,
            "allowed_skills": allowed_skills,
        }, ensure_ascii=False)
        self.dismiss(result)

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        if event.option.id:
            self._selected_model = event.option.id

    def action_cancel(self):
        self.dismiss("")


class ToolApprovalScreen(ModalScreen[bool]):
    """工具审批弹窗：危险操作需要用户确认后才执行"""

    BINDINGS = [
        Binding("enter", "approve", "确认执行", priority=True),
        Binding("escape", "reject", "拒绝", priority=True),
    ]

    def __init__(self, tool_name: str, tool_args: dict, **kwargs):
        super().__init__(**kwargs)
        self.tool_name = tool_name
        self.tool_args = tool_args

    def compose(self) -> ComposeResult:
        args_str = json.dumps(self.tool_args, ensure_ascii=False, indent=2)
        with Vertical(id="approval-dialog"):
            yield Static("[bold #ff6b6b]⚠ 工具需要确认[/bold #ff6b6b]", id="approval-title")
            yield Static(f"[bold #ffd93d]工具: {self.tool_name}[/bold #ffd93d]", id="approval-tool")
            yield Static(f"[#c0c0c0]参数:[/#c0c0c0]", id="approval-args-label")
            with VerticalScroll(id="approval-args-scroll"):
                yield Static(Text(args_str, style="#e0e0e0"), id="approval-args")
            yield Static(
                "[bold #6bcb77]Enter = 确认执行[/bold #6bcb77]  |  [bold #ff6b6b]Esc = 拒绝[/bold #ff6b6b]",
                id="approval-footer",
            )

    def action_approve(self):
        self.dismiss(True)

    def action_reject(self):
        self.dismiss(False)

`````

--- **end of file: nb_agent/tui/widgets/screens.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/widgets/tool_panel.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/widgets/tool_panel.py`

#### 📝 Module Docstring

`````
右侧工具/模型/MCP/Token 信息面板
`````

#### 📦 Imports

- `from textual.containers import Vertical`
- `from textual.containers import VerticalScroll`
- `from textual.app import ComposeResult`
- `from textual.widgets import OptionList`
- `from textual.widgets import RichLog`
- `from textual.widgets import Static`
- `from textual.widgets.option_list import Option`
- `from rich.text import Text`
- `from nb_agent.core import AgentCore`
- `from inputs import ClickableStatic`

#### 🏛️ Classes (1)

##### 📌 `class ToolPanel(Vertical)`
*Line: 17*

**Docstring:**
`````
右侧信息面板：分区展示，各区独立滚动
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, agent: AgentCore, **kwargs)`
  - **Parameters:**
    - `self`
    - `agent: AgentCore`
    - `**kwargs`

**Public Methods (4):**
- `def compose(self) -> ComposeResult`
- `def on_mount(self)`
- `def update_content(self, last_elapsed: float = 0.0)`
- `def on_option_list_option_selected(self, event: OptionList.OptionSelected)`


---

`````python
"""右侧工具/模型/MCP/Token 信息面板"""

from textual.containers import Vertical, VerticalScroll
from textual.app import ComposeResult
from textual.widgets import OptionList, RichLog, Static
from textual.widgets.option_list import Option
from rich.text import Text

from nb_agent.core import AgentCore
from .inputs import ClickableStatic


def _fmt_tokens(n: int) -> str:
    return f"{n / 1000:.1f}k"


class ToolPanel(Vertical):
    """右侧信息面板：分区展示，各区独立滚动"""

    def __init__(self, agent: AgentCore, **kwargs):
        super().__init__(**kwargs)
        self.agent = agent

    def compose(self) -> ComposeResult:
        yield Static("", id="section-tokens")
        yield Static("", id="section-models-title")
        yield OptionList(id="section-models-list")
        yield Static("", id="section-mcp-title")
        yield OptionList(id="section-mcp-list")
        yield Static("", id="section-groups-title")
        yield OptionList(id="section-groups-list")
        yield ClickableStatic("", id="section-tools-title")
        with VerticalScroll(id="section-tools-scroll"):
            yield ClickableStatic("", id="section-tools")

    def on_mount(self):
        self.update_content()

    def update_content(self, last_elapsed: float = 0.0):
        t = self.agent.get_token_usage()
        if t['total'] == 0 and t.get('last_rounds', 0) == 0:
            token_text = "[bold #ffd93d]✦ Token:[/bold #ffd93d] [#6b7394]等待对话...[/#6b7394]"
        else:
            elapsed_str = f" | 耗时{last_elapsed:.1f}s" if last_elapsed > 0 else ""
            last_info = f"本次 {_fmt_tokens(t['last_total'])}(入{_fmt_tokens(t['last_prompt'])}+出{_fmt_tokens(t['last_completion'])}){elapsed_str}"
            total_info = f"累计 {_fmt_tokens(t['total'])}(入{_fmt_tokens(t['total_prompt'])}+出{_fmt_tokens(t['total_completion'])})"
            token_text = (
                f"[bold #ffd93d]✦ Token[/bold #ffd93d]\n"
                f"  [#ffd93d]{last_info}[/#ffd93d]\n"
                f"  [#c0c0c0]{total_info}[/#c0c0c0]"
            )
        self.query_one("#section-tokens", Static).update(token_text)

        current_id = self.agent.get_model_name()
        grouped = self.agent.get_models_grouped()
        total = len(self.agent.available_models)
        self.query_one("#section-models-title", Static).update(
            f"[bold #4d96ff]模型 ({total})[/bold #4d96ff] [#6b7394]点击切换[/#6b7394]"
        )

        option_list = self.query_one("#section-models-list", OptionList)
        option_list.clear_options()
        for provider_name, models in grouped.items():
            option_list.add_option(Option(
                Text(f"── {provider_name} ──", style="#6b7394"), disabled=True
            ))
            for m in models:
                if m.id == current_id:
                    label = Text(f"▶ {m.id}", style="bold #00d4aa")
                else:
                    label = Text(f"  {m.id}", style="#8890a8")
                option_list.add_option(Option(label, id=m.id))

        mcp_status = self.agent.get_mcp_status()
        active_count = sum(1 for s in mcp_status if s["connected"] and not s.get("disabled"))
        self.query_one("#section-mcp-title", Static).update(
            f"[bold #ff922b]MCP Server ({active_count}/{len(mcp_status)})[/bold #ff922b] [#6b7394]点击切换[/#6b7394]"
        )
        mcp_list = self.query_one("#section-mcp-list", OptionList)
        mcp_list.clear_options()
        if not mcp_status:
            mcp_list.add_option(Option(Text("无配置", style="#6b7394"), disabled=True))
        else:
            mcp_sorted = sorted(mcp_status, key=lambda s: (
                s.get("config_disabled", False) or s.get("disabled", False) or not s["connected"],
                s["name"],
            ))
            for s in mcp_sorted:
                name = s["name"]
                if s.get("config_disabled"):
                    label = Text(f"  ○ {name} (配置禁用)", style="#6b7394")
                elif s.get("disabled"):
                    label = Text(f"  ◌ {name} (已禁用 {s['tools_count']}工具)", style="#8890a8")
                elif s["connected"]:
                    label = Text(f"  ● {name} ({s['tools_count']}工具)", style="#6bcb77")
                else:
                    err = s["error"][:20] if s["error"] else "失败"
                    label = Text(f"  ○ {name}: {err}", style="#ff6b6b")
                mcp_list.add_option(Option(label, id=f"mcp__{name}"))

        tool_groups = self.agent.get_tool_groups()
        toggleable = [g for g in tool_groups if g["name"] != "(无分组)" and not g["name"].startswith("mcp__")]
        if toggleable:
            enabled_groups = sum(1 for g in toggleable if not g["disabled"])
            self.query_one("#section-groups-title", Static).update(
                f"[bold #ffd93d]工具分组 ({enabled_groups}/{len(toggleable)})[/bold #ffd93d] [#6b7394]点击切换[/#6b7394]"
            )
            groups_list = self.query_one("#section-groups-list", OptionList)
            groups_list.clear_options()
            toggleable.sort(key=lambda g: (g["disabled"], g["name"]))
            for g in toggleable:
                name = g["name"]
                count = g["count"]
                source = g["source"]
                if g["disabled"]:
                    label = Text(f"  ○ {name} ({count}工具) [已禁用]", style="#ffd93d")
                elif source.startswith("MCP:"):
                    label = Text(f"  ● {name} ({count}工具)", style="#b39ddb")
                elif source == "第三方":
                    label = Text(f"  ● {name} ({count}工具)", style="#4d96ff")
                else:
                    label = Text(f"  ● {name} ({count}工具)", style="#6bcb77")
                groups_list.add_option(Option(label, id=f"group__{name}"))
        else:
            self.query_one("#section-groups-title", Static).update("")
            groups_list = self.query_one("#section-groups-list", OptionList)
            groups_list.clear_options()

        tools = self.agent.get_tools()
        enabled_count = sum(1 for t in tools if not t.get("disabled"))
        self.query_one("#section-tools-title", Static).update(
            f"[bold #6bcb77]函数 ({enabled_count}/{len(tools)})[/bold #6bcb77] [dim #6b7394]点击查看详情[/dim #6b7394]"
        )

        groups = {}
        for t in tools:
            group = t.get("group", "") or "(无分组)"
            if group not in groups:
                groups[group] = {"tools": [], "source": t["source"], "disabled": t.get("disabled", False)}
            groups[group]["tools"].append(t)

        tool_lines = []
        for group_name in sorted(groups.keys(), key=lambda n: (groups[n]["disabled"], n)):
            g = groups[group_name]
            src = g["source"]
            disabled = g["disabled"]
            disabled_tag = " [已禁用]" if disabled else ""
            if disabled:
                tool_lines.append(f"[dim #ffd93d]── {group_name}{disabled_tag} ──[/dim #ffd93d]")
            elif src.startswith("MCP:"):
                tool_lines.append(f"[dim #b39ddb]── {group_name} ──[/dim #b39ddb]")
            elif group_name == "(无分组)":
                tool_lines.append(f"[dim #6b7394]── {group_name} ──[/dim #6b7394]")
            elif src == "第三方":
                tool_lines.append(f"[dim #4d96ff]── {group_name} ──[/dim #4d96ff]")
            else:
                tool_lines.append(f"[dim #6bcb77]── {group_name} ──[/dim #6bcb77]")
            for t in g["tools"]:
                func_name = t.get("func_name", t["name"])
                t_src = t.get("source", "")
                if disabled:
                    tool_lines.append(f"  [#ffd93d]○ {func_name}[/#ffd93d]")
                elif t_src.startswith("MCP:"):
                    tool_lines.append(f"  [#b39ddb]◆[/#b39ddb] [#c0c0c0]{func_name}[/#c0c0c0]")
                elif t_src == "第三方":
                    tool_lines.append(f"  [#4d96ff]●[/#4d96ff] [#c0c0c0]{func_name}[/#c0c0c0]")
                else:
                    tool_lines.append(f"  [#6bcb77]●[/#6bcb77] [#c0c0c0]{func_name}[/#c0c0c0]")
        self.query_one("#section-tools", Static).update("\n".join(tool_lines))

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        if not event.option.id:
            return
        opt_id = event.option.id

        if opt_id.startswith("group__"):
            group_name = opt_id[7:]
            enabled = self.agent.toggle_tool_group(group_name)
            state = "启用" if enabled else "禁用"
            chat = self.app.query_one("#chat-panel", RichLog)
            chat.write(f"[#ffd93d]✦ 工具组 [{group_name}] 已{state}[/#ffd93d]")
            self.update_content()
            return

        if opt_id.startswith("mcp__"):
            server_name = opt_id[5:]
            status = self.agent.get_mcp_status()
            srv = next((s for s in status if s["name"] == server_name), None)
            if srv and srv.get("config_disabled"):
                self.app.notify(f"{server_name} 在配置中禁用，请修改 config.jsonc", severity="warning", timeout=3)
                return
            if srv and not srv["connected"]:
                self.app.notify(f"{server_name} 连接失败，无法切换", severity="warning", timeout=3)
                return
            enabled = self.agent.toggle_mcp_server(server_name)
            state = "启用" if enabled else "禁用"
            chat = self.app.query_one("#chat-panel", RichLog)
            chat.write(f"[#ff922b]✦ MCP [{server_name}] 已{state}[/#ff922b]")
            self.update_content()
            return

        model_id = opt_id
        old = self.agent.get_model_name()
        if model_id == old:
            return
        if self.agent.switch_model(model_id):
            chat = self.app.query_one("#chat-panel", RichLog)
            chat.write(f"\n[bold #ffd93d]✦ 模型已切换:[/bold #ffd93d] [#6b7394]{old}[/#6b7394] → [bold #00d4aa]{self.agent.get_model_name()}[/bold #00d4aa]")
            app = self.app
            if hasattr(app, '_update_subtitle'):
                app._update_subtitle()
            self.update_content()

`````

--- **end of file: nb_agent/tui/widgets/tool_panel.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/tui/widgets/__init__.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/tui/widgets/__init__.py`

#### 📦 Imports

- `from inputs import ChatInput`
- `from inputs import ClickableStatic`
- `from tool_panel import ToolPanel`
- `from screens import ModelSelectScreen`
- `from screens import HelpScreen`
- `from screens import SessionSelectScreen`
- `from screens import ToolDetailScreen`
- `from screens import RoundsInputScreen`
- `from screens import ToolApprovalScreen`
- `from screens import SkillListScreen`
- `from screens import SkillContentScreen`
- `from screens import MentionSelectScreen`
- `from screens import AgentSelectScreen`
- `from screens import AgentContentScreen`
- `from screens import AgentEditScreen`
- `from commands import AgentCommands`


---

`````python
from .inputs import ChatInput, ClickableStatic
from .tool_panel import ToolPanel
from .screens import (
    ModelSelectScreen,
    HelpScreen,
    SessionSelectScreen,
    ToolDetailScreen,
    RoundsInputScreen,
    ToolApprovalScreen,
    SkillListScreen,
    SkillContentScreen,
    MentionSelectScreen,
    AgentSelectScreen,
    AgentContentScreen,
    AgentEditScreen,
)
from .commands import AgentCommands

__all__ = [
    "ChatInput",
    "ClickableStatic",
    "ToolPanel",
    "ModelSelectScreen",
    "HelpScreen",
    "SessionSelectScreen",
    "ToolDetailScreen",
    "RoundsInputScreen",
    "ToolApprovalScreen",
    "SkillListScreen",
    "SkillContentScreen",
    "MentionSelectScreen",
    "AgentSelectScreen",
    "AgentContentScreen",
    "AgentEditScreen",
    "AgentCommands",
]

`````

--- **end of file: nb_agent/tui/widgets/__init__.py** (project: nb_agent) --- 

---


--- **start of file: nb_agent/utils/loggers.py** (project: nb_agent) --- 


### 📄 Python File Metadata: `nb_agent/utils/loggers.py`

#### 📝 Module Docstring

`````
nb_agent 统一日志管理 — 所有模块的 logger 集中定义

所有 logger 统一设置 is_add_stream_handler=False（不向终端输出），
仅写入各自的 log 文件。TUI 层面另有 handler 重定向兜底。
`````

#### 📦 Imports

- `from nb_log import get_logger`


---

`````python
"""nb_agent 统一日志管理 — 所有模块的 logger 集中定义

所有 logger 统一设置 is_add_stream_handler=False（不向终端输出），
仅写入各自的 log 文件。TUI 层面另有 handler 重定向兜底。
"""

from nb_log import get_logger

logger_httpx = get_logger("httpx", 
                          is_add_stream_handler=False,
                          log_filename="nb_agent_httpx.log",
                          )

logger_config = get_logger("nb_agent.config",
                            is_add_stream_handler=False,
                            log_filename="nb_agent_config.log")

logger_mcp = get_logger("nb_agent.mcp",
                         is_add_stream_handler=False,
                         log_filename="nb_agent_mcp.log")

logger_llm_call = get_logger("nb_agent.llm_call",
                         is_add_stream_handler=False,
                         log_filename="nb_agent_llm_call.log",
                         )

logger_llm_call_raw = get_logger("nb_agent.llm_call_raw",
                               is_add_stream_handler=False,
                               log_filename="nb_agent_llm_call_raw.log",
                               )
`````

--- **end of file: nb_agent/utils/loggers.py** (project: nb_agent) --- 

---

# markdown content namespace: 项目文档 


## nb_agent File Tree (relative dir: `.`)


`````

└── nb_agent_config_jsonc_abount.md

`````

---


## nb_agent (relative dir: `.`)  Included Files (total: 1 files)


- `nb_agent_config_jsonc_abount.md`


---


--- **start of file: nb_agent_config_jsonc_abount.md** (project: nb_agent) --- 

`````markdown
# config.jsonc 配置说明

## 概述

`config.jsonc` 是 nb_agent 的 JSONC 格式配置文件（JSONC 支持 `//` 注释和尾逗号），放在项目根目录即可。

**配置优先级：** CLI 参数 > 环境变量 > 项目级 `./config.jsonc` > 全局 `~/.nb_agent/config.jsonc` > 默认值

**环境变量替换：** 配置中的任何字符串值都可以使用 `{env:变量名}` 语法从环境变量读取，缺失的环境变量会被替换为空字符串。

```jsonc
// 示例：api_key 从环境变量 DEEPSEEK_API_KEY 读取
"api_key": "{env:DEEPSEEK_API_KEY}"
```

---

## 完整配置结构

```jsonc
{
    "provider": { /* LLM 提供商 */ },
    "agent":    { /* Agent 行为 */ },
    "mcp":      { /* MCP Server */ },
    "approval": { /* 审批规则 */ },
    "session":  { /* 会话存储 */ },
    "ui":       { /* 界面设置 */ }
}
```

---

## 1. provider — LLM 提供商

配置一个或多个 LLM 提供商（API 代理），每个提供商下可定义多个模型。

```jsonc
"provider": {
    "提供商ID，随意命名": {
        "name":     "显示名称（可选，UI 中展示）",
        "base_url": "API 地址，例如 https://api.deepseek.com/v1",
        "api_key":  "API Key，支持 {env:XXX}",
        "models": {
            "模型ID": {
                "name":  "显示名称",
                "limit": {
                    "context": 64000,   // 上下文窗口 token 数
                    "output":  8192     // 最大输出 token 数
                }
            }
        }
    }
}
```

### 完整示例

**示例 A：直连 DeepSeek 官方 API**

```jsonc
"provider": {
    "deepseek": {
        "name": "DeepSeek",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": "{env:DEEPSEEK_API_KEY}",
        "models": {
            "deepseek-chat": {
                "name": "DeepSeek V3",
                "limit": { "context": 64000, "output": 8192 }
            },
            "deepseek-reasoner": {
                "name": "DeepSeek R1",
                "limit": { "context": 64000, "output": 8192 }
            }
        }
    }
}
```

**示例 B：通过 LiteLLM Proxy 聚合多个模型**

```jsonc
"provider": {
    "litellm": {
        "name": "LiteLLM Proxy",
        "base_url": "http://localhost:4000/v1",
        "api_key": "not-needed",
        "models": {
            "aku-qwen3.5-397b": {
                "name": "Qwen3.5 397B",
                "limit": { "context": 131072, "output": 65536 }
            },
            "ark-deepseek-v3.2": {
                "name": "DeepSeek V3.2",
                "limit": { "context": 131072, "output": 65536 }
            }
        }
    }
}
```

> **模型 ID 规则：** `provider` 下的模型 ID 必须与 API 返回的 `model` 字段一致。LiteLLM 的模型 ID 就是 `litellm` 路由中配置的名称。

---

## 2. agent — Agent 行为

```jsonc
"agent": {
    "system_prompt":       "系统提示词，定义 AI 的角色和行为",
    "default_model":       "默认使用的模型 ID（对应 provider 中某个模型）",
    "max_context_tokens":  0,       // 上下文窗口上限，0=使用模型默认值
    "streaming":           true     // 是否启用流式输出
}
```

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `system_prompt` | string | `"你是一个智能助手。"` | 系统提示词，会追加当前日期和 Skills 清单 |
| `default_model` | string | 空=自动选第一个 | 默认使用的模型 ID |
| `max_context_tokens` | int | `0` | 上下文窗口上限，0 表示使用模型的 context limit |
| `streaming` | bool | `true` | 流式输出开关，false 为非流式 |

---

## 3. mcp — MCP Server 配置

nb_agent 支持四种 MCP 传输方式：

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| `local` | 启动子进程，通过 stdio 通信 | 本地安装的工具/自定义 MCP |
| `sse` | 通过 SSE 连接远程 MCP Server | Docker 部署的 Web 服务 |
| `http` / `streamableHttp` | 通过 Streamable HTTP 连接 | 独立启动的 HTTP MCP 服务 |

### 3.1 local — 本地 stdio 方式

```jsonc
"mcp_server_name": {
    "type":    "local",
    "command": "可执行文件",                          // 字符串
    // 或
    "command": ["python", "mcp_servers/xxx.py"],     // 数组（推荐，自动拆分）
    // 可选字段：
    "args":          ["--port", "3000"],             // 额外参数，会追加到 command 后面
    "environment":   { "REDIS_URL": "redis://..." }, // 自定义环境变量
    "cwd":           "D:/your/project",              // 工作目录，默认=项目根目录
    "init_timeout":  60,                             // 初始化超时秒数，默认 60
    "enabled":       true                            // 是否启用，默认 true
}
```

**`command` 是字符串还是数组？**

两种写法都支持：
- **字符串**：`"command": "python mcp_servers/xxx.py"` — 简单场景用
- **数组（推荐）**：`"command": ["python", "mcp_servers/xxx.py"]` — 带空格路径更安全

`args` 是可选的，它会被追加到 `command` 后面。下面两种写法等价：

```jsonc
// 写法一：全写在 command 里
"command": ["serena", "start-mcp-server", "--project", "D:/codes/my_project"]

// 写法二：拆分 command + args
"command": "serena",
"args":    ["start-mcp-server", "--project", "D:/codes/my_project"]
```

**local 模式示例：**

```jsonc
"mcp": {
    // 示例 1：启动自定义 FastMCP（你写的 Python MCP Server）
    "bookmark": {
        "type": "local",
        "command": ["python", "mcp_servers/bookmark_server.py"],
        "enabled": true
    },

    // 示例 2：带环境变量的 Redis 工具 MCP
    "redis-tools": {
        "type": "local",
        "command": ["python", "mcp_servers/redis_tools_server.py"],
        "environment": {
            "REDIS_URL": "redis://localhost:6379"
        },
        "enabled": true
    },

    // 示例 3：npx 启动第三方 MCP
    "context7": {
        "type": "local",
        "command": ["npx", "-y", "@upstash/context7-mcp@latest"],
        "enabled": false
    },

    // 示例 4：文件系统 MCP（必须指定目录绝对路径）
    "filesystem": {
        "type": "local",
        "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "D:/codes/my_project"],
        "enabled": false
    },

    // 示例 5：Serena 编程 MCP
    "serena": {
        "type": "local",
        "command": ["serena", "start-mcp-server", "--project", "D:/codes/my_project"],
        "enabled": false
    },

    // 示例 6：command + args 拆分写法（兼容 Cursor/Cline 风格配置，直接复制迁移）
    // 第三方配置常有: command="npx", args=["-y", "@xxx/server", "/path"]
    // 拆过来只需把 command 和 args 原样搬过来即可，不需要手动合并
    "my-mcp": {
        "type": "local",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/codes/my_project"],
        "enabled": false
    }
}
```

### 3.2 sse — SSE 连接方式

```jsonc
"mcp_server_name": {
    "type":    "sse",
    "url":     "http://localhost:3000/sse",     // SSE 端点地址
    "headers": { "Authorization": "..." },       // 可选：自定义请求头
    "init_timeout": 30,                          // 可选：初始化超时秒数，默认 30
    "enabled": true                              // 可选：默认 true
}
```

**示例：**

```jsonc
// 先启动：docker run -d --name web-search -p 3000:3000 -e ENABLE_CORS=true ghcr.io/aas-ee/open-web-search:latest
"web-search": {
    "type": "sse",
    "url": "http://localhost:3000/sse",
    "enabled": true
}
```

### 3.3 http / streamableHttp — HTTP 连接方式

`http` 是 `streamableHttp` 的别名，两者完全等价。

```jsonc
"mcp_server_name": {
    "type":    "http",                           // 或 "streamableHttp"
    "url":     "http://localhost:9101/mcp",      // MCP 端点地址
    "headers": { "Authorization": "..." },        // 可选：自定义请求头
    "init_timeout": 30,                           // 可选：初始化超时秒数，默认 30
    "enabled": true                               // 可选：默认 true
}
```

**示例：**

```jsonc
// 先启动 nbrag 服务：uvx nbrag --transport streamable-http --port 9101
// 环境变量：NBRAG_API_KEY（访问 LLM 所需）
"nbrag": {
    "type": "http",
    "url": "http://localhost:9101/mcp"
}
```

---

## 4. approval — 审批规则

危险工具执行前，TUI 会弹窗让用户确认。

```jsonc
"approval": {
    "dangerous_tools": [
        "note__delete_note",                     // 工具名（精确匹配）
        "mcp__redis-tools__redis_smart_set"      // MCP 工具名格式: mcp__{server}__{tool}
    ],
    "auto_approve": false                        // true=所有操作自动放行（不弹窗）
}
```

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `dangerous_tools` | string[] | `[]` | 需要审批的工具名列表 |
| `auto_approve` | bool | `false` | true = 全部自动放行，不弹窗 |

**工具名规则：**
- 内置工具：直接写函数名，如 `note__delete_note`
- MCP 工具：格式为 `mcp__服务器名__工具名`，如 `mcp__redis-tools__redis_smart_set`

> 如需更灵活的审批逻辑（如按参数值判断），可编写 `approval_rules.py` 自定义规则函数，代码的表达能力比配置更强。

---

## 5. session — 会话存储

```jsonc
"session": {
    "db_path": ""    // 空字符串 = 默认 ~/.nb_agent/sessions.db
}
```

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `db_path` | string | `""` | SQLite 数据库路径，空 = `~/.nb_agent/sessions.db` |

会话数据包括：对话历史、Agent 预设配置（工具组/MCP/Skills 开关）。

---

## 6. ui — 界面设置

```jsonc
"ui": {
    "theme":             "dark",    // 主题：目前仅 "dark"
    "show_tool_panel":   true,      // 是否显示右侧工具/MCP/模型面板
    "show_token_usage":  true       // 是否在底部状态栏显示 Token 用量
}
```

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `theme` | string | `"dark"` | 主题，目前仅支持 `"dark"` |
| `show_tool_panel` | bool | `true` | 右侧面板开关（工具/MCP/模型列表） |
| `show_token_usage` | bool | `true` | 底部状态栏 Token 统计 |

---

## 完整配置示例

```jsonc
{
    "agent": {
        "system_prompt": "你是一个智能助手，可以调用工具来帮助用户解决问题。请用中文回答。",
        "default_model": "deepseek-chat",
        "streaming": true
    },

    "provider": {
        "deepseek": {
            "name": "DeepSeek",
            "base_url": "https://api.deepseek.com/v1",
            "api_key": "{env:DEEPSEEK_API_KEY}",
            "models": {
                "deepseek-chat": {
                    "name": "DeepSeek V3",
                    "limit": { "context": 64000, "output": 8192 }
                },
                "deepseek-reasoner": {
                    "name": "DeepSeek R1",
                    "limit": { "context": 64000, "output": 8192 }
                }
            }
        }
    },

    "mcp": {
        "context7": {
            "type": "local",
            "command": ["npx", "-y", "@upstash/context7-mcp@latest"],
            "enabled": false
        },
        "serena": {
            "type": "local",
            "command": ["serena", "start-mcp-server", "--project", "D:/codes/my_project"],
            "enabled": false
        },
        "nbrag": {
            "type": "http",
            "url": "http://localhost:9101/mcp"
        }
    },

    "approval": {
        "dangerous_tools": [],
        "auto_approve": false
    },

    "session": {
        "db_path": ""
    },

    "ui": {
        "theme": "dark",
        "show_tool_panel": true,
        "show_token_usage": true
    }
}
```

---

## 常见问题

**Q: 如何设置 API Key？**

方式一（推荐）：使用环境变量替换 `"api_key": "{env:DEEPSEEK_API_KEY}"`，然后在终端设置 `$env:DEEPSEEK_API_KEY="sk-xxx"` 或写入 `.env` 文件。

方式二：直接写在配置里（不推荐，仅限本地开发）。

**Q: MCP 的 `command` 用字符串还是数组？**

都支持。带空格、特殊字符的路径用数组更安全。`args` 可选，会被追加到 `command` 后面。

**Q: `http` 和 `streamableHttp` 有什么区别？**

没有区别，`http` 是 `streamableHttp` 的别名。

**Q: MCP 怎么传环境变量？**

使用 `environment` 字段，例如：

```jsonc
"my-mcp": {
    "type": "local",
    "command": ["python", "server.py"],
    "environment": {
        "NBRAG_API_KEY": "{env:NBRAG_API_KEY}",
        "MY_VAR": "my_value"
    }
}
```

**Q: 配置写错了怎么排查？**

启动时控制台会打印 MCP 连接状态和错误信息。也可以在 TUI 右侧面板查看每个 MCP Server 的连接状态和错误原因。

`````

--- **end of file: nb_agent_config_jsonc_abount.md** (project: nb_agent) --- 

---

