
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **此文档生成时间**：2026-05-26 11:43:49
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
# markdown content namespace: learn_agent project summary 



- `learn_agent` 是一个学习型 AI Agent 项目，模仿 OpenCode 的架构设计。
- 支持 TUI（Terminal User Interface）交互、MCP 工具调用、RAG 知识库检索、多轮对话等功能。
- 核心模块：
  - `agent/`: Agent 核心逻辑（对话循环、MCP 客户端、会话管理、审批规则）
  - `ui/`: 基于 Textual 的 TUI 界面（彩虹跑马灯、计时器等炫酷效果）
  - `mcp_servers/`: MCP 服务端（Redis 工具、系统工具、开发者工具包）
  - `rag/`: RAG 检索增强生成（ChromaDB + SiliconFlow 向量化 + Rerank）
  - `tools/`: 内置工具集（文件操作、Shell 执行等）
- 入口：`main.py` 启动 Textual TUI 应用
- 配置：`config.jsonc` 集中管理模型、MCP、RAG 等配置


## 📋 learn_agent most core source files metadata (Entry Points)


以下是项目 learn_agent 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project learn_agent most core source code files as follows: 
- `learn_agent/__init__.py`
- `learn_agent/main.py`
- `learn_agent/config.jsonc`
- `learn_agent/config_loader.py`
- `learn_agent/agent/core.py`
- `learn_agent/agent/mcp_client.py`
- `learn_agent/agent/approval_rules.py`
- `learn_agent/ui/app.py`


### 📄 Python File Metadata: `learn_agent/__init__.py`


---




### 📄 Python File Metadata: `learn_agent/main.py`

#### 📝 Module Docstring

`````
Learn Agent —— 入口

使用方法:
    conda activate py312
    python main.py
`````

#### 📦 Imports

- `import os`
- `import sys`
- `from config_loader import CONFIG`
- `from ui.app import AgentApp`

#### 🔧 Public Functions (1)

- `def main()`
  - *Line: 18*


---




### 📄 Python File Metadata: `learn_agent/config_loader.py`

#### 📝 Module Docstring

`````
config.jsonc 配置加载器 —— 与 config.jsonc 同目录

支持 {env:VARIABLE_NAME} 语法从环境变量读取值（参考 OpenCode 设计）。
缺失的环境变量会替换为空字符串。

用法:
    from config_loader import CONFIG

    rag = CONFIG["rag"]
    mcp = CONFIG["mcp"]
    agent = CONFIG["agent"]
`````

#### 📦 Imports

- `import os`
- `import re`
- `import json5`
- `from dotenv import load_dotenv`


---




### 📄 Python File Metadata: `learn_agent/agent/core.py`

#### 📝 Module Docstring

`````
Agent 核心 —— 真实 LLM + Function Calling + 工具调用

核心循环：
  用户输入 → LLM(messages + tools) → 判断:
    有 tool_calls → 执行工具 → 结果回传 LLM → 再次判断（可能多轮）
    无 tool_calls → 返回文本回复
`````

#### 📦 Imports

- `import asyncio`
- `import functools`
- `import json`
- `import uuid`
- `from dataclasses import dataclass`
- `from dataclasses import field`
- `from typing import AsyncIterator`
- `from typing import List`
- `from typing import Dict`
- `from typing import Optional`
- `from typing import Callable`
- `from openai import AsyncOpenAI`
- `from openai import APITimeoutError`
- `from openai import RateLimitError`
- `from openai import APIConnectionError`
- `from agent.session import SessionStore`
- `from agent.mcp_client import MCPManager`
- `from agent.approval_rules import ApprovalEngine`
- `from tools import TOOL_REGISTRY`
- `import os`

#### 🏛️ Classes (4)

##### 📌 `class ToolCallRecord`
*Line: 27*

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
*Line: 36*

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
*Line: 45*

**Docstring:**
`````
模型信息
`````

**Class Variables (8):**
- `id: str`
- `name: str`
- `provider: str`
- `provider_name: str`
- `base_url: str`
- `api_key: str`
- `context_limit: int = 0`
- `output_limit: int = 0`

##### 📌 `class AgentCore`
*Line: 89*

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

**Public Methods (16):**
- `async def chat(self, user_input: str) -> AgentResponse`
  - **Docstring:**
  `````
  Agent 主循环：
  1. 发送 messages + tools 给 LLM
  2. 如果 LLM 返回 tool_calls → 执行 → 结果回传 → 重新调 LLM
  3. 如果 LLM 返回文本 → 结束，返回给用户
  `````
- `async def chat_stream(self, user_input: str) -> AsyncIterator[str]`
  - **Docstring:**
  `````
  流式版本。工具调用阶段用非流式（需要完整 tool_calls），
  最终回复用流式输出。
  `````
- `def register_tool(self, name: str, func: Callable, description: str, parameters: dict)`
  - *注册自定义工具*
- `async def connect_mcp(self)`
  - *连接配置中的所有 MCP Server*
- `async def disconnect_mcp(self)`
  - *断开所有 MCP Server*
- `def switch_model(self, model_id: str) -> bool`
- `def get_models_grouped(self) -> Dict[str, List[ModelInfo]]`
- `async def generate_smart_title(self)`
  - *用 LLM 生成一个简短的会话标题（首轮对话后调用）*
- `def clear_history(self)`
- `def get_session_list(self, limit: int = 50) -> list`
- `def get_tools(self) -> list`
- `def get_mcp_status(self) -> list`
- `def toggle_mcp_server(self, name: str) -> bool`
  - *切换 MCP Server 启用/禁用，返回新的启用状态*
- `def get_model_name(self) -> str`
- `def get_model_display_name(self) -> str`
- `def get_token_usage(self) -> dict`

**Class Variables (4):**
- `MAX_TOOL_ROUNDS = 30`
- `MAX_RETRIES = 3`
- `RETRY_DELAYS = [1, 3, 5]`
- `RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, APIConnectionError, ConnectionError, TimeoutError)`

#### 🔧 Public Functions (1)

- `def load_models_from_config(config: dict) -> List[ModelInfo]`
  - *Line: 64*
  - *从 config.jsonc 的 provider 节解析所有模型*


---




### 📄 Python File Metadata: `learn_agent/agent/mcp_client.py`

#### 📝 Module Docstring

`````
MCP 客户端管理器 —— 连接多个 MCP Server，统一管理工具

支持三种传输方式:
  - local (stdio): 启动子进程，通过 stdin/stdout 通信
  - sse: 通过 SSE (Server-Sent Events) 连接远程 MCP Server
  - streamableHttp: 通过 Streamable HTTP 连接远程 MCP Server

使用方式:
    manager = MCPManager()
    await manager.connect_all(config["mcp"])
    tools = manager.get_all_tools_openai_format()
    result = await manager.call_tool("mcp__server__tool", {"arg": "val"})
    await manager.disconnect_all()
`````

#### 📦 Imports

- `import asyncio`
- `import contextlib`
- `import json`
- `import logging`
- `import os`
- `from typing import Dict`
- `from typing import List`
- `from typing import Optional`
- `from typing import Any`
- `from mcp import ClientSession`
- `from mcp.client.stdio import stdio_client`
- `from mcp.client.stdio import StdioServerParameters`
- `from mcp.client.sse import sse_client`
- `from mcp.client.streamable_http import streamablehttp_client`

#### 🏛️ Classes (2)

##### 📌 `class MCPServerInfo`
*Line: 47*

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

##### 📌 `class MCPManager`
*Line: 59*

**Docstring:**
`````
管理多个 MCP Server 的连接和工具调用
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self)`
  - **Parameters:**
    - `self`

**Public Methods (10):**
- `async def connect_all(self, mcp_config: dict, project_root: str = '')`
  - **Docstring:**
  `````
  根据配置连接所有 MCP Server
  
  SSE/HTTP 连接必须在调用者任务中初始化（anyio cancel scope 要求），
  因此只有 stdio 类型才能用 asyncio.gather 并发启动。
  `````
- `async def connect_server(self, name: str, cfg: dict)`
  - *连接单个 MCP Server（支持 local/sse/streamableHttp 三种传输）*
- `async def disconnect_all(self)`
  - *断开所有 MCP Server*
- `def toggle_server(self, name: str) -> bool`
  - *切换 Server 启用/禁用状态，返回新的启用状态（True=启用）*
- `def is_server_disabled(self, name: str) -> bool`
- `def get_all_tools_openai_format(self) -> List[dict]`
  - *将所有 MCP 工具转换为 OpenAI function calling 格式（跳过禁用的 Server）*
- `def get_tool_info_list(self) -> List[dict]`
  - *获取所有工具的简要信息（用于 TUI 显示，跳过禁用的 Server）*
- `def get_server_status(self) -> List[dict]`
  - *获取所有 Server 的状态（包括已连接、已禁用、连接失败、配置禁用）*
- `async def call_tool(self, full_tool_name: str, arguments: dict) -> str`
  - **Docstring:**
  `````
  调用 MCP 工具。
  full_tool_name 格式: mcp__{server_name}__{tool_name}
  `````
- `def is_mcp_tool(self, tool_name: str) -> bool`
  - *判断是否为 MCP 工具（名称以 mcp__ 开头）*


---




### 📄 Python File Metadata: `learn_agent/agent/approval_rules.py`

#### 📝 Module Docstring

`````
工具审批规则引擎

职责：判断工具调用是否需要用户确认。
设计：可插拔规则列表，每条规则是一个 (tool_name, tool_kwargs) -> bool 的函数。

使用方式:
    engine = ApprovalEngine()
    if engine.needs_approval("mcp__redis-tools__redis_execute", {"command": "DEL foo"}):
        # 弹窗问用户
        ...

扩展规则:
    1. 在本文件末尾的 DEFAULT_RULES 列表中添加新规则函数
    2. 或调用 engine.add_rule(my_rule_func) 动态添加
`````

#### 📦 Imports

- `from typing import Callable`
- `from typing import List`
- `from typing import Optional`

#### 🏛️ Classes (1)

##### 📌 `class ApprovalEngine`
*Line: 72*

**Docstring:**
`````
工具审批规则引擎。

初始化时加载 DEFAULT_RULES，也可动态添加/移除规则。
core.py 和 app.py 只需调用 engine.needs_approval(tool_name, tool_kwargs)，
不需要知道具体规则逻辑。
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, rules: Optional[List[Callable]] = None)`
  - **Parameters:**
    - `self`
    - `rules: Optional[List[Callable]] = None`

**Public Methods (3):**
- `def needs_approval(self, tool_name: str, tool_kwargs: dict) -> bool`
  - *检查是否有任一规则命中*
- `def add_rule(self, rule: Callable)`
  - *动态添加规则*
- `def remove_rule(self, rule: Callable)`
  - *动态移除规则*

#### 🔧 Public Functions (2)

- `def rule_redis_write(tool_name: str, tool_kwargs: dict) -> bool`
  - *Line: 48*
  - *redis_execute 中的写命令需要审批，只读命令放行*

- `def rule_dangerous_tools(tool_name: str, tool_kwargs: dict) -> bool`
  - *Line: 58*
  - *ALWAYS_APPROVE_TOOLS 名单中的工具始终需要审批*


---




### 📄 Python File Metadata: `learn_agent/ui/app.py`

#### 📝 Module Docstring

`````
TUI 界面 —— 用 Textual 框架构建

布局:
┌─────────────────────────────────────────────────┐
│  Learn Agent | deepseek-v4-flash | Tokens: 0    │  ← Header
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
- `import json`
- `import os`
- `import sys`
- `import time`
- `from typing import Optional`
- `from textual.app import App`
- `from textual.app import ComposeResult`
- `from textual.containers import Horizontal`
- `from textual.containers import Vertical`
- `from textual.containers import VerticalScroll`
- `from textual.widgets import Footer`
- `from textual.widgets import Header`
- `from textual.widgets import OptionList`
- `from textual.widgets import RichLog`
- `from textual.widgets import Static`
- `from textual.widgets import TextArea`
- `from textual.widgets import Input`
- `from textual.widgets.option_list import Option`
- `from textual.binding import Binding`
- `from textual.screen import ModalScreen`
- `from textual.command import Hit`
- `from textual.command import Hits`
- `from textual.command import Provider`
- `from textual.command import DiscoveryHit`
- `from textual.events import Key`
- `from rich.text import Text`
- `from rich.markdown import Markdown as RichMarkdown`
- `from rich.panel import Panel`
- `from rich.box import ROUNDED`
- `from agent.core import AgentCore`
- `import os`
- `import re`
- `from datetime import datetime`

#### 🏛️ Classes (11)

##### 📌 `class ChatInput(TextArea)`
*Line: 72*

**Docstring:**
`````
聊天输入框：Enter=换行，Ctrl+Enter(ctrl+j)=发送
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, **kwargs)`
  - **Parameters:**
    - `self`
    - `**kwargs`

##### 📌 `class ClickableStatic(Static)`
*Line: 80*

**Docstring:**
`````
可点击的 Static 组件 — 点击时打开工具详情
`````

**Public Methods (1):**
- `def on_click(self, event)`

##### 📌 `class ToolPanel(Vertical)`
*Line: 89*

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
  - *处理模型点击切换 或 MCP 点击切换*

##### 📌 `class ModelSelectScreen(ModalScreen[str])`
*Line: 217*

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
*Line: 259*

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
*Line: 321*

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
*Line: 371*

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
*Line: 408*

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
  - *Input 组件的 Enter 提交事件*
- `def action_confirm(self)`
  - *Binding 回调（备用）*
- `def action_cancel(self)`

**Class Variables (1):**
- `BINDINGS = [Binding('escape', 'cancel', '取消')]`

##### 📌 `class ToolApprovalScreen(ModalScreen[bool])`
*Line: 451*

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

##### 📌 `class AgentCommands(Provider)`
*Line: 484*

**Docstring:**
`````
命令面板: 提供会话管理、导出、设置等操作
`````

**Public Methods (2):**
- `async def discover(self) -> Hits`
  - *默认展示所有命令（不与底部状态栏重复）*
- `async def search(self, query: str) -> Hits`
  - *搜索命令*

##### 📌 `class AgentApp(App)`
*Line: 521*

**Docstring:**
`````
Learn Agent TUI 主应用
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, config: dict)`
  - **Parameters:**
    - `self`
    - `config: dict`

**Public Methods (12):**
- `def compose(self) -> ComposeResult`
- `async def on_mount(self)`
- `def action_stop_ai(self)`
  - *Esc: 弹窗打开时关闭弹窗，否则终止 AI 回答*
- `def action_edit_last(self)`
  - *Ctrl+↑: 编辑上一轮提问*
- `async def action_send_msg(self)`
  - *Ctrl+Enter 发送消息*
- `def action_new_session(self)`
  - *Ctrl+N: 新建会话*
- `def action_resume_session(self)`
  - *Ctrl+R: 打开会话选择弹窗*
- `def action_show_help(self)`
  - *显示帮助弹窗*
- `def action_toggle_input(self)`
  - *展开/收起输入框*
- `async def on_unmount(self)`
  - *应用退出时断开 MCP 连接*
- `def action_clear_chat(self)`
- `def action_select_model(self)`
  - *打开模型选择弹窗*

**Class Variables (4):**
- `TITLE = 'Learn Agent'`
- `CSS_PATH = 'styles.tcss'`
- `COMMANDS = App.COMMANDS | {AgentCommands}`
- `BINDINGS = [Binding('ctrl+j', 'send_msg', '发送', show=True, priority=True), Binding('ctrl+k', 'stop_ai', '终止', show=True, priority=True), Binding('ctrl+up', 'edit_last', '编辑上轮', show=True, priority=True), Binding('tab', 'select_model', '模型', show=True, priority=True), Binding('ctrl+n', 'new_session', '新建', show=True, priority=True), Binding('ctrl+r', 'resume_session', '恢复', show=True, priority=True), Binding('ctrl+e', 'toggle_input', '展开', show=True, priority=True), Binding('ctrl+l', 'clear_chat', '清屏', show=True), Binding('f1', 'show_help', '帮助', show=True), Binding('ctrl+q', 'quit', '退出', show=True, priority=True)]`


---



## 🔗 learn_agent Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ learn_agent/__init__.py
  ★ learn_agent/agent/approval_rules.py
  ★ learn_agent/agent/core.py
  ★ learn_agent/agent/mcp_client.py
  ★ learn_agent/config_loader.py
  ★ learn_agent/main.py
  ★ learn_agent/ui/app.py

`````

### 📋 Detailed Dependencies

### 📦 Third-party Dependencies

项目使用的第三方库：

- `agent`
- `config_loader`
- `dotenv`
- `json5`
- `mcp`
- `openai`
- `rich`
- `textual`
- `tools`
- `ui`
- ......以及更多的第三方库......


---
# markdown content namespace: learn_agent codes 


## learn_agent File Tree (relative dir: `learn_agent`)


`````

└── learn_agent
    ├── __init__.py
    ├── agent
    │   ├── __init__.py
    │   ├── approval_rules.py
    │   ├── core.py
    │   ├── mcp_client.py
    │   └── session.py
    ├── config.jsonc
    ├── config_loader.py
    ├── main.py
    ├── mcp_servers
    │   ├── dev_toolkit_server.py
    │   ├── redis_tools_server.py
    │   ├── start_mcp_http_scripts
    │   │   ├── start_all_mcp.py
    │   │   ├── start_rag_mcp.py
    │   │   └── start_serena_mcp.py
    │   └── system_tools_server.py
    ├── rag
    │   ├── RAG_OPTIMIZATION_PLAN.md
    │   ├── __init__.py
    │   ├── chunker.py
    │   ├── core.py
    │   ├── import_funboost.py
    │   ├── mcp_server.py
    │   └── readme.md
    ├── requirements.txt
    ├── task.md
    ├── tools
    │   ├── __init__.py
    │   ├── base.py
    │   ├── builtin.py
    │   └── extra_serena_tools.py
    └── ui
        ├── __init__.py
        ├── app.py
        └── styles.tcss

`````

---


## learn_agent (relative dir: `learn_agent`)  Included Files (total: 31 files)


- `learn_agent/config.jsonc`

- `learn_agent/config_loader.py`

- `learn_agent/main.py`

- `learn_agent/requirements.txt`

- `learn_agent/task.md`

- `learn_agent/__init__.py`

- `learn_agent/agent/approval_rules.py`

- `learn_agent/agent/core.py`

- `learn_agent/agent/mcp_client.py`

- `learn_agent/agent/session.py`

- `learn_agent/agent/__init__.py`

- `learn_agent/mcp_servers/dev_toolkit_server.py`

- `learn_agent/mcp_servers/redis_tools_server.py`

- `learn_agent/mcp_servers/system_tools_server.py`

- `learn_agent/mcp_servers/start_mcp_http_scripts/start_all_mcp.py`

- `learn_agent/mcp_servers/start_mcp_http_scripts/start_rag_mcp.py`

- `learn_agent/mcp_servers/start_mcp_http_scripts/start_serena_mcp.py`

- `learn_agent/rag/chunker.py`

- `learn_agent/rag/core.py`

- `learn_agent/rag/import_funboost.py`

- `learn_agent/rag/mcp_server.py`

- `learn_agent/rag/RAG_OPTIMIZATION_PLAN.md`

- `learn_agent/rag/readme.md`

- `learn_agent/rag/__init__.py`

- `learn_agent/tools/base.py`

- `learn_agent/tools/builtin.py`

- `learn_agent/tools/extra_serena_tools.py`

- `learn_agent/tools/__init__.py`

- `learn_agent/ui/app.py`

- `learn_agent/ui/styles.tcss`

- `learn_agent/ui/__init__.py`


---


--- **start of file: learn_agent/config.jsonc** (project: learn_agent) --- 

`````text
{
    // ====== Agent 配置 ======
    "agent": {
        "name": "Learn Agent",
        "default_model": "ark-kimi-k2.6",
        "system_prompt": "你是一个智能助手，可以调用工具来帮助用户解决问题。请用中文回答。\n\n重要规则：当你需要通过命令行运行 Python 脚本时，必须先设置 PYTHONPATH 环境变量为项目根目录。因为 IDE（VSCode/PyCharm）会自动把项目根目录加到 PYTHONPATH，但命令行不会。\n示例：\n- Windows CMD: set PYTHONPATH=D:/codes/myproject && python script.py\n- PowerShell: $env:PYTHONPATH='D:/codes/myproject'; python script.py\n- Linux/Mac: PYTHONPATH=D:/codes/myproject python script.py\n\nweb-search 搜索策略：\n- engines 可选值：baidu, bing, duckduckgo, sogou, startpage, brave, exa, csdn, juejin\n- 每次搜索必须使用以下多个引擎 [\"baidu\",\"bing\",\"duckduckgo\",\"sogou\",\"startpage\",\"brave\",\"exa\",\"csdn\",\"juejin\"]，limit 设为 50（最大值），因为很多引擎会返回空结果\n- 搜索完成后，从所有结果中筛选出质量最高、最相关的 10 条，用 fetchWebContent 工具逐一抓取这 10 条的详情全文\n- 最终整理为结构化的摘要呈现给用户",
        "max_context_tokens": 32000,
        "streaming": true
    },

    // ====== Provider + 模型配置（格式参考 OpenCode） ======
    "provider": {
        "litellm": {
            "name": "LiteLLM Proxy",
            "base_url": "http://localhost:4000/v1",
            "api_key": "not-needed",
            "models": {
                "ds-deepseek-v4-flash": {
                    "name": "DeepSeek V4 Flash (官方直连)",
                    "limit": {
                        "context": 1000000,
                        "output": 384000
                    }
                },
                "ds-deepseek-v4-pro": {
                    "name": "DeepSeek V4 Pro (官方直连)",
                    "limit": {
                        "context": 1000000,
                        "output": 384000
                    }
                },
                "aku-qwen3.5-397b": {
                    "name": "Qwen3.5 397B (公司)",
                    "limit": {
                        "context": 131072,
                        "output": 65536
                    }
                },
                "aku-qwen3.6-35b": {
                    "name": "Qwen3.6 35B (公司)",
                    "limit": {
                        "context": 131072,
                        "output": 65536
                    }
                },
                "ark-code-latest": {
                    "name": "Coding Plan Auto (方舟)",
                    "limit": { "context": 200000, "output": 64000 }
                },
                "ark-doubao-seed-code": {
                    "name": "Doubao Seed Code (方舟)",
                    "limit": { "context": 200000, "output": 64000 }
                },
                "ark-deepseek-v3.2": {
                    "name": "DeepSeek V3.2 (方舟)",
                    "limit": { "context": 131072, "output": 65536 }
                },
                "ark-doubao-seed-2.0-code": {
                    "name": "Doubao Seed 2.0 Code (方舟)",
                    "limit": { "context": 200000, "output": 64000 }
                },
                "ark-doubao-seed-2.0-pro": {
                    "name": "Doubao Seed 2.0 Pro (方舟)",
                    "limit": { "context": 200000, "output": 64000 }
                },
                "ark-doubao-seed-2.0-lite": {
                    "name": "Doubao Seed 2.0 Lite (方舟)",
                    "limit": { "context": 200000, "output": 64000 }
                },
                "ark-minimax-m2.7": {
                    "name": "MiniMax M2.7 (方舟)",
                    "limit": { "context": 204800, "output": 204800 }
                },
                "ark-glm-5.1": {
                    "name": "GLM-5.1 (方舟)",
                    "limit": { "context": 200000, "output": 131072 }
                },
                "ark-kimi-k2.6": {
                    "name": "Kimi K2.6 (方舟)",
                    "limit": { "context": 262144, "output": 262144 }
                },
                "ark-deepseek-v4-flash": {
                    "name": "DeepSeek V4 Flash (方舟)",
                    "limit": { "context": 1000000, "output": 384000 }
                },
                "ark-deepseek-v4-pro": {
                    "name": "DeepSeek V4 Pro (方舟)",
                    "limit": { "context": 1000000, "output": 384000 }
                }
            }
        }
    },

    // ====== 记忆配置 ======
    "memory": {
        "session_db": "chat_history.db",
        "long_term": false
    },

    // ====== RAG 知识库配置 ======
    "rag": {
        "siliconflow_api_key": "{env:SILICONFLOW_API_KEY}",
        "embedding_base_url": "https://api.siliconflow.cn/v1",
        "embedding_model": "BAAI/bge-m3",
        "rerank_base_url": "https://api.siliconflow.cn/v1",
        "rerank_model": "BAAI/bge-reranker-v2-m3"
    },

    // ====== MCP Server 配置 ======
    "mcp": {
        "ddg-search": {
            "type": "local",
            "command": ["npx", "-y", "@oevortex/ddg_search@latest"],
            "enabled": false
        },
        "context7": {
            "type": "local",
            "command": ["npx", "-y", "@upstash/context7-mcp@latest"],
            "enabled": false
        },
        "memory": {
            "type": "local",
            "command": ["npx", "-y", "@modelcontextprotocol/server-memory"],
            "enabled": false,
            "environment": {
                "MEMORY_FILE_PATH": "data/mcp-memory.json"
            }
        },
        // 自定义 Python MCP Server（系统工具：系统信息查询）
        "system-tools": {
            "type": "local",
            "command": ["D:/ProgramData/miniconda3/envs/py312/python.exe", "D:/codes/ai_proj/learn_agent/mcp_servers/system_tools_server.py"],
            "enabled": false
        },
        // 自定义 Python MCP Server（开发者工具箱：编码转换、HTTP调试、进程管理、SQLite查询、正则测试）
        "dev-toolkit": {
            "type": "local",
            "command": ["D:/ProgramData/miniconda3/envs/py312/python.exe", "D:/codes/ai_proj/learn_agent/mcp_servers/dev_toolkit_server.py"],
            "enabled": false
        },
        // Desktop Commander（编辑文件、执行命令、搜索代码、内存执行 Python/Node.js）
        "desktop-commander": {
            "type": "local",
            "command": ["npx", "-y", "@wonderwhy-er/desktop-commander"],
            "enabled": false,
            "init_timeout": 120
        },
        // Serena（语义级编程 MCP：代码索引、符号导航、跨文件重构、智能编辑）
        // 安装: uv tool install -p 3.12 serena-agent@latest --prerelease=allow
        "serena": {
            "type": "local",
            "command": ["C:/Users/ydf6/.local/bin/serena.exe", "start-mcp-server", "--project", "D:/codes/funboost"],
            "enabled": true
        },
        // RAG 知识库工具（配置在顶层 "rag" 节，ChromaDB 本地存储）
        "rag-tools": {
            "type": "local",
            "command": ["D:/ProgramData/miniconda3/envs/py312/python.exe", "D:/codes/ai_proj/learn_agent/rag/mcp_server.py"],
            "enabled": true,
            "environment": {
                "PYTHONPATH": "D:/codes/ai_proj"
            }
        },
        // Redis 工具（万能命令执行 + 智能读写 + 统计 + 慢查询）
        // 连接配置: 设 REDIS_URL 或单独设 REDIS_HOST/PORT/PASSWORD/DB
        "redis-tools": {
            "type": "local",
            "command": ["D:/ProgramData/miniconda3/envs/py312/python.exe", "D:/codes/ai_proj/learn_agent/mcp_servers/redis_tools_server.py"],
            "enabled": false,
            "environment": {
                // "REDIS_URL": "redis://:password@192.168.1.100:6379/0"
            }
        },
        // Open Web Search（多引擎搜索 + 文章抓取，Docker 部署）
        // 启动: docker run -d --name web-search -p 3000:3000 -e ENABLE_CORS=true -e CORS_ORIGIN=* ghcr.io/aas-ee/open-web-search:latest
        "web-search": {
            "type": "sse",
            "url": "http://localhost:3000/sse",
            "enabled": false
        }
    },

    // ====== UI 配置 ======
    "ui": {
        "theme": "dark",
        "show_tool_panel": true,
        "show_token_usage": true
    }
}

`````

--- **end of file: learn_agent/config.jsonc** (project: learn_agent) --- 

---


--- **start of file: learn_agent/config_loader.py** (project: learn_agent) --- 

`````python
"""
config.jsonc 配置加载器 —— 与 config.jsonc 同目录

支持 {env:VARIABLE_NAME} 语法从环境变量读取值（参考 OpenCode 设计）。
缺失的环境变量会替换为空字符串。

用法:
    from config_loader import CONFIG

    rag = CONFIG["rag"]
    mcp = CONFIG["mcp"]
    agent = CONFIG["agent"]
"""

import os
import re
import json5
from dotenv import load_dotenv

load_dotenv("D:/codes/ydfhome/importtantdir/envs/sec_dotenv.env", override=False)

_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.jsonc")


def _substitute_env(text):
    """将 {env:VAR_NAME} 替换为对应环境变量值，缺失则替换为空字符串。"""
    return re.sub(r"\{env:([^}]+)\}", lambda m: os.environ.get(m.group(1), ""), text)


with open(_CONFIG_PATH, "r", encoding="utf-8") as _f:
    _raw = _f.read()
    _raw = _substitute_env(_raw)
    CONFIG = json5.loads(_raw)
    print(CONFIG)

`````

--- **end of file: learn_agent/config_loader.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/main.py** (project: learn_agent) --- 

`````python
"""
Learn Agent —— 入口

使用方法:
    conda activate py312
    python main.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_loader import CONFIG
from ui.app import AgentApp


def main():
    CONFIG["_project_root"] = os.path.dirname(os.path.abspath(__file__))
    app = AgentApp(CONFIG)
    app.run()


if __name__ == "__main__":
    main()

`````

--- **end of file: learn_agent/main.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/requirements.txt** (project: learn_agent) --- 

`````text
textual>=0.50.0
json5>=0.9.0
openai>=1.0.0
httpx>=0.24.0
pyyaml>=6.0
mcp>=1.0.0

`````

--- **end of file: learn_agent/requirements.txt** (project: learn_agent) --- 

---


--- **start of file: learn_agent/task.md** (project: learn_agent) --- 

`````markdown
# 真实 AI Agent 完整需求清单

## 一、骨架层（Agent 最基本的能力）

1. **连续会话保持** —— 同一轮对话内保持上下文记忆
2. **工具函数自定义** —— 用户可以定义自己的工具函数，AI 自动发现并使用
3. **支持 MCP 协议** —— 工具可以通过 MCP Server 独立部署，实现跨 AI 复用
4. **AI 自主多次工具调用** —— 用户只提问一次，AI 自己决定调用哪些工具、调用几次、或者不调用

## 二、核心层（没有就不算完整 Agent）

5. **流式输出 (Streaming)** —— 像打字一样逐字输出，而不是等全部生成完再显示
6. **上下文窗口管理** —— 对话太长时自动截断/摘要，防止超出模型 token 上限导致报错
7. **错误处理 + 重试 + 降级** —— 工具失败自动重试（指数退避），API 挂了切备用模型，给用户友好提示
8. **人工确认 (Human-in-the-Loop)** —— 敏感操作（删文件、发邮件、执行 SQL DELETE）先问用户确认再执行

## 三、生产层（生产级 Agent 必备）

9. **跨会话长期记忆** —— 不只是本次对话的记忆，还要记住跨会话的用户偏好、历史问题、之前犯的错
10. **任务规划 (Planning)** —— 复杂任务自动拆解成多个子步骤，按顺序/并行执行（Plan-and-Execute 模式）
11. **自我反思 / 纠错** —— AI 拿到工具结果后判断是否正确、是否需要补充，而不是盲目返回
12. **并行工具调用** —— LLM 一次返回多个 tool_calls 时并行执行，减少等待时间
13. **多模型路由** —— 简单问题用便宜快速模型，复杂推理用强力模型，自动选择控制成本

## 四、高级层（进阶特性）

14. **多 Agent 协作 / 转交 (Handoff)** —— 多个专业 Agent 分工，超出能力范围自动转交
15. **结构化输出** —— 不只返回文本，还能返回 JSON、表格、代码块等结构化数据
16. **可观测性 (Observability)** —— 记录每次 LLM 调用、工具调用、耗时、token 用量，方便 debug
17. **工具调用超时管理** —— 工具执行超过 N 秒自动终止，防止卡死
18. **并发用户支持** —— 多用户同时使用，每人独立会话，异步架构
19. **安全防御** —— 防止 Prompt 注入攻击，工具权限管理，输入校验

## 五、界面与配置

20. **TUI 终端界面** —— 用 Textual 框架，包含对话区域、工具调用实时显示、流式渲染、快捷键操作
21. **JSONC 配置文件** —— 类似 OpenCode 的 config.jsonc，统一管理模型/API/MCP/工具/UI 配置
22. **UI 和逻辑解耦** —— TUI 只是一个"前端"，Agent 核心可以对接任何 UI（Web/CLI/API）

---

## 技术选型

| 组件 | 选择 | 备选 |
|---|---|---|
| LLM | DeepSeek V4 Flash（已有 API） | Qwen / Kimi / GLM |
| Embedding | 阿里通义 text-embedding-v3 | 本地 BGE-M3 |
| 向量数据库 | ChromaDB（pip 安装） | Milvus（生产级） |
| Agent 框架 | 手写 + OpenAI Agents SDK | LangChain |
| TUI 框架 | Textual | — |
| 配置格式 | JSONC（json5 包解析） | — |
| MCP | 知识库检索做成 MCP Server | — |
| 文档处理 | PyMuPDF + 递归分块 | unstructured |
| 会话存储 | SQLite | — |

## 项目结构（预设计）

```
learn_agent/
├── config.jsonc                # 配置文件（模型/API/MCP/UI）
├── main.py                     # 入口：启动 TUI
├── agent/
│   ├── core.py                 # Agent 核心决策循环
│   ├── memory.py               # 短期 + 长期记忆管理
│   ├── context.py              # 上下文窗口管理
│   └── router.py               # 多模型路由
├── tools/
│   ├── builtin.py              # 内置工具（搜索、执行代码等）
│   └── mcp_manager.py          # MCP Server 连接管理
├── rag/
│   ├── rag_server.py           # RAG MCP Server（知识库检索）
│   ├── indexer.py              # 文档解析 + 向量化 + 入库
│   └── retriever.py            # 检索 + 重排序
├── ui/
│   ├── app.py                  # Textual TUI 主界面
│   ├── chat_panel.py           # 对话面板
│   ├── tool_panel.py           # 工具状态面板
│   └── styles.tcss             # 样式文件
└── requirements.txt
```

`````

--- **end of file: learn_agent/task.md** (project: learn_agent) --- 

---


--- **start of file: learn_agent/__init__.py** (project: learn_agent) --- 

`````python


`````

--- **end of file: learn_agent/__init__.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/agent/approval_rules.py** (project: learn_agent) --- 

`````python
"""
工具审批规则引擎

职责：判断工具调用是否需要用户确认。
设计：可插拔规则列表，每条规则是一个 (tool_name, tool_kwargs) -> bool 的函数。

使用方式:
    engine = ApprovalEngine()
    if engine.needs_approval("mcp__redis-tools__redis_execute", {"command": "DEL foo"}):
        # 弹窗问用户
        ...

扩展规则:
    1. 在本文件末尾的 DEFAULT_RULES 列表中添加新规则函数
    2. 或调用 engine.add_rule(my_rule_func) 动态添加
"""

from typing import Callable, List, Optional


# ── Redis 写命令集（只对 redis_execute 生效）────────────
REDIS_WRITE_COMMANDS = {
    "SET", "SETNX", "SETEX", "PSETEX", "MSET", "MSETNX", "APPEND",
    "INCR", "INCRBY", "INCRBYFLOAT", "DECR", "DECRBY",
    "DEL", "UNLINK", "RENAME", "RENAMENX", "EXPIRE", "EXPIREAT",
    "PEXPIRE", "PEXPIREAT", "PERSIST", "MOVE", "COPY",
    "HSET", "HSETNX", "HMSET", "HDEL", "HINCRBY", "HINCRBYFLOAT",
    "LPUSH", "RPUSH", "LPOP", "RPOP", "LSET", "LINSERT", "LREM", "LTRIM",
    "SADD", "SREM", "SPOP", "SMOVE", "SDIFFSTORE", "SINTERSTORE", "SUNIONSTORE",
    "ZADD", "ZREM", "ZINCRBY", "ZPOPMIN", "ZPOPMAX",
    "XADD", "XDEL", "XTRIM",
    "PFADD", "PFMERGE",
    "GEOADD",
}

# ── 始终需要审批的工具名单 ─────────────────────────────
# 工具名格式: mcp__{config.jsonc 中的 MCP 服务键名}__{MCP Server 中 @mcp.tool() 的函数名}
# 示例: config.jsonc 里 "dev-toolkit": {...} + dev_toolkit_server.py 里 def kill_process(...)
#       → 拼接为 "mcp__dev-toolkit__kill_process"
ALWAYS_APPROVE_TOOLS = {
    "mcp__dev-toolkit__kill_process",       # dev-toolkit 服务的 kill_process 工具
    "mcp__redis-tools__redis_smart_set",    # redis-tools 服务的 redis_smart_set 工具
}


# ── 规则函数 ──────────────────────────────────────────

def rule_redis_write(tool_name: str, tool_kwargs: dict) -> bool:
    """redis_execute 中的写命令需要审批，只读命令放行"""
    if tool_name != "mcp__redis-tools__redis_execute":
        return False
    cmd_parts = tool_kwargs.get("command", "").strip().split()
    if not cmd_parts:
        return False
    return cmd_parts[0].upper() in REDIS_WRITE_COMMANDS


def rule_dangerous_tools(tool_name: str, tool_kwargs: dict) -> bool:
    """ALWAYS_APPROVE_TOOLS 名单中的工具始终需要审批"""
    return tool_name in ALWAYS_APPROVE_TOOLS


# ── 默认规则列表（按顺序检查，任一命中即触发审批）──────
DEFAULT_RULES: List[Callable[[str, dict], bool]] = [
    rule_redis_write,
    rule_dangerous_tools,
]


# ── 规则引擎 ──────────────────────────────────────────

class ApprovalEngine:
    """
    工具审批规则引擎。

    初始化时加载 DEFAULT_RULES，也可动态添加/移除规则。
    core.py 和 app.py 只需调用 engine.needs_approval(tool_name, tool_kwargs)，
    不需要知道具体规则逻辑。
    """

    def __init__(self, rules: Optional[List[Callable]] = None):
        self.rules: List[Callable] = list(rules or DEFAULT_RULES)

    def needs_approval(self, tool_name: str, tool_kwargs: dict) -> bool:
        """检查是否有任一规则命中"""
        return any(rule(tool_name, tool_kwargs) for rule in self.rules)

    def add_rule(self, rule: Callable):
        """动态添加规则"""
        self.rules.append(rule)

    def remove_rule(self, rule: Callable):
        """动态移除规则"""
        self.rules = [r for r in self.rules if r is not rule]

`````

--- **end of file: learn_agent/agent/approval_rules.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/agent/core.py** (project: learn_agent) --- 

`````python
"""
Agent 核心 —— 真实 LLM + Function Calling + 工具调用

核心循环：
  用户输入 → LLM(messages + tools) → 判断:
    有 tool_calls → 执行工具 → 结果回传 LLM → 再次判断（可能多轮）
    无 tool_calls → 返回文本回复
"""

import asyncio
import functools
import json
import uuid
from dataclasses import dataclass, field
from typing import AsyncIterator, List, Dict, Optional, Callable

from openai import AsyncOpenAI, APITimeoutError, RateLimitError, APIConnectionError
from agent.session import SessionStore
from agent.mcp_client import MCPManager
from agent.approval_rules import ApprovalEngine
from tools import TOOL_REGISTRY


# ==================== 数据结构 ====================

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



# 内置工具已迁移到 tools/ 模块（基于 Pydantic + @tool 装饰器自动注册）
# 参见: tools/builtin.py, tools/serena_tools.py


# ==================== 配置加载 ====================

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
            ))
    return models


# ==================== Agent 核心 ====================

class AgentCore:
    """
    Agent 核心：
    - Function Calling：LLM 自主决定是否调用工具
    - 多轮工具调用：一次对话中可调用多个工具、多轮
    - 通过回调实时通知 TUI 工具调用状态
    """

    MAX_TOOL_ROUNDS = 30
    MAX_RETRIES = 3
    RETRY_DELAYS = [1, 3, 5]
    RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, APIConnectionError, ConnectionError, TimeoutError)

    def __init__(self, config: dict):
        self.config = config
        self.system_prompt = config.get("agent", {}).get("system_prompt", "你是一个智能助手。")
        self.messages = [{"role": "system", "content": self.system_prompt}]
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0

        self.tool_registry: Dict[str, dict] = dict(TOOL_REGISTRY)

        self.available_models: List[ModelInfo] = load_models_from_config(config)
        self.current_model: Optional[ModelInfo] = None
        self._llm_clients: Dict[str, AsyncOpenAI] = {}
        self._select_default_model()

        self.on_tool_call: Optional[Callable] = None
        self.approval_callback: Optional[Callable] = None
        self.approval_engine = ApprovalEngine()

        self.mcp_manager = MCPManager()

        import os
        db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
        self.session_store = SessionStore(db_dir)
        self.session_id = str(uuid.uuid4())[:8]
        model_id = self.current_model.id if self.current_model else ""
        self.session_store.create_session(self.session_id, title="新会话", model_id=model_id)

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
        """生成 OpenAI function calling 格式的工具列表（内置 + MCP）"""
        tools = [t["schema"] for t in self.tool_registry.values()]
        tools.extend(self.mcp_manager.get_all_tools_openai_format())
        return tools

    async def _execute_with_approval(self, name: str, args: dict) -> str:
        """检查审批引擎，命中规则则弹窗等待用户确认；无审批回调时默认拒绝"""
        if self.approval_engine.needs_approval(name, args):
            if not self.approval_callback:
                return "[已拦截] 此操作需要审批但无审批通道（非 TUI 环境），已自动拒绝"
            approved = await self.approval_callback(name, args)
            if not approved:
                return "[用户已拒绝执行此操作]"
        return await self._execute_tool(name, args)

    async def _execute_tool(self, name: str, args: dict) -> str:
        """执行工具函数（内置或 MCP）
        若工具有 model_cls（Pydantic），先将 args dict 转为 model 实例再传入
        """
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

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """粗略估算 token 数（中文约 1.5 字/token，英文约 4 字符/token）"""
        if not text:
            return 0
        cn_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        en_chars = len(text) - cn_chars
        return int(cn_chars / 1.5 + en_chars / 4)

    def _trim_context(self):
        """
        上下文窗口管理：当消息总 token 超出模型限制时，
        从最早的非 system 消息开始移除，保留 system prompt。
        """
        if not self.current_model or not self.current_model.context_limit:
            return

        max_tokens = int(self.current_model.context_limit * 0.85)

        total = sum(
            self._estimate_tokens(m.get("content", "") or "")
            for m in self.messages
        )

        while total > max_tokens and len(self.messages) > 2:
            removed = self.messages.pop(1)
            total -= self._estimate_tokens(removed.get("content", "") or "")

    async def _call_llm_with_retry(self, client, **kwargs):
        """带重试的 LLM 调用（超时/限流/网络错误自动重试）"""
        last_error: Exception = RuntimeError("LLM 调用失败（未知错误）")
        for attempt in range(self.MAX_RETRIES):
            try:
                return await client.chat.completions.create(**kwargs)
            except self.RETRYABLE_ERRORS as e:
                last_error = e
                if attempt < self.MAX_RETRIES - 1:
                    delay = self.RETRY_DELAYS[min(attempt, len(self.RETRY_DELAYS) - 1)]
                    await asyncio.sleep(delay)
        raise last_error

    def _clean_messages_for_api(self) -> list:
        """发送给 LLM API 前，过滤掉 _ 开头的内部字段（如 _model）"""
        return [
            {k: v for k, v in m.items() if not k.startswith('_')}
            for m in self.messages
        ]

    def _build_assistant_msg(self, resp_msg) -> dict:
        """构建 assistant 消息（处理 tool_calls 和 reasoning_content）"""
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

    async def chat(self, user_input: str) -> AgentResponse:
        """
        Agent 主循环：
        1. 发送 messages + tools 给 LLM
        2. 如果 LLM 返回 tool_calls → 执行 → 结果回传 → 重新调 LLM
        3. 如果 LLM 返回文本 → 结束，返回给用户
        """
        self.messages.append({"role": "user", "content": user_input})
        self._trim_context()
        self.session_store.save_message(self.session_id, "user", user_input)
        self._auto_update_title(user_input)

        if not self.current_model:
            return AgentResponse(text="[错误] 没有配置任何模型")

        client = self._get_client(self.current_model)
        openai_tools = self._get_openai_tools()
        all_tool_calls = []
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0

        for round_idx in range(self.MAX_TOOL_ROUNDS):
            try:
                kwargs = {
                    "model": self.current_model.id,
                    "messages": self._clean_messages_for_api(),
                }
                if openai_tools:
                    kwargs["tools"] = openai_tools

                resp = await self._call_llm_with_retry(client, **kwargs)
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
                        text=reply,
                        reasoning=reasoning,
                        tool_calls=all_tool_calls,
                        token_usage=self.get_token_usage(),
                    )

                self.messages.append(self._build_assistant_msg(resp_msg))

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

                    result = await self._execute_with_approval(func_name, func_args)
                    record.result = result
                    record.status = "error" if result.startswith(("[已拦截]", "[用户已拒绝", "错误:", "工具执行失败")) else "done"

                    if self.on_tool_call:
                        self.on_tool_call(record)

                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": result,
                    })

            except self.RETRYABLE_ERRORS as e:
                error_text = f"[网络/超时错误（已重试 {self.MAX_RETRIES} 次）] {type(e).__name__}: {e}"
                self.messages.append({"role": "assistant", "content": error_text})
                return AgentResponse(
                    text=error_text,
                    tool_calls=all_tool_calls,
                    token_usage=self.get_token_usage(),
                )
            except Exception as e:
                error_text = f"[LLM 调用失败] {type(e).__name__}: {e}"
                self.messages.append({"role": "assistant", "content": error_text})
                return AgentResponse(
                    text=error_text,
                    tool_calls=all_tool_calls,
                    token_usage=self.get_token_usage(),
                )

        return AgentResponse(
            text="[警告] 工具调用轮次超限，已强制停止",
            tool_calls=all_tool_calls,
            token_usage=self.get_token_usage(),
        )

    async def chat_stream(self, user_input: str) -> AsyncIterator[str]:
        """
        流式版本。工具调用阶段用非流式（需要完整 tool_calls），
        最终回复用流式输出。
        """
        self.messages.append({"role": "user", "content": user_input})
        self._trim_context()
        self.session_store.save_message(self.session_id, "user", user_input)
        self._auto_update_title(user_input)

        if not self.current_model:
            yield "[错误] 没有配置任何模型"
            return

        client = self._get_client(self.current_model)
        openai_tools = self._get_openai_tools()
        _stream_full_reply = ""
        self.last_turn_prompt = 0
        self.last_turn_completion = 0
        self.last_turn_tool_calls = 0

        for round_idx in range(self.MAX_TOOL_ROUNDS):
            try:
                kwargs = {
                    "model": self.current_model.id,
                    "messages": self._clean_messages_for_api(),
                    "stream": True,
                    "stream_options": {"include_usage": True},
                }
                if openai_tools:
                    kwargs["tools"] = openai_tools

                stream_resp = await self._call_llm_with_retry(client, **kwargs)

                full_content = ""
                full_reasoning = ""
                tool_calls_map = {}
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
                                tool_calls_map[idx] = {
                                    "id": tc_delta.id or "",
                                    "name": "",
                                    "arguments": "",
                                }
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

                stream_tool_records = []
                for tc in assembled_tool_calls:
                    func_name = tc["function"]["name"]
                    try:
                        func_args = json.loads(tc["function"]["arguments"])
                    except json.JSONDecodeError:
                        func_args = {}

                    self.last_turn_tool_calls += 1
                    yield f"\n🔧 调用工具: {func_name}({json.dumps(func_args, ensure_ascii=False)})\n"

                    result = await self._execute_with_approval(func_name, func_args)
                    stream_tool_records.append({"name": func_name, "args": func_args, "result": result})

                    yield f"📋 结果: {result}\n"

                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tc["id"],
                        "content": result,
                    })

                self.session_store.save_message(
                    self.session_id, "assistant", full_content,
                    reasoning=full_reasoning, tool_calls=stream_tool_records,
                )

            except self.RETRYABLE_ERRORS as e:
                yield f"\n[网络/超时错误（已重试 {self.MAX_RETRIES} 次）] {type(e).__name__}: {e}"
                return
            except Exception as e:
                yield f"\n[LLM 调用失败] {type(e).__name__}: {e}"
                return

        yield "\n[警告] 工具调用轮次超限"

    def register_tool(self, name: str, func: Callable, description: str, parameters: dict):
        """注册自定义工具"""
        self.tool_registry[name] = {
            "function": func,
            "schema": {
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": parameters,
                },
            },
        }

    # ==================== MCP ====================

    async def connect_mcp(self):
        """连接配置中的所有 MCP Server"""
        mcp_config = self.config.get("mcp", {})
        project_root = self.config.get("_project_root", "")
        if mcp_config:
            await self.mcp_manager.connect_all(mcp_config, project_root=project_root)

    async def disconnect_mcp(self):
        """断开所有 MCP Server"""
        await self.mcp_manager.disconnect_all()

    # ==================== 查询接口 ====================

    def switch_model(self, model_id: str) -> bool:
        for m in self.available_models:
            if m.id == model_id:
                self.current_model = m
                return True
        return False

    def get_models_grouped(self) -> Dict[str, List[ModelInfo]]:
        groups = {}
        for m in self.available_models:
            groups.setdefault(m.provider_name, []).append(m)
        return groups

    def _auto_update_title(self, user_input: str):
        """首条用户消息时，先用消息前30字作为临时标题"""
        current_title = self.session_store.get_session_title(self.session_id)
        if current_title == "新会话":
            title = user_input[:30].replace("\n", " ").strip()
            if title:
                self.session_store.update_session_title(self.session_id, title)

    async def generate_smart_title(self):
        """用 LLM 生成一个简短的会话标题（首轮对话后调用）"""
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
                model=self.current_model.id,
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
        self.session_store.create_session(self.session_id, title="新会话", model_id=model_id)

    def get_session_list(self, limit: int = 50) -> list:
        return self.session_store.list_sessions(limit)

    def get_tools(self) -> list:
        builtin = [
            {"name": name, "description": t["schema"]["function"]["description"], "source": "内置"}
            for name, t in self.tool_registry.items()
        ]
        mcp_tools = [
            {"name": f"{t['server']}/{t['name']}", "description": t["description"], "source": f"MCP:{t['server']}"}
            for t in self.mcp_manager.get_tool_info_list()
        ]
        return builtin + mcp_tools

    def get_mcp_status(self) -> list:
        return self.mcp_manager.get_server_status()

    def toggle_mcp_server(self, name: str) -> bool:
        """切换 MCP Server 启用/禁用，返回新的启用状态"""
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
            "total_prompt": self.total_prompt_tokens,
            "total_completion": self.total_completion_tokens,
            "total": self.total_prompt_tokens + self.total_completion_tokens,
        }

`````

--- **end of file: learn_agent/agent/core.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/agent/mcp_client.py** (project: learn_agent) --- 

`````python
"""
MCP 客户端管理器 —— 连接多个 MCP Server，统一管理工具

支持三种传输方式:
  - local (stdio): 启动子进程，通过 stdin/stdout 通信
  - sse: 通过 SSE (Server-Sent Events) 连接远程 MCP Server
  - streamableHttp: 通过 Streamable HTTP 连接远程 MCP Server

使用方式:
    manager = MCPManager()
    await manager.connect_all(config["mcp"])
    tools = manager.get_all_tools_openai_format()
    result = await manager.call_tool("mcp__server__tool", {"arg": "val"})
    await manager.disconnect_all()
"""

import asyncio
import contextlib
import json
import logging
import os
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)

try:
    from mcp import ClientSession
    from mcp.client.stdio import stdio_client, StdioServerParameters
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False
    logger.warning("MCP SDK 未安装，请运行: pip install mcp")

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


class MCPManager:
    """管理多个 MCP Server 的连接和工具调用"""

    def __init__(self):
        self.servers: Dict[str, MCPServerInfo] = {}
        self._stdio_exit_stack = contextlib.AsyncExitStack()
        self._project_root = ""
        self._all_configs: Dict[str, dict] = {}
        self._disabled_servers: set = set()

    async def connect_all(self, mcp_config: dict, project_root: str = ""):
        """根据配置连接所有 MCP Server

        SSE/HTTP 连接必须在调用者任务中初始化（anyio cancel scope 要求），
        因此只有 stdio 类型才能用 asyncio.gather 并发启动。
        """
        self._project_root = project_root
        self._all_configs = dict(mcp_config)

        if not MCP_AVAILABLE:
            logger.error("MCP SDK 未安装，跳过所有 MCP 连接")
            return

        stdio_tasks = []
        remote_servers = []

        for name, cfg in mcp_config.items():
            if not cfg.get("enabled", True):
                continue
            server_type = cfg.get("type", "local")
            if server_type in ("sse", "streamableHttp", "streamable_http"):
                remote_servers.append((name, cfg))
            else:
                stdio_tasks.append(self.connect_server(name, cfg))

        if stdio_tasks:
            await asyncio.gather(*stdio_tasks, return_exceptions=True)

        for name, cfg in remote_servers:
            await self.connect_server(name, cfg)

    async def connect_server(self, name: str, cfg: dict):
        """连接单个 MCP Server（支持 local/sse/streamableHttp 三种传输）"""
        if not MCP_AVAILABLE:
            return

        info = MCPServerInfo(name)
        self.servers[name] = info
        server_type = cfg.get("type", "local")

        try:
            if server_type in ("sse",):
                await self._connect_sse(name, cfg, info)
            elif server_type in ("streamableHttp", "streamable_http"):
                await self._connect_streamable_http(name, cfg, info)
            else:
                await self._connect_stdio(name, cfg, info)

            logger.info(f"MCP [{name}] 已连接 ({server_type})，{len(info.tools)} 个工具")

        except asyncio.TimeoutError:
            info.error = "连接超时"
            logger.error(f"MCP [{name}] 连接超时")
            await self._cleanup_remote(info)
        except FileNotFoundError as e:
            info.error = f"命令未找到: {e}"
            logger.error(f"MCP [{name}] {info.error}")
        except BaseException as e:
            if isinstance(e, BaseExceptionGroup):
                msgs = [f"{type(se).__name__}: {se}" for se in e.exceptions]
                info.error = "; ".join(msgs)
            else:
                info.error = f"{type(e).__name__}: {e}"
            logger.error(f"MCP [{name}] 连接失败: {info.error}")
            await self._cleanup_remote(info)

    @staticmethod
    async def _cleanup_remote(info: MCPServerInfo):
        """清理失败的远程连接的 exit_stack"""
        if info._exit_stack is not None:
            try:
                await info._exit_stack.aclose()
            except (Exception, BaseException):
                pass
            info._exit_stack = None

    async def _connect_stdio(self, name: str, cfg: dict, info: MCPServerInfo):
        """通过 stdio（本地子进程）连接"""
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

        transport = stdio_client(server_params)
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
        """通过 SSE 连接远程 MCP Server（使用独立生命周期，避免 anyio cancel scope 冲突）"""
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
        """通过 Streamable HTTP 连接远程 MCP Server（使用独立生命周期）"""
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
        """断开所有 MCP Server"""
        # 关闭 stdio 连接（共享 exit stack）
        try:
            await self._stdio_exit_stack.aclose()
        except (Exception, BaseException):
            pass
        self._stdio_exit_stack = contextlib.AsyncExitStack()

        # 关闭每个远程连接（独立 exit stack）
        for info in self.servers.values():
            if info._exit_stack is not None:
                try:
                    await info._exit_stack.aclose()
                except (Exception, BaseException):
                    pass
                info._exit_stack = None

        self.servers.clear()

    def toggle_server(self, name: str) -> bool:
        """切换 Server 启用/禁用状态，返回新的启用状态（True=启用）"""
        if name in self._disabled_servers:
            self._disabled_servers.discard(name)
            return True
        else:
            self._disabled_servers.add(name)
            return False

    def is_server_disabled(self, name: str) -> bool:
        return name in self._disabled_servers

    def get_all_tools_openai_format(self) -> List[dict]:
        """将所有 MCP 工具转换为 OpenAI function calling 格式（跳过禁用的 Server）"""
        tools = []
        for server_name, info in self.servers.items():
            if not info.connected or server_name in self._disabled_servers:
                continue
            for tool in info.tools:
                input_schema = {}
                if hasattr(tool, 'inputSchema') and tool.inputSchema:
                    input_schema = tool.inputSchema
                elif hasattr(tool, 'input_schema') and tool.input_schema:
                    input_schema = tool.input_schema

                tools.append({
                    "type": "function",
                    "function": {
                        "name": f"mcp__{server_name}__{tool.name}",
                        "description": f"[MCP:{server_name}] {tool.description or tool.name}",
                        "parameters": input_schema,
                    },
                })
        return tools

    def get_tool_info_list(self) -> List[dict]:
        """获取所有工具的简要信息（用于 TUI 显示，跳过禁用的 Server）"""
        result = []
        for server_name, info in self.servers.items():
            if not info.connected or server_name in self._disabled_servers:
                continue
            for tool in info.tools:
                result.append({
                    "name": tool.name,
                    "server": server_name,
                    "description": tool.description or "",
                })
        return result

    def get_server_status(self) -> List[dict]:
        """获取所有 Server 的状态（包括已连接、已禁用、连接失败、配置禁用）"""
        result = []
        seen = set()
        for name, info in self.servers.items():
            seen.add(name)
            result.append({
                "name": name,
                "connected": info.connected,
                "tools_count": len(info.tools),
                "error": info.error,
                "disabled": name in self._disabled_servers,
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
        """
        调用 MCP 工具。
        full_tool_name 格式: mcp__{server_name}__{tool_name}
        """
        parts = full_tool_name.split("__", 2)
        if len(parts) != 3 or parts[0] != "mcp":
            return f"[错误] 无效的 MCP 工具名: {full_tool_name}"

        server_name = parts[1]
        tool_name = parts[2]

        if server_name in self._disabled_servers:
            return f"[已拦截] MCP Server '{server_name}' 已被禁用"

        info = self.servers.get(server_name)
        if not info or not info.connected or not info.session:
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
            return f"[错误] MCP 工具调用失败: {type(e).__name__}: {e}"

    def is_mcp_tool(self, tool_name: str) -> bool:
        """判断是否为 MCP 工具（名称以 mcp__ 开头）"""
        return tool_name.startswith("mcp__")

`````

--- **end of file: learn_agent/agent/mcp_client.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/agent/session.py** (project: learn_agent) --- 

`````python
"""
会话持久化模块 —— 使用 SQLite 保存/恢复对话历史

表结构:
  sessions(id, title, model_id, created_at, updated_at)
  messages(id, session_id, role, content, reasoning, tool_calls_json, created_at)
"""

import json
import os
import sqlite3
import datetime
from typing import List, Dict, Optional


DB_NAME = "sessions.db"


class SessionStore:

    def __init__(self, db_dir: str):
        os.makedirs(db_dir, exist_ok=True)
        self.db_path = os.path.join(db_dir, DB_NAME)
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_db(self):
        conn = self._get_conn()
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS sessions (
                id          TEXT PRIMARY KEY,
                title       TEXT NOT NULL DEFAULT '',
                model_id    TEXT NOT NULL DEFAULT '',
                created_at  TEXT NOT NULL,
                updated_at  TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS messages (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id      TEXT NOT NULL,
                role            TEXT NOT NULL,
                content         TEXT NOT NULL DEFAULT '',
                reasoning       TEXT NOT NULL DEFAULT '',
                tool_calls_json TEXT NOT NULL DEFAULT '[]',
                created_at      TEXT NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
            );
            CREATE INDEX IF NOT EXISTS idx_msg_session ON messages(session_id);
        """)
        conn.commit()
        conn.close()

    def create_session(self, session_id: str, title: str = "", model_id: str = "") -> str:
        now = datetime.datetime.now().isoformat()
        conn = self._get_conn()
        conn.execute(
            "INSERT INTO sessions (id, title, model_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (session_id, title, model_id, now, now),
        )
        conn.commit()
        conn.close()
        return session_id

    def get_session_title(self, session_id: str) -> str:
        conn = self._get_conn()
        row = conn.execute("SELECT title FROM sessions WHERE id = ?", (session_id,)).fetchone()
        conn.close()
        return row["title"] if row else ""

    def update_session_title(self, session_id: str, title: str):
        now = datetime.datetime.now().isoformat()
        conn = self._get_conn()
        conn.execute(
            "UPDATE sessions SET title = ?, updated_at = ? WHERE id = ?",
            (title, now, session_id),
        )
        conn.commit()
        conn.close()

    def list_sessions(self, limit: int = 50) -> List[dict]:
        conn = self._get_conn()
        rows = conn.execute(
            "SELECT * FROM sessions ORDER BY updated_at DESC LIMIT ?",
            (limit,),
        ).fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def save_message(self, session_id: str, role: str, content: str,
                     reasoning: str = "", tool_calls: Optional[list] = None):
        now = datetime.datetime.now().isoformat()
        tc_json = json.dumps(tool_calls or [], ensure_ascii=False)
        conn = self._get_conn()
        conn.execute(
            "INSERT INTO messages (session_id, role, content, reasoning, tool_calls_json, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (session_id, role, content, reasoning, tc_json, now),
        )
        conn.execute(
            "UPDATE sessions SET updated_at = ? WHERE id = ?",
            (now, session_id),
        )
        conn.commit()
        conn.close()

    def get_messages(self, session_id: str) -> List[Dict]:
        conn = self._get_conn()
        rows = conn.execute(
            "SELECT role, content, reasoning, tool_calls_json FROM messages "
            "WHERE session_id = ? ORDER BY id ASC",
            (session_id,),
        ).fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def delete_session(self, session_id: str):
        conn = self._get_conn()
        conn.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
        conn.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
        conn.commit()
        conn.close()

`````

--- **end of file: learn_agent/agent/session.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/agent/__init__.py** (project: learn_agent) --- 

`````python

`````

--- **end of file: learn_agent/agent/__init__.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/mcp_servers/dev_toolkit_server.py** (project: learn_agent) --- 

`````python
"""
自定义 Python MCP Server —— 开发者工具箱 (dev-toolkit)

提供 9 个实用开发工具，覆盖编码转换、网络调试、进程管理、数据处理四大类。
所有工具与 Serena（代码智能）、web-search（搜索引擎）无功能重叠。

工具列表:
  编码/转换:
    1. hash_text        → 计算文本的 MD5/SHA1/SHA256/SHA512
    2. encode_decode    → Base64/URL/HTML 编解码
    3. generate_id      → 生成 UUID / 随机密码 / 短ID
    4. json_format      → JSON 格式化 / 压缩 / JSON↔YAML 转换

  网络/API:
    5. http_request     → 发送 HTTP 请求 (GET/POST/PUT/DELETE)
    6. check_port       → 检测端口是否被占用及占用进程

  进程/环境:
    7. list_processes   → 列出进程 (可按名称过滤，显示 CPU/内存)
    8. kill_process     → 终止指定 PID 的进程

  数据处理:
    9. query_sqlite     → 对任意 SQLite 数据库执行 SQL 查询

  已移除:
    regex_test → 与 Serena 的 find_in_file 存在功能重叠风险，避免 AI 决策混乱

运行方式:
  由 MCP Client 作为子进程自动启动（stdio 传输）。
  手动测试: python dev_toolkit_server.py
"""

import hashlib
import base64
import uuid
import json
import os
import sqlite3
import string
import secrets
import socket
import subprocess
import sys
import urllib.parse
import html as html_module

from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dev-toolkit")


# ─────────────────────────────────────────────
# 第一类：编码/转换工具
# ─────────────────────────────────────────────

@mcp.tool()
def hash_text(
    text: str = Field(description="要计算哈希的文本内容"),
    algorithm: str = Field(default="sha256", description="哈希算法: md5 / sha1 / sha256 / sha512"),
) -> str:
    """计算文本的哈希值。"""
    algo = algorithm.lower().strip()
    supported = {"md5", "sha1", "sha256", "sha512"}
    if algo not in supported:
        return f"错误: 不支持的算法 '{algo}'，可选: {', '.join(sorted(supported))}"
    h = hashlib.new(algo, text.encode("utf-8"))
    return (
        f"算法: {algo.upper()}\n"
        f"输入长度: {len(text)} 字符\n"
        f"哈希值: {h.hexdigest()}"
    )


@mcp.tool()
def encode_decode(
    text: str = Field(description="输入文本"),
    method: str = Field(default="base64", description="编码方式: base64 / url / html"),
    action: str = Field(default="encode", description="操作类型: encode(编码) / decode(解码)"),
) -> str:
    """对文本进行编码或解码。"""
    method = method.lower().strip()
    action = action.lower().strip()
    if action not in ("encode", "decode"):
        return "错误: action 只能是 encode 或 decode"

    try:
        if method == "base64":
            if action == "encode":
                result = base64.b64encode(text.encode("utf-8")).decode("ascii")
            else:
                result = base64.b64decode(text).decode("utf-8")
        elif method == "url":
            if action == "encode":
                result = urllib.parse.quote(text, safe="")
            else:
                result = urllib.parse.unquote(text)
        elif method == "html":
            if action == "encode":
                result = html_module.escape(text)
            else:
                result = html_module.unescape(text)
        else:
            return f"错误: 不支持的编码方式 '{method}'，可选: base64 / url / html"
    except Exception as e:
        return f"错误: {action} 失败 — {type(e).__name__}: {e}"

    return (
        f"方式: {method} | 操作: {action}\n"
        f"输入: {text[:200]}{'...' if len(text) > 200 else ''}\n"
        f"结果: {result[:2000]}{'...' if len(result) > 2000 else ''}"
    )


@mcp.tool()
def generate_id(
    kind: str = Field(default="uuid4", description="类型: uuid4 / uuid1 / password / hex / short_id"),
    count: int = Field(default=1, description="生成数量，1-20"),
    length: int = Field(default=16, description="随机字符串长度（仅 password/hex/short_id 有效）"),
) -> str:
    """生成各种类型的唯一标识符或随机字符串。"""
    kind = kind.lower().strip()
    count = max(1, min(count, 20))
    length = max(4, min(length, 128))

    results = []
    for _ in range(count):
        if kind == "uuid4":
            results.append(str(uuid.uuid4()))
        elif kind == "uuid1":
            results.append(str(uuid.uuid1()))
        elif kind == "password":
            alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
            results.append("".join(secrets.choice(alphabet) for _ in range(length)))
        elif kind == "hex":
            results.append(secrets.token_hex(length // 2))
        elif kind == "short_id":
            alphabet = string.ascii_lowercase + string.digits
            results.append("".join(secrets.choice(alphabet) for _ in range(length)))
        else:
            return f"错误: 不支持的类型 '{kind}'，可选: uuid4 / uuid1 / password / hex / short_id"

    header = f"类型: {kind} | 数量: {count}"
    if kind in ("password", "hex", "short_id"):
        header += f" | 长度: {length}"
    body = "\n".join(f"  {i + 1}. {r}" for i, r in enumerate(results))
    return f"{header}\n{body}"


@mcp.tool()
def json_format(
    text: str = Field(description="输入的 JSON 或 YAML 文本"),
    action: str = Field(default="pretty", description="操作: pretty(格式化) / compact(压缩) / to_yaml(转YAML) / to_json(转JSON)"),
) -> str:
    """JSON 处理工具：格式化、压缩、或 JSON↔YAML 转换。"""
    action = action.lower().strip()

    if action in ("pretty", "compact"):
        try:
            obj = json.loads(text)
        except json.JSONDecodeError as e:
            return f"错误: JSON 解析失败 — {e}"
        if action == "pretty":
            return json.dumps(obj, indent=2, ensure_ascii=False)
        return json.dumps(obj, separators=(",", ":"), ensure_ascii=False)

    if action == "to_yaml":
        try:
            import yaml
        except ImportError:
            return "错误: 需要安装 PyYAML (pip install pyyaml)"
        try:
            obj = json.loads(text)
        except json.JSONDecodeError as e:
            return f"错误: JSON 解析失败 — {e}"
        return yaml.dump(obj, allow_unicode=True, default_flow_style=False, sort_keys=False)

    if action == "to_json":
        try:
            import yaml
        except ImportError:
            return "错误: 需要安装 PyYAML (pip install pyyaml)"
        try:
            obj = yaml.safe_load(text)
        except Exception as e:
            return f"错误: YAML 解析失败 — {e}"
        return json.dumps(obj, indent=2, ensure_ascii=False)

    return f"错误: 不支持的操作 '{action}'，可选: pretty / compact / to_yaml / to_json"


# ─────────────────────────────────────────────
# 第二类：网络/API 工具
# ─────────────────────────────────────────────

@mcp.tool()
def http_request(
    url: str = Field(description="请求 URL"),
    method: str = Field(default="GET", description="HTTP 方法: GET / POST / PUT / DELETE / PATCH"),
    headers: str = Field(default="{}", description='请求头(JSON 字符串)，如 \'{"Authorization":"Bearer xxx"}\''),
    body: str = Field(default="", description="请求体（POST/PUT 时使用）"),
    timeout: int = Field(default=15, description="超时秒数"),
) -> str:
    """发送 HTTP 请求并返回响应，适合调试 API 接口。仅允许 http/https 协议。"""
    try:
        import urllib.request
        import urllib.error
        from urllib.parse import urlparse

        method = method.upper().strip()
        if method not in ("GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"):
            return f"错误: 不支持的方法 '{method}'"

        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return f"安全限制: 仅允许 http/https 协议，不支持 '{parsed.scheme}'"

        try:
            hdrs = json.loads(headers) if headers.strip() else {}
        except json.JSONDecodeError:
            return "错误: headers 不是合法的 JSON"

        data = body.encode("utf-8") if body else None
        req = urllib.request.Request(url, data=data, headers=hdrs, method=method)

        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
            resp_headers = dict(resp.headers)
            content_type = resp_headers.get("Content-Type", "")
            raw = resp.read()

            try:
                resp_body = raw.decode("utf-8")
            except UnicodeDecodeError:
                resp_body = f"(二进制数据，{len(raw)} 字节)"

            if len(resp_body) > 5000:
                resp_body = resp_body[:5000] + f"\n... (已截断，共 {len(raw)} 字节)"

        lines = [
            f"HTTP {status}",
            f"Content-Type: {content_type}",
            f"响应大小: {len(raw)} 字节",
            "── Headers ──",
        ]
        for k, v in list(resp_headers.items())[:15]:
            lines.append(f"  {k}: {v}")
        lines.append("── Body ──")
        lines.append(resp_body)
        return "\n".join(lines)

    except urllib.error.HTTPError as e:
        body_text = ""
        try:
            body_text = e.read().decode("utf-8")[:2000]
        except Exception:
            pass
        return f"HTTP 错误 {e.code}: {e.reason}\n{body_text}"
    except urllib.error.URLError as e:
        return f"连接错误: {e.reason}"
    except Exception as e:
        return f"请求失败: {type(e).__name__}: {e}"


@mcp.tool()
def check_port(
    port: int = Field(description="端口号 (1-65535)"),
    host: str = Field(default="127.0.0.1", description="主机地址"),
) -> str:
    """检测指定端口是否被占用，并显示占用进程信息。"""
    if not 1 <= port <= 65535:
        return f"错误: 端口号必须在 1-65535 之间，收到 {port}"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        result = sock.connect_ex((host, port))
        is_open = result == 0
    finally:
        sock.close()

    if not is_open:
        return f"端口 {host}:{port} — 未占用 (空闲)"

    process_info = _get_port_process(port)
    return (
        f"端口 {host}:{port} — 已占用 ✗\n"
        f"占用进程: {process_info}"
    )


def _get_port_process(port: int) -> str:
    try:
        if sys.platform == "win32":
            out = subprocess.check_output(
                ["netstat", "-ano", "-p", "TCP"],
                text=True, timeout=5, stderr=subprocess.DEVNULL,
            )
            for line in out.splitlines():
                if f":{port}" in line and "LISTENING" in line:
                    parts = line.split()
                    pid = parts[-1]
                    try:
                        name_out = subprocess.check_output(
                            ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"],
                            text=True, timeout=5, stderr=subprocess.DEVNULL,
                        )
                        proc_name = name_out.strip().split(",")[0].strip('"')
                        return f"PID={pid} ({proc_name})"
                    except Exception:
                        return f"PID={pid}"
        else:
            out = subprocess.check_output(
                ["lsof", "-i", f":{port}", "-sTCP:LISTEN", "-P", "-n"],
                text=True, timeout=5, stderr=subprocess.DEVNULL,
            )
            for line in out.splitlines()[1:]:
                parts = line.split()
                if len(parts) >= 2:
                    return f"PID={parts[1]} ({parts[0]})"
    except Exception:
        pass
    return "(无法获取进程信息)"


# ─────────────────────────────────────────────
# 第三类：进程/环境工具
# ─────────────────────────────────────────────

@mcp.tool()
def list_processes(
    name_filter: str = Field(default="", description="进程名过滤（模糊匹配，不区分大小写），留空列出所有"),
    sort_by: str = Field(default="memory", description="排序方式: memory(内存) / cpu"),
    limit: int = Field(default=20, description="显示数量上限"),
) -> str:
    """列出系统进程，可按名称过滤、按资源排序。"""
    try:
        import psutil
    except ImportError:
        return "错误: 需要安装 psutil (pip install psutil)"

    procs = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]):
        try:
            info = p.info
            name = info.get("name", "") or ""
            if name_filter and name_filter.lower() not in name.lower():
                continue
            mem = info.get("memory_info")
            mem_mb = mem.rss / (1024 * 1024) if mem else 0
            procs.append({
                "pid": info["pid"],
                "name": name,
                "cpu": info.get("cpu_percent", 0) or 0,
                "mem_mb": mem_mb,
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if sort_by == "cpu":
        procs.sort(key=lambda x: x["cpu"], reverse=True)
    else:
        procs.sort(key=lambda x: x["mem_mb"], reverse=True)

    procs = procs[:limit]
    if not procs:
        msg = "没有找到匹配的进程"
        if name_filter:
            msg += f"（过滤: '{name_filter}'）"
        return msg

    lines = [f"{'PID':>8}  {'进程名':<30}  {'CPU%':>6}  {'内存(MB)':>10}"]
    lines.append("─" * 60)
    for p in procs:
        lines.append(f"{p['pid']:>8}  {p['name']:<30}  {p['cpu']:>5.1f}%  {p['mem_mb']:>9.1f}")

    header = f"共 {len(procs)} 个进程"
    if name_filter:
        header += f"（过滤: '{name_filter}'）"
    header += f" | 排序: {sort_by}"
    return f"{header}\n" + "\n".join(lines)


@mcp.tool()
def kill_process(
    pid: int = Field(description="进程 PID"),
    force: bool = Field(default=False, description="是否强制终止(SIGKILL)，默认 False 使用 SIGTERM"),
) -> str:
    """终止指定 PID 的进程。建议先用 list_processes 确认目标。"""
    try:
        import psutil
    except ImportError:
        return "错误: 需要安装 psutil (pip install psutil)"

    try:
        p = psutil.Process(pid)
        proc_name = p.name()
    except psutil.NoSuchProcess:
        return f"错误: PID {pid} 不存在"
    except psutil.AccessDenied:
        return f"错误: 没有权限访问 PID {pid}"

    try:
        if force:
            p.kill()
            action = "强制终止 (SIGKILL)"
        else:
            p.terminate()
            action = "优雅终止 (SIGTERM)"
        return f"已对 PID={pid} ({proc_name}) 发送 {action} 信号"
    except psutil.AccessDenied:
        return f"错误: 没有权限终止 PID {pid} ({proc_name})"
    except Exception as e:
        return f"错误: 终止失败 — {type(e).__name__}: {e}"


# ─────────────────────────────────────────────
# 第四类：数据处理工具
# ─────────────────────────────────────────────

@mcp.tool()
def query_sqlite(
    db_path: str = Field(description="数据库文件路径"),
    sql: str = Field(description="SQL 查询语句（仅允许 SELECT / PRAGMA / EXPLAIN）"),
    max_rows: int = Field(default=100, description="最大返回行数"),
) -> str:
    """对 SQLite 数据库执行只读 SQL 查询并返回结果。"""
    db_path = os.path.expanduser(db_path)
    if not os.path.exists(db_path):
        return f"错误: 数据库文件不存在: {db_path}"

    sql_stripped = sql.strip().upper()
    allowed_prefixes = ("SELECT", "PRAGMA", "EXPLAIN")
    if not any(sql_stripped.startswith(p) for p in allowed_prefixes):
        return f"错误: 仅允许 SELECT / PRAGMA / EXPLAIN 查询，禁止修改操作。收到: {sql[:50]}"

    try:
        conn = sqlite3.connect(db_path, timeout=5)
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(sql)
        rows = cursor.fetchmany(max_rows + 1)

        if not rows:
            desc = cursor.description
            if desc:
                cols = [d[0] for d in desc]
                return f"查询成功，0 行结果\n列: {', '.join(cols)}"
            return "查询成功，无返回数据"

        cols = [d[0] for d in cursor.description]
        truncated = len(rows) > max_rows
        rows = rows[:max_rows]

        col_widths = [len(c) for c in cols]
        str_rows = []
        for row in rows:
            str_row = [str(row[i]) if row[i] is not None else "NULL" for i in range(len(cols))]
            for i, v in enumerate(str_row):
                col_widths[i] = min(max(col_widths[i], len(v)), 40)
            str_rows.append(str_row)

        header = "  ".join(c.ljust(col_widths[i]) for i, c in enumerate(cols))
        sep = "  ".join("─" * col_widths[i] for i in range(len(cols)))
        body_lines = []
        for sr in str_rows:
            line = "  ".join(sr[i][:40].ljust(col_widths[i]) for i in range(len(cols)))
            body_lines.append(line)

        result = f"{header}\n{sep}\n" + "\n".join(body_lines)
        if truncated:
            result += f"\n... (已截断，最多显示 {max_rows} 行)"
        result += f"\n\n共 {len(str_rows)} 行"
        conn.close()
        return result

    except sqlite3.Error as e:
        return f"SQL 错误: {e}"
    except Exception as e:
        return f"查询失败: {type(e).__name__}: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")

`````

--- **end of file: learn_agent/mcp_servers/dev_toolkit_server.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/mcp_servers/redis_tools_server.py** (project: learn_agent) --- 

`````python
"""
自定义 Python MCP Server —— Redis 工具 (redis-tools)

设计哲学：
  不逐个封装 200+ Redis 命令，而是提供 7 个高价值工具：
  - 1 个万能命令执行器（AI 自己拼 Redis 命令）
  - 6 个高频/复杂场景的专用工具（AI 容易搞错或需要组合多步的操作）

工具列表:
  1. redis_execute     → 万能 Redis 命令执行器（AI 自己写命令）
  2. redis_info        → 查看服务器状态（内存/连接/版本等）
  3. redis_keys        → 按模式搜索 key（显示类型/TTL/大小）
  4. redis_smart_get   → 智能读取（自动识别 string/hash/list/set/zset 并完整读取）
  5. redis_smart_set   → 智能写入（支持 TTL、自动选择数据类型）
  6. redis_db_stats    → 数据库全局统计（key 总数、内存分布、各类型占比）
  7. redis_slowlog     → 慢查询日志（排查性能问题）

连接配置（通过环境变量，优先级从高到低）:
  REDIS_URL      完整 URL，如 redis://:password@host:6379/0（优先使用）
  REDIS_HOST     主机地址，默认 127.0.0.1
  REDIS_PORT     端口，默认 6379
  REDIS_PASSWORD 密码，默认无
  REDIS_DB       数据库号，默认 0

运行方式:
  由 MCP Client 作为子进程自动启动（stdio 传输）。
  手动测试: python redis_tools_server.py
"""

import os
import json
import shlex

from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("redis-tools")

DANGEROUS_COMMANDS = {
    "FLUSHDB", "FLUSHALL", "SHUTDOWN", "DEBUG", "CONFIG SET",
    "SLAVEOF", "REPLICAOF", "CLUSTER RESET", "SCRIPT FLUSH",
    "KEYS", "EVAL", "EVALSHA", "SCRIPT LOAD", "MODULE LOAD",
    "MODULE UNLOAD", "ACL SETUSER", "ACL DELUSER", "CONFIG RESETSTAT",
    "SWAPDB", "MIGRATE",
}


def _get_redis():
    """创建 Redis 连接（每次调用新建，避免长连接超时问题）"""
    try:
        import redis as redis_lib
    except ImportError:
        raise RuntimeError("需要安装 redis-py: pip install redis")

    redis_url = os.environ.get("REDIS_URL", "").strip()
    if redis_url:
        return redis_lib.Redis.from_url(
            redis_url, decode_responses=True, socket_timeout=10,
        )

    host = os.environ.get("REDIS_HOST", "127.0.0.1")
    port = int(os.environ.get("REDIS_PORT", "6379"))
    password = os.environ.get("REDIS_PASSWORD") or None
    db = int(os.environ.get("REDIS_DB", "0"))

    return redis_lib.Redis(
        host=host, port=port, password=password, db=db,
        decode_responses=True, socket_timeout=10,
    )


def _format_value(value, max_len=2000):
    s = str(value)
    if len(s) > max_len:
        return s[:max_len] + f"... (共 {len(s)} 字符)"
    return s


# ─────────────────────────────────────────────
# 工具 1: 万能命令执行器
# ─────────────────────────────────────────────

@mcp.tool()
def redis_execute(
    command: str = Field(description='完整的 Redis 命令，如 "SET mykey hello EX 60" 或 "HGETALL user:1001"'),
) -> str:
    """执行任意 Redis 命令（FLUSHDB/FLUSHALL/SHUTDOWN 等危险命令被禁止）。"""
    if not command.strip():
        return "错误: 命令不能为空"

    cmd_upper = command.strip().upper()
    for dangerous in DANGEROUS_COMMANDS:
        if cmd_upper.startswith(dangerous):
            return f"安全限制: 禁止执行危险命令 {dangerous}。如确需执行，请通过 redis-cli 手动操作。"

    try:
        r = _get_redis()
        try:
            parts = shlex.split(command.strip())
        except ValueError:
            parts = command.strip().split()
        result = r.execute_command(*parts)

        if result is None:
            return "(nil)"
        if isinstance(result, bool):
            return "OK" if result else "FAIL"
        if isinstance(result, (int, float)):
            return str(result)
        if isinstance(result, bytes):
            try:
                return result.decode("utf-8")
            except UnicodeDecodeError:
                return f"(binary data, {len(result)} bytes)"
        if isinstance(result, list):
            lines = []
            for i, item in enumerate(result[:100]):
                lines.append(f"  {i + 1}) {_format_value(item, 500)}")
            if len(result) > 100:
                lines.append(f"  ... (共 {len(result)} 项)")
            return "\n".join(lines) if lines else "(empty list)"
        if isinstance(result, dict):
            return json.dumps(result, ensure_ascii=False, indent=2, default=str)

        return _format_value(result)

    except Exception as e:
        return f"执行失败: {type(e).__name__}: {e}"


# ─────────────────────────────────────────────
# 工具 2: 服务器信息
# ─────────────────────────────────────────────

@mcp.tool()
def redis_info(
    section: str = Field(
        default="overview",
        description="信息区域: overview(精简概要) / server / clients / memory / stats / replication / keyspace / all",
    ),
) -> str:
    """查看 Redis 服务器信息。"""
    try:
        r = _get_redis()

        if section == "overview":
            info = r.info()
            db_info = r.info("keyspace")
            total_keys = sum(
                v.get("keys", 0) for k, v in db_info.items() if k.startswith("db")
            )
            return (
                f"Redis 服务器概要\n"
                f"{'─' * 40}\n"
                f"  版本: {info.get('redis_version', '?')}\n"
                f"  运行时间: {info.get('uptime_in_days', '?')} 天\n"
                f"  已用内存: {info.get('used_memory_human', '?')}\n"
                f"  峰值内存: {info.get('used_memory_peak_human', '?')}\n"
                f"  连接客户端: {info.get('connected_clients', '?')}\n"
                f"  总 key 数: {total_keys}\n"
                f"  命中率: {_calc_hit_rate(info)}\n"
                f"  TCP 端口: {info.get('tcp_port', '?')}\n"
                f"  操作系统: {info.get('os', '?')}"
            )

        if section in ("server", "clients", "memory", "stats", "replication", "keyspace"):
            info = r.info(section)
        elif section == "all":
            info = r.info("all")
        else:
            return f"错误: 不支持的 section '{section}'，可选: overview/server/clients/memory/stats/replication/keyspace/all"

        lines = []
        for k, v in info.items():
            if isinstance(v, dict):
                lines.append(f"[{k}]")
                for sk, sv in v.items():
                    lines.append(f"  {sk}: {sv}")
            else:
                lines.append(f"  {k}: {v}")
        return "\n".join(lines[:200])

    except Exception as e:
        return f"获取信息失败: {type(e).__name__}: {e}"


def _calc_hit_rate(info: dict) -> str:
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    if total == 0:
        return "N/A (无访问)"
    rate = hits / total * 100
    return f"{rate:.1f}% ({hits}/{total})"


# ─────────────────────────────────────────────
# 工具 3: Key 搜索
# ─────────────────────────────────────────────

@mcp.tool()
def redis_keys(
    pattern: str = Field(default="*", description='key 匹配模式，支持 * ? [] 通配符，如 "user:*"'),
    limit: int = Field(default=50, description="最多返回数量（防止 key 太多卡住）"),
    show_details: bool = Field(default=True, description="是否显示每个 key 的类型/TTL/内存大小"),
) -> str:
    """按模式搜索 Redis key，可显示每个 key 的类型、TTL、大小等详情。"""
    try:
        r = _get_redis()
        keys = []
        cursor = 0
        while len(keys) < limit:
            cursor, batch = r.scan(cursor=cursor, match=pattern, count=200)
            keys.extend(batch)
            if cursor == 0:
                break

        keys = keys[:limit]
        if not keys:
            return f"模式 '{pattern}' 没有匹配到任何 key"

        if not show_details:
            return f"匹配 '{pattern}': {len(keys)} 个 key\n" + "\n".join(f"  {k}" for k in keys)

        pipe = r.pipeline()
        for k in keys:
            pipe.type(k)
            pipe.ttl(k)
            pipe.memory_usage(k)
        results = pipe.execute()

        lines = [f"匹配 '{pattern}': {len(keys)} 个 key\n"]
        lines.append(f"  {'Key':<40} {'类型':<10} {'TTL':<12} {'内存':<10}")
        lines.append("  " + "─" * 72)
        for i, k in enumerate(keys):
            key_type = results[i * 3] or "?"
            ttl = results[i * 3 + 1]
            mem = results[i * 3 + 2]
            ttl_str = "永不过期" if ttl == -1 else f"{ttl}s" if ttl >= 0 else "?"
            mem_str = _format_bytes(mem) if mem else "?"
            lines.append(f"  {k:<40} {key_type:<10} {ttl_str:<12} {mem_str:<10}")

        return "\n".join(lines)

    except Exception as e:
        return f"搜索失败: {type(e).__name__}: {e}"


def _format_bytes(n):
    if n is None:
        return "?"
    if n < 1024:
        return f"{n}B"
    if n < 1024 * 1024:
        return f"{n / 1024:.1f}KB"
    return f"{n / (1024 * 1024):.1f}MB"


# ─────────────────────────────────────────────
# 工具 4: 智能读取
# ─────────────────────────────────────────────

@mcp.tool()
def redis_smart_get(
    key: str = Field(description="Redis key 名称"),
) -> str:
    """智能读取 Redis key 的值，自动识别数据类型（string/hash/list/set/zset/stream）并完整展示。"""
    try:
        r = _get_redis()

        if not r.exists(key):
            return f"key '{key}' 不存在"

        key_type = r.type(key)
        ttl = r.ttl(key)
        ttl_str = "永不过期" if ttl == -1 else f"{ttl}s"

        header = f"Key: {key}\n类型: {key_type}\nTTL: {ttl_str}\n{'─' * 40}\n"

        if key_type == "string":
            val = r.get(key)
            try:
                parsed = json.loads(val)
                val = json.dumps(parsed, ensure_ascii=False, indent=2)
                header += f"值 (JSON):\n{_format_value(val, 3000)}"
            except (json.JSONDecodeError, TypeError):
                header += f"值: {_format_value(val, 3000)}"

        elif key_type == "hash":
            data = r.hgetall(key)
            header += f"字段数: {len(data)}\n"
            for k, v in list(data.items())[:100]:
                header += f"  {k}: {_format_value(v, 200)}\n"
            if len(data) > 100:
                header += f"  ... (共 {len(data)} 个字段)"

        elif key_type == "list":
            length = r.llen(key)
            items = r.lrange(key, 0, min(99, length - 1))
            header += f"长度: {length}\n"
            for i, item in enumerate(items):
                header += f"  [{i}] {_format_value(item, 200)}\n"
            if length > 100:
                header += f"  ... (共 {length} 项)"

        elif key_type == "set":
            size = r.scard(key)
            members = list(r.sscan_iter(key, count=100))[:100]
            header += f"成员数: {size}\n"
            for m in members:
                header += f"  • {_format_value(m, 200)}\n"
            if size > 100:
                header += f"  ... (共 {size} 个成员)"

        elif key_type == "zset":
            size = r.zcard(key)
            items = r.zrange(key, 0, 99, withscores=True)
            header += f"成员数: {size}\n"
            for member, score in items:
                header += f"  {score:>10.2f}  {_format_value(member, 200)}\n"
            if size > 100:
                header += f"  ... (共 {size} 个成员)"

        elif key_type == "stream":
            length = r.xlen(key)
            entries = r.xrange(key, count=20)
            header += f"消息数: {length}\n"
            for entry_id, fields in entries:
                header += f"  [{entry_id}] {json.dumps(fields, ensure_ascii=False)}\n"
            if length > 20:
                header += f"  ... (共 {length} 条消息)"

        else:
            header += f"(不支持直接显示类型 '{key_type}'，请用 redis_execute 操作)"

        return header

    except Exception as e:
        return f"读取失败: {type(e).__name__}: {e}"


# ─────────────────────────────────────────────
# 工具 5: 智能写入
# ─────────────────────────────────────────────

@mcp.tool()
def redis_smart_set(
    key: str = Field(description="Redis key 名称"),
    value: str = Field(description='要写入的值。string→字符串; hash→JSON对象如{"a":"1"}; list/set→JSON数组如["a","b"]'),
    ttl: int = Field(default=-1, description="过期时间(秒)，-1 表示永不过期"),
    data_type: str = Field(default="string", description="数据类型: string / hash / list / set"),
) -> str:
    """智能写入 Redis key，支持多种数据类型和 TTL 设置。"""
    data_type = data_type.lower().strip()
    if data_type not in ("string", "hash", "list", "set"):
        return f"错误: 不支持的数据类型 '{data_type}'，可选: string / hash / list / set"

    try:
        r = _get_redis()

        if data_type == "string":
            if ttl > 0:
                r.setex(key, ttl, value)
            else:
                r.set(key, value)
            return f"已设置 {key} = {_format_value(value, 200)} (string, TTL={ttl}s)"

        if data_type == "hash":
            try:
                obj = json.loads(value)
                if not isinstance(obj, dict):
                    return "错误: hash 类型的 value 必须是 JSON 对象"
            except json.JSONDecodeError as e:
                return f"错误: JSON 解析失败 — {e}"
            r.delete(key)
            str_obj = {str(k): str(v) for k, v in obj.items()}
            r.hset(key, mapping=str_obj)
            if ttl > 0:
                r.expire(key, ttl)
            return f"已设置 {key} (hash, {len(obj)} 个字段, TTL={ttl}s)"

        if data_type == "list":
            try:
                items = json.loads(value)
                if not isinstance(items, list):
                    return "错误: list 类型的 value 必须是 JSON 数组"
            except json.JSONDecodeError as e:
                return f"错误: JSON 解析失败 — {e}"
            r.delete(key)
            if items:
                r.rpush(key, *[str(i) for i in items])
            if ttl > 0:
                r.expire(key, ttl)
            return f"已设置 {key} (list, {len(items)} 项, TTL={ttl}s)"

        if data_type == "set":
            try:
                items = json.loads(value)
                if not isinstance(items, list):
                    return "错误: set 类型的 value 必须是 JSON 数组"
            except json.JSONDecodeError as e:
                return f"错误: JSON 解析失败 — {e}"
            r.delete(key)
            if items:
                r.sadd(key, *[str(i) for i in items])
            if ttl > 0:
                r.expire(key, ttl)
            return f"已设置 {key} (set, {len(items)} 个成员, TTL={ttl}s)"

    except Exception as e:
        return f"写入失败: {type(e).__name__}: {e}"


# ─────────────────────────────────────────────
# 工具 6: 数据库统计
# ─────────────────────────────────────────────

@mcp.tool()
def redis_db_stats() -> str:
    """查看当前 Redis 数据库的全局统计：key 总数、各类型分布、内存占用等。"""
    try:
        r = _get_redis()
        info = r.info()
        db_info = r.info("keyspace")

        db_num = int(os.environ.get("REDIS_DB", "0"))
        db_key = f"db{db_num}"
        db_data = db_info.get(db_key, {})
        total_keys = db_data.get("keys", 0)

        type_counts = {"string": 0, "hash": 0, "list": 0, "set": 0, "zset": 0, "stream": 0, "other": 0}
        if total_keys > 0 and total_keys <= 10000:
            cursor = 0
            scanned = 0
            pipe = r.pipeline()
            keys_batch = []
            while True:
                cursor, batch = r.scan(cursor=cursor, count=500)
                keys_batch.extend(batch)
                scanned += len(batch)
                if cursor == 0 or scanned >= 10000:
                    break
            for k in keys_batch:
                pipe.type(k)
            types = pipe.execute()
            for t in types:
                t = t if isinstance(t, str) else "other"
                if t in type_counts:
                    type_counts[t] += 1
                else:
                    type_counts["other"] += 1

        lines = [
            f"Redis 数据库统计 (db{db_num})",
            "─" * 40,
            f"  Key 总数: {total_keys}",
            f"  已用内存: {info.get('used_memory_human', '?')}",
            f"  峰值内存: {info.get('used_memory_peak_human', '?')}",
            f"  内存碎片率: {info.get('mem_fragmentation_ratio', '?')}",
            "",
        ]

        if total_keys > 0 and total_keys <= 10000:
            lines.append("  类型分布:")
            for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
                if c > 0:
                    pct = c / total_keys * 100
                    bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
                    lines.append(f"    {t:<10} {bar} {c:>5} ({pct:.1f}%)")
        elif total_keys > 10000:
            lines.append(f"  (key 数量超过 10000，跳过类型统计以避免阻塞)")

        lines.extend([
            "",
            f"  每秒操作数: {info.get('instantaneous_ops_per_sec', '?')}",
            f"  已连接客户端: {info.get('connected_clients', '?')}",
            f"  命中率: {_calc_hit_rate(info)}",
        ])

        return "\n".join(lines)

    except Exception as e:
        return f"统计失败: {type(e).__name__}: {e}"


# ─────────────────────────────────────────────
# 工具 7: 慢查询日志
# ─────────────────────────────────────────────

@mcp.tool()
def redis_slowlog(
    count: int = Field(default=10, description="显示最近几条慢查询，1-50"),
) -> str:
    """查看 Redis 慢查询日志，用于排查性能瓶颈。"""
    try:
        r = _get_redis()
        count = max(1, min(count, 50))
        logs = r.slowlog_get(count)

        if not logs:
            threshold = r.config_get("slowlog-log-slower-than")
            threshold_us = threshold.get("slowlog-log-slower-than", "?")
            return f"暂无慢查询记录\n(当前阈值: {threshold_us}μs)"

        lines = [f"最近 {len(logs)} 条慢查询\n"]
        for entry in logs:
            entry_id = entry.get("id", "?")
            start_time = entry.get("start_time", 0)
            duration = entry.get("duration", 0)
            command = entry.get("command", b"?")

            if isinstance(command, bytes):
                command = command.decode("utf-8", errors="replace")
            elif isinstance(command, (list, tuple)):
                command = " ".join(
                    c.decode("utf-8", errors="replace") if isinstance(c, bytes) else str(c)
                    for c in command
                )

            import datetime
            ts = datetime.datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
            lines.append(
                f"  #{entry_id} | {ts} | 耗时 {duration}μs\n"
                f"    命令: {_format_value(command, 300)}"
            )

        return "\n".join(lines)

    except Exception as e:
        return f"获取慢查询失败: {type(e).__name__}: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")

`````

--- **end of file: learn_agent/mcp_servers/redis_tools_server.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/mcp_servers/system_tools_server.py** (project: learn_agent) --- 

`````python
"""
自定义 Python MCP Server —— 系统工具集

本 MCP Server 提供以下工具，展示如何用 Python 编写实用的 MCP 服务：

工具列表（已启用）:
  1. get_system_info  → 获取当前系统信息（OS、Python 版本、CPU、内存）

已禁用（功能被 Serena MCP 覆盖，且 Serena 版本更完善，与其他 Serena 工具搭配更好）:
  2. list_directory   → Serena 有 list_directory_tree / find_files 等，支持递归与过滤
  3. read_text_file   → Serena 有 read_file，且能结合 find_symbol 等代码智能工具一起使用
  4. save_note        → 可由 Serena 的 create_file / write_file 替代，同时保持代码库索引更新

运行方式:
  通常由 MCP Client（如 learn_agent）作为子进程自动启动。
  手动测试:
    python system_tools_server.py
"""

import os
import sys
import platform
import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("system-tools")

NOTES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "notes")


@mcp.tool()
def get_system_info() -> str:
    """获取当前系统的详细信息，包括操作系统、Python 版本、CPU、内存和磁盘。"""
    try:
        import psutil
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        cpu_percent = psutil.cpu_percent(interval=0.5)
        mem_info = (
            f"  内存: {mem.total / (1024**3):.1f} GB 总计, "
            f"{mem.used / (1024**3):.1f} GB 已用 ({mem.percent}%)"
        )
        disk_info = (
            f"  磁盘: {disk.total / (1024**3):.1f} GB 总计, "
            f"{disk.free / (1024**3):.1f} GB 可用 ({disk.percent}% 已用)"
        )
        cpu_info = f"  CPU: {psutil.cpu_count()} 核, 使用率 {cpu_percent}%"
    except ImportError:
        mem_info = "  内存: (需安装 psutil 查看)"
        disk_info = "  磁盘: (需安装 psutil 查看)"
        cpu_info = f"  CPU: {os.cpu_count()} 核"

    return (
        f"系统信息:\n"
        f"  操作系统: {platform.system()} {platform.release()} ({platform.machine()})\n"
        f"  主机名: {platform.node()}\n"
        f"  Python: {sys.version}\n"
        f"{cpu_info}\n"
        f"{mem_info}\n"
        f"{disk_info}\n"
        f"  当前时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )


# @mcp.tool()  # 已禁用：Serena 的 list_directory_tree/find_files 功能更完善，支持递归和过滤，且与其他 Serena 工具配合更好
def list_directory(path: str = ".", show_hidden: bool = False) -> str:
    """
    列出指定目录的内容。

    参数:
        path: 目录路径，默认当前目录
        show_hidden: 是否显示隐藏文件（以 . 开头），默认 False
    """
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return f"错误: 路径不存在: {path}"
    if not os.path.isdir(path):
        return f"错误: 不是目录: {path}"

    entries = []
    try:
        for name in sorted(os.listdir(path)):
            if not show_hidden and name.startswith('.'):
                continue
            full = os.path.join(path, name)
            try:
                stat = os.stat(full)
                size = stat.st_size
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
                if os.path.isdir(full):
                    entries.append(f"  📁 {name}/  (dir, {mtime})")
                else:
                    size_str = _format_size(size)
                    entries.append(f"  📄 {name}  ({size_str}, {mtime})")
            except OSError:
                entries.append(f"  ❓ {name}  (无法读取)")
    except PermissionError:
        return f"错误: 没有权限访问: {path}"

    header = f"目录: {os.path.abspath(path)} ({len(entries)} 项)"
    if not entries:
        return header + "\n  (空目录)"
    return header + "\n" + "\n".join(entries)


# @mcp.tool()  # 已禁用：Serena 的 read_file 功能更完善，能结合 find_symbol / get_symbols_overview 等代码智能工具一起使用
def read_text_file(path: str, max_lines: int = 200) -> str:
    """
    读取文本文件内容。

    参数:
        path: 文件路径
        max_lines: 最大读取行数，默认 200 行，防止读取超大文件
    """
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return f"错误: 文件不存在: {path}"
    if not os.path.isfile(path):
        return f"错误: 不是文件: {path}"

    size = os.path.getsize(path)
    if size > 5 * 1024 * 1024:
        return f"错误: 文件过大 ({_format_size(size)})，最大支持 5MB"

    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            lines = []
            for i, line in enumerate(f):
                if i >= max_lines:
                    lines.append(f"\n... (已截断，共读取 {max_lines} 行，文件大小 {_format_size(size)})")
                    break
                lines.append(line.rstrip('\n'))
        total = len(lines)
        header = f"文件: {os.path.abspath(path)} ({_format_size(size)}, {total} 行)\n{'─' * 40}"
        return header + "\n" + "\n".join(lines)
    except UnicodeDecodeError:
        return f"错误: 无法以文本模式读取（可能是二进制文件）: {path}"
    except PermissionError:
        return f"错误: 没有权限读取: {path}"


# @mcp.tool()  # 已禁用：Serena 的 create_file / write_file 替代，可同时更新代码库索引，不会和代码库产生游离文件
def save_note(title: str, content: str) -> str:
    """
    保存一条笔记到文件。AI 可以用此工具帮用户记录信息、总结要点。

    参数:
        title: 笔记标题（用于文件名）
        content: 笔记内容（支持 Markdown 格式）
    """
    os.makedirs(NOTES_DIR, exist_ok=True)

    safe_title = "".join(c if c.isalnum() or c in ('-', '_', ' ') else '_' for c in title)
    safe_title = safe_title.strip()[:50] or "untitled"

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{safe_title}.md"
    filepath = os.path.join(NOTES_DIR, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"> 创建时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(content)

    return f"笔记已保存: {filepath}"


def _format_size(size: int) -> str:
    """将字节数格式化为可读字符串"""
    for unit in ('B', 'KB', 'MB', 'GB'):
        if size < 1024:
            return f"{size:.1f} {unit}" if unit != 'B' else f"{size} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


if __name__ == "__main__":
    mcp.run(transport="stdio")

`````

--- **end of file: learn_agent/mcp_servers/system_tools_server.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/mcp_servers/start_mcp_http_scripts/start_all_mcp.py** (project: learn_agent) --- 

`````python
"""
一键启动所有 MCP Server（RAG + Serena）

用途: 同时启动 RAG MCP 和 Serena MCP，供 Open WebUI 连接使用

启动后地址:
  RAG MCP:    http://localhost:9101/mcp
  Serena MCP: http://localhost:9102/mcp
"""
import subprocess
import sys
import os
import signal
import time

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

SERVERS = [
    {
        "name": "RAG MCP",
        "script": os.path.join(SCRIPTS_DIR, "start_rag_mcp.py"),
        "port": 9101,
        "args": [],
    },
    {
        "name": "Serena MCP",
        "script": os.path.join(SCRIPTS_DIR, "start_serena_mcp.py"),
        "port": 9102,
        "args": ["--port", "9102"],
    },
]


def main():
    processes = []
    print("=" * 50)
    print("启动所有 MCP Server")
    print("=" * 50)

    for server in SERVERS:
        name = server["name"]
        script = server["script"]
        port = server["port"]

        if not os.path.exists(script):
            print(f"[跳过] {name}: 脚本不存在 ({script})")
            continue

        extra_args = server.get("args", [])
        print(f"[启动] {name} -> http://localhost:{port}/mcp")
        try:
            env = os.environ.copy()
            env['PYTHONUNBUFFERED'] = '1'
            p = subprocess.Popen(
                [PYTHON, script] + extra_args,
                env=env,
                stdout=sys.stdout,
                stderr=sys.stderr,
            )
            processes.append((name, p))
            time.sleep(1)
        except Exception as e:
            print(f"[错误] {name}: {e}")

    if not processes:
        print("没有成功启动的服务")
        sys.exit(1)

    print(f"\n已启动 {len(processes)} 个 MCP Server，按 Ctrl+C 停止所有服务\n")

    exited = set()
    try:
        while True:
            all_done = True
            for name, p in processes:
                if p.poll() is not None:
                    if name not in exited:
                        print(f"[退出] {name} (exit code: {p.returncode})")
                        exited.add(name)
                else:
                    all_done = False
            if all_done:
                print("所有服务已退出")
                break
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n正在停止所有服务...")
        for name, p in processes:
            if p.poll() is None:
                p.terminate()
                print(f"[停止] {name}")
        for _, p in processes:
            p.wait(timeout=10)
        print("所有服务已停止")


if __name__ == '__main__':
    main()

`````

--- **end of file: learn_agent/mcp_servers/start_mcp_http_scripts/start_all_mcp.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/mcp_servers/start_mcp_http_scripts/start_rag_mcp.py** (project: learn_agent) --- 

`````python
"""
启动 RAG MCP Server（Streamable HTTP 模式）

用途: 为 Open WebUI 等外部客户端提供 RAG 知识库工具
地址: http://localhost:9101/mcp

在 Open WebUI 中配置:
  类型: MCP 流式 HTTP
  URL: http://localhost:9101/mcp
  认证: 无

包含工具: rag_search, rag_grep, rag_find_definition, rag_get_raw_file, rag_stats 等 12 个
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
os.environ.setdefault('PYTHONUNBUFFERED', '1')

from learn_agent.rag.mcp_server import mcp

if __name__ == '__main__':
    print("=" * 50)
    print("RAG MCP Server (Streamable HTTP)")
    print("地址: http://localhost:9101/mcp")
    print("=" * 50)
    mcp.run(transport='streamable-http')

`````

--- **end of file: learn_agent/mcp_servers/start_mcp_http_scripts/start_rag_mcp.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/mcp_servers/start_mcp_http_scripts/start_serena_mcp.py** (project: learn_agent) --- 

`````python
"""
启动 Serena MCP Server（Streamable HTTP 模式）

用途: 为 Open WebUI 等外部客户端提供代码智能工具（索引、符号导航、编辑、终端命令）
地址: http://localhost:9102/mcp

安装 Serena:
  pip install serena-agent
  # 或: uv tool install -p 3.12 serena-agent@latest --prerelease=allow

在 Open WebUI 中配置:
  类型: MCP 流式 HTTP
  URL: http://localhost:9102/mcp
  认证: 无

注意:
  - Serena 是有状态的，一个实例同时只能服务一个项目
  - 默认项目目录: D:/codes/funboost（可通过 --project 参数修改）
  - Serena 有终端命令执行能力，多用户场景需注意安全
"""
import subprocess
import sys
import os
import shutil

DEFAULT_PROJECT = "D:/codes/funboost"
DEFAULT_PORT = 9102

def find_serena():
    """查找 serena 可执行文件路径。"""
    serena = shutil.which("serena")
    if serena:
        return serena

    scripts_dir = os.path.join(os.path.dirname(sys.executable), "Scripts")
    if not os.path.isdir(scripts_dir):
        scripts_dir = os.path.dirname(sys.executable)
    for name in ("serena.exe", "serena"):
        candidate = os.path.join(scripts_dir, name)
        if os.path.isfile(candidate):
            return candidate

    return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="启动 Serena MCP Server")
    parser.add_argument("--project", default=DEFAULT_PROJECT, help="项目目录路径")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="监听端口")
    args = parser.parse_args()

    serena = find_serena()
    if serena is None:
        print("错误: Serena 未安装！")
        print("安装方法:")
        print("  pip install serena-agent")
        print("  # 或: uv tool install -p 3.12 serena-agent@latest --prerelease=allow")
        sys.exit(1)

    cmd = [
        serena,
        "start-mcp-server",
        "--transport", "streamable-http",
        "--port", str(args.port),
        "--project", args.project,
    ]

    print("=" * 50)
    print("Serena MCP Server (Streamable HTTP)")
    print(f"地址: http://localhost:{args.port}/mcp")
    print(f"项目: {args.project}")
    print(f"命令: {' '.join(cmd)}")
    print("=" * 50)

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nSerena 已停止")
    except FileNotFoundError:
        print(f"错误: 找不到 serena 命令: {cmd[0]}")
        print("请先安装: pip install serena-agent")
        sys.exit(1)


if __name__ == '__main__':
    main()

`````

--- **end of file: learn_agent/mcp_servers/start_mcp_http_scripts/start_serena_mcp.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/chunker.py** (project: learn_agent) --- 

`````python
"""
RAG 分块增强模块 —— 文本切分 + 行号计算 + AST scope 解析 + 头部上下文注入。

从 core.py 拆分出来，专注于「把原始文本变成 enriched chunks」这一步。
core.py 专注于存储和检索。
"""

import os
import ast
import bisect
import warnings

from langchain_text_splitters import Language, RecursiveCharacterTextSplitter


DEFAULT_CHUNK_SIZE = 1500
DEFAULT_CHUNK_OVERLAP = 200

# ─── 文件类型映射 ─────────────────────────────────────────

TEXT_EXTENSIONS = {
    ".txt", ".md", ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go",
    ".rs", ".c", ".cpp", ".h", ".hpp", ".cs", ".rb", ".php", ".sh",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf",
    ".csv", ".tsv", ".xml", ".html", ".css", ".sql", ".r", ".lua",
    ".swift", ".kt", ".scala", ".dart", ".vue", ".svelte",
    ".rst", ".tex", ".log", ".env", ".bat", ".ps1",
}

_EXT_TO_LANG = {
    ".py": Language.PYTHON, ".js": Language.JS, ".ts": Language.TS,
    ".jsx": Language.JS, ".tsx": Language.TS,
    ".java": Language.JAVA, ".go": Language.GO,
    ".rs": Language.RUST, ".rb": Language.RUBY,
    ".cpp": Language.CPP, ".c": Language.C, ".h": Language.C, ".hpp": Language.CPP,
    ".cs": Language.CSHARP, ".php": Language.PHP,
    ".swift": Language.SWIFT, ".kt": Language.KOTLIN, ".scala": Language.SCALA,
    ".lua": Language.LUA, ".sol": Language.SOL,
    ".md": Language.MARKDOWN, ".html": Language.HTML,
    ".tex": Language.LATEX, ".rst": Language.RST,
}


# ─── 文本切分 ─────────────────────────────────────────────

def chunk_text(text, chunk_size=DEFAULT_CHUNK_SIZE, overlap=DEFAULT_CHUNK_OVERLAP,
               file_ext=""):
    """根据文件类型自动选择最优切分策略（不含头部注入）。
    代码文件按 class/function 边界切分；Markdown 按标题切分；通用文本按段落切分。
    """
    text = text.strip()
    if not text:
        return []

    lang = _EXT_TO_LANG.get(file_ext.lower())
    if lang:
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=lang, chunk_size=chunk_size, chunk_overlap=overlap,
        )
    else:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=overlap,
            separators=["\n\n", "\n", "。", ".", "；", ";", "，", ",", " ", ""],
        )
    return splitter.split_text(text)


# ─── 行号计算 ─────────────────────────────────────────────

def _build_line_offsets(text):
    """构建行号偏移表: line_offsets[i] = 第 i+1 行的起始字符位置。"""
    offsets = [0]
    for line in text.split('\n'):
        offsets.append(offsets[-1] + len(line) + 1)
    return offsets


def compute_line_ranges(full_text, chunks, overlap=DEFAULT_CHUNK_OVERLAP):
    """为每个 chunk 计算它在原文中的行号范围 (1-based)。

    使用顺序搜索 + 重叠偏移，确保每个 chunk 匹配到正确位置。
    Returns: [(start_line, end_line), ...]
    """
    line_offsets = _build_line_offsets(full_text)
    ranges = []
    search_start = 0

    for chunk in chunks:
        stripped = chunk.strip()
        if not stripped:
            ranges.append((0, 0))
            continue

        needle = stripped[:200]
        pos = full_text.find(needle, search_start)
        if pos == -1:
            pos = full_text.find(needle)

        if pos >= 0:
            start_line = bisect.bisect_right(line_offsets, pos)
            end_pos = pos + len(stripped)
            end_line = bisect.bisect_right(line_offsets, end_pos)
            ranges.append((start_line, end_line))
            advance = max(1, len(stripped) - overlap)
            search_start = pos + advance
        else:
            ranges.append((0, 0))

    return ranges


# ─── Python AST scope 解析 ────────────────────────────────

def _extract_signature(node):
    """从 AST 节点提取函数签名字符串。ClassDef 返回基类列表。"""
    if isinstance(node, ast.ClassDef):
        if node.bases:
            bases = []
            for b in node.bases:
                if isinstance(b, ast.Name):
                    bases.append(b.id)
                elif isinstance(b, ast.Attribute):
                    bases.append(b.attr)
                else:
                    bases.append("?")
            return f"class {node.name}({', '.join(bases)})"
        return f"class {node.name}"

    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = node.args
        params = []
        all_args = args.args + args.posonlyargs
        defaults_offset = len(all_args) - len(args.defaults)
        for i, arg in enumerate(all_args):
            p = arg.arg
            if arg.annotation and isinstance(arg.annotation, ast.Name):
                p += f": {arg.annotation.id}"
            if i >= defaults_offset:
                p += "=..."
            params.append(p)
        if args.vararg:
            params.append(f"*{args.vararg.arg}")
        if args.kwonlyargs:
            if not args.vararg:
                params.append("*")
            for kw in args.kwonlyargs:
                p = kw.arg
                if kw.annotation and isinstance(kw.annotation, ast.Name):
                    p += f": {kw.annotation.id}"
                params.append(p)
        if args.kwarg:
            params.append(f"**{args.kwarg.arg}")
        prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
        sig = f"{prefix} {node.name}({', '.join(params)})"
        if node.returns and isinstance(node.returns, ast.Name):
            sig += f" -> {node.returns.id}"
        return sig

    return ""


def _build_python_scope_map(text):
    """解析 Python 代码，构建 scope 列表。

    返回: [(start_line, end_line, scope_str, signature), ...]
    scope_str 示例: "BrokerEnum", "RedisKeys.gen_xxx", "my_function"
    signature 示例: "def push(self, *func_args, **func_kwargs)"
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(text)
    except SyntaxError:
        return []

    scopes = []

    def _walk(node, parent_chain=""):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                name = child.name
                scope_str = f"{parent_chain}.{name}" if parent_chain else name
                start = child.lineno
                end = child.end_lineno if hasattr(child, 'end_lineno') and child.end_lineno else start
                sig = _extract_signature(child)
                scopes.append((start, end, scope_str, sig))
                _walk(child, scope_str)

    _walk(tree)
    return scopes


def get_python_scope_at_line(text, line_number):
    """给定行号，返回该行所属的完整 scope 链字符串。

    返回示例: "BrokerEnum", "RedisKeys.gen_xxx", ""(模块级)
    """
    scope_map = _build_python_scope_map(text)
    scope, _sig, _parent = _find_scope_in_map(scope_map, line_number)
    return scope


# ─── 头部上下文注入 ───────────────────────────────────────

def _format_header(file_path, line_start, line_end, scope="", signature="",
                   parent_class_sig=""):
    """格式化 chunk 头部注入字符串。"""
    parts = [f"[File: {file_path}]"]
    if scope:
        if "." in scope:
            class_part, method_part = scope.rsplit(".", 1)
            if parent_class_sig:
                parts.append(f"[Class: {parent_class_sig}]")
            else:
                parts.append(f"[Class: {class_part}]")
            parts.append(f"[Method: {method_part}]")
        else:
            parts.append(f"[Scope: {scope}]")
    if signature:
        parts.append(f"[Sig: {signature}]")
    if line_start and line_end:
        parts.append(f"[Lines: {line_start}-{line_end}]")
    return "# " + " ".join(parts)


def _find_scope_in_map(scope_map, line_number):
    """从预构建的 scope_map 中查找指定行号的最内层 scope。
    返回 (scope_str, signature, parent_class_sig) 元组。
    parent_class_sig: 如果当前 scope 是方法（如 Cls.method），返回父类的签名（含继承链）。"""
    best_scope = ""
    best_sig = ""
    best_size = float('inf')
    parent_class_sig = ""
    for entry in scope_map:
        s_start, s_end, s_str = entry[0], entry[1], entry[2]
        sig = entry[3] if len(entry) > 3 else ""
        if s_start <= line_number <= s_end:
            size = s_end - s_start
            if size < best_size:
                best_size = size
                best_scope = s_str
                best_sig = sig
    if "." in best_scope:
        class_name = best_scope.rsplit(".", 1)[0]
        for entry in scope_map:
            if entry[2] == class_name:
                parent_class_sig = entry[3] if len(entry) > 3 else ""
                break
    return best_scope, best_sig, parent_class_sig


def enrich_chunks(chunks, full_text, file_path="", file_ext=""):
    """为 chunks 注入头部上下文信息，返回 (enriched_chunks, line_ranges, scopes)。

    头部注入在 embedding 前完成，让向量包含上下文信息。
    line_ranges 和 scopes 用于存入 metadata。
    """
    if not chunks:
        return [], [], []

    line_ranges = compute_line_ranges(full_text, chunks)

    scope_map = []
    if file_ext.lower() == ".py":
        scope_map = _build_python_scope_map(full_text)

    enriched = []
    scopes = []
    for i, chunk in enumerate(chunks):
        ls, le = line_ranges[i]
        if scope_map and ls > 0:
            scope, sig, parent_cls_sig = _find_scope_in_map(scope_map, ls)
        else:
            scope, sig, parent_cls_sig = "", "", ""
        scopes.append(scope)
        header = _format_header(file_path, ls, le, scope, sig, parent_cls_sig)
        enriched.append(f"{header}\n{chunk}")

    return enriched, line_ranges, scopes


def collect_files(path):
    """收集路径下所有文本文件（支持单文件或递归目录）。"""
    if os.path.isfile(path):
        return [path]
    files = []
    for root, _, fnames in os.walk(path):
        for fn in sorted(fnames):
            if os.path.splitext(fn)[1].lower() in TEXT_EXTENSIONS:
                files.append(os.path.join(root, fn))
    return files

`````

--- **end of file: learn_agent/rag/chunker.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/core.py** (project: learn_agent) --- 

`````python
"""
RAG 核心逻辑 —— 供 MCP 服务和独立脚本共同复用。

功能:
  - SiliconFlow Embedding / Rerank API 调用
  - ChromaDB 向量存储（CRUD + 搜索）
  - 文件导入（切分 + enrichment + 存储）

分块增强逻辑（切分、行号、AST scope、头部注入）在 chunker.py 中。
所有配置从 config.jsonc 的 "rag" 节读取。
"""

import os
import hashlib

import httpx
import chromadb
from learn_agent.config_loader import CONFIG
from learn_agent.rag.chunker import (
    chunk_text, enrich_chunks, collect_files,
    DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP,
)

# ─── 配置 ────────────────────────────────────────────────
_rag_cfg = CONFIG["rag"]

API_KEY = _rag_cfg["siliconflow_api_key"]
EMBEDDING_BASE_URL = _rag_cfg["embedding_base_url"]
EMBEDDING_MODEL = _rag_cfg["embedding_model"]
RERANK_BASE_URL = _rag_cfg["rerank_base_url"]
RERANK_MODEL = _rag_cfg["rerank_model"]

DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "rag_db",
)
os.makedirs(DATA_DIR, exist_ok=True)

RAW_FILES_DIR = os.path.join(DATA_DIR, "raw_files")
os.makedirs(RAW_FILES_DIR, exist_ok=True)

_chroma = chromadb.PersistentClient(path=DATA_DIR)

EMBEDDING_BATCH_SIZE = 32
CHROMA_UPSERT_BATCH = 5000

# doc_id → {filename, source} 映射缓存，避免每次 grep/find_def 都拉全量 metadata
_doc_id_cache = {}     # key = collection_name, value = dict
_doc_id_cache_ts = {}  # key = collection_name, value = timestamp


def _get_doc_id_map(collection_name):
    """获取 collection 的 doc_id → {filename, source} 映射（带 60s 内存缓存）。"""
    import time as _time
    now = _time.time()
    if (collection_name in _doc_id_cache
            and now - _doc_id_cache_ts.get(collection_name, 0) < 60):
        return _doc_id_cache[collection_name]

    col = _get_existing_collection(collection_name)
    if col is None:
        return {}
    all_meta = col.get(include=["metadatas"])
    mapping = {}
    for meta in all_meta["metadatas"]:
        did = meta.get("doc_id", "")
        if did and did not in mapping:
            mapping[did] = {
                "filename": meta.get("filename", "?"),
                "source": meta.get("source", "?"),
            }
    _doc_id_cache[collection_name] = mapping
    _doc_id_cache_ts[collection_name] = now
    return mapping


def invalidate_doc_id_cache(collection_name=None):
    """清除 doc_id 映射缓存（导入/删除 collection 后调用）。"""
    if collection_name:
        _doc_id_cache.pop(collection_name, None)
        _doc_id_cache_ts.pop(collection_name, None)
    else:
        _doc_id_cache.clear()
        _doc_id_cache_ts.clear()


def _normalize_path(path):
    """统一路径格式（跨平台兼容）。
    1. 转为绝对路径
    2. 反斜杠 → 正斜杠
    3. Windows 盘符统一为大写（避免 D: vs d: 不匹配）
    """
    p = os.path.abspath(path).replace("\\", "/")
    if len(p) >= 2 and p[1] == ':':
        p = p[0].upper() + p[1:]
    return p


# ─── 底层工具函数 ─────────────────────────────────────────

def get_collection(name="default"):
    """获取或创建一个 ChromaDB collection（写操作用）。"""
    return _chroma.get_or_create_collection(
        name=name, metadata={"hnsw:space": "cosine"},
    )


def _get_existing_collection(name):
    """获取已存在的 collection，不存在时返回 None（只读操作用，避免自动创建空 collection）。"""
    try:
        return _chroma.get_collection(name=name)
    except (ValueError, Exception):
        return None


def delete_collection(name):
    """删除整个 collection（清空该知识库）。"""
    _chroma.delete_collection(name)
    invalidate_doc_id_cache(name)


def list_collections():
    """列出所有 collection。"""
    return _chroma.list_collections()


_http_client = None

def _get_http_client():
    global _http_client
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.Client(timeout=120)
    return _http_client


def embed(texts, max_retries=3):
    """调用 SiliconFlow Embedding API，自动分批，失败自动重试。"""
    if not API_KEY:
        raise ValueError(
            "SILICONFLOW_API_KEY is empty. "
            "Check env var or dotenv file: D:/codes/ydfhome/importtantdir/envs/sec_dotenv.env"
        )
    import time as _time
    client = _get_http_client()
    all_embeddings = []
    for i in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[i:i + EMBEDDING_BATCH_SIZE]
        for attempt in range(max_retries):
            try:
                resp = client.post(
                    f"{EMBEDDING_BASE_URL}/embeddings",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": EMBEDDING_MODEL,
                        "input": batch,
                        "encoding_format": "float",
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                sorted_data = sorted(data["data"], key=lambda x: x["index"])
                all_embeddings.extend([d["embedding"] for d in sorted_data])
                break
            except Exception:
                if attempt < max_retries - 1:
                    _time.sleep(2 ** attempt)
                else:
                    raise
    return all_embeddings


def rerank(query, documents, top_n=5, max_retries=3):
    """调用 SiliconFlow Rerank API，返回重排后的索引列表，失败自动重试。"""
    import time as _time
    if not API_KEY or not RERANK_MODEL:
        return list(range(min(top_n, len(documents))))

    client = _get_http_client()
    for attempt in range(max_retries):
        try:
            resp = client.post(
                f"{RERANK_BASE_URL}/rerank",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": RERANK_MODEL,
                    "query": query,
                    "documents": documents,
                    "top_n": top_n,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return [r["index"] for r in data["results"]]
        except Exception:
            if attempt < max_retries - 1:
                _time.sleep(2 ** attempt)
            else:
                raise


# ─── 原始文件缓存 ─────────────────────────────────────────

def _raw_file_dir(collection_name):
    d = os.path.join(RAW_FILES_DIR, collection_name)
    os.makedirs(d, exist_ok=True)
    return d


def _raw_file_path(collection_name, doc_id, ext=""):
    return os.path.join(_raw_file_dir(collection_name), f"{doc_id}{ext}")


def _cache_raw_file(text, collection_name, doc_id, ext=""):
    """将原始文件内容缓存到 raw_files/ 目录。"""
    path = _raw_file_path(collection_name, doc_id, ext)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _delete_raw_file(collection_name, doc_id):
    """删除缓存的原始文件（尝试所有可能的扩展名）。"""
    d = os.path.join(RAW_FILES_DIR, collection_name)
    if not os.path.isdir(d):
        return
    prefix = f"{doc_id}"
    for fname in os.listdir(d):
        if fname.startswith(prefix):
            try:
                os.remove(os.path.join(d, fname))
            except OSError:
                pass


def _read_raw_file(collection_name, doc_id):
    """读取缓存的原始文件，返回 (content, cached_path) 或 (None, None)。"""
    d = os.path.join(RAW_FILES_DIR, collection_name)
    if not os.path.isdir(d):
        return None, None
    prefix = f"{doc_id}"
    for fname in os.listdir(d):
        if fname.startswith(prefix):
            fpath = os.path.join(d, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                    return f.read(), fpath
            except OSError:
                return None, None
    return None, None


def _delete_raw_files_collection(collection_name):
    """删除某个 collection 的全部缓存文件。"""
    import shutil
    d = os.path.join(RAW_FILES_DIR, collection_name)
    if os.path.isdir(d):
        shutil.rmtree(d, ignore_errors=True)


# ─── 高级操作 ─────────────────────────────────────────────

def import_single_file(file_path, collection_name="default",
                       chunk_size=DEFAULT_CHUNK_SIZE,
                       chunk_overlap=DEFAULT_CHUNK_OVERLAP):
    """导入单个文件到知识库，返回结果 dict。

    成功:   {"ok": True, "filename": ..., "chars": N, "chunks": N, "doc_id": ...}
    跳过:   {"ok": False, "skipped": True, "reason": "..."}
    失败:   {"ok": False, "error": "..."}
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        return {"ok": False, "error": f"无法读取 {file_path}: {e}"}

    if not text.strip():
        return {"ok": False, "skipped": True, "reason": f"空文件: {os.path.basename(file_path)}"}

    file_ext = os.path.splitext(file_path)[1]
    abs_path = _normalize_path(file_path)
    raw_chunks = chunk_text(text, chunk_size, chunk_overlap, file_ext=file_ext)
    if not raw_chunks:
        return {"ok": False, "skipped": True, "reason": f"切分后无内容: {os.path.basename(file_path)}"}

    enriched_chunks, line_ranges, scopes = enrich_chunks(
        raw_chunks, text, file_path=abs_path, file_ext=file_ext,
    )

    embeddings = embed(enriched_chunks)

    filename = os.path.basename(file_path)
    doc_id = hashlib.md5(abs_path.encode()).hexdigest()[:12]

    _cache_raw_file(text, collection_name, doc_id, file_ext)

    col = get_collection(collection_name)

    try:
        old_data = col.get(where={"doc_id": doc_id}, include=[])
        if old_data["ids"]:
            col.delete(ids=old_data["ids"])
    except Exception:
        pass

    ids = [f"{doc_id}_c{i}" for i in range(len(enriched_chunks))]
    metadatas = [
        {
            "source": abs_path,
            "filename": filename,
            "doc_id": doc_id,
            "chunk_index": i,
            "total_chunks": len(enriched_chunks),
            "line_start": line_ranges[i][0],
            "line_end": line_ranges[i][1],
            "scope": scopes[i],
        }
        for i in range(len(enriched_chunks))
    ]

    for start in range(0, len(ids), CHROMA_UPSERT_BATCH):
        end = start + CHROMA_UPSERT_BATCH
        col.upsert(
            ids=ids[start:end],
            documents=enriched_chunks[start:end],
            embeddings=embeddings[start:end],
            metadatas=metadatas[start:end],
        )
    return {
        "ok": True, "filename": filename,
        "chars": len(text), "chunks": len(enriched_chunks), "doc_id": doc_id,
    }


def import_path(path, collection_name="default",
                chunk_size=DEFAULT_CHUNK_SIZE,
                chunk_overlap=DEFAULT_CHUNK_OVERLAP):
    """导入文件或目录到知识库。返回 (results_list, errors_list, skipped_count)。"""
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return [], [f"路径不存在: {path}"], 0

    files = collect_files(path)
    if not files:
        return [], [f"目录中没有找到文本文件: {path}"], 0

    results = []
    errors = []
    skipped = []
    for fp in files:
        try:
            r = import_single_file(fp, collection_name, chunk_size, chunk_overlap)
        except Exception as e:
            r = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}"}
        if r["ok"]:
            results.append(r)
        elif r.get("skipped"):
            skipped.append(r["reason"])
        else:
            errors.append(r["error"])

    return results, errors, len(skipped)


def batch_import(paths, collection_name="default",
                 chunk_size=DEFAULT_CHUNK_SIZE,
                 chunk_overlap=DEFAULT_CHUNK_OVERLAP,
                 delete_first=False, on_progress=None,
                 verbose=False):
    """批量导入多个路径到知识库（一站式封装）。"""
    import time as _time

    if isinstance(paths, str):
        paths = [paths]

    t0 = _time.time()

    if delete_first:
        deleted_col = False
        try:
            delete_collection(collection_name)
            deleted_col = True
        except Exception:
            pass
        try:
            _delete_raw_files_collection(collection_name)
        except Exception:
            pass
        if verbose:
            print(f"[rag] 已删除旧 collection: {collection_name}"
                  f" (collection={'ok' if deleted_col else 'not found'}, raw_files=cleaned)")

    all_files = []
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.exists(p):
            found = collect_files(p)
            if verbose:
                print(f"[rag] {p} -> {len(found)} 个文件")
            all_files.extend(found)

    if verbose:
        print(f"[rag] 共 {len(all_files)} 个文件, 开始 Embedding...\n")

    results = []
    errors = []
    skipped = []
    total_chars = 0
    total_chunks = 0
    large_files = []

    for i, fp in enumerate(all_files):
        file_size = os.path.getsize(fp)
        if file_size > 100 * 1024:
            size_kb = file_size / 1024
            large_files.append((fp, file_size))
            if verbose:
                print(f"  [大文件] {fp} ({size_kb:.1f} KB)")

        try:
            r = import_single_file(fp, collection_name, chunk_size, chunk_overlap)
        except Exception as e:
            r = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}"}

        if r["ok"]:
            results.append(r)
            total_chars += r["chars"]
            total_chunks += r["chunks"]
        elif r.get("skipped"):
            skipped.append(r["reason"])
        else:
            errors.append(r["error"])

        if on_progress:
            on_progress(i + 1, len(all_files), fp, r)
        elif verbose:
            idx = i + 1
            name = os.path.basename(fp)
            if r["ok"]:
                print(f"  [{idx:>4}/{len(all_files)}] {name} ({r['chunks']}块)")
            elif r.get("skipped"):
                print(f"  [{idx:>4}/{len(all_files)}] - {name}  (跳过: 空文件)")
            else:
                err_msg = r.get("error", "未知错误")
                print(f"  [{idx:>4}/{len(all_files)}] X {name}  ({err_msg})")

    elapsed = _time.time() - t0
    stats = {
        "success": len(results), "failed": len(errors), "skipped": len(skipped),
        "total_chars": total_chars, "total_chunks": total_chunks,
        "file_count": len(all_files), "elapsed": elapsed,
        "results": results, "errors": errors, "skipped_reasons": skipped,
        "large_files": large_files,
    }

    if verbose:
        skip_str = f" {stats['skipped']}跳过" if skipped else ""
        print(f"\n[rag] 完成! {stats['success']}成功 {stats['failed']}失败{skip_str}"
              f" | {total_chunks}块 {total_chars:,}字 | {elapsed:.0f}s")
        if large_files:
            print(f"\n[rag] 超过100KB的大文件汇总 ({len(large_files)}个):")
            large_files_sorted = sorted(large_files, key=lambda x: x[1], reverse=True)
            for fp, size in large_files_sorted:
                print(f"  {size / 1024:.1f} KB  {fp}")
            total_large_size = sum(s for _, s in large_files)
            print(f"  合计: {len(large_files)}个文件, {total_large_size / 1024 / 1024:.2f} MB")

    return stats


def search(query, collection_name="default", top_k=5, use_rerank=True,
           filter_filename=None):
    """语义搜索。返回 (documents, metadatas, distances, rerank_used, total)。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return [], [], [], False, 0
    total = col.count()

    if total == 0:
        return [], [], [], False, 0

    query_vec = embed([query])[0]
    retrieve_k = min(top_k * 4, total) if use_rerank else min(top_k, total)

    where_filter = None
    if filter_filename:
        where_filter = {"filename": filter_filename}

    results = col.query(
        query_embeddings=[query_vec],
        n_results=retrieve_k,
        where=where_filter,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    rerank_used = False
    if use_rerank and RERANK_MODEL and len(documents) > top_k:
        try:
            reranked_idx = rerank(query, documents, top_n=top_k)
            documents = [documents[i] for i in reranked_idx]
            metadatas = [metadatas[i] for i in reranked_idx]
            distances = [distances[i] for i in reranked_idx]
            rerank_used = True
        except Exception:
            documents = documents[:top_k]
            metadatas = metadatas[:top_k]
            distances = distances[:top_k]
    else:
        documents = documents[:top_k]
        metadatas = metadatas[:top_k]
        distances = distances[:top_k]

    return documents, metadatas, distances, rerank_used, total


def get_file_chunks(file_identifier, collection_name="default",
                    start_chunk=0, max_chunks=5,
                    raw=False, line_start=-1, line_end=-1):
    """按文件路径或文件名获取知识库中该文件的内容。

    file_identifier: 完整绝对路径（优先匹配 source 字段）或文件名（fallback 匹配 filename 字段）
    raw=False (默认): 返回 chunks 分页列表（含 overlap）
    raw=True: 返回缓存的原始文件内容（无 overlap），支持按行截取
    """
    col = _get_existing_collection(collection_name)
    if col is None:
        return {"found": False, "error": f"collection '{collection_name}' does not exist"}
    total = col.count()
    if total == 0:
        return {"found": False, "error": f"collection '{collection_name}' is empty"}

    all_data = _query_file_by_identifier(col, file_identifier)

    if not all_data["ids"]:
        return {"found": False, "error": f"未找到文件 '{file_identifier}'"}

    items = list(zip(all_data["ids"], all_data["documents"], all_data["metadatas"]))
    items.sort(key=lambda x: x[2].get("chunk_index", 0))

    first_meta = items[0][2]
    total_chunks = len(items)
    max_line = max(m.get("line_end", 0) for _, _, m in items)
    doc_id = first_meta.get("doc_id", "?")
    source = first_meta.get("source", "?")
    actual_filename = first_meta.get("filename", "?")

    if raw:
        return _get_raw_file_result(
            collection_name, doc_id, source, actual_filename,
            total_chunks, max_line, line_start, line_end,
        )

    chunk_line_ranges = [
        (m.get("line_start", 0), m.get("line_end", 0)) for _, _, m in items
    ]

    end_chunk = min(start_chunk + max_chunks, total_chunks)
    selected = items[start_chunk:end_chunk]

    chunks = []
    for _, doc, meta in selected:
        chunks.append({
            "index": meta.get("chunk_index", 0),
            "line_start": meta.get("line_start", 0),
            "line_end": meta.get("line_end", 0),
            "scope": meta.get("scope", ""),
            "content": doc,
        })

    return {
        "found": True,
        "source": source,
        "filename": actual_filename,
        "doc_id": doc_id,
        "total_chunks": total_chunks,
        "total_lines": max_line,
        "chunk_line_ranges": chunk_line_ranges,
        "chunks": chunks,
        "start_chunk": start_chunk,
        "end_chunk": end_chunk,
    }


def _query_file_by_identifier(col, file_identifier):
    """按路径或文件名查找文件的 chunks。优先匹配 source（完整路径），fallback 到 filename。"""
    is_path = ('/' in file_identifier or '\\' in file_identifier)
    empty = {"ids": [], "documents": [], "metadatas": []}

    if is_path:
        normalized = _normalize_path(file_identifier)
        try:
            result = col.get(where={"source": normalized}, include=["documents", "metadatas"])
            if result["ids"]:
                return result
        except Exception:
            pass
        basename = os.path.basename(file_identifier)
        try:
            return col.get(where={"filename": basename}, include=["documents", "metadatas"])
        except Exception:
            return empty

    try:
        return col.get(where={"filename": file_identifier}, include=["documents", "metadatas"])
    except Exception:
        return empty


def _get_raw_file_result(collection_name, doc_id, source, filename,
                         total_chunks, total_lines, line_start, line_end):
    """从缓存读取原始文件，支持按行截取。"""
    content, cached_path = _read_raw_file(collection_name, doc_id)
    if content is None:
        return {
            "found": False,
            "error": f"原始文件缓存不存在 (doc_id={doc_id})。"
                     f"该文件可能在缓存功能上线前导入，请重新导入。",
        }

    lines = content.splitlines(keepends=True)
    actual_total = len(lines)

    ls = max(1, line_start) if line_start > 0 else 1
    le = min(actual_total, line_end) if line_end > 0 else actual_total
    selected_lines = lines[ls - 1:le]

    return {
        "found": True,
        "raw": True,
        "source": source,
        "filename": filename,
        "doc_id": doc_id,
        "total_chunks": total_chunks,
        "total_lines": actual_total,
        "line_start": ls,
        "line_end": le,
        "content": "".join(selected_lines),
    }


def get_context_chunks(doc_id, collection_name="default",
                       chunk_index=None, window=2,
                       line_start=None, line_end=None):
    """获取指定文档的上下文 chunks。

    两种模式:
    1. 按 chunk_index + window: 返回 [chunk_index-window, chunk_index+window]
    2. 按 line_start + line_end: 返回覆盖该行号范围的所有 chunks
    """
    col = _get_existing_collection(collection_name)
    if col is None:
        return {"found": False, "error": f"collection '{collection_name}' does not exist"}

    try:
        all_data = col.get(
            where={"doc_id": doc_id},
            include=["documents", "metadatas"],
        )
    except Exception:
        all_data = {"ids": [], "documents": [], "metadatas": []}

    if not all_data["ids"]:
        return {"found": False, "error": f"未找到文档 '{doc_id}'"}

    items = list(zip(all_data["ids"], all_data["documents"], all_data["metadatas"]))
    items.sort(key=lambda x: x[2].get("chunk_index", 0))

    if chunk_index is not None:
        idx_min = max(0, chunk_index - window)
        idx_max = min(len(items) - 1, chunk_index + window)
        selected = items[idx_min:idx_max + 1]
    elif line_start is not None and line_end is not None:
        selected = []
        for item in items:
            meta = item[2]
            cl_start = meta.get("line_start", 0)
            cl_end = meta.get("line_end", 0)
            if cl_start < line_end and cl_end > line_start:
                selected.append(item)
        if not selected:
            return {"found": True, "chunks": [],
                    "message": f"行号范围 {line_start}-{line_end} 没有匹配的 chunks"}
    else:
        return {"found": False, "error": "需要提供 chunk_index 或 line_start+line_end"}

    first_meta = items[0][2]
    chunks = []
    for _, doc, meta in selected:
        chunks.append({
            "index": meta.get("chunk_index", 0),
            "line_start": meta.get("line_start", 0),
            "line_end": meta.get("line_end", 0),
            "scope": meta.get("scope", ""),
            "content": doc,
        })

    return {
        "found": True,
        "source": first_meta.get("source", "?"),
        "filename": first_meta.get("filename", "?"),
        "doc_id": doc_id,
        "total_chunks": len(items),
        "chunks": chunks,
    }


def grep_knowledge(keyword, collection_name="default", max_results=10,
                    case_sensitive=False, filter_filename=None, context_lines=5):
    """在知识库的原始缓存文件中进行关键词/正则搜索。

    与 search() 的区别: search() 是语义向量匹配，适合自然语言问题；
    grep_knowledge() 是精确文本匹配，适合查找类名、函数名、常量、配置项等符号。

    返回: list[dict]，每个 dict 包含 filename, source, doc_id, line_number, line_content, context。
    """
    import re

    raw_dir = os.path.join(RAW_FILES_DIR, collection_name)
    if not os.path.isdir(raw_dir):
        return []

    doc_id_to_info = _get_doc_id_map(collection_name)

    flags = 0 if case_sensitive else re.IGNORECASE
    try:
        pattern = re.compile(keyword, flags)
    except re.error:
        pattern = re.compile(re.escape(keyword), flags)

    results = []
    for fname in os.listdir(raw_dir):
        doc_id = os.path.splitext(fname)[0]
        info = doc_id_to_info.get(doc_id, {})

        if filter_filename and info.get("filename", "") != filter_filename:
            continue

        fpath = os.path.join(raw_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                file_lines = f.readlines()
        except OSError:
            continue

        for i, line in enumerate(file_lines):
            if pattern.search(line):
                ctx_start = max(0, i - context_lines)
                ctx_end = min(len(file_lines), i + context_lines + 1)
                ctx_parts = []
                for j in range(ctx_start, ctx_end):
                    prefix = ">>>" if j == i else "   "
                    ctx_parts.append(f"{prefix} {j + 1:>5}| {file_lines[j].rstrip()}")

                results.append({
                    "filename": info.get("filename", fname),
                    "source": info.get("source", fpath),
                    "doc_id": doc_id,
                    "line_number": i + 1,
                    "line_content": line.rstrip(),
                    "context": "\n".join(ctx_parts),
                })

                if len(results) >= max_results:
                    return results

    return results


def find_symbol_definition(symbol, collection_name="default", max_results=5):
    """在知识库中查找符号（类/函数/方法）的完整定义。

    利用 AST 精确定位 Python 类/函数的起止行号，返回完整定义源码。
    非 Python 文件降级为 grep + 大上下文。

    返回: list[dict]，每个 dict 包含 filename, source, doc_id, symbol_type, line_start, line_end, definition。
    """
    import re
    import ast as _ast
    import warnings as _warnings

    raw_dir = os.path.join(RAW_FILES_DIR, collection_name)
    if not os.path.isdir(raw_dir):
        return []

    doc_id_to_info = _get_doc_id_map(collection_name)

    all_files = os.listdir(raw_dir)
    py_files = [f for f in all_files if f.lower().endswith(".py")]
    other_files = [f for f in all_files if not f.lower().endswith(".py")]

    results = []

    def _scan_py(fname):
        doc_id = os.path.splitext(fname)[0]
        info = doc_id_to_info.get(doc_id, {})
        fpath = os.path.join(raw_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            return
        try:
            with _warnings.catch_warnings():
                _warnings.simplefilter("ignore", SyntaxWarning)
                tree = _ast.parse(content)
        except SyntaxError:
            return

        file_lines = content.splitlines()

        def _search_nodes(node, parent_chain=""):
            for child in _ast.iter_child_nodes(node):
                if isinstance(child, (_ast.ClassDef, _ast.FunctionDef, _ast.AsyncFunctionDef)):
                    name = child.name
                    qualified = f"{parent_chain}.{name}" if parent_chain else name
                    if name == symbol or qualified == symbol or qualified.endswith(f".{symbol}"):
                        start = child.lineno
                        end = child.end_lineno if hasattr(child, 'end_lineno') and child.end_lineno else start
                        definition_lines = file_lines[start - 1:end]
                        sym_type = "class" if isinstance(child, _ast.ClassDef) else "function"

                        methods_summary = ""
                        if isinstance(child, _ast.ClassDef):
                            method_sigs = []
                            for sub in _ast.iter_child_nodes(child):
                                if isinstance(sub, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
                                    from learn_agent.rag.chunker import _extract_signature
                                    method_sigs.append(_extract_signature(sub))
                            if method_sigs:
                                methods_summary = "\n".join(f"  {s}" for s in method_sigs)

                        results.append({
                            "filename": info.get("filename", fname),
                            "source": info.get("source", fpath),
                            "doc_id": doc_id,
                            "symbol_type": sym_type,
                            "qualified_name": qualified,
                            "line_start": start,
                            "line_end": end,
                            "definition": "\n".join(definition_lines),
                            "methods_summary": methods_summary,
                        })
                    _search_nodes(child, qualified)

        _search_nodes(tree)

    for fname in py_files:
        _scan_py(fname)
        if len(results) >= max_results:
            break

    if len(results) < max_results:
        pattern = re.compile(r'\b' + re.escape(symbol) + r'\b')
        for fname in other_files:
            doc_id = os.path.splitext(fname)[0]
            info = doc_id_to_info.get(doc_id, {})
            fpath = os.path.join(raw_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue
            file_lines = content.splitlines()
            for i, line in enumerate(file_lines):
                if pattern.search(line):
                    ctx_start = max(0, i - 3)
                    ctx_end = min(len(file_lines), i + 20)
                    results.append({
                        "filename": info.get("filename", fname),
                        "source": info.get("source", fpath),
                        "doc_id": doc_id,
                        "symbol_type": "unknown",
                        "qualified_name": symbol,
                        "line_start": i + 1,
                        "line_end": ctx_end,
                        "definition": "\n".join(file_lines[ctx_start:ctx_end]),
                        "methods_summary": "",
                    })
                    break
            if len(results) >= max_results:
                break

    return results


def list_documents(collection_name="default"):
    """列出知识库中已导入的文档。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return {}
    total = col.count()
    if total == 0:
        return {}

    all_data = col.get(include=["metadatas"])
    docs = {}
    for meta in all_data["metadatas"]:
        if meta is None:
            continue
        did = meta.get("doc_id", "unknown")
        if did not in docs:
            docs[did] = {
                "filename": meta.get("filename", "?"),
                "source": meta.get("source", "?"),
                "total_chunks": meta.get("total_chunks", 0),
                "chunk_count": 0,
            }
        docs[did]["chunk_count"] += 1
    return docs


def delete_document(doc_id, collection_name="default"):
    """删除指定文档的所有向量数据及缓存文件。返回 (deleted_count, filename)。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return 0, "?"

    try:
        doc_data = col.get(where={"doc_id": doc_id}, include=["metadatas"])
    except Exception:
        doc_data = {"ids": [], "metadatas": []}

    if not doc_data["ids"]:
        return 0, "?"

    filename = doc_data["metadatas"][0].get("filename", "?") if doc_data["metadatas"] else "?"
    col.delete(ids=doc_data["ids"])
    _delete_raw_file(collection_name, doc_id)
    return len(doc_data["ids"]), filename


def get_stats():
    """返回所有知识库的统计信息。"""
    collections = list_collections()
    stats = {
        "embedding_model": EMBEDDING_MODEL,
        "rerank_model": RERANK_MODEL or "未配置",
        "data_dir": DATA_DIR,
        "collection_count": len(collections),
        "collections": {},
    }

    for col_obj in collections:
        name = col_obj.name
        try:
            col = _chroma.get_collection(name)
            count = col.count()
            if count > 0:
                all_meta = col.get(include=["metadatas"])
                doc_ids = set(m.get("doc_id", "") for m in all_meta["metadatas"] if m is not None)
                stats["collections"][name] = {
                    "doc_count": len(doc_ids), "chunk_count": count,
                }
            else:
                stats["collections"][name] = {"doc_count": 0, "chunk_count": 0}
        except Exception as e:
            stats["collections"][name] = {"error": str(e)}

    return stats

`````

--- **end of file: learn_agent/rag/core.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/import_funboost.py** (project: learn_agent) --- 

`````python
"""
导入 funboost 项目到 RAG 知识库。

    set PYTHONPATH=D:/codes/ai_proj
    python learn_agent/rag/import_funboost.py
"""
from learn_agent.rag.core import batch_import

batch_import(
    paths=[
        "D:/codes/funboost/funboost",
        "D:/codes/funboost/test_frame",
        "D:/codes/funboost/tests",
        "D:/codes/funboost_docs/source/articles/c0.md",
        "D:/codes/funboost_docs/source/articles/c1.md",
        "D:/codes/funboost_docs/source/articles/c2.md",
        "D:/codes/funboost_docs/source/articles/c3.md",
        "D:/codes/funboost_docs/source/articles/c4.md",
        "D:/codes/funboost_docs/source/articles/c4b.md",
        "D:/codes/funboost_docs/source/articles/c6.md",
        "D:/codes/funboost_docs/source/articles/c7.md",
        "D:/codes/funboost_docs/source/articles/c8.md",
        "D:/codes/funboost_docs/source/articles/c9.md",
        "D:/codes/funboost_docs/source/articles/c10.md",
        "D:/codes/funboost_docs/source/articles/c11.md",
        "D:/codes/funboost_docs/source/articles/c12.md",
        "D:/codes/funboost_docs/source/articles/c13.md",
        "D:/codes/funboost_docs/source/articles/c14.md",
        "D:/codes/funboost_docs/source/articles/c15.md",
        "D:/codes/funboost_docs/source/articles/c20.md",
    ],
    collection_name="funboost",
    delete_first=True,
    verbose=True,
)

`````

--- **end of file: learn_agent/rag/import_funboost.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/mcp_server.py** (project: learn_agent) --- 

`````python
"""
RAG 知识库 MCP Server —— 薄包装层，所有逻辑复用 core.py。

Tools (12):
  1. rag_add_document         → Import file/directory into collection
  2. rag_search               → Semantic search (vector + rerank)
  3. rag_search_and_fetch     → Search + auto-fetch raw source (combo tool)
  4. rag_grep                 → Keyword/regex exact search (complements semantic search)
  5. rag_find_definition      → Find complete class/function definition by symbol name
  6. rag_get_file_chunks      → Paginated chunks with scope/line metadata
  7. rag_get_raw_file         → Raw file content without overlap
  8. rag_get_adjacent_chunks  → Adjacent chunks by chunk index
  9. rag_get_chunks_by_lines  → Chunks covering a line range
  10. rag_list                → List imported documents
  11. rag_delete              → Delete a document
  12. rag_stats               → Collection overview and config

运行方式: 由 MCP Client 作为子进程自动启动（stdio 传输）。
"""

from pydantic import Field
from mcp.server.fastmcp import FastMCP
from learn_agent.rag.chunker import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP
from learn_agent.rag.core import (
    EMBEDDING_MODEL, RERANK_MODEL,
    import_path, search, list_documents, delete_document, get_stats,
    get_file_chunks, get_context_chunks, grep_knowledge, find_symbol_definition,
)

mcp = FastMCP("rag-tools", port=9101)


@mcp.tool()
def rag_add_document(
    path: str = Field(description="Absolute path to a file or directory. Directory imports all text files recursively"),
    collection_name: str = Field(description="Collection name (required, auto-created if not exists. Use rag_stats to see existing)"),
    chunk_size: int = Field(default=DEFAULT_CHUNK_SIZE, description="Chunk size in chars, default 1500, recommended 1000-2000"),
    chunk_overlap: int = Field(default=DEFAULT_CHUNK_OVERLAP, description="Chunk overlap in chars, default 200"),
) -> str:
    """Import file or directory into RAG collection. Auto-creates collection if not exists.
    Each chunk is enriched with file path, line numbers, and Python class/function scope.
    Use rag_search to retrieve imported content."""
    results, errors, skipped_count = import_path(path, collection_name, chunk_size, chunk_overlap)

    total_chunks = sum(r["chunks"] for r in results)
    total_chars = sum(r["chars"] for r in results)

    skip_str = f", {skipped_count} skipped" if skipped_count else ""
    lines = [f"Import done: {len(results)} ok, {len(errors)} failed{skip_str}"]
    lines.append(f"collection: {collection_name} | chars: {total_chars} | chunks: {total_chunks}")
    lines.append(f"chunk_size={chunk_size} overlap={chunk_overlap} | embed: {EMBEDDING_MODEL}")

    if len(results) <= 10:
        lines.append("")
        for r in results:
            lines.append(f"  {r['filename']} ({r['chunks']} chunks, {r['chars']} chars, doc_id:{r['doc_id']})")
    else:
        lines.append(f"\n{len(results)} files imported (too many to list)")

    if errors:
        lines.append(f"\nFailed ({len(errors)}):")
        for e in errors[:10]:
            lines.append(f"  {e}")

    return "\n".join(lines)


@mcp.tool()
def rag_search(
    query: str = Field(description="Search query (natural language question or keywords)"),
    collection_name: str = Field(description="Collection name (required, use rag_stats to see available collections)"),
    top_k: int = Field(default=5, description="Number of results to return"),
    use_rerank: bool = Field(default=True, description="Enable reranker for better accuracy (recommended)"),
    filter_filename: str = Field(default="", description="Optional: filter by filename only (e.g. 'constant.py', not full path)"),
) -> str:
    """Semantic search in RAG collection. Vector recall + Rerank. Call rag_stats first to see available collections.

    Each result contains: file_path (full path), chunk:X/Y, line:N-M, scope, doc_id, dist (cosine distance, lower=more similar).

    Recommended deep-analysis workflow (use multiple tools, not just search):
      1. rag_search → find relevant files and rough location
      2. rag_grep → pinpoint exact class/method/constant names (what semantic search may miss)
      3. rag_find_definition → get complete class/function source with inheritance chain
      4. rag_get_raw_file → read full source code to verify details
      5. Cross-file tracing: when you see unknown symbols in code, repeat steps 2-4 to trace references

    Follow-up tools — use result fields directly as parameters:
      - rag_find_definition(symbol, collection_name) → complete class/function definition + methods summary
      - rag_get_raw_file(file_path, collection_name) → full source code without overlap
      - rag_get_file_chunks(file_path, collection_name) → paginated chunks with scope metadata
      - rag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result
      - rag_get_chunks_by_lines(doc_id, line_start, line_end, collection_name) → chunks covering line range"""
    fname_filter = filter_filename if filter_filename else None
    documents, metadatas, distances, rerank_used, total = search(
        query, collection_name, top_k, use_rerank,
        filter_filename=fname_filter,
    )

    if total == 0:
        stats = get_stats()
        avail = list(stats["collections"].keys())
        exists = collection_name in avail
        if not exists:
            return (f"collection '{collection_name}' does not exist.\n"
                    f"Available collections: {avail}\n"
                    f"Use rag_add_document to create and import docs.")
        return (f"collection '{collection_name}' is empty. "
                f"Use rag_add_document to import docs first.")

    if not documents:
        return f"No results (collection has {total} chunks, filter: {filter_filename or 'none'})"

    rerank_str = RERANK_MODEL if rerank_used else "off"
    header = f"[{collection_name}] {total} chunks | rerank: {rerank_str}"
    if filter_filename:
        header += f" | filter: {filter_filename}"
    lines = [header, ""]

    preview_limit = min(8000, 40000 // max(len(documents), 1))
    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances)):
        if meta is None:
            meta = {}
        src = meta.get("source", meta.get("filename", "?"))
        ci = meta.get("chunk_index", "?")
        tc = meta.get("total_chunks", "?")
        ls = meta.get("line_start", 0)
        le = meta.get("line_end", 0)
        scope = meta.get("scope", "")
        doc_id = meta.get("doc_id", "?")

        meta_parts = [f"chunk:{ci}/{tc}"]
        if ls and le:
            meta_parts.append(f"line:{ls}-{le}")
        if scope:
            meta_parts.append(f"scope:{scope}")
        meta_parts.append(f"doc_id:{doc_id}")
        meta_parts.append(f"dist:{dist:.4f}")

        lines.append(f"[{i + 1}/{len(documents)}] {meta.get('filename', '?')} {' '.join(meta_parts)}")
        lines.append(f"file_path: {src}")
        preview = doc[:preview_limit] + ("..." if len(doc) > preview_limit else "")
        lines.append(preview)
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def rag_search_and_fetch(
    query: str = Field(description="Search query (natural language question or keywords)"),
    collection_name: str = Field(description="Collection name (required, use rag_stats to see available collections)"),
    top_k: int = Field(default=5, description="Number of search results to return"),
    fetch_top_n_raw: int = Field(default=3, description="Auto-fetch raw source for top N results (0 to skip fetching)"),
    context_lines: int = Field(default=100, description="Lines of context around matched chunk. Small files (≤2x this) are fetched fully"),
) -> str:
    """Search + auto-fetch raw source code for top results in one call (combo tool).
    Saves a round-trip vs calling rag_search then rag_get_raw_file separately.
    Same doc_id appearing in multiple results is fetched only once with merged line range."""
    fname_filter = None
    documents, metadatas, distances, rerank_used, total = search(
        query, collection_name, top_k, True, filter_filename=fname_filter,
    )

    if total == 0:
        stats = get_stats()
        avail = list(stats["collections"].keys())
        exists = collection_name in avail
        if not exists:
            return (f"collection '{collection_name}' does not exist.\n"
                    f"Available collections: {avail}\n"
                    f"Use rag_add_document to create and import docs.")
        return (f"collection '{collection_name}' is empty. "
                f"Use rag_add_document to import docs first.")

    if not documents:
        return f"No results (collection has {total} chunks)"

    rerank_str = RERANK_MODEL if rerank_used else "off"
    lines = [f"[{collection_name}] {total} chunks | rerank: {rerank_str}", ""]

    preview_limit = min(8000, 40000 // max(len(documents), 1))
    fetch_targets = {}
    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances)):
        if meta is None:
            meta = {}
        src = meta.get("source", meta.get("filename", "?"))
        ci = meta.get("chunk_index", "?")
        tc = meta.get("total_chunks", "?")
        _ls = meta.get("line_start", 0)
        _le = meta.get("line_end", 0)
        ls = int(_ls) if isinstance(_ls, (int, float)) else 0
        le = int(_le) if isinstance(_le, (int, float)) else 0
        scope = str(meta.get("scope", ""))
        doc_id = str(meta.get("doc_id", "?"))

        meta_parts = [f"chunk:{ci}/{tc}"]
        if ls and le:
            meta_parts.append(f"line:{ls}-{le}")
        if scope:
            meta_parts.append(f"scope:{scope}")
        meta_parts.append(f"doc_id:{doc_id}")
        meta_parts.append(f"dist:{dist:.4f}")

        lines.append(f"[{i + 1}/{len(documents)}] {meta.get('filename', '?')} {' '.join(meta_parts)}")
        lines.append(f"file_path: {src}")
        preview = doc[:preview_limit] + ("..." if len(doc) > preview_limit else "")
        lines.append(preview)
        lines.append("")

        if i < fetch_top_n_raw and doc_id != "?" and src != "?":
            if doc_id not in fetch_targets:
                fetch_targets[doc_id] = {"src": str(src), "line_min": ls, "line_max": le}
            else:
                t = fetch_targets[doc_id]
                if ls:
                    t["line_min"] = min(t["line_min"], ls) if t["line_min"] else ls
                if le:
                    t["line_max"] = max(t["line_max"], le) if t["line_max"] else le

    if fetch_targets:
        lines.append("=" * 40)
        lines.append(f"Auto-fetched raw source ({len(fetch_targets)} file(s)):")
        lines.append("")

    for doc_id, target in fetch_targets.items():
        center_start = target["line_min"] or 1
        center_end = target["line_max"] or center_start
        center = (center_start + center_end) // 2
        half = context_lines

        raw_result = get_file_chunks(
            target["src"], collection_name, 0, 0,
            raw=True, line_start=-1, line_end=-1,
        )

        if not raw_result.get("found"):
            lines.append(f"[{target['src']}] raw cache not available")
            lines.append("")
            continue

        tl = raw_result["total_lines"]
        if tl <= context_lines * 2:
            lines.append(_format_raw_result(raw_result))
        else:
            fetch_start = max(1, center - half)
            fetch_end = min(tl, center + half)
            excerpt = get_file_chunks(
                target["src"], collection_name, 0, 0,
                raw=True, line_start=fetch_start, line_end=fetch_end,
            )
            if excerpt.get("found"):
                lines.append(_format_raw_result(excerpt))
            else:
                lines.append(f"[{target['src']}] excerpt failed")
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def rag_grep(
    keyword: str = Field(description="Keyword or regex pattern (e.g. class name 'ConsumerCacheProxy', method '_dispatch_task', constant 'redis_bulk_push')"),
    collection_name: str = Field(description="Collection name (required, use rag_stats to see available collections)"),
    max_results: int = Field(default=10, description="Maximum number of matches to return"),
    case_sensitive: bool = Field(default=False, description="Case-sensitive matching"),
    filter_filename: str = Field(default="", description="Optional: filter by filename only (e.g. 'booster.py', not full path)"),
    context_lines: int = Field(default=10, description="Lines of context before and after each match (default 10, use 20+ for seeing full function/class headers)"),
) -> str:
    """Keyword/regex exact search in cached raw files. Complements rag_search (semantic search).

    Use cases where rag_search falls short:
      - Find class/function/variable names: 'ConsumerCacheProxy', '_dispatch_task'
      - Find config keys/constants: 'redis_bulk_push', 'concurrent_num'
      - Find import statements: 'from funboost.core'
      - Find string literals: 'queue_test2'

    Tip: use context_lines=15 to see class headers + inheritance chain around the match.
    For complete definitions, use rag_find_definition instead.
    Typical workflow: rag_search (find direction) → rag_grep (pinpoint symbols) → rag_find_definition (full definition)"""
    fname_filter = filter_filename if filter_filename else None
    results = grep_knowledge(
        keyword, collection_name, max_results, case_sensitive,
        filter_filename=fname_filter, context_lines=context_lines,
    )

    if not results:
        return f"No matches for '{keyword}' (collection: {collection_name})"

    lines = [f"grep: '{keyword}' | collection_name: {collection_name} | {len(results)} match(es)", ""]
    for i, r in enumerate(results):
        lines.append(f"[{i + 1}/{len(results)}] {r['filename']} line:{r['line_number']} doc_id:{r['doc_id']}")
        lines.append(f"file_path: {r['source']}")
        lines.append(r["context"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def rag_find_definition(
    symbol: str = Field(description="Symbol name to find (class name like 'ConsumerCacheProxy', function name like '_dispatch_task', or qualified name like 'Booster.__call__')"),
    collection_name: str = Field(description="Collection name (required, use rag_stats to see available collections)"),
    max_results: int = Field(default=5, description="Maximum number of definitions to return"),
) -> str:
    """Find the complete definition of a class/function/method by symbol name.
    Uses AST parsing to extract exact boundaries — returns the FULL source code of the definition.
    For classes, also returns a methods summary (all method signatures).

    Best for cross-file tracing: when you see an unknown symbol in code, use this to get its complete definition.
    Much more efficient than grep + raw_file for understanding class hierarchy and implementation."""
    results = find_symbol_definition(symbol, collection_name, max_results)

    if not results:
        return f"No definition found for '{symbol}' (collection: {collection_name}). Try rag_grep for a broader search."

    lines = [f"definition: '{symbol}' | collection_name: {collection_name} | {len(results)} found", ""]
    for i, r in enumerate(results):
        header_parts = [
            f"[{i + 1}/{len(results)}]",
            f"{r['symbol_type']}",
            f"{r['qualified_name']}",
            f"line:{r['line_start']}-{r['line_end']}",
            f"doc_id:{r['doc_id']}",
        ]
        lines.append(" ".join(header_parts))
        lines.append(f"file_path: {r['source']}")

        if r.get("methods_summary"):
            lines.append("methods:")
            lines.append(r["methods_summary"])

        lines.append("---")
        lines.append(r["definition"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def rag_get_file_chunks(
    file_path: str = Field(description="Full absolute path (use 'file_path' value from rag_search results)"),
    collection_name: str = Field(description="Collection name (use rag_stats to see available collections)"),
    start_chunk: int = Field(default=0, description="Start chunk index (0-based), use for pagination"),
    max_chunks: int = Field(default=10, description="Max chunks to return (use for pagination)"),
) -> str:
    """Paginated view of file chunks with scope and line metadata. Use start_chunk to paginate.
    Note: adjacent chunks have overlap. For clean source code without overlap, use rag_get_raw_file instead."""
    result = get_file_chunks(
        file_path, collection_name, start_chunk, max_chunks,
        raw=False,
    )

    if not result.get("found"):
        return result.get("error", f"File not found: '{file_path}'")

    return _format_chunks_result(result)


@mcp.tool()
def rag_get_raw_file(
    file_path: str = Field(description="Full absolute path (use 'file_path' value from rag_search results)"),
    collection_name: str = Field(description="Collection name (use rag_stats to see available collections)"),
    line_start: int = Field(default=-1, description="Start line (1-based), -1 for beginning"),
    line_end: int = Field(default=-1, description="End line (inclusive), -1 for end of file"),
) -> str:
    """Get cached raw file content without chunk overlap. Recommended for viewing full source code.
    Supports line_start/line_end for extracting specific line ranges.
    Only available for files imported with raw cache (re-import older files if needed)."""
    result = get_file_chunks(
        file_path, collection_name, 0, 0,
        raw=True, line_start=line_start, line_end=line_end,
    )

    if not result.get("found"):
        return result.get("error", f"File not found: '{file_path}'")

    return _format_raw_result(result)


def _format_raw_result(result):
    """Format raw file result in compact English."""
    ls = result["line_start"]
    le = result["line_end"]
    tl = result["total_lines"]
    shown = le - ls + 1
    range_info = f"line:{ls}-{le}" + (f" ({shown}/{tl} lines)" if shown < tl else " (full)")
    lines = [
        f"raw_file: {result['filename']} | doc_id:{result['doc_id']} | {tl} lines | {result['total_chunks']} chunks",
        f"file_path: {result['source']}",
        f"range: {range_info}",
        "",
        result["content"],
    ]
    if le < tl:
        lines.append(f"\n({tl - le} lines remaining, use line_start={le + 1} to continue)")
    return "\n".join(lines)


def _format_chunks_result(result):
    """Format chunks result in compact English."""
    tc = result["total_chunks"]
    lines = [
        f"file: {result['filename']} | doc_id:{result['doc_id']} | {tc} chunks | ~{result['total_lines']} lines",
        f"file_path: {result['source']}",
        "chunk_ranges: " + " ".join(f"[{s}-{e}]" for s, e in result["chunk_line_ranges"]),
        "",
    ]

    for chunk in result["chunks"]:
        idx = chunk["index"]
        scope = chunk["scope"]
        scope_str = f" scope:{scope}" if scope else ""
        lines.append(f"-- chunk {idx}/{tc} line:{chunk['line_start']}-{chunk['line_end']}{scope_str} --")
        lines.append(chunk["content"])
        lines.append("")

    sc = result["start_chunk"]
    ec = result["end_chunk"]
    if ec < tc:
        lines.append(f"(showing chunk {sc}-{ec - 1}, {ec - sc}/{tc} total. Use start_chunk={ec} for more)")
    else:
        lines.append(f"(all {tc} chunks shown)")

    return "\n".join(lines)


@mcp.tool()
def rag_get_adjacent_chunks(
    doc_id: str = Field(description="Document ID (use 'doc_id' value from rag_search/rag_grep results)"),
    chunk_index: int = Field(description="Target chunk index (0-based, the X from 'chunk:X/Y' in rag_search results)"),
    collection_name: str = Field(description="Collection name (use rag_stats to see available collections)"),
    window: int = Field(default=3, description="Context window: returns chunk_index ± window chunks"),
) -> str:
    """Get adjacent chunks around a specific chunk index, for expanding context of a search result.
    Requires doc_id and chunk_index from rag_search results (not file_path).
    Example: doc_id="abc123", chunk_index=3, window=2 → returns chunks 1-5"""
    result = get_context_chunks(
        doc_id, collection_name,
        chunk_index=chunk_index, window=window,
    )
    return _format_context_result(result, doc_id)


@mcp.tool()
def rag_get_chunks_by_lines(
    doc_id: str = Field(description="Document ID (use 'doc_id' value from rag_search/rag_grep results)"),
    line_start: int = Field(description="Start line number (1-based, from 'line:N-M' in search results)"),
    line_end: int = Field(description="End line number (inclusive, from 'line:N-M' in search results)"),
    collection_name: str = Field(description="Collection name (use rag_stats to see available collections)"),
) -> str:
    """Get all chunks covering a line range, with scope metadata.
    vs rag_get_raw_file: this returns chunks (with scope but has overlap),
    rag_get_raw_file returns raw code (no overlap but no scope).
    Example: doc_id="abc123", line_start=80, line_end=200"""
    result = get_context_chunks(
        doc_id, collection_name,
        line_start=line_start, line_end=line_end,
    )
    return _format_context_result(result, doc_id)


def _format_context_result(result, doc_id):
    """Format context/adjacent chunks result in compact English."""
    if not result.get("found"):
        return result.get("error", f"doc_id '{doc_id}' not found")

    if not result.get("chunks"):
        return result.get("message", "No matching chunks")

    tc = result["total_chunks"]
    lines = [
        f"file: {result.get('filename', '?')} | doc_id:{doc_id} | {tc} chunks",
        f"file_path: {result['source']}",
        "",
    ]

    for chunk in result["chunks"]:
        scope = chunk["scope"]
        scope_str = f" scope:{scope}" if scope else ""
        lines.append(f"-- chunk {chunk['index']}/{tc} line:{chunk['line_start']}-{chunk['line_end']}{scope_str} --")
        lines.append(chunk["content"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def rag_list(
    collection_name: str = Field(description="Collection name (required, use rag_stats to see available collections)"),
) -> str:
    """List all documents in a collection (filename, path, chunk count, doc_id).
    Use returned doc_id with rag_delete to remove documents."""
    docs = list_documents(collection_name)

    if not docs:
        return f"collection '{collection_name}' is empty."

    total_chunks = sum(info["chunk_count"] for info in docs.values())
    lines = [f"[{collection_name}] {len(docs)} docs, {total_chunks} chunks\n"]
    for did, info in docs.items():
        lines.append(f"  {info['filename']} | file_path: {info['source']} | {info['chunk_count']} chunks | doc_id:{did}")

    return "\n".join(lines)


@mcp.tool()
def rag_delete(
    doc_id: str = Field(description="Document ID to delete (use 'doc_id' value from rag_list results)"),
    collection_name: str = Field(description="Collection name (use rag_stats to see available collections)"),
) -> str:
    """Delete a document's vectors and cached files from the collection. Get doc_id from rag_list."""
    deleted, filename = delete_document(doc_id, collection_name)

    if deleted == 0:
        return f"Error: doc_id '{doc_id}' not found. Use rag_list to see available doc_ids."

    return f"Deleted: {filename} | {deleted} chunks | doc_id:{doc_id}"


@mcp.tool()
def rag_stats() -> str:
    """Get RAG overview: all collection names, doc/chunk counts, and config.
    Call this FIRST to discover available collection_name values for other tools.
    Glossary: collection = 知识库, doc = imported file, chunk = vector-embedded text segment."""
    stats = get_stats()

    lines = [
        "RAG Stats",
        f"embed: {stats['embedding_model']} | rerank: {stats['rerank_model']}",
        f"data_dir: {stats['data_dir']}",
        f"chunk: size={DEFAULT_CHUNK_SIZE} overlap={DEFAULT_CHUNK_OVERLAP} | collections: {stats['collection_count']}",
        "",
    ]

    if not stats["collections"]:
        lines.append("(no collections yet, use rag_add_document to import)")
        return "\n".join(lines)

    for name, info in stats["collections"].items():
        if "error" in info:
            lines.append(f"  [{name}] error: {info['error']}")
        elif info["chunk_count"] > 0:
            lines.append(f"  [{name}] {info['doc_count']} docs, {info['chunk_count']} chunks")
        else:
            lines.append(f"  [{name}] empty")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")

`````

--- **end of file: learn_agent/rag/mcp_server.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/RAG_OPTIMIZATION_PLAN.md** (project: learn_agent) --- 

`````markdown
# RAG 优化方案

> 创建时间: 2026-05-22
> 最后更新: 2026-05-22
> 背景: 讨论 funboost `constant.py` 的 `BrokerEnum` 类在 RAG 检索中被切碎导致信息丢失的问题

---

## 一、当前问题

| # | 问题 | 严重程度 | 发现场景 |
|---|------|----------|---------|
| 1 | chunk_size=500 太小，代码类被切成碎片 | 高 | BrokerEnum（8000字符）被切成43块 |
| 2 | chunk 丢失所属 class/function 上下文 | 高 | chunk里的枚举值不知道属于 BrokerEnum |
| 3 | metadata 没有行号范围 | 中 | AI 无法精确引用代码位置 |
| 4 | 没有"按文件获取"检索工具 | 高 | AI 知道文件名但无法获取完整内容 |
| 5 | 没有"相邻 chunk / 上下文扩展"检索工具 | 中 | AI 拿到块 5/43 但无法扩展上下文 |
| 6 | 文件变短后幽灵 chunks 不清理 | 中 | 旧的多余 chunks 污染搜索结果 |
| 7 | 无增量更新，改1行重新 embedding 全文件 | 低 | 大文件全量重建浪费 |

### 核心矛盾

- LangChain `RecursiveCharacterTextSplitter.from_language(Python)` 会优先在 class/def 边界切分
- 但 chunk_size < class 大小时，被迫在 class 内部按空行/换行切
- 切出的子 chunk 完全丢失 class 头部信息
- 按文件后缀动态设置 chunk_size 不可靠（markdown 里经常有代码块）
- LangChain 的 `from_language` 本质是预设文本分隔符（`\nclass `, `\ndef ` 等），不是真正的 AST 解析

---

## 二、优化方案（按优先级）

### P0：最高优先级

#### 1. 统一调大 chunk_size 到 1500

- 改 `chunk_text()` 和 `import_single_file()`/`import_path()`/`batch_import()` 的默认参数
- chunk_overlap 调到 200
- 不按文件类型区分，统一 1500（markdown里经常有代码块，按后缀区分不可靠）
- 效果: BrokerEnum 从43块 → ~6块
- bge-m3 embedding 最佳输入区间: 256-1024 token（约700-3000字符），chunk_size=1500 落在甜点区

#### 2. 头部上下文注入

每个 chunk 前自动注入**绝对路径**和行号:

```
# [File: D:/codes/funboost/funboost/constant.py] [Lines: 60-90]
KAFKA_CONFLUENT = 30
...
```

Python 文件额外注入完整 scope 链 (best effort, AST 解析失败则退回只加文件名):

```
# [File: D:/codes/funboost/funboost/constant.py] [Class: BrokerEnum] [Lines: 60-90]
KAFKA_CONFLUENT = 30
...
```

```
# [File: D:/codes/funboost/funboost/constant.py] [Class: RedisKeys] [Method: gen_funboost_hearbeat_queue__dict_key_by_queue_name] [Lines: 261-262]
return f'{RedisKeys.FUNBOOST_HEARTBEAT_QUEUE__DICT_PREFIX}{queue_name}'
```

**Scope 链处理规则（通用，不只是 class 下的属性）**:
- 模块级代码: `[File: /path/to/xxx.py]`
- 模块级函数: `[File: /path/to/xxx.py] [Function: func_name]`
- 类直接属性: `[File: /path/to/xxx.py] [Class: ClassName]`
- 类的方法: `[File: /path/to/xxx.py] [Class: ClassName] [Method: method_name]`
- 嵌套类/函数: `[File: /path/to/xxx.py] [Class: Outer] [Class: Inner] [Method: method]`

改动点: `chunk_text()` 需要接收 `file_path` 参数, 返回前做 enrich

#### 3. Metadata 增强

```python
metadata = {
    "source": "D:/codes/funboost/funboost/constant.py",  # 绝对路径（已有）
    "filename": "constant.py",                              # 文件名（已有）
    "doc_id": "abc123",
    "chunk_index": 5,
    "total_chunks": 6,
    "line_start": 60,              # 新增
    "line_end": 90,                # 新增
    "scope": "BrokerEnum",         # 新增 (Python only, best effort)
    # scope 示例: "BrokerEnum" / "RedisKeys.gen_xxx" / "" (模块级)
}
```

改动点: `import_single_file()` 中计算行号和 scope 并存入 metadata

搜索结果显示格式调整:
```
── 结果 1/5 (来源: D:/codes/funboost/funboost/constant.py, 块 5/6, 行 60-90, 距离: 0.3210) ──
```

---

### P1：高优先级（新检索工具）

#### 4. 新增 `rag_get_file_chunks` 工具（带概要 + 分页）

AI 知道文件名后，先看文件概要，再按需获取指定范围的 chunks:

```python
@mcp.tool()
def rag_get_file_chunks(
    filename: str,          # 文件名或相对路径关键词
    collection_name: str = "default",
    start_chunk: int = 0,   # 从第几块开始返回
    max_chunks: int = 5,    # 最多返回几块
) -> str:
    """按文件名获取知识库中该文件的内容块。
    
    总是返回文件概要（总行数/总大小/总块数/各块行号范围），
    加上 start_chunk 起的 max_chunks 块内容。
    适用于大文件（上千行）的渐进式浏览。
    """
```

返回格式示例:
```
📄 文件概要: D:/codes/funboost/funboost/constant.py
  总块数: 6  |  约总行数: 323  |  约大小: 12KB
  各块行号: [1-55] [55-110] [110-165] [165-220] [220-275] [275-323]

── 块 0/6 (行 1-55) ──
class BrokerEnum:
    """在funboost中万物皆可为消息队列broker..."""
    ...

── 块 1/6 (行 55-110) ──
...

（显示块 0-4，共 5/6 块）
提示: 还有 1 块未显示，可用 start_chunk=5 获取
```

#### 5. 新增 `rag_get_context` 工具（合并相邻 + 行号两种模式）

支持按 chunk_index 或按行号范围获取上下文:

```python
@mcp.tool()
def rag_get_context(
    doc_id: str,
    collection_name: str = "default",
    # 模式A: 按 chunk 索引取相邻块
    chunk_index: int = None,
    window: int = 2,            # 前后各取几块
    # 模式B: 按行号范围取
    line_start: int = None,
    line_end: int = None,
) -> str:
    """获取指定文档的上下文内容。

    两种用法:
    1. 按 chunk 索引: 传 chunk_index + window，返回相邻块
       示例: rag_get_context(doc_id="abc123", chunk_index=3, window=2) → 块 1-5
    2. 按行号范围: 传 line_start + line_end，返回覆盖该行号范围的所有块
       示例: rag_get_context(doc_id="abc123", line_start=80, line_end=200)
    """
```

#### 6. `rag_search` 增加 metadata 过滤（和 P1 一起做）

```python
@mcp.tool()
def rag_search(
    query: str,
    collection_name: str = "default",
    top_k: int = 5,
    use_rerank: bool = True,
    filter_filename: str = None,  # 新增: 限定在某个文件中搜索
) -> str:
    """语义搜索，可选限定文件范围。"""
```

---

### P2：中优先级

#### 7. 修复幽灵 chunks bug

`import_single_file` 中 upsert 前先删除该 doc_id 的旧 chunks:

```python
old_data = col.get(where={"doc_id": doc_id}, include=[])
if old_data["ids"]:
    col.delete(ids=old_data["ids"])
col.upsert(...)
```

#### 8. Python AST scope 链解析（通用逻辑）

用 `ast` 模块为 Python 代码的每个 chunk 自动识别完整 scope 链:

```python
def get_scope_chain_at_line(full_text, line_number):
    """给定行号，返回完整 scope 链字符串。
    
    示例:
    - "BrokerEnum"                                    (class 下的属性)
    - "RedisKeys.gen_funboost_hearbeat_queue__dict_key"  (class 的方法)
    - "some_utility"                                  (模块级函数)
    - "Outer.Inner.method"                            (嵌套)
    - ""                                               (模块级代码)
    """
    tree = ast.parse(full_text)
    # 遍历 AST 节点，找包含该行号的最内层 scope
    # 递归处理 ClassDef/FunctionDef/AsyncFunctionDef
    ...
```

注意:
- AST 解析失败（语法错误文件）时静默退回，不影响导入流程
- `ast.get_source_segment()` 需要 Python 3.8+，需检查兼容性
- 对非 Python 文件不做 scope 解析，只注入文件名和行号

---

### P3：低优先级（以后按需实现）

#### 9. 文件级 hash 增量导入

- metadata 增加 `content_hash: md5(file_content)`
- 导入时先比对 hash，内容未变则跳过
- 减少不必要的 embedding API 调用

---

## 三、改动文件范围

| 文件 | 改动 |
|------|------|
| `rag/core.py` | P0: chunk_size默认值、头部注入（绝对路径+行号+scope）、行号计算 |
| `rag/core.py` | P2: 幽灵清理、AST scope链解析 |
| `rag/core.py` | P3: 文件hash增量 |
| `rag/mcp_server.py` | P0: 搜索结果显示绝对路径和行号 |
| `rag/mcp_server.py` | P1: 新增 rag_get_file_chunks(带概要+分页)、rag_get_context(chunk索引+行号两种模式)、rag_search加filter_filename |
| `config.jsonc` | 可选: rag配置增加 default_chunk_size |

## 四、预期效果

| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| constant.py chunk数 | 43块 | ~6块 |
| BrokerEnum 单次搜索覆盖率 | ~15% | ~50-80% |
| AI 需要搜索次数 | 5-7次 | 1-2次 |
| chunk 上下文完整性 | 无 | 有绝对路径+行号+scope链 |
| 大文件浏览 | 无法浏览 | 文件概要+分页获取 |
| 幽灵数据 | 有 | 无 |

## 五、实施顺序

```
第一批 (P0): 调大 chunk_size + 头部注入 + 行号/scope metadata
    ↓
重新导入知识库 (delete_first=True)
    ↓
第二批 (P1): 新增 rag_get_file_chunks + rag_get_context + rag_search filter
    ↓
测试验证效果
    ↓
第三批 (P2): 幽灵清理 + AST scope链完善
    ↓
第四批 (P3): 增量导入 (按需)
```

## 六、导入策略

不再导入 `funboost_all_docs_and_codes.md`（3MB合并文件），改为:

```python
# funboost 源码 (每个py文件独立doc_id，改了只需重新导入那一个)
"D:/codes/funboost/funboost"
"D:/codes/funboost/test_frame"  
"D:/codes/funboost/tests"

# funboost 教程文档 (每个md独立，单个不超过200KB)
"D:/codes/funboost_docs/source/articles/c0.md"
"D:/codes/funboost_docs/source/articles/c1.md"
"D:/codes/funboost_docs/source/articles/c2.md"
"D:/codes/funboost_docs/source/articles/c3.md"
"D:/codes/funboost_docs/source/articles/c4.md"
"D:/codes/funboost_docs/source/articles/c4b.md"
"D:/codes/funboost_docs/source/articles/c6.md"
"D:/codes/funboost_docs/source/articles/c7.md"
"D:/codes/funboost_docs/source/articles/c8.md"
"D:/codes/funboost_docs/source/articles/c9.md"
"D:/codes/funboost_docs/source/articles/c10.md"
"D:/codes/funboost_docs/source/articles/c11.md"
"D:/codes/funboost_docs/source/articles/c12.md"
"D:/codes/funboost_docs/source/articles/c13.md"
"D:/codes/funboost_docs/source/articles/c14.md"
"D:/codes/funboost_docs/source/articles/c15.md"
"D:/codes/funboost_docs/source/articles/c20.md"
```

## 七、关键技术点备忘

- bge-m3 最大输入 8192 token，最佳效果区间 256-1024 token（约700-3000字符）
- ChromaDB 混合存储: SQLite 存原文+metadata，UUID文件夹存 HNSW 向量索引
- ChromaDB `delete_collection()` 同时清除 SQLite 和 HNSW 文件
- 改 chunk_size 后必须 `delete_first=True` 重建知识库，否则新旧 chunks 混杂
- `ast.get_source_segment()` 需要 Python 3.8+
- 当前项目要兼容 Python 3.7+，AST 相关功能需要版本检查

`````

--- **end of file: learn_agent/rag/RAG_OPTIMIZATION_PLAN.md** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/readme.md** (project: learn_agent) --- 

`````markdown
# RAG 知识库模块

## 架构：Agentic RAG vs Naive RAG

本项目采用 **Agentic RAG** 架构——AI Agent 自主决定是否检索、检索什么、检索几次。
与传统 Naive RAG 有本质区别。

### 对比总览

| 维度 | Naive RAG | Agentic RAG（本项目） |
|------|-----------|----------------------|
| **检索决策** | 每次提问都检索（代码写死） | AI 自主判断是否需要检索 |
| **检索轮数** | 1 轮 | AI 决定（0~N 轮） |
| **搜索词** | 直接用用户原话做 query | AI 自己构造精准关键词 |
| **多轮追问** | 不支持，每轮孤立 | 自然多轮，上下文保留在 tool 消息中 |
| **检索结果存放** | 拼入 user 或 system 消息 | 以 tool 角色存入对话历史 |
| **上下文连贯性** | 每轮丢弃上一轮检索结果 | 完整对话历史（含所有 tool 结果） |
| **无关问题** | 照样检索（"你好"也搜知识库） | AI 判断不需要 → 不调工具 |
| **深度分析能力** | 一次搜 5 条就得出结论 | 搜→理解→发现缺口→再搜，循环深入 |

### 实测对比（funboost 代码调用链路分析）

同一个问题："分析这段 funboost 代码的调用链路，画出链路图"

| | Naive RAG | Agentic RAG | Serena MCP |
|---|---|---|---|
| 检索次数 | 1 次 | 10 次搜索 + 5 次读文件 | 31 次符号查找 |
| 耗时 | ~10 秒 | ~85 秒 | ~160 秒 |
| 回答深度 | 浅层（"boost 是装饰器"） | 5 阶段完整链路图 | 6 阶段完整链路图 |
| 涉及文件 | 1-2 个 chunk | 6+ 个文件的完整源码 | 6+ 个文件的精确符号 |

Naive RAG 只有 1 次检索机会，搜到的 5 个 chunk 不可能覆盖跨 6 个文件的完整调用链。
Agentic RAG 通过多轮自主检索逐步补全知识缺口，最终拼出完整链路。

### 核心流程

```
用户提问
    │
    ▼
LLM 判断: 需要搜知识库吗？
    │
    ├── 不需要 → 直接回答
    │
    └── 需要 → 调用 rag_search("关键词")
              │
              ▼
        看到搜索结果，发现还需要更多信息
              │
              ├── rag_search("另一个关键词")
              ├── rag_get_raw_file("某文件")
              ├── rag_get_adjacent_chunks(...)
              │
              ▼
        信息足够 → 综合所有检索结果 → 生成回答
```

Naive RAG 只有最上面一条直线：`用户提问 → 搜索 → 拼接 → 回答`。

---

## 技术实现

### 存储架构

```
learn_agent/data/rag_db/
├── chroma.sqlite3                    # ChromaDB（chunks + metadata）
├── {uuid}/                           # HNSW 向量索引（二进制）
│   ├── data_level0.bin
│   ├── header.bin
│   └── ...
└── raw_files/                        # 原始文件快照缓存
    └── {collection_name}/
        ├── {doc_id}.py               # 导入时的文件快照
        └── ...
```

### 双存储设计

| 存储 | 内容 | 用途 |
|------|------|------|
| **ChromaDB** | 切分后的 chunks（带 overlap + 头部注入） | 语义搜索 |
| **raw_files/** | 导入时的完整原始文件 | 无 overlap 的完整代码查看 |

### Chunk 增强（Contextual Embedding）

每个 chunk 在 embedding 前注入上下文头部：

```
# [File: D:\codes\funboost\funboost\core\booster.py] [Scope: Booster.__call__] [Lines: 117-220]
def __call__(self, *args, **kwargs):
    ...实际代码内容...
```

增强信息来源：
- **文件路径**：绝对路径
- **行号范围**：通过 `str.find()` + `bisect` 定位
- **AST Scope**：Python 文件用 `ast.parse()` 解析 class/function 嵌套关系

### Chunk Metadata（自定义 ChromaDB 元数据）

| 字段 | 说明 | 示例 |
|------|------|------|
| `doc_id` | 文件标识（MD5(路径)[:12]） | `0a2e27f4aa6a` |
| `source` | 原始文件绝对路径 | `D:\codes\funboost\...` |
| `filename` | 文件名 | `booster.py` |
| `chunk_index` | 块序号（0-based） | `3` |
| `total_chunks` | 该文件总块数 | `15` |
| `line_start` | 起始行号 | `117` |
| `line_end` | 结束行号 | `220` |
| `scope` | AST scope 链 | `Booster.__call__` |

这些 metadata 不是 ChromaDB 原生字段，而是自定义的。
99% 的 RAG 教程不会教 metadata 设计——这是从"能跑"到"好用"的分水岭。

### 检索管线

```
语义搜索:  query → embed → ChromaDB 向量检索（top_k × 4）
              ↓
Rerank:    SiliconFlow bge-reranker-v2-m3 精排 → top_k 结果
              ↓
返回:      chunk 内容 + 来源路径 + 行号 + scope + doc_id
```

### 技术栈

| 组件 | 选型 |
|------|------|
| Embedding | SiliconFlow BAAI/bge-m3（1024 维，中文最强之一，免费） |
| Rerank | SiliconFlow BAAI/bge-reranker-v2-m3（免费） |
| 向量数据库 | ChromaDB 本地持久化（SQLite + HNSW） |
| 分块 | LangChain RecursiveCharacterTextSplitter（语言感知） |
| MCP | FastMCP（9 个工具，stdio 传输） |

### 分块参数

| 参数 | 值 | 说明 |
|------|-----|------|
| `chunk_size` | 1500 | 每块最大字符数 |
| `chunk_overlap` | 200 | 相邻块重叠字符数 |

---

## MCP 工具清单（9 个）

### 导入与管理

| 工具 | 功能 |
|------|------|
| `rag_add_document` | 导入文件或目录到知识库 |
| `rag_list` | 列出已导入的文档 |
| `rag_delete` | 删除指定文档及缓存 |
| `rag_stats` | 知识库统计信息 |

### 检索与浏览

| 工具 | 功能 |
|------|------|
| `rag_search` | 语义搜索（向量 + Rerank） |
| `rag_get_file_chunks` | 按文件分页浏览 chunks |
| `rag_get_raw_file` | 获取原始文件内容（无 overlap） |
| `rag_get_adjacent_chunks` | 按 chunk 索引获取相邻块 |
| `rag_get_chunks_by_lines` | 按行号范围获取 chunks |

### 工具设计原则

1. **职责单一**：每个工具只做一件事，参数最少化，减少 AI 幻觉
2. **互相引导**：每个工具的 docstring 说明何时应该用其他工具
3. **参数来源明确**：描述中标注参数从哪里获取（如"从 rag_search 的'来源'字段获取"）

---

## 文件结构

```
learn_agent/rag/
├── __init__.py          # 导出核心接口
├── core.py              # 核心逻辑（embed/search/import/CRUD）
├── chunker.py           # 分块增强（切分、行号、AST scope、头部注入）
├── mcp_server.py        # MCP 工具层（9 个工具，薄包装）
├── import_funboost.py   # 独立 CLI 脚本（绕过 TUI/MCP 直接导入）
└── README.md            # 本文件
```

## 使用方式

```python
# 方式 1: 在 TUI 中让 AI 调用 MCP 工具
#   "帮我把 D:/codes/funboost 导入到 funboost 知识库"
#   "funboost 的 boost 装饰器是怎么工作的？"

# 方式 2: 独立脚本导入
#   python learn_agent/rag/import_funboost.py

# 方式 3: 代码中直接调用
from learn_agent.rag.core import import_path, search
results, errors = import_path("D:/my_project/src", "my_project")
hits = search("某个关键词", collection_name="my_project")
```

`````

--- **end of file: learn_agent/rag/readme.md** (project: learn_agent) --- 

---


--- **start of file: learn_agent/rag/__init__.py** (project: learn_agent) --- 

`````python
"""
RAG 知识库模块 —— 供 MCP 服务和独立脚本共同复用。

用法:
    from learn_agent.rag.core import import_path, search, delete_collection

    results, errors = import_path("D:/my_project/src", "my_project")
    docs, metas, dists, reranked, total = search("如何使用?", "my_project")
"""

from .chunker import (
    chunk_text,
    enrich_chunks,
    compute_line_ranges,
    get_python_scope_at_line,
    collect_files,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_CHUNK_OVERLAP,
    TEXT_EXTENSIONS,
)

from .core import (
    batch_import,
    import_path,
    import_single_file,
    search,
    get_file_chunks,
    get_context_chunks,
    list_documents,
    list_collections,
    delete_document,
    delete_collection,
    get_collection,
    get_stats,
    embed,
    rerank,
    EMBEDDING_MODEL,
    RERANK_MODEL,
    DATA_DIR,
)

__all__ = [
    # chunker
    "chunk_text",
    "enrich_chunks",
    "compute_line_ranges",
    "get_python_scope_at_line",
    "collect_files",
    "DEFAULT_CHUNK_SIZE",
    "DEFAULT_CHUNK_OVERLAP",
    "TEXT_EXTENSIONS",
    # core
    "batch_import",
    "import_path",
    "import_single_file",
    "search",
    "get_file_chunks",
    "get_context_chunks",
    "list_documents",
    "list_collections",
    "delete_document",
    "delete_collection",
    "get_collection",
    "get_stats",
    "embed",
    "rerank",
    "EMBEDDING_MODEL",
    "RERANK_MODEL",
    "DATA_DIR",
]

`````

--- **end of file: learn_agent/rag/__init__.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/tools/base.py** (project: learn_agent) --- 

`````python
"""
工具注册框架 —— 基于 Pydantic + 装饰器自动生成 OpenAI Function Calling Schema

用法：
    from pydantic import BaseModel, Field
    from tools.base import tool

    class MyParams(BaseModel):
        name: str = Field(description="用户名")
        age: int = Field(default=0, description="年龄，可选")

    @tool
    def greet(params: MyParams) -> str:
        \"\"\"向用户打招呼\"\"\"
        return f"你好, {params.name}!"

自动生成等价的 OpenAI function schema，无需手写 JSON。
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


def tool(func: Callable) -> Callable:
    """装饰器：自动注册工具函数

    要求：
    1. 函数必须有一个 Pydantic BaseModel 类型的参数
    2. 函数必须有 docstring（作为工具描述）
    3. BaseModel 的 Field 必须有 description（作为参数描述）
    """
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
    tool_name = func.__name__

    TOOL_REGISTRY[tool_name] = {
        "function": func,
        "model_cls": model_cls,
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

`````

--- **end of file: learn_agent/tools/base.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/tools/builtin.py** (project: learn_agent) --- 

`````python
"""
内置工具 —— 使用 Pydantic + @tool 装饰器自动注册
"""

import datetime

from pydantic import BaseModel, Field

from .base import tool

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo


class GetCurrentTimeParams(BaseModel):
    timezone: str = Field(default="Asia/Shanghai", description="时区，默认 Asia/Shanghai")


@tool
def get_current_time(params: GetCurrentTimeParams) -> str:
    """获取当前日期和时间"""
    try:
        tz = ZoneInfo(params.timezone)
    except (KeyError, Exception):
        tz = ZoneInfo("Asia/Shanghai")
    now = datetime.datetime.now(tz)
    return now.strftime(f"%Y-%m-%d %H:%M:%S ({now.strftime('%A')}) [{params.timezone}]")


class CalculateParams(BaseModel):
    expression: str = Field(description="数学表达式，如 '2+3*4' 或 '(100-20)/8'")


@tool
def calculate(params: CalculateParams) -> str:
    """计算数学表达式（支持加减乘除、幂运算、取余等）"""
    import ast
    import operator

    _ops = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod,
        ast.Pow: operator.pow, ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def _safe_eval(node):
        if isinstance(node, ast.Expression):
            return _safe_eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _ops:
            left = _safe_eval(node.left)
            right = _safe_eval(node.right)
            if isinstance(node.op, ast.Pow) and right > 1000:
                raise ValueError("指数过大")
            return _ops[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ops:
            return _ops[type(node.op)](_safe_eval(node.operand))
        raise ValueError(f"不支持的表达式: {ast.dump(node)}")

    try:
        tree = ast.parse(params.expression.strip(), mode='eval')
        result = _safe_eval(tree)
        return str(result)
    except ZeroDivisionError:
        return "计算错误: 除以零"
    except Exception as e:
        return f"计算错误: {e}"

`````

--- **end of file: learn_agent/tools/builtin.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/tools/extra_serena_tools.py** (project: learn_agent) --- 

`````python
"""
Serena 相关工具 —— 使用 Pydantic + @tool 装饰器自动注册
"""

import asyncio
import os
from typing import List, Optional

from pydantic import BaseModel, Field

from .base import tool


class SerenaIndexParams(BaseModel):
    project_path: str = Field(description="项目根目录的绝对路径，如 'D:/codes/funboost'")
    languages: Optional[List[str]] = Field(
        default=None,
        description="要索引的编程语言列表，如 ['python', 'markdown']。为空则使用项目已有配置。",
    )


def _ensure_languages(project_path: str, languages: List[str]) -> str:
    """确保 project.yml 中包含指定的 languages，返回操作日志"""
    yml_path = os.path.join(project_path, ".serena", "project.yml")
    if not os.path.exists(yml_path):
        return f"project.yml 不存在: {yml_path}，Serena 将在索引时自动创建"

    with open(yml_path, "r", encoding="utf-8") as f:
        content = f.read()

    import re
    match = re.search(r"^languages:\s*\n((?:\s*-\s*.+\n)*)", content, re.MULTILINE)
    if not match:
        return "未找到 languages 配置块，跳过自动修改"

    existing = re.findall(r"-\s*(\S+)", match.group(1))
    missing = [lang for lang in languages if lang not in existing]
    if not missing:
        return f"languages 已包含 {languages}，无需修改"

    new_langs = existing + missing
    lang_block = "languages:\n" + "".join(f"- {lang}\n" for lang in new_langs)
    new_content = content[:match.start()] + lang_block + content[match.end():]

    with open(yml_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return f"已更新 project.yml: {existing} → {new_langs}"


@tool
async def serena_index_project(params: SerenaIndexParams) -> str:
    """为指定项目创建 Serena 语义索引（Python/Markdown 符号），索引后可按符号名精确查找代码。可通过 languages 参数自动配置要索引的语言。"""
    if not os.path.isdir(params.project_path):
        return f"错误: 目录不存在 '{params.project_path}'"

    log_parts = []

    if params.languages:
        yml_log = _ensure_languages(params.project_path, params.languages)
        log_parts.append(yml_log)

    proc = await asyncio.create_subprocess_exec(
        "serena", "project", "index", params.project_path, "--log-level", "INFO",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )
    stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=120)
    output = stdout.decode("utf-8", errors="replace") if stdout else ""
    keywords = ("Indexed", "language", "error", "Error", "complete")
    lines = [l for l in output.splitlines() if any(k in l for k in keywords)]
    summary = "\n".join(lines[-20:]) if lines else output[-500:]
    log_parts.append(f"索引完成 (exit={proc.returncode})\n{summary}")

    return "\n".join(log_parts)

`````

--- **end of file: learn_agent/tools/extra_serena_tools.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/tools/__init__.py** (project: learn_agent) --- 

`````python
"""
工具模块 —— 导入所有工具文件以触发 @tool 注册，然后导出 TOOL_REGISTRY
"""

from .base import TOOL_REGISTRY, tool  # noqa: F401

import tools.builtin  # noqa: F401
import tools.extra_serena_tools  # noqa: F401

`````

--- **end of file: learn_agent/tools/__init__.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/ui/app.py** (project: learn_agent) --- 

`````python
"""
TUI 界面 —— 用 Textual 框架构建

布局:
┌─────────────────────────────────────────────────┐
│  Learn Agent | deepseek-v4-flash | Tokens: 0    │  ← Header
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
import json
import os
import sys
import time
from typing import Optional

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (
    Footer,
    Header,
    OptionList,
    RichLog,
    Static,
    TextArea,
    Input,
)
from textual.widgets.option_list import Option
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.command import Hit, Hits, Provider, DiscoveryHit
from textual.events import Key
from rich.text import Text
from rich.markdown import Markdown as RichMarkdown
from rich.panel import Panel
from rich.box import ROUNDED

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent.core import AgentCore


_SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
_SPINNER_BIG = ["◐", "◓", "◑", "◒"]
_MARQUEE_BASE = "  ◐  AI 正在回答中，请稍候...  按 Ctrl+K 停止  ✦  "
_RAINBOW_COLORS = [
    "#ff0080", "#ff2060", "#ff4040", "#ff6020",
    "#ff8000", "#ffb000", "#ffff00", "#80ff00",
    "#00ff80", "#00ffff", "#0080ff", "#4040ff",
    "#8000ff", "#c000ff", "#ff00ff", "#ff0080",
]


def _fmt_tokens(n: int) -> str:
    """将 token 数格式化为可读字符串：如 1234 → 1.2k"""
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


class ChatInput(TextArea):
    """聊天输入框：Enter=换行，Ctrl+Enter(ctrl+j)=发送"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_line_numbers = False


class ClickableStatic(Static):
    """可点击的 Static 组件 — 点击时打开工具详情"""

    def on_click(self, event):
        app = self.app
        if hasattr(app, '_show_tool_details'):
            app._show_tool_details()


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
        yield ClickableStatic("", id="section-tools-title")
        with VerticalScroll(id="section-tools-scroll"):
            yield ClickableStatic("", id="section-tools")

    def on_mount(self):
        self.update_content()

    def update_content(self, last_elapsed: float = 0.0):
        t = self.agent.get_token_usage()
        if t['total'] == 0:
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
            for s in mcp_status:
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

        tools = self.agent.get_tools()
        self.query_one("#section-tools-title", Static).update(
            f"[bold #6bcb77]工具 ({len(tools)})[/bold #6bcb77] [dim #6b7394]点击查看详情[/dim #6b7394]"
        )
        tool_lines = []
        for t in tools:
            source = t.get("source", "")
            if source.startswith("MCP:"):
                icon = "[#b39ddb]◆[/#b39ddb]"
            else:
                icon = "[#6bcb77]●[/#6bcb77]"
            tool_lines.append(f"  {icon} [#c0c0c0]{t['name']}[/#c0c0c0]")
        self.query_one("#section-tools", Static).update("\n".join(tool_lines))

    def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        """处理模型点击切换 或 MCP 点击切换"""
        if not event.option.id:
            return
        opt_id = event.option.id

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
        lines.append("[bold #00d4aa]═══ Learn Agent 帮助 ═══[/bold #00d4aa]\n")

        lines.append("[bold #ffd93d]⌨ 快捷键[/bold #ffd93d]")
        keys = [
            ("Ctrl+J", "发送消息"),
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
        lines.append("[bold #6bcb77]💡 提示[/bold #6bcb77]")
        lines.append("  [#c0c0c0]• 右侧面板可直接点击模型名称切换[/#c0c0c0]")
        lines.append("  [#c0c0c0]• MCP 工具在后台自动连接[/#c0c0c0]")
        lines.append("  [#c0c0c0]• 对话超长时自动截断早期消息[/#c0c0c0]")
        lines.append("  [#c0c0c0]• Alt+Shift+鼠标拖选 = 矩形区域选择[/#c0c0c0]")

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
        lines = [f"[bold #6bcb77]工具详情 ({len(tools)})[/bold #6bcb77]\n"]
        for t in tools:
            source = t.get("source", "")
            if source.startswith("MCP:"):
                icon = "[#b39ddb]◆[/#b39ddb]"
                src_label = f"[#b39ddb]{source}[/#b39ddb]"
            else:
                icon = "[#6bcb77]●[/#6bcb77]"
                src_label = f"[#6bcb77]{source}[/#6bcb77]"
            lines.append(f"{icon} [bold #c0c0c0]{t['name']}[/bold #c0c0c0]  {src_label}")
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
        """Input 组件的 Enter 提交事件"""
        self._do_confirm(event.value)

    def action_confirm(self):
        """Binding 回调（备用）"""
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


class AgentCommands(Provider):
    """命令面板: 提供会话管理、导出、设置等操作"""

    async def discover(self) -> Hits:
        """默认展示所有命令（不与底部状态栏重复）"""
        app = self.app
        assert isinstance(app, AgentApp)

        commands = [
            ("编辑上轮提问", "撤回最后一轮对话，重新编辑发送", app._edit_last_message),
            ("切换思考显示", "显示或隐藏 AI 的思考过程", app._cmd_toggle_thinking),
            ("查看工具详情", "查看所有工具的完整描述", app._show_tool_details),
            ("复制为 Markdown", "复制对话为 Markdown 到剪贴板", app._cmd_copy_markdown),
            ("导出 Markdown 文件", "将对话导出为 .md 文件", app._cmd_export_markdown),
        ]
        for name, help_text, callback in commands:
            yield DiscoveryHit(name, callback, help=help_text)

    async def search(self, query: str) -> Hits:
        """搜索命令"""
        matcher = self.matcher(query)
        app = self.app
        assert isinstance(app, AgentApp)

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


class AgentApp(App):
    """Learn Agent TUI 主应用"""

    TITLE = "Learn Agent"
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
        Binding("ctrl+q", "quit", "退出", show=True, priority=True),
    ]

    def __init__(self, config: dict):
        super().__init__()
        self.agent = AgentCore(config)
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

    async def _request_tool_approval(self, tool_name: str, tool_args: dict) -> bool:
        """弹出确认弹窗，等待用户按 Enter/Esc，返回是否同意"""
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
        chat = self.query_one("#chat-panel", RichLog)
        model = self.agent.get_model_name()
        total = len(self.agent.available_models)
        chat.write(f"[bold #00d4aa]Learn Agent[/bold #00d4aa] | 模型: [bold #4d96ff]{model}[/bold #4d96ff] | 共 [#ffd93d]{total}[/#ffd93d] 个可用模型")
        chat.write("[#6b7394]Enter=换行 | Ctrl+Enter=发送 | Tab=切换模型 | Ctrl+P=命令面板 | F1=帮助[/#6b7394]\n")
        self._update_subtitle()
        self.query_one("#user-input", ChatInput).focus()

        mcp_config = self.config.get("mcp", {})
        enabled_count = sum(1 for v in mcp_config.values() if v.get("enabled", True))
        if enabled_count > 0:
            chat.write(f"[#ff922b]⟳ {enabled_count} 个 MCP Server 后台连接中...[/#ff922b]")
            self.run_worker(self._connect_mcp_background(), exclusive=False)

    async def _connect_mcp_background(self):
        """后台连接 MCP Server，连接完成后更新 UI"""
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
        tool_panel = self.query_one("#tool-panel", ToolPanel)
        tool_panel.update_content()

    def _update_subtitle(self):
        title = self.agent.session_store.get_session_title(self.agent.session_id)
        if title and title != "新会话":
            self.sub_title = title
            self._set_terminal_title(f"Learn Agent - {title}")
        else:
            self.sub_title = ""
            self._set_terminal_title("Learn Agent")

    @staticmethod
    def _set_terminal_title(title: str):
        """通过 ANSI 转义序列设置终端窗口标题（cmd/PowerShell/Windows Terminal 等）"""
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

    def _start_thinking_animation(self) -> None:
        """启动底部跑马灯动画"""
        self._spinner_idx = 0
        self._marquee_pos = 0
        if self._spinner_timer is not None:
            self._spinner_timer.stop()
        self._spinner_timer = self.set_interval(0.12, self._tick_spinner)

    def _stop_thinking_animation(self) -> None:
        """停止跑马灯并清空状态栏"""
        if self._spinner_timer is not None:
            self._spinner_timer.stop()
            self._spinner_timer = None
        try:
            self.query_one("#ai-status-bar", Static).update("")
            self.query_one("#ai-timer", Static).update("")
        except Exception:
            pass

    def _tick_spinner(self) -> None:
        """每帧更新：左侧彩虹跑马灯 + 右侧固定计时器（两个独立控件）"""
        if not self._sending:
            self._stop_thinking_animation()
            return

        # --- 左侧跑马灯 ---
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

        # --- 右侧固定计时器（spinner + 脉冲色彩）---
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

    async def _do_send(self, user_text: str):
        """后台任务：执行 LLM 调用，不阻塞 UI 事件循环"""
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

        use_stream = self.config.get("agent", {}).get("streaming", True)

        if use_stream:
            await self._handle_stream(user_text, chat)
        else:
            await self._handle_non_stream(user_text, chat)

        self._stop_thinking_animation()
        tool_panel = self.query_one("#tool-panel", ToolPanel)
        tool_panel.update_content(last_elapsed=self._last_elapsed)
        self._sending = False
        self.query_one("#user-input", ChatInput).focus()

        if is_first_msg:
            self._update_subtitle()
            self.run_worker(self._generate_title(), exclusive=False)

    async def _generate_title(self):
        """后台异步生成会话标题"""
        try:
            await self.agent.generate_smart_title()
            self._update_subtitle()
        except Exception:
            pass

    def _is_at_bottom(self, chat: RichLog) -> bool:
        """检查用户是否在聊天区底部（允许 2 行误差）"""
        return chat.scroll_y >= chat.max_scroll_y - 2

    def _smart_scroll(self, chat: RichLog):
        """智能滚动：仅在用户在底部时自动跟随"""
        if self._is_at_bottom(chat):
            chat.scroll_end(animate=False)

    async def _handle_stream(self, user_text: str, chat: RichLog):
        """流式输出：逐行显示 AI 回复，思考内容用特殊颜色"""
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
        tc_str = f" | 工具{t['last_tool_calls']}次" if t['last_tool_calls'] > 0 else ""
        chat.write(f"[#6b7394](本次 入{_fmt_tokens(t['last_prompt'])}+出{_fmt_tokens(t['last_completion'])}={_fmt_tokens(t['last_total'])} | 耗时{elapsed:.1f}s{tc_str} | 累计 {_fmt_tokens(t['total'])})[/#6b7394]")
        chat.auto_scroll = True
        chat.scroll_end(animate=False)

    async def _handle_non_stream(self, user_text: str, chat: RichLog):
        """非流式输出：一次性显示（包含思考和工具调用过程）"""
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
        tc_str = f" | 工具{t['last_tool_calls']}次" if t['last_tool_calls'] > 0 else ""
        chat.write(f"[#6b7394](本次 入{_fmt_tokens(t['last_prompt'])}+出{_fmt_tokens(t['last_completion'])}={_fmt_tokens(t['last_total'])} | 耗时{elapsed:.1f}s{tc_str} | 累计 {_fmt_tokens(t['total'])})[/#6b7394]")

    def action_stop_ai(self):
        """Esc: 弹窗打开时关闭弹窗，否则终止 AI 回答"""
        if isinstance(self.screen, ModalScreen):
            self.screen.dismiss()
            return
        if self._sending:
            self._cancel_requested = True
            self.notify("正在终止 AI 回答...", timeout=2)

    def action_edit_last(self):
        """Ctrl+↑: 编辑上一轮提问"""
        self._edit_last_message()

    async def action_send_msg(self):
        """Ctrl+Enter 发送消息"""
        if self._sending:
            return
        input_widget = self.query_one("#user-input", ChatInput)
        user_text = input_widget.text.strip()
        if not user_text:
            return
        input_widget.clear()
        self._sending = True
        self.run_worker(self._do_send(user_text), exclusive=False)

    def _cmd_new_session(self):
        """命令面板: 新建会话"""
        chat = self.query_one("#chat-panel", RichLog)
        self.agent.clear_history()
        chat.clear()
        chat.write("[#6b7394]✦ 新会话已创建，上下文已重置[/#6b7394]\n")
        self.query_one("#tool-panel", ToolPanel).update_content()
        self._update_subtitle()

    def _cmd_toggle_thinking(self):
        """命令面板: 切换思考显示（切换后立即重绘聊天区）"""
        self._show_thinking = not self._show_thinking
        state = "显示" if self._show_thinking else "隐藏"
        self._redraw_chat()
        self.notify(f"思考过程已{state}", timeout=2)

    def _cmd_export_markdown(self):
        """命令面板: 导出 Markdown（先弹窗让用户选择轮次）"""
        self.push_screen(RoundsInputScreen("导出 Markdown 文件"), self._on_export_rounds)

    def _on_export_rounds(self, rounds):
        """轮次选择回调：导出 Markdown"""
        if rounds is None or rounds < 0:
            return
        self._export_markdown(rounds)

    async def _cmd_resume_session(self, session_id: str, title: str):
        """命令面板: 恢复指定会话"""
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

    def _export_markdown(self, rounds: int = 0):
        """导出对话为 Markdown，rounds=0 表示全部"""
        import os
        import re
        from datetime import datetime

        messages = self._get_round_messages(rounds)
        session_title = self.agent.session_store.get_session_title(
            self.agent.session_id
        ) or ""
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

        save_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
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
        """复制对话为 Markdown 到剪贴板，rounds=0 表示全部"""
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

    def _get_round_messages(self, rounds: int = 0) -> list:
        """获取最近 N 轮对话的消息列表，rounds=0 返回全部

        "一轮" 定义：一条 user 消息 + 其后连续的 assistant/tool 消息
        """
        messages = self.agent.messages
        if rounds <= 0:
            return messages

        # 从后往前数 user 消息，定位到第 N 轮的起始位置
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

        # 保留 system 消息 + 从 start_idx 开始的消息
        result = [m for m in messages if m.get("role") == "system"]
        result.extend(m for i, m in enumerate(messages) if m.get("role") != "system" and i >= start_idx)
        return result

    def _cmd_copy_markdown(self):
        """命令面板: 复制为 Markdown（先弹窗让用户选择轮次）"""
        self.push_screen(RoundsInputScreen("复制为 Markdown"), self._on_copy_rounds)

    def _on_copy_rounds(self, rounds):
        """轮次选择回调：复制 Markdown"""
        if rounds is None or rounds < 0:
            return
        self._copy_markdown(rounds)

    def action_new_session(self):
        """Ctrl+N: 新建会话"""
        self._cmd_new_session()

    def action_resume_session(self):
        """Ctrl+R: 打开会话选择弹窗"""
        self.push_screen(SessionSelectScreen(self.agent), self._on_session_selected)

    def _on_session_selected(self, session_id):
        """会话选择回调"""
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

    def _show_tool_details(self):
        """显示工具详情弹窗"""
        self.push_screen(ToolDetailScreen(self.agent))

    def _edit_last_message(self):
        """编辑上一轮提问：撤回最后一轮对话，将用户消息放入输入框"""
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

    def _redraw_chat(self):
        """根据 agent.messages 重绘聊天区（各角色用不同颜色/背景区分）

        视觉设计（参考 ChatGPT / Claude / Cursor 的配色最佳实践）：
          - 用户消息：绿色边框 Panel（已有）
          - AI 回复：青蓝色标签 + Markdown 内容
          - 思考过程：紫灰色标签 + 缩进斜体内容
          - 工具调用：琥珀色标签 + 深色背景面板
          - 工具结果：灰绿色标签 + 深色背景面板
        """
        chat = self.query_one("#chat-panel", RichLog)
        chat.clear()
        total = len(self.agent.available_models)
        chat.write(f"[bold #00d4aa]Learn Agent[/bold #00d4aa] | 共 [#ffd93d]{total}[/#ffd93d] 个可用模型")
        chat.write("[#6b7394]Enter=换行 | Ctrl+Enter=发送 | ↑=编辑上条 | F1=帮助[/#6b7394]\n")

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

    def action_show_help(self):
        """显示帮助弹窗"""
        self.push_screen(HelpScreen())

    def action_toggle_input(self):
        """展开/收起输入框"""
        input_widget = self.query_one("#user-input", ChatInput)
        input_widget.toggle_class("expanded")
        input_widget.focus()

    async def on_unmount(self):
        """应用退出时断开 MCP 连接"""
        await self.agent.disconnect_mcp()

    def action_clear_chat(self):
        chat = self.query_one("#chat-panel", RichLog)
        chat.clear()
        self.agent.clear_history()
        chat.write("[#6b7394]对话已清空，上下文已重置[/#6b7394]\n")

    def action_select_model(self):
        """打开模型选择弹窗"""
        self.push_screen(ModelSelectScreen(self.agent), self._on_model_selected)

    def _on_model_selected(self, model_name):
        """模型选择回调"""
        if not model_name:
            self.query_one("#user-input", ChatInput).focus()
            return

        old = self.agent.get_model_name()
        if self.agent.switch_model(model_name):
            new = self.agent.get_model_name()
            chat = self.query_one("#chat-panel", RichLog)
            chat.write(f"\n[bold #ffd93d]✦ 模型已切换:[/bold #ffd93d] [#6b7394]{old}[/#6b7394] → [bold #00d4aa]{new}[/bold #00d4aa]")
            self._update_subtitle()
            tool_panel = self.query_one("#tool-panel", ToolPanel)
            tool_panel.update_content()

        self.query_one("#user-input", ChatInput).focus()



`````

--- **end of file: learn_agent/ui/app.py** (project: learn_agent) --- 

---


--- **start of file: learn_agent/ui/styles.tcss** (project: learn_agent) --- 

`````text
/* Learn Agent TUI — Modern Dark Theme */

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

`````

--- **end of file: learn_agent/ui/styles.tcss** (project: learn_agent) --- 

---


--- **start of file: learn_agent/ui/__init__.py** (project: learn_agent) --- 

`````python

`````

--- **end of file: learn_agent/ui/__init__.py** (project: learn_agent) --- 

---

