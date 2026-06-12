
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **系统指令**：你正在解析一份由工具 **`nb_ai_context`** 自动生成的**结构化项目快照**。
> **文档性质**：这**不是**一份普通的文档，而是专为 AI 大模型（LLM）设计的上下文数据流。它将项目文档、源代码和 AST 架构元数据进行了特殊的结构化合并。

## 🧠 AI 认知与解析准则

这份由 `nb_ai_context` 生成的文档是你的核心知识库。其中的内容是动态的——它可能包含完整的底层源码，也可能仅包含使用教程，或者是两者的混合。请遵循以下自适应阅读策略：

### 1. 信息的层级与互补
*   **文档即意图**：将 `README`、教程文档和 Docstrings 视为项目设计的**最高意图**。如果文档中详细描述了某个功能的用法，即使生成器没有包含其对应的源码实现，也请完全信任文档中的逻辑，并以此为基础进行回答。
*   **源码即事实**：当遇到 `.py` 源码或 AST 元数据（类/函数签名）时，请以此作为实现细节、类型约束和语法准确性的**事实标准**。
*   **缺失内容的推断**：如果教程演示了调用 `API.process()`，但本文档未包含 `API` 类的源码，**请勿认为该功能不存在**。你应该基于教程中的演示，合理推断该接口的输入输出和行为模式，并据此协助用户。

### 2. 文件边界与架构感知
*   **上下文定界**：`nb_ai_context` 使用以下标记严格界定文件内容：
    `--- **start of file: <路径>** ---` ... 内容 ... `--- **end of file: <路径>** ---`
*   **结构可视化**：请利用“文件树 (File Tree)”章节来建立项目的宏观架构认知，即便某些文件未被展开显示。
*   **依赖关系**：利用工具生成的“文件依赖分析”章节来理解模块间的引用关系，这有助于你在只有部分代码的情况下理清数据流向。

### 3. 代码生成与交互
*   **风格一致性**：在生成代码或解释逻辑时，请严格模仿文档中已有的代码风格和命名规范。
*   **元数据利用**：对于仅展示 AST 元数据（如仅有类定义而无函数体）的 Python 文件，请将其视为有效的接口定义，确保你的代码调用符合这些签名约束。
*   **事实锚定 (Fact Anchoring)**：生成代码时必须严格**锚定**在本文档提供的范围内。
    *   涉及 API 调用时，必须基于**源码中的 AST 签名**或**教程中的演示示例**。
    *   **严禁臆造**文档中既未定义、也未在教程中提及的类名、方法名或参数。确保每一个生成的 Token 都有文档依据。

---
# markdown content namespace: nb_cmd project summary 



- `nb_cmd` is a powerful cron library for Python.
- `NbCron(...)` is the main class to create a cron object. 


## 📋 nb_cmd most core source files metadata (Entry Points)


以下是项目 nb_cmd 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nb_cmd most core source code files as follows: 
- `nb_cmd/__init__.py`
- `nb_cmd/core/base.py`
- `nb_cmd/core/meta.py`
- `nb_cmd/ui/helper.py`


### 📄 Python File Metadata: `nb_cmd/__init__.py`

#### 📝 Module Docstring

`````
nb_cmd — Python 码农的低代码平台
写一个 class，自动获得六种能力：Python 直接调用 + CLI + REST API + Web UI + TUI 终端交互 + Markdown 文档。

用法::

    from nb_cmd import NbCmd

    class MyTool(NbCmd):
        def greet(self, name: str, times: int = 1):
            for _ in range(times):
                print('你好, {}!'.format(name))

    if __name__ == '__main__':
        MyTool().run()
`````

#### 📦 Imports

- `from core.base import NbCmd`
- `from core.meta import NbCmdMeta`
- `from core.arg import Annotated`
- `from core.arg import Param`
- `from ui.helper import UIHelper`
- `from ui.helper import cmdui`
- `from utils.validators import validate`
- `from core.gen_cmd import CmdGen`
- `from core.gen_skill import SkillGen`


---




### 📄 Python File Metadata: `nb_cmd/core/base.py`

#### 📝 Module Docstring

`````
NbCmd 基类 —— 所有命令行工具的父类。
`````

#### 📦 Imports

- `from __future__ import annotations`
- `import logging`
- `import sys`
- `from meta import NbCmdMeta`
- `from typing import Annotated`
- `import subprocess`
- `from modes.cli_mode import run_cli`
- `from modes.web_mode import start_web_server`
- `from modes.tui_mode import start_tui`
- `from typing_extensions import Annotated`
- `from parser import print_full_help`
- `from parser import print_easy_help`
- `from parser import print_full_help`
- `import nb_log`

#### 🏛️ Classes (1)

##### 📌 `class NbCmd(object)`
*Line: 21*

**Docstring:**
`````
NbCmd 基类 —— 所有命令行工具的父类。

用法:
    1. 继承 NbCmd
    2. 定义公有方法（自动成为子命令）
    3. 调用 .run() 启动

功能:
    - 公有方法 → 子命令
    - 方法签名 → 参数自动推导
    - 六种能力：Python 直接调用 / CLI / REST API / Web UI / TUI 终端交互 / Markdown 文档
    - 支持 OOP 继承覆写
    - 支持多层级子命令（sub_commands）
    - 支持 nbctx 跨层级上下文传递

工具方法通过 cmdui 模块级单例访问（from nb_cmd import cmdui）:
    cmdui.table()  cmdui.kv()  cmdui.tree()  cmdui.json_print()
    cmdui.success() cmdui.warning() cmdui.error() cmdui.info()
    cmdui.progress() cmdui.confirm() cmdui.prompt() cmdui.select()
`````

**Public Methods (7):**
- `def make_nbctx(self)`
  - **Docstring:**
  `````
  模板方法：创建跨层级共享的上下文对象。
  
  覆写此方法以返回一个 dataclass 实例，框架会自动将其传递给
  所有子命令组的 self.nbctx。
  
  用法::
  
      @dataclass
      class AppCtx:
          region: str = 'beijing'
          env: str = 'prod'
  
      class MyApp(NbCmd):
          def __init__(self, region='beijing', env='prod'):
              self.region = region
              self.env = env
  
          def make_nbctx(self):
              return AppCtx(region=self.region, env=self.env)
  
  Returns
  -------
  object or None
      上下文对象，返回 None 表示不启用 nbctx。
  `````
- `def before_run(self)`
  - *所有子命令执行前的钩子，子类可覆写*
- `def after_run(self)`
  - *所有子命令执行后的钩子，子类可覆写*
- `def on_error(self, command, error)`
  - *子命令执行出错时的钩子，子类可覆写*
- `def shell(self, cmd, capture = False, check = False)`
  - **Docstring:**
  `````
  执行系统命令。
  
  Parameters
  ----------
  cmd : str  要执行的命令
  capture : bool  是否捕获输出（True 返回 stdout 字符串，False 通过 print 输出）
  check : bool  命令失败时是否抛出异常
  
  Returns
  -------
  str (capture=True 时返回 stdout) 或 None
  `````
- `def exec(self, cmd: Annotated[str, '要执行的系统命令', 'c'])`
  - *执行任意系统命令*
- `def run(self, args = None)`
  - **Docstring:**
  `````
  主入口方法。根据参数决定运行模式。
  
  Parameters
  ----------
  args : list, optional
      命令行参数列表，默认使用 sys.argv[1:]
  `````

**Properties (1):**
- `@property logger -> logging.Logger`

**Class Variables (4):**
- `sub_commands = {}`
- `Meta = NbCmdMeta`
- `nbctx = None`
- `_HELP_HANDLED = object()`


---




### 📄 Python File Metadata: `nb_cmd/core/meta.py`

#### 📝 Module Docstring

`````
NbCmd Meta 配置基类。

用法::

    from nb_cmd import NbCmd, NbCmdMeta

    class MyTool(NbCmd):
        class Meta(NbCmdMeta):
            name = "my-tool"
            version = "1.0.0"
            use_nb_log = True
`````

#### 📦 Imports

- `from typing import Dict`
- `from typing import List`
- `from typing import Optional`

#### 🏛️ Classes (1)

##### 📌 `class NbCmdMeta(object)`
*Line: 19*

**Docstring:**
`````
NbCmd 的 Meta 配置基类。

子类继承后可覆盖任意字段，IDE 可自动补全所有可用选项。
`````

**Class Variables (21):**
- `name: Optional[str] = None`
- `version: str = '0.0.1'`
- `description: Optional[str] = None`
- `use_nb_log: bool = False`
- `log_level: str = 'INFO'`
- `log_file: Optional[str] = None`
- `auto_save_last_args: bool = False`
- `config_file: Optional[str] = None`
- `serve_host: str = '0.0.0.0'`
- `serve_port: int = 8080`
- `serve_workers: int = 1`
- `web_title: Optional[str] = None`
- `web_theme: str = 'light'`
- `enable_exec: bool = True`
- `help_mode: str = 'full'`
- `aliases: Dict[str, List[str]] = {}`
- `allow_method_list: Optional[List[str]] = None`
- `hide_method_list: Optional[List[str]] = None`
- `auth_token: Optional[str] = None`
- `timeout: int = 0`
- `db_dir: Optional[str] = None`


---




### 📄 Python File Metadata: `nb_cmd/ui/helper.py`

#### 📝 Module Docstring

`````
UI 工具方法集合 —— cmdui 单例的实现。

通过 ``from nb_cmd import cmdui`` 导入使用。
`````

#### 📦 Imports

- `import json`
- `import sys`
- `from colors import print_success`
- `from colors import print_warning`
- `from colors import print_error`
- `from colors import print_info`
- `from table import print_table`
- `from table import print_kv`
- `from progress import progress as _progress_iter`

#### 🏛️ Classes (1)

##### 📌 `class UIHelper(object)`
*Line: 15*

**Docstring:**
`````
NbCmd 的 UI 工具方法集合。

通过 ``from nb_cmd import cmdui`` 导入使用，避免与用户自定义的子命令方法名冲突。
包含: 输出(table/kv/tree/json_print)、彩色(success/warning/error/info)、
      交互(confirm/prompt/select)、进度(progress) 等工具。
`````

**Public Methods (12):**
- `def table(self, data, headers = None)`
  - *表格输出*
- `def kv(self, data)`
  - *键值对输出*
- `def tree(self, data, prefix = '', is_last = True)`
  - *树形输出*
- `def json_print(self, data)`
  - *JSON美化输出*
- `def progress(self, iterable, desc = None, total = None)`
  - *进度条迭代器*
- `def confirm(self, message)`
  - *确认提示，返回 True/False*
- `def prompt(self, message, default = None)`
  - *输入提示*
- `def select(self, message, choices)`
  - *选择提示*
- `def success(self, msg)`
  - *绿色成功信息*
- `def warning(self, msg)`
  - *黄色警告信息*
- `def error(self, msg)`
  - *红色错误信息*
- `def info(self, msg)`
  - *蓝色信息*


---



## 🔗 nb_cmd Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Core Files (imported by other files, sorted by import count):
  ◆ nb_cmd/__init__.py (imported by 2 files)
  ◆ nb_cmd/core/meta.py (imported by 2 files)
  ◆ nb_cmd/core/base.py (imported by 1 files)
  ◆ nb_cmd/ui/helper.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `nb_cmd/__init__.py`

**Imports from project:**
- `nb_cmd/core/base.py`
- `nb_cmd/core/meta.py`
- `nb_cmd/ui/helper.py`

**Imported by:**
- `nb_cmd/core/base.py`
- `nb_cmd/ui/helper.py`

#### `nb_cmd/core/base.py`

**Imports from project:**
- `nb_cmd/__init__.py`
- `nb_cmd/core/meta.py`

**Imported by:**
- `nb_cmd/__init__.py`

#### `nb_cmd/core/meta.py`

**Imported by:**
- `nb_cmd/__init__.py`
- `nb_cmd/core/base.py`

#### `nb_cmd/ui/helper.py`

**Imports from project:**
- `nb_cmd/__init__.py`

**Imported by:**
- `nb_cmd/__init__.py`

### 📦 Third-party Dependencies

项目使用的第三方库：

- `nb_log`
- ......以及更多的第三方库......


---
# markdown content namespace: nb_cmd Project Root Dir Some Files 


## nb_cmd File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## nb_cmd (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: nb_cmd) --- 

`````markdown
# nb_cmd

**Python 码农的低代码平台** —— 写一个 class，自动获得七种能力：Python 直接调用 + CLI + REST API + Web UI + TUI 终端交互 + Markdown 文档 + skills 七种操作方式。不写路由、不写前端、不写 UI 代码、不写文档，全自动。

**nb-cmd: 不是"更好的 CLI 框架"，而是"低代码平台"**

用户只需要写一个 class，nb_cmd 自动生成 `python类自身正常直接调用` + `CLI` + `REST API` + `Web UI(含 WebSocket 实时控制台)` + `TUI 终端交互界面` + `自动生成Markdown使用文档` + `为ai生成agentskills.io规范的skills` 七种能力。
- 类自身完全照常使用（Python 直接调用）
- 自动生成 CLI 命令行
- 自动生成 REST API（含 Swagger 文档）
- 自动生成 Markdown 使用文档（CmdGen）
- 自动生成前端 Web UI（含 WebSocket 实时控制台）
- 自动生成 TUI 终端交互界面（基于 Textual，命令树 + 参数表单 + 实时控制台）
- 自动生成 为ai生成agentskills.io规范）规范的skills

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## why nb_cmd?

为什么要用nb_cmd?nb_cmd是不是装逼？是不是重复造轮子？抛开nb_cmd自带低代码平台的气质，只看命令行最本质的功能本身，比较下nb_cmd对其他顶流命令行框架的碾压优势。

> 详细的多维度对比（含多层级子命令 + 全局参数的完整代码对比）请看：[nb_cmd vs click vs typer vs fire](https://github.com/ydf0509/nb_cmd/blob/main/nb_cmd_vs_click_vs_typer.md)

> **GitHub CLI 实战对比：** 以真实 `gh` CLI 语义为基准（5 全局参数 + 3 子命令组 + 9 子命令），三框架完整实现对比。Click 需 49 个装饰器，Typer 需模块全局变量，nb_cmd 零装饰器 + 强类型上下文 + CmdGen 一行生成 Markdown 文档。[查看对比](examples/github_cli_demos/gh_comparison.md) | [nb_cmd 实现](examples/github_cli_demos/gh_nb_cmd.py) | [自动生成文档](examples/github_cli_demos/gh_nb_cmd_gen_doc.md)

## 目录

- [为什么用 nb_cmd？](#为什么用-nb_cmd)
- [核心价值与典型场景](#核心价值与典型场景)
- [安装](#安装)
- [nbcmd —— 零代码个人命令中心](#nbcmd--零代码个人命令中心)
- [5 分钟快速上手](#5-分钟快速上手)
- [核心特性](#核心特性)
- [完整 API 速查](#完整-api-速查)
- [和竞品对比](#和竞品对比)
- [项目结构](#项目结构)

---

## 为什么用 nb_cmd？

现有 CLI 框架（argparse / click / typer / fire）只解决了一件事：**怎么方便地定义 CLI 参数**。

但实际开发中，你一定遇到过：

- 你写了一个 CLI 工具 → 产品说"加个 Web 页面"
- 你写了一个 CLI 工具 → 运维说"要通过 API 远程调用"
- 你写了一个 CLI 工具 → 老板说"能让不懂命令行的人也能用吗"

**每次都是重写。**

nb_cmd 换了一种思路：**Class 是中心，能力是投影。**

```
             ┌── Python 直接调用（类自身完全照常使用）
             │
             ├── CLI 命令行（自动生成）
             │
业务逻辑(class) ─┼── REST API（自动 Swagger 文档）
             │
             ├── Web UI（自动生成页面 + WebSocket 实时控制台）
             │
             └── Markdown 使用文档（CmdGen 自动生成）
```

一次编写，七种能力全自动，不改一行代码。

**你写什么 → 你得到什么：**

| 你写的 | 自动获得 |
|--------|----------|
| 方法签名 `def deploy(self, host: str, port: int = 22)` | CLI 参数 + API 端点 + Web 表单 + TUI 参数表单 |
| 方法的 docstring `"""部署到远程服务器"""` | CLI --help + Swagger 文档 + Web/TUI UI 描述 |
| 类型注解 `env: Environment`（Enum） | CLI choices + API 校验 + Web/TUI 下拉选择 |
| `print()` / `cmdui.table()` | CLI 终端输出 + Web 实时流式推送 + TUI 实时控制台 |
| `sub_commands = {'git': GitTool}` | CLI 多级子命令 + API 嵌套路由 + Web/TUI 折叠分组 |
| `CmdGen(MyApp).doc(file='cli.md')` | **自动生成带 TOC + 参数表格 + 可复制命令行的 Markdown 文档** |
| `self.nbctx = AppCtx(region=self.region)` | **跨层级强类型上下文，自动穿透到所有子命令组，IDE 补全 + 零手动传递** |
| `MyTool().greet('张三', 3)` | **方法就是普通 Python 方法，随时直接调用、单元测试、import 复用** |

**不需要写的：** 路由定义、Pydantic 模型、HTML 表单、CSS 样式、JavaScript 交互、WebSocket 端点、Swagger 注解、前后端联调、**CLI 使用文档**。

> **零装饰器，方法可直接调用：** click/typer 的装饰器把函数变成了 `click.Command` 对象，无法直接 `greet('张三', 3)` 调用——必须用 `CliRunner().invoke()` 模拟 CLI 或自己拆两层。nb_cmd 的方法始终是普通的 Python 类方法，`MyTool().greet('张三', 3)` 直接就能跑，IDE 补全、断点调试、单元测试全部正常。

> **文档生成吊打 `--help`：** 传统框架的文档止步于 `--help` 纯文本，click 需要第三方 `sphinx-click`，typer 只是搬运 `--help` 输出。nb_cmd 的 `CmdGen` 一行代码生成完整的 Markdown 文档——自动目录、参数表格、默认值/必填标注、可复制的 bash 命令行模板，测试人员拿到直接能用。[查看示例](https://github.com/ydf0509/nb_cmd/blob/main/examples/nbctx_demo/nbctx_demo_gen_doc.md)

> **nbctx 跨层级上下文：** click 用 `ctx.obj` 字典（无类型、需手动 `@pass_context`），typer 用模块全局变量（无封装），nb_cmd 用 `self.nbctx`（强类型 dataclass + IDE 补全 + 框架自动注入到任意深度子命令组）。[nbctx 完整示例，实现github cli](examples/nbctx_demo/nbctx_demo.py)

| 功能 | argparse | click | typer | fire | **nb_cmd** |
|------|:--------:|:-----:|:-----:|:----:|:----------:|
| 零配置 | ✗ | ✗ | 部分 | ✓ | **✓** |
| 类型驱动 | 手动 | 手动 | ✓ | ✗ | **✓** |
| OOP 继承/覆写 | ✗ | ✗ | ✗ | 有限 | **✓** |
| 自动生成 REST API | ✗ | ✗ | ✗ | ✗ | **✓** |
| 自动生成 Web UI | ✗ | ✗ | ✗ |  | **✓** |
| 自动生成 TUI | ✗ | ✗ | ✗ | ✗ | **✓（Textual 终端图形界面）** |
| 多层级子命令 | 手动 | ✓ | ✓ | 有限 | **✓** |
| Swagger 文档 | ✗ | ✗ | ✗ | ✗ | **✓** |
| 进度条/表格/彩色 | ✗ | ✓ | ✓(rich) | ✗ | **✓** |
| 自动生成 CLI 文档 | ✗ | 第三方 | 基础 | ✗ | **✓（Markdown+表格+TOC+可复制命令行）** |
| 方法可直接调用 | ✓ | ✗ | ✗ | ✓ | **✓（零装饰器，普通类方法）** |
| 跨层级强类型上下文 | ✗ | ctx.obj(字典) | 全局变量 | ✗ | **✓（dataclass + IDE 补全 + 自动注入）** |
| async 方法支持 | ✗ | ✗ | ✓ | ✗ | **✓（自动检测，透明执行）** |

---

## 核心价值与典型场景

### 打破企业内部工具开发的"死循环"

在企业开发中，经常遇到这样的困境：

```
产品经理："这个工具不是公司核心业务，不立项"
    ↓
前端码农："没立项就没有需求排期，我不开发"
    ↓
Python 码农："我会写逻辑，但不会写前端"
    ↓
结果：工具永远停留在 CLI，只有技术人员能用
    ↓
测试/运营/产品："能不能给我们也用用？"
    ↓
Python 码农："等我学学 Vue/React..."（然后就没有然后了）
   ↓
最终：工具被遗忘，需求依然存在，问题继续存在
```

**nb_cmd 打破了这个死循环：**

```
Python 码农：写一个 class（30分钟）
    ↓
nb_cmd：自动生成 cli  + API +  Web UI
    ↓
测试/运营/产品：直接用网页操作
    ↓
前端人员：完全不需要介入！
```

### 效率对比

**传统方式的成本：**
```
需求沟通：2小时
前端开发：2-3天
前后端联调：1天
测试：0.5天
总计：约 4-5 天
```

**用 nb_cmd 的成本：**
```
写 Python class：1小时
启动 Web 模式：1分钟
总计：约 1 小时
```

**效率提升：40-50 倍！**

### 零成本优势

#### 1. 零前端成本
- 不需要懂 HTML/CSS/JavaScript
- 不需要学 Vue/React/Angular
- 不需要配置 webpack/vite
- 不需要处理前后端联调

#### 2. 零立项成本
- 产品经理不需要评估 ROI
- 不需要排期会议
- 不需要跨部门协调
- Python 码农自己就能搞定

#### 3. 零学习成本（对使用者）
- 测试人员：打开网页，填表单，点按钮
- 产品经理：看到的是专业的 UI，不是黑乎乎的命令行
- 运维人员：可以用 API 集成到自动化流程

### 典型应用场景

- **数据处理** — 导入 Excel、导出报表，测试和产品经理自己就能跑
- **测试辅助** — 创建测试用户、清理测试数据，测试人员自助操作
- **运维管理** — 重启服务、检查状态，运维用 API 集成到监控告警
- **配置管理** — 更新配置、查看配置，运营人员不用找开发

每个场景只需写一个 NbCmd 子类，`--web` 启动后发给团队即可使用。

---

## 安装

```bash
# 核心（CLI 模式，零外部依赖）
pip install nb-cmd

# 带 Web UI + REST API 模式（推荐）
pip install nb-cmd[web]

# 全部功能
pip install nb-cmd[all]
```

---

## nb_cmd 的两种使用方式

nb_cmd 提供两种使用方式，满足不同场景：

### 方式一：`nbcmd` 内置命令 —— 零代码个人命令中心

**不需要创建项目，不需要写任何一行 Python 代码。**

`nbcmd` 是 nb_cmd 自带的一个开箱即用的命令行工具。安装后，在任何终端直接输入 `nbcmd --tui`，即可启动一个个人命令管理器——通过内置的 `exec` 执行任意系统命令，收藏常用命令并设置短别名，以后再也不用记复杂的命令行。

你可以把 nbcmd --tui 当做linux服务器的的万能首屏，太香了，因为你可以把任何常用命令和其他click命令都收藏起来，一键点击运行。
xshell 和 finalshell的命令收藏，只有你一个人看得到，换个软件和电脑就看不到了，别人也看不到，nbcmd 的命令收藏是保存到sqlite持久化，所有人无论用xshell还是finalshell还是网页堡垒机，永远都可以看到。

```bash
# 一次安装
pip install nb-cmd[tui]

# 随时随地，在任何终端直接启动（无需进入任何项目目录）
nbcmd --tui

# 或者用浏览器模式
nbcmd --web
```

**工作流：**

```
1. 在任何终端输入 nbcmd --tui，打开命令中心
2. 选择 exec → 输入命令（如 docker-compose -f /opt/project/docker-compose.yml up -d）
3. 点击收藏 ★ → 输入别名（如"启动生产环境"）
4. 以后直接在收藏夹里找到并一键运行，永远不用再记命令
```

**典型场景**：一台 Linux 服务器上跑着 5 个项目，每个项目有不同的启动、部署、日志查看命令。以前要记 20 多条命令，现在全部收藏到 `nbcmd`，加上别名，一目了然。

| 功能 | 说明 |
|------|------|
| **exec 执行** | 通过内置 `exec` 命令执行任意系统命令 |
| **收藏 + 别名** | 给常用命令加短别名（如 `[启动前端]`、`[部署生产]`、`[查看日志]`） |
| **收藏夹运行** | 点击收藏命令直接运行，或填充到输入框修改参数后执行 |
| **历史记录** | 自动记录最近 1000 条执行历史，可搜索、可回填 |
| **TUI / Web 双模式** | 终端交互界面 + 浏览器界面，收藏数据自动同步 |
| **全局数据** | 收藏和历史保存在 `~/.nb_cmd/nb_cmd_web.db`，任何目录下启动都能访问 |

> **团队共享**：把常用命令收藏好，新人入职打开 `nbcmd --tui`，一眼看到所有常用操作，比任何 Wiki 文档都直观。

### 方式二：继承 `NbCmd` 类 —— 写一个 class 获得七种能力

**适合开发者**：继承 `NbCmd` 基类，定义业务方法，自动获得 Python 直接调用 + CLI + REST API + Web UI + TUI + Markdown 文档 + skills 七种能力。这是 nb_cmd 的核心价值，详见下文"5 分钟快速上手"。

```python
from nb_cmd import NbCmd

class MyTool(NbCmd):
    """我的运维工具"""
    def deploy(self, host: str, port: int = 22):
        """部署到远程服务器"""
        print('部署到 {}:{}'.format(host, port))

if __name__ == '__main__':
    MyTool().run()
```

```bash
python my_tool.py deploy web-01           # CLI 模式
python my_tool.py --web                   # Web UI + REST API 模式
python my_tool.py --tui                   # TUI 终端交互模式
```

> **两种方式的区别**：`nbcmd` 是内置的零配置工具，只有 `exec` 命令，适合"不想写代码，只想管理命令"的场景；继承 `NbCmd` 是开发者模式，适合"把业务逻辑封装成专业工具"的场景。

---

## nb_cmd 网页截图

> `nb_cmd` 只要你写了一个继承 `NbCmd` 的类，就自动生成 FastAPI 接口和接口文档，自动生成前端输入框和按钮。让你只写普通的类，无需接触 Web 后端接口开发，更无需接触前端界面开发，更无需接触 WebSocket 实时输出——你的方法中的任何普通的日志和 `print` 都会自动实时推送到 Web 前端页面上。

![nb_cmd 网页截图](https://github.com/ydf0509/nb_cmd/blob/main/docs/images/nb_cmd_web.png)

## nb_cmd TUI 截图

> `nb_cmd` 只要你写了一个继承 `NbCmd` 的类，就自动生成 Textual 终端图形界面，支持命令树、参数表单、实时控制台输出、命令历史、收藏等功能。

![nb_cmd TUI 截图](https://github.com/ydf0509/nb_cmd/blob/main/pictures/tui1.png)

## 5 分钟快速上手

### 第一步：写一个 class

```python
# my_tool.py
from nb_cmd import NbCmd, cmdui

class MyTool(NbCmd):
    """我的超级工具"""

    def greet(self, name: str, times: int = 1):
        """向某人问好"""
        for _ in range(times):
            print('你好, {}!'.format(name))

    def deploy(self, host: str, port: int = 22, verbose: bool = False):
        """部署到远程服务器"""
        if verbose:
            cmdui.info('正在部署到 {}:{} ...'.format(host, port))
        print('部署到 {}:{} 完成'.format(host, port))
        cmdui.success('部署成功!')

if __name__ == '__main__':
    MyTool().run()
```

> **注意：** nb_cmd 强制要求所有公有方法的参数必须声明类型注解（如 `name: str`），启动时自动校验，缺少注解直接报错。

### 第二步：当 CLI 用

```bash
$ python my_tool.py --help
我的超级工具

system params:
  -h, --help           显示帮助信息
  --cmd-version        show program's version number and exit
  --full-help, -fh     显示所有命令的完整参数详情
  --web                以Web UI + REST API模式启动
  --web-port WEB_PORT  Web UI 服务端口（用于 --web）

commands:
  {deploy,exec,greet}  可用命令
    deploy             部署到远程服务器 (HOST, --port=22, --verbose)
    exec               执行任意系统命令 (CMD)
    greet              向某人问好 (NAME, --times=1)

# 执行子命令
$ python my_tool.py greet 张三 --times 3
你好, 张三!
你好, 张三!
你好, 张三!

# 查看子命令的详细帮助
$ python my_tool.py deploy --help

# 执行带参数的命令
$ python my_tool.py deploy web-01 --port 2222 --verbose
[INFO] 正在部署到 web-01:2222 ...
部署到 web-01:2222 完成
[OK] 部署成功!
```

### 第三步：切换为 Web UI + REST API

```bash
$ python my_tool.py --web --web-port 8080
Web UI启动在 http://0.0.0.0:8080
API文档: http://0.0.0.0:8080/docs
```

打开浏览器：

- `http://localhost:8080` → **Web UI**：左侧是命令输入 + 收藏/历史搜索 + 参数表单，右侧是实时控制台输出，中间分割条可自由拖动
- `http://localhost:8080/docs` → **Swagger 文档**：所有命令自动生成 REST API

**Web UI 主要功能：**

- 命令行直接输入任意命令（非 NbCmd 命令自动通过 `exec` 执行）
- 参数表单自动生成（根据方法签名推导控件类型）
- WebSocket 实时流式输出（支持 ANSI 彩色渲染）
- 长时间命令可随时取消（停止按钮，类似 Ctrl+C）
- 命令收藏 + 执行历史（SQLite 持久化，Select2 风格弹框搜索）

用 curl 或 requests 调用（和 Web UI 共用同一套接口）：

```bash
$ curl -X POST http://localhost:8080/greet \
    -H "Content-Type: application/json" \
    -d '{"name": "张三", "times": 3}'
```

响应：

```json
{
  "status": "success",
  "result": null,
  "stdout": "你好, 张三!\n你好, 张三!\n你好, 张三!\n",
  "duration_ms": 1
}
```

**不改一行业务代码，CLI 和 Web + API 自由切换。**

---

## 核心特性

### 1. 自动推导规则

nb_cmd 通过 Python 方法签名自动生成 CLI 参数，零配置：

| Python 方法签名元素 | CLI 映射 | 示例 |
|---|---|---|
| 公有方法名 | 子命令名（`snake_case` → `kebab-case`） | `def show_users` → `show-users` |
| 方法的 docstring | 子命令帮助文本 | `"""查看用户"""` → `--help` 里的描述 |
| 无默认值的参数 | 位置参数（必填）；有短别名时为 `--flag`（必填） | `name: str` → `greet 张三`；`name: Annotated[str, '', 'n']` → `-n 张三` |
| 有默认值的参数 | 可选参数（`--xxx`） | `port: int = 22` → `--port 2222` |
| `bool` 类型 | 开关参数（`--flag`） | `verbose: bool = False` → `--verbose` |
| `int` / `float` 类型 | 自动类型转换和校验 | 输入非数字会报错 |
| `Enum` 类型 | 自动生成选择项 | `env: Environment` → `{dev,staging,prod}` |
| `Annotated[type, desc, alias]` | 参数描述 + 短别名 | `name: Annotated[str, '用户名', 'n']` → `-n` |
| `_` 开头的方法 | 不暴露为子命令 | `_helper()` → 内部方法 |

### 2. OOP 继承覆写

nb_cmd 基于类继承，天然支持模板方法模式：

```python
class BaseDeploy(NbCmd):
    """基础部署"""
    def deploy(self, host: str, version: str = "latest"):
        self._pre_deploy(host)
        self._do_deploy(host, version)
        self._post_deploy(host)
        cmdui.success('部署完成!')

    def _pre_deploy(self, host):
        cmdui.info('检查 {} 连接...'.format(host))

    def _do_deploy(self, host, version):
        cmdui.info('上传文件并重启服务')

    def _post_deploy(self, host):
        cmdui.info('验证服务状态')

class DockerDeploy(BaseDeploy):
    """Docker 部署——只需覆写一个方法"""
    def _do_deploy(self, host, version):
        cmdui.info('docker pull app:{}'.format(version))
        cmdui.info('docker-compose up -d')

class K8sDeploy(BaseDeploy):
    """K8s 部署——覆写 + 新增命令"""
    def _do_deploy(self, host, version):
        cmdui.info('kubectl set image app=app:{}'.format(version))

    def scale(self, replicas: int = 3):
        """扩缩容（K8s 特有命令）"""
        cmdui.info('kubectl scale --replicas={}'.format(replicas))
        cmdui.success('已扩缩至 {} 个副本'.format(replicas))
```

```bash
# 基础部署
$ python deploy.py deploy web-01

# Docker 部署——同样的命令，不同的实现
$ python docker_deploy.py deploy web-01

# K8s 多了一个 scale 命令
$ python k8s_deploy.py scale --replicas 5
```

其他框架做不到这一点：click/typer 用装饰器绑定函数，无法继承覆写；fire 虽然也基于类，但不支持多层级子命令和 Web/API 投影。

#### 方法可直接调用——零装饰器设计

click/typer 的装饰器会把函数**变成 `click.Command` 对象**，你无法像普通函数一样调用它：

```python
# click —— 装饰器改变了函数本质
@click.command()
@click.argument('name')
@click.option('--times', default=1)
def greet(name, times):
    print(f'Hello, {name}!')

greet('张三', 3)  # TypeError! greet 已经不是普通函数了
# 必须绕路：CliRunner().invoke(greet, ['张三', '--times', '3'])
# 或者自己拆两层：_greet_impl() + @click.command() 包一层
```

nb_cmd 的方法始终是**普通的 Python 类方法**，框架只在 `run()` 时通过反射发现它们：

```python
# nb_cmd —— 就是普通方法，零装饰器
class MyTool(NbCmd):
    def greet(self, name: str, times: int = 1):
        for _ in range(times):
            print(f'Hello, {name}!')

# 直接调用 —— 完全OK
MyTool().greet('张三', 3)

# 当 CLI 用 —— 也OK
MyTool().run()  # python script.py greet --name 张三 --times 3

# import 到别的模块 —— 也OK
from my_tool import MyTool
result = MyTool().greet('张三', 3)
```

**这意味着：** 你的业务逻辑（方法）永远可以直接调用、单元测试、import 复用，不被 CLI 框架绑架。

### 3. 多层级子命令

通过 `sub_commands` 定义子命令组，支持 `git remote add` 这样的多级命令：

```python
class GitRemote(NbCmd):
    """远程仓库管理"""
    def add(self, name: str, url: str):
        """添加远程仓库"""
        print('git remote add {} {}'.format(name, url))

    def remove(self, name: str):
        """删除远程仓库"""
        print('git remote remove {}'.format(name))

class GitTool(NbCmd):
    """Git 工具"""
    sub_commands = {'remote': GitRemote}

    def status(self):
        """查看状态"""
        print('当前分支: main')

    def commit(self, message: str, all: bool = False):
        """提交"""
        if all:
            print('git add -A')
        print("git commit -m '{}'".format(message))
```

```bash
$ python git_tool.py status                           # 一级命令
$ python git_tool.py remote add origin https://...    # 二级命令
$ python git_tool.py commit "fix bug" --all           # 一级命令
```

启动 Web 模式后，用 curl 调用多层级子命令：

```bash
# 启动 Web UI + REST API
$ python git_tool.py --web --web-port 8080

# 一级命令：POST /status（无参数）
$ curl -X POST http://localhost:8080/status

# 一级命令带参数：POST /commit
$ curl -X POST http://localhost:8080/commit \
    -H "Content-Type: application/json" \
    -d '{"message": "fix bug", "all": true}'

# 二级命令（子命令组）：POST /remote/add
$ curl -X POST http://localhost:8080/remote/add \
    -H "Content-Type: application/json" \
    -d '{"name": "origin", "url": "https://github.com/user/repo.git"}'

# 二级命令：POST /remote/remove
$ curl -X POST http://localhost:8080/remote/remove \
    -H "Content-Type: application/json" \
    -d '{"name": "origin"}'
```

> **路由规则：** 一级命令路由为 `/{command}`，子命令组中的命令路由为 `/{group}/{sub_command}`，与 CLI 的层级结构一一对应。所有接口在 Swagger 文档 `http://localhost:8080/docs` 中可查看。

在 Web UI 中，子命令组以蓝色标题 `[组]` 展示，展开后列出每个子命令的参数表单。

#### 组合多个 NbCmd 类为统一入口

已有的多个 NbCmd 类可以通过 `sub_commands` 组合成一个"大一统"工具，共享同一个 Web UI / API 入口：

```python
from nb_cmd import NbCmd

class MyTool(NbCmd):
    """基础工具"""
    def greet(self, name: str, times: int = 1):
        """问好"""
        for _ in range(times):
            print('你好, {}!'.format(name))

class DeployTool(NbCmd):
    """部署工具"""
    def deploy(self, host: str, port: int = 22):
        """部署"""
        print('部署到 {}:{}'.format(host, port))

    def status(self):
        """查看状态"""
        print('当前状态: 运行中')

class OneAllTool(NbCmd):
    """综合工具，在一个网页运行所有NbCmd其他类"""

    sub_commands = {
        'mytool': MyTool,
        'deploy-tool': DeployTool,
    }

if __name__ == '__main__':
    OneAllTool().run()
```

```bash
# CLI 用法
$ python bigone.py mytool greet 张三 --times 3
$ python bigone.py deploy-tool deploy web-01 --port 2222
$ python bigone.py deploy-tool status
```

启动 Web 模式后，所有子类的命令统一暴露为 REST API：

```bash
$ python bigone.py --web --web-port 8025

# mytool 组的 greet 命令
$ curl -X POST http://localhost:8025/mytool/greet \
    -H "Content-Type: application/json" \
    -d '{"name": "张三", "times": 3}'

# deploy-tool 组的 deploy 命令
$ curl -X POST http://localhost:8025/deploy-tool/deploy \
    -H "Content-Type: application/json" \
    -d '{"host": "web-01", "port": 2222}'

# deploy-tool 组的 status 命令（无参数）
$ curl -X POST http://localhost:8025/deploy-tool/status
```

> 这样可以把团队中各个人写的 NbCmd 类"插拔式"地组合到一个统一入口，Web UI 中每个组独立折叠展示。

#### sub_commands 支持传入实例

如果子类的 `__init__` 有必填参数，直接传 class 会因为无法无参实例化而报错。此时可以传入**实例**，nb_cmd 会自动提取 init 参数用于后续重建实例：

```python
from typing import Annotated

from nb_cmd import NbCmd

class ServerTool(NbCmd):
    def __init__(self, region: Annotated[str, '机房区域']):
        super().__init__()
        self.region = region

    def stats(self):
        print('区域: {}'.format(self.region))

class OneAllTool(NbCmd):
    sub_commands = {
        'mytool': MyTool,                    # 传 class（无 __init__ 参数）
        'server': ServerTool('beijing'),     # 传实例（有 __init__ 参数）
    }
```

> `sub_commands` 的 value 可以是 **class** 或 **instance**。传 instance 时，nb_cmd 从实例上提取 init 参数值，Web/API 模式下每次请求仍会新建隔离实例。

### 4. 内置输出工具（通过 cmdui 访问）

所有 UI/交互方法统一通过 `from nb_cmd import cmdui` 导入使用，**独立函数和类方法中均可调用**：

```python
from nb_cmd import NbCmd, cmdui

class DbTool(NbCmd):
    def query(self, sql: str):
        """执行 SQL 查询"""
        result = [
            {"id": 1, "name": "张三", "age": 25},
            {"id": 2, "name": "李四", "age": 30},
        ]
        cmdui.table(result)

    def stats(self):
        """数据库统计"""
        cmdui.kv({
            "数据库": "SQLite",
            "大小": "15.3 MB",
            "表数量": "12",
        })

    def schema(self):
        """数据库结构"""
        cmdui.tree({
            "数据库": {
                "users": {"id": "INT PK", "name": "VARCHAR"},
                "orders": {"id": "INT PK", "total": "DECIMAL"},
            }
        })

    def migrate(self, version: str = "latest"):
        """数据库迁移"""
        import time
        steps = ["检查版本", "备份数据", "执行迁移", "验证结果"]
        for step in cmdui.progress(steps, desc="迁移进度"):
            time.sleep(0.5)
        cmdui.success("迁移完成!")
```

输出效果：

```
# cmdui.table()
┌────┬──────┬─────┐
│ id │ name │ age │
├────┼──────┼─────┤
│ 1  │ 张三 │ 25  │
│ 2  │ 李四 │ 30  │
└────┴──────┴─────┘

# cmdui.kv()
数据库:  SQLite
大小  :  15.3 MB
表数量:  12

# cmdui.tree()
├── 数据库
│   ├── users
│   │   ├── id: INT PK
│   │   └── name: VARCHAR
│   └── orders
│       ├── id: INT PK
│       └── total: DECIMAL

# cmdui.progress()
迁移进度 ████████████████████████ 100% 4/4 [00:02<00:00]
[OK] 迁移完成!
```

### 5. Annotated 参数描述

用 `typing.Annotated` 为参数添加描述和短别名，CLI `--help`、Web UI 输入框、Swagger 文档会同步显示：

```python
from typing import Annotated

from nb_cmd import NbCmd

class MyTool(NbCmd):
    """部署工具"""

    def deploy(self, host: Annotated[str, '服务器地址', 'H'],
               port: Annotated[int, '端口号', 'p'] = 22,
               verbose: Annotated[bool, '详细模式', 'v'] = False):
        """部署到远程服务器"""
        ...
```

```bash
$ python my_tool.py deploy --help
optional arguments:
  --host HOST, -H HOST  服务器地址 (str, 必填)
  --port PORT, -p PORT  端口号 (int, 默认: 22)
  --verbose, -v         详细模式 (bool, 默认: False)

$ python my_tool.py deploy -H 10.0.0.1 -p 2222 -v
```

`Annotated` 的元数据是渐进式的——描述与短别名可选，不影响原有的 `name: str` 写法：

```python
name: str                                    # 最简写法，完全兼容
name: Annotated[str, '用户名']               # 加描述
name: Annotated[str, '用户名', 'n']          # 加描述 + 短别名
name: Annotated[str, '', 'n']                # 只加短别名
```

也可以用 `Param` 对象获得关键字参数风格（IDE 可补全字段名）：

```python
from nb_cmd import Param

name: Annotated[str, Param(desc='用户名', alias='n')]
port: Annotated[int, Param(desc='端口号')] = 22
```

> `Param(desc, alias)` 和位置字符串完全等价。Web UI 中，描述会显示在输入框旁边的灰色提示文字和 placeholder 中。

### 6. 全局参数（`__init__` 参数）

当多个子命令需要共享上下文（如机房区域、数据库连接、超时时间），把它们放到 `__init__` 中：

```python
from typing import Annotated
from enum import Enum

from nb_cmd import NbCmd, NbCmdMeta, cmdui

class Environment(Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"

class ServerTool(NbCmd):
    """服务器运维工具"""

    class Meta(NbCmdMeta):
        version = "1.0.0"
        use_nb_log = True

    def __init__(self, region: Annotated[str, '机房区域', 'r'],
                 timeout: Annotated[int, '超时秒数'] = 30):
        super().__init__()
        self.region = region
        self.timeout = timeout

    def deploy(self, host: str, env: Environment = Environment.DEV):
        """部署服务到目标主机"""
        cmdui.info('部署到 {} (区域: {}, 环境: {})'.format(host, self.region, env.value))
        cmdui.success('部署完成!')

    def stats(self):
        """查看系统状态"""
        cmdui.kv({"区域": self.region, "超时": "{}s".format(self.timeout)})

if __name__ == '__main__':
    ServerTool('beijing').run()
```

> **`region` 是必填参数**（无默认值），`timeout` 是选填参数（默认 30）。`ServerTool('beijing')` 中的 `'beijing'` 作为 `region` 的预设值，CLI / Web UI 均会以此作为默认值。

#### CLI 用法

`__init__` 参数在 CLI 中变为全局选项，放在子命令之前：

```bash
# --help 中会显示 init params 分区
$ python server_tool.py --help
system params:
  -h, --help           显示帮助信息
  --cmd-version        show program's version number and exit
  --full-help, -fh     显示所有命令的完整参数详情

init params:
  --region REGION, -r REGION  机房区域 (默认: beijing)
  --timeout TIMEOUT           超时秒数 (默认: 30)

commands:
  {deploy,exec,stats}  可用命令

# 使用预设值
$ python server_tool.py deploy 10.0.0.1

# 覆盖 region
$ python server_tool.py --region shanghai deploy 10.0.0.1 --env prod

# 用短别名
$ python server_tool.py -r shanghai --timeout 60 stats
```

#### Web UI 用法

```bash
$ python server_tool.py --web --web-port 8080
```

Web UI 顶部会自动生成全局参数表单，必填参数带 `*` 标记。修改后执行任意命令，自动携带。

#### curl / REST API 用法

启动 Web 模式后，REST API 端点自动注册：

```bash
# 查看有哪些全局参数及当前预设值
$ curl http://localhost:8080/api/init-params

# 不传 init_params → 使用预设值 region='beijing', timeout=30
$ curl -X POST http://localhost:8080/deploy \
    -H "Content-Type: application/json" \
    -d '{"host": "10.0.0.1", "env": "prod"}'

# 通过 init_params 覆盖全局参数
$ curl -X POST http://localhost:8080/deploy \
    -H "Content-Type: application/json" \
    -d '{
      "host": "10.0.0.1",
      "env": "prod",
      "init_params": {"region": "shanghai", "timeout": 60}
    }'

# 只覆盖部分参数，其余用预设值
$ curl -X POST http://localhost:8080/stats \
    -H "Content-Type: application/json" \
    -d '{"init_params": {"region": "guangzhou"}}'
```

响应示例：

```json
{
  "status": "success",
  "result": null,
  "stdout": "[INFO] 部署到 10.0.0.1 (区域: shanghai, 环境: prod)\n[OK] 部署完成!\n",
  "duration_ms": 5
}
```

> `init_params` 是可选字段，不传时使用 `ServerTool('beijing').run()` 中的预设值。Swagger 文档（`/docs`）中每个接口也会显示该字段。

> **多用户隔离：** Web 模式下，每次命令执行都会创建一个新的 `ServerTool` 实例，不同用户/请求之间互不影响。Web UI / curl 中传入的全局参数只影响当前这次执行。

### 7. nbctx 跨层级上下文传递

多层级子命令的核心难题：**子命令组怎么拿到顶层的全局参数？**

- **click** 用 `ctx.obj`（无类型字典），需要每层 `@click.pass_context` 手动传递
- **typer** 用模块级全局变量（无封装、无类型安全）
- **nb_cmd** 用 `self.nbctx`（强类型 dataclass），框架自动递归注入到任意深度

```python
from dataclasses import dataclass
from typing import Annotated
from nb_cmd import NbCmd

@dataclass
class AppCtx:
    region: str = 'beijing'
    env: str = 'prod'
    debug: bool = False

class DbTool(NbCmd):
    """数据库工具"""
    nbctx: AppCtx  # 类型注解 → IDE 补全 self.nbctx.region

    def migrate(self, dry_run: Annotated[bool, '仅模拟'] = False):
        """执行迁移"""
        print(f'[{self.nbctx.region}/{self.nbctx.env}] 迁移 (dry_run={dry_run})')

class MyApp(NbCmd):
    """云平台管理"""
    nbctx: AppCtx

    def __init__(self,
                 region: Annotated[str, '部署区域'] = 'beijing',
                 env: Annotated[str, '运行环境'] = 'prod',
                 debug: Annotated[bool, '调试模式'] = False):
        self.region = region
        self.env = env
        self.debug = debug
        # 直接赋值 nbctx，CLI/Web/API 所有模式自动拿到正确值
        self.nbctx = AppCtx(region=self.region, env=self.env, debug=self.debug)

    sub_commands = {'db': DbTool}
```

```bash
# CLI: 全局参数自动穿透到子命令组
$ python app.py --region tokyo db migrate --dry-run
[tokyo/prod] 迁移 (dry_run=True)

# curl: 通过 init_params 传递全局参数
$ curl -X POST http://localhost:8080/db/migrate \
    -d '{"dry_run": true, "init_params": {"region": "tokyo"}}'
```

**核心设计：**

- 在 `__init__` 中直接 `self.nbctx = AppCtx(...)` 赋值，所有模式（CLI / Web / API / Python 直接调用）均能拿到正确的参数值
- 也可以用 `make_nbctx()` 模板方法替代直接赋值（两种方式等价）
- 子命令组只需写 `nbctx: AppCtx` 类型注解，IDE 自动补全 `self.nbctx.region` 等字段
- 框架自动 `child.nbctx = parent.nbctx` 递归传递，支持任意嵌套深度
- 不同用户/请求之间完全隔离（Web 模式下每次请求新建实例）

> 完整三层嵌套示例见 [examples/nbctx_demo/](examples/nbctx_demo/nbctx_demo.py)

### 8. 参数校验

```python
from nb_cmd import NbCmd, validate

class MyTool(NbCmd):
    @validate(port=lambda x: 1 <= x <= 65535)
    def deploy(self, host: str, port: int = 22):
        """部署"""
        print('部署到 {}:{}'.format(host, port))
```

```bash
$ python my_tool.py deploy web-01 --port 99999
# 自动报错: port 校验失败
```

### 8. 内置系统命令执行

所有 NbCmd 子类自动拥有 `exec` 子命令和 `self.shell()` 工具方法：

```bash
# exec 子命令——直接在 CLI/Web UI 中执行任意系统命令
$ python my_tool.py exec "docker ps"
$ python my_tool.py exec "ls -la"
```

> **Web UI 智能路由：** 在 Web UI 的命令输入框中，输入非 NbCmd 命令（如 `python script.py`、`docker ps`、`ls -la`）会自动通过 `exec` 执行，无需手动加 `exec` 前缀。

```python
class MyTool(NbCmd):
    def deploy(self, host: str):
        """部署"""
        self.shell('scp app.tar.gz {}:/opt/'.format(host))
        self.shell('ssh {} "cd /opt && tar xzf app.tar.gz"'.format(host))
        cmdui.success('部署完成!')

    def version(self):
        """查看远程版本"""
        ver = self.shell('python --version', capture=True)
        print('Python: {}'.format(ver))
```

### 9. Meta 配置

通过内部类 `Meta` 自定义工具的行为。继承 `NbCmdMeta` 可获得 IDE 自动补全：

```python
from nb_cmd import NbCmd, NbCmdMeta

class MyTool(NbCmd):
    class Meta(NbCmdMeta):
        name = "mytool"
        version = "1.0.0"
        description = "我的超级工具"
        use_nb_log = True
        log_level = "DEBUG"
        web_theme = "dark"
        serve_port = 9000
```

> 也可以写 `class Meta(NbCmd.Meta):`，效果一样。不继承也行（向后兼容），但无法 IDE 补全。

**Meta 完整字段一览：**

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `name` | str | `None` | CLI/API 名称（默认用类名） |
| `version` | str | `'0.0.1'` | 版本号（`--cmd-version` 显示） |
| `description` | str | `None` | 描述（默认用类的 docstring） |
| `use_nb_log` | bool | `False` | 启用 [nb_log](https://github.com/ydf0509/nb_log) 增强日志 |
| `log_level` | str | `'INFO'` | 日志级别 |
| `log_file` | str | `None` | 日志文件路径 |
| `auto_save_last_args` | bool | `False` | 自动保存上次参数（规划中） |
| `config_file` | str | `None` | 配置持久化文件路径（规划中） |
| `serve_host` | str | `'0.0.0.0'` | Web/API 绑定地址 |
| `serve_port` | int | `8080` | Web/API 默认端口 |
| `serve_workers` | int | `1` | 工作进程数（规划中） |
| `web_title` | str | `None` | Web UI 页面标题 |
| `web_theme` | str | `'light'` | Web UI 主题（`'light'` / `'dark'`） |
| `enable_exec` | bool | `True` | 是否暴露内置 `exec` 命令（设为 `False` 可防止恶意执行系统命令） |
| `help_mode` | str | `'full'` | `-h` 的默认行为：`'full'` 显示完整帮助，`'easy'` 显示 argparse 原生格式 |
| `aliases` | dict | `{}` | 参数别名（推荐用 `Annotated[..., 'desc', 'a']` 指定短别名替代） |
| `allow_method_list` | list | `None` | 命令白名单（仅限制 CLI/API/Web/TUI 暴露；`None` 暴露全部；Python 直接调用不受影响） |
| `hide_method_list` | list | `None` | 命令黑名单（与白名单互斥，白名单优先；仅限制 CLI/API/Web/TUI） |
| `auth_token` | str | `None` | 简易 Bearer token 鉴权（配置后 API/Web 请求须带 `Authorization: Bearer <token>`） |
| `timeout` | int | `0` | 命令执行超时秒数（0=不限；作用于 CLI/API/Web/TUI 模式） |
| `db_dir` | str | `None` | SQLite 数据库目录（默认当前工作目录；设为 `~/.nb_cmd` 可全局共享收藏和历史） |

### 10. 生命周期钩子

```python
class MyTool(NbCmd):
    def before_run(self):
        """所有子命令执行前"""
        self.logger.info("工具启动")

    def after_run(self):
        """所有子命令执行后"""
        self.logger.info("操作完成")

    def on_error(self, command, error):
        """出错时"""
        self.logger.error("命令 {} 失败: {}".format(command, error))
```

### 11. 帮助系统

nb_cmd 提供三级帮助：

```bash
# 一级：总览（所有命令 + 简要参数提示）
$ python server_tool.py --help

# 二级：单个子命令的详细帮助
$ python server_tool.py deploy --help
usage: server_tool.py deploy [-h] [--env {dev,staging,prod}] HOST

部署服务到目标主机

positional arguments:
  HOST                     (str, 必填)

optional arguments:
  --env {dev,staging,prod}  (str, 默认: dev)

# 三级：所有命令的完整参数详情（对应前文第 6 节的 ServerTool 示例）
$ python server_tool.py --full-help   # 或 -fh
========================================================
  ServerTool v1.0.0
  服务器运维工具
========================================================

system params:
    --help, -h               显示简要帮助
    --full-help, -fh         显示本完整帮助
    --cmd-version            显示版本号
    --web                    以Web UI + REST API模式启动
    --web-port PORT          Web UI 服务端口

init params:
    --region, -r             机房区域  (全局, str, 默认: beijing)
    --timeout                超时秒数  (全局, int, 默认: 30)

--------------------------------------------------------
deploy — 部署服务到目标主机
    HOST                     (str, 必填)
    --env                    (Environment, 默认: Environment.DEV)

stats — 查看系统状态
```

通过 `Meta.help_mode` 可以控制 `-h` 的默认行为：

```python
class MyTool(NbCmd):
    class Meta:
        help_mode = 'full'   # -h 显示完整帮助（默认）
        # help_mode = 'easy' # -h 显示 argparse 原生格式
```

> 无论 `help_mode` 设置如何，`-fh` 始终显示完整帮助，`-eh` 始终显示简易帮助。

### 12. 自动文档生成（CmdGen）—— 吊打 `--help`

传统 CLI 框架的文档能力止步于 `--help`：一段纯文本，不能复制、不能跳转、不能分享。即使 typer 有 `typer utils docs`，也只是把 `--help` 搬到 Markdown 里而已。

nb_cmd 的 `CmdGen` 是真正的**面向用户的 API 文档生成器**——自动生成带 TOC 目录、参数表格、可复制命令行、占位符约定的**高质量 Markdown 文档**，测试人员和运维人员拿到就能直接用。

```python
from nb_cmd import CmdGen

g = CmdGen(MyApp, script='my_tool.py')

# 生成单个命令的可复制命令行
print(g.cmd(DbTool.migrate))
# python my_tool.py --region ${beijing} --env ${prod} --debug db migrate --dry-run

# 一键生成完整 Markdown 文档到文件
g.doc(file='docs/cli_reference.md')
```

**生成的 Markdown 包含：**

| 区域 | 内容 |
|------|------|
| 标题 + 版本 | `# cloud-tool v1.0.0` |
| Table of Contents | 自动递归生成，支持多层级子命令组，可点击跳转 |
| System Params | 系统参数表格（`-h` / `-fh` / `--web` 等） |
| Global Params | 全局参数表格（类型 + 默认值 + 描述） |
| Quick Start | 三条最常用命令（查看帮助/版本/启动 Web） |
| 命令行约定 | `${value}` / `$<required>` / `--flag` 含义说明 |
| 每个命令 | 标题 + 描述 + 参数表格 + 可复制 `bash` 代码块 |

**vs 其他框架的文档能力：**

| 功能 | click | typer | nb_cmd `CmdGen` |
|------|-------|-------|-----------------|
| 终端 `--help` | 有 | 有（Rich） | 有（三级帮助系统） |
| 自动生成 Markdown | 需第三方 `sphinx-click` | 基础版（搬运 `--help`） | **完整版（表格+TOC+代码块）** |
| 可复制命令行模板 | ✗ | ✗ | **✓** `${default}` / `$<required>` |
| 参数表格（类型/默认/描述） | ✗ | ✗ | **✓** 每个命令自动生成 |
| 单命令示例生成 | ✗ | ✗ | **✓** `g.cmd(DbTool.migrate)` |
| 一键写入文件 | ✗ | ✗ | **✓** `g.doc(file='xxx.md')` |
| 智能格式路由 | ✗ | ✗ | **✓** `.md` 文件自动用 Markdown 格式 |

> 完整示例见 [examples/nbctx_demo/nbctx_demo_gen_doc.md](https://github.com/ydf0509/nb_cmd/blob/main/examples/nbctx_demo/nbctx_demo_gen_doc.md)

### 13. Web UI 交互特性

以下功能在 `--web` 模式下自动可用，无需额外配置：

| 功能 | 说明 |
|------|------|
| 实时流式输出 | WebSocket 推送，print() 实时显示在控制台，支持 ANSI 彩色渲染 |
| 命令取消 | 长时间运行的命令可点击"停止"按钮随时取消（类似 Ctrl+C），执行中"执行"按钮自动置灰 |
| 命令收藏 | 点击 ★ 按钮将常用命令保存到 SQLite，自动去重 |
| 执行历史 | 每次执行自动记录到 SQLite，保留最近 1000 条 |
| Select2 搜索 | 收藏和历史各有独立的 Select2 风格弹框，支持模糊搜索、键盘导航，点击即填入命令行 |
| 智能路由 | 命令行输入非 NbCmd 命令时自动通过 exec 执行，可直接输入 `python xxx.py`、`docker ps` 等 |
| 参数表单 | 根据方法签名自动推导控件（文本框、数字框、复选框、下拉选择等） |
| 可拖拽布局 | 左右面板中间的分割条可自由拖动调整比例 |
| 并发安全 | 每次请求新建实例，stdout/stderr 通过 `threading.local()` 隔离，多用户同时操作互不影响 |

### 14. async 方法支持

nb_cmd 自动检测 `async def` 方法，透明地用 `asyncio.run()` 执行，无需额外配置：

```python
import asyncio
from nb_cmd import NbCmd

class MyTool(NbCmd):
    async def fetch(self, url: str):
        """异步请求"""
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(f'Status: {resp.status}')
                return await resp.text()
```

```bash
$ python my_tool.py fetch https://httpbin.org/get
```

同步和异步方法可以在同一个类中自由混用，CLI / Web / API 三种模式均自动处理。

---

## 完整 API 速查

### 导入

```python
from typing import Annotated
from nb_cmd import NbCmd, NbCmdMeta, Param, cmdui, validate, CmdGen
```

### CmdGen（自动文档生成）

```python
from nb_cmd import CmdGen

g = CmdGen(entry_cls, script='app.py', python='python', fmt='text')
```

| 方法 | 说明 |
|------|------|
| `CmdGen(cls, script, python, fmt)` | 创建生成器。`fmt`: `'text'` / `'markdown'` |
| `g.cmd(Method)` | 生成单个方法的可复制 CLI 命令行 |
| `g.doc()` | 生成完整文档字符串 |
| `g.doc(file='path.md')` | 生成完整文档并写入文件（`.md` 自动用 Markdown 格式） |

### cmdui（UI / 交互工具）

`from nb_cmd import cmdui` —— 模块级单例，类方法和独立函数中均可使用：

| 方法 | 说明 |
|------|------|
| `cmdui.table(data, headers)` | 表格输出（list[dict]） |
| `cmdui.kv(data)` | 键值对输出（dict） |
| `cmdui.tree(data)` | 树形输出（嵌套 dict） |
| `cmdui.json_print(data)` | JSON 美化输出 |
| `cmdui.progress(iter, desc, total)` | 进度条迭代器 |
| `cmdui.confirm(msg)` | 确认提示 `[y/N]` → bool |
| `cmdui.prompt(msg, default)` | 输入提示 → str |
| `cmdui.select(msg, choices)` | 选择提示 → str |
| `cmdui.success(msg)` / `warning` / `error` / `info` | 彩色状态输出 |

### self 直属方法 / 属性

| 方法 / 属性 | 说明 |
|------|------|
| `self.shell(cmd, capture, check)` | 执行系统命令。`capture=True` 返回 stdout 字符串 |
| `self.logger` | 日志器（`use_nb_log=True` 时为 nb_log 增强版） |
| `self.before_run()` / `after_run()` | 钩子：子命令执行前后调用 |
| `self.on_error(command, error)` | 钩子：子命令出错时调用 |
| `exec <cmd>` (内置子命令) | 执行任意系统命令（CLI 和 Web UI 均可用） |

### Annotated 参数描述

两种等价写法：

**位置字符串：** `Annotated[类型, '描述', '别名']`

| 位置 | 必填 | 说明 |
|------|------|------|
| 第一个参数（类型） | 是 | 实际参数类型（`str`, `int`, `bool`, `Enum`, `List[str]` 等） |
| 第二个参数（字符串） | 否 | 参数描述（`--help`、Web UI placeholder、Swagger 同步显示） |
| 第三个参数（字符串） | 否 | 短别名（`'n'` → `-n`，`'host-name'` → `--host-name`） |

**Param 对象：** `Annotated[类型, Param(desc='描述', alias='别名')]`

| 参数 | 必填 | 说明 |
|------|------|------|
| `desc` | 否 | 参数描述 |
| `alias` | 否 | 短别名 |

---

## 和竞品对比

> 详细的多维度对比（含多层级子命令 + 全局参数的完整代码对比）请看：[nb_cmd vs click vs typer vs fire](https://github.com/ydf0509/nb_cmd/blob/main/nb_cmd_vs_click_vs_typer.md)

> **GitHub CLI 三框架实战对比**：以真实 `gh` CLI 为基准（5 全局参数 + 3 子命令组 + 9 子命令），三框架完整可运行代码对比。[查看完整对比文档](examples/github_cli_demos/gh_comparison.md) | [Click 实现](examples/github_cli_demos/gh_click.py) | [Typer 实现](examples/github_cli_demos/gh_typer.py) | [nb_cmd 实现](examples/github_cli_demos/gh_nb_cmd.py) | [CmdGen 自动生成文档](examples/github_cli_demos/gh_nb_cmd_gen_doc.md)

### 代码对比：实现同一个工具

**argparse（30+ 行样板代码）：**

```python
import argparse

parser = argparse.ArgumentParser(description='部署工具')
subparsers = parser.add_subparsers(dest='command')

deploy_parser = subparsers.add_parser('deploy', help='部署服务')
deploy_parser.add_argument('host', type=str, help='目标主机')
deploy_parser.add_argument('--port', type=int, default=22, help='端口')
deploy_parser.add_argument('--verbose', action='store_true', help='详细输出')

status_parser = subparsers.add_parser('status', help='查看状态')

args = parser.parse_args()
if args.command == 'deploy':
    deploy(args.host, args.port, args.verbose)
elif args.command == 'status':
    status()
# 还需要手动实现 API 和 Web UI...
```

**click（装饰器地狱）：**

```python
import click

@click.group()
def cli():
    """部署工具"""
    pass

@cli.command()
@click.argument('host')
@click.option('--port', default=22, type=int, help='端口')
@click.option('--verbose', is_flag=True, help='详细输出')
def deploy(host, port, verbose):
    """部署服务"""
    ...

@cli.command()
def status():
    """查看状态"""
    ...
# 想加 API？对不起，请重写一遍...
```

**nb_cmd（一次编写，七种能力）：**

```python
from nb_cmd import NbCmd

class DeployTool(NbCmd):
    """部署工具"""

    def deploy(self, host: str, port: int = 22, verbose: bool = False):
        """部署服务"""
        ...

    def status(self):
        """查看状态"""
        ...

if __name__ == '__main__':
    DeployTool().run()
```

```bash
python deploy.py deploy web-01            # CLI
python deploy.py --web --web-port 8080     # Web UI + REST API
```

**核心差异：** argparse / click / typer 的世界观是"CLI 是终点"。nb_cmd 的世界观是"Class 是中心，能力是投影"——Python 直接调用、CLI、API、Web UI、TUI、Markdown 文档 、为ai生成agentskills.io规范的skills， 只是同一份业务逻辑的七种不同表现形式。

### vs 传统前后端开发

传统方式：**写后端 → 写接口 → 写文档 → 写前端 → 联调**，5 步缺一不可。nb_cmd 方式：只写 class，其余自动生成。

| 能力 | 传统方式 | nb_cmd |
|------|---------|--------|
| REST API（含 Swagger） | 手写路由 + 模型 | **方法签名自动生成** |
| Web UI（表单 + 控件） | 手写 HTML/CSS/JS | **类型注解自动推导控件** |
| WebSocket 实时输出 | 手写 WS 端点 + 前端接收 | **print() 自动流式推送** |
| 命令行 CLI | 另写 argparse | **同一份代码** |
| 文档同步 | 手动维护 | **永远一致（同一个类）** |
| 新增 1 个参数 | 改 3 处（后端/前端/文档） | **改 1 处（方法签名）** |
| 前端开发者 | 需要 | **不需要** |

> **本质区别：** 传统开发是"手动映射"——后端定义接口，前端照着文档手写表单；nb_cmd 是"自动投影"——Python 类是唯一真相源，Python 直接调用 / CLI / REST API / Web UI / TUI / Markdown 文档 是它的六个不同维度的投影。改真相源，投影自动跟着变。

---

## 项目结构

```
nb_cmd/
├── __init__.py            # 统一导出（from nb_cmd import ...）
├── core/
│   ├── base.py            # NbCmd 基类
│   ├── meta.py            # NbCmdMeta 配置基类
│   ├── arg.py             # Annotated / Param 参数元数据解析
│   ├── discovery.py       # 命令发现（反射 + 类型检查）
│   ├── parser.py          # argparse 解析器构建
│   ├── type_utils.py      # 类型工具（Enum/Optional/List 等）
│   ├── gen_cmd.py         # CmdGen 自动文档/命令行示例生成器
│   ├── result_handler.py  # 返回值自动处理
│   └── _io_dispatch.py    # 线程安全的 stdout/stderr 分发器
├── modes/
│   ├── cli_mode.py        # CLI 执行引擎
│   ├── api_mode.py        # REST API 路由生成（FastAPI）
│   ├── web_mode.py        # Web UI 页面生成 + WebSocket 实时输出
│   └── tui_mode.py        # TUI 终端交互界面（基于 Textual）
├── ui/
│   ├── helper.py          # UIHelper（cmdui 单例）
│   ├── colors.py          # ANSI 彩色输出
│   ├── table.py           # 表格 / 键值对输出
│   └── progress.py        # 进度条
└── utils/
    ├── validators.py      # @validate 装饰器
    └── config.py          # 配置持久化
```

---

## 依赖

| 模式 | 额外依赖 | 说明 |
|------|----------|------|
| CLI 模式 | **无** | 纯标准库，开箱即用 |
| Web UI + REST API | fastapi + uvicorn | `pip install nb-cmd[web]` |
| TUI 终端交互 | textual | `pip install nb-cmd[tui]` |
| nb_log 增强日志 | nb_log | 可选，`pip install nb_log` |

---

## License

MIT

`````

--- **end of file: README.md** (project: nb_cmd) --- 

---


--- **start of file: pyproject.toml** (project: nb_cmd) --- 

`````text
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "nb-cmd"
version = "0.2.2"
description = "万能接口生成器——你写一个 Python class，自动获得 CLI + REST API + Web UI + TUI 终端交互 + Python 直接调用 + markdown说明文档 + 为ai生成agentskills.io规范的skills 7种操作方式，堪称python界低代码平台"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.7"
authors = [
    {name = "ydf", email = "ydf0509@sohu.com"},
]
keywords = ["cli", "api", "webui", "tui", "command", "argparse", "fastapi", "textual"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",

    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

[project.optional-dependencies]
api = ["fastapi>=0.68.0", "uvicorn>=0.15.0", "pydantic>=1.8.0"]
web = ["fastapi>=0.68.0", "uvicorn>=0.15.0", "websockets>=10.0"]
tui = ["textual>=1.0.0"]
all = ["fastapi>=0.68.0", "uvicorn>=0.15.0", "pydantic>=1.8.0", "websockets>=10.0", "textual>=1.0.0"]
nb = ["nb_log"]

[project.scripts]
nbcmd = "nb_cmd.cli:main"

[project.urls]
Homepage = "https://github.com/ydf0509/nb_cmd"

[tool.setuptools.packages.find]
include = ["nb_cmd*"]

[tool.setuptools.package-data]
nb_cmd = ["ui/static/**/*"]

`````

--- **end of file: pyproject.toml** (project: nb_cmd) --- 

---

# markdown content namespace: nb_cmd 和其他顶流命令行框架例如click typer fire对比 


## nb_cmd File Tree (relative dir: `.`)


`````

└── nb_cmd_vs_click_vs_typer.md

`````

---


## nb_cmd (relative dir: `.`)  Included Files (total: 1 files)


- `nb_cmd_vs_click_vs_typer.md`


---


--- **start of file: nb_cmd_vs_click_vs_typer.md** (project: nb_cmd) --- 

`````markdown
# nb_cmd vs click vs typer vs fire：谁用法更简单？

> 从 Python 码农的实际体验出发，逐维度对比四大 CLI 框架的**简洁性**、**功能**和**扩展能力**。

---

## 一、同一个需求，五种写法

### 需求：部署工具

- 两个子命令：`deploy`（部署）和 `status`（查看状态）
- `deploy` 有三个参数：`host`（必填）、`port`（默认 22）、`verbose`（开关）
- `status` 无参数

---

### 1. argparse（30+ 行样板代码）

```python
import argparse

parser = argparse.ArgumentParser(description='部署工具')
subparsers = parser.add_subparsers(dest='command')

deploy_parser = subparsers.add_parser('deploy', help='部署服务')
deploy_parser.add_argument('host', type=str, help='目标主机')
deploy_parser.add_argument('--port', type=int, default=22, help='端口')
deploy_parser.add_argument('--verbose', action='store_true', help='详细输出')

status_parser = subparsers.add_parser('status', help='查看状态')

args = parser.parse_args()
if args.command == 'deploy':
    print('部署到 {}:{}'.format(args.host, args.port))
elif args.command == 'status':
    print('当前状态: 运行中')
```

**痛点：** 参数定义和业务逻辑分离，每加一个参数要改两处地方（定义 + 分发）。

---

### 2. click（装饰器堆叠）

```python
import click

@click.group()
def cli():
    """部署工具"""
    pass

@cli.command()
@click.argument('host')
@click.option('--port', default=22, type=int, help='端口')
@click.option('--verbose', is_flag=True, help='详细输出')
def deploy(host, port, verbose):
    """部署服务"""
    if verbose:
        click.echo('正在部署...')
    click.echo('部署到 {}:{}'.format(host, port))

@cli.command()
def status():
    """查看状态"""
    click.echo('当前状态: 运行中')

if __name__ == '__main__':
    cli()
```

**痛点：** 每个参数需要一个 `@click.option` / `@click.argument` 装饰器，3 个参数就 3 层装饰器。子命令间共享上下文需要用 `ctx.obj`，不直观。

---

### 3. typer（类型驱动，更简洁）

```python
import typer

app = typer.Typer(help='部署工具')

@app.command()
def deploy(host: str, port: int = 22, verbose: bool = False):
    """部署服务"""
    if verbose:
        print('正在部署...')
    print('部署到 {}:{}'.format(host, port))

@app.command()
def status():
    """查看状态"""
    print('当前状态: 运行中')

if __name__ == '__main__':
    app()
```

**优点：** 利用类型注解代替了 click 的装饰器堆叠。  
**痛点：** 仍然是函数式 + 装饰器，子命令间共享状态需要全局变量或 callback。无法继承覆写。

---

### 4. fire（零配置，最懒）

```python
import fire

class DeployTool:
    """部署工具"""
    def deploy(self, host, port=22, verbose=False):
        """部署服务"""
        if verbose:
            print('正在部署...')
        print('部署到 {}:{}'.format(host, port))

    def status(self):
        """查看状态"""
        print('当前状态: 运行中')

if __name__ == '__main__':
    fire.Fire(DeployTool)
```

**优点：** 代码最少，直接把 class 传给 `fire.Fire()`。  
**痛点：** 不强制类型注解，参数全是字符串需要手动转换；无法生成 API 和 Web UI；`--help` 信息简陋。

---

### 5. nb_cmd（一次编写，五种能力）

```python
from nb_cmd import NbCmd

class DeployTool(NbCmd):
    """部署工具"""

    def deploy(self, host: str, port: int = 22, verbose: bool = False):
        """部署服务"""
        if verbose:
            print('正在部署...')
        print('部署到 {}:{}'.format(host, port))

    def status(self):
        """查看状态"""
        print('当前状态: 运行中')

if __name__ == '__main__':
    DeployTool().run()
```

```bash
python deploy.py deploy web-01 --port 2222 --verbose   # CLI
python deploy.py --web                                   # Web UI + REST API
```

**优点：** 代码量和 fire 接近，但强制类型注解、自动类型校验、支持五种能力（Python 直接调用 + CLI + REST API + Web UI + Markdown 文档）。

---

## 二、逐维度详细对比

### 1. 代码行数（实现同一需求）

| 框架 | 行数 | 装饰器数 | 分发逻辑 |
|------|------|---------|---------|
| argparse | 15+ | 0 | 手动 if/elif |
| click | 18 | 5 | 自动 |
| typer | 14 | 2 | 自动 |
| fire | 12 | 0 | 自动 |
| **nb_cmd** | **12** | **0** | **自动** |

nb_cmd 和 fire 的行数几乎一样，但 nb_cmd 多了类型注解带来的自动校验。

---

### 2. 参数定义方式

| 框架 | 参数定义位置 | 类型校验 | 枚举支持 |
|------|------------|---------|---------|
| argparse | 独立的 `add_argument()` | 手动 `type=int` | 手动 `choices=[...]` |
| click | 装饰器 `@click.option()` | 手动 `type=int` | `type=click.Choice(...)` |
| typer | **函数签名** | **自动** | `typer.Option(..., case_sensitive=False)` |
| fire | 函数签名（无注解） | **无** | **无** |
| **nb_cmd** | **方法签名** | **自动** | **自动**（`Enum` 子类） |

nb_cmd 和 typer 都利用类型注解自动推导，但 nb_cmd 还自动支持 `Enum` → 选择项。

---

### 3. 子命令共享上下文（全局参数）

场景：多个子命令需要共享 `region`（机房区域）。

**click：**
```python
@click.group()
@click.option('--region', default='beijing')
@click.pass_context
def cli(ctx, region):
    ctx.ensure_object(dict)
    ctx.obj['region'] = region

@cli.command()
@click.pass_context
def deploy(ctx):
    region = ctx.obj['region']  # 通过 ctx 传递
```

**typer：**
```python
app = typer.Typer()
state = {"region": "beijing"}  # 全局变量

@app.callback()
def main(region: str = "beijing"):
    state["region"] = region

@app.command()
def deploy():
    region = state["region"]   # 通过全局变量
```

**nb_cmd：**
```python
class MyTool(NbCmd):
    def __init__(self, region: str = 'beijing'):
        super().__init__()
        self.region = region

    def deploy(self):
        print(self.region)   # 直接用 self
```

**nb_cmd 最自然**——`__init__` 就是全局参数，`self` 就是上下文。OOP 开发者零学习成本。

---

### 4. OOP 继承与覆写

| 框架 | 支持继承 | 支持覆写 | 模板方法模式 |
|------|---------|---------|-----------|
| argparse | ✗ | ✗ | ✗ |
| click | ✗ | ✗ | ✗ |
| typer | ✗ | ✗ | ✗ |
| fire | 有限 | 有限 | ✗ |
| **nb_cmd** | **✓** | **✓** | **✓** |

click 和 typer 用装饰器绑定函数，函数无法被子类覆写。nb_cmd 基于 class 继承，天然支持模板方法模式。

---

### 5. 多层级子命令

需求：`git remote add origin https://...`

**click：**
```python
@click.group()
def cli(): pass

@cli.group()
def remote(): pass

@remote.command()
@click.argument('name')
@click.argument('url')
def add(name, url):
    print('git remote add {} {}'.format(name, url))
```

**typer：**
```python
app = typer.Typer()
remote_app = typer.Typer()
app.add_typer(remote_app, name="remote")

@remote_app.command()
def add(name: str, url: str):
    print('git remote add {} {}'.format(name, url))
```

**nb_cmd：**
```python
class GitRemote(NbCmd):
    def add(self, name: str, url: str):
        print('git remote add {} {}'.format(name, url))

class GitTool(NbCmd):
    sub_commands = {'remote': GitRemote}
```

nb_cmd 用 `sub_commands` dict 声明，最简洁。click 需要嵌套 `@group()`，typer 需要 `add_typer()`。

---

### 6. 接口模式对比（核心差异）

| 能力 | argparse | click | typer | fire | **nb_cmd** |
|------|:--------:|:-----:|:-----:|:----:|:----------:|
| CLI | ✓ | ✓ | ✓ | ✓ | **✓** |
| REST API | ✗ | ✗ | ✗ | ✗ | **自动生成** |
| Web UI | ✗ | ✗ | ✗ | ✗ | **自动生成** |
| Swagger 文档 | ✗ | ✗ | ✗ | ✗ | **自动生成** |
| WebSocket 实时输出 | ✗ | ✗ | ✗ | ✗ | **✓** |
| 命令取消（停止按钮） | ✗ | ✗ | ✗ | ✗ | **✓** |
| 多用户并发隔离 | ✗ | ✗ | ✗ | ✗ | **✓** |

**这是 nb_cmd 的独家优势。** 其他框架的世界观是"CLI 是终点"，nb_cmd 是"Class 是中心，CLI/API/Web UI 是投影"。

---

### 7. 新增一个参数的改动量

假设要给 `deploy` 新增一个 `timeout: int = 30` 参数：

| 框架 | 需要改的地方 | 改动量 |
|------|------------|-------|
| argparse | `add_argument` + `if/elif` 分发 | 2 处 |
| click | `@click.option` 装饰器 + 函数签名 | 2 处 |
| typer | 函数签名 | **1 处** |
| fire | 函数签名 | **1 处** |
| **nb_cmd** | 方法签名 | **1 处** |

typer、fire、nb_cmd 都只需改方法签名。但 nb_cmd 改完后，CLI + API + Web UI 三处同步更新。

---

### 8. 参数描述与别名

**click：**
```python
@click.option('--host', '-H', help='服务器地址', required=True)
```

**typer：**
```python
def deploy(host: Annotated[str, typer.Argument(help='服务器地址')]):
```

**nb_cmd：**
```python
def deploy(self, host: Annotated[str, '服务器地址', 'H']):
```

nb_cmd 的 Annotated 写法最紧凑：类型、描述、别名写在一行。

---

## 三、纯 CLI 场景的真实对比（多层级子命令 + 全局参数）

抛开 Web/API 不谈，**纯 CLI 场景下**，一旦需求稍微复杂（多层级子命令 + 全局参数），nb_cmd 的优势就非常明显。

### 需求

- 全局参数：`region`（机房区域，必填）、`timeout`（超时，默认 30）
- 子命令组 `remote`：`add`（添加远程仓库）、`remove`（删除远程仓库）
- 子命令组 `branch`：`create`（创建分支）、`delete`（删除分支）
- 一级命令 `status`：查看状态
- 所有子命令都需要访问 `region`

用法：
```bash
python tool.py --region shanghai remote add origin https://...
python tool.py --region beijing branch create feature-x
python tool.py --region beijing status
```

---

### click 实现（约 60 行）

光看这一坨装饰器就头皮发麻——`@click.group()` 套 `@click.pass_context` 套 `@click.option()` 套 `@click.argument()`，一个子命令 4 层装饰器起步。你写的不是业务逻辑，你写的是装饰器俄罗斯套娃。半年后回来看自己的代码，第一反应是"这谁写的"。很多 Python 码农看到 click 的写法，转头就回去抱 argparse 了——至少 argparse 虽然笨，但看得懂。

这样写命令行，作者和读者都真的很想撞墙啊。

```python
import click

@click.group()
@click.option('--region', '-r', required=True, help='机房区域')
@click.option('--timeout', default=30, type=int, help='超时秒数')
@click.pass_context
def cli(ctx, region, timeout):
    """Git 风格工具"""
    ctx.ensure_object(dict)
    ctx.obj['region'] = region
    ctx.obj['timeout'] = timeout

@cli.command()
@click.pass_context
def status(ctx):
    """查看状态"""
    print('区域: {}'.format(ctx.obj['region']))

# ---------- remote 子命令组 ----------
@cli.group()
@click.pass_context
def remote(ctx):
    """远程仓库管理"""
    pass

@remote.command()
@click.argument('name')
@click.argument('url')
@click.pass_context
def add(ctx, name, url):
    """添加远程仓库"""
    print('git remote add {} {}'.format(name, url))

@remote.command()
@click.argument('name')
@click.pass_context
def remove(ctx, name):
    """删除远程仓库"""
    print('git remote remove {}'.format(name))

# ---------- branch 子命令组 ----------
@cli.group()
@click.pass_context
def branch(ctx):
    """分支管理"""
    pass

@branch.command()
@click.argument('name')
@click.option('--from-branch', default='main', help='基于哪个分支')
@click.pass_context
def create(ctx, name, from_branch):
    """创建分支"""
    print('git branch {} from {}'.format(name, from_branch))

@branch.command()
@click.argument('name')
@click.option('--force', '-f', is_flag=True, help='强制删除')
@click.pass_context
def delete(ctx, name, force):
    """删除分支"""
    flag = ' --force' if force else ''
    print('git branch -d{} {}'.format(flag, name))

if __name__ == '__main__':
    cli()
```

**痛点：**
- **`@click.pass_context` 到处传递**：每个子命令都要加 `@click.pass_context` + `ctx` 参数，才能访问全局参数
- **装饰器累积**：`remote add` 一个命令就要 3 个装饰器（`@remote.command()` + `@click.argument('name')` + `@click.argument('url')`），还要加 `@click.pass_context`
- **函数散落各处**：`add` 和 `remove` 是裸函数，和 `remote` 组的关系只靠装饰器维持
- **无法继承复用**：如果要做一个类似的工具（比如换成 SVN），整个文件要复制一遍

---

### typer 实现（约 50 行）

typer 号称"现代版 click"，确实少了一堆装饰器。但一遇到全局参数，立刻露馅——你得搞一个全局字典 `state = {}` 在模块顶部晃荡，每个子命令函数里 `state["region"]` 这么取值。这不就是 Java 码农最鄙视的"全局变量传参"吗？Python 写成这样，OOP 祖师爷看了都摇头。

而且如果多层级子命令太多的时候，需要精确的使用不同的 `typer.Typer()` 实例来区分不同的子命令组，你的装饰器千万不能用错了app，必须使用 `@精准的app.command()`,这个写法简直是太反人类了。
而NbCmd的多层级子命令，压根不需要关心自身处在哪个层级这个问题。

```python
import typer
from typing import Annotated

app = typer.Typer(help='Git 风格工具')
state = {"region": "", "timeout": 30}

@app.callback()
def main(region: Annotated[str, typer.Option('-r', help='机房区域')],
         timeout: int = 30):
    state["region"] = region
    state["timeout"] = timeout

@app.command()
def status():
    """查看状态"""
    print('区域: {}'.format(state["region"]))

# ---------- remote 子命令组 ----------
remote_app = typer.Typer(help='远程仓库管理')
app.add_typer(remote_app, name="remote")

@remote_app.command()
def add(name: str, url: str):
    """添加远程仓库"""
    print('git remote add {} {}'.format(name, url))

@remote_app.command()
def remove(name: str):
    """删除远程仓库"""
    print('git remote remove {}'.format(name))

# ---------- branch 子命令组 ----------
branch_app = typer.Typer(help='分支管理')
app.add_typer(branch_app, name="branch")

@branch_app.command()
def create(name: str, from_branch: str = "main"):
    """创建分支"""
    print('git branch {} from {}'.format(name, from_branch))

@branch_app.command()
def delete(name: str, force: bool = False):
    """删除分支"""
    flag = ' --force' if force else ''
    print('git branch -d{} {}'.format(flag, name))

if __name__ == '__main__':
    app()
```

**比 click 好的地方：** 类型注解代替装饰器，参数定义更简洁。  
**仍然的痛点：**
- **全局参数用全局变量 `state` 传递**：不够优雅，不是 OOP 风格
- **`add_typer()` 连接子命令组**：每个子组需要 `typer.Typer()` + `app.add_typer()`，两步操作
- **函数仍然散落**：`add` 函数和 `remote_app` 的关系靠 `@remote_app.command()` 装饰器维持
- **无法继承覆写**：同样无法做模板方法

---

### nb_cmd 实现（约 30 行）

看完上面那两坨代码，再看 nb_cmd——你会有一种"回家了"的感觉。没有装饰器、没有全局变量、没有 `ctx.obj`。就是正常写 Python class，该怎么写怎么写，`self` 就是上下文，`__init__` 就是全局参数。任何会写 class 的 Python 码农，不用看文档就能上手。

```python
from typing import Annotated
from nb_cmd import NbCmd

class GitRemote(NbCmd):
    """远程仓库管理"""
    def add(self, name: str, url: str):
        """添加远程仓库"""
        print('git remote add {} {}'.format(name, url))

    def remove(self, name: str):
        """删除远程仓库"""
        print('git remote remove {}'.format(name))

class GitBranch(NbCmd):
    """分支管理"""
    def create(self, name: str, from_branch: str = "main"):
        """创建分支"""
        print('git branch {} from {}'.format(name, from_branch))

    def delete(self, name: str, force: bool = False):
        """删除分支"""
        flag = ' --force' if force else ''
        print('git branch -d{} {}'.format(flag, name))

class GitTool(NbCmd):
    """Git 风格工具"""
    sub_commands = {'remote': GitRemote, 'branch': GitBranch}

    def __init__(self, region: Annotated[str, '机房区域', 'r'],
                 timeout: Annotated[int, '超时秒数'] = 30):
        super().__init__()
        self.region = region
        self.timeout = timeout

    def status(self):
        """查看状态"""
        print('区域: {}, 超时: {}s'.format(self.region, self.timeout))

if __name__ == '__main__':
    GitTool('beijing').run()
```

**nb_cmd 的优势（纯 CLI 角度）：**

1. **全局参数就是 `__init__`**：`self.region` 是自然的实例属性，不需要 `ctx.obj` 也不需要全局变量 `state`
2. **子命令组就是 class**：`sub_commands = {'remote': GitRemote}` 一行搞定，不需要 `app.add_typer()` 或嵌套 `@group()`
3. **每个子命令组是独立的 class**：可以单独测试、单独复用、单独继承
4. **零装饰器**：方法签名即定义，不需要任何 `@command()` 或 `@option()`
5. **支持继承覆写**：做一个 `SvnTool(GitTool)` 只需要覆写几个方法，click/typer 做不到

---

### 代码行数对比

| 框架 | 纯业务代码行数 | 框架样板代码 | 全局参数传递方式 | 子命令组定义 |
|------|-------------|------------|---------------|------------|
| click | ~60 行 | `@click.pass_context` × 6 | `ctx.obj['region']` | `@cli.group()` 嵌套 |
| typer | ~50 行 | `app.add_typer()` × 2 | `state["region"]` 全局变量 | `typer.Typer()` + `add_typer()` |
| **nb_cmd** | **~30 行** | **无** | **`self.region`** | **`sub_commands = {...}`** |

**即使纯 CLI 场景，nb_cmd 的代码量也只有 click 的一半、typer 的 60%。**

差距的核心原因：
- click/typer 是**函数式**的，子命令间共享状态需要额外机制（ctx 或全局变量）
- nb_cmd 是**OOP** 的，`self` 天然就是共享上下文

---

## 四、适用场景建议

| 场景 | 推荐框架 | 原因 |
|------|---------|------|
| 简单脚本（1-2 个命令，无全局参数） | fire / typer / **nb_cmd** | 代码量几乎一样少 |
| 多层级子命令 + 全局参数 | **nb_cmd** | `self` + `sub_commands` 比 ctx/全局变量简洁得多 |
| 需要继承覆写（模板方法） | **nb_cmd** | 独家支持，click/typer 做不到 |
| 多人协作的大型工具集 | **nb_cmd** | OOP 继承 + sub_commands 组合 |
| 正式发行包（需要 shell 补全） | typer | shell 补全开箱即用 |
| 需要额外 Web UI / API 的场景 | **nb_cmd** | 自动生成，额外的加分项 |

---

## 五、总结

| 维度 | 最简 | 说明 |
|------|------|------|
| 简单场景代码量 | fire ≈ **nb_cmd** ≈ typer | 都只需 12-14 行，nb_cmd 不比任何框架多 |
| 复杂场景代码量 | **nb_cmd** | 多层级 + 全局参数场景下，代码量只有 click 的一半 |
| 类型安全 | typer ≈ **nb_cmd** | 都利用类型注解 |
| 全局参数传递 | **nb_cmd** | `self.xxx` 最自然，click 用 ctx，typer 用全局变量 |
| 子命令组定义 | **nb_cmd** | `sub_commands = {...}` 一行，click/typer 需要多步 |
| OOP 继承/覆写 | **nb_cmd** | 独家支持，其他框架做不到 |
| 多接口模式 | **nb_cmd** | CLI + API + Web UI 三合一（额外加分） |
| Shell 补全 | typer | 开箱即用 |
| 生态成熟度 | click | 社区最大、插件最多 |

**一句话总结：**

- 简单场景 → nb_cmd 代码量和 fire/typer 一样少，没有额外负担
- **复杂场景（多层级子命令 + 全局参数 + 代码复用）**→ nb_cmd 的 OOP 模型比 click/typer 的函数式模型**简洁一倍**，这个优势跟 Web/API 无关
- Web/API 是额外的加分项，不是 nb_cmd 的唯一卖点

---

## 六、nb_cmd 在多层级命令下的碾压优势

多层级子命令是 CLI 框架的试金石——简单工具看不出差距，一旦子命令层级加深、全局参数需要穿透，各框架的设计哲学差距就彻底暴露出来。

### click/typer 的致命设计缺陷

**每个子命令都要"知道自己在哪"。**

click 里，`add` 函数必须通过 `@remote.command()` 才知道自己属于 `remote` 组。你有 `remote`、`branch`、`tag` 三个组，就有 `remote_app`、`branch_app`、`tag_app` 三个实例在模块顶部晃荡。写多了根本分不清哪个函数挂在哪个 app 下面。

typer 更离谱——你必须在文件头部创建 `remote_app = typer.Typer()`，然后 `app.add_typer(remote_app, name="remote")`，接着在下面的函数上 `@remote_app.command()`。一个子命令组就要**三步操作**：创建实例 → 注册到父级 → 装饰器绑定。搞 5 个子命令组你头都晕了。

更致命的是：**装饰器用错了 app 实例，命令就跑到错误的层级去了。** 这种 bug 极其隐蔽——代码不报错，`--help` 里命令位置不对，你得挨个排查每个装饰器绑的是哪个 app。

### nb_cmd 的设计：子命令不需要知道自己在哪

```python
class GitRemote(NbCmd):
    """远程仓库管理"""
    def add(self, name: str, url: str):
        print('git remote add {} {}'.format(name, url))
```

`GitRemote` 写的时候完全不知道自己会被挂在哪里——它是独立的 class，可以单独运行、单独测试。直到父级声明 `sub_commands = {'remote': GitRemote}`，它才被"挂载"到命令树上。

这意味着：
- **同一个 NbCmd 子类可以复用到不同的父级下**，不需要修改一行代码
- **层级关系是声明式的**，一眼就看出 `{'remote': GitRemote, 'branch': GitBranch}` 这棵树长什么样
- **不可能挂错层级**，因为根本没有装饰器可以用错

### 用数据说话

当子命令组数量增加时，各框架的代码膨胀率：

| 子命令组数量 | click 额外代码 | typer 额外代码 | nb_cmd 额外代码 |
|:---:|:---:|:---:|:---:|
| 1 组 | +8 行 (`@group` + `@pass_context` × N) | +3 行 (`Typer()` + `add_typer()` + 函数) | +1 行 (`sub_commands` 加一项) |
| 3 组 | +24 行 | +9 行 | +3 行 |
| 5 组 | +40 行 | +15 行 | +5 行 |
| 10 组 | +80 行 | +30 行 | +10 行 |

**nb_cmd 的膨胀率是 click 的 1/8、typer 的 1/3。** 子命令组越多，差距越大。

### 核心结论

> **nb_cmd 的多层级子命令不是"也能做到"——而是"碾压性地简洁"。**
>
> click 和 typer 的函数式设计在多层级场景下会产生大量样板代码（装饰器绑定、上下文传递、实例注册），而 nb_cmd 的 OOP 模型让这些统统变成了一行 dict 声明。
>
> 这个优势**纯粹是 CLI 层面的**，跟 Web/API 完全无关。

`````

--- **end of file: nb_cmd_vs_click_vs_typer.md** (project: nb_cmd) --- 

---

# markdown content namespace: nb_cmd examples 


## nb_cmd File Tree (relative dir: `examples`)


`````

└── examples
    ├── ai_skill_gen_demo
    │   ├── ai_skill_gen_demo.py
    │   └── skills
    │       ├── devops-tool
    │       │   └── SKILL.md
    │       ├── devops-tool-full
    │       │   └── SKILL.md
    │       └── devops-tool-py
    │           └── SKILL.md
    ├── bigone_cmd.py
    ├── demo_advanced.py
    ├── demo_basic.py
    ├── demo_full.py
    ├── demo_inherit.py
    ├── demo_most_easy.py
    ├── demo_nb_log.py
    ├── demo_subcommands.py
    ├── five_in_one_demo.py
    ├── five_in_one_demo_doc.md
    ├── git_demos
    │   ├── README.md
    │   ├── git_click.py
    │   └── git_nb_cmd.py
    ├── github_cli_demos
    │   ├── gh_click.py
    │   ├── gh_comparison.md
    │   ├── gh_nb_cmd.py
    │   ├── gh_nb_cmd_gen_doc.md
    │   └── gh_typer.py
    └── nbctx_demo
        ├── nbctx_demo.py
        └── nbctx_demo_gen_doc.md

`````

---


## nb_cmd (relative dir: `examples`)  Included Files (total: 24 files)


- `examples/bigone_cmd.py`

- `examples/demo_advanced.py`

- `examples/demo_basic.py`

- `examples/demo_full.py`

- `examples/demo_inherit.py`

- `examples/demo_most_easy.py`

- `examples/demo_nb_log.py`

- `examples/demo_subcommands.py`

- `examples/five_in_one_demo.py`

- `examples/five_in_one_demo_doc.md`

- `examples/ai_skill_gen_demo/ai_skill_gen_demo.py`

- `examples/ai_skill_gen_demo/skills/devops-tool/SKILL.md`

- `examples/ai_skill_gen_demo/skills/devops-tool-full/SKILL.md`

- `examples/ai_skill_gen_demo/skills/devops-tool-py/SKILL.md`

- `examples/github_cli_demos/gh_click.py`

- `examples/github_cli_demos/gh_comparison.md`

- `examples/github_cli_demos/gh_nb_cmd.py`

- `examples/github_cli_demos/gh_nb_cmd_gen_doc.md`

- `examples/github_cli_demos/gh_typer.py`

- `examples/git_demos/git_click.py`

- `examples/git_demos/git_nb_cmd.py`

- `examples/git_demos/README.md`

- `examples/nbctx_demo/nbctx_demo.py`

- `examples/nbctx_demo/nbctx_demo_gen_doc.md`


---


--- **start of file: examples/bigone_cmd.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 综合入口 demo —— 把多个 NbCmd 类组合到一个统一的 CLI / Web UI / TUI / REST API

用法:
    python bigone_cmd.py --help
    python bigone_cmd.py mytool greet 张三 --times 3
    python bigone_cmd.py deploy deploy web-01 --env prod
    python bigone_cmd.py k8s scale --replicas 5
    python bigone_cmd.py db query "SELECT 1"
    python bigone_cmd.py git status
    python bigone_cmd.py git remote add origin https://github.com/x/x.git
    python bigone_cmd.py server deploy 10.0.0.1 --env staging
    python bigone_cmd.py server stats
    python bigone_cmd.py --web --web-port 8025
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from nb_cmd import NbCmd
from demo_basic import MyTool
from demo_advanced import DeployTool
from demo_inherit import K8sDeploy
from demo_full import DbTool
from demo_subcommands import GitTool
from demo_nb_log import ServerTool


class OneAllTool(NbCmd):
    """
    综合工具，在一个网页运行所有NbCmd其他类
    """

    sub_commands = {
        'mytool': MyTool,
        'deploy': DeployTool,
        'k8s': K8sDeploy,
        'db': DbTool,
        'git': GitTool,
        'server': ServerTool('beijing'),
    }


if __name__ == '__main__':
    OneAllTool().run()

    '''
    D:/ProgramData/Miniconda3/envs/py39b/python.exe D:/codes/nb_cmd/examples/bigone_cmd.py --web --web-port 8025

    curl -X POST http://localhost:8025/mytool/greet -H "Content-Type: application/json" -d "{\"name\": \"张三\", \"times\": 3}"
    curl -X POST http://localhost:8025/deploy/deploy -H "Content-Type: application/json" -d "{\"host\": \"web-01\", \"env\": \"prod\"}"
    curl -X POST http://localhost:8025/deploy/status
    curl -X POST http://localhost:8025/k8s/deploy -H "Content-Type: application/json" -d "{\"host\": \"10.0.0.1\"}"
    curl -X POST http://localhost:8025/k8s/scale -H "Content-Type: application/json" -d "{\"replicas\": 5}"
    curl -X POST http://localhost:8025/db/query -H "Content-Type: application/json" -d "{\"sql\": \"SELECT * FROM users\"}"
    curl -X POST http://localhost:8025/db/stats
    curl -X POST http://localhost:8025/git/status
    curl -X POST http://localhost:8025/git/commit -H "Content-Type: application/json" -d "{\"message\": \"fix bug\", \"all\": true}"
    curl -X POST http://localhost:8025/server/deploy -H "Content-Type: application/json" -d "{\"host\": \"10.0.0.1\", \"env\": \"staging\"}"
    curl -X POST http://localhost:8025/server/stats
    '''


`````

--- **end of file: examples/bigone_cmd.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_advanced.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 高级用法 demo —— 继承覆写 + 子命令组 + 高级类型
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from typing import Annotated

from nb_cmd import NbCmd, NbCmdMeta, cmdui
from enum import Enum


class Environment(Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


class DeployTool(NbCmd):
    """部署工具"""

    class Meta(NbCmdMeta):
        use_nb_log = True
        log_level = "DEBUG"
        log_file = "deploy_tool.log"
        web_theme = "dark"
        serve_port = 8082
        serve_workers = 1
        web_title = "部署工具"

    def deploy(self,
               host: Annotated[str, '目标服务器地址', 'H'],
               port: Annotated[int, '端口号', 'p'] = 22,
               env: Annotated[Environment, '部署环境', 'e'] = Environment.DEV,
               dry_run: Annotated[bool, '试运行模式'] = False,
               ):
        """执行部署到指定服务器"""
        print('环境: {}'.format(env.value if hasattr(env, 'value') else env))
        print('目标: {}:{}'.format(host, port))
        if dry_run:
            print('** 试运行模式，不会实际执行 **')
        else:
            print('部署完成!')

    def status(self):
        """查看部署状态"""
        cmdui.kv({
            "当前环境": "dev",
            "最后部署": "2026-04-17 10:30",
            "服务状态": "运行中",
        })

    def show_users(self):
        """展示用户列表"""
        data = [
            {"名字": "张三", "年龄": 25, "城市": "北京"},
            {"名字": "李四", "年龄": 30, "城市": "上海"},
            {"名字": "王五", "年龄": 28, "城市": "广州"},
        ]
        cmdui.table(data)

    def process(self):
        """模拟处理任务（带进度条）"""
        
        items = list(range(20))
        for _ in cmdui.progress(items, desc="处理中"):
            time.sleep(0.1)
        cmdui.success("处理完成!")
    
    def many_print(self, num: int = 30):
        """持续打印多行（用于测试 WebSocket 实时流式输出）"""
        for i in range(num):
            time.sleep(1)
            print('print {}'.format(i))
            self.logger.debug('logger debug {}'.format(i))
            self.logger.info('logger info {}'.format(i))
            self.logger.warning('logger warning {}'.format(i))
            self.logger.error('logger error {}'.format(i))
            self.logger.critical('logger critical {}'.format(i))

            cmdui.info('ui info {}'.format(i))
            cmdui.success('ui success {}'.format(i))
            cmdui.error('ui error {}'.format(i))
            cmdui.warning('ui warning {}'.format(i))



if __name__ == '__main__':
    DeployTool().run()


    '''
    D:/ProgramData/Miniconda3/envs/py39b/python.exe examples/demo_advanced.py --web --web-port 8082
    
    '''

`````

--- **end of file: examples/demo_advanced.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_basic.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 基础用法 demo —— 对应设计文档 4.1 最简示例

用法:
    python demo_basic.py --help
    python demo_basic.py greet -n 张三 -t 3
    python demo_basic.py deploy -H 192.168.1.1 -p 2222 -v
    python demo_basic.py deploy --help
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from typing import Annotated

from nb_cmd import NbCmd
import asyncio


class MyTool(NbCmd):
    """我的超级工具（自动变成CLI的description）"""

    def greet(self, name: Annotated[str, '要问候的人名', 'n'],
              times: Annotated[int, '问候次数', 't'] = 1):
        """向某人问好（自动变成子命令的帮助信息）"""
        for _ in range(times):
            print('你好, {}!'.format(name))

    async def deploy(self, host: Annotated[str, '服务器地址', 'H'],
               port: Annotated[int, '端口号', 'p'] = 22,
               verbose: Annotated[bool, '详细模式', 'v'] = False):
        """部署到远程服务器"""
        # 这个函数是测试asyncio函数的运行
        if verbose:
            print('[详细模式] 正在部署到 {}:{} ...'.format(host, port))
        await asyncio.sleep(1)
        print('部署到 {}:{} 开始'.format(host, port))
        await asyncio.sleep(1)
        print('部署到 {}:{} 进行中'.format(host, port))
        await asyncio.sleep(1)
        print('部署到 {}:{} 完成'.format(host, port))

    def _private_helper(self):
        """下划线开头的方法不会暴露为子命令"""
        pass


if __name__ == '__main__':
    MyTool().run()

    '''
    D:/ProgramData/Miniconda3/envs/py39b/python.exe examples/demo_basic.py --web --web-port 8081
    
    '''

`````

--- **end of file: examples/demo_basic.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_full.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 完整功能 demo —— 对应设计文档附录A (数据库管理工具)

用法:
    python demo_full.py --help
    python demo_full.py query "SELECT * FROM users"
    python demo_full.py query "SELECT * FROM users" --output json
    python demo_full.py stats
    python demo_full.py migrate --version v2.0 --dry-run

    # REST API 模式
    # Web UI 模式
    python demo_full.py --web --web-port 9904
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from typing import Annotated

from nb_cmd import NbCmd, NbCmdMeta, cmdui
from enum import Enum


class OutputFormat(Enum):
    TABLE = "table"
    JSON = "json"
    CSV = "csv"


class DbTool(NbCmd):
    """数据库管理工具 - 支持多种数据库的通用管理"""

    class Meta(NbCmdMeta):
        name = "dbtool"
        version = "1.0.0"

    def query(self, sql: Annotated[str, 'SQL查询语句'],
              output: Annotated[OutputFormat, '输出格式'] = OutputFormat.TABLE,
              limit: Annotated[int, '返回行数上限'] = 100):
        """执行SQL查询并展示结果"""
        cmdui.info('执行: {}'.format(sql))
        result = [
            {"id": 1, "name": "张三", "age": 25},
            {"id": 2, "name": "李四", "age": 30},
            {"id": 3, "name": "王五", "age": 28},
        ]

        if output == OutputFormat.TABLE or output == 'table':
            cmdui.table(result)
        elif output == OutputFormat.JSON or output == 'json':
            cmdui.json_print(result)
        elif output == OutputFormat.CSV or output == 'csv':
            print("id,name,age")
            for row in result:
                print(",".join(str(v) for v in row.values()))

    def migrate(self, version: Annotated[str, '目标版本号'] = "latest",
                dry_run: Annotated[bool, '试运行，不实际执行'] = False):
        """执行数据库迁移"""
        if dry_run:
            cmdui.warning("试运行模式，不会实际执行")
        cmdui.info('迁移到版本: {}'.format(version))
        import time
        steps = ["检查版本", "备份数据", "执行迁移", "验证结果"]
        for step in cmdui.progress(steps, desc="迁移进度"):
            time.sleep(0.3)
        cmdui.success("迁移完成")

    def stats(self):
        """显示数据库统计信息"""
        cmdui.kv({
            "数据库类型": "SQLite",
            "数据库大小": "15.3 MB",
            "表数量": "12",
            "总行数": "1,234,567",
            "最后备份": "2026-04-17 10:30:00",
            "连接池状态": "5/20 活跃",
        })

    def tree_demo(self):
        """树形结构展示 demo"""
        cmdui.tree({
            "数据库": {
                "users": {
                    "id": "INT PRIMARY KEY",
                    "name": "VARCHAR(100)",
                    "age": "INT",
                },
                "orders": {
                    "id": "INT PRIMARY KEY",
                    "user_id": "INT FOREIGN KEY",
                    "total": "DECIMAL(10,2)",
                },
            },
            "配置": {
                "max_connections": "20",
                "timeout": "30s",
            },
        })


if __name__ == '__main__':
    DbTool().run()

    '''
    D:/ProgramData/Miniconda3/envs/py39b/python.exe examples/demo_full.py --web --web-port 8083
    
    '''

`````

--- **end of file: examples/demo_full.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_inherit.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 继承覆写 demo —— 对应设计文档 5.2 和附录B

用法:
    python demo_inherit.py deploy web-01 --version v2.0
    python demo_inherit.py status
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from nb_cmd import NbCmd, cmdui


class BaseDeploy(NbCmd):
    """基础部署工具"""

    def deploy(self, host: str, version: str = "latest"):
        """部署服务到目标主机"""
        self._pre_deploy(host)
        self._do_deploy(host, version)
        self._post_deploy(host)
        cmdui.success('{}@{} 已部署到 {}'.format("app", version, host))

    def status(self):
        """查看部署状态"""
        cmdui.kv({
            "部署方式": self._deploy_type(),
            "最后部署": "2026-04-17 15:00",
            "状态": "运行中",
        })

    def _deploy_type(self):
        return "基础部署"

    def _pre_deploy(self, host):
        cmdui.info('部署前检查: {}'.format(host))

    def _do_deploy(self, host, version):
        cmdui.info('上传文件到 {} ...'.format(host))
        cmdui.info('重启服务 ...')

    def _post_deploy(self, host):
        cmdui.info('验证服务状态: OK')


class DockerDeploy(BaseDeploy):
    """Docker部署——只需覆写部署逻辑"""

    def _deploy_type(self):
        return "Docker"

    def _do_deploy(self, host, version):
        cmdui.info('docker pull app:{}'.format(version))
        cmdui.info('docker-compose up -d')


class K8sDeploy(BaseDeploy):
    """K8s部署——覆写部署逻辑，还新增了 scale 命令"""

    def _deploy_type(self):
        return "Kubernetes"

    def _do_deploy(self, host, version):
        cmdui.info('kubectl set image deployment/app app=app:{}'.format(version))
        cmdui.info('kubectl rollout status deployment/app')

    def scale(self, replicas: int = 3):
        """扩缩容（K8s特有命令）"""
        cmdui.info('kubectl scale deployment/app --replicas={}'.format(replicas))
        cmdui.success('app 已扩缩至 {} 个副本'.format(replicas))


if __name__ == '__main__':
    import sys as _sys
    ops_map = {'base': BaseDeploy, 'docker': DockerDeploy, 'k8s': K8sDeploy}
    if len(_sys.argv) > 1 and _sys.argv[1] in ops_map:
        mode = _sys.argv.pop(1)
        ops_map[mode]().run()
    else:
        BaseDeploy().run()

`````

--- **end of file: examples/demo_inherit.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_most_easy.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 最简 demo —— 不使用 Annotated，只用基本类型注解

用法:
    python demo_most_easy.py --help
    python demo_most_easy.py hello 世界
    python demo_most_easy.py add 3 5
    python demo_most_easy.py greet 张三 --times 3
    python demo_most_easy.py say-hi --loud
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from nb_cmd import NbCmd


class Demo(NbCmd):
    """最简示例 —— 连 Annotated 都不需要"""

    def hello(self, name: str):
        """向某人打招呼"""
        print(f'你好, {name}!')

    def add(self, a: int, b: int):
        """两数相加"""
        print(f'{a} + {b} = {a + b}')

    def greet(self, name: str, times: int = 1):
        """重复问候"""
        for _ in range(times):
            print(f'Hi, {name}!')

    def say_hi(self, loud: bool = False):
        """打个招呼"""
        msg = 'HI!!!' if loud else 'hi~'
        print(msg)


if __name__ == '__main__':
    Demo().run()

`````

--- **end of file: examples/demo_most_easy.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_nb_log.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 集成 nb_log 的 demo —— 对应设计文档 7.1 Meta 配置类

演示 use_nb_log = True 时的效果:
  - self.logger 变为 nb_log 增强版 logger（彩色、文件名行号等）
  - 日志自动写入 log_file

前提: pip install nb_log

用法:
    python demo_nb_log.py --help
    python demo_nb_log.py deploy 10.0.0.1 --env staging
    python demo_nb_log.py stats
    python demo_nb_log.py --web --web-port 9911
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from typing import Annotated

from nb_cmd import NbCmd, NbCmdMeta, cmdui
from enum import Enum


class Environment(Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


class ServerTool(NbCmd):
    """服务器运维工具（启用 nb_log 增强日志）"""

    class Meta(NbCmdMeta):
        name = "server-tool"
        version = "1.0.0"

        use_nb_log = True
        log_level = "DEBUG"
        log_file = "server_tool.log"

        web_theme = "dark"

    def __init__(self, region: Annotated[str, '机房区域', 'r'],
                 timeout: Annotated[int, '超时秒数'] = 30):
        super().__init__()
        self.region = region
        self.timeout = timeout

    def before_run(self):
        """所有子命令执行前的钩子"""
        self.logger.info('服务器运维工具启动 (区域: {}, 超时: {}s)'.format(
            self.region, self.timeout))

    def after_run(self):
        """所有子命令执行后的钩子"""
        self.logger.info('运维操作完成')

    def deploy(self, host: str, env: Environment = Environment.DEV, dry_run: bool = False):
        """部署服务到目标主机"""
        self.logger.debug('参数: host={}, env={}, dry_run={}'.format(host, env.value, dry_run))

        if dry_run:
            cmdui.warning('试运行模式，不会实际部署')

        self.logger.info('正在部署到 {} (环境: {})'.format(host, env.value))
        cmdui.info('检查服务器连接...')
        cmdui.info('上传代码包...')
        cmdui.info('重启服务...')
        cmdui.success('部署完成: {} ({})'.format(host, env.value))

    def stats(self):
        """查看系统状态"""
        self.logger.info('查询系统状态')
        cmdui.kv({
            "CPU使用率": "45%",
            "内存使用": "2.3GB / 8GB",
            "磁盘使用": "120GB / 500GB",
            "运行时间": "3天12小时",
            "活跃连接": "128",
        })

    def check(self, host: str):
        """健康检查"""
        self.logger.info('检查 {} 健康状态'.format(host))
        data = [
            {"服务": "nginx", "状态": "running", "端口": 80},
            {"服务": "mysql", "状态": "running", "端口": 3306},
            {"服务": "redis", "状态": "running", "端口": 6379},
        ]
        cmdui.table(data)
        cmdui.success('所有服务运行正常')

    def logs(self, service: str = "nginx", lines: int = 10):
        """查看服务日志"""
        self.logger.info('查看 {} 最近 {} 行日志'.format(service, lines))
        for i in range(lines):
            print('[2026-04-17 15:{:02d}:00] {} - 请求处理完成'.format(30 + i, service))


if __name__ == '__main__':
    ServerTool('beijing').run()

    '''
    D:/ProgramData/Miniconda3/envs/py39b/python.exe examples/demo_nb_log.py --web --web-port 8087

    '''

`````

--- **end of file: examples/demo_nb_log.py** (project: nb_cmd) --- 

---


--- **start of file: examples/demo_subcommands.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 多层级子命令 demo —— 对应设计文档 5.3
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from typing import Annotated

from nb_cmd import NbCmd


class GitRemote(NbCmd):
    """远程仓库管理"""

    def add(self, name: Annotated[str, '远程仓库名'], url: Annotated[str, '仓库URL']):
        """添加远程仓库"""
        print('git remote add {} {}'.format(name, url))

    def remove(self, name: Annotated[str, '要删除的远程名']):
        """删除远程仓库"""
        print('git remote remove {}'.format(name))

    def show(self):
        """列出所有远程仓库"""
        print('origin  https://github.com/xxx/xxx.git (fetch)')


class GitBranch(NbCmd):
    """分支管理"""

    def create(self, name: Annotated[str, '分支名'],
               from_branch: Annotated[str, '基于哪个分支'] = "main"):
        """创建分支"""
        print('git checkout -b {} {}'.format(name, from_branch))

    def delete(self, name: Annotated[str, '分支名'],
               force: Annotated[bool, '强制删除', 'f'] = False):
        """删除分支"""
        flag = "-D" if force else "-d"
        print('git branch {} {}'.format(flag, name))

    def show(self):
        """列出所有分支"""
        print('* main')
        print('  develop')
        print('  feature/login')


class GitTool(NbCmd):
    """简易Git工具"""

    sub_commands = {
        'remote': GitRemote,
        'branch': GitBranch,
    }

    def status(self):
        """查看状态"""
        print('当前分支: main')

    def commit(self, message: Annotated[str, '提交信息', 'm'],
               all: Annotated[bool, '自动 add 所有文件', 'a'] = False):
        """提交"""
        if all:
            print('git add -A')
        print("git commit -m '{}'".format(message))


if __name__ == '__main__':
    GitTool().run()
   
    '''
    D:/ProgramData/Miniconda3/envs/py39b/python.exe examples/demo_subcommands.py --web --web-port 8084
    
    '''
`````

--- **end of file: examples/demo_subcommands.py** (project: nb_cmd) --- 

---


--- **start of file: examples/five_in_one_demo.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd 六重能力演示 —— 一次编写，六处全自动

    1. Python 直接调用（类自身完全照常使用）
    2. 自动生成 CLI 命令行
    3. 自动生成 REST API（含 Swagger 文档）
    4. 自动生成 Markdown 使用文档
    5. 自动生成 Web UI（含 WebSocket 实时控制台）
    6. 自动生成 TUI 终端交互界面（基于 Textual）

用法:
    # --- 能力 2: CLI ---
    python five_in_one_demo.py --help
    python five_in_one_demo.py ping 8.8.8.8
    python five_in_one_demo.py scan 192.168.1.0/24 --port 80 --verbose
    python five_in_one_demo.py calc 100 200

    # --- 能力 3+5: API + Web UI ---
    python five_in_one_demo.py --web

    # --- 能力 6: TUI ---
    python five_in_one_demo.py --tui

    # --- 能力 4: 自动生成 Markdown 文档 ---
    python five_in_one_demo.py gen-doc
"""
import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from nb_cmd import NbCmd, CmdGen, NbCmdMeta


class NetTool(NbCmd):
    """网络小工具 —— 一次编写，五处全自动"""

    class Meta(NbCmdMeta):
        version = '1.0.0'

    def ping(self, host: str, count: int = 4):
        """Ping 指定主机"""
        for i in range(1, count + 1):
            time.sleep(0.3)
            print(f'[{i}/{count}] PING {host} — 64 bytes, time={i * 12}ms')
        print(f'\n--- {host} ping 统计 ---')
        print(f'{count} 个包已发送, {count} 个包已接收, 0% 丢包')

    def scan(self, target: str, port: int = 80, verbose: bool = False):
        """扫描目标端口"""
        if verbose:
            print(f'[*] 正在扫描 {target}:{port} ...')
        time.sleep(0.5)
        print(f'[+] {target}:{port} — OPEN')
        if verbose:
            print(f'[*] 服务: HTTP')
            print(f'[*] 扫描完成')

    def calc(self, a: int, b: int):
        """计算两数之和"""
        result = a + b
        print(f'{a} + {b} = {result}')
        return result

    def gen_doc(self):
        """自动生成 Markdown 使用文档"""
        g = CmdGen(NetTool, script='five_in_one_demo.py', fmt='markdown')
        doc_path = os.path.join(os.path.dirname(__file__), 'five_in_one_demo_doc.md')
        g.doc(file=doc_path)
        print(f'文档已生成: {doc_path}')


if __name__ == '__main__':
    # --- 能力 1: Python 直接调用（类完全照常使用）---
    # tool = NetTool()
    # tool.ping('127.0.0.1', count=2)
    # tool.calc(100, 200)

    # --- 能力 2~6: CLI / API / Web / TUI / 文档 全自动 ---
    NetTool().run()

`````

--- **end of file: examples/five_in_one_demo.py** (project: nb_cmd) --- 

---


--- **start of file: examples/five_in_one_demo_doc.md** (project: nb_cmd) --- 

`````markdown
> *Auto-generated by nb-cmd CmdGen*

# None v1.0.0

> 网络小工具 —— 一次编写，五处全自动

## Table of Contents

- [`calc`](#calc)
- [`gen-doc`](#gen-doc)
- [`ping`](#ping)
- [`scan`](#scan)

---

## System Params

| Flag | Description |
|------|-------------|
| `-h`, `--help` | 显示帮助信息 |
| `-fh`, `--full-help` | 显示完整帮助（所有参数详情） |
| `-eh`, `--easy-help` | 显示简易帮助（argparse 原生格式） |
| `--cmd-version` | 显示版本号 |
| `--web` | 以 Web UI + REST API 模式启动 |
| `--web-port PORT` | Web UI 服务端口（用于 `--web`） |
| `--tui` | 以 TUI 终端交互模式启动 |

## Quick Start

```bash
# 查看完整帮助
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py -fh

# 查看版本
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py --cmd-version

# 启动 Web UI
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py --web

# 启动 TUI 终端交互
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py --tui
```

## 命令行约定

命令格式：`python script.py [全局参数] <子命令路径> [命令参数]`

| 标记 | 含义 |
|------|------|
| `${value}` | 带默认值的参数 — 可按需替换 |
| `$<name>` | **必填**参数 — 必须提供值 |
| `--flag`（无值） | 布尔开关，添加即启用 |

---

## Commands

### `calc`

计算两数之和

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--a` | `int` | *(required)* | - |
| `--b` | `int` | *(required)* | - |

```bash
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py calc --a $<a> --b $<b>
```

### `gen-doc`

自动生成 Markdown 使用文档

```bash
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py gen-doc
```

### `ping`

Ping 指定主机

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--host` | `str` | *(required)* | - |
| `--count` | `int` | `4` | - |

```bash
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py ping --host $<host> --count ${4}
```

### `scan`

扫描目标端口

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--target` | `str` | *(required)* | - |
| `--port` | `int` | `80` | - |
| `--verbose` | `bool` | `False` | - |

```bash
D:\ProgramData\miniconda3\python.exe five_in_one_demo.py scan --target $<target> --port ${80} --verbose
```

`````

--- **end of file: examples/five_in_one_demo_doc.md** (project: nb_cmd) --- 

---


--- **start of file: examples/ai_skill_gen_demo/ai_skill_gen_demo.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
AI Skill 自动生成演示 —— nb_cmd 第七种能力。

本示例演示如何将一个普通的 NbCmd 工具类，一键生成符合
agentskills.io 国际开放标准的 AI Skill 文件夹，让 Cursor、
Claude Code、Codex 等 AI Agent 能自动识别并正确使用你的工具。

功能:
    - 定义一个带全局参数 + 多级子命令组的 DevOps 工具
    - 一键生成 AI Skill 文件夹（仅 SKILL.md）
    - 演示 SkillGen 的各种配置选项

用法:
    # 1. 直接运行（Python 本地调用 + SkillGen 演示）
    python ai_skill_gen_demo.py

    # 2. CLI 模式
    python ai_skill_gen_demo.py --env staging deploy --version 2.1.0

    # 3. Web UI 模式
    python ai_skill_gen_demo.py --web --web-port 8086

    # 4. TUI 模式
    python ai_skill_gen_demo.py --tui
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from dataclasses import dataclass
from typing import Annotated
from nb_cmd import NbCmd, SkillGen


# ==================== 1. 全局上下文 ====================

@dataclass
class DevCtx:
    """DevOps 全局上下文"""
    env: str = 'prod'
    region: str = 'us-east'
    verbose: bool = False


# ==================== 2. 子命令组 ====================

class DbCmd(NbCmd):
    """数据库管理 (二级子命令组)"""
    nbctx: DevCtx

    def migrate(self,
                dry_run: Annotated[bool, '仅预览，不执行'] = False,
                target: Annotated[str, '目标迁移版本'] = 'latest'):
        """执行数据库迁移"""
        prefix = '[DRY-RUN]' if dry_run else '[EXEC]'
        print(f'{prefix} [{self.nbctx.env}/{self.nbctx.region}] 迁移到 {target}')

    def backup(self, compress: Annotated[bool, '启用压缩'] = True):
        """备份数据库"""
        fmt = 'tar.gz' if compress else 'sql'
        print(f'[{self.nbctx.env}] 备份数据库 → backup.{fmt}')

    def restore(self, file: Annotated[str, '备份文件路径']):
        """从备份恢复数据库"""
        print(f'[{self.nbctx.env}] 恢复数据库: {file}')


class DeployCmd(NbCmd):
    """部署管理 (二级子命令组)"""
    nbctx: DevCtx

    def rolling(self,
                version: Annotated[str, '部署版本号', 'v'],
                batch_size: Annotated[int, '每批实例数'] = 3,
                wait: Annotated[int, '每批等待秒数'] = 30):
        """滚动部署"""
        print(f'[{self.nbctx.env}] 滚动部署 v{version} (每批 {batch_size} 台, 等待 {wait}s)')

    def canary(self,
               version: Annotated[str, '部署版本号', 'v'],
               traffic: Annotated[float, '流量比例 0-1'] = 0.1):
        """金丝雀部署"""
        print(f'[{self.nbctx.env}] 金丝雀部署 v{version} (流量 {traffic*100:.0f}%)')

    def rollback(self, steps: Annotated[int, '回退步数'] = 1):
        """回滚到上一个版本"""
        print(f'[{self.nbctx.env}] 回滚 {steps} 个版本')


class MonitorCmd(NbCmd):
    """监控告警 (二级子命令组)"""
    nbctx: DevCtx

    def status(self, service: Annotated[str, '服务名'] = None):
        """查看服务状态"""
        target = service or 'all'
        print(f'[{self.nbctx.env}] 服务状态: {target}')

    def alert(self, rule: Annotated[str, '告警规则名'], threshold: Annotated[float, '阈值']):
        """配置告警规则"""
        print(f'[{self.nbctx.env}] 告警规则: {rule} > {threshold}')


# ==================== 3. 顶层工具类 ====================

class DevOpsTool(NbCmd):
    """
    DevOps 运维工具 —— AI Skill 自动生成演示。

    支持数据库管理、部署管理、监控告警三大模块。
    全局参数 env/region/verbose 自动穿透到所有子命令组。
    """
    nbctx: DevCtx

    class Meta:
        name = 'devops-tool'
        version = '1.0.0'
        description = 'DevOps 运维工具，支持数据库管理、部署、监控等操作。'
        enable_exec = False

    def __init__(self,
                 env: Annotated[str, '运行环境 prod/staging/dev'] = 'prod',
                 region: Annotated[str, '部署区域'] = 'us-east',
                 verbose: Annotated[bool, '输出详细信息'] = False):
        self.env = env
        self.region = region
        self.verbose = verbose

    def make_nbctx(self):
        return DevCtx(env=self.env, region=self.region, verbose=self.verbose)

    sub_commands = {
        'db': DbCmd,
        'deploy': DeployCmd,
        'monitor': MonitorCmd,
    }

    def health(self):
        """查看全局健康状态"""
        print(f'=== 全局健康检查 [{self.nbctx.env}/{self.nbctx.region}] ===')
        print('  Database: OK')
        print('  API:      OK')
        print('  Cache:    OK')

    def version(self):
        """查看工具版本"""
        return {'tool': 'devops-tool', 'version': '1.0.0', 'env': self.nbctx.env}


# ==================== 4. SkillGen 演示 ====================

def demo_basic():
    """演示 1: 最简用法 —— 一键生成 Skill"""
    print('\n' + '='*60)
    print('演示 1: SkillGen 最简用法')
    print('='*60)

    base_dir = os.path.join(os.path.dirname(__file__), 'skills')
    g = SkillGen(DevOpsTool, base_dir=base_dir, script='ai_skill_gen_demo.py')
    path = g.gen()
    print(f'\nSkill 已生成到: {path}')
    print(f'  SKILL.md -> {os.path.join(path, "SKILL.md")}')


def demo_full():
    """演示 2: 完整用法 —— 自定义元数据 + 环境提示"""
    print('\n' + '='*60)
    print('演示 2: SkillGen 完整用法（含环境提示 + 元数据）')
    print('='*60)

    base_dir = os.path.join(os.path.dirname(__file__), 'skills')
    priority_prompt = (
        '## 运行环境说明\n'
        '- 线上服务器：使用 `/usr/bin/python3`，脚本位于 `/opt/devops/ai_skill_gen_demo.py`\n'
        '- 本地开发：使用 `python`，脚本位于当前目录\n'
        '- 运行前请确保设置 `PYTHONPATH=/opt/devops`（线上）或项目根目录（本地）'
    )

    g = SkillGen(
        DevOpsTool,
        base_dir=base_dir,
        name='devops-tool-full',
        script='ai_skill_gen_demo.py',
        description='DevOps 运维工具 —— 数据库迁移/备份/恢复、滚动/金丝雀部署、服务监控。当需要执行运维操作时使用。',
        license='MIT',
        compatibility='Requires Python 3.8+ and nb_cmd >= 0.2.0',
        metadata={'author': 'ops-team', 'version': '1.0', 'category': 'devops'},
        user_highest_priority_skill_prompt=priority_prompt,
        include_python_examples=True,
    )
    path = g.gen()
    print(f'\nSkill 已生成到: {path}')
    print(f'  SKILL.md -> OK')


def demo_string_only():
    """演示 3: 仅生成 SKILL.md 内容字符串（不写入文件）"""
    print('\n' + '='*60)
    print('演示 3: 仅生成 SKILL.md 字符串')
    print('='*60)

    g = SkillGen(DevOpsTool, base_dir='/tmp', script='ai_skill_gen_demo.py')
    content = g.gen_skill_md()

    print(f'\nSKILL.md 内容长度: {len(content)} 字符, {len(content.splitlines())} 行')
    print('\n--- 前 20 行预览 ---')
    for i, line in enumerate(content.splitlines()[:20], 1):
        print(f'  {i:2}: {line}')
    print('  ...')


def demo_python_examples():
    """演示 4: 开启 Python 调用示例"""
    print('\n' + '='*60)
    print('演示 4: 开启 Python 调用示例')
    print('='*60)

    base_dir = os.path.join(os.path.dirname(__file__), 'skills')
    g = SkillGen(
        DevOpsTool,
        base_dir=base_dir,
        name='devops-tool-py',
        script='ai_skill_gen_demo.py',
        include_python_examples=True,
    )
    path = g.gen()
    print(f'\nSkill 已生成到: {path}')

    skill_md = os.path.join(path, 'SKILL.md')
    with open(skill_md, 'r', encoding='utf-8') as f:
        content = f.read()
    has_python = '```python' in content
    has_cli = '```bash' in content
    print(f'  包含 Python 示例: {has_python}')
    print(f'  包含 CLI 示例: {has_cli}')


def print_generated_skills():
    """打印生成的 Skill 文件夹结构"""
    print('\n' + '='*60)
    print('生成的 Skill 目录结构')
    print('='*60)

    skills_dir = os.path.join(os.path.dirname(__file__), 'skills')
    if not os.path.exists(skills_dir):
        print('(无)')
        return

    for root, dirs, files in os.walk(skills_dir):
        level = root.replace(skills_dir, '').count(os.sep)
        indent = '  ' * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = '  ' * (level + 1)
        for f in files:
            print(f'{subindent}{f}')


# ==================== 5. 入口 ====================

if __name__ == '__main__':
    import sys as _sys

    if len(_sys.argv) > 1:
        # CLI / Web / API / TUI 模式
        DevOpsTool().run()
    else:
        # 本地直接调用演示
        print('='*60)
        print('AI Skill 自动生成演示')
        print('='*60)

        # 先清理旧的生成结果
        skills_dir = os.path.join(os.path.dirname(__file__), 'skills')
        if os.path.exists(skills_dir):
            import shutil
            shutil.rmtree(skills_dir)
            print('\n已清理旧的 skills/ 目录')

        # 运行各种演示
        demo_basic()
        demo_full()
        demo_string_only()
        demo_python_examples()
        print_generated_skills()

        print('\n' + '='*60)
        print('所有演示完成！')
        print('='*60)
        print(f'\n查看生成的 Skill 文件:')
        print(f'  {skills_dir}')
        print('\n你也可以运行 CLI 模式测试:')
        print(f'  python ai_skill_gen_demo.py --env staging db migrate --dry-run')

`````

--- **end of file: examples/ai_skill_gen_demo/ai_skill_gen_demo.py** (project: nb_cmd) --- 

---


--- **start of file: examples/ai_skill_gen_demo/skills/devops-tool/SKILL.md** (project: nb_cmd) --- 

`````markdown
---
name: devops-tool
description: >-
  DevOps 运维工具，支持数据库管理、部署、监控等操作。
---
# devops-tool

## Overview

DevOps 运维工具 —— AI Skill 自动生成演示。

支持数据库管理、部署管理、监控告警三大模块。
全局参数 env/region/verbose 自动穿透到所有子命令组。

## Guidelines

- This tool is implemented using the `nb_cmd` framework. Each public instance method of the `NbCmd` subclass becomes a subcommand. You can read the `Implementation Note` to learn more details.
- If you are unsure about the specific logic of a command, inspect the source code of the corresponding method in the implementation.
- Global parameters defined in `__init__` are automatically passed to all subcommands.
- Boolean flags default to `False`; add the flag to set it to `True`.
- Subcommand groups are accessed via space, e.g., `<group> <command>`.
- Use `--help` or `-h` to see available commands and options.
- Use `--full-help` or `-fh` to see detailed parameter descriptions.

## When to Use

Activate this skill when you need to perform devops-tool-related operations, such as:
- health
- version
- db backup
- db migrate
- db restore
- deploy canary
- deploy rollback
- deploy rolling
- monitor alert
- monitor status

## Command Structure

### CLI
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py [global_params] <command_path> [command_params]
```

**Parameter conventions:**
- `${value}` — parameter with default value (replace as needed)
- `$<name>` — **required** parameter (must provide a value)
- `--flag` (no value) — boolean switch (add to enable)

## Global Parameters

These parameters are defined in `__init__` and passed to all subcommands automatically.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--env` | `str` | `prod` | 运行环境 prod/staging/dev |
| `--region` | `str` | `us-east` | 部署区域 |
| `--verbose` | `bool` | `False` | 输出详细信息 |

## Commands

### `health`

查看全局健康状态

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| *(none)* | — | — | This command takes no parameters. |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose health
```

### `version`

查看工具版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| *(none)* | — | — | This command takes no parameters. |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose version
```

### `db` *(subcommand group)*

数据库管理 (二级子命令组)

### `db backup`

备份数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--compress` | `bool` | `True` | 启用压缩 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db backup
```

### `db migrate`

执行数据库迁移

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--dry-run` | `bool` | `False` | 仅预览，不执行 |
| `--target` | `str` | `latest` | 目标迁移版本 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db migrate --dry-run --target ${latest}
```

### `db restore`

从备份恢复数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--file` | `str` | *(required)* | 备份文件路径 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db restore --file $<file>
```

### `deploy` *(subcommand group)*

部署管理 (二级子命令组)

### `deploy canary`

金丝雀部署

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 部署版本号 |
| `--traffic` | `float` | `0.1` | 流量比例 0-1 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy canary --version $<version> --traffic ${0.1}
```

### `deploy rollback`

回滚到上一个版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--steps` | `int` | `1` | 回退步数 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy rollback --steps ${1}
```

### `deploy rolling`

滚动部署

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 部署版本号 |
| `--batch-size` | `int` | `3` | 每批实例数 |
| `--wait` | `int` | `30` | 每批等待秒数 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy rolling --version $<version> --batch-size ${3} --wait ${30}
```

### `monitor` *(subcommand group)*

监控告警 (二级子命令组)

### `monitor alert`

配置告警规则

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--rule` | `str` | *(required)* | 告警规则名 |
| `--threshold` | `float` | *(required)* | 阈值 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose monitor alert --rule $<rule> --threshold $<threshold>
```

### `monitor status`

查看服务状态

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--service` | `str` | `None` | 服务名 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose monitor status --service ${None}
```


## Implementation Note

This tool is built on the `nb_cmd` framework. Here is how the Python source code maps to CLI commands:

1. **Class = Top-level command group**. The main class `DevOpsTool` inherits from `NbCmd`.
   Each public instance method of this class becomes a top-level subcommand.

2. **`sub_commands` dict = Nested command groups**. When a class defines:
   ```python
   sub_commands = {"db": DbCmd, "deploy": DeployCmd}
   ```
   the keys become the command path segments, and the values are other `NbCmd` subclasses.
   So `DbCmd.backup(...)` in Python maps to `db backup` on the CLI.
   Deeper nesting works the same way: if `DbCmd` itself has `sub_commands = {"ops": OpsCmd}`,
   then `OpsCmd.deploy(...)` maps to `db ops deploy` on the CLI.

3. **`__init__` params = Global CLI options**. Parameters of `__init__(self, ...)` become global options:
   - `str` / `int` / `float` params → `--name value` (e.g., `--env prod`, `--port 8080`)
   - `bool` params with default `False` → `--name` (no value, presence means `True`)
   - `bool` params with default `True` → `--no-name` (no value, presence means `False`)
   These options are automatically passed to all subcommands and subcommand groups.
   Inside subcommands, global parameters are accessed via instance attributes or `self.nbctx`.

4. **Method params = Command-level options**. Same parameter-to-flag rules as above:
   - `str` / `int` / `float` → `--name value`
   - `bool` default `False` → `--name`
   - `bool` default `True` → `--no-name`
   - **No default value** → required parameter (marked as `*(required)*` in the parameter table)
   For example:
   - `def backup(self, compress: bool = True)` produces `--compress` (default True, so `--no-compress` to disable)
   - `def restore(self, file: str)` produces `--file` (required, no default)
   - Parameter descriptions and short aliases (e.g., `--version, -v`) come from `Annotated[type, "description", "-v"]`.

5. **Method docstring = Command description**. The first line of a method's docstring becomes the help text for that command.

6. **Return values**. If a method returns a value, `nb_cmd` automatically prints it in CLI mode.

7. **Python direct call vs CLI**. In Python you instantiate the class with global params:
   ```python
   app = DevOpsTool(env="staging", region="us-west")
   app.db.backup(compress=False)
   ```
   The equivalent CLI is:
   ```bash
   python ai_skill_gen_demo.py --env staging --region us-west db backup --no-compress
   ```

If a command's behavior is unclear, locate the corresponding method in the source code of `DevOpsTool` (or its nested `NbCmd` subclasses) and read the implementation directly.

`````

--- **end of file: examples/ai_skill_gen_demo/skills/devops-tool/SKILL.md** (project: nb_cmd) --- 

---


--- **start of file: examples/ai_skill_gen_demo/skills/devops-tool-full/SKILL.md** (project: nb_cmd) --- 

`````markdown
---
name: devops-tool-full
description: >-
  DevOps 运维工具 —— 数据库迁移/备份/恢复、滚动/金丝雀部署、服务监控。当需要执行运维操作时使用。
license: MIT
compatibility: Requires Python 3.8+ and nb_cmd >= 0.2.0
metadata:
  author: "ops-team"
  version: "1.0"
  category: "devops"
---
# devops-tool

## Overview

DevOps 运维工具 —— AI Skill 自动生成演示。

支持数据库管理、部署管理、监控告警三大模块。
全局参数 env/region/verbose 自动穿透到所有子命令组。

## Important

## 运行环境说明
- 线上服务器：使用 `/usr/bin/python3`，脚本位于 `/opt/devops/ai_skill_gen_demo.py`
- 本地开发：使用 `python`，脚本位于当前目录
- 运行前请确保设置 `PYTHONPATH=/opt/devops`（线上）或项目根目录（本地）

## Guidelines

- This tool is implemented using the `nb_cmd` framework. Each public instance method of the `NbCmd` subclass becomes a subcommand. You can read the `Implementation Note` to learn more details.
- If you are unsure about the specific logic of a command, inspect the source code of the corresponding method in the implementation.
- Global parameters defined in `__init__` are automatically passed to all subcommands.
- Boolean flags default to `False`; add the flag to set it to `True`.
- Subcommand groups are accessed via space, e.g., `<group> <command>`.
- Use `--help` or `-h` to see available commands and options.
- Use `--full-help` or `-fh` to see detailed parameter descriptions.

## When to Use

Activate this skill when you need to perform devops-tool-related operations, such as:
- health
- version
- db backup
- db migrate
- db restore
- deploy canary
- deploy rollback
- deploy rolling
- monitor alert
- monitor status

## Command Structure

### CLI
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py [global_params] <command_path> [command_params]
```

### Python
```python
from ai_skill_gen_demo import DevOpsTool
app = DevOpsTool()  # pass global params if needed
# app.subcommand.method(param=value)
```

**Parameter conventions:**
- `${value}` — parameter with default value (replace as needed)
- `$<name>` — **required** parameter (must provide a value)
- `--flag` (no value) — boolean switch (add to enable)

## Global Parameters

These parameters are defined in `__init__` and passed to all subcommands automatically.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--env` | `str` | `prod` | 运行环境 prod/staging/dev |
| `--region` | `str` | `us-east` | 部署区域 |
| `--verbose` | `bool` | `False` | 输出详细信息 |

## Commands

### `health`

查看全局健康状态

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| *(none)* | — | — | This command takes no parameters. |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose health
```

**Python:**
```python
app.health()
```

### `version`

查看工具版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| *(none)* | — | — | This command takes no parameters. |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose version
```

**Python:**
```python
app.version()
```

### `db` *(subcommand group)*

数据库管理 (二级子命令组)

### `db backup`

备份数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--compress` | `bool` | `True` | 启用压缩 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db backup
```

**Python:**
```python
app.db.backup(compress=True)
```

### `db migrate`

执行数据库迁移

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--dry-run` | `bool` | `False` | 仅预览，不执行 |
| `--target` | `str` | `latest` | 目标迁移版本 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db migrate --dry-run --target ${latest}
```

**Python:**
```python
app.db.migrate(dry_run=False, target="latest")
```

### `db restore`

从备份恢复数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--file` | `str` | *(required)* | 备份文件路径 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db restore --file $<file>
```

**Python:**
```python
app.db.restore(file=<file>)
```

### `deploy` *(subcommand group)*

部署管理 (二级子命令组)

### `deploy canary`

金丝雀部署

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 部署版本号 |
| `--traffic` | `float` | `0.1` | 流量比例 0-1 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy canary --version $<version> --traffic ${0.1}
```

**Python:**
```python
app.deploy.canary(version=<version>, traffic=0.1)
```

### `deploy rollback`

回滚到上一个版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--steps` | `int` | `1` | 回退步数 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy rollback --steps ${1}
```

**Python:**
```python
app.deploy.rollback(steps=1)
```

### `deploy rolling`

滚动部署

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 部署版本号 |
| `--batch-size` | `int` | `3` | 每批实例数 |
| `--wait` | `int` | `30` | 每批等待秒数 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy rolling --version $<version> --batch-size ${3} --wait ${30}
```

**Python:**
```python
app.deploy.rolling(version=<version>, batch_size=3, wait=30)
```

### `monitor` *(subcommand group)*

监控告警 (二级子命令组)

### `monitor alert`

配置告警规则

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--rule` | `str` | *(required)* | 告警规则名 |
| `--threshold` | `float` | *(required)* | 阈值 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose monitor alert --rule $<rule> --threshold $<threshold>
```

**Python:**
```python
app.monitor.alert(rule=<rule>, threshold=<threshold>)
```

### `monitor status`

查看服务状态

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--service` | `str` | `None` | 服务名 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose monitor status --service ${None}
```

**Python:**
```python
app.monitor.status(service=None)
```


## Implementation Note

This tool is built on the `nb_cmd` framework. Here is how the Python source code maps to CLI commands:

1. **Class = Top-level command group**. The main class `DevOpsTool` inherits from `NbCmd`.
   Each public instance method of this class becomes a top-level subcommand.

2. **`sub_commands` dict = Nested command groups**. When a class defines:
   ```python
   sub_commands = {"db": DbCmd, "deploy": DeployCmd}
   ```
   the keys become the command path segments, and the values are other `NbCmd` subclasses.
   So `DbCmd.backup(...)` in Python maps to `db backup` on the CLI.
   Deeper nesting works the same way: if `DbCmd` itself has `sub_commands = {"ops": OpsCmd}`,
   then `OpsCmd.deploy(...)` maps to `db ops deploy` on the CLI.

3. **`__init__` params = Global CLI options**. Parameters of `__init__(self, ...)` become global options:
   - `str` / `int` / `float` params → `--name value` (e.g., `--env prod`, `--port 8080`)
   - `bool` params with default `False` → `--name` (no value, presence means `True`)
   - `bool` params with default `True` → `--no-name` (no value, presence means `False`)
   These options are automatically passed to all subcommands and subcommand groups.
   Inside subcommands, global parameters are accessed via instance attributes or `self.nbctx`.

4. **Method params = Command-level options**. Same parameter-to-flag rules as above:
   - `str` / `int` / `float` → `--name value`
   - `bool` default `False` → `--name`
   - `bool` default `True` → `--no-name`
   - **No default value** → required parameter (marked as `*(required)*` in the parameter table)
   For example:
   - `def backup(self, compress: bool = True)` produces `--compress` (default True, so `--no-compress` to disable)
   - `def restore(self, file: str)` produces `--file` (required, no default)
   - Parameter descriptions and short aliases (e.g., `--version, -v`) come from `Annotated[type, "description", "-v"]`.

5. **Method docstring = Command description**. The first line of a method's docstring becomes the help text for that command.

6. **Return values**. If a method returns a value, `nb_cmd` automatically prints it in CLI mode.

7. **Python direct call vs CLI**. In Python you instantiate the class with global params:
   ```python
   app = DevOpsTool(env="staging", region="us-west")
   app.db.backup(compress=False)
   ```
   The equivalent CLI is:
   ```bash
   python ai_skill_gen_demo.py --env staging --region us-west db backup --no-compress
   ```

If a command's behavior is unclear, locate the corresponding method in the source code of `DevOpsTool` (or its nested `NbCmd` subclasses) and read the implementation directly.

`````

--- **end of file: examples/ai_skill_gen_demo/skills/devops-tool-full/SKILL.md** (project: nb_cmd) --- 

---


--- **start of file: examples/ai_skill_gen_demo/skills/devops-tool-py/SKILL.md** (project: nb_cmd) --- 

`````markdown
---
name: devops-tool-py
description: >-
  DevOps 运维工具，支持数据库管理、部署、监控等操作。
---
# devops-tool

## Overview

DevOps 运维工具 —— AI Skill 自动生成演示。

支持数据库管理、部署管理、监控告警三大模块。
全局参数 env/region/verbose 自动穿透到所有子命令组。

## Guidelines

- This tool is implemented using the `nb_cmd` framework. Each public instance method of the `NbCmd` subclass becomes a subcommand. You can read the `Implementation Note` to learn more details.
- If you are unsure about the specific logic of a command, inspect the source code of the corresponding method in the implementation.
- Global parameters defined in `__init__` are automatically passed to all subcommands.
- Boolean flags default to `False`; add the flag to set it to `True`.
- Subcommand groups are accessed via space, e.g., `<group> <command>`.
- Use `--help` or `-h` to see available commands and options.
- Use `--full-help` or `-fh` to see detailed parameter descriptions.

## When to Use

Activate this skill when you need to perform devops-tool-related operations, such as:
- health
- version
- db backup
- db migrate
- db restore
- deploy canary
- deploy rollback
- deploy rolling
- monitor alert
- monitor status

## Command Structure

### CLI
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py [global_params] <command_path> [command_params]
```

### Python
```python
from ai_skill_gen_demo import DevOpsTool
app = DevOpsTool()  # pass global params if needed
# app.subcommand.method(param=value)
```

**Parameter conventions:**
- `${value}` — parameter with default value (replace as needed)
- `$<name>` — **required** parameter (must provide a value)
- `--flag` (no value) — boolean switch (add to enable)

## Global Parameters

These parameters are defined in `__init__` and passed to all subcommands automatically.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--env` | `str` | `prod` | 运行环境 prod/staging/dev |
| `--region` | `str` | `us-east` | 部署区域 |
| `--verbose` | `bool` | `False` | 输出详细信息 |

## Commands

### `health`

查看全局健康状态

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| *(none)* | — | — | This command takes no parameters. |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose health
```

**Python:**
```python
app.health()
```

### `version`

查看工具版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| *(none)* | — | — | This command takes no parameters. |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose version
```

**Python:**
```python
app.version()
```

### `db` *(subcommand group)*

数据库管理 (二级子命令组)

### `db backup`

备份数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--compress` | `bool` | `True` | 启用压缩 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db backup
```

**Python:**
```python
app.db.backup(compress=True)
```

### `db migrate`

执行数据库迁移

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--dry-run` | `bool` | `False` | 仅预览，不执行 |
| `--target` | `str` | `latest` | 目标迁移版本 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db migrate --dry-run --target ${latest}
```

**Python:**
```python
app.db.migrate(dry_run=False, target="latest")
```

### `db restore`

从备份恢复数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--file` | `str` | *(required)* | 备份文件路径 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose db restore --file $<file>
```

**Python:**
```python
app.db.restore(file=<file>)
```

### `deploy` *(subcommand group)*

部署管理 (二级子命令组)

### `deploy canary`

金丝雀部署

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 部署版本号 |
| `--traffic` | `float` | `0.1` | 流量比例 0-1 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy canary --version $<version> --traffic ${0.1}
```

**Python:**
```python
app.deploy.canary(version=<version>, traffic=0.1)
```

### `deploy rollback`

回滚到上一个版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--steps` | `int` | `1` | 回退步数 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy rollback --steps ${1}
```

**Python:**
```python
app.deploy.rollback(steps=1)
```

### `deploy rolling`

滚动部署

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 部署版本号 |
| `--batch-size` | `int` | `3` | 每批实例数 |
| `--wait` | `int` | `30` | 每批等待秒数 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose deploy rolling --version $<version> --batch-size ${3} --wait ${30}
```

**Python:**
```python
app.deploy.rolling(version=<version>, batch_size=3, wait=30)
```

### `monitor` *(subcommand group)*

监控告警 (二级子命令组)

### `monitor alert`

配置告警规则

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--rule` | `str` | *(required)* | 告警规则名 |
| `--threshold` | `float` | *(required)* | 阈值 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose monitor alert --rule $<rule> --threshold $<threshold>
```

**Python:**
```python
app.monitor.alert(rule=<rule>, threshold=<threshold>)
```

### `monitor status`

查看服务状态

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--service` | `str` | `None` | 服务名 |

**CLI:**
```bash
D:\ProgramData\Miniconda3\envs\py39b\python.exe ai_skill_gen_demo.py --env ${prod} --region ${us-east} --verbose monitor status --service ${None}
```

**Python:**
```python
app.monitor.status(service=None)
```


## Implementation Note

This tool is built on the `nb_cmd` framework. Here is how the Python source code maps to CLI commands:

1. **Class = Top-level command group**. The main class `DevOpsTool` inherits from `NbCmd`.
   Each public instance method of this class becomes a top-level subcommand.

2. **`sub_commands` dict = Nested command groups**. When a class defines:
   ```python
   sub_commands = {"db": DbCmd, "deploy": DeployCmd}
   ```
   the keys become the command path segments, and the values are other `NbCmd` subclasses.
   So `DbCmd.backup(...)` in Python maps to `db backup` on the CLI.
   Deeper nesting works the same way: if `DbCmd` itself has `sub_commands = {"ops": OpsCmd}`,
   then `OpsCmd.deploy(...)` maps to `db ops deploy` on the CLI.

3. **`__init__` params = Global CLI options**. Parameters of `__init__(self, ...)` become global options:
   - `str` / `int` / `float` params → `--name value` (e.g., `--env prod`, `--port 8080`)
   - `bool` params with default `False` → `--name` (no value, presence means `True`)
   - `bool` params with default `True` → `--no-name` (no value, presence means `False`)
   These options are automatically passed to all subcommands and subcommand groups.
   Inside subcommands, global parameters are accessed via instance attributes or `self.nbctx`.

4. **Method params = Command-level options**. Same parameter-to-flag rules as above:
   - `str` / `int` / `float` → `--name value`
   - `bool` default `False` → `--name`
   - `bool` default `True` → `--no-name`
   - **No default value** → required parameter (marked as `*(required)*` in the parameter table)
   For example:
   - `def backup(self, compress: bool = True)` produces `--compress` (default True, so `--no-compress` to disable)
   - `def restore(self, file: str)` produces `--file` (required, no default)
   - Parameter descriptions and short aliases (e.g., `--version, -v`) come from `Annotated[type, "description", "-v"]`.

5. **Method docstring = Command description**. The first line of a method's docstring becomes the help text for that command.

6. **Return values**. If a method returns a value, `nb_cmd` automatically prints it in CLI mode.

7. **Python direct call vs CLI**. In Python you instantiate the class with global params:
   ```python
   app = DevOpsTool(env="staging", region="us-west")
   app.db.backup(compress=False)
   ```
   The equivalent CLI is:
   ```bash
   python ai_skill_gen_demo.py --env staging --region us-west db backup --no-compress
   ```

If a command's behavior is unclear, locate the corresponding method in the source code of `DevOpsTool` (or its nested `NbCmd` subclasses) and read the implementation directly.

`````

--- **end of file: examples/ai_skill_gen_demo/skills/devops-tool-py/SKILL.md** (project: nb_cmd) --- 

---


--- **start of file: examples/github_cli_demos/gh_click.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
GitHub CLI — Click 实现。

演示 Click 在多层级子命令 + 全局参数场景下的典型写法：
  - 每个子命令/组必须 @click.pass_context
  - 取值靠 ctx.obj['key']（字符串键，无 IDE 补全）
  - 装饰器随层级指数叠加

用法:
    python gh_click.py -R myorg/api issue list --state all
    python gh_click.py --repo prod/web --debug pr merge --number 42 --squash
    python gh_click.py -R team/cli --no-prompt --auth-token ghp_xxx issue create --title "Deploy failed"
"""
import click


@click.group()
@click.option('--repo', '-R', required=True, help='目标仓库 (owner/repo)')
@click.option('--hostname', default=None, help='GitHub Enterprise 域名')
@click.option('--auth-token', default=None, help='访问令牌 (覆盖配置)')
@click.option('--debug', is_flag=True, help='开启调试模式')
@click.option('--no-prompt', is_flag=True, help='禁用交互提示')
@click.pass_context
def cli(ctx, repo, hostname, auth_token, debug, no_prompt):
    """gh-cli: GitHub 命令行工具 (Click 版)"""
    ctx.ensure_object(dict)
    ctx.obj.update(
        repo=repo,
        hostname=hostname,
        auth_token=auth_token,
        debug=debug,
        no_prompt=no_prompt,
    )


# ==================== issue 子命令组 ====================

@cli.group()
@click.pass_context
def issue(ctx):
    """Issue 管理"""
    pass


@issue.command('list')
@click.option('--state', default='open', type=click.Choice(['open', 'closed', 'all']),
              help='Issue 状态过滤')
@click.option('--label', default=None, help='按标签过滤')
@click.option('--limit', default=30, type=int, help='最大返回数量')
@click.pass_context
def issue_list(ctx, state, label, limit):
    """列出 Issues"""
    c = ctx.obj
    print(f"[issue list] repo={c['repo']}, state={state}, label={label}, limit={limit}")
    if c['debug']:
        print(f"  DEBUG: hostname={c['hostname']}, no_prompt={c['no_prompt']}")


@issue.command('create')
@click.option('--title', '-t', required=True, help='Issue 标题')
@click.option('--body', '-b', default='', help='Issue 正文')
@click.option('--assignee', '-a', default=None, help='指定负责人')
@click.pass_context
def issue_create(ctx, title, body, assignee):
    """创建新 Issue"""
    c = ctx.obj
    print(f"[issue create] repo={c['repo']}, title={title}")
    if body:
        print(f"  body={body}")
    if assignee:
        print(f"  assignee={assignee}")


@issue.command('view')
@click.argument('number', type=int)
@click.pass_context
def issue_view(ctx, number):
    """查看 Issue 详情"""
    c = ctx.obj
    print(f"[issue view] repo={c['repo']}, #{number}")


# ==================== pr 子命令组 ====================

@cli.group()
@click.pass_context
def pr(ctx):
    """Pull Request 管理"""
    pass


@pr.command('list')
@click.option('--state', default='open', type=click.Choice(['open', 'closed', 'merged', 'all']),
              help='PR 状态过滤')
@click.option('--author', default=None, help='按作者过滤')
@click.pass_context
def pr_list(ctx, state, author):
    """列出 Pull Requests"""
    c = ctx.obj
    print(f"[pr list] repo={c['repo']}, state={state}, author={author}")


@pr.command('create')
@click.option('--title', '-t', required=True, help='PR 标题')
@click.option('--body', '-b', default='', help='PR 描述')
@click.option('--base', default='main', help='目标分支')
@click.option('--draft', is_flag=True, help='创建为 Draft PR')
@click.pass_context
def pr_create(ctx, title, body, base, draft):
    """创建新 Pull Request"""
    c = ctx.obj
    kind = 'Draft PR' if draft else 'PR'
    print(f"[pr create] repo={c['repo']}, {kind}: {title} → {base}")
    if c['debug']:
        tok = '***' if c['auth_token'] else 'default'
        print(f"  DEBUG: auth={tok}")


@pr.command('merge')
@click.option('--number', '-n', required=True, type=int, help='PR 编号')
@click.option('--squash', is_flag=True, help='Squash 合并')
@click.option('--delete-branch', is_flag=True, help='合并后删除分支')
@click.pass_context
def pr_merge(ctx, number, squash, delete_branch):
    """合并 Pull Request"""
    c = ctx.obj
    method = 'squash' if squash else 'merge'
    tok = '***' if c['auth_token'] else 'default'
    print(f"[pr merge] repo={c['repo']}, #{number}, method={method}, auth={tok}")
    if delete_branch:
        print("  → 合并后将删除源分支")


# ==================== repo 子命令组 ====================

@cli.group()
@click.pass_context
def repo(ctx):
    """仓库管理"""
    pass


@repo.command('clone')
@click.argument('target_repo')
@click.option('--depth', default=0, type=int, help='浅克隆深度 (0=完整)')
@click.pass_context
def repo_clone(ctx, target_repo, depth):
    """克隆仓库"""
    c = ctx.obj
    depth_info = f' (depth={depth})' if depth else ''
    print(f"[repo clone] {target_repo}{depth_info}")
    if c['hostname']:
        print(f"  → 从 {c['hostname']} 克隆")


@repo.command('fork')
@click.option('--org', default=None, help='Fork 到指定组织')
@click.pass_context
def repo_fork(ctx, org):
    """Fork 仓库"""
    c = ctx.obj
    target = f" → {org}" if org else ''
    print(f"[repo fork] {c['repo']}{target}")


if __name__ == '__main__':
    cli()

`````

--- **end of file: examples/github_cli_demos/gh_click.py** (project: nb_cmd) --- 

---


--- **start of file: examples/github_cli_demos/gh_comparison.md** (project: nb_cmd) --- 

`````markdown
---
noteId: "e71b7b113bc511f1a9787921be2453f8"
tags: []

---

# GitHub CLI 三框架实现对比：nb_cmd vs Click vs Typer

> 以真实 GitHub CLI (`gh`) 的语义为基准，统一实现 **5 个全局参数 + 3 个子命令组 + 9 个子命令**，对比三个 Python CLI 框架的代码质量和开发体验。

## 场景覆盖

| 命令路径 | 功能 | 参数 |
|---------|------|------|
| `issue list` | 列出 Issues | `--state`, `--label`, `--limit` |
| `issue create` | 创建 Issue | `--title/-t`, `--body/-b`, `--assignee/-a` |
| `issue view` | 查看 Issue | `NUMBER` (必填) |
| `pr list` | 列出 PRs | `--state`, `--author` |
| `pr create` | 创建 PR | `--title/-t`, `--body/-b`, `--base`, `--draft` |
| `pr merge` | 合并 PR | `--number/-n`, `--squash`, `--delete-branch` |
| `repo clone` | 克隆仓库 | `TARGET_REPO` (必填), `--depth` |
| `repo fork` | Fork 仓库 | `--org` |
| `status` | 全局配置 | (无) |

**全局参数**：`--repo/-R`, `--hostname`, `--auth-token`, `--debug`, `--no-prompt`

---

## 终端调用（三框架完全一致）

```bash
# 基础调用
python gh_xxx.py --repo myorg/api issue list --state all

# 覆盖全局参数 + 执行二级命令
python gh_xxx.py --repo prod/web --debug pr merge --number 42 --squash

# CI 场景（禁用交互 + 指定 Token）
python gh_xxx.py -R team/cli --no-prompt --auth-token ghp_xxx issue create --title "Deploy failed"
```

---

## 代码量化对比

| 指标 | Click | Typer | nb_cmd |
|------|-------|-------|--------|
| **CLI 定义代码行** | 108 | 94 | 104 |
| **装饰器数量** | **49 个** | 9 个 | **0 个** |
| **全局参数传递方式** | `ctx.obj['repo']` 字典 | `state['repo']` 全局变量 | `self.nbctx.repo` 强类型 |
| **IDE 补全/跳转** | ❌ 字符串键 | ❌ 字符串键 | ✅ dataclass 字段 |
| **子命令独立性** | ❌ 绑定到 `@cli.group` | ❌ 绑定到 `app` 实例 | ✅ 纯 Class，可单独实例化 |
| **自动文档生成** | ❌ 需 `sphinx-click` | ❌ 只搬运 `--help` | ✅ `CmdGen` 一行生成 Markdown |
| **Web UI 支持** | ❌ 需额外重写 | ❌ 需额外重写 | ✅ `--web` 一键启动 |
| **REST API 支持** | ❌ 需额外重写 | ❌ 需额外重写 | ✅ 内置 |

---

## 核心差异详解

### 1. 全局参数定义与传递

**Click** — 装饰器 + `ctx.obj` 字典：

```python
@click.group()
@click.option('--repo', '-R', required=True, help='...')
@click.option('--hostname', default=None, help='...')
@click.option('--auth-token', default=None, help='...')
@click.option('--debug', is_flag=True, help='...')
@click.option('--no-prompt', is_flag=True, help='...')
@click.pass_context
def cli(ctx, repo, hostname, auth_token, debug, no_prompt):
    ctx.ensure_object(dict)
    ctx.obj.update(repo=repo, hostname=hostname, ...)
```

每个子命令/组必须加 `@click.pass_context`，取值靠 `ctx.obj['repo']`（拼错 key 运行时才爆发）。

**Typer** — `@callback` + 模块全局字典：

```python
state = {}  # ⚠️ 破坏封装，非线程安全

@app.callback()
def main(repo: str = typer.Option(..., "--repo", "-R", help="..."), ...):
    state.update(repo=repo, ...)
```

所有子命令读 `state['repo']` — 模块级全局变量，无法独立测试、并发时会串。

**nb_cmd** — `__init__` + `make_nbctx()` 强类型上下文：

```python
@dataclass
class GhCtx:
    repo: Optional[str] = None
    hostname: Optional[str] = None
    auth_token: Optional[str] = None
    debug: bool = False
    no_prompt: bool = False

class GhCli(NbCmd):
    nbctx: GhCtx  # ← IDE 补全入口

    def __init__(self,
                 repo: Annotated[str, '目标仓库', 'R'] = None, ...):
        self.repo = repo; ...

    def make_nbctx(self):
        return GhCtx(repo=self.repo, ...)

    sub_commands = {'issue': IssueCmd, 'pr': PrCmd, 'repo': RepoCmd}
```

`self.nbctx.repo` 在 IDE 中自动补全、可跳转到 `GhCtx` 定义。拼写错误编译期就能发现。

---

### 2. 子命令组定义

**Click** — 每新增一个子命令组需要 1 个 `@cli.group` + N 个 `@group.command` + N 个 `@click.pass_context`：

```python
@cli.group()
@click.pass_context
def issue(ctx): pass

@issue.command('list')
@click.option('--state', ...)
@click.pass_context
def issue_list(ctx, state):
    c = ctx.obj  # 再次字典取值
```

**Typer** — 每新增一个子命令组需要 `Typer()` 实例 + `add_typer()` 注册：

```python
issue_app = typer.Typer(help="Issue 管理")
app.add_typer(issue_app, name="issue")

@issue_app.command("list")
def issue_list(state_filter: str = typer.Option("open", "--state", ...)):
    print(f"repo={state['repo']}")  # 全局变量取值
```

**nb_cmd** — 纯 Class 继承，一行声明层级：

```python
class IssueCmd(NbCmd):
    """Issue 管理"""
    nbctx: GhCtx  # IDE 补全

    def list(self, state: Annotated[str, 'Issue 状态'] = 'open', ...):
        print(f"repo={self.nbctx.repo}")  # 强类型取值
```

新增子命令组只需：写一个 Class + 在父级 `sub_commands` 加一项。全局参数自动穿透。

---

### 3. 子命令独立测试

**Click/Typer** — 子命令强绑定到 `cli` / `app` 实例，无法脱离框架调用：

```python
# Click：无法直接调用 issue_list
# Typer：需要 state 全局变量预先填充，且非线程安全
```

**nb_cmd** — 子命令组是独立 Class，可脱离框架运行/测试：

```python
# 直接实例化 + 注入 ctx，不需要启动整个 CLI 框架
ctx = GhCtx(repo='myorg/api', debug=True)
issue = IssueCmd()
issue.nbctx = ctx
issue.list(state='all')       # ✅ 直接调用
issue.create(title='Bug')     # ✅ 直接调用
```

---

### 4. 自动文档生成（nb_cmd 独有）

一行代码生成完整 Markdown 文档，包含目录、参数表格、默认值标注、可复制 bash 命令行模板：

```python
from nb_cmd import CmdGen

g = CmdGen(GhCli, script='gh_nb_cmd.py', fmt='markdown')
g.doc(file='gh_nb_cmd_gen_doc.md')
```

生成结果包含：
- Table of Contents（自动目录）
- System Params / Global Params 表格
- 每个命令的参数表格（Flag / Type / Default / Description）
- 每个命令的可复制 bash 命令行模板

Click 需要第三方 `sphinx-click`，Typer 只搬运 `--help` 纯文本输出。

---

### 5. 多模式支持（nb_cmd 独有）

同一套代码自动获得 5 种能力：

```bash
# 1. Python 直接调用
issue = IssueCmd(); issue.nbctx = GhCtx(repo='myorg/api')
issue.list(state='all')

# 2. CLI 命令行
python gh_nb_cmd.py --repo myorg/api issue list

# 3. REST API（随 Web 一起启动）
curl -X POST http://localhost:8090/issue/list \
  -d '{"state": "all", "init_params": {"repo": "myorg/api"}}'

# 4. Web UI（一键启动，含表单/实时输出/Swagger）
python gh_nb_cmd.py --web --web-port 8090

# 5. Markdown 文档自动生成
CmdGen(GhCli, script='gh_nb_cmd.py').doc(file='gh_nb_cmd_gen_doc.md')
```

Click 和 Typer 只提供 CLI，需额外用 FastAPI/Flask 重写才能支持 Web/API/TUI。

---

## 碾压点总结

| 维度 | nb_cmd 优势 |
|------|------------|
| **上下文传递** | `make_nbctx()` → `self.nbctx.xxx` 强类型穿透，终结了 `ctx.obj` 字典和全局变量反模式 |
| **装饰器数量** | 49 (Click) → 0 (nb_cmd)，代码噪音归零 |
| **IDE 体验** | `self.nbctx.repo` 自动补全+类型校验，拼写错误静态可查 |
| **可测试性** | 子命令组是独立 Class，可脱离框架单独实例化/注入 ctx/单元测试 |
| **文档生成** | `CmdGen` 一行生成完整 Markdown，Click/Typer 无此能力 |
| **多模式支持** | `--web` 一键获得 Web UI + REST API，Click/Typer 需额外重写 |
| **新增子命令成本** | 写 Class + `sub_commands` 加一项，全局逻辑零改动 |
| **架构映射** | `__init__` 即"连接/环境配置"，完美映射 gh/aws/kubectl 的全局参数语义 |

---

## 文件清单

| 文件 | 说明 |
|------|------|
| `gh_click.py` | Click 实现（168 行，49 个装饰器） |
| `gh_typer.py` | Typer 实现（154 行，9 个装饰器） |
| `gh_nb_cmd.py` | nb_cmd 实现（216 行含本地演示，0 个装饰器） |
| `gh_nb_cmd_gen_doc.md` | nb_cmd 自动生成的 Markdown 文档（CmdGen 产出） |
| `gh_comparison.md` | 本文件 — 三框架对比总结 |

`````

--- **end of file: examples/github_cli_demos/gh_comparison.md** (project: nb_cmd) --- 

---


--- **start of file: examples/github_cli_demos/gh_nb_cmd.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
GitHub CLI — nb_cmd 实现。

演示 nb_cmd 在多层级子命令 + 全局参数场景下的碾压优势：
  - 零装饰器：所有命令通过纯 Class + 方法定义
  - __init__ 直接赋值 self.nbctx：无需 make_nbctx()，CLI/Web/TUI/API 所有模式均正确传参
  - self.nbctx 强类型 + IDE 补全：子命令组通过类型注解获取代码补全和跳转
  - 子命令独立可测：每个 NbCmd 子类可脱离父级单独实例化和测试
  - CmdGen 自动文档：一行代码生成完整 Markdown 文档

用法:
    1. CLI:  python gh_nb_cmd.py --repo myorg/api issue list --state all
    2. CLI:  python gh_nb_cmd.py --repo prod/web --debug pr merge --number 42 --squash
    3. CLI:  python gh_nb_cmd.py -R team/cli --no-prompt --auth-token ghp_xxx issue create --title "Deploy failed"
    4. Web:  python gh_nb_cmd.py --web --web-port 8090
    5. 本地: python gh_nb_cmd.py  (无参数，进入本地演示)

D:\ProgramData\miniconda3\envs\py39b\python.exe D:/codes/nb_cmd/examples/git_demos/git_nb_cmd.py --tui

"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from dataclasses import dataclass
from typing import Optional
from typing import Annotated
from nb_cmd import NbCmd, CmdGen
from nb_cmd.core.meta import NbCmdMeta


# ==================== 1. 定义全局上下文 ====================

@dataclass
class GhCtx:
    """GitHub CLI 全局上下文，所有子命令组共享"""
    repo: Optional[str] = None
    hostname: Optional[str] = None
    auth_token: Optional[str] = None
    debug: bool = False
    no_prompt: bool = False


# ==================== 2. 子命令组（纯 Class，可独立测试）====================

class IssueCmd(NbCmd):
    """Issue 管理"""
    nbctx: GhCtx

    def list(self, state: Annotated[str, 'Issue 状态过滤 (open/closed/all)'] = 'open',
             label: Annotated[str, '按标签过滤'] = None,
             limit: Annotated[int, '最大返回数量'] = 30):
        """列出 Issues"""
        print(f"[issue list] repo={self.nbctx.repo}, state={state}, label={label}, limit={limit}")
        if self.nbctx.debug:
            print(f"  DEBUG: hostname={self.nbctx.hostname}, no_prompt={self.nbctx.no_prompt}")

    def create(self, title: Annotated[str, 'Issue 标题', 't'],
               body: Annotated[str, 'Issue 正文', 'b'] = '',
               assignee: Annotated[str, '指定负责人', 'a'] = None):
        """创建新 Issue"""
        print(f"[issue create] repo={self.nbctx.repo}, title={title}")
        if body:
            print(f"  body={body}")
        if assignee:
            print(f"  assignee={assignee}")

    def view(self, number: Annotated[int, 'Issue 编号']):
        """查看 Issue 详情"""
        print(f"[issue view] repo={self.nbctx.repo}, #{number}")


class PrCmd(NbCmd):
    """Pull Request 管理"""
    nbctx: GhCtx

    def list(self, state: Annotated[str, 'PR 状态过滤 (open/closed/merged/all)'] = 'open',
             author: Annotated[str, '按作者过滤'] = None):
        """列出 Pull Requests"""
        print(f"[pr list] repo={self.nbctx.repo}, state={state}, author={author}")

    def create(self, title: Annotated[str, 'PR 标题', 't'],
               body: Annotated[str, 'PR 描述', 'b'] = '',
               base: Annotated[str, '目标分支'] = 'main',
               draft: Annotated[bool, '创建为 Draft PR'] = False):
        """创建新 Pull Request"""
        kind = 'Draft PR' if draft else 'PR'
        print(f"[pr create] repo={self.nbctx.repo}, {kind}: {title} → {base}")
        if self.nbctx.debug:
            tok = '***' if self.nbctx.auth_token else 'default'
            print(f"  DEBUG: auth={tok}")

    def merge(self, number: Annotated[int, 'PR 编号', 'n'],
              squash: Annotated[bool, 'Squash 合并'] = False,
              delete_branch: Annotated[bool, '合并后删除分支'] = False):
        """合并 Pull Request"""
        method = 'squash' if squash else 'merge'
        tok = '***' if self.nbctx.auth_token else 'default'
        print(f"[pr merge] repo={self.nbctx.repo}, #{number}, method={method}, auth={tok}")
        if delete_branch:
            print("  → 合并后将删除源分支")


class RepoCmd(NbCmd):
    """仓库管理"""
    nbctx: GhCtx

    def clone(self, target_repo: Annotated[str, '要克隆的仓库'],
              depth: Annotated[int, '浅克隆深度 (0=完整)'] = 0):
        """克隆仓库"""
        depth_info = f' (depth={depth})' if depth else ''
        print(f"[repo clone] {target_repo}{depth_info}")
        if self.nbctx.hostname:
            print(f"  → 从 {self.nbctx.hostname} 克隆")

    def fork(self, org: Annotated[str, 'Fork 到指定组织'] = None):
        """Fork 仓库"""
        target = f" → {org}" if org else ''
        print(f"[repo fork] {self.nbctx.repo}{target}")


# ==================== 3. 顶层入口 ====================

class GhCli(NbCmd):
    """
    gh-cli: GitHub 命令行工具 (nb_cmd 版)

    全局参数 repo/hostname/auth_token/debug/no_prompt 自动穿透到所有子命令组。
    """
    nbctx: GhCtx

    class Meta(NbCmdMeta):
        name = 'gh-cli'
        version = '1.0.0'
        enable_exec = False
        # 白名单示例：仅暴露 status + issue/list + pr/merge（Python 直接调用不受影响）
        # allow_method_list = ['status', 'issue.list', 'pr/merge']
        # 黑名单示例：隐藏 status（与白名单互斥，白名单优先）
        # hide_method_list = ['status']
        # 鉴权示例：API/Web 请求须带 Authorization: Bearer <token>
        auth_token = 'my-secret-token'
        # 超时示例：命令执行超过 60 秒自动终止
        # timeout = 60

    def __init__(
        self,
        repo: Annotated[str, '目标仓库 (owner/repo)', 'R'] = None,
        hostname: Annotated[str, 'GitHub Enterprise 域名'] = None,
        auth_token: Annotated[str, '访问令牌 (覆盖配置)'] = None,
        debug: Annotated[bool, '开启调试模式'] = False,
        no_prompt: Annotated[bool, '禁用交互提示'] = False,
    ):
        self.repo = repo
        self.hostname = hostname
        self.auth_token = auth_token
        self.debug = debug
        self.no_prompt = no_prompt
        # 直接赋值 nbctx，CLI/Web/TUI/API 所有模式均能拿到正确的参数值
        self.nbctx = GhCtx(
            repo=self.repo,
            hostname=self.hostname,
            auth_token=self.auth_token,
            debug=self.debug,
            no_prompt=self.no_prompt,
        )
        # 也可以用 make_nbctx() 模板方法替代上面的直接赋值（两种方式均可）：
        # def make_nbctx(self):
        #     return GhCtx(repo=self.repo, ...)

    sub_commands = {
        'issue': IssueCmd,
        'pr': PrCmd,
        'repo': RepoCmd,
    }

    def status(self):
        """查看 CLI 全局配置状态"""
        print("=== gh-cli 全局配置 ===")
        print(f"repo:       {self.nbctx.repo}")
        print(f"hostname:   {self.nbctx.hostname}")
        print(f"auth_token: {'***' if self.nbctx.auth_token else 'None'}")
        print(f"debug:      {self.nbctx.debug}")
        print(f"no_prompt:  {self.nbctx.no_prompt}")


if __name__ == '__main__':
    import sys as _sys

    if len(_sys.argv) > 1:
        GhCli().run()
    else:
        print('=' * 60)
        print('GitHub CLI (nb_cmd 版) — 本地直接调用 + CmdGen 文档演示')
        print('=' * 60)

        # 场景 1: 本地直接调用（子命令独立测试）
        print('\n--- 场景 1: 子命令独立测试（无需启动整个 CLI）---')
        ctx = GhCtx(repo='myorg/api', debug=True)
        issue = IssueCmd()
        issue.nbctx = ctx
        issue.list(state='all', limit=10)
        issue.create(title='Bug: login failed')

        # 场景 2: 多个子命令组共享同一个 ctx
        print('\n--- 场景 2: 多子命令组共享 ctx ---')
        ctx = GhCtx(repo='prod/web', auth_token='ghp_xxx')
        pr = PrCmd()
        repo = RepoCmd()
        pr.nbctx = ctx
        repo.nbctx = ctx
        pr.merge(number=42, squash=True)
        repo.fork(org='my-team')

        # 场景 3: CmdGen 自动生成命令行示例
        print('\n--- 场景 3: CmdGen 命令行示例 ---')
        g = CmdGen(GhCli, script='gh_nb_cmd.py')
        print(g.cmd(IssueCmd.list))
        print(g.cmd(IssueCmd.create))
        print(g.cmd(PrCmd.merge))
        print(g.cmd(RepoCmd.clone))
        print(g.cmd(GhCli.status))

        # 场景 4: CmdGen.doc() 生成完整 Markdown 文档
        print('\n--- 场景 4: CmdGen.doc() 生成 Markdown ---')
        g_md = CmdGen(GhCli, script='gh_nb_cmd.py', fmt='markdown')
        doc_path = os.path.join(os.path.dirname(__file__), 'gh_nb_cmd_gen_doc.md')
        g_md.doc(file=doc_path)
        print(f'Markdown 文档已生成: {doc_path}')

`````

--- **end of file: examples/github_cli_demos/gh_nb_cmd.py** (project: nb_cmd) --- 

---


--- **start of file: examples/github_cli_demos/gh_nb_cmd_gen_doc.md** (project: nb_cmd) --- 

`````markdown
> *Auto-generated by nb-cmd CmdGen*

# gh-cli v1.0.0

> gh-cli: GitHub 命令行工具 (nb_cmd 版)

全局参数 repo/hostname/auth_token/debug/no_prompt 自动穿透到所有子命令组。

## Table of Contents

- [`status`](#status)
- [`issue`  *(子命令组)*](#issue-子命令组)
  - [`issue create`](#issue-create)
  - [`issue list`](#issue-list)
  - [`issue view`](#issue-view)
- [`pr`  *(子命令组)*](#pr-子命令组)
  - [`pr create`](#pr-create)
  - [`pr list`](#pr-list)
  - [`pr merge`](#pr-merge)
- [`repo`  *(子命令组)*](#repo-子命令组)
  - [`repo clone`](#repo-clone)
  - [`repo fork`](#repo-fork)

---

## System Params

| Flag | Description |
|------|-------------|
| `-h`, `--help` | 显示帮助信息 |
| `-fh`, `--full-help` | 显示完整帮助（所有参数详情） |
| `-eh`, `--easy-help` | 显示简易帮助（argparse 原生格式） |
| `--cmd-version` | 显示版本号 |
| `--web` | 以 Web UI + REST API 模式启动 |
| `--web-port PORT` | Web UI 服务端口（用于 `--web`） |

## Global Params (`__init__`)

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--repo, -R` | `str` | `None` | 目标仓库 (owner/repo) |
| `--hostname` | `str` | `None` | GitHub Enterprise 域名 |
| `--auth-token` | `str` | `None` | 访问令牌 (覆盖配置) |
| `--debug` | `bool` | `False` | 开启调试模式 |
| `--no-prompt` | `bool` | `False` | 禁用交互提示 |

## Quick Start

```bash
# 查看完整帮助
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py -fh

# 查看版本
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --cmd-version

# 启动 Web UI
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --web
```

## 命令行约定

命令格式：`python script.py [全局参数] <子命令路径> [命令参数]`

| 标记 | 含义 |
|------|------|
| `${value}` | 带默认值的参数 — 可按需替换 |
| `$<name>` | **必填**参数 — 必须提供值 |
| `--flag`（无值） | 布尔开关，添加即启用 |

---

## Commands

### `status`

查看 CLI 全局配置状态

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt status
```

### `issue` *(子命令组)*

> Issue 管理

#### `issue create`

创建新 Issue

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--title, -t` | `str` | *(required)* | Issue 标题 |
| `--body, -b` | `str` | `` | Issue 正文 |
| `--assignee, -a` | `str` | `None` | 指定负责人 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt issue create --title $<title> --body ${} --assignee ${None}
```

#### `issue list`

列出 Issues

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--state` | `str` | `open` | Issue 状态过滤 (open/closed/all) |
| `--label` | `str` | `None` | 按标签过滤 |
| `--limit` | `int` | `30` | 最大返回数量 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt issue list --state ${open} --label ${None} --limit ${30}
```

#### `issue view`

查看 Issue 详情

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--number` | `int` | *(required)* | Issue 编号 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt issue view --number $<number>
```

### `pr` *(子命令组)*

> Pull Request 管理

#### `pr create`

创建新 Pull Request

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--title, -t` | `str` | *(required)* | PR 标题 |
| `--body, -b` | `str` | `` | PR 描述 |
| `--base` | `str` | `main` | 目标分支 |
| `--draft` | `bool` | `False` | 创建为 Draft PR |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt pr create --title $<title> --body ${} --base ${main} --draft
```

#### `pr list`

列出 Pull Requests

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--state` | `str` | `open` | PR 状态过滤 (open/closed/merged/all) |
| `--author` | `str` | `None` | 按作者过滤 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt pr list --state ${open} --author ${None}
```

#### `pr merge`

合并 Pull Request

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--number, -n` | `int` | *(required)* | PR 编号 |
| `--squash` | `bool` | `False` | Squash 合并 |
| `--delete-branch` | `bool` | `False` | 合并后删除分支 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt pr merge --number $<number> --squash --delete-branch
```

### `repo` *(子命令组)*

> 仓库管理

#### `repo clone`

克隆仓库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--target-repo` | `str` | *(required)* | 要克隆的仓库 |
| `--depth` | `int` | `0` | 浅克隆深度 (0=完整) |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt repo clone --target-repo $<target_repo> --depth ${0}
```

#### `repo fork`

Fork 仓库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--org` | `str` | `None` | Fork 到指定组织 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe gh_nb_cmd.py --repo ${None} --hostname ${None} --auth-token ${None} --debug --no-prompt repo fork --org ${None}
```

`````

--- **end of file: examples/github_cli_demos/gh_nb_cmd_gen_doc.md** (project: nb_cmd) --- 

---


--- **start of file: examples/github_cli_demos/gh_typer.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
GitHub CLI — Typer 实现。

演示 Typer 在多层级子命令 + 全局参数场景下的典型写法：
  - 必须用模块级全局 state 字典穿透参数（破坏封装、非线程安全）
  - add_typer() 手动管理多个 Typer 实例
  - 子命令与全局状态强耦合，无法独立测试

用法:
    python gh_typer.py --repo myorg/api issue list --state all
    python gh_typer.py --repo prod/web --debug pr merge --number 42 --squash
    python gh_typer.py -R team/cli --no-prompt --auth-token ghp_xxx issue create --title "Deploy failed"
"""
import typer
from typing import Optional

app = typer.Typer(help="gh-cli: GitHub 命令行工具 (Typer 版)")

# ⚠️ 模块级全局字典 — 破坏封装，非线程安全
state = {}


@app.callback()
def main(
    repo: str = typer.Option(..., "--repo", "-R", help="目标仓库 (owner/repo)"),
    hostname: Optional[str] = typer.Option(None, help="GitHub Enterprise 域名"),
    auth_token: Optional[str] = typer.Option(None, help="访问令牌 (覆盖配置)"),
    debug: bool = typer.Option(False, help="开启调试模式"),
    no_prompt: bool = typer.Option(False, help="禁用交互提示"),
):
    """全局参数入口"""
    state.update(
        repo=repo,
        hostname=hostname,
        auth_token=auth_token,
        debug=debug,
        no_prompt=no_prompt,
    )


# ==================== issue 子命令组 ====================

issue_app = typer.Typer(help="Issue 管理")
app.add_typer(issue_app, name="issue")


@issue_app.command("list")
def issue_list(
    state_filter: str = typer.Option("open", "--state", help="Issue 状态过滤 (open/closed/all)"),
    label: Optional[str] = typer.Option(None, help="按标签过滤"),
    limit: int = typer.Option(30, help="最大返回数量"),
):
    """列出 Issues"""
    print(f"[issue list] repo={state['repo']}, state={state_filter}, label={label}, limit={limit}")
    if state['debug']:
        print(f"  DEBUG: hostname={state['hostname']}, no_prompt={state['no_prompt']}")


@issue_app.command("create")
def issue_create(
    title: str = typer.Option(..., "--title", "-t", help="Issue 标题"),
    body: str = typer.Option("", "--body", "-b", help="Issue 正文"),
    assignee: Optional[str] = typer.Option(None, "--assignee", "-a", help="指定负责人"),
):
    """创建新 Issue"""
    print(f"[issue create] repo={state['repo']}, title={title}")
    if body:
        print(f"  body={body}")
    if assignee:
        print(f"  assignee={assignee}")


@issue_app.command("view")
def issue_view(
    number: int = typer.Argument(..., help="Issue 编号"),
):
    """查看 Issue 详情"""
    print(f"[issue view] repo={state['repo']}, #{number}")


# ==================== pr 子命令组 ====================

pr_app = typer.Typer(help="Pull Request 管理")
app.add_typer(pr_app, name="pr")


@pr_app.command("list")
def pr_list(
    state_filter: str = typer.Option("open", "--state", help="PR 状态过滤 (open/closed/merged/all)"),
    author: Optional[str] = typer.Option(None, help="按作者过滤"),
):
    """列出 Pull Requests"""
    print(f"[pr list] repo={state['repo']}, state={state_filter}, author={author}")


@pr_app.command("create")
def pr_create(
    title: str = typer.Option(..., "--title", "-t", help="PR 标题"),
    body: str = typer.Option("", "--body", "-b", help="PR 描述"),
    base: str = typer.Option("main", help="目标分支"),
    draft: bool = typer.Option(False, help="创建为 Draft PR"),
):
    """创建新 Pull Request"""
    kind = 'Draft PR' if draft else 'PR'
    print(f"[pr create] repo={state['repo']}, {kind}: {title} → {base}")
    if state['debug']:
        tok = '***' if state['auth_token'] else 'default'
        print(f"  DEBUG: auth={tok}")


@pr_app.command("merge")
def pr_merge(
    number: int = typer.Option(..., "--number", "-n", help="PR 编号"),
    squash: bool = typer.Option(False, help="Squash 合并"),
    delete_branch: bool = typer.Option(False, help="合并后删除分支"),
):
    """合并 Pull Request"""
    method = 'squash' if squash else 'merge'
    tok = '***' if state['auth_token'] else 'default'
    print(f"[pr merge] repo={state['repo']}, #{number}, method={method}, auth={tok}")
    if delete_branch:
        print("  → 合并后将删除源分支")


# ==================== repo 子命令组 ====================

repo_app = typer.Typer(help="仓库管理")
app.add_typer(repo_app, name="repo")


@repo_app.command("clone")
def repo_clone(
    target_repo: str = typer.Argument(..., help="要克隆的仓库"),
    depth: int = typer.Option(0, help="浅克隆深度 (0=完整)"),
):
    """克隆仓库"""
    depth_info = f' (depth={depth})' if depth else ''
    print(f"[repo clone] {target_repo}{depth_info}")
    if state['hostname']:
        print(f"  → 从 {state['hostname']} 克隆")


@repo_app.command("fork")
def repo_fork(
    org: Optional[str] = typer.Option(None, help="Fork 到指定组织"),
):
    """Fork 仓库"""
    target = f" → {org}" if org else ''
    print(f"[repo fork] {state['repo']}{target}")


if __name__ == "__main__":
    app()

`````

--- **end of file: examples/github_cli_demos/gh_typer.py** (project: nb_cmd) --- 

---


--- **start of file: examples/git_demos/git_click.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
Git 命令行工具 — Click 实现。

演示 Click 在多层级子命令 + 全局参数场景下的典型写法：
  - 全局参数通过 @click.group() + @click.pass_context 传递
  - 子命令组通过 @cli.group() 嵌套
  - 深层子命令 (config → user → name/email) 通过 ctx.obj 访问全局参数
  - 每个子命令都要加 @click.pass_context 才能访问全局参数

用法:
    python git_click.py --verbose status
    python git_click.py -C /etc/git remote add origin https://github.com/user/repo.git
    python git_click.py --verbose branch create feature/login --from-branch develop
    python git_click.py -C ~/my-config config user name "John Doe"
    python git_click.py --verbose config user email
"""
import click


@click.group()
@click.option('--verbose', '-v', is_flag=True, help='详细输出')
@click.option('--path', '-C', default='.', help='工作目录路径')
@click.pass_context
def cli(ctx, verbose, path):
    """Git 命令行工具 (Click 版)"""
    ctx.ensure_object(dict)
    ctx.obj.update(
        verbose=verbose,
        path=path,
    )


# ==================== 一级命令 ====================

@cli.command()
@click.pass_context
def status(ctx):
    """查看仓库状态"""
    c = ctx.obj
    verbose_flag = ' (详细模式)' if c['verbose'] else ''
    print(f'[status] 检查仓库状态{verbose_flag}')
    print(f'  工作目录: {c["path"]}')
    print('  On branch main')
    print('  nothing to commit, working tree clean')


@cli.command()
@click.option('--oneline', is_flag=True, help='单行显示')
@click.option('--graph', is_flag=True, help='图形化显示')
@click.option('--max-count', '-n', default=10, type=int, help='最大显示数量')
@click.pass_context
def log(ctx, oneline, graph, max_count):
    """查看提交历史"""
    c = ctx.obj
    if c['verbose']:
        print(f'[log] 工作目录: {c["path"]}')
    fmt = '--oneline' if oneline else ''
    graph_flag = '--graph' if graph else ''
    print(f'git log {fmt} {graph_flag} -{max_count}')
    print('  commit a1b2c3d4 (HEAD -> main)')
    print('  Author: User <user@example.com>')
    print('  Date:   2026-05-11')
    print('      initial commit')


# ==================== remote 子命令组 (二级) ====================

@cli.group()
@click.pass_context
def remote(ctx):
    """远程仓库管理"""
    pass


@remote.command('add')
@click.argument('name')
@click.argument('url')
@click.pass_context
def remote_add(ctx, name, url):
    """添加远程仓库"""
    c = ctx.obj
    if c['verbose']:
        print(f'[remote add] 工作目录: {c["path"]}')
    print(f'git remote add {name} {url}')


@remote.command('remove')
@click.argument('name')
@click.pass_context
def remote_remove(ctx, name):
    """删除远程仓库"""
    c = ctx.obj
    print(f'git remote remove {name}')
    if c['verbose']:
        print(f'  (工作目录: {c["path"]})')


@remote.command('show')
@click.argument('name', required=False, default=None)
@click.pass_context
def remote_show(ctx, name):
    """显示远程仓库信息"""
    c = ctx.obj
    target = name or 'origin'
    print(f'git remote show {target}')
    if c['verbose']:
        print(f'  工作目录: {c["path"]}')
    print(f'  Fetch URL: https://github.com/user/{target}.git')
    print(f'  Push  URL: https://github.com/user/{target}.git')


# ==================== branch 子命令组 (二级) ====================

@cli.group()
@click.pass_context
def branch(ctx):
    """分支管理"""
    pass


@branch.command('create')
@click.argument('name')
@click.option('--from-branch', default='main', help='基于哪个分支')
@click.pass_context
def branch_create(ctx, name, from_branch):
    """创建分支"""
    c = ctx.obj
    print(f'git checkout -b {name} {from_branch}')
    if c['verbose']:
        print(f'  (工作目录: {c["path"]})')


@branch.command('delete')
@click.argument('name')
@click.option('--force', '-f', is_flag=True, help='强制删除')
@click.pass_context
def branch_delete(ctx, name, force):
    """删除分支"""
    c = ctx.obj
    flag = '-D' if force else '-d'
    print(f'git branch {flag} {name}')
    if c['verbose']:
        print('  (强制模式)')


@branch.command('list')
@click.option('--merged', is_flag=True, help='只显示已合并的分支')
@click.pass_context
def branch_list(ctx, merged):
    """列出分支"""
    c = ctx.obj
    filter_flag = '--merged' if merged else ''
    print(f'git branch {filter_flag}')
    if c['verbose']:
        print(f'  工作目录: {c["path"]}')
    print('  * main')
    print('    develop')
    print('    feature/login')


# ==================== config → user 深层子命令组 (三级) ====================

@cli.group()
@click.pass_context
def config(ctx):
    """配置管理"""
    pass


@config.group()
@click.pass_context
def user(ctx):
    """用户配置"""
    pass


@user.command('name')
@click.argument('value', required=False, default=None)
@click.pass_context
def user_name(ctx, value):
    """获取/设置用户名 — 深层子命令，通过 ctx.obj 访问全局参数"""
    c = ctx.obj
    work_path = c['path']
    if value:
        print(f'git -C {work_path} config user.name "{value}"')
        print(f'  → 用户名已设置为: {value}')
    else:
        print(f'git -C {work_path} config user.name')
        print(f'  → 当前用户名: User')
    if c['verbose']:
        print(f'  (详细模式: 工作目录={work_path})')


@user.command('email')
@click.argument('value', required=False, default=None)
@click.pass_context
def user_email(ctx, value):
    """获取/设置用户邮箱 — 深层子命令，通过 ctx.obj 访问全局参数"""
    c = ctx.obj
    work_path = c['path']
    if value:
        print(f'git -C {work_path} config user.email "{value}"')
        print(f'  → 邮箱已设置为: {value}')
    else:
        print(f'git -C {work_path} config user.email')
        print(f'  → 当前邮箱: user@example.com')
    if c['verbose']:
        print(f'  (详细模式: 工作目录={work_path})')


if __name__ == '__main__':
    cli()
`````

--- **end of file: examples/git_demos/git_click.py** (project: nb_cmd) --- 

---


--- **start of file: examples/git_demos/git_nb_cmd.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
Git 命令行工具 — nb_cmd 实现。

演示 nb_cmd 在多层级子命令 + 全局参数场景下的优势：
  - 零装饰器：所有命令通过纯 Class + 方法定义
  - __init__ 即全局参数：self.nbctx 自动穿透到所有子命令组
  - self.nbctx 强类型 + IDE 补全：子命令组通过类型注解获取代码补全
  - 子命令独立可测：每个 NbCmd 子类可脱离父级单独实例化和测试
  - 深层子命令 (config → user → name/email) 通过 self.nbctx 访问全局参数

用法:
    python git_nb_cmd.py --verbose status
    python git_nb_cmd.py -C /etc/git remote add origin https://github.com/user/repo.git
    python git_nb_cmd.py --verbose branch create feature/login --from-branch develop
    python git_nb_cmd.py -C ~/my-config config user name "John Doe"
    python git_nb_cmd.py --verbose config user email

D:/ProgramData/Miniconda3/envs/py39b/python.exe D:\codes/nb_cmd/examples/git_demos/git_nb_cmd.py --tui


"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from dataclasses import dataclass
from typing import Annotated
from nb_cmd import NbCmd


# ==================== 1. 定义全局上下文 ====================

@dataclass
class GitCtx:
    """Git 全局上下文，所有子命令组共享"""
    verbose: bool = False
    path: str = '.'


# ==================== 2. 子命令组（纯 Class，可独立测试）====================

class RemoteCmd(NbCmd):
    """远程仓库管理 (二级子命令组)"""
    nbctx: GitCtx

    def add(self, name: Annotated[str, '远程仓库名'], url: Annotated[str, '仓库 URL']):
        """添加远程仓库"""
        if self.nbctx.verbose:
            print(f'[remote add] 工作目录: {self.nbctx.path}')
        print(f'git remote add {name} {url}')

    def remove(self, name: Annotated[str, '要删除的远程名']):
        """删除远程仓库"""
        print(f'git remote remove {name}')
        if self.nbctx.verbose:
            print(f'  (工作目录: {self.nbctx.path})')

    def show(self, name: Annotated[str, '远程仓库名'] = None):
        """显示远程仓库信息"""
        target = name or 'origin'
        print(f'git remote show {target}')
        if self.nbctx.verbose:
            print(f'  工作目录: {self.nbctx.path}')
        print(f'  Fetch URL: https://github.com/user/{target}.git')
        print(f'  Push  URL: https://github.com/user/{target}.git')


class BranchCmd(NbCmd):
    """分支管理 (二级子命令组)"""
    nbctx: GitCtx

    def create(self, name: Annotated[str, '分支名'],
               from_branch: Annotated[str, '基于哪个分支'] = 'main'):
        """创建分支"""
        print(f'git checkout -b {name} {from_branch}')
        if self.nbctx.verbose:
            print(f'  (工作目录: {self.nbctx.path})')

    def delete(self, name: Annotated[str, '分支名'],
               force: Annotated[bool, '强制删除', 'f'] = False):
        """删除分支"""
        flag = '-D' if force else '-d'
        print(f'git branch {flag} {name}')
        if self.nbctx.verbose:
            print('  (强制模式)')

    def list(self, merged: Annotated[bool, '只显示已合并的分支'] = False):
        """列出分支"""
        filter_flag = '--merged' if merged else ''
        print(f'git branch {filter_flag}')
        if self.nbctx.verbose:
            print(f'  工作目录: {self.nbctx.path}')
        print('  * main')
        print('    develop')
        print('    feature/login')


class UserConfigCmd(NbCmd):
    """用户配置 (三级深层子命令组，通过 self.nbctx 访问全局参数)"""
    nbctx: GitCtx

    def name(self, value: Annotated[str, '用户名 (不传则查询)'] = None):
        """获取/设置用户名 — 深层子命令，（通过 self.nbctx 访问全局参数）"""
        work_path = self.nbctx.path
        if value:
            print(f'git -C {work_path} config user.name "{value}"')
            print(f'  → 用户名已设置为: {value}')
        else:
            print(f'git -C {work_path} config user.name')
            print(f'  → 当前用户名: User')
        if self.nbctx.verbose:
            print(f'  (详细模式: 工作目录={work_path})')

    def email(self, value: Annotated[str, '用户邮箱 (不传则查询)'] = None):
        """获取/设置用户邮箱 — 深层子命令，（通过 self.nbctx 访问全局参数，传入 value 则设置，不传入则查询）"""
        work_path = self.nbctx.path
        if value:
            print(f'git -C {work_path} config user.email "{value}"')
            print(f'  → 邮箱已设置为: {value}')
        else:
            print(f'git -C {work_path} config user.email')
            print(f'  → 当前邮箱: user@example.com')
        if self.nbctx.verbose:
            print(f'  (详细模式: 工作目录={work_path})')


class ConfigCmd(NbCmd):
    """配置管理 (二级子命令组，挂载三级子命令)"""
    nbctx: GitCtx

    sub_commands = {
        'user': UserConfigCmd,
    }


# ==================== 3. 顶层入口 ====================

class GitTool(NbCmd):
    """
    Git 命令行工具 (nb_cmd 版)

    全局参数 verbose/config_dir 自动穿透到所有子命令组。
    演示多层级子命令: remote, branch (二级), config → user (三级)
    """
    nbctx: GitCtx

    def __init__(
        self,
        verbose: Annotated[bool, '详细输出', 'v'] = False,
        path: Annotated[str, '工作目录路径', 'C'] = '.',
    ):
        self.verbose = verbose
        self.path = path
        self.nbctx = GitCtx(
            verbose=self.verbose,
            path=self.path,
        )

    sub_commands = {
        'remote': RemoteCmd,
        'branch': BranchCmd,
        'config': ConfigCmd,
    }

    def status(self):
        """查看仓库状态"""
        verbose_flag = ' (详细模式)' if self.nbctx.verbose else ''
        print(f'[status] 检查仓库状态{verbose_flag}')
        print(f'  工作目录: {self.nbctx.path}')
        print('  On branch main')
        print('  nothing to commit, working tree clean')

    def log(self,
            oneline: Annotated[bool, '单行显示'] = False,
            graph: Annotated[bool, '图形化显示'] = False,
            max_count: Annotated[int, '最大显示数量', 'n'] = 10):
        """查看提交历史"""
        if self.nbctx.verbose:
            print(f'[log] 工作目录: {self.nbctx.path}')
        fmt = '--oneline' if oneline else ''
        graph_flag = '--graph' if graph else ''
        print(f'git log {fmt} {graph_flag} -{max_count}')
        print('  commit a1b2c3d4 (HEAD -> main)')
        print('  Author: User <user@example.com>')
        print('  Date:   2026-05-11')
        print('      initial commit')


if __name__ == '__main__':
    GitTool().run()
`````

--- **end of file: examples/git_demos/git_nb_cmd.py** (project: nb_cmd) --- 

---


--- **start of file: examples/git_demos/README.md** (project: nb_cmd) --- 

`````markdown
# Git 命令行工具 — Click vs nb_cmd 实现对比

## 概述

本目录用 **Click** 和 **nb_cmd** 两种框架分别实现了 Git 部分命令，重点演示三个核心特性：

| 特性 | 说明 |
|------|------|
| **全局传参** | `--verbose` / `-v` 和 `--path` / `-C` 两个全局参数穿透到所有子命令 |
| **多层级子命令** | `remote`、`branch`（二级），`config → user`（三级） |
| **深层子命令使用全局参数** | `config user name/email` 读取全局 `--path` 和 `--verbose` |

---

## 文件说明

| 文件 | 框架 | 装饰器数 |
|------|------|---------|
| `git_click.py` | Click | 18 个 |
| `git_nb_cmd.py` | nb_cmd | **0 个** |

---

## 命令结构

```
git-tool
├── --verbose / -v          # 全局参数：详细输出
├── --path / -C             # 全局参数：工作目录路径
│
├── status                  # 一级命令
├── log [--oneline] [--graph] [-n]   # 一级命令
│
├── remote                  # 二级子命令组
│   ├── add <name> <url>
│   ├── remove <name>
│   └── show [name]
│
├── branch                  # 二级子命令组
│   ├── create <name> [--from-branch]
│   ├── delete <name> [--force]
│   └── list [--merged]
│
└── config                  # 二级子命令组
    └── user                # 三级深层子命令组
        ├── name [value]    ← 使用全局 --path 和 --verbose
        └── email [value]   ← 使用全局 --path 和 --verbose
```

---

## 全局传参方式对比

### Click：`@click.pass_context` + `ctx.obj` 字典

```python
@click.group()
@click.option('--verbose', '-v', is_flag=True)
@click.option('--path', '-C', default='.')
@click.pass_context
def cli(ctx, verbose, path):
    ctx.ensure_object(dict)
    ctx.obj.update(verbose=verbose, path=path)

# 每个子命令都要加 @click.pass_context
@remote.command('add')
@click.argument('name')
@click.argument('url')
@click.pass_context
def remote_add(ctx, name, url):
    c = ctx.obj          # 字典取值，无 IDE 补全
    if c['verbose']:     # 字符串 key，拼写错误无提示
        ...
```

**痛点：**
- 每个子命令都要加 `@click.pass_context` 装饰器
- 取值靠 `ctx.obj['key']`（字符串键，无 IDE 补全，拼写错误运行时才暴露）
- 装饰器随层级指数叠加：三级子命令 `config user name` 需要 4 个装饰器

### nb_cmd：`__init__` + `self.nbctx` 强类型属性

```python
@dataclass
class GitCtx:
    verbose: bool = False
    path: str = '.'

class GitTool(NbCmd):
    nbctx: GitCtx

    def __init__(self, verbose: bool = False, path: str = '.'):
        self.nbctx = GitCtx(verbose=verbose, path=path)

    sub_commands = {'remote': RemoteCmd, 'branch': BranchCmd, 'config': ConfigCmd}

# 子命令组中直接通过 self.nbctx 访问
class RemoteCmd(NbCmd):
    nbctx: GitCtx

    def add(self, name: str, url: str):
        if self.nbctx.verbose:    # 强类型属性，IDE 自动补全
            print(self.nbctx.path)
```

**优势：**
- 零装饰器：`__init__` 即全局参数定义
- `self.nbctx.verbose` 强类型访问，IDE 自动补全 + 跳转
- 框架自动 `child.nbctx = parent.nbctx` 递归传递，任意嵌套深度无需额外代码

---

## 多层级子命令定义对比

### Click：装饰器嵌套

```python
# 二级：@cli.group()
@cli.group()
@click.pass_context
def remote(ctx): pass

@remote.command('add')
@click.pass_context
def remote_add(ctx, name, url): ...

# 三级：@cli.group() → @config.group()
@cli.group()
@click.pass_context
def config(ctx): pass

@config.group()
@click.pass_context
def user(ctx): pass

@user.command('name')
@click.pass_context
def user_name(ctx, value): ...
```

**痛点：**
- 每新增一个子命令组需要 `@cli.group()` + 函数定义
- 装饰器用错实例（如 `@remote.command()` 写成 `@branch.command()`），命令跑到错误层级，不报错但行为异常
- 函数散落各处，层级关系靠装饰器维持，代码可读性差

### nb_cmd：`sub_commands` 字典

```python
class GitTool(NbCmd):
    sub_commands = {
        'remote': RemoteCmd,    # 二级
        'branch': BranchCmd,    # 二级
        'config': ConfigCmd,    # 二级 → 三级
    }

class ConfigCmd(NbCmd):
    sub_commands = {
        'user': UserConfigCmd,  # 三级
    }

class UserConfigCmd(NbCmd):
    def name(self, value=None): ...   # 三级子命令
    def email(self, value=None): ...  # 三级子命令
```

**优势：**
- 子命令组是独立 Class，层级关系一目了然
- 新增子命令组只需：写一个 Class + 在父级 `sub_commands` 加一项
- 子命令组可单独实例化、单独测试、单独复用

---

## 深层子命令使用全局参数

### Click 版（`config user name` 使用 `--path`）

```python
@user.command('name')
@click.argument('value', required=False, default=None)
@click.pass_context
def user_name(ctx, value):
    c = ctx.obj
    work_path = c['path']               # 从 ctx.obj 取全局参数
    if c['verbose']:                    # 从 ctx.obj 取全局参数
        print(f'详细模式: 工作目录={work_path}')
    print(f'git -C {work_path} config user.name "{value}"')
```

### nb_cmd 版（`config user name` 使用 `--path`）

```python
class UserConfigCmd(NbCmd):
    nbctx: GitCtx

    def name(self, value: str = None):
        work_path = self.nbctx.path     # 强类型属性访问
        if self.nbctx.verbose:          # 强类型属性访问
            print(f'详细模式: 工作目录={work_path}')
        print(f'git -C {work_path} config user.name "{value}"')
```
**关键差异：** nb_cmd 的 `self.nbctx` 由框架自动从父级传递到子级，`UserConfigCmd` 不需要任何额外代码就能拿到全局参数。Click 需要每层都加 `@click.pass_context` 并手动从 `ctx.obj` 取值。

---

## 运行示例

```bash
# 1. 查看状态（带全局参数）
python git_click.py --verbose status
python git_nb_cmd.py --verbose status

# 2. 添加远程仓库（指定工作目录）
python git_click.py -C /etc/git remote add origin https://github.com/user/repo.git
python git_nb_cmd.py -C /etc/git remote add origin https://github.com/user/repo.git

# 3. 创建分支（详细模式）
python git_click.py --verbose branch create feature/login --from-branch develop
python git_nb_cmd.py --verbose branch create feature/login --from-branch develop

# 4. 深层子命令：设置用户名（使用全局 -C）
python git_click.py -C ~/my-config config user name "John Doe"
python git_nb_cmd.py -C ~/my-config config user name "John Doe"

# 5. 深层子命令：查询邮箱（使用全局 --verbose）
python git_click.py --verbose config user email
python git_nb_cmd.py --verbose config user email

# 6. 查看帮助
python git_click.py --help
python git_nb_cmd.py --help

python git_click.py remote --help
python git_nb_cmd.py remote --help

python git_click.py config user --help
python git_nb_cmd.py config user --help
```

---

## 总结

| 维度 | Click | nb_cmd |
|------|-------|--------|
| **全局参数定义** | `@click.group()` + `@click.option()` | `__init__` 方法参数 |
| **全局参数传递** | `@click.pass_context` + `ctx.obj['key']` | `self.nbctx.attr` 自动穿透 |
| **子命令组定义** | `@cli.group()` 装饰器嵌套 | `sub_commands = {...}` 字典 |
| **深层子命令** | 每层都要 `@group()` + `@pass_context` | 框架自动递归传递 `nbctx` |
| **IDE 补全** | ❌ `ctx.obj['key']` 无补全 | ✅ `self.nbctx.attr` 强类型补全 |
| **独立测试** | ❌ 函数绑定到 `cli` 实例 | ✅ Class 可单独实例化测试 |
| **装饰器数量** | 18 个 | **0 个** |
| **代码可读性** | 装饰器散落，层级关系隐式 | Class 嵌套，层级关系显式 |

**结论：** 对于多层级子命令 + 全局参数的 CLI 工具，nb_cmd 的 OOP 设计（`__init__` 定义全局参数、`sub_commands` 声明层级、`self.nbctx` 自动穿透）比 Click 的函数式 + 装饰器方案更简洁、更可维护、更易测试。
`````

--- **end of file: examples/git_demos/README.md** (project: nb_cmd) --- 

---


--- **start of file: examples/nbctx_demo/nbctx_demo.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd nbctx 跨层级上下文传递 demo。

演示：顶层全局参数（region/env/debug）如何自动穿透到任意深度的子命令组。

六种能力：
    1. Python 直接调用: 见本文件底部 if __name__ == '__main__' 部分
    2. CLI:  python nbctx_demo.py --region shanghai db migrate
    3. REST API:  curl -X POST http://localhost:8085/db/migrate -d '{"init_params":{"region":"shanghai"}}'
    4. Web UI:  python nbctx_demo.py --web --web-port 8085
    5. TUI:  python nbctx_demo.py --tui
    6. 文档生成: 见本文件底部 CmdGen 示例
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from dataclasses import dataclass
from typing import Annotated
from nb_cmd import NbCmd


# ==================== 1. 定义全局上下文 ====================

@dataclass
class AppCtx:
    """应用级上下文，所有子命令组共享"""
    region: str = 'beijing'
    env: str = 'prod'
    debug: bool = False


# ==================== 2. 子命令组（多层嵌套）====================

class OpsTool(NbCmd):
    """运维操作（第三级子命令组）"""
    nbctx: AppCtx

    def deploy(self, version: Annotated[str, '目标版本号', '-v'], rollback: Annotated[bool, '是否回滚'] = False):
        """部署指定版本"""
        action = '回滚' if rollback else '部署'
        print(f'[{self.nbctx.region}/{self.nbctx.env}] {action} v{version}')
        if self.nbctx.debug:
            print(f'  DEBUG: deploy(version={version}, rollback={rollback})')

    def restart(self):
        """重启服务"""
        print(f'[{self.nbctx.region}/{self.nbctx.env}] 重启服务')


class DbTool(NbCmd):
    """数据库工具（第二级子命令组）"""
    nbctx: AppCtx

    def migrate(self, dry_run: Annotated[bool, '仅模拟，不执行'] = False):
        """执行数据库迁移"""
        mode = 'DRY-RUN' if dry_run else 'EXECUTE'
        print(f'[{self.nbctx.region}/{self.nbctx.env}] 数据库迁移 ({mode})')
        if self.nbctx.debug:
            print(f'  DEBUG: migrate(dry_run={dry_run})')

    def backup(self, compress: Annotated[bool, '启用压缩'] = True):
        """备份数据库"""
        fmt = 'tar.gz' if compress else 'sql'
        print(f'[{self.nbctx.region}/{self.nbctx.env}] 备份数据库 → backup.{fmt}')

    def status(self):
        """查看数据库连接状态"""
        print(f'[{self.nbctx.region}] 数据库连接正常 (env={self.nbctx.env})')


class ServerTool(NbCmd):
    """服务器管理（第二级子命令组，包含第三级 ops）"""
    nbctx: AppCtx

    sub_commands = {
        'ops': OpsTool,
    }

    def info(self):
        """查看服务器信息"""
        print(f'[{self.nbctx.region}] 服务器: {self.nbctx.env} 环境')
        print(f'  Region: {self.nbctx.region}')
        print(f'  Env:    {self.nbctx.env}')
        print(f'  Debug:  {self.nbctx.debug}')

    def ssh(self, user: Annotated[str, '登录用户名'] = 'root'):
        """SSH 登录"""
        host = f'{self.nbctx.region}-{self.nbctx.env}.example.com'
        print(f'ssh {user}@{host}')


# ==================== 3. 顶层命令 ====================

class MyApp(NbCmd):
    """
    云平台管理工具 —— nbctx 跨层级上下文传递 demo。

    全局参数 region/env/debug 会自动传递给所有子命令组。
    """
    nbctx: AppCtx  # 类型注解，让 IDE 补全 self.nbctx.region 等

    class Meta:
        name = 'cloud-tool'
        version = '1.0.0'
        enable_exec = False

    def __init__(self,
                 region: Annotated[str, '部署区域，如 beijing/shanghai/tokyo'] = 'beijing',
                 env: Annotated[str, '运行环境，如 prod/staging/test'] = 'prod',
                 debug: Annotated[bool, '开启调试模式'] = False):
        self.region = region
        self.env = env
        self.debug = debug

    def make_nbctx(self):
        """构造上下文，框架自动传给所有子命令组"""
        return AppCtx(region=self.region, env=self.env, debug=self.debug)

    sub_commands = {
        'db': DbTool,
        'server': ServerTool,
    }

    def status(self):
        """查看全局状态"""
        print(f'=== 云平台状态 ===')
        print(f'Region: {self.nbctx.region}')
        print(f'Env:    {self.nbctx.env}')
        print(f'Debug:  {self.nbctx.debug}')

    def whoami(self):
        """显示当前用户信息"""
        return {'user': 'admin', 'region': self.nbctx.region, 'env': self.nbctx.env}


if __name__ == '__main__':
    import sys as _sys

    if len(_sys.argv) > 1:
        # CLI / Web / API 模式
        MyApp().run()
    else:
        # 本地直接调用演示
        print('='*50)
        print('本地直接调用演示（不走 CLI/Web/API）')
        print('='*50)

        # 场景 1: 顶层命令使用 nbctx
        print('\n--- 场景 1: 顶层命令 ---')
        app = MyApp(region='shanghai', env='staging', debug=True)
        app.nbctx = app.make_nbctx()
        app.status()

        # 场景 2: 子命令组手动注入 nbctx
        print('\n--- 场景 2: 子命令组手动注入 nbctx ---')
        ctx = AppCtx(region='tokyo', env='test', debug=True)
        db = DbTool()
        db.nbctx = ctx
        db.migrate(dry_run=True)
        db.backup()

        # 场景 3: 用默认 ctx
        print('\n--- 场景 3: 用默认 ctx ---')
        db2 = DbTool()
        db2.nbctx = AppCtx()  # 使用 dataclass 默认值
        db2.migrate()

        # 场景 4: 多个子命令组共享同一个 ctx
        print('\n--- 场景 4: 多子命令组共享 ctx ---')
        ctx = AppCtx(region='us-east', env='canary')
        db = DbTool()
        server = ServerTool()
        ops = OpsTool()
        db.nbctx = ctx
        server.nbctx = ctx
        ops.nbctx = ctx
        db.status()
        server.info()
        ops.deploy('2.0.0')

        # 场景 5: CmdGen 自动生成命令行示例
        print('\n--- 场景 5: CmdGen 自动生成命令行示例 ---')
        from nb_cmd import CmdGen

        g = CmdGen(MyApp, script='nbctx_demo.py')
        print(g.cmd(DbTool.migrate))
        print(g.cmd(OpsTool.deploy))
        print(g.cmd(MyApp.status))
        print(g.cmd(ServerTool.ssh))
        print()
        g_md = CmdGen(MyApp, script='d:/codes/nb_cmd/examples/nbctx_demo/nbctx_demo.py', fmt='markdown')
        print(g_md.cmd(DbTool.migrate))

        # 场景 6: CmdGen.doc() 生成完整文档
        print('\n--- 场景 6: CmdGen.doc() 生成完整文档 ---')
        print(g.doc())
        print()
        print('--- Markdown 格式 ---')
        print(g_md.doc(file='d:/codes/nb_cmd/examples/nbctx_demo/nbctx_demo_gen_doc.md'))

`````

--- **end of file: examples/nbctx_demo/nbctx_demo.py** (project: nb_cmd) --- 

---


--- **start of file: examples/nbctx_demo/nbctx_demo_gen_doc.md** (project: nb_cmd) --- 

`````markdown
> *Auto-generated by nb-cmd CmdGen*

# cloud-tool v1.0.0

> 云平台管理工具 —— nbctx 跨层级上下文传递 demo。

全局参数 region/env/debug 会自动传递给所有子命令组。

## Table of Contents

- [`status`](#status)
- [`whoami`](#whoami)
- [`db`  *(子命令组)*](#db-子命令组)
  - [`db backup`](#db-backup)
  - [`db migrate`](#db-migrate)
  - [`db status`](#db-status)
- [`server`  *(子命令组)*](#server-子命令组)
  - [`server info`](#server-info)
  - [`server ssh`](#server-ssh)
  - [`server ops`  *(子命令组)*](#server-ops-子命令组)
    - [`server ops deploy`](#server-ops-deploy)
    - [`server ops restart`](#server-ops-restart)

---

## System Params

| Flag | Description |
|------|-------------|
| `-h`, `--help` | 显示帮助信息 |
| `-fh`, `--full-help` | 显示完整帮助（所有参数详情） |
| `-eh`, `--easy-help` | 显示简易帮助（argparse 原生格式） |
| `--cmd-version` | 显示版本号 |
| `--web` | 以 Web UI + REST API 模式启动 |
| `--web-port PORT` | Web UI 服务端口（用于 `--web`） |

## Global Params (`__init__`)

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--region` | `str` | `beijing` | 部署区域，如 beijing/shanghai/tokyo |
| `--env` | `str` | `prod` | 运行环境，如 prod/staging/test |
| `--debug` | `bool` | `False` | 开启调试模式 |

## Quick Start

```bash
# 查看完整帮助
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py -fh

# 查看版本
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --cmd-version

# 启动 Web UI
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --web
```

## 命令行约定

命令格式：`python script.py [全局参数] <子命令路径> [命令参数]`

| 标记 | 含义 |
|------|------|
| `${value}` | 带默认值的参数 — 可按需替换 |
| `$<name>` | **必填**参数 — 必须提供值 |
| `--flag`（无值） | 布尔开关，添加即启用 |

---

## Commands

### `status`

查看全局状态

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug status
```

### `whoami`

显示当前用户信息

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug whoami
```

### `db` *(子命令组)*

> 数据库工具（第二级子命令组）

#### `db backup`

备份数据库

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--compress` | `bool` | `True` | 启用压缩 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug db backup
```

#### `db migrate`

执行数据库迁移

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--dry-run` | `bool` | `False` | 仅模拟，不执行 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug db migrate --dry-run
```

#### `db status`

查看数据库连接状态

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug db status
```

### `server` *(子命令组)*

> 服务器管理（第二级子命令组，包含第三级 ops）

#### `server info`

查看服务器信息

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug server info
```

#### `server ssh`

SSH 登录

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--user` | `str` | `root` | 登录用户名 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug server ssh --user ${root}
```

#### `server ops` *(子命令组)*

> 运维操作（第三级子命令组）

##### `server ops deploy`

部署指定版本

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `--version, -v` | `str` | *(required)* | 目标版本号 |
| `--rollback` | `bool` | `False` | 是否回滚 |

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug server ops deploy --version $<version> --rollback
```

##### `server ops restart`

重启服务

```bash
D:\ProgramData\miniconda3\envs\py39b\python.exe nbctx_demo.py --region ${beijing} --env ${prod} --debug server ops restart
```

`````

--- **end of file: examples/nbctx_demo/nbctx_demo_gen_doc.md** (project: nb_cmd) --- 

---

# markdown content namespace: nb_cmd codes 


## nb_cmd File Tree (relative dir: `nb_cmd`)


`````

└── nb_cmd
    ├── __init__.py
    ├── cli.py
    ├── core
    │   ├── __init__.py
    │   ├── _io_dispatch.py
    │   ├── arg.py
    │   ├── base.py
    │   ├── discovery.py
    │   ├── gen_cmd.py
    │   ├── gen_skill.py
    │   ├── meta.py
    │   ├── parser.py
    │   ├── result_handler.py
    │   └── type_utils.py
    ├── modes
    │   ├── __init__.py
    │   ├── api_mode.py
    │   ├── cli_mode.py
    │   ├── tui_mode.py
    │   └── web_mode.py
    ├── ui
    │   ├── __init__.py
    │   ├── colors.py
    │   ├── helper.py
    │   ├── progress.py
    │   └── table.py
    └── utils
        ├── __init__.py
        ├── config.py
        └── validators.py

`````

---


## nb_cmd (relative dir: `nb_cmd`)  Included Files (total: 26 files)


- `nb_cmd/cli.py`

- `nb_cmd/__init__.py`

- `nb_cmd/core/arg.py`

- `nb_cmd/core/base.py`

- `nb_cmd/core/discovery.py`

- `nb_cmd/core/gen_cmd.py`

- `nb_cmd/core/gen_skill.py`

- `nb_cmd/core/meta.py`

- `nb_cmd/core/parser.py`

- `nb_cmd/core/result_handler.py`

- `nb_cmd/core/type_utils.py`

- `nb_cmd/core/_io_dispatch.py`

- `nb_cmd/core/__init__.py`

- `nb_cmd/modes/api_mode.py`

- `nb_cmd/modes/cli_mode.py`

- `nb_cmd/modes/tui_mode.py`

- `nb_cmd/modes/web_mode.py`

- `nb_cmd/modes/__init__.py`

- `nb_cmd/ui/colors.py`

- `nb_cmd/ui/helper.py`

- `nb_cmd/ui/progress.py`

- `nb_cmd/ui/table.py`

- `nb_cmd/ui/__init__.py`

- `nb_cmd/utils/config.py`

- `nb_cmd/utils/validators.py`

- `nb_cmd/utils/__init__.py`


---


--- **start of file: nb_cmd/cli.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nbcmd —— 个人命令中心。

零代码启动，通过 exec 收藏和管理所有常用系统命令。

用法:
    nbcmd --tui          # TUI 终端交互模式
    nbcmd --web          # Web 浏览器模式
    nbcmd exec <命令>    # 直接执行系统命令
    nbcmd -h             # 查看帮助
"""
import os

from nb_cmd.core.base import NbCmd
from nb_cmd.core.meta import NbCmdMeta


class _NbCmdApp(NbCmd):
    """个人命令中心 —— 收藏和管理常用系统命令"""

    class Meta(NbCmdMeta):
        name = 'nbcmd'
        version = '0.2.1'
        description = '个人命令中心 —— 通过 exec 收藏和管理所有常用系统命令'
        web_title = 'NbCmd 命令中心'
        db_dir = os.path.join(os.path.expanduser('~'), '.nb_cmd')


def main():
    app = _NbCmdApp()
    app.run()


if __name__ == '__main__':
    main()

`````

--- **end of file: nb_cmd/cli.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/__init__.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
nb_cmd — Python 码农的低代码平台
写一个 class，自动获得六种能力：Python 直接调用 + CLI + REST API + Web UI + TUI 终端交互 + Markdown 文档。

用法::

    from nb_cmd import NbCmd

    class MyTool(NbCmd):
        def greet(self, name: str, times: int = 1):
            for _ in range(times):
                print('你好, {}!'.format(name))

    if __name__ == '__main__':
        MyTool().run()
"""

__version__ = '0.1.0'

from .core.base import NbCmd  # noqa: F401
from .core.meta import NbCmdMeta  # noqa: F401
from .core.arg import Annotated, Param  # noqa: F401
from .ui.helper import UIHelper, cmdui  # noqa: F401
from .utils.validators import validate  # noqa: F401
from .core.gen_cmd import CmdGen  # noqa: F401
from .core.gen_skill import SkillGen  # noqa: F401

`````

--- **end of file: nb_cmd/__init__.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/arg.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
参数描述器 —— 通过 Annotated 为方法参数附加描述和别名。

用法::

    from typing import Annotated  # Python 3.9+
    from nb_cmd import NbCmd, Param

    class MyTool(NbCmd):
        # 方式一：位置参数（简洁）
        def greet(self, name: Annotated[str, '要问候的人名', 'n'],
                  times: Annotated[int, '问候次数'] = 1):
            ...

        # 方式二：Param 对象（关键字参数，清晰）
        def deploy(self, host: Annotated[str, Param(desc='服务器地址', alias='H')],
                   port: Annotated[int, Param(desc='端口号', alias='p')] = 22):
            ...

Annotated 规则:
    Annotated[类型]                              → 纯类型，无描述无别名
    Annotated[类型, '描述']                      → 有描述，无别名
    Annotated[类型, '描述', '别名']              → 有描述 + 别名
    Annotated[类型, Param(desc=..., alias=...)]  → 关键字风格
"""
import sys

if sys.version_info >= (3, 9):
    from typing import Annotated, get_args, get_origin
else:
    try:
        from typing_extensions import Annotated, get_args, get_origin
    except ImportError:
        Annotated = None

        def get_args(tp):
            return getattr(tp, '__args__', ())

        def get_origin(tp):
            return getattr(tp, '__origin__', None)


class Param(object):
    """
    参数元数据描述器，用于 Annotated 内部。

    Parameters
    ----------
    desc : str, optional
        参数描述，显示在 CLI --help 和 Web UI 输入框中
    alias : str or list, optional
        CLI 短参数别名，如 'n' 自动转为 '-n'，'host-name' 转为 '--host-name'
    """

    def __init__(self, desc=None, alias=None):
        self.desc = desc
        if alias is None:
            self.aliases = []
        elif isinstance(alias, (list, tuple)):
            self.aliases = [_normalize_alias(a) for a in alias]
        else:
            self.aliases = [_normalize_alias(alias)]

    def __repr__(self):
        parts = []
        if self.desc:
            parts.append('desc={!r}'.format(self.desc))
        if self.aliases:
            parts.append('alias={!r}'.format(self.aliases))
        return 'Param({})'.format(', '.join(parts))


class _ArgMeta(object):
    """内部元数据容器，保存从 Annotated 中提取的描述和别名"""

    def __init__(self, desc=None, aliases=None):
        self.desc = desc
        self.aliases = aliases or []

    def __repr__(self):
        parts = []
        if self.desc:
            parts.append('desc={!r}'.format(self.desc))
        if self.aliases:
            parts.append('alias={!r}'.format(self.aliases))
        return '_ArgMeta({})'.format(', '.join(parts))


def _normalize_alias(alias):
    """将用户给的 alias 标准化为 CLI flag 格式"""
    s = str(alias)
    if s.startswith('-'):
        return s
    if len(s) == 1:
        return '-' + s
    return '--' + s


def unwrap_arg(hint):
    """
    解析类型注解，提取真实类型和元数据。

    支持:
    - Annotated[str, '描述']                     → (str, _ArgMeta(desc='描述'))
    - Annotated[str, '描述', 'n']                → (str, _ArgMeta(desc='描述', aliases=['-n']))
    - Annotated[str, Param(desc='描述', alias='n')]  → 同上
    - Optional[Annotated[str, '描述']]           → (str, _ArgMeta(desc='描述'))
    - str                                        → (str, None)
    """
    if Annotated is not None and get_origin(hint) is Annotated:
        args = get_args(hint)
        real_type = args[0]

        for meta in args[1:]:
            if isinstance(meta, Param):
                return real_type, _ArgMeta(desc=meta.desc, aliases=list(meta.aliases))

        desc = None
        alias_val = None
        if len(args) > 1 and isinstance(args[1], str):
            desc = args[1]
        if len(args) > 2 and isinstance(args[2], str):
            alias_val = args[2]

        if desc is not None or alias_val is not None:
            aliases = [_normalize_alias(alias_val)] if alias_val else []
            return real_type, _ArgMeta(desc=desc, aliases=aliases)
        return real_type, None

    # Optional[Annotated[...]] — get_type_hints 对 default=None 的参数自动包装 Optional
    if _is_optional(hint):
        inner = _unwrap_optional(hint)
        if inner is not hint and Annotated is not None and get_origin(inner) is Annotated:
            return unwrap_arg(inner)

    return hint, None


def _is_optional(tp):
    """判断 tp 是否为 Optional[X]（即 Union[X, None]），兼容 Python 3.7+"""
    import typing
    origin = getattr(tp, '__origin__', None)
    if origin is getattr(typing, 'Union', None):
        args = getattr(tp, '__args__', ())
        return type(None) in args
    return False


def _unwrap_optional(tp):
    """Optional[X] → X，兼容 Python 3.7+"""
    args = getattr(tp, '__args__', ())
    non_none = [a for a in args if a is not type(None)]
    if len(non_none) == 1:
        return non_none[0]
    return tp

`````

--- **end of file: nb_cmd/core/arg.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/base.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
NbCmd 基类 —— 所有命令行工具的父类。
"""
from __future__ import annotations

import logging
import sys

from .meta import NbCmdMeta

try:
    from typing import Annotated
except ImportError:
    try:
        from typing_extensions import Annotated
    except ImportError:
        pass


class NbCmd(object):
    """
    NbCmd 基类 —— 所有命令行工具的父类。

    用法:
        1. 继承 NbCmd
        2. 定义公有方法（自动成为子命令）
        3. 调用 .run() 启动

    功能:
        - 公有方法 → 子命令
        - 方法签名 → 参数自动推导
        - 六种能力：Python 直接调用 / CLI / REST API / Web UI / TUI 终端交互 / Markdown 文档
        - 支持 OOP 继承覆写
        - 支持多层级子命令（sub_commands）
        - 支持 nbctx 跨层级上下文传递

    工具方法通过 cmdui 模块级单例访问（from nb_cmd import cmdui）:
        cmdui.table()  cmdui.kv()  cmdui.tree()  cmdui.json_print()
        cmdui.success() cmdui.warning() cmdui.error() cmdui.info()
        cmdui.progress() cmdui.confirm() cmdui.prompt() cmdui.select()
    """

    sub_commands = {}

    Meta = NbCmdMeta

    nbctx = None  # 跨层级共享的上下文对象，子类通过 nbctx: AppCtx 注解获取 IDE 补全

    def make_nbctx(self):
        """
        模板方法：创建跨层级共享的上下文对象。

        覆写此方法以返回一个 dataclass 实例，框架会自动将其传递给
        所有子命令组的 self.nbctx。

        用法::

            @dataclass
            class AppCtx:
                region: str = 'beijing'
                env: str = 'prod'

            class MyApp(NbCmd):
                def __init__(self, region='beijing', env='prod'):
                    self.region = region
                    self.env = env

                def make_nbctx(self):
                    return AppCtx(region=self.region, env=self.env)

        Returns
        -------
        object or None
            上下文对象，返回 None 表示不启用 nbctx。
        """
        return None

    def _setup_logging(self):
        """设置日志"""
        meta = self._get_meta()
        use_nb_log = getattr(meta, 'use_nb_log', False)
        log_level = getattr(meta, 'log_level', 'INFO')

        if use_nb_log:
            try:
                import nb_log
                self._logger = nb_log.get_logger(
                    self.__class__.__name__,
                    log_level_int=getattr(logging, log_level, logging.INFO),
                    log_filename=getattr(meta, 'log_file', None),
                )
                return
            except ImportError:
                pass

        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(getattr(logging, log_level, logging.INFO))
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter(
                '%(asctime)s [%(name)s] %(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            ))
            self._logger.addHandler(handler)

    def _get_meta(self):
        """获取 Meta 配置类"""
        return getattr(self.__class__, 'Meta', NbCmd.Meta)

    @property
    def logger(self) -> logging.Logger:
        """日志器（懒初始化：子类未调 super().__init__() 时也能正常工作）"""
        if not hasattr(self, '_logger') or self._logger is None:
            self._setup_logging()
        return self._logger

    # ==================== 生命周期钩子 ====================

    def before_run(self):
        """所有子命令执行前的钩子，子类可覆写"""
        pass

    def after_run(self):
        """所有子命令执行后的钩子，子类可覆写"""
        pass

    def on_error(self, command, error):
        """子命令执行出错时的钩子，子类可覆写"""
        self.logger.error('命令 {} 执行失败: {}'.format(command, error))

    # ==================== 系统命令工具 ====================

    def shell(self, cmd, capture=False, check=False):
        """
        执行系统命令。

        Parameters
        ----------
        cmd : str  要执行的命令
        capture : bool  是否捕获输出（True 返回 stdout 字符串，False 通过 print 输出）
        check : bool  命令失败时是否抛出异常

        Returns
        -------
        str (capture=True 时返回 stdout) 或 None
        """
        import subprocess
        if capture:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True,
            )
            if check and result.returncode != 0:
                raise RuntimeError(
                    '命令执行失败 (exit {}): {}\n{}'.format(
                        result.returncode, cmd, result.stderr
                    )
                )
            return result.stdout.strip()

        proc = subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1,
        )
        try:
            if proc.stdout:
                for line in proc.stdout:
                    print(line, end='')
            proc.wait()
        except KeyboardInterrupt:
            proc.kill()
            proc.wait()
            raise
        if check and proc.returncode != 0:
            raise RuntimeError(
                '命令执行失败 (exit {}): {}'.format(proc.returncode, cmd)
            )

    def exec(self, cmd: Annotated[str, '要执行的系统命令', 'c']):
        """执行任意系统命令"""
        self.shell(cmd)

    # ==================== 主入口 ====================

    def run(self, args=None):
        """
        主入口方法。根据参数决定运行模式。

        Parameters
        ----------
        args : list, optional
            命令行参数列表，默认使用 sys.argv[1:]
        """
        raw_args = args if args is not None else sys.argv[1:]

        help_result = self._handle_help(raw_args)
        if help_result is not None:
            return help_result

        if '--web' in raw_args:
            return self._start_web_server(raw_args)

        if '--tui' in raw_args:
            return self._start_tui()

        from ..modes.cli_mode import run_cli
        return run_cli(self, NbCmd, args)

    _HELP_HANDLED = object()

    def _handle_help(self, raw_args):
        """
        处理帮助参数（在 argparse 解析之前拦截）。
        -fh/--full-help: 始终显示完整帮助
        -eh/--easy-help: 始终显示简易帮助
        -h/--help: 由 Meta.help_mode 决定

        返回 _HELP_HANDLED 表示已处理，应结束。返回 None 表示未处理。
        """
        if '--full-help' in raw_args or '-fh' in raw_args:
            from .parser import print_full_help
            print_full_help(self, NbCmd)
            return self._HELP_HANDLED

        if '--easy-help' in raw_args or '-eh' in raw_args:
            from .parser import print_easy_help
            print_easy_help(self, NbCmd)
            return self._HELP_HANDLED

        meta = self._get_meta()
        help_mode = getattr(meta, 'help_mode', 'full')
        if help_mode == 'full' and ('--help' in raw_args or '-h' in raw_args):
            from .parser import print_full_help
            print_full_help(self, NbCmd)
            return self._HELP_HANDLED

        return None

    def _start_web_server(self, raw_args):
        """启动 Web UI 服务"""
        port = self._extract_port(raw_args)
        meta = self._get_meta()
        host = getattr(meta, 'serve_host', '0.0.0.0')
        if port is None:
            port = getattr(meta, 'serve_port', 8080)

        from ..modes.web_mode import start_web_server
        start_web_server(self, NbCmd, host=host, port=port)

    def _start_tui(self):
        """启动 TUI 模式"""
        from ..modes.tui_mode import start_tui
        start_tui(self, NbCmd)

    @staticmethod
    def _extract_port(raw_args):
        """从参数列表中提取 --web-port 的值"""
        if '--web-port' in raw_args:
            idx = raw_args.index('--web-port')
            if idx + 1 < len(raw_args):
                try:
                    return int(raw_args[idx + 1])
                except ValueError:
                    pass
        return None

`````

--- **end of file: nb_cmd/core/base.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/discovery.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
命令发现模块 —— 通过反射发现类中的所有公有方法，自动转换为子命令。
"""
import sys
import inspect

if sys.version_info >= (3, 11):
    from typing import get_type_hints
elif sys.version_info >= (3, 9):
    from typing import get_type_hints
else:
    try:
        from typing_extensions import get_type_hints
    except ImportError:
        from typing import get_type_hints as _get_type_hints

        def get_type_hints(func, **kwargs):
            kwargs.pop('include_extras', None)
            return _get_type_hints(func, **kwargs)

from .arg import unwrap_arg


def discover_commands(instance, base_cls, include_builtins=True, enable_exec=True,
                      allow_method_list=None, hide_method_list=None, command_prefix=''):
    """
    发现 instance 上所有应暴露为 CLI 子命令的方法，以及 sub_commands 中的子命令组。

    Parameters
    ----------
    include_builtins : bool
        是否包含基类内置命令（如 exec），顶层类为 True，子命令组为 False
    enable_exec : bool
        是否启用内置 exec 命令，由 Meta.enable_exec 控制
    allow_method_list : list[str] or None
        命令白名单。为空/None 表示不过滤；有值时仅暴露白名单命令。
        支持写法：['status', 'db.migrate', 'db/migrate', 'db migrate']。
    hide_method_list : list[str] or None
        命令黑名单。为空/None 表示不过滤；有值时隐藏指定命令。
        与 allow_method_list 互斥，同时配置时 allow_method_list 优先。
    command_prefix : str
        当前 discover 所在的命令路径前缀（内部递归使用）。

    返回: OrderedDict  { cmd_name: cmd_info_dict }
    """
    from collections import OrderedDict
    commands = OrderedDict()
    allow_set = _normalize_allow_method_set(allow_method_list)
    hide_set = _normalize_allow_method_set(hide_method_list) if not allow_set else set()
    current_prefix = _normalize_command_path(command_prefix)

    _BUILTIN_COMMANDS = {'exec'} if (include_builtins and enable_exec) else set()
    base_methods = set(dir(base_cls)) - _BUILTIN_COMMANDS

    for name in sorted(dir(instance)):
        if name.startswith('_'):
            continue
        if name in base_methods:
            continue
        if name in ('sub_commands',):
            continue

        attr = getattr(instance, name, None)
        if attr is None:
            continue
        if not callable(attr):
            continue
        if not (inspect.ismethod(attr) or inspect.isfunction(attr)):
            continue

        sig = inspect.signature(attr)
        doc = inspect.getdoc(attr) or ""

        try:
            hints = get_type_hints(attr, include_extras=True)
        except Exception:
            hints = {}

        real_hints = {}
        arg_meta = {}
        missing_types = []

        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
            raw_hint = hints.get(param_name)
            if raw_hint is None:
                anno = param.annotation
                if anno is not inspect.Parameter.empty:
                    raw_hint = anno
            if raw_hint is None:
                missing_types.append(param_name)
                continue
            real_type, arg_inst = unwrap_arg(raw_hint)
            real_hints[param_name] = real_type
            if arg_inst is not None:
                arg_meta[param_name] = arg_inst

        if missing_types:
            cls_name = instance.__class__.__name__
            raise TypeError(
                '{cls}.{method}() 的参数 {params} 缺少类型注解。'
                'nb_cmd 要求所有公有方法的参数必须声明类型，例如: '
                'def {method}(self, {example}: str)'.format(
                    cls=cls_name,
                    method=name,
                    params=', '.join("'{}'".format(p) for p in missing_types),
                    example=missing_types[0],
                )
            )

        full_path = _join_command_path(current_prefix, name)
        if not _is_method_allowed(full_path, allow_set):
            continue
        if _is_method_hidden(full_path, hide_set):
            continue

        commands[name] = {
            'method': attr,
            'signature': sig,
            'type_hints': real_hints,
            'arg_meta': arg_meta,
            'doc': doc.split('\n')[0],
            'full_doc': doc,
            'is_group': False,
        }

    sub_cmds = getattr(instance.__class__, 'sub_commands', {})
    for group_name, group_val in sub_cmds.items():
        group_path = _join_command_path(current_prefix, group_name)
        if not _is_group_allowed(group_path, allow_set):
            continue
        if _is_group_hidden(group_path, hide_set):
            continue

        if inspect.isclass(group_val) and issubclass(group_val, base_cls):
            commands[group_name] = {
                'cls': group_val,
                'doc': (inspect.getdoc(group_val) or "").split('\n')[0],
                'is_group': True,
                'init_kwargs': {},
            }
        elif isinstance(group_val, dict) and 'cls' in group_val:
            group_cls = group_val['cls']
            commands[group_name] = {
                'cls': group_cls,
                'doc': group_val.get('doc', (inspect.getdoc(group_cls) or "").split('\n')[0]),
                'is_group': True,
                'init_kwargs': {k: v for k, v in group_val.items() if k not in ('cls', 'doc')},
            }
        elif isinstance(group_val, base_cls):
            group_cls = group_val.__class__
            commands[group_name] = {
                'cls': group_cls,
                'doc': (inspect.getdoc(group_cls) or "").split('\n')[0],
                'is_group': True,
                'init_kwargs': _extract_init_kwargs(group_val),
            }

    if _BUILTIN_COMMANDS:
        ordered = OrderedDict()
        for builtin_name in sorted(_BUILTIN_COMMANDS):
            if builtin_name in commands:
                ordered[builtin_name] = commands.pop(builtin_name)
        ordered.update(commands)
        return ordered

    return commands


def _normalize_allow_method_set(allow_method_list):
    """
    归一化 allow_method_list，返回 set。

    - None / [] / () / '' -> 空 set（表示不过滤）
    - str -> 视为单条规则
    - 路径分隔支持 '.', '/', 空格
    - CLI 风格 '-' 自动转为 '_'（与 Python 方法名对齐）
    """
    if allow_method_list is None:
        return set()

    if isinstance(allow_method_list, str):
        raw_items = [allow_method_list]
    elif isinstance(allow_method_list, (list, tuple, set)):
        raw_items = list(allow_method_list)
    else:
        raw_items = [str(allow_method_list)]

    normalized = set()
    for item in raw_items:
        p = _normalize_command_path(item)
        if p:
            normalized.add(p)
    return normalized


def _normalize_command_path(path):
    """将命令路径统一为 'group/sub/cmd' 形式（内部用 '_' 命名）。"""
    if path is None:
        return ''
    s = str(path).strip()
    if not s:
        return ''

    # 支持 db.migrate / db/migrate / db migrate
    s = s.replace('\\', '/').replace('.', '/').replace(' ', '/')
    while '//' in s:
        s = s.replace('//', '/')
    s = s.strip('/')
    if not s:
        return ''

    parts = []
    for part in s.split('/'):
        p = part.strip()
        if not p:
            continue
        parts.append(p.replace('-', '_'))
    return '/'.join(parts)


def _join_command_path(prefix, name):
    """拼接完整命令路径。"""
    p = _normalize_command_path(prefix)
    n = _normalize_command_path(name)
    if not p:
        return n
    if not n:
        return p
    return p + '/' + n


def _iter_ancestor_paths(path):
    """迭代 path 的祖先路径（不含自身），用于白名单祖先命中判断。"""
    p = _normalize_command_path(path)
    if not p:
        return []
    parts = p.split('/')
    ancestors = []
    # issue/list -> ['issue']
    for i in range(1, len(parts)):
        ancestors.append('/'.join(parts[:i]))
    return ancestors


def _is_method_allowed(method_path, allow_set):
    """方法是否在白名单内（支持父组命中）。"""
    if not allow_set:
        return True

    p = _normalize_command_path(method_path)
    if p in allow_set:
        return True

    # allow=['issue'] 时，issue 下所有方法可见
    for anc in _iter_ancestor_paths(p):
        if anc in allow_set:
            return True
    return False


def _is_group_allowed(group_path, allow_set):
    """命令组是否需要暴露（自身命中、祖先命中、或有子命令命中）。"""
    if not allow_set:
        return True

    p = _normalize_command_path(group_path)
    if p in allow_set:
        return True

    # allow=['admin']，admin/ops 也应可见
    for anc in _iter_ancestor_paths(p):
        if anc in allow_set:
            return True

    # allow=['issue/list']，issue 组需保留用于路由到子命令
    prefix = p + '/'
    for item in allow_set:
        if item.startswith(prefix):
            return True
    return False


def _is_method_hidden(method_path, hide_set):
    """方法是否在黑名单内（精确命中或祖先组被隐藏）。"""
    if not hide_set:
        return False
    p = _normalize_command_path(method_path)
    if p in hide_set:
        return True
    for anc in _iter_ancestor_paths(p):
        if anc in hide_set:
            return True
    return False


def _is_group_hidden(group_path, hide_set):
    """命令组是否整体被隐藏（自身命中或祖先命中）。"""
    if not hide_set:
        return False
    p = _normalize_command_path(group_path)
    if p in hide_set:
        return True
    for anc in _iter_ancestor_paths(p):
        if anc in hide_set:
            return True
    return False


def _extract_init_kwargs(instance):
    """从实例上提取 __init__ 参数的当前值，用于子命令组的重新实例化"""
    cls = instance.__class__
    init_method = cls.__init__
    if init_method is object.__init__:
        return {}
    sig = inspect.signature(init_method)
    kwargs = {}
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        if hasattr(instance, pname):
            kwargs[pname] = getattr(instance, pname)
    return kwargs

`````

--- **end of file: nb_cmd/core/discovery.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/gen_cmd.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
命令行示例生成器 —— 自动生成 CLI 用法示例和完整文档。

用法::

    from nb_cmd import CmdGen

    g = CmdGen(MyApp, script='app.py')
    print(g.cmd(DbTool.migrate))
    print(g.doc())
"""
import sys
import inspect

from .discovery import discover_commands


class CmdGen(object):
    """
    命令行示例生成器。

    Parameters
    ----------
    entry_cls : class
        顶层入口类，如 MyApp
    script : str, optional
        脚本名。默认用 sys.argv[0]。
    python : str, optional
        Python 解释器路径。默认用 sys.executable（当前解释器完整路径）。
    fmt : str
        输出格式: 'text' (纯文本) | 'markdown' (markdown 代码块)
    """

    def __init__(self, entry_cls, script=None, python=None, fmt='text'):
        self.entry_cls = entry_cls
        self.script = script or _get_script_name()
        self.python = python or sys.executable
        self.fmt = fmt
        self._base_cls = _find_base_cls(entry_cls)
        self._allow_methods = _get_allow_method_list(entry_cls)
        self._hide_methods = _get_hide_method_list(entry_cls)

    def cmd(self, method):
        """
        生成单个方法的 CLI 命令行示例。

        Parameters
        ----------
        method : unbound method
            目标方法，如 DbTool.migrate

        Returns
        -------
        str
            生成的命令行示例字符串
        """
        method_name = method.__name__
        method_cls = _get_method_class(method)

        global_args = _format_init_args(self.entry_cls)
        path = _find_command_path(self.entry_cls, method_cls, self._base_cls)

        method_args = _format_method_args(method)
        cmd_name = method_name.replace('_', '-')

        parts = [self.python, self.script]
        if global_args:
            parts.append(global_args)
        if path:
            parts.append(path)
        parts.append(cmd_name)
        if method_args:
            parts.append(method_args)

        cmd_line = ' '.join(parts)
        return _apply_fmt(cmd_line, self.fmt)

    def doc(self, file=None):
        """
        生成入口类的完整命令行文档。

        包含完整帮助信息和每个命令的可复制命令行示例。
        当 fmt='markdown' 或 file 以 .md 结尾时，输出高质量 Markdown 文档。

        Parameters
        ----------
        file : str, optional
            输出文件路径。传入后自动写入文件并返回文件路径。

        Returns
        -------
        str
            生成的完整文档字符串（传了 file 时同时写入文件）
        """
        use_md = self.fmt == 'markdown'
        if not use_md and file and file.endswith('.md'):
            use_md = True

        if use_md:
            text = self._build_md_doc()
        else:
            text = self._build_text_doc()

        if file is not None:
            import os
            dir_name = os.path.dirname(file)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(text)

        return text

    def _build_text_doc(self):
        """构建纯文本格式的完整文档"""
        from .parser import get_full_help_text

        meta = getattr(self.entry_cls, 'Meta', None)
        app_name = getattr(meta, 'name', self.entry_cls.__name__) if meta else self.entry_cls.__name__

        instance = _safe_instantiate(self.entry_cls)
        full_help = get_full_help_text(instance, self._base_cls)

        lines = ['[This Doc Is Auto-generated by nb-cmd CmdGen]', '', full_help.rstrip(), '']
        lines.append('{} 命令行示例'.format(app_name))
        lines.append('=' * (len(app_name) + 14))

        global_args = _format_init_args(self.entry_cls)
        commands = discover_commands(instance, self._base_cls,
                                     include_builtins=False, enable_exec=False,
                                     allow_method_list=self._allow_methods,
                                     hide_method_list=self._hide_methods)
        _collect_text_doc(commands, self._base_cls, self.script, self.python,
                          global_args, '', lines, depth=0,
                          allow_method_list=self._allow_methods,
                          hide_method_list=self._hide_methods,
                          command_prefix='')

        return '\n'.join(lines)

    def _build_md_doc(self):
        """构建高质量 Markdown 格式的完整文档"""
        meta = getattr(self.entry_cls, 'Meta', type('Meta', (), {}))
        app_name = getattr(meta, 'name', self.entry_cls.__name__) if meta else self.entry_cls.__name__
        version = getattr(meta, 'version', '0.0.1') if meta else '0.0.1'
        instance = _safe_instantiate(self.entry_cls)
        description = inspect.getdoc(instance) or self.entry_cls.__name__

        commands = discover_commands(instance, self._base_cls,
                                     include_builtins=False, enable_exec=False,
                                     allow_method_list=self._allow_methods,
                                     hide_method_list=self._hide_methods)
        global_args = _format_init_args(self.entry_cls)

        lines = []

        lines.append('> *Auto-generated by nb-cmd CmdGen*')
        lines.append('')
        lines.append('# {} v{}'.format(app_name, version))
        lines.append('')
        lines.append('> {}'.format(description))
        lines.append('')

        toc_items = _collect_toc(commands, self._base_cls, prefix='',
                                 allow_method_list=self._allow_methods,
                                 hide_method_list=self._hide_methods,
                                 command_prefix='')
        if toc_items:
            lines.append('## Table of Contents')
            lines.append('')
            for item in toc_items:
                indent = '  ' * item['depth']
                anchor = item['display'].lower().replace(' ', '-').replace('_', '-')
                if item['is_group']:
                    lines.append('{}- [`{}`  *(子命令组)*](#{}-子命令组)'.format(
                        indent, item['display'], anchor))
                else:
                    lines.append('{}- [`{}`](#{})'.format(indent, item['display'], anchor))
            lines.append('')

        lines.append('---')
        lines.append('')

        lines.append('## System Params')
        lines.append('')
        lines.append('| Flag | Description |')
        lines.append('|------|-------------|')
        sys_params = [
            ('`-h`, `--help`', '显示帮助信息'),
            ('`-fh`, `--full-help`', '显示完整帮助（所有参数详情）'),
            ('`-eh`, `--easy-help`', '显示简易帮助（argparse 原生格式）'),
            ('`--cmd-version`', '显示版本号'),
            ('`--web`', '以 Web UI + REST API 模式启动'),
            ('`--web-port PORT`', 'Web UI 服务端口（用于 `--web`）'),
            ('`--tui`', '以 TUI 终端交互模式启动'),
        ]
        for flag, desc in sys_params:
            lines.append('| {} | {} |'.format(flag, desc))
        lines.append('')

        init_params = _collect_init_params(self.entry_cls)
        if init_params:
            lines.append('## Global Params (`__init__`)')
            lines.append('')
            lines.append('| Flag | Type | Default | Description |')
            lines.append('|------|------|---------|-------------|')
            for p in init_params:
                lines.append('| `{}` | `{}` | `{}` | {} |'.format(
                    p['flag'], p['type'], p['default'], p['desc']))
            lines.append('')

        lines.append('## Quick Start')
        lines.append('')
        lines.append('```bash')
        lines.append('# 查看完整帮助')
        lines.append('{} {} -fh'.format(self.python, self.script))
        lines.append('')
        lines.append('# 查看版本')
        lines.append('{} {} --cmd-version'.format(self.python, self.script))
        lines.append('')
        lines.append('# 启动 Web UI')
        lines.append('{} {} --web'.format(self.python, self.script))
        lines.append('')
        lines.append('# 启动 TUI 终端交互')
        lines.append('{} {} --tui'.format(self.python, self.script))
        lines.append('```')
        lines.append('')

        lines.append('## 命令行约定')
        lines.append('')
        lines.append('命令格式：`python script.py [全局参数] <子命令路径> [命令参数]`')
        lines.append('')
        lines.append('| 标记 | 含义 |')
        lines.append('|------|------|')
        lines.append('| `${value}` | 带默认值的参数 — 可按需替换 |')
        lines.append('| `$<name>` | **必填**参数 — 必须提供值 |')
        lines.append('| `--flag`（无值） | 布尔开关，添加即启用 |')
        lines.append('')

        lines.append('---')
        lines.append('')
        lines.append('## Commands')
        lines.append('')

        _collect_md_doc(commands, self._base_cls, self.script, self.python,
                        global_args, '', lines, depth=0,
                        allow_method_list=self._allow_methods,
                        hide_method_list=self._hide_methods,
                        command_prefix='')

        return '\n'.join(lines)


def _collect_toc(commands, base_cls, prefix='', depth=0, allow_method_list=None,
                 hide_method_list=None, command_prefix=''):
    """递归收集命令目录结构"""
    items = []
    for cmd_name, cmd_info in commands.items():
        full_path = '{} {}'.format(prefix, cmd_name).strip() if prefix else cmd_name
        display = full_path.replace('_', '-')

        if cmd_info.get('is_group'):
            items.append({'display': display, 'is_group': True, 'depth': depth})
            group_cls = cmd_info['cls']
            group_instance = _safe_instantiate(group_cls)
            group_path = '{}/{}'.format(command_prefix, cmd_name) if command_prefix else cmd_name
            sub_commands = discover_commands(group_instance, base_cls,
                                             include_builtins=False, enable_exec=False,
                                             allow_method_list=allow_method_list,
                                             hide_method_list=hide_method_list,
                                             command_prefix=group_path)
            items.extend(_collect_toc(sub_commands, base_cls, prefix=full_path,
                                      depth=depth + 1,
                                      allow_method_list=allow_method_list,
                                      hide_method_list=hide_method_list,
                                      command_prefix=group_path))
        else:
            items.append({'display': display, 'is_group': False, 'depth': depth})
    return items


def _collect_init_params(entry_cls):
    """收集 __init__ 的全局参数信息列表"""
    from .arg import unwrap_arg
    from .type_utils import type_display_name

    init_method = entry_cls.__init__
    if init_method is object.__init__:
        return []

    sig = inspect.signature(init_method)
    results = []
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        has_default = param.default is not inspect.Parameter.empty
        default_val = param.default if has_default else None
        raw_hint = param.annotation
        if raw_hint is inspect.Parameter.empty:
            raw_hint = type(default_val) if default_val is not None else str
        real_type, arg_inst = unwrap_arg(raw_hint)
        desc = arg_inst.desc if arg_inst and arg_inst.desc else ''
        flag = '--{}'.format(pname.replace('_', '-'))
        if arg_inst and arg_inst.aliases:
            flag = '{}, {}'.format(flag, ', '.join(arg_inst.aliases))
        results.append({
            'flag': flag,
            'type': type_display_name(real_type),
            'default': default_val if has_default else '*(required)*',
            'desc': desc or '-',
        })
    return results


def _collect_text_doc(commands, base_cls, script_name, python_path, global_args,
                      prefix, lines, depth, allow_method_list=None,
                      hide_method_list=None, command_prefix=''):
    """递归收集纯文本格式的命令文档"""
    for cmd_name, cmd_info in commands.items():
        full_path = '{} {}'.format(prefix, cmd_name).strip() if prefix else cmd_name

        if cmd_info.get('is_group'):
            group_cls = cmd_info['cls']
            group_doc = cmd_info.get('doc', '')
            indent = '  ' * depth
            lines.append('')
            lines.append('{}[{}]  {}'.format(indent, full_path, group_doc))
            group_instance = _safe_instantiate(group_cls)
            group_path = '{}/{}'.format(command_prefix, cmd_name) if command_prefix else cmd_name
            sub_commands = discover_commands(group_instance, base_cls,
                                             include_builtins=False, enable_exec=False,
                                             allow_method_list=allow_method_list,
                                             hide_method_list=hide_method_list,
                                             command_prefix=group_path)
            _collect_text_doc(sub_commands, base_cls, script_name, python_path,
                              global_args, full_path, lines, depth=depth + 1,
                              allow_method_list=allow_method_list,
                              hide_method_list=hide_method_list,
                              command_prefix=group_path)
        else:
            method = cmd_info['method']
            doc = cmd_info.get('doc', '')
            method_args = _format_method_args(method)
            display_name = cmd_name.replace('_', '-')
            parts = [python_path, script_name]
            if global_args:
                parts.append(global_args)
            if prefix:
                parts.append(prefix)
            parts.append(display_name)
            if method_args:
                parts.append(method_args)
            cmd_line = ' '.join(parts)
            indent = '  ' * depth
            lines.append('')
            lines.append('{}{}  {}'.format(indent, full_path.replace('_', '-'), doc))
            lines.append('{}  {}'.format(indent, cmd_line))


def _collect_md_doc(commands, base_cls, script_name, python_path, global_args,
                    prefix, lines, depth, allow_method_list=None,
                    hide_method_list=None, command_prefix=''):
    """递归收集 Markdown 格式的命令文档"""
    from .type_utils import (
        is_optional, unwrap_optional, type_display_name,
    )

    for cmd_name, cmd_info in commands.items():
        full_path = '{} {}'.format(prefix, cmd_name).strip() if prefix else cmd_name
        display = full_path.replace('_', '-')

        if cmd_info.get('is_group'):
            group_cls = cmd_info['cls']
            group_doc = cmd_info.get('doc', '')
            level = '#' * min(depth + 3, 6)
            lines.append('{} `{}` *(子命令组)*'.format(level, display))
            lines.append('')
            if group_doc:
                lines.append('> {}'.format(group_doc))
                lines.append('')
            group_instance = _safe_instantiate(group_cls)
            group_path = '{}/{}'.format(command_prefix, cmd_name) if command_prefix else cmd_name
            sub_commands = discover_commands(group_instance, base_cls,
                                             include_builtins=False, enable_exec=False,
                                             allow_method_list=allow_method_list,
                                             hide_method_list=hide_method_list,
                                             command_prefix=group_path)
            _collect_md_doc(sub_commands, base_cls, script_name, python_path,
                            global_args, full_path, lines, depth=depth + 1,
                            allow_method_list=allow_method_list,
                            hide_method_list=hide_method_list,
                            command_prefix=group_path)
        else:
            method = cmd_info['method']
            doc = cmd_info.get('doc', '')
            method_args = _format_method_args(method)
            display_name = cmd_name.replace('_', '-')

            parts = [python_path, script_name]
            if global_args:
                parts.append(global_args)
            if prefix:
                parts.append(prefix)
            parts.append(display_name)
            if method_args:
                parts.append(method_args)
            cmd_line = ' '.join(parts)

            level = '#' * min(depth + 3, 6)
            lines.append('{} `{}`'.format(level, display))
            lines.append('')
            if doc:
                lines.append(doc)
                lines.append('')

            sig = cmd_info['signature']
            hints = cmd_info.get('type_hints', {})
            arg_meta = cmd_info.get('arg_meta', {})
            param_rows = []
            for pname, param in sig.parameters.items():
                if pname == 'self':
                    continue
                ptype = hints.get(pname, str)
                real_type = unwrap_optional(ptype) if is_optional(ptype) else ptype
                tname = type_display_name(real_type)
                has_default = param.default is not inspect.Parameter.empty
                arg_inst = arg_meta.get(pname)
                desc = arg_inst.desc if arg_inst and arg_inst.desc else '-'
                flag = '--{}'.format(pname.replace('_', '-'))
                if arg_inst and arg_inst.aliases:
                    flag = '{}, {}'.format(flag, ', '.join(arg_inst.aliases))
                default_str = '`{}`'.format(param.default) if has_default else '*(required)*'
                param_rows.append((flag, tname, default_str, desc))

            if param_rows:
                lines.append('| Param | Type | Default | Description |')
                lines.append('|-------|------|---------|-------------|')
                for flag, tname, default_str, desc in param_rows:
                    lines.append('| `{}` | `{}` | {} | {} |'.format(
                        flag, tname, default_str, desc))
                lines.append('')

            lines.append('```bash')
            lines.append(cmd_line)
            lines.append('```')
            lines.append('')


def _get_script_name():
    """获取当前脚本名"""
    import os
    name = sys.argv[0] if sys.argv[0] else 'script.py'
    return os.path.basename(name)


def _get_method_class(method):
    """从 unbound method 获取所属类"""
    qualname = getattr(method, '__qualname__', '')
    parts = qualname.split('.')
    if len(parts) >= 2:
        cls_name = parts[-2]
        module = inspect.getmodule(method)
        if module:
            cls = getattr(module, cls_name, None)
            if cls is not None:
                return cls
    return None


def _find_base_cls(entry_cls):
    """找到 NbCmd 基类"""
    from .base import NbCmd
    return NbCmd


def _get_allow_method_list(entry_cls):
    """从 entry_cls.Meta 获取命令白名单（为空表示不过滤）。"""
    meta = getattr(entry_cls, 'Meta', None)
    if meta is None:
        return None
    return getattr(meta, 'allow_method_list', None)


def _get_hide_method_list(entry_cls):
    """从 entry_cls.Meta 获取命令黑名单（为空表示不过滤）。"""
    meta = getattr(entry_cls, 'Meta', None)
    if meta is None:
        return None
    return getattr(meta, 'hide_method_list', None)


def _find_command_path(entry_cls, target_cls, base_cls):
    """
    从 entry_cls 的 sub_commands 树中递归搜索 target_cls，
    返回子命令组路径字符串（如 'db' 或 'server ops'）。
    """
    if target_cls is None or target_cls is entry_cls:
        return ''

    sub_cmds = getattr(entry_cls, 'sub_commands', {})
    for group_name, group_val in sub_cmds.items():
        group_cls = group_val if inspect.isclass(group_val) else group_val.__class__
        if group_cls is target_cls:
            return group_name

        deeper = _find_command_path(group_cls, target_cls, base_cls)
        if deeper:
            return '{} {}'.format(group_name, deeper)

    return ''


def _format_init_args(entry_cls):
    """将 entry_cls 的 __init__ 参数格式化为 CLI 全局参数字符串"""
    init_method = entry_cls.__init__
    if init_method is object.__init__:
        return ''

    sig = inspect.signature(init_method)
    parts = []
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        flag = '--{}'.format(pname.replace('_', '-'))
        default = param.default
        if default is inspect.Parameter.empty:
            ptype = param.annotation if param.annotation is not inspect.Parameter.empty else str
            if ptype is bool:
                parts.append(flag)
            else:
                parts.append('{} $<{}>'.format(flag, pname))
        else:
            if isinstance(default, bool):
                if not default:
                    parts.append(flag)
            else:
                parts.append('{} ${{{}}}'.format(flag, default))

    return ' '.join(parts)


def _format_method_args(method):
    """将方法的参数格式化为 CLI 参数字符串"""
    sig = inspect.signature(method)
    parts = []
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        flag = '--{}'.format(pname.replace('_', '-'))
        default = param.default
        ptype = param.annotation if param.annotation is not inspect.Parameter.empty else str

        if default is inspect.Parameter.empty:
            if ptype is bool:
                parts.append(flag)
            else:
                parts.append('{} $<{}>'.format(flag, pname))
        else:
            if isinstance(default, bool):
                if not default:
                    parts.append(flag)
            else:
                parts.append('{} ${{{}}}'.format(flag, default))

    return ' '.join(parts)


def _safe_instantiate(cls):
    """安全实例化类，失败时用 __new__"""
    try:
        return cls()
    except TypeError:
        return cls.__new__(cls)


def _apply_fmt(cmd_line, fmt):
    """应用输出格式"""
    if fmt == 'markdown':
        return '```bash\n{}\n```'.format(cmd_line)
    return cmd_line

`````

--- **end of file: nb_cmd/core/gen_cmd.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/gen_skill.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
AI Skill 文件夹生成器 —— 自动生成符合 agentskills.io 规范的 Skill 文件夹。

用法::

    from nb_cmd import SkillGen

    g = SkillGen(MyApp, base_dir='./skills')
    g.gen()
"""
import os
import re
import sys
import inspect

from .discovery import discover_commands
from .gen_cmd import (
    _find_base_cls,
    _get_allow_method_list,
    _get_hide_method_list,
    _find_command_path,
    _format_init_args,
    _format_method_args,
    _safe_instantiate,
    _collect_init_params,
)
from .type_utils import is_optional, unwrap_optional, type_display_name


class SkillGen(object):
    """
    AI Skill 文件夹生成器。

    根据 NbCmd 子类的结构，自动生成符合 agentskills.io 规范的 Skill 文件夹。

    Parameters
    ----------
    entry_cls : class
        顶层入口类，如 MyApp
    name : str, optional
        Skill name（默认从 Meta.name 或类名转 kebab-case）。
        最终生成的 Skill 文件夹名即为 name。
    base_dir : str, optional
        父目录路径。默认当前目录 `.`。最终输出路径为 `{base_dir}/{name}/`。
    script : str, optional
        脚本名。默认用 sys.argv[0]。
    python : str, optional
        Python 解释器路径。默认用 sys.executable。
    description : str, optional
        Skill description（默认从 Meta.description 或类 docstring）
    license : str, optional
        License 名称
    compatibility : str, optional
        环境兼容性说明
    metadata : dict, optional
        额外元数据键值对
    allowed_tools : str, optional
        允许使用的工具列表（空格分隔）
    disable_model_invocation : bool, optional
        是否禁用模型自动触发（默认 False，允许自动触发）
    user_highest_priority_skill_prompt : str, optional
        用户自定义的最高优先级提示语，会放在 SKILL.md 的显要位置。
        可用于告知 AI 运行环境信息（如 Python 解释器路径、脚本位置、
        PYTHONPATH 设置等）。
    include_cli_examples : bool, optional
        是否在 SKILL.md 中包含 CLI 命令示例（默认 True）
    include_python_examples : bool, optional
        是否在 SKILL.md 中包含 Python 调用示例（默认 False）
    include_api_examples : bool, optional
        是否在 SKILL.md 中包含 REST API 调用示例（默认 False）
    """

    def __init__(
        self,
        entry_cls,
        name=None,
        base_dir='.',
        script=None,
        python=None,
        description=None,
        license=None,
        compatibility=None,
        metadata=None,
        allowed_tools=None,
        disable_model_invocation=False,
        user_highest_priority_skill_prompt=None,
        include_cli_examples=True,
        include_python_examples=False,
        include_api_examples=False,
    ):
        self.entry_cls = entry_cls
        self._base_dir = base_dir
        self.script = script or self._get_script_name()
        self.python = python or sys.executable
        self._base_cls = _find_base_cls(entry_cls)
        self._allow_methods = _get_allow_method_list(entry_cls)
        self._hide_methods = _get_hide_method_list(entry_cls)

        self._user_name = name
        self._user_description = description
        self._license = license
        self._compatibility = compatibility
        self._metadata = metadata or {}
        self._allowed_tools = allowed_tools
        self._disable_model_invocation = disable_model_invocation
        self._user_priority_prompt = user_highest_priority_skill_prompt

        self._include_cli = include_cli_examples
        self._include_python = include_python_examples
        self._include_api = include_api_examples

        self._name = self._resolve_name()
        self._description = self._resolve_description()
        self._validate_name()
        self._validate_description()
        self.output_dir = os.path.join(self._base_dir, self._name)

    def _get_script_name(self):
        import os
        name = sys.argv[0] if sys.argv[0] else 'script.py'
        return os.path.basename(name)

    def _resolve_name(self):
        """解析 Skill name，优先级：用户传入 > Meta.name > 类名转 kebab-case"""
        if self._user_name:
            return self._user_name.strip()
        meta = getattr(self.entry_cls, 'Meta', None)
        if meta:
            meta_name = getattr(meta, 'name', None)
            if meta_name:
                return self._to_kebab_case(meta_name)
        return self._to_kebab_case(self.entry_cls.__name__)

    def _to_kebab_case(self, s):
        """将字符串转为 kebab-case"""
        s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', s)
        s = re.sub(r'([a-z\d])([A-Z])', r'\1-\2', s)
        s = s.lower().replace('_', '-').replace(' ', '-')
        s = re.sub(r'-+', '-', s)
        return s.strip('-')

    def _validate_name(self):
        """校验 name 是否符合 agentskills.io 规范"""
        n = self._name
        if not n:
            raise ValueError('Skill name cannot be empty')
        if len(n) > 64:
            raise ValueError('Skill name must be <= 64 characters, got {}'.format(len(n)))
        if n.startswith('-') or n.endswith('-'):
            raise ValueError('Skill name cannot start or end with a hyphen')
        if '--' in n:
            raise ValueError('Skill name cannot contain consecutive hyphens')
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', n):
            raise ValueError(
                'Skill name must be lowercase alphanumeric with hyphens only, '
                'got: {}'.format(n)
            )

    def _resolve_description(self):
        """解析 Skill description，优先级：用户传入 > Meta.description > 类 docstring > 自动生成"""
        if self._user_description:
            return self._user_description.strip()
        meta = getattr(self.entry_cls, 'Meta', None)
        if meta:
            meta_desc = getattr(meta, 'description', None)
            if meta_desc:
                return meta_desc.strip()
        doc = inspect.getdoc(self.entry_cls)
        if doc:
            lines = [ln.strip() for ln in doc.strip().split('\n') if ln.strip()]
            if lines:
                # 取前几句（不超过 200 字符），确保包含足够信息
                desc = lines[0]
                for ln in lines[1:]:
                    if len(desc) + len(ln) + 1 < 200:
                        desc += ' ' + ln
                    else:
                        break
                return desc
        return self._auto_description()

    def _auto_description(self):
        """自动生成 description（英文，适配任意工具）"""
        meta = getattr(self.entry_cls, 'Meta', None)
        app_name = getattr(meta, 'name', self.entry_cls.__name__) if meta else self.entry_cls.__name__
        instance = _safe_instantiate(self.entry_cls)
        commands = discover_commands(
            instance, self._base_cls,
            include_builtins=False, enable_exec=False,
            allow_method_list=self._allow_methods,
            hide_method_list=self._hide_methods,
        )
        cmd_names = [k.replace('_', '-') for k in commands.keys() if not commands[k].get('is_group')]
        if not cmd_names:
            cmd_names = [k.replace('_', '-') for k in commands.keys()]
        cmd_preview = ', '.join(cmd_names[:5])
        if len(commands) > 5:
            cmd_preview += ', etc.'
        desc = '{} —— supports operations such as {}. Activate when you need to run {} commands.'.format(
            app_name, cmd_preview, app_name
        )
        return desc

    def _validate_description(self):
        """校验 description 长度"""
        if not self._description:
            raise ValueError('Skill description cannot be empty')
        if len(self._description) > 1024:
            raise ValueError(
                'Skill description must be <= 1024 characters, got {}'.format(len(self._description))
            )

    def gen(self):
        """
        生成 Skill 文件夹（仅包含 SKILL.md）。

        Returns
        -------
        str
            生成的 Skill 文件夹路径
        """
        os.makedirs(self.output_dir, exist_ok=True)

        skill_md_content = self.gen_skill_md()
        skill_md_path = os.path.join(self.output_dir, 'SKILL.md')
        with open(skill_md_path, 'w', encoding='utf-8') as f:
            f.write(skill_md_content)

        return self.output_dir

    def gen_skill_md(self):
        """
        生成 SKILL.md 内容字符串。

        Returns
        -------
        str
            SKILL.md 完整内容
        """
        frontmatter = self._gen_frontmatter()
        body = self._gen_body()
        return frontmatter + '\n' + body

    def _gen_frontmatter(self):
        """生成 YAML frontmatter"""
        lines = ['---']
        lines.append('name: {}'.format(self._name))

        # description 使用 >- 折叠块样式（保留换行但折叠为空格）
        desc = self._description
        lines.append('description: >-')
        for paragraph in desc.split('\n\n'):
            for wrap_line in self._wrap_text(paragraph.strip(), 78):
                lines.append('  {}'.format(wrap_line))

        if self._license:
            lines.append('license: {}'.format(self._license))
        if self._compatibility:
            lines.append('compatibility: {}'.format(self._compatibility))
        if self._metadata:
            lines.append('metadata:')
            for k, v in self._metadata.items():
                val = str(v)
                # YAML 安全处理：如果值含双引号，用单引号包裹
                if '"' in val:
                    lines.append("  {}: '{}'".format(k, val))
                else:
                    lines.append('  {}: "{}"'.format(k, val))
        if self._allowed_tools:
            lines.append('allowed-tools: {}'.format(self._allowed_tools))
        if self._disable_model_invocation:
            lines.append('disable-model-invocation: true')

        lines.append('---')
        return '\n'.join(lines)

    def _wrap_text(self, text, width):
        """简单文本折行"""
        if len(text) <= width:
            return [text]
        words = text.split(' ')
        lines = []
        current = ''
        for word in words:
            if len(current) + len(word) + 1 > width:
                if current:
                    lines.append(current)
                current = word
            else:
                current = current + ' ' + word if current else word
        if current:
            lines.append(current)
        return lines if lines else ['']

    def _gen_body(self):
        """生成 Markdown body"""
        instance = _safe_instantiate(self.entry_cls)
        commands = discover_commands(
            instance, self._base_cls,
            include_builtins=False, enable_exec=False,
            allow_method_list=self._allow_methods,
            hide_method_list=self._hide_methods,
        )
        meta = getattr(self.entry_cls, 'Meta', type('Meta', (), {}))
        app_name = getattr(meta, 'name', self.entry_cls.__name__) if meta else self.entry_cls.__name__
        doc = inspect.getdoc(instance) or app_name

        lines = []
        lines.append('# {}'.format(app_name))
        lines.append('')
        lines.append('## Overview')
        lines.append('')
        lines.append(doc)
        lines.append('')

        if self._user_priority_prompt:
            lines.append('## Important')
            lines.append('')
            lines.append(self._user_priority_prompt)
            lines.append('')

        init_params = _collect_init_params(self.entry_cls)
        lines.append('## Guidelines')
        lines.append('')
        lines.append(self._gen_guidelines(init_params))
        lines.append('')

        lines.append('## When to Use')
        lines.append('')
        lines.append(self._gen_when_to_use(commands, app_name))
        lines.append('')

        lines.append('## Command Structure')
        lines.append('')
        lines.append(self._gen_command_structure())
        lines.append('')

        if init_params:
            lines.append('## Global Parameters')
            lines.append('')
            lines.append('These parameters are defined in `__init__` and passed to all subcommands automatically.')
            lines.append('')
            lines.append('| Flag | Type | Default | Description |')
            lines.append('|------|------|---------|-------------|')
            for p in init_params:
                lines.append('| `{}` | `{}` | `{}` | {} |'.format(
                    p['flag'], p['type'], p['default'], p['desc']))
            lines.append('')

        lines.append('## Commands')
        lines.append('')
        self._collect_skill_commands(
            commands, '', lines, depth=0,
            allow_method_list=self._allow_methods,
            hide_method_list=self._hide_methods,
            command_prefix='',
        )
        lines.append('')

        lines.append('## Implementation Note')
        lines.append('')
        lines.append(self._gen_impl_note())
        lines.append('')

        return '\n'.join(lines)

    def _gen_when_to_use(self, commands, app_name):
        """生成 When to Use 段落（递归收集所有叶子命令）"""
        cmd_names = []
        self._collect_leaf_commands(commands, '', cmd_names)

        when_lines = ['Activate this skill when you need to perform {}-related operations, such as:'.format(app_name)]
        for cmd_name in cmd_names[:15]:
            when_lines.append('- {}'.format(cmd_name))
        if len(cmd_names) > 15:
            when_lines.append('- And other {} commands'.format(app_name))
        return '\n'.join(when_lines)

    def _collect_leaf_commands(self, commands, prefix, result):
        """递归收集所有叶子命令名"""
        for cmd_name, cmd_info in commands.items():
            full_path = '{} {}'.format(prefix, cmd_name).strip() if prefix else cmd_name
            display = full_path.replace('_', '-')
            if cmd_info.get('is_group'):
                group_cls = cmd_info['cls']
                group_instance = _safe_instantiate(group_cls)
                sub_commands = discover_commands(
                    group_instance, self._base_cls,
                    include_builtins=False, enable_exec=False,
                    allow_method_list=self._allow_methods,
                    hide_method_list=self._hide_methods,
                )
                self._collect_leaf_commands(sub_commands, full_path, result)
            else:
                result.append(display)

    def _gen_command_structure(self):
        """生成命令结构说明"""
        lines = []
        if self._include_cli:
            lines.append('### CLI')
            lines.append('```bash')
            lines.append('{} {} [global_params] <command_path> [command_params]'.format(self.python, self.script))
            lines.append('```')
            lines.append('')
        if self._include_python:
            lines.append('### Python')
            lines.append('```python')
            lines.append('from {} import {}'.format(
                self._module_name_hint(), self.entry_cls.__name__))
            lines.append('app = {}()  # pass global params if needed'.format(self.entry_cls.__name__))
            lines.append('# app.subcommand.method(param=value)')
            lines.append('```')
            lines.append('')
        if self._include_api:
            lines.append('### REST API')
            lines.append('```bash')
            lines.append('curl -X POST http://localhost:8000/api/v1/<command_path> \\')
            lines.append('  -H "Content-Type: application/json" \\')
            lines.append('  -d \'{"param": "value"}\'')
            lines.append('```')
            lines.append('')
        lines.append('**Parameter conventions:**')
        lines.append('- `${value}` — parameter with default value (replace as needed)')
        lines.append('- `$<name>` — **required** parameter (must provide a value)')
        lines.append('- `--flag` (no value) — boolean switch (add to enable)')
        return '\n'.join(lines)

    def _module_name_hint(self):
        """推测模块导入名"""
        module = inspect.getmodule(self.entry_cls)
        if module and hasattr(module, '__name__') and module.__name__ != '__main__':
            return module.__name__
        return self.script.replace('.py', '').replace('/', '.').replace('\\', '.')

    def _collect_skill_commands(self, commands, prefix, lines, depth=0,
                                allow_method_list=None, hide_method_list=None,
                                command_prefix=''):
        """递归收集命令说明（面向 AI 的 Skill 格式）"""
        for cmd_name, cmd_info in commands.items():
            full_path = '{} {}'.format(prefix, cmd_name).strip() if prefix else cmd_name
            display = full_path.replace('_', '-')

            if cmd_info.get('is_group'):
                group_cls = cmd_info['cls']
                group_doc = cmd_info.get('doc', '')
                level = '###'
                lines.append('{} `{}` *(subcommand group)*'.format(level, display))
                lines.append('')
                if group_doc:
                    lines.append(group_doc)
                    lines.append('')
                group_instance = _safe_instantiate(group_cls)
                group_path = '{}/{}'.format(command_prefix, cmd_name) if command_prefix else cmd_name
                sub_commands = discover_commands(
                    group_instance, self._base_cls,
                    include_builtins=False, enable_exec=False,
                    allow_method_list=allow_method_list,
                    hide_method_list=hide_method_list,
                    command_prefix=group_path,
                )
                self._collect_skill_commands(
                    sub_commands, full_path, lines, depth=depth + 1,
                    allow_method_list=allow_method_list,
                    hide_method_list=hide_method_list,
                    command_prefix=group_path,
                )
            else:
                method = cmd_info['method']
                doc = cmd_info.get('doc', '')
                level = '###'
                lines.append('{} `{}`'.format(level, display))
                lines.append('')
                if doc:
                    lines.append(doc)
                    lines.append('')

                # 参数表格
                sig = cmd_info['signature']
                hints = cmd_info.get('type_hints', {})
                arg_meta = cmd_info.get('arg_meta', {})
                param_rows = []
                for pname, param in sig.parameters.items():
                    if pname == 'self':
                        continue
                    ptype = hints.get(pname, str)
                    real_type = unwrap_optional(ptype) if is_optional(ptype) else ptype
                    tname = type_display_name(real_type)
                    has_default = param.default is not inspect.Parameter.empty
                    arg_inst = arg_meta.get(pname)
                    desc = arg_inst.desc if arg_inst and arg_inst.desc else '-'
                    flag = '--{}'.format(pname.replace('_', '-'))
                    if arg_inst and arg_inst.aliases:
                        flag = '{}, {}'.format(flag, ', '.join(arg_inst.aliases))
                    default_str = '`{}`'.format(param.default) if has_default else '*(required)*'
                    param_rows.append((flag, tname, default_str, desc))

                lines.append('| Param | Type | Default | Description |')
                lines.append('|-------|------|---------|-------------|')
                if param_rows:
                    for flag, tname, default_str, desc in param_rows:
                        lines.append('| `{}` | `{}` | {} | {} |'.format(
                            flag, tname, default_str, desc))
                else:
                    lines.append('| *(none)* | — | — | This command takes no parameters. |')
                lines.append('')

                # 示例
                method_args = _format_method_args(method)
                display_name = cmd_name.replace('_', '-')

                if self._include_cli:
                    global_args = _format_init_args(self.entry_cls)
                    parts = [self.python, self.script]
                    if global_args:
                        parts.append(global_args)
                    if prefix:
                        parts.append(prefix.replace('_', '-'))
                    parts.append(display_name)
                    if method_args:
                        parts.append(method_args)
                    cmd_line = ' '.join(parts)
                    lines.append('**CLI:**')
                    lines.append('```bash')
                    lines.append(cmd_line)
                    lines.append('```')
                    lines.append('')

                if self._include_python:
                    lines.append('**Python:**')
                    lines.append('```python')
                    # 生成 Python 调用示例
                    py_parts = ['app']
                    if prefix:
                        for part in prefix.split():
                            py_parts.append(part.replace('_', ''))
                    py_parts.append('{}({})'.format(
                        cmd_name,
                        self._format_python_args(method),
                    ))
                    lines.append('.'.join(py_parts))
                    lines.append('```')
                    lines.append('')

    def _format_python_args(self, method):
        """格式化 Python 调用示例的参数"""
        sig = inspect.signature(method)
        parts = []
        for pname, param in sig.parameters.items():
            if pname == 'self':
                continue
            default = param.default
            if default is inspect.Parameter.empty:
                ptype = param.annotation if param.annotation is not inspect.Parameter.empty else str
                if ptype is bool:
                    parts.append('{}=True'.format(pname))
                else:
                    parts.append('{}=<{}>'.format(pname, pname))
            else:
                if isinstance(default, bool):
                    parts.append('{}={}'.format(pname, default))
                elif isinstance(default, str):
                    parts.append('{}="{}"'.format(pname, default))
                else:
                    parts.append('{}={}'.format(pname, default))
        return ', '.join(parts)

    def _gen_guidelines(self, init_params):
        """生成使用指南"""
        lines = []
        lines.append('- This tool is implemented using the `nb_cmd` framework. Each public instance method of the `NbCmd` subclass becomes a subcommand. You can read the `Implementation Note` to learn more details.')
        lines.append('- If you are unsure about the specific logic of a command, inspect the source code of the corresponding method in the implementation.')
        if init_params:
            lines.append('- Global parameters defined in `__init__` are automatically passed to all subcommands.')
        lines.append('- Boolean flags default to `False`; add the flag to set it to `True`.')
        lines.append('- Subcommand groups are accessed via space, e.g., `<group> <command>`.')
        lines.append('- Use `--help` or `-h` to see available commands and options.')
        lines.append('- Use `--full-help` or `-fh` to see detailed parameter descriptions.')
        return '\n'.join(lines)
    
    def _gen_impl_note(self):
        """生成实现原理说明，帮助 AI 理解源码与命令行的对应关系"""
        lines = []
        lines.append('This tool is built on the `nb_cmd` framework. Here is how the Python source code maps to CLI commands:')
        lines.append('')
        lines.append('1. **Class = Top-level command group**. The main class `{}` inherits from `NbCmd`.'.format(self.entry_cls.__name__))
        lines.append('   Each public instance method of this class becomes a top-level subcommand.')
        lines.append('')
        lines.append('2. **`sub_commands` dict = Nested command groups**. When a class defines:')
        lines.append('   ```python')
        lines.append('   sub_commands = {"db": DbCmd, "deploy": DeployCmd}')
        lines.append('   ```')
        lines.append('   the keys become the command path segments, and the values are other `NbCmd` subclasses.')
        lines.append('   So `DbCmd.backup(...)` in Python maps to `db backup` on the CLI.')
        lines.append('   Deeper nesting works the same way: if `DbCmd` itself has `sub_commands = {"ops": OpsCmd}`,')
        lines.append('   then `OpsCmd.deploy(...)` maps to `db ops deploy` on the CLI.')
        lines.append('')
        lines.append('3. **`__init__` params = Global CLI options**. Parameters of `__init__(self, ...)` become global options:')
        lines.append('   - `str` / `int` / `float` params → `--name value` (e.g., `--env prod`, `--port 8080`)')
        lines.append('   - `bool` params with default `False` → `--name` (no value, presence means `True`)')
        lines.append('   - `bool` params with default `True` → `--no-name` (no value, presence means `False`)')
        lines.append('   These options are automatically passed to all subcommands and subcommand groups.')
        lines.append('   Inside subcommands, global parameters are accessed via instance attributes or `self.nbctx`.')
        lines.append('')
        lines.append('4. **Method params = Command-level options**. Same parameter-to-flag rules as above:')
        lines.append('   - `str` / `int` / `float` → `--name value`')
        lines.append('   - `bool` default `False` → `--name`')
        lines.append('   - `bool` default `True` → `--no-name`')
        lines.append('   - **No default value** → required parameter (marked as `*(required)*` in the parameter table)')
        lines.append('   For example:')
        lines.append('   - `def backup(self, compress: bool = True)` produces `--compress` (default True, so `--no-compress` to disable)')
        lines.append('   - `def restore(self, file: str)` produces `--file` (required, no default)')
        lines.append('   - Parameter descriptions and short aliases (e.g., `--version, -v`) come from `Annotated[type, "description", "-v"]`.')
        lines.append('')
        lines.append('5. **Method docstring = Command description**. The first line of a method\'s docstring becomes the help text for that command.')
        lines.append('')
        lines.append('6. **Return values**. If a method returns a value, `nb_cmd` automatically prints it in CLI mode.')
        lines.append('')
        lines.append('7. **Python direct call vs CLI**. In Python you instantiate the class with global params:')
        lines.append('   ```python')
        lines.append('   app = {}(env="staging", region="us-west")'.format(self.entry_cls.__name__))
        lines.append('   app.db.backup(compress=False)')
        lines.append('   ```')
        lines.append('   The equivalent CLI is:')
        lines.append('   ```bash')
        lines.append('   python {} --env staging --region us-west db backup --no-compress'.format(self.script))
        lines.append('   ```')
        lines.append('')
        lines.append('If a command\'s behavior is unclear, locate the corresponding method in the source code of `{}` (or its nested `NbCmd` subclasses) and read the implementation directly.'.format(self.entry_cls.__name__))
        return '\n'.join(lines)



`````

--- **end of file: nb_cmd/core/gen_skill.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/meta.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
NbCmd Meta 配置基类。

用法::

    from nb_cmd import NbCmd, NbCmdMeta

    class MyTool(NbCmd):
        class Meta(NbCmdMeta):
            name = "my-tool"
            version = "1.0.0"
            use_nb_log = True
"""

from typing import Dict, List, Optional


class NbCmdMeta(object):
    """
    NbCmd 的 Meta 配置基类。

    子类继承后可覆盖任意字段，IDE 可自动补全所有可用选项。
    """
    name: Optional[str] = None               # CLI/API 名称（默认用类名）
    version: str = '0.0.1'                   # 版本号（--cmd-version 显示）
    description: Optional[str] = None        # 描述（默认用类的 docstring）
    use_nb_log: bool = False                 # 启用 nb_log 增强日志
    log_level: str = 'INFO'                  # 日志级别
    log_file: Optional[str] = None           # 日志文件路径
    auto_save_last_args: bool = False        # 自动保存上次参数
    config_file: Optional[str] = None        # 配置持久化文件路径
    serve_host: str = '0.0.0.0'              # Web/API 绑定地址
    serve_port: int = 8080                   # Web/API 默认端口
    serve_workers: int = 1                   # 工作进程数
    web_title: Optional[str] = None          # Web UI 页面标题
    web_theme: str = 'light'                 # Web UI 主题 ('light' / 'dark')
    enable_exec: bool = True                 # 是否暴露内置 exec 命令（False 可防止恶意执行）
    help_mode: str = 'full'                  # -h 帮助模式: 'full'(完整帮助) / 'easy'(简易帮助)
    aliases: Dict[str, List[str]] = {}       # 参数别名（推荐用 Annotated 替代）
    allow_method_list: Optional[List[str]] = None  # 命令白名单（仅限制 CLI/API/Web 暴露；Python 直接调用不受影响）
    hide_method_list: Optional[List[str]] = None   # 命令黑名单（与白名单互斥；仅限制 CLI/API/Web 暴露）
    auth_token: Optional[str] = None               # 简易鉴权 token（配置后 API/Web 请求须带 Authorization: Bearer <token>）
    timeout: int = 0                               # 命令执行超时秒数（0=不限；仅作用于 CLI/API/Web 模式）
    db_dir: Optional[str] = None                     # SQLite 数据库目录（默认 None=当前工作目录；可设为 ~/.nb_cmd 等固定路径）

`````

--- **end of file: nb_cmd/core/meta.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/parser.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
argparse 解析器自动构建模块。
根据方法签名自动生成 argparse.ArgumentParser。
"""
import argparse
import inspect

from .type_utils import (
    get_argparse_type, get_nargs, get_choices,
    is_optional, unwrap_optional, type_display_name,
)


class _RawDefaultsHelpFormatter(argparse.RawDescriptionHelpFormatter,
                                argparse.ArgumentDefaultsHelpFormatter):
    pass


def build_parser(instance, commands, meta, base_cls=None, allow_method_list=None,
                 hide_method_list=None):
    """
    为顶层 NbCmd 实例构建完整的 argparse 解析器。

    Parameters
    ----------
    instance : NbCmd 实例
    commands : dict  由 discover_commands 返回
    meta : Meta 配置类
    base_cls : type, optional  NbCmd 基类，用于子命令组 discover 过滤
    """
    if base_cls is None:
        from .base import NbCmd as _NbCmd
        base_cls = _NbCmd
    description = inspect.getdoc(instance) or instance.__class__.__name__
    version = getattr(meta, 'version', '0.0.1')

    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=_RawDefaultsHelpFormatter,
        add_help=False,
    )

    sys_group = parser.add_argument_group('system params')
    sys_group.add_argument('-h', '--help', action='help',
                           default=argparse.SUPPRESS, help='显示帮助信息（-h 行为由 Meta.help_mode 控制）')
    sys_group.add_argument('--cmd-version', action='version', version=version)
    sys_group.add_argument('-fh', '--full-help', action='store_true',
                           default=False, help='显示所有命令的完整参数详情')
    sys_group.add_argument('-eh', '--easy-help', action='store_true',
                           default=False, help='显示简易帮助（argparse 原生格式）')
    sys_group.add_argument('--web', action='store_true',
                           help='以Web UI + REST API模式启动')
    sys_group.add_argument('--web-port', type=int, default=None,
                           help='Web UI 服务端口（用于 --web）')
    sys_group.add_argument('--tui', action='store_true',
                           help='以 TUI 终端交互模式启动')

    init_group = parser.add_argument_group('init params')
    _add_init_global_options(init_group, instance)

    subparsers = parser.add_subparsers(dest='_nb_command',
                                       title='commands', help='可用命令')

    for cmd_name, cmd_info in commands.items():
        cli_name = cmd_name.replace('_', '-')

        if cmd_info.get('is_group'):
            group_cls = cmd_info['cls']
            group_doc = cmd_info.get('doc', '')
            group_kwargs = cmd_info.get('init_kwargs', {})
            sub = subparsers.add_parser(
                cli_name,
                help=group_doc + '（子命令组）' if group_doc else '子命令组',
                description=group_doc,
                formatter_class=_RawDefaultsHelpFormatter,
            )
            _build_group_subparser(sub, group_cls, base_cls, group_kwargs,
                                   allow_method_list=allow_method_list,
                                   hide_method_list=hide_method_list,
                                   command_prefix=cmd_name)
        else:
            param_hint = _build_param_hint(cmd_info)
            help_text = cmd_info['doc']
            if param_hint:
                help_text = '{} {}'.format(help_text, param_hint)
            sub = subparsers.add_parser(
                cli_name,
                help=help_text,
                description=cmd_info['full_doc'],
                formatter_class=_RawDefaultsHelpFormatter,
            )
            _add_method_arguments(sub, cmd_info, meta)

    return parser


def _build_param_hint(cmd_info):
    """为子命令生成简短的参数提示，显示在顶层 --help 的子命令描述后面"""
    sig = cmd_info['signature']
    arg_meta = cmd_info.get('arg_meta', {})
    parts = []
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        has_default = param.default is not inspect.Parameter.empty
        arg_inst = arg_meta.get(pname)
        cli_name = '--' + pname.replace('_', '-')
        if arg_inst and arg_inst.aliases:
            short = arg_inst.aliases[0]
            flag = '{}/{}'.format(short, cli_name)
        else:
            flag = cli_name
        if has_default and param.default is not False and param.default is not True:
            parts.append('{}={}'.format(flag, param.default))
        else:
            parts.append(flag)
    if not parts:
        return ''
    return '({})'.format(', '.join(parts))


def print_easy_help(instance, base_cls):
    """打印简易帮助（argparse 原生格式）"""
    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    _enable_exec = getattr(meta, 'enable_exec', True)
    _allow_methods = getattr(meta, 'allow_method_list', None)
    _hide_methods = getattr(meta, 'hide_method_list', None)
    from .discovery import discover_commands
    commands = discover_commands(instance, base_cls, enable_exec=_enable_exec,
                                 allow_method_list=_allow_methods,
                                 hide_method_list=_hide_methods)
    parser = build_parser(instance, commands, meta, base_cls=base_cls,
                          allow_method_list=_allow_methods,
                          hide_method_list=_hide_methods)
    parser.print_help()


def get_full_help_text(instance, base_cls):
    """生成完整帮助文本并返回字符串（无 ANSI 颜色码）"""
    lines = _build_full_help_lines(instance, base_cls, color=False)
    return '\n'.join(lines)


def print_full_help(instance, base_cls):
    """打印所有命令的完整参数详情到 stdout（带 ANSI 颜色码）"""
    import sys as _sys
    lines = _build_full_help_lines(instance, base_cls, color=True)
    _sys.stdout.write('\n'.join(lines))
    _sys.stdout.write('\n')
    _sys.stdout.flush()


def _build_full_help_lines(instance, base_cls, color=True):
    """构建完整帮助的所有行，返回列表"""
    from .discovery import discover_commands

    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    _enable_exec = getattr(meta, 'enable_exec', True)
    _allow_methods = getattr(meta, 'allow_method_list', None)
    _hide_methods = getattr(meta, 'hide_method_list', None)
    commands = discover_commands(instance, base_cls, enable_exec=_enable_exec,
                                 allow_method_list=_allow_methods,
                                 hide_method_list=_hide_methods)
    description = inspect.getdoc(instance) or instance.__class__.__name__
    version = getattr(meta, 'version', '0.0.1')

    sep = '=' * 56
    lines = [
        '',
        sep,
        '  {} v{}'.format(instance.__class__.__name__, version),
        '  {}'.format(description),
        sep,
        '',
        'system params:',
        '    {:<24s} {}'.format('--help, -h', '显示帮助信息'),
        '    {:<24s} {}'.format('--full-help, -fh', '显示完整帮助（所有参数详情）'),
        '    {:<24s} {}'.format('--easy-help, -eh', '显示简易帮助（argparse 原生格式）'),
        '    {:<24s} {}'.format('--cmd-version', '显示版本号'),
        '    {:<24s} {}'.format('--web', '以Web UI + REST API模式启动'),
        '    {:<24s} {}'.format('--web-port PORT', 'Web UI 服务端口（用于 --web）'),
        '    {:<24s} {}'.format('--tui', '以 TUI 终端交互模式启动'),
        '',
    ]

    if _has_init_params(instance):
        lines.append('init params:')
        lines.extend(_build_init_param_lines(instance))
        lines.append('')

    lines.append('-' * 56)
    lines.extend(_build_group_command_lines(commands, base_cls, prefix='', color=color,
                                            allow_method_list=_allow_methods,
                                            hide_method_list=_hide_methods,
                                            command_prefix=''))

    return lines


def _build_group_command_lines(commands, base_cls, prefix='', color=True,
                               allow_method_list=None, hide_method_list=None,
                               command_prefix=''):
    """递归收集命令组及其所有子命令的帮助行"""
    from .discovery import discover_commands

    lines = []
    for cmd_name, cmd_info in commands.items():
        cli_name = cmd_name.replace('_', '-')
        full_name = '{} {}'.format(prefix, cli_name).strip() if prefix else cli_name
        cmd_path = '{}/{}'.format(command_prefix, cmd_name) if command_prefix else cmd_name

        if cmd_info.get('is_group'):
            tag = '\033[36m[子命令组]\033[0m' if color else '[子命令组]'
            lines.append('{} {}  {}'.format(full_name, tag, cmd_info.get('doc', '')))
            group_cls = cmd_info['cls']
            group_kwargs = cmd_info.get('init_kwargs', {})
            try:
                group_inst = group_cls(**group_kwargs) if group_kwargs else group_cls()
            except TypeError:
                group_inst = group_cls.__new__(group_cls)
            group_cmds = discover_commands(group_inst, base_cls,
                                           include_builtins=False,
                                           allow_method_list=allow_method_list,
                                           hide_method_list=hide_method_list,
                                           command_prefix=cmd_path)
            lines.extend(_build_group_command_lines(group_cmds, base_cls,
                                                    prefix=full_name, color=color,
                                                    allow_method_list=allow_method_list,
                                                    hide_method_list=hide_method_list,
                                                    command_prefix=cmd_path))
            lines.append('')
        else:
            if prefix:
                lines.append('')
                lines.append('  {} — {}'.format(full_name, cmd_info.get('doc', '')))
            else:
                lines.append('{} — {}'.format(full_name, cmd_info.get('doc', '')))
            lines.extend(_build_param_lines(cmd_info))
            if not prefix:
                lines.append('')

    return lines


def _build_param_lines(cmd_info):
    """构建一个命令的完整参数列表行"""
    sig = cmd_info['signature']
    hints = cmd_info.get('type_hints', {})
    arg_meta = cmd_info.get('arg_meta', {})
    lines = []

    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        ptype = hints.get(pname, str)
        real_type = unwrap_optional(ptype) if is_optional(ptype) else ptype
        type_name = type_display_name(real_type)
        has_default = param.default is not inspect.Parameter.empty
        arg_inst = arg_meta.get(pname)
        desc = arg_inst.desc if arg_inst and arg_inst.desc else ''

        cli_flag = '--' + pname.replace('_', '-')
        if arg_inst and arg_inst.aliases:
            flags_str = '{}, {}'.format(cli_flag, ', '.join(arg_inst.aliases))
        else:
            flags_str = cli_flag

        if has_default:
            meta_str = '({}, 默认: {})'.format(type_name, param.default)
        else:
            meta_str = '({}, 必填)'.format(type_name)

        if desc:
            lines.append('    {:<24s} {}  {}'.format(flags_str, desc, meta_str))
        else:
            lines.append('    {:<24s} {}'.format(flags_str, meta_str))

    return lines


def _has_init_params(instance):
    """判断实例的 __init__ 是否有自定义全局参数"""
    init_method = instance.__class__.__init__
    if init_method is object.__init__:
        return False
    sig = inspect.signature(init_method)
    for pname, param in sig.parameters.items():
        if pname != 'self':
            return True
    return False


def _build_init_param_lines(instance):
    """构建 __init__ 全局选项的详情行"""
    from .arg import unwrap_arg

    init_method = instance.__class__.__init__
    if init_method is object.__init__:
        return []

    sig = inspect.signature(init_method)
    lines = []

    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue

        has_default = param.default is not inspect.Parameter.empty
        if has_default:
            default_val = param.default
        else:
            default_val = getattr(instance, pname, None)

        raw_hint = param.annotation
        if raw_hint is inspect.Parameter.empty:
            if default_val is not None:
                raw_hint = type(default_val)
            else:
                raw_hint = str

        real_type, arg_inst = unwrap_arg(raw_hint)
        type_name = type_display_name(real_type)
        desc = arg_inst.desc if arg_inst and arg_inst.desc else ''

        cli_flag = '--' + pname.replace('_', '-')
        if arg_inst and arg_inst.aliases:
            flags_str = '{}, {}'.format(cli_flag, ', '.join(arg_inst.aliases))
        else:
            flags_str = cli_flag

        meta_str = '(全局, {}, 默认: {})'.format(type_name, default_val)

        if desc:
            lines.append('    {:<24s} {}  {}'.format(flags_str, desc, meta_str))
        else:
            lines.append('    {:<24s} {}'.format(flags_str, meta_str))

    return lines


def _add_init_global_options(parser, instance):
    """将 __init__ 中的自定义参数变为全局选项，支持 Annotated 描述"""
    from .arg import unwrap_arg

    init_method = instance.__class__.__init__
    if init_method is object.__init__:
        return

    sig = inspect.signature(init_method)

    for param_name, param in sig.parameters.items():
        if param_name == 'self':
            continue

        has_default = param.default is not inspect.Parameter.empty
        if has_default:
            default_val = param.default
        else:
            default_val = getattr(instance, param_name, None)

        raw_hint = param.annotation
        if raw_hint is inspect.Parameter.empty:
            if default_val is not None:
                raw_hint = type(default_val)
            else:
                raw_hint = str

        param_type, arg_inst = unwrap_arg(raw_hint)

        cli_flag = '--' + param_name.replace('_', '-')
        extra_flags = arg_inst.aliases if arg_inst and arg_inst.aliases else []
        desc = arg_inst.desc if arg_inst and arg_inst.desc else None

        metavar = param_name.upper()
        if param_type is bool:
            flags = [cli_flag] + extra_flags
            auto_help = '(全局选项, bool, 默认: {})'.format(default_val)
            parser.add_argument(
                *flags,
                action='store_true' if not default_val else 'store_false',
                default=default_val,
                dest='_nb_init_' + param_name,
                help='{} {}'.format(desc, auto_help) if desc else auto_help,
            )
        else:
            flags = [cli_flag] + extra_flags
            auto_help = '(全局选项, {}, 默认: {})'.format(
                type_display_name(param_type), default_val)
            parser.add_argument(
                *flags,
                type=get_argparse_type(param_type),
                default=default_val,
                dest='_nb_init_' + param_name,
                metavar=metavar,
                help='{} {}'.format(desc, auto_help) if desc else auto_help,
            )


def _add_method_arguments(sub_parser, cmd_info, meta):
    """根据方法签名向 subparser 添加参数。

    必填参数采用"双模式"：同时注册位置参数（nargs='?'）和 --flag，
    用户可以 ``fa 5`` 也可以 ``fa --x 5``，两种写法等价。
    """
    sig = cmd_info['signature']
    hints = cmd_info.get('type_hints', {})
    arg_meta = cmd_info.get('arg_meta', {})
    method_name = cmd_info['method'].__name__

    aliases_map = getattr(meta, 'aliases', {})

    pos_index = 0
    positional_map = []

    for param_name, param in sig.parameters.items():
        if param_name == 'self':
            continue

        param_type = hints.get(param_name, str)
        if is_optional(param_type):
            param_type_unwrapped = unwrap_optional(param_type)
        else:
            param_type_unwrapped = param_type

        has_default = param.default is not inspect.Parameter.empty
        is_keyword_only = param.kind == inspect.Parameter.KEYWORD_ONLY

        arg_inst = arg_meta.get(param_name)
        if arg_inst and arg_inst.aliases:
            extra_flags = list(arg_inst.aliases)
        else:
            alias_key = '{}.{}'.format(method_name, param_name)
            extra_flags = aliases_map.get(alias_key, [])

        desc = arg_inst.desc if arg_inst and arg_inst.desc else None

        cli_flag = '--' + param_name.replace('_', '-')
        nargs = get_nargs(param_type)
        choices = get_choices(param_type)
        ap_type = get_argparse_type(param_type)
        type_name = type_display_name(param_type_unwrapped)

        if param_type_unwrapped is bool:
            flags = [cli_flag] + extra_flags
            auto_help = '(bool, 默认: {})'.format(param.default if has_default else False)
            sub_parser.add_argument(
                *flags,
                action='store_true' if not (has_default and param.default) else 'store_false',
                default=param.default if has_default else False,
                dest=param_name,
                help='{} {}'.format(desc, auto_help) if desc else auto_help,
            )
        elif has_default or is_keyword_only:
            flags = [cli_flag] + extra_flags
            auto_help = '({}, 默认: {})'.format(type_name, param.default if has_default else 'None')
            kwargs = dict(
                type=ap_type,
                default=param.default if has_default else None,
                dest=param_name,
                help='{} {}'.format(desc, auto_help) if desc else auto_help,
            )
            if nargs is not None:
                kwargs['nargs'] = nargs
            if choices is not None:
                kwargs['choices'] = choices
            sub_parser.add_argument(*flags, **kwargs)
        else:
            auto_help = '({}, 必填)'.format(type_name)
            help_text = '{} {}'.format(desc, auto_help) if desc else auto_help

            use_dual = (nargs is None)

            if use_dual:
                pos_dest = '_nb_pos_{}'.format(pos_index)
                pos_index += 1
                positional_map.append((pos_dest, param_name, ap_type))

                sub_parser.add_argument(
                    pos_dest, nargs='?', default=None, type=str,
                    help=argparse.SUPPRESS,
                )

                flags = [cli_flag] + extra_flags
                flag_kwargs = dict(
                    type=ap_type,
                    default=None,
                    dest=param_name,
                    help=help_text,
                )
                if choices is not None:
                    flag_kwargs['choices'] = choices
                sub_parser.add_argument(*flags, **flag_kwargs)
            else:
                if extra_flags:
                    flags = [cli_flag] + extra_flags
                    kwargs = dict(
                        type=ap_type,
                        required=True,
                        dest=param_name,
                        help=help_text,
                    )
                    if nargs is not None:
                        kwargs['nargs'] = nargs
                    if choices is not None:
                        kwargs['choices'] = choices
                    sub_parser.add_argument(*flags, **kwargs)
                else:
                    kwargs = dict(
                        type=ap_type,
                        help=help_text,
                        metavar=param_name.upper(),
                    )
                    if nargs is not None:
                        kwargs['nargs'] = nargs
                    if choices is not None:
                        kwargs['choices'] = choices
                    sub_parser.add_argument(param_name, **kwargs)

    if positional_map:
        sub_parser.set_defaults(_nb_pos_map=positional_map)


def reassign_positionals(parsed):
    """后处理：将位置参数值与 --flag 值智能合并。

    规则：--flag 优先；被 flag "顶掉" 的位置值向后挪给其他未填参数。
    位置参数统一以 str 类型接收，此处完成目标类型的转换。
    """
    pos_map = getattr(parsed, '_nb_pos_map', None)
    if not pos_map:
        return

    free_values = []
    for pos_dest, param_name, ap_type in pos_map:
        flag_val = getattr(parsed, param_name, None)
        pos_val = getattr(parsed, pos_dest, None)
        if flag_val is not None and pos_val is not None:
            free_values.append((pos_val, ap_type))
        elif flag_val is None and pos_val is not None:
            setattr(parsed, param_name, _safe_convert(pos_val, ap_type))

    for _, param_name, ap_type in pos_map:
        if getattr(parsed, param_name, None) is None and free_values:
            val, orig_type = free_values.pop(0)
            setattr(parsed, param_name, _safe_convert(val, ap_type))

    for pos_dest, _, _ in pos_map:
        try:
            delattr(parsed, pos_dest)
        except AttributeError:
            pass

    missing = [pn for _, pn, _ in pos_map if getattr(parsed, pn, None) is None]
    if missing:
        import sys
        flags = ', '.join('--' + m.replace('_', '-') for m in missing)
        sys.stderr.write('error: 缺少必填参数: {}\n'.format(flags))
        raise SystemExit(2)


def _safe_convert(value, ap_type):
    """将字符串值转换为目标类型，转换失败时原样返回"""
    if ap_type is None or ap_type is str:
        return value
    try:
        return ap_type(value)
    except (ValueError, TypeError):
        return value


def _build_group_subparser(parent_parser, group_cls, base_cls, init_kwargs=None, depth=1,
                           allow_method_list=None, hide_method_list=None, command_prefix=''):
    """递归为子命令组构建 subparser"""
    from .discovery import discover_commands

    if init_kwargs:
        group_instance = group_cls(**init_kwargs)
    else:
        group_instance = group_cls.__new__(group_cls)
        if hasattr(group_cls.__init__, '__func__') and group_cls.__init__ is not object.__init__:
            try:
                group_cls.__init__(group_instance)
            except TypeError:
                pass

    group_commands = discover_commands(group_instance, base_cls, include_builtins=False,
                                       allow_method_list=allow_method_list,
                                       hide_method_list=hide_method_list,
                                       command_prefix=command_prefix)

    if not group_commands:
        return

    sub_group_meta = getattr(group_cls, 'Meta', type('Meta', (), {}))

    dest = '_nb_sub_command' if depth == 1 else '_nb_sub_command_{}'.format(depth)
    group_subparsers = parent_parser.add_subparsers(dest=dest, help='可用子命令')

    for cmd_name, cmd_info in group_commands.items():
        cli_name = cmd_name.replace('_', '-')

        if cmd_info.get('is_group'):
            nested_cls = cmd_info['cls']
            nested_doc = cmd_info.get('doc', '')
            nested_kwargs = cmd_info.get('init_kwargs', {})
            nested_sub = group_subparsers.add_parser(
                cli_name,
                help=nested_doc + '（子命令组）' if nested_doc else '子命令组',
                description=nested_doc,
                formatter_class=_RawDefaultsHelpFormatter,
            )
            _build_group_subparser(nested_sub, nested_cls, base_cls, nested_kwargs, depth + 1,
                                   allow_method_list=allow_method_list,
                                   hide_method_list=hide_method_list,
                                   command_prefix='{}/{}'.format(command_prefix, cmd_name)
                                   if command_prefix else cmd_name)
        else:
            sub = group_subparsers.add_parser(
                cli_name,
                help=cmd_info['doc'],
                description=cmd_info['full_doc'],
                formatter_class=_RawDefaultsHelpFormatter,
            )
            _add_method_arguments(sub, cmd_info, sub_group_meta)

`````

--- **end of file: nb_cmd/core/parser.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/result_handler.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
返回值自动处理模块。
根据返回值类型决定如何在 CLI / API 中展示结果。
"""
import json
from pathlib import Path

from ..ui.table import _display_width as _cjk_display_width


def handle_cli_result(result):
    """
    CLI 模式下自动处理方法返回值。

    规则:
    - None          → 不输出
    - str           → 直接 print
    - int / float   → 直接 print
    - dict          → JSON 格式化输出
    - list[dict]    → 表格输出（降级为 JSON）
    - list          → 每行一个
    - Path          → 输出路径字符串
    """
    if result is None:
        return

    if isinstance(result, str):
        print(result)
        return

    if isinstance(result, (int, float)):
        print(result)
        return

    if isinstance(result, dict):
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if isinstance(result, (list, tuple)):
        if result and isinstance(result[0], dict):
            _print_list_of_dicts_as_table(result)
        else:
            for item in result:
                print(item)
        return

    if isinstance(result, Path):
        print(str(result))
        return

    print(result)


def handle_api_result(result):
    """API 模式下处理返回值"""
    if result is None:
        return None

    if isinstance(result, (str, int, float)):
        return {"result": result}

    if isinstance(result, dict):
        return result

    if isinstance(result, (list, tuple)):
        return {"result": result}

    if isinstance(result, Path):
        return {"result": str(result)}

    return {"result": str(result)}


def _print_list_of_dicts_as_table(data):
    """简易表格输出 list[dict]，无外部依赖"""
    if not data:
        return

    headers = list(data[0].keys())
    col_widths = {}
    for h in headers:
        col_widths[h] = len(str(h))
    for row in data:
        for h in headers:
            val = str(row.get(h, ''))
            if len(val) > col_widths[h]:
                col_widths[h] = len(val)

    for h in headers:
        col_widths[h] = max(col_widths[h], _cjk_display_width(str(h)))
    for row in data:
        for h in headers:
            w = _cjk_display_width(str(row.get(h, '')))
            if w > col_widths[h]:
                col_widths[h] = w

    def _pad(text, width):
        dw = _cjk_display_width(text)
        return text + ' ' * (width - dw)

    sep_line = '+' + '+'.join('-' * (col_widths[h] + 2) for h in headers) + '+'
    header_line = '| ' + ' | '.join(_pad(str(h), col_widths[h]) for h in headers) + ' |'

    print(sep_line)
    print(header_line)
    print(sep_line)
    for row in data:
        vals = [_pad(str(row.get(h, '')), col_widths[h]) for h in headers]
        print('| ' + ' | '.join(vals) + ' |')
    print(sep_line)



`````

--- **end of file: nb_cmd/core/result_handler.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/type_utils.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
Python类型 → argparse类型/nargs/choices 的映射工具。
兼容 Python 3.7+。
"""
import enum
from pathlib import Path


def _get_origin(tp):
    """兼容 3.7 的 typing.get_origin"""
    return getattr(tp, '__origin__', None)


def _get_args(tp):
    """兼容 3.7 的 typing.get_args"""
    return getattr(tp, '__args__', ())


def is_optional(tp):
    """判断是否是 Optional[X] (即 Union[X, None])"""
    origin = _get_origin(tp)
    if origin is not None:
        import typing
        if origin is getattr(typing, 'Union', None):
            args = _get_args(tp)
            return type(None) in args
    return False


def unwrap_optional(tp):
    """Optional[X] → X"""
    if is_optional(tp):
        args = _get_args(tp)
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1:
            return non_none[0]
    return tp


def is_enum_type(tp):
    return isinstance(tp, type) and issubclass(tp, enum.Enum)


def is_list_type(tp):
    origin = _get_origin(tp)
    return origin is list


def is_tuple_type(tp):
    origin = _get_origin(tp)
    return origin is tuple


def get_argparse_type(python_type):
    """Python类型 → argparse type 参数"""
    real_type = unwrap_optional(python_type)

    if real_type is bool:
        return None
    if real_type in (int, float, str):
        return real_type
    if real_type is Path:
        return str
    if is_enum_type(real_type):
        return str
    if is_list_type(real_type):
        args = _get_args(real_type)
        if args:
            inner = args[0]
            if inner in (int, float, str):
                return inner
        return str
    if is_tuple_type(real_type):
        return str
    return str


def get_nargs(python_type):
    """Python类型 → argparse nargs"""
    real_type = unwrap_optional(python_type)
    if is_list_type(real_type):
        return '+'
    if is_tuple_type(real_type):
        args = _get_args(real_type)
        if args:
            return len(args)
    return None


def get_choices(python_type):
    """Python类型 → argparse choices"""
    real_type = unwrap_optional(python_type)
    if is_enum_type(real_type):
        return [e.value for e in real_type]
    return None


def convert_value(value, python_type):
    """将 argparse 解析出的字符串值转为目标 Python 类型"""
    real_type = unwrap_optional(python_type)

    if value is None:
        return None

    if real_type is bool:
        return value

    if real_type in (int, float, str):
        return real_type(value)

    if real_type is Path:
        return Path(value)

    if is_enum_type(real_type):
        for member in real_type:
            if member.value == value:
                return member
        return real_type(value)

    if is_list_type(real_type):
        args = _get_args(real_type)
        inner = args[0] if args else str
        if isinstance(value, (list, tuple)):
            return [inner(v) for v in value]
        return [inner(value)]

    if is_tuple_type(real_type):
        args = _get_args(real_type)
        if isinstance(value, (list, tuple)) and args:
            return tuple(args[i](value[i]) for i in range(min(len(args), len(value))))
        return value

    return value


def type_display_name(python_type):
    """获取类型的可读显示名"""
    if hasattr(python_type, '__name__'):
        return python_type.__name__
    return str(python_type).replace('typing.', '')

`````

--- **end of file: nb_cmd/core/type_utils.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/_io_dispatch.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
线程安全的 stdout/stderr 分发器。

web_mode 和 api_mode 共用同一个 threading.local() + 分发器，
避免并发请求之间 stdout 串流。

用法:
    注册输出目标:
        _tls.output_queue = some_queue        # WebSocket 推送（队列模式）
        _tls.captured_stdout = StringIO()     # API 捕获（StringIO 模式）
        _tls.captured_stderr = StringIO()

    注销:
        _tls.output_queue = None
        _tls.captured_stdout = None
        _tls.captured_stderr = None

    没有注册时, 写到原始 sys.stdout / sys.stderr。
"""
import sys
import threading

_tls = threading.local()
_original_stdout = sys.stdout
_original_stderr = sys.stderr


class _DispatchWriter(object):
    """
    线程安全的 stdout/stderr 替代品。
    按优先级检查当前线程的输出目标:
      1. _tls.output_queue     → put((stream_type, data))     (WebSocket)
      2. _tls.captured_stdout  → write(data)                  (API StringIO)
      3. 原始流                → write(data)                  (服务器控制台)
    """
    def __init__(self, original, stream_type):
        self._orig = original
        self._type = stream_type
        self._cap_attr = 'captured_stdout' if stream_type == 'stdout' else 'captured_stderr'
        self.encoding = getattr(original, 'encoding', 'utf-8')

    def write(self, data):
        if not data:
            return
        q = getattr(_tls, 'output_queue', None)
        if q is not None:
            q.put((self._type, data))
            return
        cap = getattr(_tls, self._cap_attr, None)
        if cap is not None:
            cap.write(data)
            return
        self._orig.write(data)

    def flush(self):
        self._orig.flush()

    def isatty(self):
        return True

    def fileno(self):
        return self._orig.fileno()

    def __getattr__(self, name):
        return getattr(self._orig, name)


def install():
    """安装分发器（幂等，多次调用安全）"""
    if not isinstance(sys.stdout, _DispatchWriter):
        sys.stdout = _DispatchWriter(_original_stdout, 'stdout')
        sys.stderr = _DispatchWriter(_original_stderr, 'stderr')

`````

--- **end of file: nb_cmd/core/_io_dispatch.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/core/__init__.py** (project: nb_cmd) --- 

`````python

`````

--- **end of file: nb_cmd/core/__init__.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/modes/api_mode.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
REST API 模式 —— 自动将 NbCmd 类的方法生成 FastAPI 路由。
需要安装: pip install fastapi uvicorn
"""
import asyncio
import functools
import inspect
import io
import time

from ..core.discovery import discover_commands
from ..core.result_handler import handle_api_result


async def _run_in_thread(func, *args):
    """asyncio.to_thread 的 Python 3.7+ 兼容版"""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, functools.partial(func, *args))


def start_api_server(instance, base_cls, host=None, port=None):
    """
    启动 REST API 服务。

    Parameters
    ----------
    instance : NbCmd 实例
    base_cls : NbCmd 类
    host : str
    port : int
    """
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        import uvicorn
    except ImportError:
        print("REST API模式需要安装 fastapi 和 uvicorn:")
        print("  pip install fastapi uvicorn")
        return

    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    title = getattr(meta, 'name', None) or instance.__class__.__name__
    description = inspect.getdoc(instance) or ''
    version = getattr(meta, 'version', None) or '0.0.1'

    if host is None:
        host = getattr(meta, 'serve_host', '0.0.0.0')
    if port is None:
        port = getattr(meta, 'serve_port', 8080)

    app = FastAPI(title=title, description=description, version=version)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _enable_exec = getattr(meta, 'enable_exec', True)
    _allow_methods = getattr(meta, 'allow_method_list', None)
    _hide_methods = getattr(meta, 'hide_method_list', None)
    _auth_token = getattr(meta, 'auth_token', None)
    _timeout = getattr(meta, 'timeout', 0)
    commands = discover_commands(instance, base_cls, enable_exec=_enable_exec,
                                 allow_method_list=_allow_methods,
                                 hide_method_list=_hide_methods)

    if _auth_token:
        _install_auth_middleware(app, _auth_token)

    _register_routes(app, instance, commands, base_cls=base_cls,
                     allow_method_list=_allow_methods, hide_method_list=_hide_methods,
                     command_prefix='', timeout=_timeout)

    from fastapi.responses import RedirectResponse

    @app.get('/', include_in_schema=False)
    async def root():
        """根路径自动跳转到 Swagger 文档"""
        return RedirectResponse(url='/docs')

    @app.get('/help', summary='所有命令帮助')
    async def help_all():
        result = {}
        for name, info in commands.items():
            if info.get('is_group'):
                result[name] = {'type': 'group', 'description': info.get('doc', '')}
            else:
                params = {}
                for pname, param in info['signature'].parameters.items():
                    if pname == 'self':
                        continue
                    ptype = info['type_hints'].get(pname, str)
                    has_default = param.default is not inspect.Parameter.empty
                    params[pname] = {
                        'type': str(ptype),
                        'required': not has_default,
                        'default': _safe_default(param.default) if has_default else None,
                    }
                result[name] = {
                    'type': 'command',
                    'description': info.get('doc', ''),
                    'parameters': params,
                }
        return result

    print('API服务启动在 http://{}:{}'.format(host, port))
    print('Swagger文档: http://{}:{}/docs'.format(host, port))
    uvicorn.run(app, host=host, port=port)


def _safe_default(value):
    """将默认值转为 JSON 可序列化的形式"""
    import enum
    from pathlib import Path
    if value is inspect.Parameter.empty:
        return None
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (str, int, float, bool, type(None))):
        return value
    if isinstance(value, (list, tuple, dict)):
        return value
    return str(value)


def _register_routes(app, instance, commands, base_cls=None, prefix='',
                     allow_method_list=None, hide_method_list=None,
                     command_prefix='', timeout=0):
    """为每个命令注册 POST 路由，支持递归注册子命令组"""
    for cmd_name, cmd_info in commands.items():
        if cmd_info.get('is_group'):
            if base_cls is not None:
                group_cls = cmd_info['cls']
                group_kwargs = cmd_info.get('init_kwargs', {})
                group_path = '{}/{}'.format(command_prefix, cmd_name) if command_prefix else cmd_name
                try:
                    group_instance = group_cls(**group_kwargs) if group_kwargs else group_cls()
                except TypeError:
                    group_instance = group_cls.__new__(group_cls)
                parent_ctx = instance.nbctx if hasattr(instance, 'nbctx') else None
                if parent_ctx is not None:
                    group_instance.nbctx = parent_ctx
                group_commands = discover_commands(group_instance, base_cls,
                                                   include_builtins=False,
                                                   allow_method_list=allow_method_list,
                                                   hide_method_list=hide_method_list,
                                                   command_prefix=group_path)
                group_prefix = '{}/{}'.format(prefix, cmd_name) if prefix else cmd_name
                _register_routes(app, group_instance, group_commands,
                                 base_cls=base_cls, prefix=group_prefix,
                                 allow_method_list=allow_method_list,
                                 hide_method_list=hide_method_list,
                                 command_prefix=group_path, timeout=timeout)
            continue

        sig = cmd_info['signature']
        hints = cmd_info.get('type_hints', {})
        cli_name = cmd_name.replace('_', '-')
        if prefix:
            route_path = '{}/{}'.format(prefix.replace('_', '-'), cli_name)
        else:
            route_path = cli_name
        doc = cmd_info.get('doc', '')

        try:
            from pydantic import create_model as _create_model

            fields = {}
            for param_name, param in sig.parameters.items():
                if param_name == 'self':
                    continue
                param_type = hints.get(param_name, str)

                import enum
                from pathlib import Path
                from ..core.type_utils import unwrap_optional, is_enum_type, is_list_type, is_tuple_type

                real_type = unwrap_optional(param_type)
                if is_enum_type(real_type):
                    real_type = str
                if real_type is Path:
                    real_type = str
                if is_list_type(real_type):
                    real_type = list
                if is_tuple_type(real_type):
                    real_type = list

                has_default = param.default is not inspect.Parameter.empty
                if has_default:
                    default_val = param.default
                    if isinstance(default_val, enum.Enum):
                        default_val = default_val.value
                    if isinstance(default_val, Path):
                        default_val = str(default_val)
                    fields[param_name] = (real_type, default_val)
                else:
                    fields[param_name] = (real_type, ...)

            if _get_init_kwargs(instance):
                from typing import Optional as _Optional
                fields['init_params'] = (_Optional[dict], None)

            model_name = '{}_{}_request'.format(prefix, cmd_name) if prefix else '{}_request'.format(cmd_name)
            RequestModel = _create_model(model_name, **fields)
        except Exception:
            RequestModel = None

        _make_route(app, route_path, doc, cmd_name, instance, RequestModel, hints, timeout=timeout)


def _get_init_kwargs(instance):
    """从实例上提取 __init__ 参数的当前值，用于重新实例化"""
    cls = instance.__class__
    init_method = cls.__init__
    if init_method is object.__init__:
        return {}
    sig = inspect.signature(init_method)
    kwargs = {}
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        if hasattr(instance, pname):
            kwargs[pname] = getattr(instance, pname)
    return kwargs


def _get_init_types(instance):
    """获取 __init__ 参数名到真实类型的映射，用于 REST API 中 _init_params 的类型转换"""
    from ..core.arg import unwrap_arg
    cls = instance.__class__
    init_method = cls.__init__
    if init_method is object.__init__:
        return {}
    sig = inspect.signature(init_method)
    types = {}
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        raw_hint = param.annotation
        if raw_hint is inspect.Parameter.empty:
            val = getattr(instance, pname, None)
            types[pname] = type(val) if val is not None else str
        else:
            real_type, _ = unwrap_arg(raw_hint)
            types[pname] = real_type
    return types


def _make_route(app, path, summary, cmd_name, instance, request_model, type_hints, timeout=0):
    """创建单个 API 路由，每次请求新建实例执行命令，支持 init_params 覆盖全局参数"""
    _cmd_name = cmd_name
    _cls = instance.__class__
    _init_kwargs = _get_init_kwargs(instance)
    _init_types = _get_init_types(instance)
    _hints = type_hints
    _path = path
    _timeout = timeout

    def _fresh(raw_init_params=None):
        if not raw_init_params or not _init_types:
            inst = _cls(**_init_kwargs) if _init_kwargs else _cls()
        else:
            from ..core.type_utils import convert_value
            merged = dict(_init_kwargs)
            for pname, val in raw_init_params.items():
                if pname in _init_types:
                    merged[pname] = convert_value(val, _init_types[pname])
            inst = _cls(**merged) if merged else _cls()
        ctx = inst.make_nbctx()
        if ctx is not None:
            inst.nbctx = ctx
        return inst

    def _convert_kwargs(kwargs):
        from ..core.type_utils import convert_value
        converted = {}
        for k, v in kwargs.items():
            if k in _hints:
                converted[k] = convert_value(v, _hints[k])
            else:
                converted[k] = v
        return converted

    from ..core._io_dispatch import _tls as _api_tls, install as _install_io
    _install_io()

    def _exec_in_thread(fresh_inst, kwargs):
        import asyncio as _aio
        captured_out = io.StringIO()
        captured_err = io.StringIO()
        _api_tls.captured_stdout = captured_out
        _api_tls.captured_stderr = captured_err
        try:
            method = getattr(fresh_inst, _cmd_name)
            result = method(**_convert_kwargs(kwargs))
            if inspect.iscoroutine(result):
                result = _aio.run(result)
        finally:
            _api_tls.captured_stdout = None
            _api_tls.captured_stderr = None
        return result, captured_out.getvalue(), captured_err.getvalue()

    async def _exec_with_timeout(fresh_inst, kwargs):
        coro = _run_in_thread(_exec_in_thread, fresh_inst, kwargs)
        if _timeout > 0:
            return await asyncio.wait_for(coro, timeout=_timeout)
        return await coro

    if request_model is not None:
        @app.post('/{}'.format(path), summary=summary)
        async def endpoint(request: request_model):
            start = time.time()
            kwargs = request.dict() if hasattr(request, 'dict') else request.model_dump()
            raw_init = kwargs.pop('init_params', None)
            fresh_inst = _fresh(raw_init)
            fresh_inst.before_run()
            try:
                result, stdout_output, stderr_output = await _exec_with_timeout(
                    fresh_inst, kwargs)
                api_result = handle_api_result(result)
                duration_ms = int((time.time() - start) * 1000)
                return {
                    "status": "success",
                    "result": api_result,
                    "stdout": stdout_output if stdout_output else None,
                    "stderr": stderr_output if stderr_output else None,
                    "duration_ms": duration_ms,
                }
            except asyncio.TimeoutError:
                duration_ms = int((time.time() - start) * 1000)
                return {
                    "status": "error",
                    "error": "命令执行超时（{} 秒）".format(_timeout),
                    "duration_ms": duration_ms,
                }
            except Exception as e:
                fresh_inst.on_error(_path, e)
                return {
                    "status": "error",
                    "error": str(e),
                    "duration_ms": int((time.time() - start) * 1000),
                }
            finally:
                fresh_inst.after_run()
    else:
        @app.post('/{}'.format(path), summary=summary)
        async def endpoint(request: dict = {}):
            start = time.time()
            raw_init = request.pop('init_params', None)
            fresh_inst = _fresh(raw_init)
            fresh_inst.before_run()
            try:
                result, stdout_output, stderr_output = await _exec_with_timeout(
                    fresh_inst, request)
                api_result = handle_api_result(result)
                duration_ms = int((time.time() - start) * 1000)
                return {
                    "status": "success",
                    "result": api_result,
                    "stdout": stdout_output if stdout_output else None,
                    "stderr": stderr_output if stderr_output else None,
                    "duration_ms": duration_ms,
                }
            except asyncio.TimeoutError:
                duration_ms = int((time.time() - start) * 1000)
                return {
                    "status": "error",
                    "error": "命令执行超时（{} 秒）".format(_timeout),
                    "duration_ms": duration_ms,
                }
            except Exception as e:
                fresh_inst.on_error(_path, e)
                return {
                    "status": "error",
                    "error": str(e),
                    "duration_ms": int((time.time() - start) * 1000),
                }
            finally:
                fresh_inst.after_run()


def _install_auth_middleware(app, token, exempt_prefixes=None):
    """
    安装 Bearer token 认证中间件。

    Parameters
    ----------
    exempt_prefixes : list[str], optional
        额外的免认证路径前缀列表。
        默认已豁免 /docs /redoc /openapi.json。
        Web 模式会传入 /api/ /ws/ 等前缀，使页面可以正常访问。
    """
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.responses import JSONResponse

    _always_exempt = ('/', '/docs', '/redoc', '/openapi.json')
    _extra_prefixes = tuple(exempt_prefixes) if exempt_prefixes else ()

    class _AuthMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            path = request.url.path
            if path in _always_exempt:
                return await call_next(request)
            for prefix in _extra_prefixes:
                if path.startswith(prefix):
                    return await call_next(request)
            auth_header = request.headers.get('authorization', '')
            if not auth_header.startswith('Bearer '):
                return JSONResponse({'detail': 'Missing or invalid Authorization header'},
                                    status_code=401)
            if auth_header[7:] != token:
                return JSONResponse({'detail': 'Invalid token'}, status_code=403)
            return await call_next(request)

    app.add_middleware(_AuthMiddleware)

`````

--- **end of file: nb_cmd/modes/api_mode.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/modes/cli_mode.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
CLI 模式 —— 默认的命令行交互模式。
"""
import asyncio
import inspect

from ..core.discovery import discover_commands
from ..core.parser import build_parser, reassign_positionals
from ..core.type_utils import convert_value
from ..core.result_handler import handle_cli_result


def _run_method(method, kwargs):
    """执行方法，自动处理同步和异步函数"""
    result = method(**kwargs)
    if inspect.iscoroutine(result):
        result = asyncio.run(result)
    return result


def _run_method_with_timeout(method, kwargs, timeout):
    """执行方法并在超时后抛出 TimeoutError（timeout=0 表示不限）"""
    if timeout <= 0:
        return _run_method(method, kwargs)

    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_run_method, method, kwargs)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            raise TimeoutError(
                '命令执行超时（{} 秒）。可通过 Meta.timeout 调整超时时间。'.format(timeout)
            )


def run_cli(instance, base_cls, args=None):
    """
    以 CLI 模式执行 NbCmd 实例。

    Parameters
    ----------
    instance : NbCmd 实例
    base_cls : NbCmd 类（用于过滤基类方法）
    args : list, optional  命令行参数列表，默认 sys.argv[1:]
    """
    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    _enable_exec = getattr(meta, 'enable_exec', True)
    _allow_methods = getattr(meta, 'allow_method_list', None)
    _hide_methods = getattr(meta, 'hide_method_list', None)
    _timeout = getattr(meta, 'timeout', 0)
    commands = discover_commands(instance, base_cls, enable_exec=_enable_exec,
                                 allow_method_list=_allow_methods,
                                 hide_method_list=_hide_methods)
    parser = build_parser(instance, commands, meta, base_cls=base_cls,
                          allow_method_list=_allow_methods,
                          hide_method_list=_hide_methods)

    parsed = parser.parse_args(args)
    reassign_positionals(parsed)

    _apply_init_args(instance, parsed)
    _ensure_nbctx(instance)

    command_name = getattr(parsed, '_nb_command', None)
    if not command_name:
        parser.print_help()
        return

    python_name = command_name.replace('-', '_')

    if python_name in commands and commands[python_name].get('is_group'):
        _run_group_command(instance, commands[python_name], parsed, base_cls, depth=1,
                           allow_method_list=_allow_methods, hide_method_list=_hide_methods,
                           command_prefix=python_name)
        return

    if python_name not in commands:
        parser.print_help()
        return

    cmd_info = commands[python_name]
    method = cmd_info['method']
    kwargs = _extract_kwargs(method, cmd_info, parsed)

    instance.before_run()
    try:
        result = _run_method_with_timeout(method, kwargs, _timeout)
        handle_cli_result(result)
    except Exception as e:
        instance.on_error(command_name, e)
        raise
    finally:
        instance.after_run()


def _apply_init_args(instance, parsed):
    """
    将解析出的全局选项（__init__参数）应用到实例上。

    通过重新调用 __init__（带 CLI 解析值）来更新实例状态，
    这样用户在 __init__ 中直接赋值 self.nbctx = XxxCtx(...) 也能拿到正确的 CLI 值。
    """
    init_method = instance.__class__.__init__
    if init_method is object.__init__:
        return

    sig = inspect.signature(init_method)
    kwargs = {}
    for param_name in sig.parameters:
        if param_name == 'self':
            continue
        attr_name = '_nb_init_' + param_name
        if hasattr(parsed, attr_name):
            cli_val = getattr(parsed, attr_name)
            if cli_val is not None:
                kwargs[param_name] = cli_val
            elif hasattr(instance, param_name):
                kwargs[param_name] = getattr(instance, param_name)
        elif hasattr(instance, param_name):
            kwargs[param_name] = getattr(instance, param_name)

    instance.__init__(**kwargs)


def _extract_kwargs(method, cmd_info, parsed):
    """从 parsed namespace 中提取方法所需的关键字参数"""
    sig = cmd_info['signature']
    hints = cmd_info.get('type_hints', {})
    kwargs = {}

    for param_name, param in sig.parameters.items():
        if param_name == 'self':
            continue

        raw_value = getattr(parsed, param_name, None)
        param_type = hints.get(param_name, str)
        converted = convert_value(raw_value, param_type)
        kwargs[param_name] = converted

    return kwargs


def _ensure_nbctx(instance):
    """确保实例的 nbctx 已初始化（调用 make_nbctx）"""
    if instance.nbctx is None:
        ctx = instance.make_nbctx()
        if ctx is not None:
            instance.nbctx = ctx


def _inject_nbctx(parent, child):
    """将父级的 nbctx 注入到子命令组实例"""
    parent_ctx = parent.nbctx
    if parent_ctx is not None:
        child.nbctx = parent_ctx


def _run_group_command(instance, group_info, parsed, base_cls, depth=1,
                       allow_method_list=None, hide_method_list=None, command_prefix=''):
    """执行子命令组中的命令"""
    group_cls = group_info['cls']
    group_kwargs = group_info.get('init_kwargs', {})

    try:
        group_instance = group_cls(**group_kwargs) if group_kwargs else group_cls()
    except TypeError:
        group_instance = group_cls.__new__(group_cls)

    _inject_nbctx(instance, group_instance)

    dest = '_nb_sub_command' if depth == 1 else '_nb_sub_command_{}'.format(depth)
    sub_command = getattr(parsed, dest, None)
    if not sub_command:
        print('请指定子命令。使用 --help 查看可用子命令。')
        return

    sub_python_name = sub_command.replace('-', '_')
    sub_commands = discover_commands(group_instance, base_cls,
                                     allow_method_list=allow_method_list,
                                     hide_method_list=hide_method_list,
                                     command_prefix=command_prefix)

    if sub_python_name in sub_commands and sub_commands[sub_python_name].get('is_group'):
        next_prefix = '{}/{}'.format(command_prefix, sub_python_name) if command_prefix else sub_python_name
        _run_group_command(group_instance, sub_commands[sub_python_name], parsed, base_cls,
                           depth=depth + 1, allow_method_list=allow_method_list,
                           hide_method_list=hide_method_list,
                           command_prefix=next_prefix)
        return

    if sub_python_name not in sub_commands:
        print('未知子命令: {}'.format(sub_command))
        return

    cmd_info = sub_commands[sub_python_name]
    method = cmd_info['method']
    kwargs = _extract_kwargs(method, cmd_info, parsed)

    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    _timeout = getattr(meta, 'timeout', 0)

    group_instance.before_run()
    try:
        result = _run_method_with_timeout(method, kwargs, _timeout)
        handle_cli_result(result)
    except Exception as e:
        group_instance.on_error(sub_command, e)
        raise
    finally:
        group_instance.after_run()

`````

--- **end of file: nb_cmd/modes/cli_mode.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/modes/tui_mode.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
TUI 模式 —— 基于 Textual 的终端图形交互界面。
需要安装: pip install textual (Python 3.8+)
"""
import asyncio
import inspect
import sys
import time

from ..core.discovery import discover_commands
from ..core.result_handler import handle_api_result


class _TuiWriter(object):
    """将 print 输出按行缓冲，通过回调安全地写入 RichLog。"""

    def __init__(self, write_fn):
        self._write = write_fn
        self._buf = ''

    def write(self, data):
        if not data:
            return
        self._buf += data
        lines = self._buf.split('\n')
        for line in lines[:-1]:
            self._write(line)
        self._buf = lines[-1]

    def flush(self):
        if self._buf:
            self._write(self._buf)
            self._buf = ''


def _detect_init_params(instance, unwrap_optional, _is_opt, is_enum_type,
                        get_choices, type_display_name, unwrap_arg):
    """提取 __init__ 中的参数信息，用于 TUI 全局参数面板。"""
    init_method = instance.__class__.__init__
    if init_method is object.__init__:
        return []
    sig = inspect.signature(init_method)
    params = []
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        has_default = param.default is not inspect.Parameter.empty
        raw_hint = param.annotation
        if raw_hint is inspect.Parameter.empty:
            if has_default and param.default is not None:
                raw_hint = type(param.default)
            else:
                raw_hint = str
        real_type, arg_inst = unwrap_arg(raw_hint)
        unwrapped = unwrap_optional(real_type) if _is_opt(real_type) else real_type
        desc = arg_inst.desc if arg_inst and arg_inst.desc else ''
        choices = get_choices(real_type)
        current_val = getattr(instance, pname, param.default if has_default else None)
        params.append({
            'name': pname,
            'type': unwrapped,
            'type_name': type_display_name(unwrapped),
            'real_type': real_type,
            'required': not has_default,
            'default': param.default if has_default else None,
            'current': current_val,
            'choices': choices,
            'desc': desc,
            'is_enum': is_enum_type(unwrapped),
        })
    return params


def start_tui(instance, base_cls):
    """启动 TUI 模式"""
    try:
        from textual.app import App, ComposeResult
        from textual.screen import Screen
        from textual.widgets import (
            Header, Footer, Tree, RichLog, Input, Button,
            Switch, Select, Static, Markdown, Label, Collapsible,
            TextArea,
        )
        from textual.containers import Horizontal, Vertical, VerticalScroll
        from textual import work
        from rich.text import Text
    except ImportError:
        print("TUI 模式需要安装 textual:")
        print("  pip install nb-cmd[tui]")
        if sys.version_info < (3, 8):
            print("  注意: TUI 模式需要 Python 3.8+")
        return

    from ..core.type_utils import (
        type_display_name, is_enum_type, unwrap_optional,
        is_optional as _is_opt, get_choices, convert_value,
    )
    from ..core.gen_cmd import CmdGen
    import re as _re

    _ANSI_FG = {
        '30': '#b0bec5', '31': '#ff6b6b', '32': '#69f0ae', '33': '#fff176',
        '34': '#64b5f6', '35': '#ce93d8', '36': '#80deea', '37': '#ffffff',
        '90': '#cfd8dc', '91': '#ff1744', '92': '#b9f6ca', '93': '#ffff8d',
        '94': '#90caf9', '95': '#ea80fc', '96': '#b2ebf2', '97': '#ffffff',
    }
    _ANSI_BG = {
        '40': '#78909c', '41': '#ff1744', '42': '#00e676', '43': '#ffea00',
        '44': '#2979ff', '45': '#d500f9', '46': '#00e5ff', '47': '#ffffff',
    }

    def _ansi_to_rich(data):
        """ANSI → Rich Text, stateful parser with vivid bg + auto-contrast."""
        parts = _re.split(r'\x1b\[([0-9;]*)m', data)
        txt = Text()
        st_fg = None
        st_bg = None
        st_bold = False
        st_ul = False
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    sp = []
                    if st_bold:
                        sp.append('bold')
                    if st_ul:
                        sp.append('underline')
                    if st_bg:
                        sp.append('on ' + st_bg)
                        h = st_bg.lstrip('#')
                        r = int(h[0:2], 16)
                        g = int(h[2:4], 16)
                        b = int(h[4:6], 16)
                        lum = 0.299 * r + 0.587 * g + 0.114 * b
                        sp.insert(0, '#000000' if lum > 128 else '#ffffff')
                    elif st_fg:
                        sp.insert(0, st_fg)
                    txt.append(part, style=' '.join(sp) if sp else None)
            else:
                for c in part.split(';'):
                    if c == '0' or c == '':
                        st_fg = st_bg = None
                        st_bold = st_ul = False
                    elif c == '1':
                        st_bold = True
                    elif c == '4':
                        st_ul = True
                    elif c in _ANSI_FG:
                        st_fg = _ANSI_FG[c]
                    elif c in _ANSI_BG:
                        st_bg = _ANSI_BG[c]
        return txt

    import os as _os
    import sqlite3 as _sqlite3

    _meta_db_dir = getattr(
        getattr(instance.__class__, 'Meta', type('Meta', (), {})),
        'db_dir', None)
    if _meta_db_dir:
        _db_dir = _os.path.expanduser(_meta_db_dir)
        if not _os.path.isdir(_db_dir):
            _os.makedirs(_db_dir, exist_ok=True)
    else:
        _db_dir = _os.getcwd()
    _db_path = _os.path.join(_db_dir, 'nb_cmd_web.db')

    def _get_db():
        conn = _sqlite3.connect(_db_path)
        conn.execute(
            'CREATE TABLE IF NOT EXISTS saved_commands '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'command TEXT UNIQUE NOT NULL, '
            'alias TEXT DEFAULT NULL, '
            'created_at TEXT DEFAULT CURRENT_TIMESTAMP)')
        conn.execute(
            'CREATE TABLE IF NOT EXISTS command_history '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'command TEXT NOT NULL, '
            'executed_at TEXT DEFAULT CURRENT_TIMESTAMP)')
        try:
            conn.execute('ALTER TABLE saved_commands ADD COLUMN alias TEXT DEFAULT NULL')
        except Exception:
            pass
        return conn

    _get_db().close()

    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    title = (getattr(meta, 'web_title', None)
             or getattr(meta, 'name', None)
             or instance.__class__.__name__)
    version = getattr(meta, 'version', None) or '0.0.1'
    _enable_exec = getattr(meta, 'enable_exec', True)
    _allow = getattr(meta, 'allow_method_list', None)
    _hide = getattr(meta, 'hide_method_list', None)
    _timeout = getattr(meta, 'timeout', 0)

    commands = discover_commands(
        instance, base_cls,
        enable_exec=_enable_exec,
        allow_method_list=_allow,
        hide_method_list=_hide,
    )
    user_cls = instance.__class__

    from ..core.arg import unwrap_arg
    init_params_info = _detect_init_params(instance, unwrap_optional, _is_opt,
                                           is_enum_type, get_choices,
                                           type_display_name, unwrap_arg)

    gen = CmdGen(user_cls, fmt='markdown')
    md_doc = gen.doc()

    # ================================================================
    #  HistoryScreen — 命令执行历史
    # ================================================================
    class HistoryScreen(Screen):
        BINDINGS = [("escape", "dismiss_screen", "返回")]

        def compose(self):
            yield Header()
            yield Static(" \u25b6 命令执行历史 (最近100条)", id="hist-title")
            yield VerticalScroll(id="hist-list")
            yield Footer()

        async def on_mount(self):
            container = self.query_one("#hist-list")
            conn = _get_db()
            rows = conn.execute(
                'SELECT command, executed_at FROM command_history '
                'ORDER BY id DESC LIMIT 100'
            ).fetchall()
            conn.close()
            if not rows:
                await container.mount(
                    Static("暂无历史记录", classes="hist-empty"))
                return
            seen = set()
            for cmd, ts in rows:
                if cmd in seen:
                    continue
                seen.add(cmd)
                btn = Button(
                    '{} ({})'.format(cmd, ts[:16] if ts else ''),
                    classes="hist-item",
                )
                btn._hist_cmd = cmd
                await container.mount(btn)

        def on_button_pressed(self, event):
            cmd = getattr(event.button, '_hist_cmd', None)
            if cmd:
                self.app.pop_screen()
                try:
                    main = self.app.get_screen("main")
                    gen_input = main.query_one("#cmd-gen", TextArea)
                    gen_input.text = cmd
                    main.notify("已填充: {}".format(cmd[:40]), timeout=2)
                except Exception:
                    pass

        def action_dismiss_screen(self):
            self.app.pop_screen()

    # ================================================================
    #  AliasInputScreen — 别名输入弹窗
    # ================================================================
    class AliasInputScreen(Screen):
        BINDINGS = [("escape", "dismiss_screen", "取消")]

        def __init__(self, command, existing_alias='', on_done=None):
            super().__init__()
            self._command = command
            self._existing_alias = existing_alias or ''
            self._on_done = on_done

        def compose(self):
            yield Header()
            with Vertical(id="alias-box"):
                yield Static("为收藏命令设置别名（可留空跳过）", id="alias-hint")
                yield Static("命令: {}".format(
                    self._command[:60] + ('...' if len(self._command) > 60 else '')
                ), id="alias-cmd-preview")
                yield Input(
                    value=self._existing_alias,
                    placeholder="输入别名，如: 查看日志、部署生产...",
                    id="alias-input",
                )
                with Horizontal(id="alias-btn-bar"):
                    yield Button("确定", variant="success", id="alias-ok")
                    yield Button("跳过", variant="default", id="alias-skip")
            yield Footer()

        def on_button_pressed(self, event):
            if event.button.id == 'alias-ok':
                alias = self.query_one("#alias-input", Input).value.strip()
                self._finish(alias)
            elif event.button.id == 'alias-skip':
                self._finish('')

        def on_input_submitted(self, event):
            if event.input.id == 'alias-input':
                alias = event.input.value.strip()
                self._finish(alias)

        def _finish(self, alias):
            if self._on_done:
                self._on_done(self._command, alias)
            self.app.pop_screen()

        def action_dismiss_screen(self):
            self.app.pop_screen()

    # ================================================================
    #  FavoritesScreen — 收藏命令
    # ================================================================
    class FavoritesScreen(Screen):
        BINDINGS = [("escape", "dismiss_screen", "返回")]

        def compose(self):
            yield Header()
            yield Static(" \u2605 收藏命令列表", id="fav-title")
            yield VerticalScroll(id="fav-list")
            yield Footer()

        async def on_mount(self):
            await self._load_items()

        async def _load_items(self):
            container = self.query_one("#fav-list")
            await container.remove_children()
            conn = _get_db()
            rows = conn.execute(
                'SELECT command, alias, created_at FROM saved_commands '
                'ORDER BY id DESC'
            ).fetchall()
            conn.close()
            if not rows:
                await container.mount(
                    Static("暂无收藏命令", classes="fav-empty"))
                return
            for cmd, alias, ts in rows:
                row = Horizontal(classes="fav-row")
                await container.mount(row)
                if alias:
                    label = Text()
                    label.append('[{}]'.format(alias), style='bold #e65100')
                    label.append(' {}'.format(cmd))
                else:
                    label = cmd
                btn = Button(label, classes="fav-item")
                btn._fav_cmd = cmd
                run_btn = Button("\u25b6", variant="success", classes="fav-run")
                run_btn._fav_cmd = cmd
                copy_btn = Button("\u2398", variant="primary", classes="fav-copy")
                copy_btn._fav_cmd = cmd
                edit_btn = Button("\u270e", variant="warning", classes="fav-edit")
                edit_btn._fav_cmd = cmd
                edit_btn._fav_alias = alias or ''
                del_btn = Button("\u2716", variant="error", classes="fav-del")
                del_btn._fav_cmd = cmd
                await row.mount(btn, run_btn, copy_btn, edit_btn, del_btn)

        def _on_alias_edited(self, command, alias):
            conn = _get_db()
            try:
                conn.execute(
                    'UPDATE saved_commands SET alias = ? WHERE command = ?',
                    (alias if alias else None, command))
                conn.commit()
            finally:
                conn.close()
            self.notify("别名已更新" if alias else "别名已清除", timeout=2)
            self.call_later(self._load_items)

        def on_button_pressed(self, event):
            cmd = getattr(event.button, '_fav_cmd', None)
            if not cmd:
                return
            if 'fav-del' in event.button.classes:
                conn = _get_db()
                try:
                    conn.execute(
                        'DELETE FROM saved_commands WHERE command = ?', (cmd,))
                    conn.commit()
                finally:
                    conn.close()
                self.notify("已取消收藏", timeout=2)
                self.call_later(self._load_items)
            elif 'fav-edit' in event.button.classes:
                existing = getattr(event.button, '_fav_alias', '')
                self.app.push_screen(
                    AliasInputScreen(cmd, existing, self._on_alias_edited))
            elif 'fav-run' in event.button.classes:
                self.app.pop_screen()
                try:
                    main = self.app.get_screen("main")
                    gen_input = main.query_one("#cmd-gen", TextArea)
                    gen_input.text = cmd
                    main._execute_from_cli_text()
                except Exception:
                    pass
            elif 'fav-copy' in event.button.classes:
                try:
                    self.app.copy_to_clipboard(cmd)
                    self.notify("已复制: {}".format(cmd[:40]), timeout=2)
                except Exception:
                    self.notify("复制失败", timeout=2)
            else:
                self.app.pop_screen()
                try:
                    main = self.app.get_screen("main")
                    gen_input = main.query_one("#cmd-gen", TextArea)
                    gen_input.text = cmd
                    main.notify("已填充: {}".format(cmd[:40]), timeout=2)
                except Exception:
                    pass

        def action_dismiss_screen(self):
            self.app.pop_screen()

    # ================================================================
    #  DocScreen — 首屏: CmdGen 生成的 Markdown 文档
    # ================================================================
    class DocScreen(Screen):
        BINDINGS = [
            ("enter", "go_main", "请按回车键进入交互模式"),
            ("escape", "go_main", "请按回车键进入交互模式"),
            ("ctrl+q", "quit_app", "退出"),
        ]

        def compose(self):
            yield Header()
            with VerticalScroll():
                yield Markdown(md_doc, id="doc-md")
            yield Footer()

        def action_go_main(self):
            self.app.switch_screen("main")

        def action_quit_app(self):
            self.app.exit()

    # ================================================================
    #  MainScreen — 左右分栏交互界面
    # ================================================================
    class MainScreen(Screen):
        BINDINGS = [
            ("ctrl+e", "execute", "执行"),
            ("ctrl+x", "stop", "停止"),
            ("ctrl+h", "show_history", "历史"),
            ("ctrl+f", "show_favorites", "收藏夹"),
            ("ctrl+l", "clear_log", "清空控制台"),
            ("ctrl+y", "copy_log", "复制输出"),
            ("ctrl+d", "show_doc", "查看文档"),
            ("ctrl+q", "quit_app", "退出"),
        ]

        def __init__(self):
            super().__init__()
            self._current_cmd = None
            self._current_path = None
            from collections import deque
            self._log_buffer = deque(maxlen=5000)
            self._worker_tid = None
            self._param_cache = {}

        def compose(self):
            yield Header()
            with Horizontal(id="main-split"):
                with Vertical(id="left-panel"):
                    with VerticalScroll(id="left-scroll"):
                        yield Static(" \u25b6 命令列表", id="tree-title")
                        tree = Tree(title, id="cmd-tree")
                        tree.root.expand()
                        self._build_tree(tree.root, commands, '')
                        yield tree

                        if init_params_info:
                            with Collapsible(title="全局参数", id="init-collapsible", collapsed=False):
                                init_form = VerticalScroll(id="init-form")
                                yield init_form

                        with Collapsible(title="参数", id="param-collapsible", collapsed=False):
                            yield VerticalScroll(
                                Static("\u2190 请在上方选择一个命令", id="form-hint"),
                                id="param-form",
                            )
                    with Horizontal(id="cmd-gen-bar"):
                        yield Label("CLI:", classes="cmd-gen-label")
                        yield TextArea(
                            id="cmd-gen",
                            language=None,
                            soft_wrap=True,
                            show_line_numbers=False,
                        )
                        with Vertical(id="cmd-gen-btns"):
                            yield Button("\u2605", id="btn-star")
                            yield Button("生成", id="btn-gen")
                            yield Button("运行", id="btn-run")
                    with Horizontal(id="btn-bar"):
                        yield Button("执行", variant="success", id="btn-exec")
                        yield Button("停止", variant="error", id="btn-stop", disabled=True)
                        yield Button("历史", id="btn-history")
                        yield Button("收藏夹", id="btn-favs")
                        yield Button("复制输出", variant="primary", id="btn-copy")
                        yield Button("清空控制台", variant="warning", id="btn-clear")
                        yield Button("退出", id="btn-quit")

                with Vertical(id="right-panel"):
                    yield Static(" \u25b6 输出控制台", id="log-title")
                    yield RichLog(
                        highlight=True,
                        markup=True,
                        auto_scroll=True,
                        wrap=True,
                        max_lines=5000,
                        id="output-log",
                    )
            yield Footer()

        # ---------- Init params form ----------

        async def on_mount(self):
            if not init_params_info:
                return
            form = self.query_one("#init-form")
            for p in init_params_info:
                pname = p['name']
                wid = 'init-{}'.format(pname)
                req = ' *' if p['required'] else ''
                label_text = '--{}{}:'.format(pname.replace('_', '-'), req)
                if p['desc']:
                    label_text += ' ({})'.format(p['desc'])

                val = p['current']
                if p['type'] is bool:
                    widget = Switch(value=bool(val) if val else False, id=wid)
                elif p['is_enum'] and p['choices']:
                    opts = [(str(c), c) for c in p['choices']]
                    sel_val = Select.BLANK
                    if val is not None:
                        dv = val.value if hasattr(val, 'value') else val
                        for _, v in opts:
                            if v == dv:
                                sel_val = dv
                                break
                    widget = Select(options=opts, value=sel_val, id=wid)
                else:
                    sv = str(val) if val is not None else ''
                    widget = Input(value=sv, placeholder=p['type_name'], id=wid)

                row = Horizontal(classes="form-row")
                await form.mount(row)
                await row.mount(
                    Label(label_text, classes="param-label"),
                    widget,
                )

        def _collect_init_params(self):
            """Collect init params from widgets, return dict or None."""
            if not init_params_info:
                return None
            form = self.query_one("#init-form")
            kwargs = {}
            for p in init_params_info:
                wid = '#init-{}'.format(p['name'])
                try:
                    w = form.query_one(wid)
                except Exception:
                    continue
                if isinstance(w, Switch):
                    kwargs[p['name']] = w.value
                elif isinstance(w, Select):
                    if w.value != Select.BLANK:
                        kwargs[p['name']] = convert_value(w.value, p['real_type'])
                elif isinstance(w, Input):
                    if w.value.strip():
                        kwargs[p['name']] = convert_value(w.value.strip(), p['real_type'])
                    elif p['default'] is not None:
                        kwargs[p['name']] = p['default']
            return kwargs if kwargs else None

        def _make_instance(self, init_kwargs=None):
            """Create a fresh instance with optional init param overrides."""
            if not init_kwargs:
                inst = user_cls()
            else:
                inst = user_cls(**init_kwargs)
            ctx = inst.make_nbctx()
            if ctx is not None:
                inst.nbctx = ctx
            return inst

        # ---------- Tree building ----------

        def _build_tree(self, parent, cmds, prefix):
            for name, info in cmds.items():
                cli_name = name.replace('_', '-')
                full_path = '{}/{}'.format(prefix, name) if prefix else name
                if info.get('is_group'):
                    doc = info.get('doc', '')
                    label = '{} {}'.format(
                        cli_name,
                        '({})'.format(doc[:30]) if doc else '',
                    )
                    node = parent.add(
                        label,
                        data={'type': 'group', 'path': full_path, 'info': info},
                    )
                    g_cls = info['cls']
                    g_kw = info.get('init_kwargs', {})
                    try:
                        g_inst = g_cls(**g_kw) if g_kw else g_cls()
                    except TypeError:
                        g_inst = g_cls.__new__(g_cls)
                    g_cmds = discover_commands(
                        g_inst, base_cls, include_builtins=False,
                        allow_method_list=_allow,
                        hide_method_list=_hide,
                        command_prefix=full_path,
                    )
                    self._build_tree(node, g_cmds, full_path)
                    node.expand()
                else:
                    doc = info.get('doc', '')
                    label = cli_name
                    if doc:
                        label = '{}  {}'.format(cli_name, doc[:40])
                    parent.add_leaf(
                        label,
                        data={'type': 'command', 'path': full_path, 'info': info},
                    )

        # ---------- Tree selection → form update ----------

        async def on_tree_node_selected(self, event):
            node_data = event.node.data
            if not node_data or node_data['type'] != 'command':
                return
            if self._current_path and self._current_cmd:
                self._param_cache[self._current_path] = self._collect_params()
            self._current_cmd = node_data['info']
            self._current_path = node_data['path']
            if init_params_info:
                try:
                    init_coll = self.query_one("#init-collapsible")
                    is_builtin = node_data['path'] in ('exec', 'shell')
                    init_coll.display = not is_builtin
                except Exception:
                    pass
            await self._refresh_form(node_data['info'])

        async def _refresh_form(self, cmd_info):
            form = self.query_one("#param-form")
            await form.remove_children()

            sig = cmd_info['signature']
            hints = cmd_info.get('type_hints', {})
            arg_meta = cmd_info.get('arg_meta', {})

            rows = []
            for pname, param in sig.parameters.items():
                if pname == 'self':
                    continue
                ptype = hints.get(pname, str)
                has_default = param.default is not inspect.Parameter.empty
                default = param.default if has_default else None
                real_type = unwrap_optional(ptype) if _is_opt(ptype) else ptype
                choices = get_choices(ptype)

                arg_inst = arg_meta.get(pname)
                desc = arg_inst.desc if arg_inst and arg_inst.desc else ''
                req = ' *' if not has_default else ''
                label_text = '--{}{}:'.format(pname.replace('_', '-'), req)
                if desc:
                    label_text += ' ({})'.format(desc)

                wid = 'param-{}'.format(pname)
                if real_type is bool:
                    widget = Switch(
                        value=bool(default) if default else False,
                        id=wid,
                    )
                elif is_enum_type(real_type) and choices:
                    opts = [(str(c), c) for c in choices]
                    sel_val = Select.BLANK
                    if default is not None:
                        dv = default.value if hasattr(default, 'value') else default
                        for _, v in opts:
                            if v == dv:
                                sel_val = dv
                                break
                    widget = Select(options=opts, value=sel_val, id=wid)
                elif pname == 'cmd' and real_type is str:
                    val = str(default) if default is not None else ''
                    widget = TextArea(
                        val, id=wid, language=None,
                        soft_wrap=True, show_line_numbers=False,
                    )
                else:
                    val = str(default) if default is not None else ''
                    ph = type_display_name(real_type)
                    widget = Input(value=val, placeholder=ph, id=wid)

                rows.append((label_text, widget))

            if not rows:
                await form.mount(
                    Static("该命令没有参数，直接点击执行", id="no-params")
                )
                return

            for label_text, widget in rows:
                row = Horizontal(classes="form-row")
                await form.mount(row)
                await row.mount(
                    Label(label_text, classes="param-label"),
                    widget,
                )

            cached = self._param_cache.get(self._current_path)
            if cached:
                for pname, val in cached.items():
                    wid = '#param-{}'.format(pname)
                    try:
                        w = form.query_one(wid)
                    except Exception:
                        continue
                    if isinstance(w, Switch):
                        w.value = bool(val)
                    elif isinstance(w, Select):
                        sv = val.value if hasattr(val, 'value') else val
                        try:
                            w.value = sv
                        except Exception:
                            pass
                    elif isinstance(w, TextArea):
                        w.text = str(val) if val is not None else ''
                    elif isinstance(w, Input):
                        w.value = str(val) if val is not None else ''

        # ---------- Collect form values ----------

        def _collect_params(self):
            if not self._current_cmd:
                return {}
            form = self.query_one("#param-form")
            sig = self._current_cmd['signature']
            hints = self._current_cmd.get('type_hints', {})
            kwargs = {}
            for pname, param in sig.parameters.items():
                if pname == 'self':
                    continue
                wid = '#param-{}'.format(pname)
                try:
                    w = form.query_one(wid)
                except Exception:
                    continue
                ptype = hints.get(pname, str)
                if isinstance(w, Switch):
                    kwargs[pname] = w.value
                elif isinstance(w, Select):
                    if w.value != Select.BLANK:
                        kwargs[pname] = convert_value(w.value, ptype)
                elif isinstance(w, TextArea):
                    if w.text.strip():
                        kwargs[pname] = convert_value(w.text.strip(), ptype)
                    elif param.default is not inspect.Parameter.empty:
                        kwargs[pname] = param.default
                elif isinstance(w, Input):
                    if w.value.strip():
                        kwargs[pname] = convert_value(w.value.strip(), ptype)
                    elif param.default is not inspect.Parameter.empty:
                        kwargs[pname] = param.default
            return kwargs

        def _build_cmd_str(self, path=None, kwargs=None):
            if path is None:
                path = self._current_path or ''
            if kwargs is None:
                kwargs = self._collect_params()
            cmd = path.replace('/', ' ').replace('_', '-')
            for k, v in kwargs.items():
                if isinstance(v, bool):
                    if v:
                        cmd += ' --{}'.format(k.replace('_', '-'))
                else:
                    sv = str(v)
                    if ' ' in sv or '\n' in sv or '"' in sv:
                        sv = '"{}"'.format(sv.replace('"', '\\"'))
                    cmd += ' --{} {}'.format(k.replace('_', '-'), sv)
            is_builtin = path in ('exec', 'shell')
            if not is_builtin:
                init_kw = self._collect_init_params()
                if init_kw:
                    for k, v in init_kw.items():
                        if isinstance(v, bool):
                            if v:
                                cmd += ' --{}'.format(k.replace('_', '-'))
                        else:
                            sv = str(v)
                            if ' ' in sv or '\n' in sv or '"' in sv:
                                sv = '"{}"'.format(sv.replace('"', '\\"'))
                            cmd += ' --{} {}'.format(k.replace('_', '-'), sv)
            return cmd

        def _update_cmd_gen(self):
            try:
                gen_input = self.query_one("#cmd-gen", TextArea)
                gen_input.text = self._build_cmd_str()
            except Exception:
                pass

        def _parse_cli_text(self):
            """解析 CLI 输入框文本 → (cmd_path, kwargs, cmd_info) 或 None"""
            text = self.query_one("#cmd-gen", TextArea).text.strip()
            if not text:
                return None
            import shlex
            try:
                tokens = shlex.split(text)
            except ValueError:
                tokens = text.split()
            if not tokens:
                return None

            path_parts = []
            current_cmds = commands
            i = 0
            cmd_info = None
            while i < len(tokens):
                token = tokens[i]
                if token.startswith('-'):
                    break
                py_name = token.replace('-', '_')
                if py_name not in current_cmds:
                    break
                info = current_cmds[py_name]
                path_parts.append(py_name)
                if info.get('is_group'):
                    g_cls = info['cls']
                    g_kw = info.get('init_kwargs', {})
                    try:
                        g_inst = g_cls(**g_kw) if g_kw else g_cls()
                    except TypeError:
                        g_inst = g_cls.__new__(g_cls)
                    current_cmds = discover_commands(
                        g_inst, base_cls, include_builtins=False,
                        allow_method_list=_allow,
                        hide_method_list=_hide,
                        command_prefix='/'.join(path_parts),
                    )
                else:
                    cmd_info = info
                    i += 1
                    break
                i += 1

            if not path_parts or cmd_info is None:
                return None
            cmd_path = '/'.join(path_parts)

            arg_tokens = tokens[i:]
            raw_kwargs = {}
            positional_tokens = []
            j = 0
            while j < len(arg_tokens):
                tok = arg_tokens[j]
                if tok.startswith('--'):
                    key = tok[2:].replace('-', '_')
                    if j + 1 < len(arg_tokens) and not arg_tokens[j + 1].startswith('-'):
                        raw_kwargs[key] = arg_tokens[j + 1]
                        j += 2
                    else:
                        raw_kwargs[key] = True
                        j += 1
                elif tok.startswith('-') and len(tok) == 2:
                    short_flag = tok
                    alias_map = cmd_info.get('arg_meta', {})
                    matched = None
                    for pn, am in alias_map.items():
                        if am and short_flag in am.aliases:
                            matched = pn
                            break
                    key = matched or tok[1:]
                    if j + 1 < len(arg_tokens) and not arg_tokens[j + 1].startswith('-'):
                        raw_kwargs[key] = arg_tokens[j + 1]
                        j += 2
                    else:
                        raw_kwargs[key] = True
                        j += 1
                else:
                    positional_tokens.append(tok)
                    j += 1

            sig = cmd_info.get('signature')
            hints = cmd_info.get('type_hints', {})

            if sig and positional_tokens:
                pos_idx = 0
                for pname, param in sig.parameters.items():
                    if pname == 'self' or pname in raw_kwargs:
                        continue
                    if param.default is not inspect.Parameter.empty:
                        continue
                    if pos_idx < len(positional_tokens):
                        raw_kwargs[pname] = positional_tokens[pos_idx]
                        pos_idx += 1
                if pos_idx < len(positional_tokens):
                    last_required = None
                    for pname, param in sig.parameters.items():
                        if pname == 'self':
                            continue
                        if param.default is inspect.Parameter.empty:
                            last_required = pname
                    if last_required and last_required in raw_kwargs:
                        remaining = positional_tokens[pos_idx:]
                        raw_kwargs[last_required] = raw_kwargs[last_required] + ' ' + ' '.join(remaining)

            kwargs = {}
            if sig:
                for k, v in raw_kwargs.items():
                    if k not in sig.parameters:
                        continue
                    if isinstance(v, bool):
                        kwargs[k] = v
                    else:
                        ptype = hints.get(k, str)
                        real = unwrap_optional(ptype) if _is_opt(ptype) else ptype
                        kwargs[k] = convert_value(str(v), real)
            else:
                kwargs = raw_kwargs
            return cmd_path, kwargs, cmd_info

        def _execute_from_cli_text(self):
            """解析 CLI 输入框文本并执行命令"""
            result = self._parse_cli_text()
            if result is None:
                self.notify("请输入有效命令（如: log --max-count 5）", timeout=3)
                return
            cmd_path, kwargs, cmd_info = result
            if self._worker_tid is not None:
                self.notify("有命令正在执行中", timeout=2)
                return
            self._current_cmd = cmd_info
            self._current_path = cmd_path
            self._exec_log = self.query_one("#output-log", RichLog)
            self._exec_kwargs = kwargs
            self._exec_path = cmd_path
            self.query_one("#btn-exec", Button).disabled = True
            self.query_one("#btn-stop", Button).disabled = False
            self._do_execute()

        # ---------- Resolve command path → (method, instance) ----------

        def _resolve(self, route_path):
            parts = route_path.split('/')
            init_kwargs = self._collect_init_params()
            if init_kwargs is not None:
                root_inst = self._make_instance(init_kwargs)
            else:
                root_inst = self._make_instance()

            if len(parts) == 1:
                name = parts[0]
                if name in commands and not commands[name].get('is_group'):
                    return getattr(root_inst, name), root_inst
                return None, None

            current_inst = root_inst
            current_cmds = commands
            current_prefix = ''
            for i, part in enumerate(parts):
                if part not in current_cmds:
                    return None, None
                info = current_cmds[part]
                if info.get('is_group'):
                    g_cls = info['cls']
                    g_kw = info.get('init_kwargs', {})
                    try:
                        child = g_cls(**g_kw) if g_kw else g_cls()
                    except TypeError:
                        child = g_cls.__new__(g_cls)
                    if current_inst.nbctx is not None:
                        child.nbctx = current_inst.nbctx
                    current_inst = child
                    current_prefix = (
                        '{}/{}'.format(current_prefix, part)
                        if current_prefix else part
                    )
                    current_cmds = discover_commands(
                        current_inst, base_cls,
                        include_builtins=False,
                        allow_method_list=_allow,
                        hide_method_list=_hide,
                        command_prefix=current_prefix,
                    )
                elif i == len(parts) - 1:
                    return getattr(current_inst, part), current_inst
            return None, None

        # ---------- Execution ----------

        def on_button_pressed(self, event):
            bid = event.button.id
            if bid == 'btn-exec':
                self.action_execute()
            elif bid == 'btn-stop':
                self.action_stop()
            elif bid == 'btn-star':
                self._toggle_star()
            elif bid == 'btn-gen':
                self._update_cmd_gen()
            elif bid == 'btn-run':
                self._execute_from_cli_text()
            elif bid == 'btn-history':
                self.action_show_history()
            elif bid == 'btn-favs':
                self.action_show_favorites()
            elif bid == 'btn-copy':
                self.action_copy_log()
            elif bid == 'btn-clear':
                self.action_clear_log()
            elif bid == 'btn-quit':
                self.action_quit_app()

        def on_input_submitted(self, event):
            self.action_execute()

        def action_execute(self):
            cli_text = ''
            try:
                cli_text = self.query_one("#cmd-gen", TextArea).text.strip()
            except Exception:
                pass
            if not self._current_cmd or not self._current_path:
                if cli_text:
                    self._execute_from_cli_text()
                return
            if self._worker_tid is not None:
                self.notify("有命令正在执行中", timeout=2)
                return
            self._exec_log = self.query_one("#output-log", RichLog)
            self._exec_kwargs = self._collect_params()
            self._exec_path = self._current_path
            self._update_cmd_gen()
            self.query_one("#btn-exec", Button).disabled = True
            self.query_one("#btn-stop", Button).disabled = False
            self._do_execute()

        def action_stop(self):
            tid = self._worker_tid
            if tid is None:
                return
            import ctypes
            try:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(
                    ctypes.c_ulong(tid),
                    ctypes.py_object(KeyboardInterrupt),
                )
            except Exception:
                pass

        def action_clear_log(self):
            self.query_one("#output-log", RichLog).clear()
            self._log_buffer.clear()

        def action_copy_log(self):
            text = '\n'.join(self._log_buffer)
            if text.strip():
                try:
                    self.app.copy_to_clipboard(text)
                    self.notify("已复制到剪贴板", timeout=2)
                except Exception:
                    self.notify("复制失败，请用 Shift+鼠标 选择文字", timeout=3)
            else:
                self.notify("控制台为空", timeout=2)

        def action_show_doc(self):
            self.app.switch_screen("doc")

        def action_show_history(self):
            self.app.push_screen(HistoryScreen())

        def action_show_favorites(self):
            self.app.push_screen(FavoritesScreen())

        def _toggle_star(self):
            cmd = self._build_cmd_str()
            if not cmd.strip():
                self.notify("请先选择命令", timeout=2)
                return
            conn = _get_db()
            try:
                exists = conn.execute(
                    'SELECT 1 FROM saved_commands WHERE command = ?',
                    (cmd,),
                ).fetchone()
                if exists:
                    conn.execute(
                        'DELETE FROM saved_commands WHERE command = ?', (cmd,))
                    self.notify("已取消收藏", timeout=2)
                    conn.commit()
                else:
                    conn.commit()
                    self.app.push_screen(
                        AliasInputScreen(cmd, '', self._on_star_done))
            finally:
                conn.close()

        def _on_star_done(self, command, alias):
            conn = _get_db()
            try:
                conn.execute(
                    'INSERT OR IGNORE INTO saved_commands (command, alias) VALUES (?, ?)',
                    (command, alias if alias else None))
                conn.commit()
            finally:
                conn.close()
            if alias:
                self.notify("已收藏: [{}]".format(alias), timeout=2)
            else:
                self.notify("已收藏", timeout=2)

        def action_quit_app(self):
            self.app.exit()

        def _buf_write(self, log, content, plain_text=None):
            """Write to RichLog and buffer plain text for clipboard copy."""
            buf_text = plain_text if plain_text is not None else str(content)
            self._log_buffer.append(buf_text)
            self.app.call_from_thread(log.write, content)

        def _reset_btn_state(self):
            try:
                self.query_one("#btn-exec", Button).disabled = False
                self.query_one("#btn-stop", Button).disabled = True
            except Exception:
                pass

        @work(thread=True)
        def _do_execute(self):
            import threading
            self._worker_tid = threading.current_thread().ident

            log = self._exec_log
            path = self._exec_path
            kwargs = self._exec_kwargs

            cmd_str = self._build_cmd_str(path, kwargs)
            echo = '$ {}'.format(cmd_str)

            try:
                conn = _get_db()
                conn.execute(
                    'INSERT INTO command_history (command) VALUES (?)',
                    (cmd_str,))
                conn.execute(
                    'DELETE FROM command_history WHERE id NOT IN '
                    '(SELECT id FROM command_history '
                    'ORDER BY id DESC LIMIT 1000)')
                conn.commit()
                conn.close()
            except Exception:
                pass
            self._buf_write(log, echo)

            method, target_inst = self._resolve(path)
            if method is None:
                err = '[错误] 无法解析命令: {}'.format(path)
                self._buf_write(
                    log, Text.from_markup('[bold red]{}[/]'.format(err)), err,
                )
                self._worker_tid = None
                self.app.call_from_thread(self._reset_btn_state)
                return

            old_stdout = sys.stdout
            old_stderr = sys.stderr

            def _on_line(d):
                self._log_buffer.append(d)
                self.app.call_from_thread(
                    log.write, _ansi_to_rich(d) if d else d,
                )

            writer = _TuiWriter(_on_line)
            sys.stdout = writer
            sys.stderr = writer

            start = time.time()
            try:
                target_inst.before_run()
                result = method(**kwargs)
                if inspect.iscoroutine(result):
                    result = asyncio.run(result)
                result = handle_api_result(result)
                if result is not None:
                    self._buf_write(log, str(result))
                elapsed = int((time.time() - start) * 1000)
                done = '[完成] {}ms'.format(elapsed)
                self._buf_write(
                    log, Text.from_markup('[bold green]{}[/]'.format(done)), done,
                )
            except KeyboardInterrupt:
                elapsed = int((time.time() - start) * 1000)
                msg = '[已取消] {}ms'.format(elapsed)
                self._buf_write(
                    log, Text.from_markup('[bold yellow]{}[/]'.format(msg)), msg,
                )
            except Exception as exc:
                elapsed = int((time.time() - start) * 1000)
                err = '[错误] {} ({}ms)'.format(str(exc), elapsed)
                self._buf_write(
                    log, Text.from_markup('[bold red]{}[/]'.format(err)), err,
                )
                try:
                    target_inst.on_error(path, exc)
                except Exception as hook_err:
                    herr = '[on_error 钩子异常] {}'.format(hook_err)
                    self._buf_write(
                        log, Text.from_markup('[bold red]{}[/]'.format(herr)), herr,
                    )
            finally:
                writer.flush()
                sys.stdout = old_stdout
                sys.stderr = old_stderr
                try:
                    target_inst.after_run()
                except Exception as hook_err:
                    herr = '[after_run 钩子异常] {}'.format(hook_err)
                    self._buf_write(
                        log, Text.from_markup('[bold red]{}[/]'.format(herr)), herr,
                    )
                self._worker_tid = None
                self.app.call_from_thread(self._reset_btn_state)

    # ================================================================
    #  App
    # ================================================================
    class NbCmdTuiApp(App):
        TITLE = '{} v{}'.format(title, version)

        CSS = """
        #main-split {
            height: 1fr;
        }
        #left-panel {
            width: 2fr;
            border-right: tall #0097e6;
        }
        #right-panel {
            width: 3fr;
        }
        #tree-title {
            background: #1a237e;
            color: #64b5f6;
            text-style: bold;
            height: 1;
            padding: 0 1;
        }
        #init-collapsible > CollapsibleTitle {
            background: #e65100;
            color: #ffe0b2;
            text-style: bold;
            padding: 0 1;
        }
        #param-collapsible > CollapsibleTitle {
            background: #1b5e20;
            color: #a5d6a7;
            text-style: bold;
            padding: 0 1;
        }
        Collapsible {
            border: none;
            padding: 0;
        }
        #log-title {
            background: #4a148c;
            color: #ce93d8;
            text-style: bold;
            height: 1;
            padding: 0 1;
        }
        #cmd-tree {
            height: auto;
            max-height: 50%;
            border-bottom: heavy #0f3460;
            scrollbar-color: #00b0ff;
            scrollbar-background: #001a33;
        }
        Tree > .tree--cursor {
            background: #0d47a1;
            color: #bbdefb;
            text-style: bold;
        }
        Tree > .tree--highlight {
            background: #1a237e;
        }
        #init-collapsible {
            height: auto;
            max-height: 10;
        }
        #param-collapsible {
            height: auto;
            max-height: 50%;
        }
        #init-form {
            height: auto;
            max-height: 8;
            scrollbar-color: #e040fb;
            scrollbar-background: #1a002e;
        }
        #param-form {
            height: auto;
            max-height: 100%;
            scrollbar-color: #00e676;
            scrollbar-background: #001a0d;
        }
        .form-row {
            height: auto;
            padding: 0 1;
        }
        .param-label {
            width: 18;
            min-width: 14;
            height: 3;
            content-align: left middle;
            padding-right: 1;
            color: #90caf9;
        }
        .form-row Input {
            width: 1fr;
            border: tall #37474f;
        }
        .form-row Input:focus {
            border: tall #00bcd4;
        }
        .form-row Switch {
            width: auto;
            height: auto;
            background: #1a2332;
            border: tall #37474f;
            padding: 0 1;
        }
        .form-row Switch:focus {
            border: tall #00bcd4;
        }
        Switch > .switch--slider {
            color: #90caf9;
        }
        Switch.-on > .switch--slider {
            color: #00e676;
        }
        .form-row Select {
            width: 1fr;
            border: tall #37474f;
        }
        .form-row Select:focus {
            border: tall #00bcd4;
        }
        #form-hint, #no-params {
            padding: 1;
            color: #546e7a;
        }
        #left-scroll {
            height: 1fr;
            scrollbar-color: #ff6d00;
            scrollbar-background: #1a1000;
        }
        #cmd-gen-bar {
            height: auto;
            min-height: 4;
            max-height: 10;
            padding: 0 1;
            dock: bottom;
            margin-bottom: 3;
        }
        .cmd-gen-label {
            width: 5;
            height: 3;
            content-align: right middle;
            color: #64b5f6;
            text-style: bold;
        }
        #cmd-gen {
            width: 1fr;
            min-height: 3;
            max-height: 8;
            border: tall #0097e6;
            background: #0a1929;
        }
        #cmd-gen:focus {
            border: tall #00e5ff;
        }
        #cmd-gen-btns {
            width: auto;
            height: auto;
            padding: 0;
        }
        #cmd-gen-btns Button {
            height: 3;
            min-width: 6;
            margin: 0 0 0 0;
        }
        .form-row TextArea {
            width: 1fr;
            min-height: 6;
            max-height: 12;
            border: tall #37474f;
        }
        .form-row TextArea:focus {
            border: tall #00bcd4;
        }
        #btn-star {
            width: 5;
            min-width: 5;
            background: #f57f17;
            color: #000000;
        }
        #btn-gen {
            min-width: 6;
            background: #0288d1;
            color: white;
        }
        #btn-run {
            min-width: 6;
            background: #2e7d32;
            color: white;
        }
        #btn-bar {
            height: 3;
            align: left middle;
            padding: 0 0;
            dock: bottom;
            background: #0a1929;
        }
        #btn-bar Button {
            min-width: 4;
            padding: 0 1;
            margin: 0 0 0 1;
        }
        #btn-stop {
            background: #d32f2f;
            color: white;
        }
        #btn-stop:disabled {
            background: #7f1d1d;
            color: #999999;
        }
        #btn-history {
            background: #00897b;
            color: white;
        }
        #btn-favs {
            background: #6a1b9a;
            color: white;
        }
        #btn-quit {
            background: #455a64;
            color: white;
        }
        #output-log {
            height: 1fr;
            scrollbar-color: #7c4dff;
            scrollbar-background: #0a1929;
        }
        #hist-title {
            background: #1a237e;
            color: #64b5f6;
            text-style: bold;
            height: 1;
            padding: 0 1;
        }
        #fav-title {
            background: #6a1b9a;
            color: #ffffff;
            text-style: bold;
            height: 1;
            padding: 0 1;
        }
        #fav-list {
            background: #12001a;
            scrollbar-color: #ab47bc;
            scrollbar-background: #12001a;
        }
        .hist-item {
            width: 100%;
            margin: 0 0 1 0;
        }
        .hist-empty {
            padding: 2;
            color: #546e7a;
        }
        .fav-empty {
            padding: 2;
            color: #ce93d8;
        }
        .fav-row {
            height: auto;
            max-height: 4;
            background: #1e0533;
            border-bottom: solid #2d1b4e;
        }
        .fav-item {
            width: 1fr;
            background: transparent;
            color: #ffffff;
        }
        .fav-item:hover {
            background: #38006b;
            color: #00e676;
            text-style: bold;
        }
        .fav-item:focus {
            background: #4a148c;
            color: #00e676;
            text-style: bold;
        }
        .fav-run {
            width: 5;
            min-width: 5;
            background: #2e7d32;
            color: #ffffff;
        }
        .fav-run:hover {
            background: #43a047;
            color: #ffffff;
        }
        .fav-copy {
            width: 5;
            min-width: 5;
            background: #0277bd;
            color: #ffffff;
        }
        .fav-copy:hover {
            background: #039be5;
            color: #ffffff;
        }
        .fav-edit {
            width: 5;
            min-width: 5;
            background: #e65100;
            color: #ffffff;
        }
        .fav-edit:hover {
            background: #ff6d00;
            color: #ffffff;
        }
        .fav-del {
            width: 5;
            min-width: 5;
            background: #b71c1c;
            color: #ffffff;
        }
        .fav-del:hover {
            background: #d50000;
            color: #ffffff;
        }
        #alias-box {
            align: center middle;
            width: 70%;
            max-width: 80;
            height: auto;
            margin: 4 0;
            padding: 2;
            border: tall #0097e6;
            background: #0a1929;
        }
        #alias-hint {
            color: #64b5f6;
            text-style: bold;
            height: 1;
            margin-bottom: 1;
        }
        #alias-cmd-preview {
            color: #90a4ae;
            height: 1;
            margin-bottom: 1;
        }
        #alias-input {
            width: 100%;
            border: tall #37474f;
            margin-bottom: 1;
        }
        #alias-input:focus {
            border: tall #00bcd4;
        }
        #alias-btn-bar {
            height: 3;
            align: center middle;
        }
        #alias-btn-bar Button {
            margin: 0 1;
            min-width: 8;
        }
        """

        def on_mount(self):
            self.install_screen(DocScreen(), name="doc")
            self.install_screen(MainScreen(), name="main")
            self.push_screen("main")

    app = NbCmdTuiApp()
    app.run()

`````

--- **end of file: nb_cmd/modes/tui_mode.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/modes/web_mode.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
Web UI 模式 —— 自动生成 Web 界面，支持命令行输入 + 参数表单 + 实时控制台。
需要安装: pip install fastapi uvicorn websockets
"""
import asyncio
import inspect
import json
import os
import sys
import threading
import time

from ..core.discovery import discover_commands
from ..core.result_handler import handle_api_result


def start_web_server(instance, base_cls, host=None, port=None):
    """启动 Web UI 服务"""
    try:
        from fastapi import FastAPI
        from fastapi.responses import HTMLResponse
        from fastapi.middleware.cors import CORSMiddleware
        from starlette.websockets import WebSocket, WebSocketDisconnect
        import uvicorn
    except ImportError:
        print("Web UI模式需要安装 fastapi, uvicorn 和 websockets:")
        print("  pip install fastapi uvicorn websockets")
        return

    meta = getattr(instance.__class__, 'Meta', type('Meta', (), {}))
    title = getattr(meta, 'web_title', None) or getattr(meta, 'name', None) or instance.__class__.__name__
    version = getattr(meta, 'version', None) or '0.0.1'
    theme = getattr(meta, 'web_theme', 'light')

    if host is None:
        host = getattr(meta, 'serve_host', '0.0.0.0')
    if port is None:
        port = getattr(meta, 'serve_port', 8080)

    app = FastAPI(title=title, version=version)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from ..ui import colors as _colors_mod
    _colors_mod._COLOR_ENABLED = True

    _enable_exec = getattr(meta, 'enable_exec', True)
    _allow_methods = getattr(meta, 'allow_method_list', None)
    _hide_methods = getattr(meta, 'hide_method_list', None)
    _auth_token = getattr(meta, 'auth_token', None)
    _timeout = getattr(meta, 'timeout', 0)
    commands = discover_commands(instance, base_cls, enable_exec=_enable_exec,
                                 allow_method_list=_allow_methods,
                                 hide_method_list=_hide_methods)
    description = inspect.getdoc(instance) or instance.__class__.__name__

    from ..core._io_dispatch import _tls, install as _install_io
    _install_io()

    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ui', 'static')
    has_built_frontend = os.path.isfile(os.path.join(static_dir, 'index.html'))

    if _auth_token:
        from ..modes.api_mode import _install_auth_middleware
        _install_auth_middleware(app, _auth_token, exempt_prefixes=[
            '/api/', '/ws/', '/static/',
        ])

    from ..modes.api_mode import _register_routes as _register_pydantic_routes
    _register_pydantic_routes(app, instance, commands, base_cls=base_cls,
                              allow_method_list=_allow_methods,
                              hide_method_list=_hide_methods,
                              command_prefix='', timeout=_timeout)

    def _build_group_result(cmds_dict, command_prefix=''):
        """递归构建命令组的结构（含嵌套子命令组）"""
        result = {}
        for name, info in cmds_dict.items():
            if info.get('is_group'):
                g_cls = info['cls']
                g_kwargs = info.get('init_kwargs', {})
                group_path = '{}/{}'.format(command_prefix, name) if command_prefix else name
                try:
                    g_inst = g_cls(**g_kwargs) if g_kwargs else g_cls()
                except TypeError:
                    g_inst = g_cls.__new__(g_cls)
                g_cmds = discover_commands(g_inst, base_cls, include_builtins=False,
                                           allow_method_list=_allow_methods,
                                           hide_method_list=_hide_methods,
                                           command_prefix=group_path)
                result[name] = {
                    'type': 'group',
                    'description': info.get('doc', ''),
                    'sub_commands': _build_group_result(g_cmds, group_path),
                }
            else:
                result[name] = _build_cmd_info(info)
        return result

    @app.get('/api/commands', summary='获取所有命令及参数定义')
    async def get_commands():
        return _build_group_result(commands, '')

    init_params_info = _build_init_params_info(instance)
    _user_cls = instance.__class__

    @app.get('/api/init-params', summary='获取 __init__ 全局参数定义')
    async def get_init_params():
        result = []
        for p in init_params_info:
            result.append({
                'name': p['name'],
                'type': p['type'],
                'widget': p['widget'],
                'required': p.get('required', False),
                'default': p['default'],
                'current': _serialize_default(getattr(instance, p['name'], p['default'])),
                'choices': p['choices'],
                'description': p['description'],
            })
        return result

    @app.get('/api/help/{command}', summary='获取命令帮助')
    async def get_help(command: str):
        python_name = command.replace('-', '_')
        if python_name not in commands:
            return {"error": "未知命令: {}".format(command)}
        info = commands[python_name]
        return {
            "command": command,
            "description": info.get('full_doc', info.get('doc', '')),
        }

    import queue as _queue
    import sqlite3 as _sqlite3

    _meta_db_dir = getattr(
        getattr(instance.__class__, 'Meta', type('Meta', (), {})),
        'db_dir', None)
    if _meta_db_dir:
        _db_dir = os.path.expanduser(_meta_db_dir)
        if not os.path.isdir(_db_dir):
            os.makedirs(_db_dir, exist_ok=True)
    else:
        _db_dir = os.getcwd()
    _db_path = os.path.join(_db_dir, 'nb_cmd_web.db')

    def _get_db():
        conn = _sqlite3.connect(_db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS saved_commands '
                     '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                     'command TEXT UNIQUE NOT NULL, '
                     'alias TEXT DEFAULT NULL, '
                     'created_at TEXT DEFAULT CURRENT_TIMESTAMP)')
        conn.execute('CREATE TABLE IF NOT EXISTS command_history '
                     '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                     'command TEXT NOT NULL, '
                     'executed_at TEXT DEFAULT CURRENT_TIMESTAMP)')
        try:
            conn.execute('ALTER TABLE saved_commands ADD COLUMN alias TEXT DEFAULT NULL')
        except Exception:
            pass
        return conn

    _get_db().close()

    @app.get('/api/saved-commands', summary='获取收藏命令列表')
    async def get_saved_commands():
        conn = _get_db()
        rows = conn.execute(
            'SELECT id, command, alias, created_at FROM saved_commands ORDER BY id DESC'
        ).fetchall()
        conn.close()
        return [{'id': r[0], 'command': r[1], 'alias': r[2], 'created_at': r[3]} for r in rows]

    @app.post('/api/save-command', summary='收藏命令（去重）')
    async def save_command(body: dict):
        cmd = body.get('command', '').strip()
        if not cmd:
            return {'status': 'error', 'message': '命令不能为空'}
        alias = body.get('alias', '').strip() or None
        conn = _get_db()
        try:
            conn.execute(
                'INSERT OR IGNORE INTO saved_commands (command, alias) VALUES (?, ?)',
                (cmd, alias))
            conn.commit()
        finally:
            conn.close()
        return {'status': 'ok'}

    @app.put('/api/save-command', summary='更新收藏命令别名')
    async def update_saved_alias(body: dict):
        cmd = body.get('command', '').strip()
        if not cmd:
            return {'status': 'error', 'message': '命令不能为空'}
        alias = body.get('alias', '').strip() or None
        conn = _get_db()
        try:
            conn.execute(
                'UPDATE saved_commands SET alias = ? WHERE command = ?',
                (alias, cmd))
            conn.commit()
        finally:
            conn.close()
        return {'status': 'ok'}

    @app.delete('/api/save-command', summary='取消收藏命令')
    async def delete_saved_command(body: dict):
        cmd = body.get('command', '').strip()
        conn = _get_db()
        try:
            conn.execute('DELETE FROM saved_commands WHERE command = ?', (cmd,))
            conn.commit()
        finally:
            conn.close()
        return {'status': 'ok'}

    @app.get('/api/history', summary='获取命令执行历史（最近1000条）')
    async def get_history():
        conn = _get_db()
        rows = conn.execute(
            'SELECT id, command, executed_at FROM command_history '
            'ORDER BY id DESC LIMIT 1000'
        ).fetchall()
        conn.close()
        return [{'id': r[0], 'command': r[1], 'executed_at': r[2]} for r in rows]

    @app.post('/api/history', summary='记录一条执行历史')
    async def post_history(body: dict):
        cmd = body.get('command', '').strip()
        if not cmd:
            return {'status': 'error'}
        conn = _get_db()
        try:
            conn.execute('INSERT INTO command_history (command) VALUES (?)', (cmd,))
            conn.execute(
                'DELETE FROM command_history WHERE id NOT IN '
                '(SELECT id FROM command_history ORDER BY id DESC LIMIT 1000)')
            conn.commit()
        finally:
            conn.close()
        return {'status': 'ok'}

    def _make_instance(raw_init_params=None):
        """每次请求创建一个新的用户类实例，彼此隔离"""
        if not init_params_info:
            inst = _user_cls()
        else:
            from ..core.type_utils import convert_value
            kwargs = {}
            for p in init_params_info:
                pname = p['name']
                if raw_init_params and pname in raw_init_params:
                    kwargs[pname] = convert_value(raw_init_params[pname], p['_real_type'])
                elif p.get('required'):
                    kwargs[pname] = getattr(instance, pname)
            inst = _user_cls(**kwargs) if kwargs else _user_cls()
        ctx = inst.make_nbctx()
        if ctx is not None:
            inst.nbctx = ctx
        return inst

    def _resolve_command(route_path, raw_init_params=None):
        """根据路由路径解析出 (method, target_instance, cmd_info)，支持多层嵌套"""
        parts = route_path.replace('-', '_').split('/')
        if len(parts) == 1:
            cmd_name = parts[0]
            if cmd_name in commands and not commands[cmd_name].get('is_group'):
                info = commands[cmd_name]
                target_inst = _make_instance(raw_init_params)
                method = getattr(target_inst, cmd_name)
                return method, target_inst, info
        elif len(parts) >= 2:
            root_inst = _make_instance(raw_init_params)
            current_cmds = commands
            current_inst = root_inst
            current_path = ''
            for i, part in enumerate(parts):
                if part not in current_cmds:
                    break
                info = current_cmds[part]
                if info.get('is_group'):
                    current_path = '{}/{}'.format(current_path, part) if current_path else part
                    g_cls = info['cls']
                    g_kwargs = info.get('init_kwargs', {})
                    try:
                        child_inst = g_cls(**g_kwargs) if g_kwargs else g_cls()
                    except TypeError:
                        child_inst = g_cls.__new__(g_cls)
                    parent_ctx = current_inst.nbctx if current_inst is not None else None
                    if parent_ctx is not None:
                        child_inst.nbctx = parent_ctx
                    current_inst = child_inst
                    current_cmds = discover_commands(current_inst, base_cls,
                                                     include_builtins=False,
                                                     allow_method_list=_allow_methods,
                                                     hide_method_list=_hide_methods,
                                                     command_prefix=current_path)
                elif i == len(parts) - 1 and current_inst is not None:
                    return info['method'], current_inst, info
        return None, None, None

    def _cancel_thread(tid):
        """向指定线程注入 KeyboardInterrupt，模拟 Ctrl+C"""
        import ctypes
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_ulong(tid), ctypes.py_object(KeyboardInterrupt))
        return res == 1

    @app.websocket('/ws/execute')
    async def ws_execute(websocket: WebSocket):
        await websocket.accept()
        cancel_event = threading.Event()
        worker_thread = None
        try:
            msg = await websocket.receive_json()
            route_path = msg.get('command', '')
            raw_kwargs = msg.get('args', {})
            raw_init_params = msg.get('init_params', None)

            method, target_inst, cmd_info = _resolve_command(
                route_path, raw_init_params)
            if method is None:
                await websocket.send_json({
                    'type': 'error', 'error': '未知命令: {}'.format(route_path)
                })
                return

            kwargs = _convert_request_params(raw_kwargs, cmd_info)
            output_q = _queue.Queue()
            result_holder = {'result': None, 'error': None, 'cancelled': False}

            def _run():
                _tls.output_queue = output_q
                saved_streams = []
                for h in target_inst.logger.handlers:
                    if hasattr(h, 'stream'):
                        saved_streams.append((h, h.stream))
                        h.stream = sys.stderr
                try:
                    target_inst.before_run()
                    r = method(**kwargs)
                    if inspect.iscoroutine(r):
                        r = asyncio.run(r)
                    result_holder['result'] = handle_api_result(r)
                except KeyboardInterrupt:
                    result_holder['cancelled'] = True
                except Exception as exc:
                    if cancel_event.is_set():
                        result_holder['cancelled'] = True
                    else:
                        result_holder['error'] = str(exc)
                        target_inst.on_error(route_path, exc)
                finally:
                    for h, orig in saved_streams:
                        h.stream = orig
                    _tls.output_queue = None
                    target_inst.after_run()
                    output_q.put(None)

            t = threading.Thread(target=_run, daemon=True)
            worker_thread = t
            start_ts = time.time()
            t.start()

            if _timeout > 0:
                def _auto_timeout():
                    if not cancel_event.wait(_timeout):
                        cancel_event.set()
                        if t.is_alive() and t.ident:
                            _cancel_thread(t.ident)
                        result_holder['error'] = '命令执行超时（{} 秒）'.format(_timeout)
                _timer = threading.Thread(target=_auto_timeout, daemon=True)
                _timer.start()

            async def _listen_cancel():
                """后台监听客户端的取消消息"""
                try:
                    while not cancel_event.is_set():
                        client_msg = await asyncio.wait_for(
                            websocket.receive_json(), timeout=0.1)
                        if client_msg.get('action') == 'cancel':
                            cancel_event.set()
                            if t.is_alive() and t.ident:
                                _cancel_thread(t.ident)
                            return
                except asyncio.TimeoutError:
                    pass
                except (WebSocketDisconnect, Exception):
                    cancel_event.set()

            while True:
                listen_task = asyncio.ensure_future(_listen_cancel())
                try:
                    item = output_q.get(timeout=0.05)
                    if item is None:
                        listen_task.cancel()
                        break
                    stream_type, data = item
                    await websocket.send_json({'type': stream_type, 'data': data})
                except _queue.Empty:
                    if not t.is_alive():
                        while not output_q.empty():
                            item = output_q.get_nowait()
                            if item is None:
                                break
                            await websocket.send_json({
                                'type': item[0], 'data': item[1]
                            })
                        listen_task.cancel()
                        break
                    await asyncio.sleep(0.02)
                finally:
                    if not listen_task.done():
                        listen_task.cancel()

            t.join(timeout=2)
            duration = int((time.time() - start_ts) * 1000)

            if result_holder['cancelled'] or cancel_event.is_set():
                await websocket.send_json({
                    'type': 'cancelled',
                    'duration_ms': duration,
                })
            elif result_holder['error']:
                await websocket.send_json({
                    'type': 'error',
                    'error': result_holder['error'],
                    'duration_ms': duration,
                })
            else:
                await websocket.send_json({
                    'type': 'complete',
                    'result': result_holder['result'],
                    'duration_ms': duration,
                })
        except WebSocketDisconnect:
            cancel_event.set()
            if worker_thread and worker_thread.is_alive() and worker_thread.ident:
                _cancel_thread(worker_thread.ident)
        except Exception:
            pass

    if has_built_frontend:
        from fastapi.staticfiles import StaticFiles
        app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
    else:
        html_content = _generate_builtin_html(title, version, description, theme, _enable_exec)

        @app.get('/', response_class=HTMLResponse, include_in_schema=False)
        async def index():
            return html_content

    print('Web UI启动在 http://{}:{}'.format(host, port))
    print('API文档: http://{}:{}/docs'.format(host, port))
    uvicorn.run(app, host=host, port=port)


def _serialize_default(value):
    """将默认值转换为 JSON 可序列化的形式"""
    if value is inspect.Parameter.empty or value is None:
        return None
    import enum
    from pathlib import Path
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    try:
        json.dumps(value)
        return value
    except (TypeError, ValueError):
        return str(value)


def _build_init_params_info(instance):
    """提取 __init__ 中带默认值的参数，返回前端所需的参数定义列表"""
    from ..core.arg import unwrap_arg
    from ..core.type_utils import (
        type_display_name, is_enum_type, unwrap_optional,
        is_optional as _is_opt, is_list_type, get_choices,
    )

    init_method = instance.__class__.__init__
    if init_method is object.__init__:
        return []

    sig = inspect.signature(init_method)

    params = []
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue

        has_default = param.default is not inspect.Parameter.empty
        raw_hint = param.annotation
        if raw_hint is inspect.Parameter.empty:
            if has_default and param.default is not None:
                raw_hint = type(param.default)
            else:
                raw_hint = str

        real_type, arg_inst = unwrap_arg(raw_hint)
        unwrapped = unwrap_optional(real_type) if _is_opt(real_type) else real_type
        type_name = type_display_name(unwrapped)
        choices = get_choices(real_type)

        widget = 'text'
        if unwrapped is bool:
            widget = 'checkbox'
        elif unwrapped is int:
            widget = 'number'
        elif unwrapped is float:
            widget = 'number'
        elif is_enum_type(unwrapped):
            widget = 'select'
        elif is_list_type(unwrapped):
            widget = 'tags'

        desc = arg_inst.desc if arg_inst and arg_inst.desc else ''

        params.append({
            'name': pname,
            'type': type_name,
            'widget': widget,
            'required': not has_default,
            'default': _serialize_default(param.default) if has_default else None,
            'choices': choices,
            'description': desc,
            '_real_type': real_type,
        })
    return params


def _build_cmd_info(info):
    """将一条 discover_commands 返回的命令信息转为前端所需的格式"""
    from ..core.type_utils import (
        type_display_name, is_enum_type, unwrap_optional,
        is_optional as _is_opt, is_list_type,
        get_choices,
    )
    arg_meta = info.get('arg_meta', {})
    params = []
    for pname, param in info['signature'].parameters.items():
        if pname == 'self':
            continue
        ptype = info['type_hints'].get(pname, str)
        has_default = param.default is not inspect.Parameter.empty
        is_kw_only = param.kind == inspect.Parameter.KEYWORD_ONLY

        real_type = unwrap_optional(ptype)
        type_name = type_display_name(real_type)
        choices = get_choices(ptype)

        widget = 'text'
        if real_type is bool:
            widget = 'checkbox'
        elif real_type is int:
            widget = 'number'
        elif real_type is float:
            widget = 'number'
        elif is_enum_type(real_type):
            widget = 'select'
        elif is_list_type(real_type):
            widget = 'tags'

        arg_inst = arg_meta.get(pname)
        desc = arg_inst.desc if arg_inst and arg_inst.desc else ''

        params.append({
            'name': pname,
            'type': type_name,
            'widget': widget,
            'required': not has_default and not is_kw_only,
            'default': _serialize_default(param.default if has_default else None),
            'choices': choices,
            'optional': _is_opt(ptype),
            'description': desc,
        })
    return {
        'type': 'command',
        'description': info.get('doc', ''),
        'full_doc': info.get('full_doc', ''),
        'parameters': params,
    }


def _convert_request_params(request, cmd_info):
    """将 HTTP 请求参数转换为方法调用参数"""
    from ..core.type_utils import convert_value
    sig = cmd_info['signature']
    hints = cmd_info.get('type_hints', {})
    kwargs = {}
    for pname, param in sig.parameters.items():
        if pname == 'self':
            continue
        if pname in request:
            ptype = hints.get(pname, str)
            kwargs[pname] = convert_value(request[pname], ptype)
        elif param.default is not inspect.Parameter.empty:
            kwargs[pname] = param.default
    return kwargs


def _generate_builtin_html(title, version, description, theme, enable_exec=True):
    """生成内置的 Web UI HTML 页面（当没有 Vue 前端构建产物时使用）"""
    dark_css = """
        :root { --bg: #1a1a2e; --card-bg: #16213e; --text: #e0e0e0; --border: #0f3460;
                --primary: #0097e6; --primary-hover: #00b4d8; --input-bg: #0f3460;
                --console-bg: #0d1b2a; --success: #2ecc71; --warning: #f39c12;
                --error: #e74c3c; --info: #3498db; --hover-bg: #1b2838; }
    """ if theme == 'dark' else """
        :root { --bg: #f5f6fa; --card-bg: #ffffff; --text: #2c3e50; --border: #dcdde1;
                --primary: #0097e6; --primary-hover: #0078b8; --input-bg: #ffffff;
                --console-bg: #1e272e; --success: #2ecc71; --warning: #f39c12;
                --error: #e74c3c; --info: #3498db; --hover-bg: #f0f0f0; }
    """

    return '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + title + '''</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
''' + dark_css + '''
body { font-family: -apple-system, "Segoe UI", "Microsoft YaHei", sans-serif;
       background: var(--bg); color: var(--text); height: 100vh; display: flex; flex-direction: column; }
.header { padding: 12px 24px; border-bottom: 1px solid var(--border); display: flex;
           align-items: center; justify-content: space-between; background: var(--card-bg); }
.header h1 { font-size: 18px; }
.header .version { color: var(--primary); font-size: 13px; }
.main { flex: 1; display: flex; overflow: hidden; }
.left-panel { width: 45%; min-width: 200px; display: flex; flex-direction: column; overflow: hidden; }
.resizer { width: 5px; cursor: col-resize; background: var(--border); flex-shrink: 0;
           transition: background 0.15s; }
.resizer:hover, .resizer.active { background: var(--primary); }
.right-panel { flex: 1; min-width: 200px; display: flex; flex-direction: column; overflow: hidden; }
.cmd-input-area { padding: 16px; border-bottom: 1px solid var(--border); background: var(--card-bg); }
.cmd-input-area label { font-size: 13px; color: var(--info); margin-bottom: 6px; display: block; }
.cmd-input-wrapper { display: flex; align-items: center; background: var(--input-bg);
                      border: 1px solid var(--border); border-radius: 6px; padding: 0 12px; }
.cmd-input-wrapper span.prompt { color: var(--primary); font-family: monospace; margin-right: 8px; font-weight: bold; }
.cmd-input-wrapper input { flex: 1; border: none; outline: none; background: transparent;
                            color: var(--text); font-family: monospace; font-size: 15px; padding: 10px 0; }
.cmd-input-wrapper button { background: var(--primary); color: #fff; border: none; padding: 6px 16px;
                             border-radius: 4px; cursor: pointer; font-size: 13px; margin-left: 8px; }
.cmd-input-wrapper button:hover { background: var(--primary-hover); }
.form-area { flex: 1; overflow-y: auto; padding: 0; }
.form-section { border-bottom: 1px solid var(--border); }
.form-section-header { padding: 10px 16px; cursor: pointer; display: flex; align-items: center;
                        justify-content: space-between; background: var(--card-bg); }
.form-section-header:hover { background: var(--hover-bg); }
.form-section-header .cmd-name { font-weight: bold; font-size: 14px; }
.form-section-header .cmd-desc { font-size: 12px; color: #888; margin-left: 8px; }
.form-section-body { padding: 12px 16px; display: none; background: var(--bg); }
.form-section-body.open { display: block; }
.form-group { margin-bottom: 10px; display: flex; align-items: center; }
.form-group label { min-width: 120px; font-size: 13px; text-align: right; padding-right: 12px; white-space: nowrap; }
.form-group input, .form-group select { flex: 1; padding: 6px 10px; border: 1px solid var(--border);
                                          border-radius: 4px; background: var(--input-bg); color: var(--text);
                                          font-size: 13px; }
.form-group input[type=checkbox] { flex: none; width: 18px; height: 18px; }
.form-actions { margin-top: 8px; display: flex; gap: 8px; justify-content: flex-end; }
.form-actions button { padding: 6px 14px; border-radius: 4px; border: 1px solid var(--border);
                        cursor: pointer; font-size: 13px; background: var(--card-bg); color: var(--text); }
.form-actions button.primary { background: var(--primary); color: #fff; border-color: var(--primary); }
.console-area { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.console-label { padding: 8px 16px; font-size: 13px; color: var(--info); background: var(--card-bg);
                  border-bottom: 1px solid var(--border); }
.console-output { flex: 1; background: var(--console-bg); color: #a8e6cf; font-family: "Consolas","Courier New",monospace;
                   font-size: 13px; line-height: 1.6; padding: 12px 16px; overflow-y: auto; white-space: pre-wrap; word-break: break-all; }
.console-output .ts { color: #636e72; }
.console-output .cmd-echo { color: var(--primary); }
.console-output .err { color: var(--error); }
.console-output .ok { color: var(--success); }
.status-bar { padding: 6px 16px; font-size: 12px; border-top: 1px solid var(--border);
               background: var(--card-bg); display: flex; justify-content: space-between; color: #888; }
.arrow { transition: transform 0.2s; } .arrow.open { transform: rotate(90deg); }
.save-cmd-btn { background: transparent; color: #888; border: none; font-size: 18px; cursor: pointer;
               padding: 4px 8px; margin-left: 4px; line-height: 1; }
.save-cmd-btn:hover { color: #ffd740; }
.s2-wrap { display: flex; flex-direction: column; gap: 6px; padding: 6px 16px; background: var(--card-bg); border-bottom: 1px solid var(--border); }
.s2-box { position: relative; flex: 1; }
.s2-trigger { display: flex; align-items: center; gap: 6px; padding: 7px 10px; border: 1px solid var(--border);
              border-radius: 4px; background: var(--input-bg); cursor: pointer; font-size: 13px;
              transition: border-color 0.15s; user-select: none; }
.s2-trigger:hover { border-color: var(--primary); }
.s2-box.open .s2-trigger { border-color: var(--primary); border-radius: 4px 4px 0 0; }
.s2-icon { flex-shrink: 0; font-size: 14px; }
.s2-label { flex-shrink: 0; font-size: 13px; }
.s2-count { font-size: 11px; color: #888; background: var(--bg); padding: 0 6px; border-radius: 8px; margin-left: auto; }
.s2-arrow { flex-shrink: 0; font-size: 10px; color: #888; transition: transform 0.2s; }
.s2-box.open .s2-arrow { transform: rotate(180deg); }
.s2-drop { display: none; position: absolute; top: 100%; left: 0; right: 0; z-index: 1000;
           background: var(--card-bg); border: 1px solid var(--primary); border-top: none;
           border-radius: 0 0 4px 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
.s2-box.open .s2-drop { display: block; }
.s2-search { width: 100%; padding: 7px 10px; border: none; border-bottom: 1px solid var(--border);
             outline: none; background: var(--input-bg); color: var(--text); font-size: 12px; box-sizing: border-box; }
.s2-list { max-height: 200px; overflow-y: auto; }
.s2-item { padding: 6px 10px; cursor: pointer; font-family: monospace; font-size: 12px;
           display: flex; align-items: center; white-space: nowrap; overflow: hidden; }
.s2-item:hover { background: var(--hover-bg); }
.s2-item .s2-iico { margin-right: 6px; flex-shrink: 0; font-size: 11px; }
.s2-item .s2-itxt { flex: 1; overflow: hidden; text-overflow: ellipsis; }
.s2-item .s2-alias { color: #e65100; font-weight: bold; font-size: 11px; margin-right: 4px; flex-shrink: 0; }
.s2-item .s2-iedit { flex-shrink: 0; margin-left: 4px; color: #888; cursor: pointer;
                     border: none; background: none; font-size: 12px; padding: 0 3px; }
.s2-item .s2-iedit:hover { color: #ffd740; }
.s2-item .s2-idel { flex-shrink: 0; margin-left: 4px; color: #888; cursor: pointer;
                     border: none; background: none; font-size: 13px; padding: 0 4px; }
.s2-item .s2-idel:hover { color: var(--error); }
.s2-empty { padding: 10px; font-size: 11px; color: #636e72; text-align: center; }
button:disabled, .form-actions button:disabled { opacity: 0.4; cursor: not-allowed; }
.clear-btn { background: transparent; color: #888; border: 1px solid var(--border); padding: 2px 10px;
             border-radius: 4px; cursor: pointer; font-size: 12px; margin-left: 12px; }
.clear-btn:hover { color: #fff; background: var(--error); border-color: var(--error); }
.stop-btn { display: none; background: var(--error); color: #fff; border: none; padding: 2px 10px;
            border-radius: 4px; cursor: pointer; font-size: 12px; margin-left: 8px; }
.stop-btn:hover { opacity: 0.85; }
.stop-btn.visible { display: inline-block; }
</style>
</head>
<body>
<div class="header">
  <h1>''' + title + ''' <span class="version">v''' + version + '''</span></h1>
  <span>''' + description + '''</span>
</div>
<div class="main">
  <div class="left-panel">
    <div class="cmd-input-area">
      <label>&#128421; 命令行输入</label>
      <div class="cmd-input-wrapper">
        <span class="prompt">$</span>
        <input id="cmdInput" type="text" placeholder="输入命令..." autofocus autocomplete="off" />
        <button onclick="executeFromInput()">执行</button>
        <button class="save-cmd-btn" onclick="saveCurrentCmd()" onmousedown="event.preventDefault()" title="收藏当前命令">&#9733;</button>
      </div>
    </div>
    <div class="s2-wrap">
      <div class="s2-box" id="s2Saved">
        <div class="s2-trigger" onclick="toggleS2('s2Saved')">
          <span class="s2-icon" style="color:#ffd740;">&#9733;</span>
          <span class="s2-label">收藏</span>
          <span class="s2-count" id="savedCount">0</span>
          <span class="s2-arrow">&#9662;</span>
        </div>
        <div class="s2-drop" onmousedown="event.stopPropagation()">
          <input class="s2-search" id="savedSearch" type="text" placeholder="搜索收藏..." oninput="renderSaved()" />
          <div class="s2-list" id="savedBody"></div>
        </div>
      </div>
      <div class="s2-box" id="s2Hist">
        <div class="s2-trigger" onclick="toggleS2('s2Hist')">
          <span class="s2-icon" style="color:#82b1ff;">&#128339;</span>
          <span class="s2-label">历史</span>
          <span class="s2-count" id="histCount">0</span>
          <span class="s2-arrow">&#9662;</span>
        </div>
        <div class="s2-drop" onmousedown="event.stopPropagation()">
          <input class="s2-search" id="histSearch" type="text" placeholder="搜索历史..." oninput="renderHist()" />
          <div class="s2-list" id="histBody"></div>
        </div>
      </div>
    </div>
    <div id="initParamsArea" style="display:none;"></div>
    <div class="form-area" id="formArea">
      <p style="padding:16px;color:#888;">加载中...</p>
    </div>
  </div>
  <div class="resizer" id="resizer"></div>
  <div class="right-panel">
    <div class="console-area">
      <div class="console-label">&#128203; 实时控制台输出<button class="clear-btn" onclick="clearConsole()" title="清空控制台">&#128465; 清空</button><button class="stop-btn" id="stopBtn" onclick="cancelExecution()" title="停止执行">&#9632; 停止</button></div>
      <div class="console-output" id="consoleOutput"></div>
    </div>
  </div>
</div>
<div class="status-bar">
  <span id="statusText">状态: 就绪</span>
  <span id="execCount">执行次数: 0</span>
</div>

<script>
let commands = {};
let initParamNames = [];
let enableExec = ''' + ('true' if enable_exec else 'false') + ''';
let history = [];
let historyIdx = -1;
let execCount = 0;
let isExecuting = false;
let activeWs = null;

function setExecuting(running) {
  isExecuting = running;
  var btns = document.querySelectorAll('.form-actions button.primary, .cmd-input-wrapper button');
  btns.forEach(function(b) { b.disabled = running; });
  var stopBtn = document.getElementById('stopBtn');
  if (running) { stopBtn.classList.add('visible'); } else { stopBtn.classList.remove('visible'); }
}

function cancelExecution() {
  if (activeWs && activeWs.readyState === WebSocket.OPEN) {
    activeWs.send(JSON.stringify({action: 'cancel'}));
  }
}

function clearConsole() {
  document.getElementById('consoleOutput').innerHTML = '';
}

function esc(s) { var d=document.createElement('div'); d.textContent=String(s); return d.innerHTML; }

function ansiToHtml(raw) {
  var fgMap = {
    '30':'#b0bec5','31':'#ff6b6b','32':'#69f0ae','33':'#ffd740',
    '34':'#82b1ff','35':'#b388ff','36':'#84ffff','37':'#ffffff',
    '90':'#cfd8dc','91':'#ff1744','92':'#76ff03','93':'#ffff00',
    '94':'#40c4ff','95':'#ea80fc','96':'#18ffff','97':'#ffffff'
  };
  var bgMap = {
    '40':'#90a4ae','41':'#ff5252','42':'#69f0ae','43':'#ffff00',
    '44':'#448aff','45':'#7c4dff','46':'#18ffff','47':'#e0e0e0',
    '100':'#b0bec5','101':'#ff8a80','102':'#b9f6ca','103':'#ffff8d',
    '104':'#82b1ff','105':'#b388ff','106':'#84ffff','107':'#eeeeee'
  };
  var bgTxt = {
    '40':'#fff','41':'#fff','42':'#000','43':'#000',
    '44':'#fff','45':'#fff','46':'#000','47':'#000',
    '100':'#000','101':'#000','102':'#000','103':'#000',
    '104':'#000','105':'#000','106':'#000','107':'#000'
  };
  var parts = String(raw).split(/\\x1b\\[([0-9;]*)m/);
  var html = '', spans = 0;
  for (var i = 0; i < parts.length; i++) {
    if (i % 2 === 0) {
      html += esc(parts[i]);
    } else {
      var codes = parts[i].split(';');
      for (var j = 0; j < codes.length; j++) {
        var c = codes[j];
        if (c === '0' || c === '') {
          while (spans > 0) { html += '</span>'; spans--; }
        } else if (c === '1') {
          html += '<span style="font-weight:bold">'; spans++;
        } else if (c === '4') {
          html += '<span style="text-decoration:underline">'; spans++;
        } else if (fgMap[c]) {
          html += '<span style="color:' + fgMap[c] + '">'; spans++;
        } else if (bgMap[c]) {
          html += '<span style="background:' + bgMap[c] + ';color:' + (bgTxt[c]||'#fff') + ';padding:2px 6px;border-radius:3px">'; spans++;
        }
      }
    }
  }
  while (spans > 0) { html += '</span>'; spans--; }
  return html;
}

function findCmdInfo(pyName) {
  var parts = pyName.split('/');
  var node = commands;
  for (var i = 0; i < parts.length; i++) {
    if (!node || !node[parts[i]]) return null;
    if (i === parts.length - 1) return node[parts[i]];
    if (node[parts[i]].type === 'group' && node[parts[i]].sub_commands) {
      node = node[parts[i]].sub_commands;
    } else {
      return null;
    }
  }
  return null;
}

async function loadCommands() {
  try {
    const resp = await fetch('/api/commands');
    commands = await resp.json();
    renderForms();
  } catch(e) { console.error(e); }
}

async function loadInitParams() {
  try {
    var resp = await fetch('/api/init-params');
    var params = await resp.json();
    if (!params || params.length === 0) return;
    initParamNames = params.map(function(p) { return p.name; });
    var area = document.getElementById('initParamsArea');
    area.style.display = 'block';
    var html = '<div class="form-section"><div class="form-section-header" onclick="toggleSection(this)">';
    html += '<span><span class="arrow open">&#9654;</span> <span class="cmd-name" style="color:var(--warning);">&#9881; 全局选项</span>';
    html += '<span class="cmd-desc">__init__ 参数，每次执行自动携带</span></span></div>';
    html += '<div class="form-section-body open" id="initParamsForm">';
    params.forEach(function(p) {
      var descHtml = p.description ? '<span style="font-size:11px;color:#888;margin-left:4px;">' + esc(p.description) + '</span>' : '';
      html += '<div class="form-group"><label>' + p.name + (p.required?' *':'') + ':' + descHtml + '</label>';
      var val = p.current != null ? p.current : (p.default != null ? p.default : '');
      if (p.widget === 'checkbox') {
        html += '<input type="checkbox" data-init-param="' + p.name + '"' + (val ? ' checked' : '') + '/>';
      } else if (p.widget === 'select' && p.choices) {
        html += '<select data-init-param="' + p.name + '">';
        p.choices.forEach(function(c) {
          html += '<option value="' + c + '"' + (c == val ? ' selected' : '') + '>' + c + '</option>';
        });
        html += '</select>';
      } else if (p.widget === 'number') {
        html += '<input type="number" data-init-param="' + p.name + '" value="' + val + '"/>';
      } else {
        html += '<input type="text" data-init-param="' + p.name + '" value="' + val + '"/>';
      }
      html += '</div>';
    });
    html += '</div></div>';
    area.innerHTML = html;
  } catch(e) { console.error(e); }
}

function getInitParams() {
  var form = document.getElementById('initParamsForm');
  if (!form) return null;
  var data = {};
  var hasAny = false;
  form.querySelectorAll('[data-init-param]').forEach(function(el) {
    var name = el.dataset.initParam;
    if (el.type === 'checkbox') { data[name] = el.checked; hasAny = true; }
    else if (el.type === 'number' && el.value !== '') { data[name] = Number(el.value); hasAny = true; }
    else if (el.value !== '') { data[name] = el.value; hasAny = true; }
  });
  return hasAny ? data : null;
}

function renderParamFields(params) {
  var html = '';
  if (!params) return html;
  params.forEach(function(p) {
    var descHtml = p.description ? '<span style="font-size:11px;color:#888;margin-left:4px;">' + esc(p.description) + '</span>' : '';
    html += '<div class="form-group"><label>' + p.name + (p.required?' *':'') + ':' + descHtml + '</label>';
    var ph = p.description || p.type;
    if (p.widget === 'checkbox') {
      html += '<input type="checkbox" data-param="' + p.name + '"' + (p.default?' checked':'') + '/>';
    } else if (p.widget === 'select' && p.choices) {
      html += '<select data-param="' + p.name + '">';
      p.choices.forEach(function(c) {
        html += '<option value="' + c + '"' + (c==p.default?' selected':'') + '>' + c + '</option>';
      });
      html += '</select>';
    } else if (p.widget === 'number') {
      html += '<input type="number" data-param="' + p.name + '" placeholder="' + esc(ph) + '" value="' + (p.default!=null?p.default:'') + '"/>';
    } else {
      html += '<input type="text" data-param="' + p.name + '" placeholder="' + esc(ph) + '" value="' + (p.default!=null?p.default:'') + '"/>';
    }
    html += '</div>';
  });
  return html;
}

function renderCmdSection(formId, cliLabel, description, params) {
  var html = '<div class="form-section"><div class="form-section-header" onclick="toggleSection(this)">';
  html += '<span><span class="arrow">&#9654;</span> <span class="cmd-name">' + cliLabel + '</span>';
  html += '<span class="cmd-desc">' + (description||'') + '</span></span></div>';
  html += '<div class="form-section-body" id="form_' + formId + '">';
  html += renderParamFields(params);
  html += '<div class="form-actions">';
  html += '<button onclick="generateCmd(\\'' + formId + '\\')">生成命令</button>';
  html += '<button class="primary" onclick="executeForm(\\'' + formId + '\\')">直接执行</button>';
  html += '</div></div></div>';
  return html;
}

function renderGroup(cmds, prefix) {
  var html = '';
  for (var [name, info] of Object.entries(cmds)) {
    var cliName = name.replace(/_/g, '-');
    var fullPrefix = prefix ? prefix + '/' + name : name;
    var fullLabel = prefix ? prefix.replace(/_/g,'-').replace(/\\//g,' ') + ' ' + cliName : cliName;
    if (info.type === 'group') {
      html += '<div class="form-section"><div class="form-section-header" onclick="toggleSection(this)">';
      html += '<span><span class="arrow">&#9654;</span> <span class="cmd-name" style="color:var(--primary);">' + fullLabel + '</span>';
      html += '<span class="cmd-desc">[组] ' + (info.description||'') + '</span></span></div>';
      html += '<div class="form-section-body">';
      if (info.sub_commands) { html += renderGroup(info.sub_commands, fullPrefix); }
      html += '</div></div>';
    } else {
      html += renderCmdSection(fullPrefix, fullLabel, info.description, info.parameters);
    }
  }
  return html;
}

function renderForms() {
  const area = document.getElementById('formArea');
  var html = renderGroup(commands, '');
  area.innerHTML = html || '<p style="padding:16px;color:#888;">无可用命令</p>';
}

function toggleSection(el) {
  const body = el.nextElementSibling;
  const arrow = el.querySelector('.arrow');
  body.classList.toggle('open');
  arrow.classList.toggle('open');
}

function getFormData(formId) {
  const form = document.getElementById('form_' + formId);
  if (!form) return {};
  const data = {};
  form.querySelectorAll('[data-param]').forEach(function(el) {
    const name = el.dataset.param;
    if (el.type === 'checkbox') { data[name] = el.checked; }
    else if (el.type === 'number' && el.value) { data[name] = Number(el.value); }
    else if (el.value) { data[name] = el.value; }
  });
  return data;
}

function generateCmd(formId) {
  var data = getFormData(formId);
  var cliName = formId.replace(/_/g, '-').replace('/', ' ');
  var parts = cliName.split(' ');
  var pyName = formId.replace(/-/g, '_');
  var info = findCmdInfo(pyName);
  if (info && info.parameters) {
    info.parameters.forEach(function(p) {
      if (p.name in data) {
        if (p.required && p.widget !== 'checkbox') {
          parts.push(String(data[p.name]));
        } else if (p.widget === 'checkbox') {
          if (data[p.name]) parts.push('--' + p.name.replace(/_/g, '-'));
        } else {
          parts.push('--' + p.name.replace(/_/g, '-') + ' ' + String(data[p.name]));
        }
      }
    });
  }
  var isBuiltin = (formId === 'exec' || formId === 'shell');
  if (!isBuiltin) {
    var initP = getInitParams();
    if (initP) {
      Object.entries(initP).forEach(function(e) {
        if (typeof e[1] === 'boolean') {
          if (e[1]) parts.push('--' + e[0].replace(/_/g, '-'));
        } else {
          parts.push('--' + e[0].replace(/_/g, '-'));
          parts.push(String(e[1]));
        }
      });
    }
  }
  document.getElementById('cmdInput').value = parts.join(' ');
  document.getElementById('cmdInput').focus();
}

async function executeForm(formId) {
  var data = getFormData(formId);
  var routePath = formId.replace(/_/g, '-');
  await doExecute(routePath, data);
}

async function executeFromInput() {
  const input = document.getElementById('cmdInput');
  const raw = input.value.trim();
  if (!raw) return;
  const parts = raw.split(/\\s+/);
  const firstPy = parts[0].replace(/-/g, '_');
  var routePath, cmdInfo, argStart;
  if (commands[firstPy] && commands[firstPy].type === 'group' && parts.length > 1) {
    var subPy = parts[1].replace(/-/g, '_');
    var grpInfo = commands[firstPy];
    cmdInfo = grpInfo.sub_commands ? grpInfo.sub_commands[subPy] : null;
    routePath = parts[0] + '/' + parts[1];
    argStart = 2;
  } else if (commands[firstPy]) {
    cmdInfo = commands[firstPy];
    routePath = parts[0];
    argStart = 1;
  } else if (enableExec) {
    await doExecute('exec', {cmd: raw});
    return;
  } else {
    appendLog('[错误] 未知命令: ' + parts[0], 'error');
    return;
  }
  const kwargs = {};
  const inputInitP = {};
  if (cmdInfo && cmdInfo.parameters) {
    let posIdx = 0;
    const positionals = cmdInfo.parameters.filter(function(p){return p.required;});
    for (let i = argStart; i < parts.length; i++) {
      if (parts[i].startsWith('--')) {
        const flag = parts[i].substring(2).replace(/-/g, '_');
        if (initParamNames.indexOf(flag) >= 0) {
          if (i + 1 < parts.length && !parts[i+1].startsWith('--')) { i++; inputInitP[flag] = parts[i]; }
          continue;
        }
        const param = cmdInfo.parameters.find(function(p){return p.name === flag;});
        if (param && param.widget === 'checkbox') { kwargs[flag] = true; }
        else if (i + 1 < parts.length) { i++; kwargs[flag] = parts[i]; }
      } else {
        if (posIdx < positionals.length) {
          kwargs[positionals[posIdx].name] = parts[i]; posIdx++;
        } else if (positionals.length > 0) {
          var lastP = positionals[positionals.length - 1].name;
          kwargs[lastP] += ' ' + parts[i];
        }
      }
    }
  }
  var overrideInit = Object.keys(inputInitP).length > 0 ? inputInitP : null;
  await doExecute(routePath, kwargs, overrideInit);
}

function doExecute(routePath, kwargs, initParamsOverride) {
  if (isExecuting) return;
  setExecuting(true);
  var consoleEl = document.getElementById('consoleOutput');
  var ts = new Date().toLocaleTimeString();
  var initP = initParamsOverride || getInitParams();
  var cmdStr = routePath.replace(/\\//g, ' ');
  Object.entries(kwargs).forEach(function(e) {
    if (typeof e[1] === 'boolean') { if(e[1]) cmdStr += ' --' + e[0].replace(/_/g,'-'); }
    else cmdStr += ' --' + e[0].replace(/_/g,'-') + ' ' + e[1];
  });

  function _finish(statusMsg) {
    setExecuting(false);
    activeWs = null;
    document.getElementById('statusText').innerText = statusMsg;
  }

  consoleEl.innerHTML += '<span class="ts">[' + ts + ']</span> <span class="cmd-echo">$ ' + cmdStr + '</span>\\n';
  document.getElementById('statusText').innerText = '状态: 执行中... ' + cmdStr;

  var wsProto = location.protocol === 'https:' ? 'wss:' : 'ws:';
  var wsUrl = wsProto + '//' + location.host + '/ws/execute';

  try {
    var ws = new WebSocket(wsUrl);
    activeWs = ws;
    ws.onopen = function() {
      var payload = {command: routePath, args: kwargs};
      if (initP) payload.init_params = initP;
      ws.send(JSON.stringify(payload));
    };
    ws.onmessage = function(event) {
      var msg = JSON.parse(event.data);
      if (msg.type === 'stdout') {
        consoleEl.innerHTML += ansiToHtml(msg.data);
      } else if (msg.type === 'stderr') {
        consoleEl.innerHTML += ansiToHtml(msg.data);
      } else if (msg.type === 'complete') {
        if (msg.result != null) {
          var resultStr = typeof msg.result === 'object'
            ? JSON.stringify(msg.result, null, 2) : String(msg.result);
          consoleEl.innerHTML += '<span class="ok">' + esc(resultStr) + '</span>\\n';
        }
        consoleEl.innerHTML += '<span class="ok">[完成] ' + (msg.duration_ms||0) + 'ms</span>\\n\\n';
        execCount++;
        document.getElementById('execCount').innerText = '执行次数: ' + execCount;
        _finish('状态: 就绪  |  最后执行: ' + cmdStr + ' ' + ts);
      } else if (msg.type === 'cancelled') {
        consoleEl.innerHTML += '<span class="err">[已取消] ' + (msg.duration_ms||0) + 'ms</span>\\n\\n';
        _finish('状态: 就绪  |  已取消: ' + cmdStr);
      } else if (msg.type === 'error') {
        consoleEl.innerHTML += '<span class="err">[错误] ' + esc(msg.error||'未知错误') + '</span>\\n\\n';
        _finish('状态: 就绪  |  出错: ' + cmdStr);
      }
      consoleEl.scrollTop = consoleEl.scrollHeight;
    };
    ws.onerror = function() {
      setExecuting(false); activeWs = null;
      _doExecuteFallback(routePath, kwargs, cmdStr, ts);
    };
    ws.onclose = function() {
      if (isExecuting) { setExecuting(false); activeWs = null; }
    };
  } catch(e) {
    setExecuting(false); activeWs = null;
    _doExecuteFallback(routePath, kwargs, cmdStr, ts);
  }
  addHistory(cmdStr);
}

function _doExecuteFallback(routePath, kwargs, cmdStr, ts) {
  var consoleEl = document.getElementById('consoleOutput');
  fetch('/' + routePath, {
    method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(kwargs)
  }).then(function(resp) { return resp.json(); }).then(function(data) {
    if (data.stdout) consoleEl.innerHTML += ansiToHtml(data.stdout);
    if (data.stderr) consoleEl.innerHTML += ansiToHtml(data.stderr);
    if (data.status === 'success') {
      if (data.result != null) {
        var resultStr = typeof data.result === 'object'
          ? JSON.stringify(data.result, null, 2) : String(data.result);
        consoleEl.innerHTML += '<span class="ok">' + esc(resultStr) + '</span>\\n';
      }
      consoleEl.innerHTML += '<span class="ok">[完成] ' + (data.duration_ms||0) + 'ms</span>\\n\\n';
    } else {
      consoleEl.innerHTML += '<span class="err">[错误] ' + esc(data.error||'未知错误') + '</span>\\n\\n';
    }
    execCount++;
    document.getElementById('execCount').innerText = '执行次数: ' + execCount;
    document.getElementById('statusText').innerText = '状态: 就绪  |  最后执行: ' + cmdStr + ' ' + ts;
    consoleEl.scrollTop = consoleEl.scrollHeight;
  }).catch(function(e) {
    consoleEl.innerHTML += '<span class="err">[网络错误] ' + e.message + '</span>\\n\\n';
  });
}

let savedCmds = [];

function addHistory(cmd) {
  history.unshift(cmd);
  if (history.length > 100) history.pop();
  fetch('/api/history', {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({command: cmd})
  }).catch(function(){});
  renderSaved(); renderHist();
}

async function loadHistory() {
  try {
    var resp = await fetch('/api/history');
    var data = await resp.json();
    history = data.map(function(d){ return d.command; });
  } catch(e) { console.error(e); }
}

async function saveCurrentCmd() {
  var cmd = document.getElementById('cmdInput').value.trim();
  if (!cmd) return;
  var alias = prompt('为收藏命令设置别名（可留空跳过）：', '');
  if (alias === null) return;
  await fetch('/api/save-command', {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({command: cmd, alias: alias.trim() || ''})
  });
  await loadSavedCmds();
  renderSaved();
}

async function deleteSavedCmd(cmd, ev) {
  if (ev) ev.stopPropagation();
  await fetch('/api/save-command', {
    method: 'DELETE', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({command: cmd})
  });
  await loadSavedCmds();
  renderSaved();
}

async function editSavedAlias(cmd, oldAlias, ev) {
  if (ev) ev.stopPropagation();
  var alias = prompt('修改别名（留空清除）：', oldAlias || '');
  if (alias === null) return;
  await fetch('/api/save-command', {
    method: 'PUT', headers: {'Content-Type':'application/json'},
    body: JSON.stringify({command: cmd, alias: alias.trim() || ''})
  });
  await loadSavedCmds();
  renderSaved();
}

async function loadSavedCmds() {
  try {
    var resp = await fetch('/api/saved-commands');
    savedCmds = await resp.json();
  } catch(e) { console.error(e); }
}

function fuzzyMatch(query, text) {
  if (!query) return true;
  var q = query.toLowerCase();
  var t = text.toLowerCase();
  if (t.indexOf(q) >= 0) return true;
  var qi = 0;
  for (var ti = 0; ti < t.length && qi < q.length; ti++) {
    if (t[ti] === q[qi]) qi++;
  }
  return qi === q.length;
}

function renderSaved() {
  var body = document.getElementById('savedBody');
  var q = document.getElementById('savedSearch').value.trim();
  var filtered = savedCmds.filter(function(s) {
    return fuzzyMatch(q, s.command) || (s.alias && fuzzyMatch(q, s.alias));
  });
  document.getElementById('savedCount').textContent = savedCmds.length;
  var html = '';
  if (filtered.length > 0) {
    filtered.forEach(function(s) {
      var ce = s.command.replace(/'/g,"\\\\'");
      var ae = (s.alias||'').replace(/'/g,"\\\\'");
      html += '<div class="s2-item" onclick="fillCmd(\\''+ce+'\\')">';
      html += '<span class="s2-iico" style="color:#ffd740;">&#9733;</span>';
      if (s.alias) {
        html += '<span class="s2-alias">['+esc(s.alias)+']</span> ';
      }
      html += '<span class="s2-itxt">' + esc(s.command) + '</span>';
      html += '<button class="s2-iedit" onclick="editSavedAlias(\\''+ce+'\\',\\''+ae+'\\',event)" title="编辑别名">&#9998;</button>';
      html += '<button class="s2-idel" onclick="deleteSavedCmd(\\''+ce+'\\',event)" title="取消收藏">&times;</button>';
      html += '</div>';
    });
  } else {
    html += '<div class="s2-empty">' + (q ? '无匹配' : '点击 ★ 收藏命令') + '</div>';
  }
  body.innerHTML = html;
}

function renderHist() {
  var body = document.getElementById('histBody');
  var q = document.getElementById('histSearch').value.trim();
  var seen = {};
  var filtered = [];
  history.forEach(function(h) {
    if (!seen[h] && fuzzyMatch(q, h)) { filtered.push(h); seen[h]=true; }
  });
  document.getElementById('histCount').textContent = history.length;
  var html = '';
  if (filtered.length > 0) {
    filtered.forEach(function(h) {
      html += '<div class="s2-item" onclick="fillCmd(\\''+h.replace(/'/g,"\\\\'")+'\\')">';
      html += '<span class="s2-iico" style="color:#82b1ff;">&#128339;</span>';
      html += '<span class="s2-itxt">' + esc(h) + '</span>';
      html += '</div>';
    });
  } else {
    html += '<div class="s2-empty">' + (q ? '无匹配' : '执行命令后自动记录') + '</div>';
  }
  body.innerHTML = html;
}

function fillCmd(cmd) {
  document.getElementById('cmdInput').value = cmd;
  document.getElementById('cmdInput').focus();
  document.querySelectorAll('.s2-box.open').forEach(function(b) { b.classList.remove('open'); });
}

function toggleS2(id) {
  var el = document.getElementById(id);
  var wasOpen = el.classList.contains('open');
  document.querySelectorAll('.s2-box.open').forEach(function(b) { b.classList.remove('open'); });
  if (!wasOpen) {
    el.classList.add('open');
    var si = el.querySelector('.s2-search');
    if (si) { si.value = ''; si.focus(); }
    if (id === 's2Saved') renderSaved();
    else renderHist();
  }
}

document.addEventListener('mousedown', function(e) {
  document.querySelectorAll('.s2-box.open').forEach(function(box) {
    if (!box.contains(e.target)) box.classList.remove('open');
  });
});

const cmdInput = document.getElementById('cmdInput');
cmdInput.addEventListener('keydown', function(e) {
  if (e.key === 'Enter') { executeFromInput(); }
  else if (e.key === 'Tab') {
    e.preventDefault();
    var val = cmdInput.value.trim();
    var allNames = [];
    Object.keys(commands).forEach(function(n) { allNames.push(n.replace(/_/g,'-')); });
    var matches = allNames.filter(function(n){return n.startsWith(val);});
    if (matches.length === 1) cmdInput.value = matches[0] + ' ';
  }
});

Promise.all([loadHistory(), loadSavedCmds()]).then(function() { renderSaved(); renderHist(); });
loadCommands();
loadInitParams();

(function() {
  var resizer = document.getElementById('resizer');
  var left = document.querySelector('.left-panel');
  var main = document.querySelector('.main');
  var dragging = false;
  resizer.addEventListener('mousedown', function(e) {
    dragging = true;
    resizer.classList.add('active');
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none';
    e.preventDefault();
  });
  document.addEventListener('mousemove', function(e) {
    if (!dragging) return;
    var rect = main.getBoundingClientRect();
    var offset = e.clientX - rect.left;
    var pct = (offset / rect.width) * 100;
    if (pct < 15) pct = 15;
    if (pct > 80) pct = 80;
    left.style.width = pct + '%';
  });
  document.addEventListener('mouseup', function() {
    if (!dragging) return;
    dragging = false;
    resizer.classList.remove('active');
    document.body.style.cursor = '';
    document.body.style.userSelect = '';
  });
})();
</script>
</body>
</html>'''

`````

--- **end of file: nb_cmd/modes/web_mode.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/modes/__init__.py** (project: nb_cmd) --- 

`````python

`````

--- **end of file: nb_cmd/modes/__init__.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/ui/colors.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
彩色终端输出，纯标准库实现，无外部依赖。
在不支持 ANSI 的终端上自动降级为无色输出。
"""
import os
import sys


def _supports_color():
    """检测当前终端是否支持 ANSI 颜色"""
    if os.getenv('NO_COLOR'):
        return False
    if os.getenv('FORCE_COLOR'):
        return True
    if not hasattr(sys.stdout, 'isatty'):
        return False
    if not sys.stdout.isatty():
        return False
    if sys.platform == 'win32':
        return os.getenv('ANSICON') is not None or 'WT_SESSION' in os.environ or os.getenv('TERM_PROGRAM') == 'vscode'
    return True


_COLOR_ENABLED = _supports_color()

_COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
}


def _colorize(text, color_name):
    if not _COLOR_ENABLED:
        return text
    color_code = _COLORS.get(color_name, '')
    reset = _COLORS['reset']
    return '{}{}{}'.format(color_code, text, reset)


def print_success(msg):
    sys.stdout.write(_colorize('[OK] {}'.format(msg), 'bright_green') + '\n')
    sys.stdout.flush()


def print_warning(msg):
    sys.stdout.write(_colorize('[WARN] {}'.format(msg), 'bright_yellow') + '\n')
    sys.stdout.flush()


def print_error(msg):
    sys.stderr.write(_colorize('[ERROR] {}'.format(msg), 'bright_red') + '\n')
    sys.stderr.flush()


def print_info(msg):
    sys.stdout.write(_colorize('[INFO] {}'.format(msg), 'bright_blue') + '\n')
    sys.stdout.flush()

`````

--- **end of file: nb_cmd/ui/colors.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/ui/helper.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
UI 工具方法集合 —— cmdui 单例的实现。

通过 ``from nb_cmd import cmdui`` 导入使用。
"""
import json
import sys

from .colors import print_success, print_warning, print_error, print_info
from .table import print_table, print_kv
from .progress import progress as _progress_iter


class UIHelper(object):
    """
    NbCmd 的 UI 工具方法集合。

    通过 ``from nb_cmd import cmdui`` 导入使用，避免与用户自定义的子命令方法名冲突。
    包含: 输出(table/kv/tree/json_print)、彩色(success/warning/error/info)、
          交互(confirm/prompt/select)、进度(progress) 等工具。
    """

    def table(self, data, headers=None):
        """表格输出"""
        print_table(data, headers)

    def kv(self, data):
        """键值对输出"""
        print_kv(data)

    def tree(self, data, prefix='', is_last=True):
        """树形输出"""
        if isinstance(data, dict):
            items = list(data.items())
            for i, (key, value) in enumerate(items):
                last = (i == len(items) - 1)
                connector = '└── ' if last else '├── '
                if isinstance(value, dict):
                    sys.stdout.write('{}{}{}\n'.format(prefix, connector, key))
                    extension = '    ' if last else '│   '
                    self.tree(value, prefix + extension, last)
                else:
                    sys.stdout.write('{}{}{}: {}\n'.format(prefix, connector, key, value))

    def json_print(self, data):
        """JSON美化输出"""
        sys.stdout.write(json.dumps(data, ensure_ascii=False, indent=2, default=str) + '\n')
        sys.stdout.flush()

    def progress(self, iterable, desc=None, total=None):
        """进度条迭代器"""
        return _progress_iter(iterable, desc=desc, total=total)

    def confirm(self, message):
        """确认提示，返回 True/False"""
        try:
            answer = input('{} [y/N]: '.format(message)).strip().lower()
            return answer in ('y', 'yes')
        except (EOFError, KeyboardInterrupt):
            return False

    def prompt(self, message, default=None):
        """输入提示"""
        try:
            if default is not None:
                answer = input('{} [{}]: '.format(message, default)).strip()
                return answer if answer else default
            else:
                return input('{}: '.format(message)).strip()
        except (EOFError, KeyboardInterrupt):
            return default

    def select(self, message, choices):
        """选择提示"""
        sys.stdout.write(message + '\n')
        for i, choice in enumerate(choices):
            sys.stdout.write('  {}. {}\n'.format(i + 1, choice))
        sys.stdout.flush()
        try:
            idx = int(input('请选择 [1-{}]: '.format(len(choices))).strip()) - 1
            if 0 <= idx < len(choices):
                return choices[idx]
        except (ValueError, EOFError, KeyboardInterrupt):
            pass
        return choices[0] if choices else None

    def success(self, msg):
        """绿色成功信息"""
        print_success(msg)

    def warning(self, msg):
        """黄色警告信息"""
        print_warning(msg)

    def error(self, msg):
        """红色错误信息"""
        print_error(msg)

    def info(self, msg):
        """蓝色信息"""
        print_info(msg)


cmdui = UIHelper()

`````

--- **end of file: nb_cmd/ui/helper.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/ui/progress.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
纯标准库的进度条实现，无外部依赖。
"""
import sys
import time


class ProgressBar(object):
    """简易进度条，兼容 Python 3.7+"""

    def __init__(self, iterable=None, desc=None, total=None, bar_width=30, file=None):
        self.iterable = iterable
        self.desc = desc or ''
        self.bar_width = bar_width
        self.file = file or sys.stderr

        if total is not None:
            self.total = total
        elif iterable is not None:
            try:
                self.total = len(iterable)
            except TypeError:
                self.total = None
        else:
            self.total = None

        self.n = 0
        self.start_time = None

    def __iter__(self):
        self.start_time = time.time()
        self.n = 0
        for item in self.iterable:
            yield item
            self.n += 1
            self._display()
        self._display(final=True)
        self.file.write('\n')
        self.file.flush()

    def _display(self, final=False):
        elapsed = time.time() - self.start_time if self.start_time else 0

        if self.total and self.total > 0:
            frac = self.n / self.total
            percent = int(frac * 100)
            filled = int(self.bar_width * frac)
            bar = '█' * filled + '░' * (self.bar_width - filled)

            if elapsed > 0 and self.n > 0:
                rate = self.n / elapsed
                remaining = (self.total - self.n) / rate if rate > 0 else 0
                eta_str = _format_time(remaining)
                elapsed_str = _format_time(elapsed)
            else:
                eta_str = '?'
                elapsed_str = '00:00'

            line = '\r{} {} {}% {}/{} [{}<{}]'.format(
                self.desc, bar, percent, self.n, self.total,
                elapsed_str, eta_str
            )
        else:
            line = '\r{} {} 项已处理 [{:.1f}s]'.format(
                self.desc, self.n, elapsed
            )

        self.file.write(line)
        self.file.flush()


def _format_time(seconds):
    if seconds < 60:
        return '{:02d}:{:02d}'.format(0, int(seconds))
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    if minutes < 60:
        return '{:02d}:{:02d}'.format(minutes, secs)
    hours = minutes // 60
    minutes = minutes % 60
    return '{:d}:{:02d}:{:02d}'.format(hours, minutes, secs)


def progress(iterable, desc=None, total=None):
    """便捷函数：返回带进度条的可迭代对象"""
    return ProgressBar(iterable=iterable, desc=desc, total=total)

`````

--- **end of file: nb_cmd/ui/progress.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/ui/table.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
纯标准库的表格输出，支持 CJK 字符对齐。
"""
import sys


def _write(text):
    sys.stdout.write(text + '\n')
    sys.stdout.flush()


def _display_width(text):
    width = 0
    for ch in str(text):
        code = ord(ch)
        if (0x4E00 <= code <= 0x9FFF) or (0x3400 <= code <= 0x4DBF) or \
           (0xF900 <= code <= 0xFAFF) or (0xFF00 <= code <= 0xFFEF) or \
           (0x3000 <= code <= 0x303F):
            width += 2
        else:
            width += 1
    return width


def _pad(text, width):
    text = str(text)
    dw = _display_width(text)
    return text + ' ' * max(0, width - dw)


def print_table(data, headers=None):
    """
    将 list[dict] 或 list[list] 格式化为表格输出。

    Parameters
    ----------
    data : list[dict] 或 list[list]
    headers : list[str], optional
    """
    if not data:
        _write('(空)')
        return

    if isinstance(data[0], dict):
        if headers is None:
            headers = list(data[0].keys())
        rows = [[row.get(h, '') for h in headers] for row in data]
    else:
        if headers is None:
            headers = ['列{}'.format(i + 1) for i in range(len(data[0]))]
        rows = data

    col_widths = [_display_width(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            w = _display_width(str(val))
            if w > col_widths[i]:
                col_widths[i] = w

    top = '┌' + '┬'.join('─' * (w + 2) for w in col_widths) + '┐'
    mid = '├' + '┼'.join('─' * (w + 2) for w in col_widths) + '┤'
    bot = '└' + '┴'.join('─' * (w + 2) for w in col_widths) + '┘'

    header_line = '│ ' + ' │ '.join(_pad(str(h), col_widths[i]) for i, h in enumerate(headers)) + ' │'

    _write(top)
    _write(header_line)
    _write(mid)
    for row in rows:
        line = '│ ' + ' │ '.join(_pad(str(row[i]) if i < len(row) else '', col_widths[i]) for i in range(len(headers))) + ' │'
        _write(line)
    _write(bot)


def print_kv(data):
    """
    键值对格式化输出。

    Parameters
    ----------
    data : dict
    """
    if not data:
        return

    max_key_width = max(_display_width(str(k)) for k in data.keys())

    for key, value in data.items():
        padded_key = _pad(str(key), max_key_width)
        _write('{}:  {}'.format(padded_key, value))

`````

--- **end of file: nb_cmd/ui/table.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/ui/__init__.py** (project: nb_cmd) --- 

`````python

`````

--- **end of file: nb_cmd/ui/__init__.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/utils/config.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
参数持久化模块 —— 自动保存/恢复上一次执行的参数。
"""
import json
import os


class ConfigManager(object):
    """管理参数持久化到 JSON 文件"""

    def __init__(self, config_file=None):
        if config_file:
            self.config_file = os.path.expanduser(config_file)
        else:
            self.config_file = None
        self._data = {}
        if self.config_file:
            self._load()

    def _load(self):
        if self.config_file and os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self._data = json.load(f)
            except Exception:
                self._data = {}

    def save_args(self, command, kwargs):
        """保存命令的参数"""
        if not self.config_file:
            return
        serializable = {}
        for k, v in kwargs.items():
            try:
                json.dumps(v)
                serializable[k] = v
            except (TypeError, ValueError):
                serializable[k] = str(v)
        self._data[command] = serializable
        self._write()

    def load_args(self, command):
        """加载命令上次保存的参数"""
        return self._data.get(command, {})

    def _write(self):
        if not self.config_file:
            return
        dir_path = os.path.dirname(self.config_file)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

`````

--- **end of file: nb_cmd/utils/config.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/utils/validators.py** (project: nb_cmd) --- 

`````python
# -*- coding: utf-8 -*-
"""
参数校验装饰器。
"""
import functools


def validate(**validators):
    """
    参数校验装饰器。
    每个关键字参数是一个 lambda/callable，接收参数值，返回 True/False。

    示例::

        @validate(port=lambda x: 1 <= x <= 65535)
        def deploy(self, host: str, port: int = 22):
            ...

    校验失败时抛出 ValueError。
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for param_name, check_fn in validators.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not check_fn(value):
                        raise ValueError(
                            '参数 {} 校验失败 (当前值: {})'.format(param_name, value)
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator

`````

--- **end of file: nb_cmd/utils/validators.py** (project: nb_cmd) --- 

---


--- **start of file: nb_cmd/utils/__init__.py** (project: nb_cmd) --- 

`````python

`````

--- **end of file: nb_cmd/utils/__init__.py** (project: nb_cmd) --- 

---

