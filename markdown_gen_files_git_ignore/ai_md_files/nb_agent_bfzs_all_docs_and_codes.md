
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **此文档生成时间**：2026-06-05 20:18:38
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
# markdown content namespace: nb_agent_bfzs project summary 



- `nb_agent_bfzs` 是基于 nb_agent 框架的演示项目——智能笔记助手，展示如何用极少代码构建功能完整的 AI Agent + 终端 TUI。
- 核心入口 `main.py` 不到 10 行，演示了 nb_agent 的所有扩展能力：
  - Tools：7 个自定义工具（笔记 CRUD 5 个 + 项目统计 2 个）
  - MCP Server：书签管理（FastMCP）、Redis 7 工具（万能执行 + 智能读写 + 监控）、web-search（SSE）、filesystem（npx）
  - Skills：6 个（日报、会议纪要、Git changelog、代码审查、重构、代码解释）
  - 审批引擎：配置层 + 代码层双重审批（Redis 写命令细粒度控制）
- 关键文件：
  - `main.py`: 入口，加载配置 → 注册审批规则 → 启动 TUI
  - `config.jsonc`: 模型 / MCP / 审批 / UI 配置
  - `approval_rules.py`: 自定义审批规则（Redis 写命令拦截、危险工具黑名单）
  - `tools/note_tools.py`: 笔记 CRUD 工具（group="note"）
  - `tools/project_tools.py`: 项目文件统计工具（group="project"）
  - `mcp_servers/bookmark_server.py`: FastMCP 书签管理 Server
  - `mcp_servers/redis_tools_server.py`: FastMCP Redis 工具 Server
  - `.nb_agent/skills/*/SKILL.md`: Agent Skills（agentskills.io 规范）


## 📋 nb_agent_bfzs most core source files metadata (Entry Points)


以下是项目 nb_agent_bfzs 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nb_agent_bfzs most core source code files as follows: 
- `main.py`
- `approval_rules.py`
- `tools/note_tools.py`


### 📄 Python File Metadata: `main.py`

#### 📝 Module Docstring

`````
nb_agent_bfzs — 智能笔记助手（nb_agent 演示项目）

只需几行代码，就拥有自己的 AI Agent + 终端 TUI：

  1. pip install nb_agent
  2. 在 tools/ 下用 @tool 定义工具
  3. 在 .nb_agent/skills/ 下放 SKILL.md
  4. 在 config.jsonc 里配置模型和 MCP
  5. python main.py
`````

#### 📦 Imports

- `import tools`
- `from approval_rules import ALL_RULES`
- `from nb_agent import load_config`
- `from nb_agent import AgentApp`


---




### 📄 Python File Metadata: `approval_rules.py`

#### 📝 Module Docstring

`````
自定义审批规则 — 演示 nb_agent 的工具调用审批机制

nb_agent 的 ApprovalEngine 支持用户注入自定义规则函数:
  - 规则签名: (tool_name: str, tool_kwargs: dict) -> bool
  - 返回 True → 弹窗让用户确认后才执行
  - 返回 False → 放行（不弹窗）
  - 多条规则按顺序检查，任一命中即触发审批

工具名格式:
  - 本地 @tool:          函数名，如 "delete_note"
  - MCP 工具:   mcp__{config 中的 key}__{函数名}，如 "mcp__redis-tools__redis_execute"
`````

#### 🔧 Public Functions (3)

- `def rule_redis_write(tool_name: str, tool_kwargs: dict) -> bool`
  - *Line: 43*
  - *Redis redis_execute 中的写命令需要审批，只读命令（GET/HGETALL/INFO）放行*

- `def rule_dangerous_tools(tool_name: str, tool_kwargs: dict) -> bool`
  - *Line: 53*
  - *黑名单中的工具始终需要审批*

- `def rule_note_delete(tool_name: str, tool_kwargs: dict) -> bool`
  - *Line: 58*
  - *删除笔记操作需要审批*


---




### 📄 Python File Metadata: `tools/note_tools.py`

#### 📝 Module Docstring

`````
笔记管理工具 — 增删查改笔记

每个工具通过 @tool 装饰器自动注册到 nb_agent。
AI 会根据用户意图自主决定调用哪个工具。
`````

#### 📦 Imports

- `import json`
- `import os`
- `from datetime import datetime`
- `from pathlib import Path`
- `from typing import Optional`
- `from pydantic import BaseModel`
- `from pydantic import Field`
- `from nb_agent.tools import tool`

#### 🏛️ Classes (5)

##### 📌 `class CreateNoteParams(BaseModel)`
*Line: 22*

**Class Variables (3):**
- `title: str = Field(description='笔记标题')`
- `content: str = Field(description='笔记内容（支持 Markdown）')`
- `tags: str = Field(default='', description="逗号分隔的标签，如 'work,meeting,todo'")`

##### 📌 `class SearchNotesParams(BaseModel)`
*Line: 54*

**Class Variables (2):**
- `keyword: str = Field(description='搜索关键词（在标题和内容中查找）')`
- `tag: str = Field(default='', description='按标签过滤（可选）')`

##### 📌 `class ListNotesParams(BaseModel)`
*Line: 90*

**Class Variables (1):**
- `limit: int = Field(default=10, description='返回的笔记数量上限')`

##### 📌 `class ReadNoteParams(BaseModel)`
*Line: 116*

**Class Variables (1):**
- `filename: str = Field(description="笔记文件名，如 '20260527_143000_会议记录.md'")`

##### 📌 `class DeleteNoteParams(BaseModel)`
*Line: 129*

**Class Variables (1):**
- `filename: str = Field(description='要删除的笔记文件名')`

#### 🔧 Public Functions (5)

- `def create_note(params: CreateNoteParams) -> str` `tool(group='note')`
  - *Line: 29*
  - *创建一条笔记，保存到本地文件*

- `def search_notes(params: SearchNotesParams) -> str` `tool(group='note')`
  - *Line: 60*
  - *搜索笔记，按关键词和标签过滤*

- `def list_notes(params: ListNotesParams) -> str` `tool(group='note')`
  - *Line: 95*
  - *列出最近的笔记*

- `def read_note(params: ReadNoteParams) -> str` `tool(group='note')`
  - *Line: 121*
  - *读取某条笔记的完整内容*

- `def delete_note(params: DeleteNoteParams) -> str` `tool(group='note')`
  - *Line: 134*
  - *删除一条笔记（危险操作，需要用户确认）*


---



## 🔗 nb_agent_bfzs Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ main.py
  ★ tools/note_tools.py

Core Files (imported by other files, sorted by import count):
  ◆ approval_rules.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `approval_rules.py`

**Imported by:**
- `main.py`

#### `main.py`

**Imports from project:**
- `approval_rules.py`

### 📦 Third-party Dependencies

项目使用的第三方库：

- `nb_agent`
- `pydantic`
- `tools`
- ......以及更多的第三方库......


---
# markdown content namespace: nb_agent_bfzs Project Root Dir Some Files 


## nb_agent_bfzs File Tree (relative dir: `.`)


`````

└── README.md

`````

---


## nb_agent_bfzs (relative dir: `.`)  Included Files (total: 1 files)


- `README.md`


---


--- **start of file: README.md** (project: nb_agent_bfzs) --- 

`````markdown
# nb_agent_bfzs 

基于 [nb_agent](https://github.com/ydf0509/nb_agent) 框架的演示项目，展示如何用极少代码构建功能完整的 AI Agent + 终端 TUI。

此项目只是服务于演示nb_agent框架如何使用。
## 快速开始

```bash
pip install very_nb_agent # 注意install 是 very_nb_agent ，使用时候是import nb_agent ，因为nb_agent包名和别人的nbagent太相似被pypi拒绝
cd nb_agent_bfzs
python main.py
```

## 核心代码

```python
# main.py — 完整入口代码
import tools                          # 导入即注册自定义工具
from approval_rules import ALL_RULES
from nb_agent import load_config, AgentApp

config = load_config()
app = AgentApp(config)

for rule in ALL_RULES:                # 注册自定义审批规则
    app.agent.approval_engine.add_rule(rule)

app.run()
```

## 截图例子
使用nb-agent创建一个娱乐八卦新闻智能体，在智能体超级爱你回话提问如下:杨幂这个月做了什么呀？截图如下
![alt text](pictures/image.png)

创建智能体的界面截图:
![alt text](pictures/image2.png)

nb-agent 是个框架，自带tui，用户希望nb-agent 做什么都可以，可以用于ai coding编程，也可以用于联网娱乐八卦，也可以用于实现用户自定义的功能，nb-agent 不是限定只做claudecode opencdeo这样的ai编程终端。

## 项目结构

```
nb_agent_bfzs/
├── main.py                    # 入口（< 10 行核心代码）
├── config.jsonc                # 模型 + MCP + 审批配置
├── approval_rules.py           # 自定义审批规则
├── nb_log_config.py            # TUI 必需的 nb_log 配置,(自动生成的，不需要用户创建)
│
├── tools/                      # 自定义工具（@tool 装饰器，导入即注册）
│   ├── note_tools.py           #   笔记 CRUD（5 个工具，group="note"）
│   └── project_tools.py        #   项目统计（2 个工具，group="project"）
│
├── mcp_servers/                # 自研 MCP Server（FastMCP 实现）
│   ├── bookmark_server.py      #   书签管理（4 个工具）
│   └── redis_tools_server.py   #   Redis 操作（7 个工具）
│
├── .nb_agent/skills/           # Agent Skills（agentskills.io 规范）
│   ├── daily-report/           #   日报生成
│   ├── meeting-notes/          #   会议纪要
│   ├── git-changelog/          #   Git 变更日志（含辅助脚本）
│   ├── code-review/            #   代码审查
│   ├── refactor/               #   代码重构
│   └── explain-code/           #   代码解释
│
└── notes_data/                 # 笔记存储（运行时创建）
```

## nb_agent_bfzs 项目文件结构注意：

1. nb_agent_bfzs 只是演示 nb_agent框架的一个项目，是为了演示使用 nb-agent框架如何扩展 提示词 skill  tool mcp，不是最终的服务某个特定功能的产品，是个演示demo大杂烩。

2. skills 文件夹下是随意写的假的skill演示例子，不是本项目最终agent产品所需的，主要是为了演示skill的编写规则，遵循 agentskill.io 规范。

3. mcp_servers 文件夹下的mcp，是随便写的mcp，不是本项目最终agent产品所需的，，只是为了演示用户如何自定义自己的mcp，而不是只会依靠配置第三方mcp。

4. tools 文件夹下的工具函数，是随便写的工具函数，不是本项目最终agent产品所需的，只是为了演示用户如何在nb_agent框架中自定义tool函数，自动暴露给ai的请求协议的function字段

5. 这个项目不是为了实现记笔记，只是把记笔记的工具函数演示了下，其他功能都只是为了演示nb_agent框架的功能。

## 用户如何让 nb-agent 作为ai coding 来使用

可以在tui界面，点击agents按钮或者按f4，可以配置一个专属的 ai coding 智能体(但是如果你只搞编程，不精确搞10几个作用场景用途，那也可以不用专门配专门的编程agent)，在这个智能体要绑定 serena 这个mcp。

serena mcp的每个函数已经暴露了 入参和作用给ai，如果要让ai更精通serena，你还可以专门写一个skill，或者写在pomote提示词也行。

nb-agent 能快速化身ai coding工具，是因为serena mcp 提供了精确的 索引 读 写 执行 操作，不需要用户再亲自实现了。
![alt text](pictures/image103.png)

### 注意：

如果要实现编程，只需要介入 serena 这一个mcp就可以了，不要再接各种乱七八糟的mcp。 serena专门为编程而生，具备精确的 索引 读 写 执行 操作，在编程场景吊打通用的 fielsystem mcp读写。
nb-agent化身编程终端，只需要接入serena 这一个mcp就可以了，不要再另外接入其他乱七八糟的file system 和 codegraph 这些mcp。
有的人老是以为编程非要再接 fielsystem mcp ，才能读写项目的代码文件，这是完全错误的想法。

接入太多mcp会浪费tokens和加大ai决策难度，建议只接入必要的mcp。

## nb-agent创建的 联网搜索智能体
让大模型联网搜索总结，“普京上个月做了什么？”
![alt text](pictures/image104.png)

！！注意：大模型本身不能联网，如果你想联网需要配置mcp或者你自己写爬虫tool函数。推荐免费的 open-web-search  这个mcp,可以免费用十几个搜索引擎。




## 演示的 nb_agent 能力

### 1. 自定义工具（@tool 装饰器）

用 Pydantic 定义参数，docstring 作为工具描述，`group` 用于分组管理：

```python
from nb_agent.tools import tool
from pydantic import BaseModel, Field

class CreateNoteParams(BaseModel):
    title: str = Field(description="笔记标题")
    content: str = Field(description="Markdown 内容")
    tags: str = Field(default="", description="逗号分隔的标签")

@tool(group="note")
def create_note(params: CreateNoteParams) -> str:
    """创建一条 Markdown 笔记，保存到 notes_data 目录"""
    # ... 生成文件名，写入 frontmatter + 内容
    return f"笔记已创建: {filename}"
```

本项目注册了 7 个工具：

| 工具名 | 功能 |
|--------|------|
| `note__create_note` | 创建笔记 |
| `note__search_notes` | 按关键词/标签搜索 |
| `note__list_notes` | 列出最近笔记 |
| `note__read_note` | 读取完整笔记 |
| `note__delete_note` | 删除笔记（需审批） |
| `project__project_stats` | 统计文件数、代码行数、类型分布 |
| `project__find_files` | glob 模式搜索文件 |

### 2. MCP Server（FastMCP）

自研两个 MCP Server，通过 `config.jsonc` 配置为 stdio 方式启动：

**书签管理**（`bookmark_server.py`）：
- `add_bookmark` / `search_bookmarks` / `list_bookmarks` / `delete_bookmark`

**Redis 工具**（`redis_tools_server.py`）：
- `redis_execute` — 万能命令执行（禁止 FLUSHDB/SHUTDOWN 等危险命令）
- `redis_info` — 服务器信息
- `redis_keys` — SCAN 搜索 key（含类型/TTL/内存）
- `redis_smart_get` — 自动识别类型读取
- `redis_smart_set` — 智能写入（支持 TTL）
- `redis_db_stats` — 数据库统计
- `redis_slowlog` — 慢查询日志

还配置了两个第三方 MCP：
- **web-search**（SSE）— 多引擎搜索 + 文章抓取
- **filesystem**（npx）— AI 可读写项目目录

### 3. 审批引擎（ApprovalEngine）

双层审批机制：

**配置层**（`config.jsonc`）：
```jsonc
{
  "approval": {
    "dangerous_tools": ["note__delete_note", "mcp__redis-tools__redis_smart_set"],
    "auto_approve": false
  }
}
```

**代码层**（`approval_rules.py`）— 细粒度规则：

```python
REDIS_WRITE_COMMANDS = {"SET", "DEL", "HSET", "LPUSH", "RPUSH", "SADD", ...}

def rule_redis_write(tool_name: str, tool_kwargs: dict) -> bool:
    """Redis 写命令弹窗确认，只读命令（GET/INFO）直接放行"""
    if tool_name != "mcp__redis-tools__redis_execute":
        return False
    cmd = tool_kwargs.get("command", "").strip().split()
    return cmd[0].upper() in REDIS_WRITE_COMMANDS if cmd else False
```

效果：`GET key` 直接放行，`SET key value` 弹窗确认。

### 4. Skills（Markdown 指导手册）

6 个 Skill 覆盖常见开发场景。AI 在需要时自动调用 `view_skill` 加载完整指南：

| Skill | 触发场景 |
|-------|----------|
| daily-report | 写日报、工作总结 |
| meeting-notes | 会议记录、会议纪要 |
| git-changelog | 生成 changelog、查看提交历史 |
| code-review | 代码审查、review PR |
| refactor | 重构、优化代码结构 |
| explain-code | 解释代码功能、理解调用链 |

!!! 说明，这个项目知识演示项目，演示使用nb_agent框架，通过本地 tool函数 mcp skills 实现功能。
这几个skills并不是用于完整的编码，你想要 nb_agent 化身百年城opencode claudecode， 只需要配置好serenae 这个mcp server 就好了，config.jsonc 里面演示了如何配置mcp

### rag知识库
本项目的rag知识库是一个基于nbrag mcp server 的知识库，nbrag是和本项目同一个作者本人。



## TUI 快捷键

| 快捷键 | 功能 |
|--------|------|
| Ctrl+J / Ctrl+Enter | 发送消息 |
| Enter | 输入框内换行 |
| Tab | 切换模型 |
| Ctrl+N | 新建会话 |
| Ctrl+R | 恢复历史会话 |
| Ctrl+K | 终止 AI 回答 |
| Ctrl+P | 命令面板 |
| F1 | 帮助 |
| F2 | Skills 列表 |
| F4 | Agent 管理 |
| Ctrl+Q | 退出 |

## nb_log 配置

TUI 模式下需要在 `nb_log_config.py` 中设置以下 3 项，否则 TUI 会黑屏：

```python
PRINT_WRTIE_FILE_NAME = None   # 禁止 nb_log 劫持 sys.stdout
SYS_STD_FILE_NAME = None       # 禁止 nb_log 劫持 sys.stdout
AUTO_PATCH_PRINT = False       # 禁止 monkey patch print
```

## 配置说明

编辑 `config.jsonc`，主要配置项：

- **provider** — LLM 提供商（支持任何 OpenAI 兼容 API，配置 base_url + api_key + models）
- **agent** — system prompt、默认模型、流式开关
- **mcp** — MCP Server 配置（command + args 或 type + url）
- **approval** — 危险工具名单 + 是否自动审批

API Key 支持 `{env:DEEPSEEK_API_KEY}` 语法从环境变量读取。

## License

MIT

`````

--- **end of file: README.md** (project: nb_agent_bfzs) --- 

---

# markdown content namespace: nb_agent_bfzs tools 


## nb_agent_bfzs File Tree (relative dir: `tools`)


`````

└── tools
    ├── __init__.py
    ├── note_tools.py
    └── project_tools.py

`````

---


## nb_agent_bfzs (relative dir: `tools`)  Included Files (total: 3 files)


- `tools/note_tools.py`

- `tools/project_tools.py`

- `tools/__init__.py`


---


--- **start of file: tools/note_tools.py** (project: nb_agent_bfzs) --- 


### 📄 Python File Metadata: `tools/note_tools.py`

#### 📝 Module Docstring

`````
笔记管理工具 — 增删查改笔记

每个工具通过 @tool 装饰器自动注册到 nb_agent。
AI 会根据用户意图自主决定调用哪个工具。
`````

#### 📦 Imports

- `import json`
- `import os`
- `from datetime import datetime`
- `from pathlib import Path`
- `from typing import Optional`
- `from pydantic import BaseModel`
- `from pydantic import Field`
- `from nb_agent.tools import tool`

#### 🏛️ Classes (5)

##### 📌 `class CreateNoteParams(BaseModel)`
*Line: 22*

**Class Variables (3):**
- `title: str = Field(description='笔记标题')`
- `content: str = Field(description='笔记内容（支持 Markdown）')`
- `tags: str = Field(default='', description="逗号分隔的标签，如 'work,meeting,todo'")`

##### 📌 `class SearchNotesParams(BaseModel)`
*Line: 54*

**Class Variables (2):**
- `keyword: str = Field(description='搜索关键词（在标题和内容中查找）')`
- `tag: str = Field(default='', description='按标签过滤（可选）')`

##### 📌 `class ListNotesParams(BaseModel)`
*Line: 90*

**Class Variables (1):**
- `limit: int = Field(default=10, description='返回的笔记数量上限')`

##### 📌 `class ReadNoteParams(BaseModel)`
*Line: 116*

**Class Variables (1):**
- `filename: str = Field(description="笔记文件名，如 '20260527_143000_会议记录.md'")`

##### 📌 `class DeleteNoteParams(BaseModel)`
*Line: 129*

**Class Variables (1):**
- `filename: str = Field(description='要删除的笔记文件名')`

#### 🔧 Public Functions (5)

- `def create_note(params: CreateNoteParams) -> str` `tool(group='note')`
  - *Line: 29*
  - *创建一条笔记，保存到本地文件*

- `def search_notes(params: SearchNotesParams) -> str` `tool(group='note')`
  - *Line: 60*
  - *搜索笔记，按关键词和标签过滤*

- `def list_notes(params: ListNotesParams) -> str` `tool(group='note')`
  - *Line: 95*
  - *列出最近的笔记*

- `def read_note(params: ReadNoteParams) -> str` `tool(group='note')`
  - *Line: 121*
  - *读取某条笔记的完整内容*

- `def delete_note(params: DeleteNoteParams) -> str` `tool(group='note')`
  - *Line: 134*
  - *删除一条笔记（危险操作，需要用户确认）*


---

`````python
"""
笔记管理工具 — 增删查改笔记

每个工具通过 @tool 装饰器自动注册到 nb_agent。
AI 会根据用户意图自主决定调用哪个工具。
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field

from nb_agent.tools import tool

NOTES_DIR = Path(__file__).parent.parent / "notes_data"
NOTES_DIR.mkdir(parents=True, exist_ok=True)


class CreateNoteParams(BaseModel):
    title: str = Field(description="笔记标题")
    content: str = Field(description="笔记内容（支持 Markdown）")
    tags: str = Field(default="", description="逗号分隔的标签，如 'work,meeting,todo'")


@tool(group="note")
def create_note(params: CreateNoteParams) -> str:
    """创建一条笔记，保存到本地文件"""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c if c.isalnum() or c in "-_ " else "_" for c in params.title)
    filename = f"{ts}_{safe_title}.md"
    filepath = NOTES_DIR / filename

    tags_line = ""
    if params.tags:
        tag_list = [t.strip() for t in params.tags.split(",") if t.strip()]
        tags_line = f"tags: {', '.join(tag_list)}\n"

    note_content = (
        f"---\n"
        f"title: {params.title}\n"
        f"created: {datetime.now().isoformat()}\n"
        f"{tags_line}"
        f"---\n\n"
        f"{params.content}\n"
    )

    filepath.write_text(note_content, encoding="utf-8")
    return f"笔记已创建: {filepath.name}"


class SearchNotesParams(BaseModel):
    keyword: str = Field(description="搜索关键词（在标题和内容中查找）")
    tag: str = Field(default="", description="按标签过滤（可选）")


@tool(group="note")
def search_notes(params: SearchNotesParams) -> str:
    """搜索笔记，按关键词和标签过滤"""
    results = []
    keyword = params.keyword.lower()

    for f in sorted(NOTES_DIR.glob("*.md"), reverse=True):
        content = f.read_text(encoding="utf-8")
        title = _extract_field(content, "title") or f.stem
        tags = _extract_field(content, "tags") or ""
        created = _extract_field(content, "created") or ""

        if params.tag and params.tag.lower() not in tags.lower():
            continue

        if keyword in content.lower() or keyword in title.lower():
            body = content.split("---", 2)[-1].strip() if "---" in content else content
            preview = body[:100].replace("\n", " ")
            results.append({
                "file": f.name,
                "title": title,
                "tags": tags,
                "created": created[:19],
                "preview": preview,
            })

    if not results:
        return f"未找到包含 '{params.keyword}' 的笔记"
    return json.dumps(results[:10], ensure_ascii=False, indent=2)


class ListNotesParams(BaseModel):
    limit: int = Field(default=10, description="返回的笔记数量上限")


@tool(group="note")
def list_notes(params: ListNotesParams) -> str:
    """列出最近的笔记"""
    files = sorted(NOTES_DIR.glob("*.md"), reverse=True)
    if not files:
        return "暂无笔记"

    notes = []
    for f in files[:params.limit]:
        content = f.read_text(encoding="utf-8")
        title = _extract_field(content, "title") or f.stem
        tags = _extract_field(content, "tags") or ""
        created = _extract_field(content, "created") or ""
        notes.append({
            "file": f.name,
            "title": title,
            "tags": tags,
            "created": created[:19],
        })
    return json.dumps(notes, ensure_ascii=False, indent=2)


class ReadNoteParams(BaseModel):
    filename: str = Field(description="笔记文件名，如 '20260527_143000_会议记录.md'")


@tool(group="note")
def read_note(params: ReadNoteParams) -> str:
    """读取某条笔记的完整内容"""
    filepath = NOTES_DIR / params.filename
    if not filepath.exists():
        return f"文件不存在: {params.filename}"
    return filepath.read_text(encoding="utf-8")


class DeleteNoteParams(BaseModel):
    filename: str = Field(description="要删除的笔记文件名")


@tool(group="note")
def delete_note(params: DeleteNoteParams) -> str:
    """删除一条笔记（危险操作，需要用户确认）"""
    filepath = NOTES_DIR / params.filename
    if not filepath.exists():
        return f"文件不存在: {params.filename}"
    filepath.unlink()
    return f"已删除: {params.filename}"


def _extract_field(content: str, field_name: str) -> Optional[str]:
    """从 YAML frontmatter 中提取字段值"""
    for line in content.split("\n"):
        if line.startswith(f"{field_name}:"):
            return line[len(field_name) + 1:].strip()
    return None

`````

--- **end of file: tools/note_tools.py** (project: nb_agent_bfzs) --- 

---


--- **start of file: tools/project_tools.py** (project: nb_agent_bfzs) --- 


### 📄 Python File Metadata: `tools/project_tools.py`

#### 📝 Module Docstring

`````
项目统计工具 — 分析当前项目的文件结构和代码统计

展示如何编写不依赖外部服务的本地工具。
`````

#### 📦 Imports

- `import os`
- `from collections import Counter`
- `from collections import defaultdict`
- `from pathlib import Path`
- `from pydantic import BaseModel`
- `from pydantic import Field`
- `from nb_agent.tools import tool`

#### 🏛️ Classes (2)

##### 📌 `class ProjectStatsParams(BaseModel)`
*Line: 18*

**Class Variables (1):**
- `directory: str = Field(default='.', description='项目目录路径，默认当前目录')`

##### 📌 `class FindFilesParams(BaseModel)`
*Line: 70*

**Class Variables (3):**
- `pattern: str = Field(description="文件名匹配模式（支持 glob），如 '*.py' 或 'test_*.py'")`
- `directory: str = Field(default='.', description='搜索目录，默认当前目录')`
- `max_results: int = Field(default=20, description='最大返回数量')`

#### 🔧 Public Functions (2)

- `def project_stats(params: ProjectStatsParams) -> str` `tool(group='project')`
  - *Line: 23*
  - *统计项目的文件数量、代码行数、文件类型分布*

- `def find_files(params: FindFilesParams) -> str` `tool(group='project')`
  - *Line: 77*
  - *在项目中搜索匹配的文件*


---

`````python
"""
项目统计工具 — 分析当前项目的文件结构和代码统计

展示如何编写不依赖外部服务的本地工具。
"""

import os
from collections import Counter, defaultdict
from pathlib import Path

from pydantic import BaseModel, Field

from nb_agent.tools import tool

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv", ".mypy_cache", ".pytest_cache"}


class ProjectStatsParams(BaseModel):
    directory: str = Field(default=".", description="项目目录路径，默认当前目录")


@tool(group="project")
def project_stats(params: ProjectStatsParams) -> str:
    """统计项目的文件数量、代码行数、文件类型分布"""
    root = Path(params.directory).resolve()
    if not root.is_dir():
        return f"目录不存在: {params.directory}"

    ext_counter = Counter()
    lines_counter = defaultdict(int)
    total_files = 0
    total_lines = 0
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            ext = fpath.suffix.lower() or "(无后缀)"
            ext_counter[ext] += 1
            total_files += 1
            total_size += fpath.stat().st_size

            if ext in {".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".md", ".yaml", ".yml", ".json", ".toml"}:
                try:
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        line_count = sum(1 for _ in f)
                        lines_counter[ext] += line_count
                        total_lines += line_count
                except (OSError, UnicodeDecodeError):
                    pass

    report = [
        f"项目: {root.name}",
        f"路径: {root}",
        f"文件总数: {total_files}",
        f"代码总行数: {total_lines:,}",
        f"总大小: {_format_size(total_size)}",
        "",
        "文件类型分布 (Top 10):",
    ]
    for ext, count in ext_counter.most_common(10):
        lines = lines_counter.get(ext, 0)
        lines_info = f" ({lines:,} 行)" if lines > 0 else ""
        report.append(f"  {ext:>10}: {count:>5} 个{lines_info}")

    return "\n".join(report)


class FindFilesParams(BaseModel):
    pattern: str = Field(description="文件名匹配模式（支持 glob），如 '*.py' 或 'test_*.py'")
    directory: str = Field(default=".", description="搜索目录，默认当前目录")
    max_results: int = Field(default=20, description="最大返回数量")


@tool(group="project")
def find_files(params: FindFilesParams) -> str:
    """在项目中搜索匹配的文件"""
    root = Path(params.directory).resolve()
    if not root.is_dir():
        return f"目录不存在: {params.directory}"

    results = []
    for fpath in root.rglob(params.pattern):
        if any(skip in fpath.parts for skip in SKIP_DIRS):
            continue
        rel = fpath.relative_to(root)
        results.append(str(rel))
        if len(results) >= params.max_results:
            break

    if not results:
        return f"未找到匹配 '{params.pattern}' 的文件"

    return f"找到 {len(results)} 个文件:\n" + "\n".join(f"  {r}" for r in results)


def _format_size(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"

`````

--- **end of file: tools/project_tools.py** (project: nb_agent_bfzs) --- 

---


--- **start of file: tools/__init__.py** (project: nb_agent_bfzs) --- 


### 📄 Python File Metadata: `tools/__init__.py`

#### 📝 Module Docstring

`````
自定义工具包 — import 即自动注册到 nb_agent

使用 @tool 装饰器的函数在 import 时自动注册，
无需手动调用 register_tool()。
`````

#### 📦 Imports

- `from  import note_tools`
- `from  import project_tools`


---

`````python
"""
自定义工具包 — import 即自动注册到 nb_agent

使用 @tool 装饰器的函数在 import 时自动注册，
无需手动调用 register_tool()。
"""

from . import note_tools    # noqa: F401
from . import project_tools  # noqa: F401

`````

--- **end of file: tools/__init__.py** (project: nb_agent_bfzs) --- 

---

# markdown content namespace: nb_agent_bfzs mcp_servers 


## nb_agent_bfzs File Tree (relative dir: `mcp_servers`)


`````

└── mcp_servers
    ├── bookmark_server.py
    └── redis_tools_server.py

`````

---


## nb_agent_bfzs (relative dir: `mcp_servers`)  Included Files (total: 2 files)


- `mcp_servers/bookmark_server.py`

- `mcp_servers/redis_tools_server.py`


---


--- **start of file: mcp_servers/bookmark_server.py** (project: nb_agent_bfzs) --- 


### 📄 Python File Metadata: `mcp_servers/bookmark_server.py`

#### 📝 Module Docstring

`````
书签管理 MCP Server — 通过 MCP 协议提供书签增删查功能

展示如何用 FastMCP 编写一个 MCP Server，
只需一个 @mcp.tool() 装饰器即可定义工具，
schema 从函数签名 + Pydantic Field 自动生成。

配置方式（在 config.jsonc 的 mcp 节）：
  "bookmark": {
    "type": "local",
    "command": ["python", "mcp_servers/bookmark_server.py"],
    "enabled": true
  }
`````

#### 📦 Imports

- `import json`
- `from datetime import datetime`
- `from pathlib import Path`
- `from pydantic import Field`
- `from mcp.server.fastmcp import FastMCP`

#### 🔧 Public Functions (4)

- `def add_bookmark(url: str = Field(description='网页 URL'), title: str = Field(description='书签标题'), tags: str = Field(default='', description="逗号分隔的标签，如 'python,教程'")) -> str` `mcp.tool()`
  - *Line: 42*
  - *保存一个网页书签*

- `def search_bookmarks(keyword: str = Field(description='搜索关键词'), tag: str = Field(default='', description='按标签过滤（可选）')) -> str` `mcp.tool()`
  - *Line: 66*
  - *搜索书签（按关键词或标签）*

- `def list_bookmarks(limit: int = Field(default=20, description='返回数量上限')) -> str` `mcp.tool()`
  - *Line: 87*
  - *列出所有书签*

- `def delete_bookmark(url: str = Field(description='要删除的书签 URL')) -> str` `mcp.tool()`
  - *Line: 100*
  - *删除一个书签（按 URL 匹配）*


---

`````python
"""
书签管理 MCP Server — 通过 MCP 协议提供书签增删查功能

展示如何用 FastMCP 编写一个 MCP Server，
只需一个 @mcp.tool() 装饰器即可定义工具，
schema 从函数签名 + Pydantic Field 自动生成。

配置方式（在 config.jsonc 的 mcp 节）：
  "bookmark": {
    "type": "local",
    "command": ["python", "mcp_servers/bookmark_server.py"],
    "enabled": true
  }
"""

import json
from datetime import datetime
from pathlib import Path

from pydantic import Field
from mcp.server.fastmcp import FastMCP

BOOKMARKS_FILE = Path(__file__).parent.parent / "data" / "bookmarks.json"

mcp = FastMCP("bookmark-manager")


def _load_bookmarks() -> list:
    if BOOKMARKS_FILE.exists():
        return json.loads(BOOKMARKS_FILE.read_text(encoding="utf-8"))
    return []


def _save_bookmarks(bookmarks: list):
    BOOKMARKS_FILE.parent.mkdir(parents=True, exist_ok=True)
    BOOKMARKS_FILE.write_text(
        json.dumps(bookmarks, ensure_ascii=False, indent=2), encoding="utf-8"
    )


@mcp.tool()
def add_bookmark(
    url: str = Field(description="网页 URL"),
    title: str = Field(description="书签标题"),
    tags: str = Field(default="", description="逗号分隔的标签，如 'python,教程'"),
) -> str:
    """保存一个网页书签"""
    bookmarks = _load_bookmarks()

    for bm in bookmarks:
        if bm["url"] == url:
            return f"书签已存在: {url}"

    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    bookmarks.append({
        "url": url,
        "title": title,
        "tags": tag_list,
        "created": datetime.now().isoformat(),
    })
    _save_bookmarks(bookmarks)
    return f"书签已保存: {title} ({url})"


@mcp.tool()
def search_bookmarks(
    keyword: str = Field(description="搜索关键词"),
    tag: str = Field(default="", description="按标签过滤（可选）"),
) -> str:
    """搜索书签（按关键词或标签）"""
    bookmarks = _load_bookmarks()
    kw = keyword.lower()
    results = []

    for bm in bookmarks:
        if tag and tag.lower() not in [t.lower() for t in bm.get("tags", [])]:
            continue
        if kw in bm["title"].lower() or kw in bm["url"].lower():
            results.append(bm)

    if not results:
        return f"未找到包含 '{keyword}' 的书签"
    return json.dumps(results[:20], ensure_ascii=False, indent=2)


@mcp.tool()
def list_bookmarks(
    limit: int = Field(default=20, description="返回数量上限"),
) -> str:
    """列出所有书签"""
    bookmarks = _load_bookmarks()
    if not bookmarks:
        return "暂无书签"
    display = bookmarks[-limit:]
    display.reverse()
    return json.dumps(display, ensure_ascii=False, indent=2)


@mcp.tool()
def delete_bookmark(
    url: str = Field(description="要删除的书签 URL"),
) -> str:
    """删除一个书签（按 URL 匹配）"""
    bookmarks = _load_bookmarks()
    original_count = len(bookmarks)
    bookmarks = [bm for bm in bookmarks if bm["url"] != url]
    if len(bookmarks) == original_count:
        return f"未找到书签: {url}"
    _save_bookmarks(bookmarks)
    return f"已删除书签: {url}"


if __name__ == "__main__":
    mcp.run(transport="stdio")

`````

--- **end of file: mcp_servers/bookmark_server.py** (project: nb_agent_bfzs) --- 

---


--- **start of file: mcp_servers/redis_tools_server.py** (project: nb_agent_bfzs) --- 


### 📄 Python File Metadata: `mcp_servers/redis_tools_server.py`

#### 📝 Module Docstring

`````
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
`````

#### 📦 Imports

- `import os`
- `import json`
- `import shlex`
- `from pydantic import Field`
- `from mcp.server.fastmcp import FastMCP`
- `import redis as redis_lib`
- `import datetime`

#### 🔧 Public Functions (7)

- `def redis_execute(command: str = Field(description='完整的 Redis 命令，如 "SET mykey hello EX 60" 或 "HGETALL user:1001"')) -> str` `mcp.tool()`
  - *Line: 84*
  - *执行任意 Redis 命令（FLUSHDB/FLUSHALL/SHUTDOWN 等危险命令被禁止）。*

- `def redis_info(section: str = Field(default='overview', description='信息区域: overview(精简概要) / server / clients / memory / stats / replication / keyspace / all')) -> str` `mcp.tool()`
  - *Line: 136*
  - *查看 Redis 服务器信息。*

- `def redis_keys(pattern: str = Field(default='*', description='key 匹配模式，支持 * ? [] 通配符，如 "user:*"'), limit: int = Field(default=50, description='最多返回数量（防止 key 太多卡住）'), show_details: bool = Field(default=True, description='是否显示每个 key 的类型/TTL/内存大小')) -> str` `mcp.tool()`
  - *Line: 202*
  - *按模式搜索 Redis key，可显示每个 key 的类型、TTL、大小等详情。*

- `def redis_smart_get(key: str = Field(description='Redis key 名称')) -> str` `mcp.tool()`
  - *Line: 264*
  - *智能读取 Redis key 的值，自动识别数据类型（string/hash/list/set/zset/stream）并完整展示。*

- `def redis_smart_set(key: str = Field(description='Redis key 名称'), value: str = Field(description='要写入的值。string→字符串; hash→JSON对象如{"a":"1"}; list/set→JSON数组如["a","b"]'), ttl: int = Field(default=-1, description='过期时间(秒)，-1 表示永不过期'), data_type: str = Field(default='string', description='数据类型: string / hash / list / set')) -> str` `mcp.tool()`
  - *Line: 347*
  - *智能写入 Redis key，支持多种数据类型和 TTL 设置。*

- `def redis_db_stats() -> str` `mcp.tool()`
  - *Line: 419*
  - *查看当前 Redis 数据库的全局统计：key 总数、各类型分布、内存占用等。*

- `def redis_slowlog(count: int = Field(default=10, description='显示最近几条慢查询，1-50')) -> str` `mcp.tool()`
  - *Line: 491*
  - *查看 Redis 慢查询日志，用于排查性能瓶颈。*


---

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

FORBIDDEN_COMMANDS = {
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
    for forbidden in FORBIDDEN_COMMANDS:
        if cmd_upper.startswith(forbidden):
            return f"安全限制: 禁止执行命令 {forbidden}。如确需执行，请通过 redis-cli 手动操作。"

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

--- **end of file: mcp_servers/redis_tools_server.py** (project: nb_agent_bfzs) --- 

---

# markdown content namespace: nb_agent_bfzs skills 


## nb_agent_bfzs File Tree (relative dir: `.nb_agent/skills`)


`````

└── .nb_agent
    └── skills
        ├── README.md
        ├── code-review
        │   └── SKILL.md
        ├── daily-report
        │   └── SKILL.md
        ├── explain-code
        │   └── SKILL.md
        ├── git-changelog
        │   ├── SKILL.md
        │   └── scripts
        │       └── git_log.py
        ├── meeting-notes
        │   └── SKILL.md
        ├── nbrag-workflow
        │   └── SKILL.md
        └── refactor
            └── SKILL.md

`````

---


## nb_agent_bfzs (relative dir: `.nb_agent/skills`)  Included Files (total: 9 files)


- `.nb_agent/skills/README.md`

- `.nb_agent/skills/code-review/SKILL.md`

- `.nb_agent/skills/daily-report/SKILL.md`

- `.nb_agent/skills/explain-code/SKILL.md`

- `.nb_agent/skills/git-changelog/SKILL.md`

- `.nb_agent/skills/git-changelog/scripts/git_log.py`

- `.nb_agent/skills/meeting-notes/SKILL.md`

- `.nb_agent/skills/nbrag-workflow/SKILL.md`

- `.nb_agent/skills/refactor/SKILL.md`


---


--- **start of file: .nb_agent/skills/README.md** (project: nb_agent_bfzs) --- 

`````markdown


## nb_agent_bfzs 项目文件结构注意：

1. nb_agent_bfzs 只是演示 nb_agent框架的一个项目，是为了演示使用 nb-agent框架如何扩展 提示词 skill  tool mcp，不是最终的服务某个特定功能的产品，是个演示demo大杂烩 。

2. skills 文件夹下是随意写的假的skill演示例子，不是本项目最终agent产品所需的，主要是为了演示skill的编写规则，遵循 agentskill.io 规范。

3. mcp_servers 文件夹下的mcp，不是本项目最终agent产品所需的，只是为了演示用户如何自定义定义自己的mcp，而不是只会依靠配置第三方mcp。

4. tools 文件夹下的工具函数，不是本项目最终agent产品所需的，只是为了演示用户如何在nb_agent框架中自定义tool函数，自动暴露给ai的请求协议的function字段


## 用户如何让 nb-agent 作为ai coding 来使用

可以在tui界面，点击agents按钮或者按f4，可以配置一个专属的 ai coding 智能体(但是如果你只搞编程，不精确搞10几个作用场景用途，那也可以不用专门配专门的编程agent)，在这个智能体要绑定 serena 这个mcp。

serena mcp的每个函数已经暴露了 入参和作用给ai，如果要让ai更精通serena，你还可以专门写一个skill，或者写在pomote提示词也行。

### 注意：

如果要实现编程，只需要介入 serena 这一个mcp就可以了，不要再接各种乱七八糟的mcp。 serena专门为编程而生，具备精确的 索引 读 写 执行 操作，在编程场景吊打通用的 fielsystem mcp读写。
nb-agent化身编程终端，只需要接入serena 这一个mcp就可以了，不要再另外接入其他乱七八糟的file system 和 codegraph 这些mcp。



`````

--- **end of file: .nb_agent/skills/README.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/code-review/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
---
name: code-review
description: >-
  审查代码质量、安全性和最佳实践。当用户请求代码审查、review PR、
  检查代码变更、或提到"帮我看看这段代码"时使用。
---

# 代码审查 Skill

在审查代码时，按以下流程系统性地评估变更，而不是逐行扫读。

## 审查流程

1. **理解意图**：先确认这次变更要解决什么问题，再判断实现是否匹配目标。
2. **阅读范围**：优先看 diff 和调用链，必要时扩展到相关测试与配置文件。
3. **分层检查**：按严重程度归类问题，避免把风格偏好当成缺陷。
4. **给出结论**：总结风险、阻塞项、建议项，并指出验证方式。

## 检查维度

### 正确性

- 边界条件、空值、异常路径是否处理完整
- 并发、异步、重试、幂等是否会导致竞态或重复副作用
- 类型、返回值、错误码是否与调用方约定一致

### 安全性

- 是否存在注入、路径穿越、权限绕过、敏感信息泄露
- 外部输入是否经过校验与规范化
- 密钥、token、凭据是否硬编码或写入日志

### 可维护性

- 命名是否表达意图，函数是否职责单一
- 是否存在重复逻辑，能否复用现有抽象
- 注释是否解释“为什么”，而不是复述代码

### 性能

- 是否存在 N+1 查询、无界循环、重复计算
- 热路径上是否引入不必要的 I/O 或分配
- 缓存、批处理、索引使用是否合理

### 测试

- 是否覆盖新增逻辑的主路径与失败路径
- 测试是否稳定、可读，避免依赖真实外部服务
- 回归风险高的区域是否缺少断言

## 输出格式

按以下结构回复：

```markdown
## 总结
<1-2 句话概括整体质量与是否建议合并>

## 阻塞问题
- [严重] <问题> — <位置> — <原因> — <修复建议>

## 建议改进
- [建议] <问题> — <位置> — <原因> — <修复建议>

## 亮点
- <值得保留的设计或实现>

## 测试建议
- <需要补充或执行的验证>
```

## 审查原则

- 先找真实风险，再谈风格优化
- 每个问题都要给出具体位置和可执行建议
- 没有发现问题时明确说明，并列出已检查的关键面
- 区分“必须修复”和“可以后续优化”
- 尊重项目现有约定，不强行引入新风格

`````

--- **end of file: .nb_agent/skills/code-review/SKILL.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/daily-report/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
---
name: daily-report
description: >-
  生成每日工作日报。当用户提到写日报、工作总结、daily report、
  今日工作、或要求汇总今天完成的任务时使用。
---

# 日报生成 Skill

帮用户整理今天的工作内容，生成结构化日报。

## 输出模板

使用以下模板，用 `create_note` 工具保存，tags 设为 `daily`：

```markdown
# 工作日报 — YYYY-MM-DD

## 今日完成

1. **[任务名]** — 具体描述
2. **[任务名]** — 具体描述

## 进行中

1. **[任务名]** — 进度描述，预计完成时间
   - 阻塞项（如有）：...

## 明日计划

1. [计划任务]
2. [计划任务]

## 备注

（其他需要记录的事项）
```

## 处理流程

1. 先调用 `list_notes` 查看今天已有的笔记作为参考
2. 询问用户今天完成了什么、正在做什么、明天计划做什么
3. 按模板整理，语言简洁，重点突出
4. 用 `create_note` 保存，标题格式：`日报-YYYY-MM-DD`

`````

--- **end of file: .nb_agent/skills/daily-report/SKILL.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/explain-code/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
---
name: explain-code
description: >-
  清晰解释代码结构、数据流和执行逻辑。当用户询问"这段代码做什么"、
  "帮我看看这个函数"、"解释一下这个模块"、或需要理解调用链时使用。
---

# 代码解释 Skill

在解释代码时，目标是让读者快速建立 mental model，而不是复述每一行语法。

## 解释流程

1. **定位入口**：指出用户关心的文件、函数、类或调用链起点。
2. **概括职责**：用一句话说明“这段代码是做什么的”。
3. **展开结构**：按模块、层次或执行顺序组织说明。
4. **追踪数据流**：说明输入如何变成输出，关键状态在哪里变化。
5. **点明边界**：说明依赖、副作用、失败路径和隐含假设。

## 讲解层次

### 第一层：概览

- 这段代码解决什么问题
- 在系统中的位置（入口、服务、工具、中间层等）
- 最重要的 3 个概念或组件

### 第二层：执行路径

- 正常流程分几步
- 谁调用谁，关键分支在哪里
- 异步、回调、事件、消息如何传递

### 第三层：实现细节

- 重要算法、协议、数据结构
- 非显而易见的业务规则
- 与框架/库相关的关键用法

## 输出格式

默认使用以下结构：

```markdown
## 这段代码做什么
<一句话概述>

## 核心组件
- `<组件>` — <职责>

## 执行流程
1. <步骤>
2. <步骤>

## 数据如何流动
<输入 -> 处理 -> 输出>

## 需要注意的点
- <边界条件 / 副作用 / 依赖>

## 如果想继续深入
- <可选的下一步阅读位置>
```

## 讲解原则

- 先整体后局部，先目的后实现
- 使用与源码一致的命名，避免发明新术语
- 复杂逻辑优先用步骤列表或简短伪代码
- 对初学者友好，但不牺牲准确性
- 如果上下文不足，明确说明假设，而不是猜测
- 仅在有助于理解时使用类比、表格或 ASCII 图

## 常见场景

### 解释单个函数

说明参数含义、返回值、副作用、异常和典型调用方式。

### 解释模块或文件

说明模块边界、对外 API、内部协作关系和主要扩展点。

### 解释调用链

从入口到最终结果，按时间顺序说明每一跳做了什么。

### 解释配置或框架胶水代码

重点说明“为什么需要它”以及“删掉/改错会怎样”。

`````

--- **end of file: .nb_agent/skills/explain-code/SKILL.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/git-changelog/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
---
name: git-changelog
description: >-
  生成 Git 变更日志。当用户要求生成 changelog、查看最近提交记录、
  整理版本发布说明、或总结代码变更历史时使用。
  (说明：需要用户先配置了有终端执行能力的mcp,或者用户自己写个能执行终端命令的工具函数通过@tool暴露给ai，不然没法执行python脚本。)
---

# Git 变更日志生成 Skill

根据 Git 提交历史，自动生成结构化的变更日志。

## 可用脚本

- **`scripts/git_log.py`** — 提取 Git 提交记录，输出结构化 JSON
  支持参数：`--days N`（最近 N 天）、`--since DATE`（起始日期）、`--format markdown`（直接输出 Markdown）

## 工作流程

### 1. 收集提交信息

运行脚本获取提交记录：

```bash
python3 scripts/git_log.py --days 7
```

如果用户指定了时间范围：

```bash
python3 scripts/git_log.py --since 2026-05-01
```

### 2. 分类整理

将提交按以下类别分类：

| 类别 | 说明 | Commit 关键词 |
|------|------|---------------|
| ✨ 新功能 | 新增的功能 | feat, add, new |
| 🐛 修复 | Bug 修复 | fix, bugfix, hotfix |
| ♻️ 重构 | 代码重构 | refactor, restructure |
| 📝 文档 | 文档更新 | docs, readme, comment |
| 🎨 样式 | UI/样式调整 | style, ui, css |
| ⚡ 性能 | 性能优化 | perf, optimize, speed |
| 🧪 测试 | 测试相关 | test, spec, coverage |
| 🔧 配置 | 构建/配置 | build, ci, config, chore |

### 3. 生成 Changelog

按以下格式输出：

```markdown
# Changelog

## [日期范围]

### ✨ 新功能
- 功能描述 (commit hash)

### 🐛 修复
- 修复描述 (commit hash)

### ♻️ 重构
- 重构描述 (commit hash)

...
```

### 4. 保存

使用 `create_note` 工具保存变更日志，标题格式：`Changelog-YYYY-MM-DD`，tags 设为 `changelog`。

## 注意事项

- 如果提交信息是英文的，保持英文，不要翻译
- 合并提交（Merge commit）可以跳过
- 同一功能的多个提交合并为一条记录
- 如果用户没指定时间范围，默认取最近 7 天

`````

--- **end of file: .nb_agent/skills/git-changelog/SKILL.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/git-changelog/scripts/git_log.py** (project: nb_agent_bfzs) --- 


### 📄 Python File Metadata: `.nb_agent/skills/git-changelog/scripts/git_log.py`

#### 📝 Module Docstring

`````
git_log.py — 提取 Git 提交记录并输出结构化数据

用法:
  python3 scripts/git_log.py                    # 最近 7 天
  python3 scripts/git_log.py --days 30          # 最近 30 天
  python3 scripts/git_log.py --since 2026-05-01 # 指定起始日期
  python3 scripts/git_log.py --format markdown  # 直接输出 Markdown
  python3 scripts/git_log.py --help             # 查看帮助

这个需要用户配置了有执行cmd shell能力的mcp，不然没法执行python脚本。
`````

#### 📦 Imports

- `import argparse`
- `import json`
- `import re`
- `import subprocess`
- `import sys`
- `from datetime import datetime`
- `from datetime import timedelta`

#### 🔧 Public Functions (4)

- `def classify(message: str) -> str`
  - *Line: 53*

- `def get_commits(since: str) -> list`
  - *Line: 66*

- `def to_markdown(commits: list, since: str) -> str`
  - *Line: 98*

- `def main()`
  - *Line: 122*


---

`````python
#!/usr/bin/env python3
"""
git_log.py — 提取 Git 提交记录并输出结构化数据

用法:
  python3 scripts/git_log.py                    # 最近 7 天
  python3 scripts/git_log.py --days 30          # 最近 30 天
  python3 scripts/git_log.py --since 2026-05-01 # 指定起始日期
  python3 scripts/git_log.py --format markdown  # 直接输出 Markdown
  python3 scripts/git_log.py --help             # 查看帮助

这个需要用户配置了有执行cmd shell能力的mcp，不然没法执行python脚本。
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta


CATEGORIES = {
    "feat": "✨ 新功能",
    "add": "✨ 新功能",
    "new": "✨ 新功能",
    "fix": "🐛 修复",
    "bugfix": "🐛 修复",
    "hotfix": "🐛 修复",
    "refactor": "♻️ 重构",
    "restructure": "♻️ 重构",
    "docs": "📝 文档",
    "readme": "📝 文档",
    "comment": "📝 文档",
    "style": "🎨 样式",
    "ui": "🎨 样式",
    "css": "🎨 样式",
    "perf": "⚡ 性能",
    "optimize": "⚡ 性能",
    "speed": "⚡ 性能",
    "test": "🧪 测试",
    "spec": "🧪 测试",
    "coverage": "🧪 测试",
    "build": "🔧 配置",
    "ci": "🔧 配置",
    "config": "🔧 配置",
    "chore": "🔧 配置",
}

CONVENTIONAL_RE = re.compile(r"^(\w+)(?:\(.+?\))?[!:]")


def classify(message: str) -> str:
    msg_lower = message.lower()
    m = CONVENTIONAL_RE.match(msg_lower)
    if m:
        prefix = m.group(1)
        if prefix in CATEGORIES:
            return CATEGORIES[prefix]
    for keyword, category in CATEGORIES.items():
        if keyword in msg_lower.split():
            return category
    return "📦 其他"


def get_commits(since: str) -> list:
    fmt = "--format=%H|%an|%ai|%s"
    cmd = ["git", "log", f"--since={since}", fmt, "--no-merges"]
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, check=True, encoding="utf-8"
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: git log failed: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: git not found in PATH", file=sys.stderr)
        sys.exit(1)

    commits = []
    for line in result.stdout.strip().split("\n"):
        if not line.strip():
            continue
        parts = line.split("|", 3)
        if len(parts) < 4:
            continue
        hash_val, author, date, message = parts
        commits.append({
            "hash": hash_val[:7],
            "author": author.strip(),
            "date": date.strip()[:10],
            "message": message.strip(),
            "category": classify(message),
        })
    return commits


def to_markdown(commits: list, since: str) -> str:
    grouped = {}
    for c in commits:
        grouped.setdefault(c["category"], []).append(c)

    today = datetime.now().strftime("%Y-%m-%d")
    lines = [f"# Changelog\n", f"## {since} ~ {today}\n"]

    order = [
        "✨ 新功能", "🐛 修复", "♻️ 重构", "📝 文档",
        "🎨 样式", "⚡ 性能", "🧪 测试", "🔧 配置", "📦 其他",
    ]
    for cat in order:
        items = grouped.get(cat, [])
        if not items:
            continue
        lines.append(f"### {cat}\n")
        for c in items:
            lines.append(f"- {c['message']} (`{c['hash']}` by {c['author']})")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Extract git commits and output structured changelog data"
    )
    parser.add_argument(
        "--days", type=int, default=7,
        help="Number of days to look back (default: 7)"
    )
    parser.add_argument(
        "--since", type=str, default="",
        help="Start date in YYYY-MM-DD format (overrides --days)"
    )
    parser.add_argument(
        "--format", choices=["json", "markdown"], default="json",
        help="Output format: json (default) or markdown"
    )
    args = parser.parse_args()

    if args.since:
        since = args.since
    else:
        since = (datetime.now() - timedelta(days=args.days)).strftime("%Y-%m-%d")

    commits = get_commits(since)

    if not commits:
        print(f"No commits found since {since}")
        return

    if args.format == "markdown":
        print(to_markdown(commits, since))
    else:
        output = {
            "since": since,
            "total": len(commits),
            "commits": commits,
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

`````

--- **end of file: .nb_agent/skills/git-changelog/scripts/git_log.py** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/meeting-notes/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
---
name: meeting-notes
description: >-
  生成结构化的会议纪要。当用户提到会议记录、会议纪要、meeting notes、
  或要求整理会议内容时使用。
---

# 会议纪要 Skill

将用户的会议信息整理为结构化的会议纪要。

## 输出模板

使用以下模板生成纪要，用 `create_note` 工具保存，tags 设为 `meeting`：

```markdown
# [会议主题]

**日期**: YYYY-MM-DD
**参与者**: 张三, 李四, ...
**会议时长**: X 小时

## 议题与讨论

### 1. [议题名称]
- 背景：...
- 讨论要点：...
- 结论：...

### 2. [议题名称]
...

## 待办事项

| 编号 | 任务 | 负责人 | 截止日期 |
|------|------|--------|----------|
| 1 | ... | ... | ... |

## 下次会议

- 时间：
- 预定议题：
```

## 处理流程

1. 询问用户会议的主题、参与者、讨论内容
2. 如果用户提供了录音转写文本，从中提取关键信息
3. 按模板整理输出
4. 用 `create_note` 工具保存，标题格式：`会议纪要-[主题]-[日期]`
5. 确认是否需要补充或修改

`````

--- **end of file: .nb_agent/skills/meeting-notes/SKILL.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/nbrag-workflow/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
﻿---
name: nbrag-workflow
description: >-
  使用 nbrag 知识库进行多轮智能检索。当用户询问代码实现、
  查找函数定义、理解项目结构、搜索文档内容、或提到"知识库""搜索代码"时使用。
  ai要注意，这里面的函数指的是nbrag mcp自身的函数名字，当mcp被接入其他agent时候，暴露给ai的function名字会加一些前缀，比如举个例子 nbrag_search 工具 可能会变成 mcp__my_rag__nbrag_search暴露给ai，ai要根据实际请求中的fucntion的名字为准，不要死搬硬套用这个skill中的描述的函数名。
---

# RAG 知识库检索工作流

nbrag 提供 12 个 MCP 工具，核心分三类：**发现 → 检索 → 深入**。


## 前提

- 以下 4 个工具依赖导入时的 raw cache：`nbrag_grep`、`nbrag_find_definition`、`nbrag_get_raw_file`、`nbrag_search_and_fetch`。
  - `nbrag_get_raw_file` 缺 cache 时报：`Raw file cache not found (doc_id=...). This file may have been imported before caching was enabled. Please re-import.`
  - `nbrag_search_and_fetch` 缺 cache 时报：`[{file_path}] raw cache not available`
  - `nbrag_grep` / `nbrag_find_definition` 缺 cache 时**静默返回空结果**（不报错），表现与"真的没有匹配"相同——如果怀疑是 cache 缺失，先用 `nbrag_stats` 确认 collection 存在且有 chunks。
- chunk 正文开头含注入 header（非原始源码），格式因上下文而异：
  - 模块级函数：`# [File: path] [Scope: func_name] [Sig: def func(...)] [Lines: N-M]`
  - 类体级：`# [File: path] [Scope: ClassName] [Sig: class ClassName(Base)] [Lines: N-M]`
  - 类方法：`# [File: path] [Class: class ClassName(Base)] [Method: method_name] [Sig: def method(...)] [Lines: N-M]`
  - 若无 `parent_class_sig` 回退为 `[Class: ClassName]`（无基类签名）
  - `[Sig]`、`[Lines]`、`[Class]` 部分字段可能缺失。

## 第一步：发现

```
nbrag_stats()
```

返回：所有 collection 名称、文档/chunk 数、embedding/rerank 模型、data_dir、chunk_size/chunk_overlap。
首次使用或不确定 collection 名称时先调用。已知名称可直接检索。
注意：仅 `nbrag_search` / `nbrag_search_and_fetch` 在 collection 不存在时会提示 `Available collections: [...]`，
`nbrag_grep` / `nbrag_find_definition` 不会提示（静默返回空）。

## 第二步：检索

### 策略 A：语义搜索（推荐首选）

```
nbrag_search(query="用户的问题", collection_name="xxx", top_k=5)
```

- 向量召回 + rerank 精排（rerank 需配置且召回数 > top_k 才生效，失败静默降级）
- 可选 `use_rerank=False` 禁用 rerank
- 适合自然语言提问："这个项目怎么处理并发？"
- 可选 `filter_filename="core.py"` 缩小搜索范围（仅匹配文件名，非完整路径）
- 返回每条结果包含两行：
  - 标题行：`[1/5] filename chunk:X/Y line:N-M scope:xxx doc_id:xxx dist:0.1234`
  - 路径行：`file_path: /absolute/path/to/file`
- 关键字段：`chunk:X/Y`（chunk 索引/总数）、`line:N-M`、`scope`（仅 Python）、`doc_id`、`dist`（cosine 距离，越小越相似）
- chunk preview 可能被截断（加 `...`）

### 策略 B：精确搜索（补充语义搜索）

```
nbrag_grep(keyword="UserService", collection_name="xxx")
```

- 关键词/正则匹配，搜索 raw cache 文件（非向量库）
- 适合搜索确切的类名、函数名、变量名、错误信息
- 可选：`max_results=10`（默认）、`case_sensitive=True`（默认 False）、`filter_filename="core.py"`、`context_lines=10`（默认 10）
- 返回匹配行及上下文，`>>>` 标记匹配行

### 策略 C：符号查找

```
nbrag_find_definition(symbol="get_by_id", collection_name="xxx")
```

- **Python 文件**：AST 精确解析，返回 class/function 完整定义 + class 方法签名列表。AST 解析失败（语法错误）的文件会被静默跳过。
- **非 Python 文件**：正则匹配，`symbol_type` 为 `unknown`，每个文件最多返回 1 处匹配，仅约 23 行上下文（前 3 行 + 后 20 行），非完整定义。
- 可选 `max_results=5`（默认）
- 支持 qualified name：`symbol="MyClass.__init__"`

### 策略 D：一站式检索（省一轮调用）

```
nbrag_search_and_fetch(query="...", collection_name="xxx", top_k=5)
```

- 语义搜索 + 自动抓取 top N 结果的 raw 源码（省去单独调用 `nbrag_get_raw_file`）
- 小文件（≤ 2×context_lines 行）抓全文；大文件只抓匹配位置 ±context_lines 行 excerpt
- 可选：`fetch_top_n_raw=3`（默认 3，设 0 跳过抓取）、`context_lines=100`（默认）
- 同一 `doc_id` 多次命中会合并行范围只抓取一次
- **限制**：不支持 `filter_filename`，始终启用 rerank
- 需要完整源码请再用 `nbrag_get_raw_file`

## 第三步：深入

检索结果通常是代码片段（chunk），需要更多上下文时选择：

| 工具 | 特点 | 适用场景 |
|------|------|---------|
| `nbrag_get_raw_file` | 无 overlap 的干净源码，无 scope | 看完整文件或指定行号范围 |
| `nbrag_get_file_chunks` | 有 scope 元数据，chunk 间有 200 字符 overlap | 分页浏览 + 了解作用域 |
| `nbrag_get_adjacent_chunks` | 有 scope，有 overlap | 扩展搜索结果的上下文 |
| `nbrag_get_chunks_by_lines` | 有 scope，有 overlap | 按行号精确取 chunk |

### 看原始文件

```
nbrag_get_raw_file(file_path="从搜索结果获取", collection_name="xxx")
```

- 支持 `line_start` / `line_end` 指定范围（1-based），默认 -1 表示读全文
- 大文件返回后会提示 `(N lines remaining, use line_start=... to continue)`
- `file_path` 也可只传文件名（如 `"core.py"`）

### 看相邻代码块

```
nbrag_get_adjacent_chunks(doc_id="从搜索结果获取", chunk_index=3, collection_name="xxx", window=3)
```

- `chunk_index` 从搜索结果的 `chunk:X/Y` 中取 X
- `window` 默认 3，返回 chunk_index ± 3（最多 7 个 chunk）

### 按行号获取

```
nbrag_get_chunks_by_lines(doc_id="...", line_start=50, line_end=100, collection_name="xxx")
```

### 分页浏览文件

```
nbrag_get_file_chunks(file_path="...", collection_name="xxx", start_chunk=0, max_chunks=10)
```

- 与 `nbrag_get_raw_file` 的区别：有 scope 元数据 + chunk 间有 overlap，适合需要作用域信息的场景

## 推荐调用顺序

```
nbrag_stats()                          # 1. 发现知识库
    ↓
nbrag_search() / nbrag_grep()            # 2. 检索（可多次、换策略）
    ↓                                # 快捷路径：直接 nbrag_search_and_fetch() 一步到位
nbrag_find_definition()                # 3. 需要完整 class/function 定义时（Python 最佳）
    ↓
nbrag_get_raw_file()                   # 4. 看完整源码（无 overlap，无 scope）
或 nbrag_get_adjacent_chunks()          #    或扩展上下文（有 scope）
或 nbrag_get_chunks_by_lines()          #    或按行号取 chunk（有 scope）
或 nbrag_get_file_chunks()              #    或分页浏览全文件 chunks（有 scope）
    ↓
跨文件追踪：遇到未知符号 → 重复 2-4
```

## 多轮检索策略

如果第一轮搜索结果不理想：

1. **换关键词**：用同义词或更具体/更宽泛的词重新 `nbrag_search`
2. **换策略**：语义搜索不行就试 `nbrag_grep` 精确搜索
3. **缩小范围**：用 `filter_filename` 限定文件（仅 `nbrag_search` / `nbrag_grep` 支持）
4. **查定义**：找到了引用但不知道定义在哪 → `nbrag_find_definition`
5. **跨 collection**：不同知识库可能有不同内容

## 常见错误处理

### Collection 不存在

| 工具 | 返回信息 |
|------|---------|
| `nbrag_search` / `nbrag_search_and_fetch` | `collection 'xxx' does not exist. Available collections: [...] Use nbrag_add_document to create and import docs.` |
| `nbrag_grep` / `nbrag_find_definition` | **静默返回空**（与"无匹配"不可区分） |

→ 建议：用 `nbrag_stats()` 确认 collection 名称。

### Collection 为空

| 工具 | 返回信息 |
|------|---------|
| `nbrag_search` / `nbrag_search_and_fetch` | `collection 'xxx' is empty. Use nbrag_add_document to import docs first.` |

### Raw cache 缺失

| 工具 | 返回信息 |
|------|---------|
| `nbrag_get_raw_file` | `Raw file cache not found (doc_id=...). This file may have been imported before caching was enabled. Please re-import.` |
| `nbrag_search_and_fetch` | `[{file_path}] raw cache not available` |
| `nbrag_grep` / `nbrag_find_definition` | **静默返回空** |

→ 建议：重新导入该文件/目录。

### 其他常见错误

| 返回信息 | 含义 | 建议动作 |
|----------|------|---------|
| `No results (collection has N chunks, filter: xxx)` | 搜索无匹配 | 换关键词或去掉 filter |
| `No definition found ... Try nbrag_grep` | 符号未找到（或 AST 解析失败） | 用 `nbrag_grep` 扩大搜索 |
| `File not found: 'xxx'` | 文件路径或文件名不存在 | 检查路径是否正确 |
| `Document not found: 'xxx'` | 文档 ID 不存在 | 用 `nbrag_list` 查看有效 doc_id |
| `No chunks matching line range ...` | 行号范围内无 chunk | 调整行号或用 `nbrag_get_raw_file` |
| `[path] excerpt failed` | 自动抓取源码失败 | 改用 `nbrag_get_raw_file` 手动抓取 |

## 不需要 AI 调用的工具

以下工具通常由用户手动操作：

- `nbrag_add_document` — 知识库导入（人工一次性批量操作）
- `nbrag_delete` — 删除文档
- `nbrag_list` — 列出文档（除非用户明确要求）

`````

--- **end of file: .nb_agent/skills/nbrag-workflow/SKILL.md** (project: nb_agent_bfzs) --- 

---


--- **start of file: .nb_agent/skills/refactor/SKILL.md** (project: nb_agent_bfzs) --- 

`````markdown
---
name: refactor
description: >-
  安全地重构代码，保持行为不变并降低复杂度。当用户请求重构、
  优化代码结构、消除重复、简化复杂逻辑、或提到"帮我整理一下代码"时使用。
---

# 代码重构 Skill

重构的目标是在不改变外部行为的前提下，提高可读性、可测试性和可维护性。

## 重构流程

1. **确认行为基线**：明确当前功能、公共 API、边界条件与现有测试覆盖。
2. **识别坏味道**：重复、过长函数、深层嵌套、隐式依赖、命名误导等。
3. **选择最小步骤**：每次只做一种重构，便于 review 和回滚。
4. **保持测试绿**：每步完成后运行相关测试；没有测试时先补关键路径测试。
5. **验证等价性**：确认输入输出、副作用、错误处理与重构前一致。

## 适用重构手法

### 结构整理

- 提取函数 / 提取变量
- 内联过度抽象的薄封装
- 拆分大类，按职责划分子模块
- 用早返回减少嵌套

### 依赖治理

- 依赖注入替代硬编码全局状态
- 收敛重复配置与 magic number
- 将副作用与纯逻辑分离

### 接口稳定

- 优先保留现有公共 API
- 必须变更时提供过渡层或明确迁移说明
- 不在同一提交里混入无关功能改动

## 实施原则

- **小步提交**：一个重构意图对应一组清晰变更
- **行为优先**：先保证正确，再追求优雅
- **测试先行或测试同行**：没有安全网时不要大改
- **匹配项目风格**：沿用现有命名、目录结构和抽象层级
- **避免过度设计**：不为假想未来引入复杂框架

## 输出格式

重构前先给出计划：

```markdown
## 重构目标
<想改善什么问题>

## 当前问题
- <坏味道 / 风险>

## 计划步骤
1. <小步变更>
2. <小步变更>

## 风险与验证
- 风险: <可能影响的区域>
- 验证: <要运行的测试或检查>
```

重构完成后总结：

```markdown
## 已完成变更
- <具体改动>

## 行为是否保持不变
<是/否，以及依据>

## 后续建议
- <可选的下一步重构>
```

## 禁止事项

- 不要同时做重构和功能开发
- 不要在没有理解调用方的情况下修改公共接口
- 不要删除看起来“多余”的代码，除非确认无引用且无运行时依赖
- 不要为了“更短”牺牲可读性
- 不要引入与项目无关的新依赖

## 何时停止

- 代码已经清晰、测试通过、review 可理解
- 进一步抽象不会明显降低复杂度
- 剩余问题属于产品需求变更，而不是重构范围

`````

--- **end of file: .nb_agent/skills/refactor/SKILL.md** (project: nb_agent_bfzs) --- 

---

# markdown content namespace: nb_agent_bfzs root files 


## nb_agent_bfzs File Tree (relative dir: `.`)


`````

├── approval_rules.py
├── config.jsonc
├── main.py
└── nb_log_config.py

`````

---


## nb_agent_bfzs (relative dir: `.`)  Included Files (total: 4 files)


- `main.py`

- `approval_rules.py`

- `config.jsonc`

- `nb_log_config.py`


---


--- **start of file: main.py** (project: nb_agent_bfzs) --- 

`````python
"""
nb_agent_bfzs — 智能笔记助手（nb_agent 演示项目）

只需几行代码，就拥有自己的 AI Agent + 终端 TUI：

  1. pip install nb_agent
  2. 在 tools/ 下用 @tool 定义工具
  3. 在 .nb_agent/skills/ 下放 SKILL.md
  4. 在 config.jsonc 里配置模型和 MCP
  5. python main.py
"""

import tools  # noqa: F401  导入即注册自定义工具
from approval_rules import ALL_RULES
from nb_agent import load_config, AgentApp

config = load_config()
app = AgentApp(config)

for rule in ALL_RULES: # 注册自定义审批规则（Redis 写命令弹窗确认、危险工具黑名单等）
    app.agent.approval_engine.add_rule(rule)

app.run()


# powershell
# cd D:/codes/nb_agent_bfzs;$env:PYTHONPATH = "D:/codes/nb_agent_bfzs";D:\ProgramData\Miniconda3\envs\py312\python.exe main.py

`````

--- **end of file: main.py** (project: nb_agent_bfzs) --- 

---


--- **start of file: approval_rules.py** (project: nb_agent_bfzs) --- 

`````python
"""
自定义审批规则 — 演示 nb_agent 的工具调用审批机制

nb_agent 的 ApprovalEngine 支持用户注入自定义规则函数:
  - 规则签名: (tool_name: str, tool_kwargs: dict) -> bool
  - 返回 True → 弹窗让用户确认后才执行
  - 返回 False → 放行（不弹窗）
  - 多条规则按顺序检查，任一命中即触发审批

工具名格式:
  - 本地 @tool:          函数名，如 "delete_note"
  - MCP 工具:   mcp__{config 中的 key}__{函数名}，如 "mcp__redis-tools__redis_execute"
"""

# ── Redis 写命令集 ──────────────────────────────
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

# ── 始终需要审批的工具黑名单 ──────────────────────
# 工具名格式:
#   - 本地 @tool(group="xxx"):  {group}__{函数名}，如 "note__delete_note"
#   - 本地 @tool():              直接函数名，如 "get_current_time"
#   - MCP 工具:                  mcp__{config key}__{函数名}，如 "mcp__redis-tools__redis_execute"
ALWAYS_APPROVE_TOOLS = {
    "mcp__redis-tools__redis_smart_set",
    "note__delete_note",
}


# ── 规则函数 ────────────────────────────────────

def rule_redis_write(tool_name: str, tool_kwargs: dict) -> bool:
    """Redis redis_execute 中的写命令需要审批，只读命令（GET/HGETALL/INFO）放行"""
    if tool_name != "mcp__redis-tools__redis_execute":
        return False
    cmd_parts = tool_kwargs.get("command", "").strip().split()
    if not cmd_parts:
        return False
    return cmd_parts[0].upper() in REDIS_WRITE_COMMANDS


def rule_dangerous_tools(tool_name: str, tool_kwargs: dict) -> bool:
    """黑名单中的工具始终需要审批"""
    return tool_name in ALWAYS_APPROVE_TOOLS


def rule_note_delete(tool_name: str, tool_kwargs: dict) -> bool:
    """删除笔记操作需要审批"""
    return tool_name == "note__delete_note"


# ── 导出规则列表（main.py 中注册到 ApprovalEngine）──
ALL_RULES = [
    rule_redis_write,
    rule_dangerous_tools,
    rule_note_delete,
]

`````

--- **end of file: approval_rules.py** (project: nb_agent_bfzs) --- 

---


--- **start of file: config.jsonc** (project: nb_agent_bfzs) --- 

`````text
{
    // ===== nb_agent_bfzs — 智能笔记助手配置 =====

    "agent": {
        "system_prompt": "你是一个智能笔记助手。你可以帮用户创建笔记、搜索笔记、统计项目信息。\n当用户需要写会议纪要或日报时，请先查看对应的 Skill 指南。\n请用中文回答。",
        "default_model": "deepseek-chat",
        "streaming": true
    },

    // LLM 提供商配置（以下选一个，或自行替换）
     "provider": {
        "litellm": {
            "name": "LiteLLM Proxy",
            "base_url": "http://localhost:4000/v1",
            "api_key": "not-needed",
            "models": {
                "ds-deepseek-v4-flash": {
                    "name": "DeepSeek V4 Flash (官方直连)",
                    "limit": { "context": 1000000, "output": 384000 }
                },
                "ds-deepseek-v4-pro": {
                    "name": "DeepSeek V4 Pro (官方直连)",
                    "limit": { "context": 1000000, "output": 384000 }
                },
                 "ds-deepseek-v4-flash-200k": {
                    "name": "DeepSeek V4 Flash (官方直连)",
                    "limit": { "context": 200000, "output": 64000 },
                    "raw_model": "ds-deepseek-v4-flash"
                },
                "ds-deepseek-v4-pro-200k": {
                    "name": "DeepSeek V4 Pro (官方直连)",
                    "limit": { "context": 200000, "output": 64000 },
                    "raw_model": "ds-deepseek-v4-pro"
                },
                "com-qwen3.5-397b": {
                    "name": "Qwen3.5 397B (公司)",
                    "limit": { "context": 131072, "output": 65536 }
                },
                "com-qwen3.6-35b": {
                    "name": "Qwen3.6 35B (公司)",
                    "limit": { "context": 131072, "output": 65536 }
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
                },
                  "ark-deepseek-v4-flash-200k": {
                    "name": "DeepSeek V4 Flash (方舟)",
                    "limit": { "context": 200000, "output": 64000 },
                    "raw_model": "ark-deepseek-v4-flash"
                },
                "ark-deepseek-v4-pro-200k": {
                    "name": "DeepSeek V4 Pro (方舟)",
                    "limit": { "context": 200000, "output": 64000 },
                    "raw_model": "ark-deepseek-v4-pro"
                },
            }
        }
    },


    // MCP Server 配置
    "mcp": {
        // 书签管理 MCP（本地 stdio 方式） ,这个是演示启动用户自己开发的mcp
        "bookmark": {
            "type": "local",
            "command": ["D:/ProgramData/Miniconda3/envs/py312/python.exe", "mcp_servers/bookmark_server.py"],
            "enabled": true
        },



        // Redis 工具 MCP（本地 stdio 方式）,这个是演示启动用户自己开发的mcp，并且演示了如何审批执行redis命令，nb_agent的tui会弹窗给用户确认是否需要继续执行。
        // 连接配置: 环境变量 REDIS_URL 或 REDIS_HOST/REDIS_PORT/REDIS_PASSWORD/REDIS_DB
        "redis-tools": {
            "type": "local",
            "command": ["python", "mcp_servers/redis_tools_server.py"],
            "enabled": true
        },

        // 实时网页搜索 MCP（SSE 方式）
        // Open Web Search（多引擎搜索 + 文章抓取，Docker 部署）
        // 启动: docker run -d --name web-search -p 3000:3000 -e ENABLE_CORS=true -e CORS_ORIGIN=* ghcr.io/aas-ee/open-web-search:latest
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
            "command": ["npx",
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "D:/codes/nb_agent_bfzs"
            ]
        },
        // 用户可以先独立方式启动nbrag mcp web服务， 也可以使用local模式启动
         "nbrag": {
            "type": "http",    
            "url": "http://localhost:9101/mcp"
        },
        "context7": {
            "type": "local",
            "command": ["npx", "-y", "@upstash/context7-mcp@latest"],
            "enabled": true
        },
        "serena": {
            "type": "local",
            "command": ["C:/Users/ydf6/.local/bin/serena.exe", "start-mcp-server", "--project", "D:/codes/nb_agent"],
            "enabled": true
        }

    },

    // 审批规则（更多更自由灵活的自定义规则见 approval_rules.py，代码比配置的表达能力更灵活强大）
    "approval": {
        "dangerous_tools": ["note__delete_note", "mcp__redis-tools__redis_smart_set"],
        "auto_approve": false
    },

    // 会话存储
    "session": {
        "db_path": ""  // 空 = 默认 ~/.nb_agent/sessions.db
    },

    "ui": {
        "theme": "dark",
        "show_tool_panel": true,
        "show_token_usage": true
    }
}

`````

--- **end of file: config.jsonc** (project: nb_agent_bfzs) --- 

---


--- **start of file: nb_log_config.py** (project: nb_agent_bfzs) --- 

`````python
# coding=utf8
"""
This file nb_log_config.py is auto-generated into the root directory of the Python project (at sys.path[1]).
Variables defined here will override the values in nb_log_config_default. This serves as the default configuration for nb_log.
Users do not need to modify the config file inside the nb_log package installation directory.

The final configuration is determined by the parameters passed to get_logger_and_add_handlers().
If a parameter is None, the value defined here will be used.
"""

"""
To disable colored log output, set DEFAULUT_USE_COLOR_HANDLER = False
To disable block background colors in console, set DISPLAY_BACKGROUD_COLOR_IN_CONSOLE = False
To suppress the PyCharm color settings hint, set WARNING_PYCHARM_COLOR_SETINGS = False
To change the log format template, set FORMATTER_KIND (7 built-in templates available, or add custom ones)
LOG_PATH sets the directory for log file storage.
"""
import sys
# noinspection PyUnresolvedReferences
import logging
import os
# noinspection PyUnresolvedReferences
from pathlib import Path  # noqa
import socket
from pythonjsonlogger.jsonlogger import JsonFormatter

def judge_has_set_pythonpath() -> bool:
    """
    Judge whether PYTHONPATH is set.
    :return:
    """
    try:
        sys_path1_parent2 = Path(sys.path[1]).parents[2]
        if sys_path1_parent2 == Path(sys.executable).parents[2]:
            return False
        else:
            return True
    except IndexError:
        return True

def aut_get_proj_name() -> str:
    """
    Automatically determine the project name from the sys.path[1] directory.
    :return:
    """
    if judge_has_set_pythonpath() is False:
        """
         # For example /home/ydfwsl/miniconda3/lib/python37.zip, this usually happens because PYTHONPATH is not set to the project root directory.
         1. PyCharm IDE automatically adds the opened project root directory to PYTHONPATH.

         2. In VSCode, users should set the following in settings.json:
              {
                "python.analysis.extraPaths": ["${workspaceFolder}"],
                "terminal.integrated.env.windows": { "PYTHONPATH": "${workspaceFolder};${env:PYTHONPATH}" },
                "terminal.integrated.env.osx": { "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}" },
                "terminal.integrated.env.linux": { "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}" }
              }

         3. If manually starting Python scripts in cmd, PowerShell, or Linux, you need to manually set PYTHONPATH to the project root directory.
            Simply cd into the project root directory first, then execute the corresponding command:
            CMD: set PYTHONPATH=%cd%
            PowerShell: $env:PYTHONPATH = $PWD.Path
            Linux/macOS: export PYTHONPATH=$PWD

        """
        return 'no_proj_name'
    else:
        return Path(sys.path[1]).name 

# PRINT_WRTIE_FILE_NAME is an advanced feature unique to nb_log, beyond the scope of typical logging packages.
# Controls whether print output is automatically written to a file. Set to None to disable. A new file is created daily (e.g. 2023-06-30.my_proj.print) in LOG_PATH.
# If you set the environment variable PRINT_WRTIE_FILE_NAME (e.g. export PRINT_WRTIE_FILE_NAME="my_proj.print"), it takes priority over the value in nb_log_config.py.
PRINT_WRTIE_FILE_NAME = None
SYS_STD_FILE_NAME = None

USE_BULK_STDOUT_ON_WINDOWS = False  # Whether to batch stdout every 0.1s on Windows (Windows I/O performance is poor)

DEFAULUT_USE_COLOR_HANDLER = True  # Whether to use colored log output by default.
DEFAULUT_IS_USE_LOGURU_STREAM_HANDLER = False  # Whether to use loguru's console handler instead of nb_log's ColorHandler by default.
DISPLAY_BACKGROUD_COLOR_IN_CONSOLE = True  # Whether to display block background colors in console logs. Set to False to disable background colors.
AUTO_PATCH_PRINT = False              # nb_agent TUI 必需：禁止 monkey patch print
SHOW_PYCHARM_COLOR_SETINGS = False    # TUI 模式不需要 PyCharm 提示
SHOW_NB_LOG_LOGO = False              # TUI 模式不需要 logo
SHOW_IMPORT_NB_LOG_CONFIG_PATH = False  # TUI 模式不需要路径提示

WHITE_COLOR_CODE = 37  # Different PyCharm versions/themes use different codes for white (37 or 97). Adjust based on your PyCharm console color settings.

DEFAULT_ADD_MULTIPROCESSING_SAFE_ROATING_FILE_HANDLER = False  # Whether to automatically write logs to a file even when log_filename is not specified (auto-generates namespace.log).
AUTO_WRITE_ERROR_LEVEL_TO_SEPARATE_FILE = False  # Automatically write ERROR level and above to a separate file, with filename auto-generated from log_filename.
LOG_FILE_SIZE = 1000  # Max size per log file in MB. Files are rotated when this size is exceeded.
LOG_FILE_BACKUP_COUNT = 10  # Max number of backup files to keep per log file. Older backups are deleted.

LOG_PATH = os.getenv("LOG_PATH")  # Priority: read from environment variable first (e.g. export LOG_PATH='/your/log/dir/')
if not LOG_PATH:
    LOG_PATH = '/pythonlogs'  # Default log directory, located at the root of the drive where the project resides.
    # LOG_PATH = Path(__file__).absolute().parent / Path("pythonlogs")   # This would create a pythonlogs folder in the project root.
    if os.name == 'posix':  # Non-root Linux/Mac users don't have write access to /pythonlogs, so default to ~/pythonlogs instead.
        home_path = os.environ.get("HOME", '/')  # Gets the current user's home directory on Linux/Mac
        LOG_PATH = Path(home_path) / Path('pythonlogs')  # Linux/Mac permissions are strict; non-root users can't write to /pythonlogs.
# print('LOG_PATH:',LOG_PATH)

LOG_FILE_HANDLER_TYPE = 6  # 1 2 3 4 5 6 7   # nb_log file rotation - all options are multi-process safe.
"""
LOG_FILE_HANDLER_TYPE can be set to one of the following values:
1 - Multi-process safe size-based rotation with batch writing to reduce file lock operations.
    In tests with 10 processes, performance is 100x better than type 5 on Windows, 5x better on Linux.
2 - Multi-process safe daily rotation. A new log file is created each day with a date suffix.
3 - Single file without rotation (no rotation means no multi-process safety concerns).
4 - WatchedFileHandler (Linux only). Relies on external logrotate for file rotation. Multi-process safe.
5 - Third-party concurrent_log_handler.ConcurrentRotatingFileHandler for size-based rotation.
    Uses file locks (fcntl on Linux, win32con on Windows). Performance on Windows is very poor.
    For size-based rotation, type 1 is recommended over type 5.
6 - BothDayAndSizeRotatingFileHandler. Custom implementation that rotates by both time and size.
    Files are rotated whenever either the size or time threshold is reached.
7 - LoguruFileHandler. Uses the well-known loguru package's file handler for writing logs.
"""

LOG_LEVEL_FILTER = logging.DEBUG  # Default log level when not specified in get_logger(). Logs below this level are ignored (e.g. if set to INFO, debug logs are suppressed).
# It is strongly discouraged to raise this globally to INFO. Use logger namespaces to adjust levels for verbose loggers individually.
# See https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c9.html#id2 for details on logger namespace usage.

ROOT_LOGGER_LEVEL = logging.INFO  # Log level for the root logger namespace. If INFO, all unhandled loggers will capture INFO and above.
ROOT_LOGGER_FILENAME = 'root.log'  # Filename for root logger logs. Set to None to disable file logging for root.
ROOT_LOGGER_FILENAME_ERROR = 'root.error.log'  # Separate filename for ERROR level and above from root logger. Set to None to disable.

# Filter console output by keywords. If a message contains any string in this list, it will be suppressed.
# This applies to both print and logger console output. Useful for filtering verbose prints from third-party packages.
# Avoid adding too many entries as it may slightly affect performance.
FILTER_WORDS_PRINT = []  # e.g. FILTER_WORDS_PRINT = ['noisy_module', 'verbose_warning'] to suppress messages containing these strings.


def get_host_ip():
    ip = ''
    host_name = ''
    # noinspection PyBroadException
    try:
        sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sc.connect(('8.8.8.8', 80))
        ip = sc.getsockname()[0]
        host_name = socket.gethostname()
        sc.close()
    except Exception:
        pass
    return ip, host_name


computer_ip, computer_name = get_host_ip()


class JsonFormatterJumpAble(JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        # log_record['jump_click']   = f"""File '{record.__dict__.get('pathname')}', line {record.__dict__.get('lineno')}"""
        log_record[f"{record.__dict__.get('pathname')}:{record.__dict__.get('lineno')}"] = ''  # Add a clickable jump-to-source field.
        log_record['ip'] = computer_ip
        log_record['host_name'] = computer_name
        super().add_fields(log_record, record, message_dict)
        if 'for_segmentation_color' in log_record:
            del log_record['for_segmentation_color']


DING_TALK_TOKEN = '3dd0eexxxxxadab014bd604XXXXXXXXXXXX'  # DingTalk alert bot token

EMAIL_HOST = ('smtp.sohu.com', 465)
EMAIL_FROMADDR = 'aaa0509@sohu.com'  # 'matafyhotel-techl@matafy.com',
EMAIL_TOADDRS = ('cccc.cheng@silknets.com', 'yan@dingtalk.com',)
EMAIL_CREDENTIALS = ('aaa0509@sohu.com', 'abcdefg')

ELASTIC_HOST = '127.0.0.1'
ELASTIC_PORT = 9200

KAFKA_BOOTSTRAP_SERVERS = ['192.168.199.202:9092']
ALWAYS_ADD_KAFKA_HANDLER_IN_TEST_ENVIRONENT = False

MONGO_URL = 'mongodb://myUserAdmin:mimamiama@127.0.0.1:27016/admin'

RUN_ENV = 'test'

FORMATTER_DICT = {
    1: logging.Formatter(
        'Time[%(asctime)s] - Logger[%(name)s] - File[%(filename)s] - Line[%(lineno)d] - Level[%(levelname)s] - Message[%(message)s]',
        "%Y-%m-%d %H:%M:%S"),
    2: logging.Formatter(
        '%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),
    3: logging.Formatter(
        '%(asctime)s - %(name)s - [ File "%(pathname)s", line %(lineno)d, in %(funcName)s ] - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),  # Traceback-style template with clickable file path
    4: logging.Formatter(
        '%(asctime)s - %(name)s - "%(filename)s" - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s -               File "%(pathname)s", line %(lineno)d ',
        "%Y-%m-%d %H:%M:%S"),  # Also supports clickable log navigation
    5: logging.Formatter(
        '%(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),  # Recommended template
    6: logging.Formatter('%(name)s - %(asctime)-15s - %(filename)s - %(lineno)d - %(levelname)s: %(message)s',
                         "%Y-%m-%d %H:%M:%S"),
    7: logging.Formatter('%(asctime)s - %(name)s - "%(filename)s:%(lineno)d" - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"),  # Short filename with line number

    8: JsonFormatterJumpAble('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s %(lineno)d  %(process)d %(thread)d', "%Y-%m-%d %H:%M:%S.%f",
                             json_ensure_ascii=False),  # JSON format, ideal for ELK stack ingestion and analysis.

    9: logging.Formatter(
        '[p%(process)d_t%(thread)d] %(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),  # Enhanced template 5 with process and thread info.
    10: logging.Formatter(
        '[p%(process)d_t%(thread)d] %(asctime)s - %(name)s - "%(filename)s:%(lineno)d" - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"),  # Enhanced template 7 with process and thread info.
    11: logging.Formatter(
        f'%(asctime)s-({computer_ip},{computer_name})-[p%(process)d_t%(thread)d] - %(name)s - "%(filename)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"),  # Enhanced template 7 with process, thread, IP, and hostname.
}

FORMATTER_KIND = 5  # Default formatter template index when not specified in get_logger()

`````

--- **end of file: nb_log_config.py** (project: nb_agent_bfzs) --- 

---

