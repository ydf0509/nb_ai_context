
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **此文档生成时间**：2026-06-14 21:14:24
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
# markdown content namespace: lc_agent_bfzs project summary 



- `lc-agent-bfzs` 是基于 lc-agent 框架的自定义 Agent 应用实例。
- 展示如何用极少代码基于 lc-agent 框架构建功能完整的 AI Agent Web 应用。
- 核心入口 `bfzs/main.py` 演示了 lc-agent 的扩展能力：
  - Tools：自定义文件工具 + 数据工具（导入即注册到全局 ToolRegistry）
  - Agent：自定义 LangGraph CompiledGraph（research_agent，多步骤研究助手）
  - MCP：配置多个 MCP Server（filesystem、nbrag、context7 等）
  - Skills：配置 skills 目录
- 关键文件：
  - `bfzs/main.py`: 入口，加载配置 → 注册工具 → 构建 Agent → 启动
  - `bfzs/agents/research_agent.py`: 研究助手 Agent（plan → research → summarize）
  - `bfzs/tools/file_tools.py`: 文件操作工具
  - `bfzs/tools/data_tools.py`: 数据分析工具
  - `config.jsonc`: 模型/MCP/Skills 配置


## 📋 lc_agent_bfzs most core source files metadata (Entry Points)


以下是项目 lc_agent_bfzs 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project lc_agent_bfzs most core source code files as follows: 
- `bfzs/main.py`
- `bfzs/agents/research_agent.py`
- `bfzs/tools/file_tools.py`


### 📄 Python File Metadata: `bfzs/main.py`

#### 📝 Module Docstring

`````
bfzs 应用入口 — 演示如何使用 lc-agent 框架开发自定义 Agent 应用
`````

#### 📦 Imports

- `import argparse`
- `from pathlib import Path`
- `from bfzs import init_loggers`
- `from lc_agent import LcAgentApp`
- `from lc_agent import load_config`
- `import bfzs.tools.file_tools`
- `import bfzs.tools.data_tools`
- `from bfzs.agents.research_agent import build_research_agent`

#### 🔧 Public Functions (1)

- `def main()`
  - *Line: 7*


---




### 📄 Python File Metadata: `bfzs/agents/research_agent.py`

#### 📝 Module Docstring

`````
研究助手 Agent — 演示如何创建自定义 CompiledGraph 并注册到框架

这是一个多步骤研究 Agent，能够：
1. 根据用户问题制定研究计划
2. 逐步执行研究（调用工具搜集信息）
3. 整合结果并给出结论
`````

#### 📦 Imports

- `from __future__ import annotations`
- `from typing import Annotated`
- `from typing import TypedDict`
- `from langchain_core.messages import AIMessage`
- `from langchain_core.messages import HumanMessage`
- `from langchain_core.messages import SystemMessage`
- `from langgraph.graph import StateGraph`
- `from langgraph.graph import START`
- `from langgraph.graph import END`
- `from langgraph.graph.message import add_messages`
- `from lc_agent.core.chat_model import ChatOpenAIReasoning`
- `from langchain.chat_models import init_chat_model`

#### 🏛️ Classes (1)

##### 📌 `class ResearchState(TypedDict)`
*Line: 18*

**Docstring:**
`````
研究 Agent 的状态定义
`````

**Class Variables (4):**
- `messages: Annotated[list, add_messages]`
- `research_plan: str`
- `findings: list[str]`
- `step: int`

#### 🔧 Public Functions (5)

- `def build_research_agent(config: dict)`
  - *Line: 34*
  - **Docstring:**
  `````
  构建研究助手的 CompiledGraph。
  
  Args:
      config: 应用配置字典，用于获取 LLM 配置
  
  Returns:
      编译后的 LangGraph StateGraph (CompiledGraph)
  `````

- `async def plan_node(state: ResearchState) -> dict`
  - *Line: 69*
  - *制定研究计划*

- `async def research_node(state: ResearchState) -> dict`
  - *Line: 84*
  - *执行研究*

- `async def summarize_node(state: ResearchState) -> dict`
  - *Line: 100*
  - *整合总结*

- `def should_continue_research(state: ResearchState) -> str`
  - *Line: 115*
  - *判断是否继续研究*


---




### 📄 Python File Metadata: `bfzs/tools/file_tools.py`

#### 📝 Module Docstring

`````
文件管理工具组 — 提供文件读写、目录浏览等功能
`````

#### 📦 Imports

- `import os`
- `from pathlib import Path`
- `from lc_agent import tool`

#### 🔧 Public Functions (4)

- `def read_file(file_path: str) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 10*
  - **Docstring:**
  `````
  读取指定文件的内容。
  
  Args:
      file_path: 文件的绝对或相对路径
  `````

- `def write_file(file_path: str, content: str) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 28*
  - **Docstring:**
  `````
  将内容写入指定文件（会覆盖已有内容）。
  
  Args:
      file_path: 文件路径
      content: 要写入的内容
  `````

- `def list_directory(directory: str = '.', show_hidden: bool = False) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 42*
  - **Docstring:**
  `````
  列出目录下的所有文件和子目录。
  
  Args:
      directory: 目录路径，默认当前目录
      show_hidden: 是否显示隐藏文件
  `````

- `def search_files(directory: str, pattern: str) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 72*
  - **Docstring:**
  `````
  递归搜索匹配模式的文件。
  
  Args:
      directory: 搜索根目录
      pattern: glob 模式，如 *.py, **/*.md
  `````


---



## 🔗 lc_agent_bfzs Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ bfzs/main.py

Core Files (imported by other files, sorted by import count):
  ◆ bfzs/agents/research_agent.py (imported by 1 files)
  ◆ bfzs/tools/file_tools.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `bfzs/agents/research_agent.py`

**Imported by:**
- `bfzs/main.py`

#### `bfzs/main.py`

**Imports from project:**
- `bfzs/agents/research_agent.py`
- `bfzs/tools/file_tools.py`

#### `bfzs/tools/file_tools.py`

**Imported by:**
- `bfzs/main.py`

### 📦 Third-party Dependencies

项目使用的第三方库：

- `bfzs`
- `langchain`
- `langchain_core`
- `langgraph`
- `lc_agent`
- ......以及更多的第三方库......


---
# markdown content namespace: lc_agent_bfzs Project Root Dir Some Files 


## lc_agent_bfzs File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## lc_agent_bfzs (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: lc_agent_bfzs) --- 

`````markdown
# lc-agent-bfzs

基于 [lc-agent](../lc-agent) 框架开发的自定义 Agent 应用示例。

## 项目结构

```
lc-agent-bfzs/
├── pyproject.toml          # 项目配置，依赖 lc-agent
├── config.jsonc            # 运行时配置
├── bfzs/                   # Python 包
│   ├── main.py             # 入口：配置 → 注册工具 → 注册Agent → 启动
│   ├── tools/              # 自定义工具（按分组）
│   │   ├── file_tools.py   # [file_mgmt] 文件管理
│   │   └── data_tools.py   # [data_analysis] 数据分析
│   └── agents/             # 自定义 CompiledGraph Agent
│       └── research_agent.py   # 研究助手（多步骤 LangGraph）
└── myskills/               # 自定义 Skills（SKILL.md 格式）
    ├── code-review/
    │   └── SKILL.md        # [开发辅助] 代码审查
    └── doc-summarize/
        └── SKILL.md        # [文本处理] 文档摘要
```

## 安装运行

```bash
# 前提：已安装 lc-agent 框架
pip install -e D:\codes\lc-agent

# 安装本项目
pip install -e .

# 启动（默认端口 8001）
bfzs
# 或
python -m bfzs.main --port 8001

# 访问 Web UI
# http://127.0.0.1:8001
```

## 使用方式说明

本项目演示了 lc-agent 框架的三种核心扩展方式：

### 1. 自定义工具

使用 `@tool` 装饰器，导入即自动注册到全局 ToolRegistry：

```python
from lc_agent import tool

@tool(group="file_mgmt", group_description="文件管理")
def read_file(file_path: str) -> str:
    """读取文件内容"""
    ...
```

### 2. 自定义 Agent（CompiledGraph）

使用 LangGraph 构建自定义 StateGraph，通过 `app.add_agent()` 注册：

```python
from langgraph.graph import StateGraph, END

graph = StateGraph(MyState)
graph.add_node("plan", plan_node)
graph.add_node("execute", execute_node)
graph.set_entry_point("plan")
graph.add_edge("plan", "execute")
graph.add_edge("execute", END)

compiled = graph.compile()
app.add_agent("my_agent", compiled, description="我的Agent")
```

### 3. 自定义 Skills

在 `myskills/` 目录下创建 SKILL.md，遵循 agentskills.io 规范：

```yaml
---
name: my-skill          # 文件夹名必须与此一致
description: 技能描述
metadata:
  group: "技能组名"     # 用于按组激活/屏蔽
---
# 技能指令内容
```

## 配置

编辑 `config.jsonc` 配置 LLM、数据库、Skills 目录等。支持 JSONC 注释和 `{env:VAR}` 环境变量。

## 思考过程显示

框架使用 `ChatOpenAIReasoning` 类自动提取模型的推理内容（`reasoning_content`），支持在前端显示"思考中"面板。

| 模型 | 思考过程 | 说明 |
|------|:---:|------|
| `ds-deepseek-v4-flash` | 始终显示 | DeepSeek 官方 API |
| `ark-deepseek-v4-flash` | 始终显示 | 字节方舟 Coding Plan |
| `ark-glm-5.1` | 复杂任务时显示 | 简单问题不触发思考 |

## 与框架的关系

```
lc-agent（框架，pip install）
    ↓ import
lc-agent-bfzs（本项目，用户业务代码）
```

- 不修改框架代码
- 通过 import + 装饰器 + 配置文件扩展
- 框架提供 Web UI / API / 引擎 / 持久化 / reasoning 提取
- 本项目只写业务逻辑（tools / agents / skills）

`````

--- **end of file: README.md** (project: lc_agent_bfzs) --- 

---


--- **start of file: pyproject.toml** (project: lc_agent_bfzs) --- 

`````text
[project]
name = "lc-agent-bfzs"
version = "0.1.0"
description = "基于 lc-agent 框架开发的自定义 Agent 应用"
requires-python = ">=3.12"
dependencies = [
    "lc-agent",
]

[project.scripts]
bfzs = "bfzs.main:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["bfzs"]

[tool.ruff]
target-version = "py312"
line-length = 120

`````

--- **end of file: pyproject.toml** (project: lc_agent_bfzs) --- 

---

# markdown content namespace: lc_agent_bfzs 应用代码 


## lc_agent_bfzs File Tree (relative dir: `bfzs`)


`````

└── bfzs
    ├── __init__.py
    ├── agents
    │   ├── __init__.py
    │   └── research_agent.py
    ├── init_loggers.py
    ├── main.py
    └── tools
        ├── __init__.py
        ├── data_tools.py
        └── file_tools.py

`````

---


## lc_agent_bfzs (relative dir: `bfzs`)  Included Files (total: 8 files)


- `bfzs/init_loggers.py`

- `bfzs/main.py`

- `bfzs/__init__.py`

- `bfzs/agents/research_agent.py`

- `bfzs/agents/__init__.py`

- `bfzs/tools/data_tools.py`

- `bfzs/tools/file_tools.py`

- `bfzs/tools/__init__.py`


---


--- **start of file: bfzs/init_loggers.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/init_loggers.py`

#### 📦 Imports

- `import nb_log`


---

`````python

import nb_log


nb_log.get_logger("lc_agent.debug",log_filename="lc_agent_debug.log",
               error_log_filename="lc_agent_debug_error.log",)


nb_log.get_logger("lc_agent.mcp",log_filename="lc_agent_mcp.log",
               error_log_filename="lc_agent_mcp_error.log",)

`````

--- **end of file: bfzs/init_loggers.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/main.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/main.py`

#### 📝 Module Docstring

`````
bfzs 应用入口 — 演示如何使用 lc-agent 框架开发自定义 Agent 应用
`````

#### 📦 Imports

- `import argparse`
- `from pathlib import Path`
- `from bfzs import init_loggers`
- `from lc_agent import LcAgentApp`
- `from lc_agent import load_config`
- `import bfzs.tools.file_tools`
- `import bfzs.tools.data_tools`
- `from bfzs.agents.research_agent import build_research_agent`

#### 🔧 Public Functions (1)

- `def main()`
  - *Line: 7*


---

`````python
"""bfzs 应用入口 — 演示如何使用 lc-agent 框架开发自定义 Agent 应用"""

import argparse
from pathlib import Path
from bfzs import init_loggers

def main():
    parser = argparse.ArgumentParser(description="lc-agent-bfzs 自定义 Agent 应用")
    parser.add_argument("--config", "-c", help="配置文件路径", default=None)
    parser.add_argument("--host", default="127.0.0.1", help="服务器地址")
    parser.add_argument("--port", "-p", type=int, default=8001, help="服务器端口")
    args = parser.parse_args()

    config_path = args.config or str(Path(__file__).parent.parent / "config.jsonc")

    from lc_agent import LcAgentApp, load_config

    config = load_config(config_path=config_path)

    # 导入自定义工具（导入即注册到全局 ToolRegistry）
    import bfzs.tools.file_tools  # noqa: F401
    import bfzs.tools.data_tools  # noqa: F401

    app = LcAgentApp(config, host=args.host, port=args.port)

    # 注册自定义 CompiledGraph Agent
    from bfzs.agents.research_agent import build_research_agent

    research_graph = build_research_agent(config)
    app.add_agent(
        name="research_assistant",
        graph=research_graph,
        description="研究助手：擅长多步骤信息收集、整理和分析",
    )

    app.run()


if __name__ == "__main__":
    main()

`````

--- **end of file: bfzs/main.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/__init__.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/__init__.py`

#### 📝 Module Docstring

`````
lc-agent-bfzs — 基于 lc-agent 框架的自定义 Agent 应用
`````


---

`````python
"""lc-agent-bfzs — 基于 lc-agent 框架的自定义 Agent 应用"""

__version__ = "0.1.0"

`````

--- **end of file: bfzs/__init__.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/agents/research_agent.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/agents/research_agent.py`

#### 📝 Module Docstring

`````
研究助手 Agent — 演示如何创建自定义 CompiledGraph 并注册到框架

这是一个多步骤研究 Agent，能够：
1. 根据用户问题制定研究计划
2. 逐步执行研究（调用工具搜集信息）
3. 整合结果并给出结论
`````

#### 📦 Imports

- `from __future__ import annotations`
- `from typing import Annotated`
- `from typing import TypedDict`
- `from langchain_core.messages import AIMessage`
- `from langchain_core.messages import HumanMessage`
- `from langchain_core.messages import SystemMessage`
- `from langgraph.graph import StateGraph`
- `from langgraph.graph import START`
- `from langgraph.graph import END`
- `from langgraph.graph.message import add_messages`
- `from lc_agent.core.chat_model import ChatOpenAIReasoning`
- `from langchain.chat_models import init_chat_model`

#### 🏛️ Classes (1)

##### 📌 `class ResearchState(TypedDict)`
*Line: 18*

**Docstring:**
`````
研究 Agent 的状态定义
`````

**Class Variables (4):**
- `messages: Annotated[list, add_messages]`
- `research_plan: str`
- `findings: list[str]`
- `step: int`

#### 🔧 Public Functions (5)

- `def build_research_agent(config: dict)`
  - *Line: 34*
  - **Docstring:**
  `````
  构建研究助手的 CompiledGraph。
  
  Args:
      config: 应用配置字典，用于获取 LLM 配置
  
  Returns:
      编译后的 LangGraph StateGraph (CompiledGraph)
  `````

- `async def plan_node(state: ResearchState) -> dict`
  - *Line: 69*
  - *制定研究计划*

- `async def research_node(state: ResearchState) -> dict`
  - *Line: 84*
  - *执行研究*

- `async def summarize_node(state: ResearchState) -> dict`
  - *Line: 100*
  - *整合总结*

- `def should_continue_research(state: ResearchState) -> str`
  - *Line: 115*
  - *判断是否继续研究*


---

`````python
"""研究助手 Agent — 演示如何创建自定义 CompiledGraph 并注册到框架

这是一个多步骤研究 Agent，能够：
1. 根据用户问题制定研究计划
2. 逐步执行研究（调用工具搜集信息）
3. 整合结果并给出结论
"""

from __future__ import annotations

from typing import Annotated, TypedDict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class ResearchState(TypedDict):
    """研究 Agent 的状态定义"""
    messages: Annotated[list, add_messages]
    research_plan: str
    findings: list[str]
    step: int


RESEARCH_SYSTEM_PROMPT = """你是一个专业的研究助手。你的工作流程是：
1. 分析用户的问题，制定研究计划
2. 逐步执行研究计划
3. 整合所有发现，给出完整的分析报告

请用中文回答，条理清晰，有理有据。"""


def build_research_agent(config: dict):
    """构建研究助手的 CompiledGraph。

    Args:
        config: 应用配置字典，用于获取 LLM 配置

    Returns:
        编译后的 LangGraph StateGraph (CompiledGraph)
    """
    provider_name = ""
    provider_conf = {}
    for name, conf in config.get("provider", {}).items():
        if isinstance(conf, dict) and conf.get("models"):
            provider_name = name
            provider_conf = conf
            break

    model_id = config.get("agent", {}).get("default_model", "gpt-4")
    base_url = provider_conf.get("base_url", "")
    api_key = provider_conf.get("api_key", "not-set")

    if base_url:
        from lc_agent.core.chat_model import ChatOpenAIReasoning
        llm = ChatOpenAIReasoning(
            model=model_id,
            base_url=base_url,
            api_key=api_key,
            temperature=0.3,
            stream_usage=True,
        )
    else:
        from langchain.chat_models import init_chat_model
        model_str = f"{provider_name}:{model_id}" if provider_name else model_id
        llm = init_chat_model(model_str, api_key=api_key, temperature=0.3, stream_usage=True)

    async def plan_node(state: ResearchState) -> dict:
        """制定研究计划"""
        messages = [SystemMessage(content=RESEARCH_SYSTEM_PROMPT)] + state["messages"]
        planning_prompt = (
            "请分析用户的问题，制定一个简洁的研究计划（2-3个步骤）。"
            "只输出计划本身，格式：步骤1: xxx\n步骤2: xxx"
        )
        messages.append(HumanMessage(content=planning_prompt))
        response = await llm.ainvoke(messages)
        return {
            "research_plan": response.content,
            "step": 1,
            "messages": [AIMessage(content=f"📋 研究计划:\n{response.content}")],
        }

    async def research_node(state: ResearchState) -> dict:
        """执行研究"""
        messages = [SystemMessage(content=RESEARCH_SYSTEM_PROMPT)] + state["messages"]
        research_prompt = (
            f"根据研究计划:\n{state['research_plan']}\n\n"
            f"现在执行步骤 {state['step']}，给出你的分析和发现。"
        )
        messages.append(HumanMessage(content=research_prompt))
        response = await llm.ainvoke(messages)
        findings = state.get("findings", []) + [response.content]
        return {
            "findings": findings,
            "step": state["step"] + 1,
            "messages": [AIMessage(content=f"🔍 步骤{state['step']}发现:\n{response.content}")],
        }

    async def summarize_node(state: ResearchState) -> dict:
        """整合总结"""
        messages = [SystemMessage(content=RESEARCH_SYSTEM_PROMPT)] + state["messages"]
        findings_text = "\n\n".join(
            f"发现{i+1}: {f}" for i, f in enumerate(state.get("findings", []))
        )
        summary_prompt = (
            f"请整合以下研究发现，给出一份简洁、结构化的最终报告:\n\n{findings_text}"
        )
        messages.append(HumanMessage(content=summary_prompt))
        response = await llm.ainvoke(messages)
        return {
            "messages": [AIMessage(content=f"📝 研究报告:\n{response.content}")],
        }

    def should_continue_research(state: ResearchState) -> str:
        """判断是否继续研究"""
        plan_lines = [l for l in state.get("research_plan", "").split("\n") if l.strip()]
        total_steps = max(len(plan_lines), 2)
        if state.get("step", 1) > total_steps:
            return "summarize"
        return "research"

    graph = StateGraph(ResearchState)

    graph.add_node("plan", plan_node)
    graph.add_node("research", research_node)
    graph.add_node("summarize", summarize_node)

    graph.add_edge(START, "plan")
    graph.add_edge("plan", "research")
    graph.add_conditional_edges("research", should_continue_research, {
        "research": "research",
        "summarize": "summarize",
    })
    graph.add_edge("summarize", END)

    return graph.compile()

`````

--- **end of file: bfzs/agents/research_agent.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/agents/__init__.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/agents/__init__.py`

#### 📝 Module Docstring

`````
自定义 Agent 模块 — 使用 LangGraph 构建自定义 CompiledGraph
`````


---

`````python
"""自定义 Agent 模块 — 使用 LangGraph 构建自定义 CompiledGraph"""

`````

--- **end of file: bfzs/agents/__init__.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/tools/data_tools.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/tools/data_tools.py`

#### 📝 Module Docstring

`````
数据分析工具组 — 提供简单的数据处理和计算功能
`````

#### 📦 Imports

- `import json`
- `import math`
- `from typing import Any`
- `from lc_agent import tool`
- `from pathlib import Path`
- `import csv`

#### 🔧 Public Functions (4)

- `def calculate(expression: str) -> str` `tool(group='data_analysis', group_description='数据分析')`
  - *Line: 11*
  - **Docstring:**
  `````
  计算数学表达式。支持基本运算和 math 模块函数。
  
  Args:
      expression: 数学表达式，如 "2**10", "math.sqrt(144)", "sum([1,2,3,4,5])"
  `````

- `def parse_json(json_string: str) -> str` `tool(group='data_analysis', group_description='数据分析')`
  - *Line: 30*
  - **Docstring:**
  `````
  解析 JSON 字符串并格式化输出。
  
  Args:
      json_string: JSON 格式字符串
  `````

- `def text_statistics(text: str) -> str` `tool(group='data_analysis', group_description='数据分析')`
  - *Line: 45*
  - **Docstring:**
  `````
  统计文本的基本信息。
  
  Args:
      text: 要分析的文本
  `````

- `def csv_preview(file_path: str, max_rows: int = 10) -> str` `tool(group='data_analysis', group_description='数据分析')`
  - *Line: 66*
  - **Docstring:**
  `````
  预览 CSV 文件的前几行。
  
  Args:
      file_path: CSV 文件路径
      max_rows: 最多显示的行数，默认10行
  `````


---

`````python
"""数据分析工具组 — 提供简单的数据处理和计算功能"""

import json
import math
from typing import Any

from lc_agent import tool


@tool(group="data_analysis", group_description="数据分析")
def calculate(expression: str) -> str:
    """计算数学表达式。支持基本运算和 math 模块函数。

    Args:
        expression: 数学表达式，如 "2**10", "math.sqrt(144)", "sum([1,2,3,4,5])"
    """
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("_")
    }
    allowed_names.update({"abs": abs, "round": round, "sum": sum, "min": min, "max": max})

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"{expression} = {result}"
    except Exception as e:
        return f"计算错误: {e}"


@tool(group="data_analysis", group_description="数据分析")
def parse_json(json_string: str) -> str:
    """解析 JSON 字符串并格式化输出。

    Args:
        json_string: JSON 格式字符串
    """
    try:
        data = json.loads(json_string)
        formatted = json.dumps(data, ensure_ascii=False, indent=2)
        return f"解析结果:\n{formatted}"
    except json.JSONDecodeError as e:
        return f"JSON 解析失败: {e}"


@tool(group="data_analysis", group_description="数据分析")
def text_statistics(text: str) -> str:
    """统计文本的基本信息。

    Args:
        text: 要分析的文本
    """
    lines = text.split("\n")
    words = text.split()
    chars = len(text)
    chars_no_space = len(text.replace(" ", "").replace("\n", ""))

    return (
        f"文本统计:\n"
        f"  总字符数: {chars}\n"
        f"  字符数(不含空格): {chars_no_space}\n"
        f"  行数: {len(lines)}\n"
        f"  词数/段落数: {len(words)}"
    )


@tool(group="data_analysis", group_description="数据分析")
def csv_preview(file_path: str, max_rows: int = 10) -> str:
    """预览 CSV 文件的前几行。

    Args:
        file_path: CSV 文件路径
        max_rows: 最多显示的行数，默认10行
    """
    from pathlib import Path
    import csv

    p = Path(file_path).expanduser()
    if not p.exists():
        return f"错误: 文件不存在 - {p}"

    try:
        with open(p, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                if i >= max_rows + 1:
                    break
                rows.append(row)

        if not rows:
            return "CSV 文件为空"

        header = rows[0]
        data_rows = rows[1:]
        col_widths = [max(len(str(cell)) for cell in col) for col in zip(*rows)]

        lines = []
        lines.append(" | ".join(h.ljust(w) for h, w in zip(header, col_widths)))
        lines.append("-+-".join("-" * w for w in col_widths))
        for row in data_rows:
            lines.append(" | ".join(str(c).ljust(w) for c, w in zip(row, col_widths)))

        return f"CSV 预览 ({p.name}, 显示 {len(data_rows)} 行):\n\n" + "\n".join(lines)
    except Exception as e:
        return f"读取 CSV 失败: {e}"

`````

--- **end of file: bfzs/tools/data_tools.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/tools/file_tools.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/tools/file_tools.py`

#### 📝 Module Docstring

`````
文件管理工具组 — 提供文件读写、目录浏览等功能
`````

#### 📦 Imports

- `import os`
- `from pathlib import Path`
- `from lc_agent import tool`

#### 🔧 Public Functions (4)

- `def read_file(file_path: str) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 10*
  - **Docstring:**
  `````
  读取指定文件的内容。
  
  Args:
      file_path: 文件的绝对或相对路径
  `````

- `def write_file(file_path: str, content: str) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 28*
  - **Docstring:**
  `````
  将内容写入指定文件（会覆盖已有内容）。
  
  Args:
      file_path: 文件路径
      content: 要写入的内容
  `````

- `def list_directory(directory: str = '.', show_hidden: bool = False) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 42*
  - **Docstring:**
  `````
  列出目录下的所有文件和子目录。
  
  Args:
      directory: 目录路径，默认当前目录
      show_hidden: 是否显示隐藏文件
  `````

- `def search_files(directory: str, pattern: str) -> str` `tool(group='file_mgmt', group_description='文件管理')`
  - *Line: 72*
  - **Docstring:**
  `````
  递归搜索匹配模式的文件。
  
  Args:
      directory: 搜索根目录
      pattern: glob 模式，如 *.py, **/*.md
  `````


---

`````python
"""文件管理工具组 — 提供文件读写、目录浏览等功能"""

import os
from pathlib import Path

from lc_agent import tool


@tool(group="file_mgmt", group_description="文件管理")
def read_file(file_path: str) -> str:
    """读取指定文件的内容。

    Args:
        file_path: 文件的绝对或相对路径
    """
    p = Path(file_path).expanduser()
    if not p.exists():
        return f"错误: 文件不存在 - {p}"
    if not p.is_file():
        return f"错误: 路径不是文件 - {p}"
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return f"错误: 无法以 UTF-8 读取文件（可能是二进制文件）"


@tool(group="file_mgmt", group_description="文件管理")
def write_file(file_path: str, content: str) -> str:
    """将内容写入指定文件（会覆盖已有内容）。

    Args:
        file_path: 文件路径
        content: 要写入的内容
    """
    p = Path(file_path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"已写入文件: {p} ({len(content)} 字符)"


@tool(group="file_mgmt", group_description="文件管理")
def list_directory(directory: str = ".", show_hidden: bool = False) -> str:
    """列出目录下的所有文件和子目录。

    Args:
        directory: 目录路径，默认当前目录
        show_hidden: 是否显示隐藏文件
    """
    p = Path(directory).expanduser()
    if not p.exists():
        return f"错误: 目录不存在 - {p}"
    if not p.is_dir():
        return f"错误: 路径不是目录 - {p}"

    items = []
    for item in sorted(p.iterdir()):
        if not show_hidden and item.name.startswith("."):
            continue
        prefix = "📁 " if item.is_dir() else "📄 "
        size = ""
        if item.is_file():
            s = item.stat().st_size
            size = f" ({_format_size(s)})"
        items.append(f"{prefix}{item.name}{size}")

    if not items:
        return f"目录为空: {p}"
    return f"目录: {p}\n\n" + "\n".join(items)


@tool(group="file_mgmt", group_description="文件管理")
def search_files(directory: str, pattern: str) -> str:
    """递归搜索匹配模式的文件。

    Args:
        directory: 搜索根目录
        pattern: glob 模式，如 *.py, **/*.md
    """
    p = Path(directory).expanduser()
    if not p.exists():
        return f"错误: 目录不存在 - {p}"

    matches = list(p.glob(pattern))
    if not matches:
        return f"未找到匹配 '{pattern}' 的文件"

    results = [str(m.relative_to(p)) for m in matches[:50]]
    total = len(matches)
    output = "\n".join(results)
    if total > 50:
        output += f"\n\n... 共 {total} 个匹配，仅显示前 50 个"
    return output


def _format_size(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f}{unit}" if unit != "B" else f"{size}{unit}"
        size /= 1024
    return f"{size:.1f}TB"

`````

--- **end of file: bfzs/tools/file_tools.py** (project: lc_agent_bfzs) --- 

---


--- **start of file: bfzs/tools/__init__.py** (project: lc_agent_bfzs) --- 


### 📄 Python File Metadata: `bfzs/tools/__init__.py`

#### 📝 Module Docstring

`````
自定义工具包 — 所有工具模块导入时自动注册到 ToolRegistry
`````


---

`````python
"""自定义工具包 — 所有工具模块导入时自动注册到 ToolRegistry"""

`````

--- **end of file: bfzs/tools/__init__.py** (project: lc_agent_bfzs) --- 

---

# markdown content namespace: lc_agent_bfzs 配置文件 


## lc_agent_bfzs File Tree (relative dir: `.`)


`````

└── config.jsonc

`````

---


## lc_agent_bfzs (relative dir: `.`)  Included Files (total: 1 files)


- `config.jsonc`


---


--- **start of file: config.jsonc** (project: lc_agent_bfzs) --- 

`````text
{
  // LLM 提供商配置
  "provider": {
    "litellm": {
      "api_key": "sk-no-key-needed",
      "base_url": "http://localhost:4000/v1",
      "models": [
        // === 阿里百炼 ===
        // {"id": "ali-qwen3.6-plus", "context_limit": 200000},
        // {"id": "ali-qwen3.6-flash", "context_limit": 200000},
        // {"id": "ali-deepseek-v4-pro", "context_limit": 200000},
        // {"id": "ali-deepseek-v4-flash", "context_limit": 200000},
        // {"id": "ali-deepseek-v3.2", "context_limit": 200000},
        // {"id": "ali-kimi-k2.6", "context_limit": 200000},
        // {"id": "ali-kimi-k2.5", "context_limit": 200000},
        // {"id": "ali-glm-5.1", "context_limit": 200000},
        // {"id": "ali-glm-5", "context_limit": 200000},
        // {"id": "ali-MiniMax-M2.5", "context_limit": 200000},
        // === DeepSeek 官方 ===
        {"id": "ark-deepseek-v4-flash", "context_limit": 200000},
        {"id": "ds-deepseek-v4-pro", "context_limit": 200000},
        {"id": "ds-deepseek-v4-flash", "context_limit": 200000},
        // === 字节方舟 Coding Plan ===
        {"id": "ark-code-latest", "context_limit": 200000},
        {"id": "ark-doubao-seed-code", "context_limit": 200000},
        {"id": "ark-deepseek-v3.2", "context_limit": 200000},
        {"id": "ark-doubao-seed-2.0-code", "context_limit": 200000},
        {"id": "ark-doubao-seed-2.0-pro", "context_limit": 200000},
        {"id": "ark-doubao-seed-2.0-lite", "context_limit": 200000},
        {"id": "ark-minimax-m2.7", "context_limit": 200000},
        {"id": "ark-glm-5.1", "context_limit": 200000},
        {"id": "ark-kimi-k2.6", "context_limit": 200000},
        
        {"id": "ark-deepseek-v4-pro", "context_limit": 200000},
        // === 公司内部 ===
        {"id": "com-qwen3.5-397b", "context_limit": 200000},
        {"id": "com-qwen3.6-35b", "context_limit": 200000}
      ]
    }
  },

  "agent": {
    "system_prompt": "你是一个智能助手，擅长文件管理、数据分析和日常辅助任务。请用中文回答问题。",
    "default_model": "ds-deepseek-v4-flash",
    "streaming": true
  },

  "database": {
    "url": "sqlite+aiosqlite:///./bfzs_data.db",
    "checkpoint_path": "./bfzs_checkpoints.db"
  },

  "skills": {
    "directory": "./myskills"
  },

  "mcp_servers": {
    // Web 搜索 MCP
    "web-search": {
      "type": "sse",
      "url": "http://localhost:3000/sse",
      "enabled": true
    },

    // 文件系统 MCP：让 AI 读写指定目录的文件，这个是最知名的第三方文件系统MCP
    // ⚠ 必须至少提供一个绝对路径，AI 只能访问列出的目录
    // 如果编程，不要接入这个filesystem mcp，serena就够了，接入太多mcp会浪费tokens和加大ai决策难度。
    "filesystem": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem", "D:/codes/nb_agent_bfzs"]
    },

    // 用户可以先独立方式启动nbrag mcp web服务，也可以使用local模式启动
    "nbrag": {
      "type": "http",
      "url": "http://localhost:9101/mcp"
    },

    // Context7 MCP
    "context7": {
      "type": "local",
      "command": ["npx", "-y", "@upstash/context7-mcp@latest"],
      "enabled": true
    },

    // Serena 代码分析 MCP — 已修正路径
    "serena": {
      "type": "local",
      "command": ["C:/Users/ydf6/.local/bin/serena.exe", "start-mcp-server", "--project", "D:/codes/lc-agent"],
      "enabled": true
    },

    // LangChain 官方文档 MCP
    "docs-langchain": {
      "type": "http",
      "url": "https://docs.langchain.com/mcp"
    },

    // LangChain API 参考 MCP
    "reference-langchain": {
      "type": "http",
      "url": "https://reference.langchain.com/mcp"
    }
  }
}

`````

--- **end of file: config.jsonc** (project: lc_agent_bfzs) --- 

---

