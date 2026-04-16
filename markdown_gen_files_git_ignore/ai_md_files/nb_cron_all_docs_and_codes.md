
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
# markdown content namespace: nb_cron project summary 



- `nb_cron` is a powerful cron library for Python.
- `NbCron(...)` is the main class to create a cron object. 


## 📋 nb_cron most core source files metadata (Entry Points)


以下是项目 nb_cron 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nb_cron most core source code files as follows: 
- `nb_cron/__init__.py`
- `nb_cron/core/scheduler.py`


### 📄 Python File Metadata: `nb_cron/__init__.py`

#### 📝 Module Docstring

`````
nb_cron - A powerful and simple cron job scheduler that dominates APScheduler.

Usage::

    from nb_cron import NbCron, cron_register, explain_cron

    cron = NbCron("my_project")  # name 必传，隔离不同项目

    @cron.job("0 */5 * * * *")
    @cron_register('my_task')
    def my_task():
        print("every 5 minutes")

    cron.start()  # 不阻塞，Ctrl+C 退出
`````

#### 📦 Imports

- `from nb_cron._version import __version__`
- `from nb_cron.core.registry import add_cron_register`
- `from nb_cron.core.registry import cron_register`
- `from nb_cron.core.scheduler import NbCron`
- `from nb_cron.cron_utils.translator import explain_cron`
- `from nb_cron.executors.base_executor import BaseExecutor`
- `from nb_cron.executors.thread_executor import ThreadExecutor`


---




### 📄 Python File Metadata: `nb_cron/core/scheduler.py`

#### 📦 Imports

- `import logging`
- `import re`
- `import signal`
- `import threading`
- `import time`
- `from datetime import datetime`
- `from datetime import timedelta`
- `from typing import Callable`
- `from typing import List`
- `from typing import Optional`
- `from typing import Union`
- `from nb_cron.core.job import Job`
- `from nb_cron.core.registry import FunctionRegistry`
- `from nb_cron.executors.base_executor import BaseExecutor`
- `from nb_cron.executors.threadpool import _ExecutionResult`
- `from nb_cron.executors.thread_executor import ThreadExecutor`
- `from nb_cron.locks.base import BaseLock`
- `from nb_cron.locks.memory_lock import MemoryLock`
- `from nb_cron.metrics.collector import MetricsCollector`
- `from nb_cron.stores.base import BaseStore`
- `from nb_cron.stores.memory import MemoryStore`
- `from nb_cron.triggers.base import BaseTrigger`
- `from nb_cron.triggers.cron_trigger import CronTrigger`
- `from nb_cron.triggers.date_trigger import DateTrigger`
- `from nb_cron.triggers.interval_trigger import IntervalTrigger`
- `from nb_cron.utils import get_local_timezone`
- `from nb_cron.utils import now as _now`
- `from nb_cron.stores.sqlalchemy_store import SQLAlchemyStore`
- `from nb_cron.locks.sqlalchemy_lock import SQLAlchemyLock`
- `from nb_cron.stores.redis_store import RedisStore`
- `from nb_cron.stores.mongo_store import MongoStore`
- `from nb_cron.locks.redis_lock import RedisLock`
- `from nb_cron.locks.mongo_lock import MongoLock`

#### 🏛️ Classes (1)

##### 📌 `class NbCron`
*Line: 107*

**Docstring:**
`````
The one and only scheduler class you need.

Usage::

    from nb_cron import NbCron, cron_register

    cron = NbCron("my_project")  # name 必传，隔离不同项目
    # cron = NbCron("my_project", "redis://localhost:6379/0")

    @cron.job("0 */5 * * * *")
    @cron_register('report')
    def task_a(): ...

    cron.start()  # 不阻塞，Ctrl+C 退出
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, name: str, store_url: Optional[str] = None, max_workers: int = 20, tick_seconds: float = 1.0, misfire_grace_seconds: int = 60, tz = None, executor: Optional[BaseExecutor] = None)`
  - **Parameters:**
    - `self`
    - `name: str`
    - `store_url: Optional[str] = None`
    - `max_workers: int = 20`
    - `tick_seconds: float = 1.0`
    - `misfire_grace_seconds: int = 60`
    - `tz = None`
    - `executor: Optional[BaseExecutor] = None`

**Public Methods (11):**
- `def job(self, expression: str) -> Callable`
  - **Docstring:**
  `````
  装饰器，注册定时任务。函数必须先用 @cron_register 注册。
  
  :param expression: 触发表达式
  :param trigger: "cron" / "interval" / "date"，不传则自动推断
  `````
- `def add_job(self, func: Union[Callable, str], expression: str) -> Job`
- `def start(self) -> None`
  - **Docstring:**
  `````
  启动调度器（非阻塞，立即返回）。
  
  - ``start()`` 后面的代码会继续执行。
  - 主线程跑完后进程**不会退出**，定时任务继续运行。
  - ``Ctrl+C`` 优雅停止。
  `````
- `def stop(self, wait: bool = True) -> None`
- `def is_running(self) -> bool`
- `def pause_job(self, job_id: str) -> None`
- `def resume_job(self, job_id: str) -> None`
- `def remove_job(self, job_id: str) -> None`
- `def trigger_job(self, job_id: str) -> None`
- `def get_jobs(self) -> List[Job]`
- `def get_job(self, job_id: str) -> Optional[Job]`


---



## 🔗 nb_cron Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Core Files (imported by other files, sorted by import count):
  ◆ nb_cron/__init__.py (imported by 1 files)
  ◆ nb_cron/core/scheduler.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `nb_cron/__init__.py`

**Imports from project:**
- `nb_cron/core/scheduler.py`

**Imported by:**
- `nb_cron/core/scheduler.py`

#### `nb_cron/core/scheduler.py`

**Imports from project:**
- `nb_cron/__init__.py`

**Imported by:**
- `nb_cron/__init__.py`


---
# markdown content namespace: nb_cron Project Root Dir Some Files 


## nb_cron File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## nb_cron (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: nb_cron) --- 

`````markdown

# 🚀 nb_cron

**下一代 Python 分布式定时任务框架（全面超越 APScheduler）**

nb_cron 是一个强大、极简且**专为云原生架构设计**的定时任务调度库。它不仅彻底解决了 APScheduler 常年存在的序列化崩溃、多实例重复执行等痛点，更在架构理念上实现了**“业务逻辑与调度配置的物理隔离”**，让 Python 定时任务的管理进入真正的现代化阶段。

### 🥊 核心痛点对决：APScheduler vs nb_cron

| 痛点场景 | 😭 APScheduler 的历史包袱 | 🤩 nb_cron 的现代解决方案 |
| :--- | :--- | :--- |
| **云原生多副本部署**<br>*(K8s/多容器)* | 致命弱点：多实例会**重复执行任务**，需手动硬编码第三方 Redis 锁，极易死锁。 | **天生云原生**：内置极其可靠的分布式锁（Redis/Mongo/SQL），天然支持 K8s 多副本平滑扩容，保证 **exactly-once**（绝不重复执行）。 |
| **微服务跨项目调度** | 强耦合：任务代码和调度器必须在同一个项目中，无法集中化管理。 | **跨 Git 项目可视化编排**：首创业务与调度解耦机制。A 项目只写函数，B 项目（调度中心）通过 Web UI 动态下发定时配置。 |
| **代码重构与序列化** | Pickle 地狱：存入 DB 的是函数内存地址，一旦代码重构（改名/移动文件路径），反序列化直接崩溃，任务全线瘫痪。 | **彻底抛弃 Pickle**：首创 `@cron_register` 稳定名称注册表，存入 DB 的仅是纯字符串。代码随便重构，只要名字在，任务照样跑。 |
| **可视化管理后台** | 官方**没有 UI**，想要启停任务、看日志只能自己从头手搓前后端。 | **原生自带 Web UI**：内置开箱即用的 Vue3 + Element Plus 现代化后台。**前端已预编译到 `nb_cron/web`，Python 开发者无需安装 Node.js 即可一键启动。** |
| **精度与时区** | Cron 不支持秒级精度；时区配置与 Misfire 策略行为混乱。 | **强制 6 字段 Cron**（支持秒级）；默认本地时区（可传 `tz`），Misfire 容忍策略极简可控。 |
| **多项目共享存储** | 多项目共用一个 Redis 时极易发生 Key 冲突，互相踩踏任务。 | **强制物理隔离**：初始化必须传 `name` 参数，按项目名称进行 Redis Key 的绝对隔离。 |
| **选择困难症** | 提供 7 种 Scheduler 类（Blocking, Background, AsyncIO...），新手永远选错。 | **大道至简**：全局只有一个 `NbCron` 类，永远在后台非阻塞运行，同时兼容同步与 `async` 异步函数。 |
| **集群分布式消费** | 只能在本地调度并执行，面对海量重计算任务力不从心。 | **一键变身分布式 MQ**：支持无缝切换至 `FunboostExecutor`，瞬间获得**失败重试、指数退避、超时杀死**等工业级分布式消息队列消费能力。 |

### ✨ 为什么 nb_cron 是“下一代”框架？

传统的定时任务框架，往往把**“业务代码”**和**“定时规则（如每天凌晨两点）”**死死绑在一起。
nb_cron 带来了全新的架构理念：

1. **配置即数据，无需重启服务**：通过 Web UI 随时修改任务的 Cron 表达式或启停任务，配置实时写入 Redis 并生效，你的业务进程**全程无需重启**。
2. **函数定义与任务调度的物理分离**：让后端开发人员只管专心写业务函数并打上 `@cron_register` 标记；让运维或运营人员在独立的 Web 页面上，通过下拉菜单选择已注册的函数，在nb_cron_ui 的前端去创建定时任务。


## 安装

> **⚠️ 重要提示**：PyPI 上的包名是 `nb_cron_nb`（不是 `nb_cron`），因为 `nb_cron` 已被他人占用。**代码中的 import 仍然是 `from nb_cron import ...`**，只是安装时用 `pip install nb_cron_nb`。

```bash
# 基础安装（内存存储）
pip install nb_cron_nb

# Redis 存储 + FastAPI Web（推荐，生产环境一行搞定）
pip install nb_cron_nb[redis,fastapi]

# Redis + Flask
pip install nb_cron_nb[redis,flask]

# 全部功能
pip install nb_cron_nb[all]
```

各可选组件：

| 组件 | 安装命令 | 说明 |
|---|---|---|
| redis | `pip install nb_cron_nb[redis]` | Redis 存储 + 分布式锁 |
| mongo | `pip install nb_cron_nb[mongo]` | MongoDB 存储 + 分布式锁 |
| sqlalchemy | `pip install nb_cron_nb[sqlalchemy]` | SQLite/MySQL/PostgreSQL 存储 |
| fastapi | `pip install nb_cron_nb[fastapi]` | FastAPI Web 框架集成 |
| flask | `pip install nb_cron_nb[flask]` | Flask Web 框架集成 |
| django | `pip install nb_cron_nb[django]` | Django + Ninja 框架集成 |

## 快速开始

### 最简用法

```python
from nb_cron import NbCron, cron_register

cron = NbCron("my_project")  # name 必传，隔离不同项目

@cron.job("0 */5 * * * *")  # 每5分钟执行（6字段：秒 分 时 日 月 周）
@cron_register('my_task')   # 必须注册稳定名称
def my_task():
    print("Hello nb_cron!")

cron.start()  # 不阻塞，定时任务后台运行，进程不会退出
```

### 完整示例

```python
from datetime import timedelta, timezone
from nb_cron import NbCron, cron_register, add_cron_register, explain_cron

# 创建调度器（name 必传，选一个存储后端）
cron = NbCron("my_project")                                      # 内存存储
# cron = NbCron("my_project", "redis://localhost:6379/0")         # Redis（推荐）
# cron = NbCron("my_project", tz=timezone(timedelta(hours=8)))    # 指定东八区
# cron = NbCron("my_project", tz=timezone.utc)                    # UTC

# ── 装饰器方式（@cron_register 在下，@cron.job 在上） ──

# 无参数任务
@cron.job("0 */5 * * * *")
@cron_register('report')
def report_task():
    print("生成报告")

# 有参数任务（必须在装饰器中传 args/kwargs）
@cron.job("0 30 9 * * * *", args=("admin@example.com",), kwargs={"report_type": "daily"})
@cron_register('send_report_email')
def send_report_email(to_address: str, report_type: str = "daily"):
    print(f"发送{report_type}报表到 {to_address}")

# 有参数任务（装饰器中直接传参）
@cron.job("0 0 2 * * *", args=("backup_db",), kwargs={"compress": True})
@cron_register('backup')
def backup_database(db_name: str, compress: bool = False):
    print(f"备份数据库 {db_name}, 压缩={compress}")

# 异步任务也支持
@cron.job("30 0 9 * * 1-5", trigger="cron")
@cron_register('async_work')
async def async_task():
    print("异步任务也支持！")

# 间隔任务
@cron.job("@every 30s", trigger="interval")
@cron_register('heartbeat')
def heartbeat():
    print("心跳")

# 日期任务（一次性）
@cron.job("2026-10-01 09:00:00", trigger="date")
@cron_register('national_day')
def national_day_task():
    print("国庆节任务")

# ── 非装饰器写法（适合第三方函数或动态注册） ──

# 方式 1：add_cron_register + add_job
def send_sms(phone: str, message: str):
    """发送短信（第三方函数）"""
    print(f"发送短信到 {phone}: {message}")

add_cron_register('send_sms', send_sms)
cron.add_job(
    'send_sms',
    "0 0 8 * * *",
    trigger="cron",
    job_id="morning_sms",
    name="早安短信",
    args=("13800138000", "早上好！"),
)

# 方式 2：直接 add_job（自动注册）
from nb_cron import cron_register

def cleanup_logs(days: int = 7):
    """清理日志"""
    print(f"清理{days}天前的日志")

cron_register('cleanup_logs', cleanup_logs)
cron.add_job(
    cleanup_logs,  # 传函数对象
    "0 0 3 * * 0",
    trigger="cron",
    job_id="weekly_cleanup",
    name="每周清理",
    kwargs={"days": 30},  # 覆盖默认参数
)

# 方式 3：批量注册任务
def process_order(order_id: int):
    """处理订单"""
    print(f"处理订单 {order_id}")

add_cron_register('process_order', process_order)

# 动态添加多个不同参数的任务
cron.add_job('process_order', "@every 5m", job_id="process_order_batch1", args=(1001,))
cron.add_job('process_order', "@every 5m", job_id="process_order_batch2", args=(1002,))
cron.add_job('process_order', "@every 5m", job_id="process_order_batch3", args=(1003,))

# ── 启动 ──
cron.start()

# ── 管理 ──
cron.pause_job("daily_backup")
cron.resume_job("daily_backup")
cron.trigger_job("daily_backup")
cron.remove_job("daily_backup")
jobs = cron.get_jobs()

# ── Cron 翻译 ──
print(explain_cron("0 30 9 * * *", "zh"))    # "每天 09:30:00 执行"
print(explain_cron("0 30 9 * * *", "en"))    # "At 09:30:00, every day"
```

---

## 项目隔离（name 参数）

`NbCron` 的第一个参数 `name` 是**必传**的，用于隔离不同项目的数据：

- **Redis**: keys 格式为 `nb_cron:{name}:jobs`、`nb_cron:{name}:metrics`、`nb_cron:{name}:due`、`nb_cron:{name}:lock:*`
- **MongoDB**: collections 为 `nb_cron_{name}_jobs`、`nb_cron_{name}_metrics`、`nb_cron_{name}_locks`
- **SQLAlchemy**: 表名为 `nb_cron_{name}_jobs`、`nb_cron_{name}_metrics`、`nb_cron_{name}_locks`
- **Web UI**: 侧边栏标题显示 `name`，方便区分

```python
# 同一个 Redis，不同项目互不干扰
cron_a = NbCron("billing_service", "redis://localhost:6379/0")
cron_b = NbCron("user_service", "redis://localhost:6379/0")

# cron_a 只看到 billing_service:jobs 下的任务
# cron_b 只看到 user_service:jobs 下的任务
```

不传 `name` 或传空字符串会直接报错：

```python
NbCron("")   # ValueError: NbCron name 不能为空
NbCron()     # TypeError: missing required argument 'name'
```

---

## 时区支持

nb_cron 默认使用**本地时区**。所有时间（`next_run_time`、日期表达式解析等）都基于调度器的时区。

```python
from datetime import timedelta, timezone

# 默认：本地时区（推荐）
cron = NbCron("my_project")

# 显式指定时区
cron = NbCron("my_project", tz=timezone(timedelta(hours=8)))   # 东八区
cron = NbCron("my_project", tz=timezone.utc)                   # UTC

# Python 3.9+ 可用 zoneinfo
from zoneinfo import ZoneInfo
cron = NbCron("my_project", tz=ZoneInfo("Asia/Shanghai"))
```

`tz` 参数接受任何 `datetime.tzinfo` 对象。

---

## 三种触发器类型

nb_cron 支持三种触发器类型，通过 `trigger` 参数显式指定（也可以不传，自动推断）：

| trigger 值 | 含义 | expression 示例 |
|---|---|---|
| `"cron"` | 6 字段 cron 表达式 | `"0 */5 * * * *"` |
| `"interval"` | 固定间隔重复执行 | `"@every 30s"`, `"5m"`, `"2h"` |
| `"date"` | 指定时间执行一次 | `"2026-10-01 09:00:00"`, `"2026年10月01日"` |

### 自动推断 vs 显式指定

```python
# 自动推断（不传 trigger，nb_cron 自动判断）
@cron.job("0 */5 * * * *")              # → cron
@cron.job("@every 30s")                 # → interval
@cron.job("2026-10-01 09:00:00")        # → date

# 显式指定（推荐，语义更清晰）
@cron.job("0 */5 * * * *", trigger="cron")
@cron.job("@every 30s", trigger="interval")
@cron.job("2026-10-01 09:00:00", trigger="date")

# trigger="interval" 时支持简写（不需要 @every 前缀）
@cron.job("30s", trigger="interval")     # 等价于 @every 30s
@cron.job("5m", trigger="interval")      # 等价于 @every 5m
@cron.job("2h", trigger="interval")      # 等价于 @every 2h
```

> **注意：** 以上所有 `@cron.job` 下面都需要 `@cron_register('名称')` 装饰器。

---

## 函数注册（强制）

nb_cron **强制要求**所有定时函数必须通过 `@cron_register` 注册一个**稳定名称**（`cron_func_name`）。
这确保函数标识不依赖文件路径——重命名文件、移动函数不会影响调度。

```python
from nb_cron import cron_register, add_cron_register

# 装饰器注册
@cron_register('daily_backup')
def backup_db():
    print("备份")

backup_db.cron_func_name  # → 'daily_backup'  （IDE 可补全）

# 函数调用注册（适合第三方函数）
def send_email():
    print("发邮件")
add_cron_register('send_email', send_email)

# 也支持 cron_register 两参数形式
cron_register('send_email', send_email)
```

### 与 `@cron.job` 配合

`@cron_register` 放下面（靠近函数），`@cron.job` 放上面：

```python
@cron.job("0 0 2 * * *", trigger="cron")     # 第二步：读 .cron_func_name，注册调度
@cron_register('daily_backup')                # 第一步：设 .cron_func_name，注册函数
def backup_db():
    print("备份")
```

### `add_job` 三种传参方式

```python
# 1. 传函数对象（自动读 .cron_func_name）
cron.add_job(backup_db, "0 0 2 * * *", trigger="cron")

# 2. 传注册名字符串
cron.add_job('daily_backup', "0 0 2 * * *", trigger="cron")

# 3. 传 .cron_func_name（IDE 安全，等价于方式 2）
cron.add_job(backup_db.cron_func_name, "0 0 2 * * *", trigger="cron")

# 4. 带参数的任务（args 和 kwargs）
def send_email(to: str, subject: str, body: str = ""):
    print(f"发送邮件到 {to}: {subject}")

cron_register('send_email', send_email)

# 在装饰器中传参
@cron.job("0 9 * * * *", args=("admin@example.com", "日报"), kwargs={"body": "这是日报内容"})
@cron_register('daily_report_email')
def daily_report_email(to: str, subject: str, body: str = ""):
    print(f"发送日报到 {to}")

# 或在 add_job 中传参
cron.add_job(
    'send_email',
    "0 9 * * * *",
    trigger="cron",
    job_id="morning_email",
    args=("user@example.com", "晨报"),
    kwargs={"body": "这是晨报内容"},
)

# 5. 批量添加同函数不同参数的任务
def process_batch(batch_id: int):
    print(f"处理批次 {batch_id}")

cron_register('process_batch', process_batch)
cron.add_job('process_batch', "@every 10m", job_id="batch_1", args=(1,))
cron.add_job('process_batch', "@every 10m", job_id="batch_2", args=(2,))
cron.add_job('process_batch', "@every 10m", job_id="batch_3", args=(3,))
```

### 未注册直接报错

```python
@cron.job("0 */5 * * * *")
def simple_task():          # ❌ ValueError: 函数 'simple_task' 未注册 cron_func_name
    pass
```

---

## 函数找不到的处理

如果 Redis 中存储了某个 job 但对应的定时函数没有被导入或已被删除：

- **失败次数 +1**（计入 metrics）
- **job 状态变为 `error`**
- **前端显示红色"异常"标签**，不再显示"运行中"误导用户
- **日志打印 ERROR 级别信息**
- **继续调度**（下次触发时再次尝试，便于热修复后自动恢复）

---

## Web UI 管理后台（重点）

nb_cron 自带漂亮的管理后台，包含：
- **仪表盘**：任务总数、运行中/已暂停/异常卡片、24小时执行趋势图、成功率饼图
- **任务管理**：列表搜索/筛选、暂停/恢复/立即执行/删除操作、新建任务对话框
- **任务详情**：执行指标图表、最近10次执行记录、错误日志
- **Cron 工具**：Cron 表达式翻译器
- **中英文切换**

支持 **FastAPI、Flask、Django** 三种框架一键启动。

---

### 方式一：FastAPI 启动（推荐）

```bash
pip install nb_cron_nb[redis,fastapi]
```

创建 `app.py`：

```python
from nb_cron import NbCron, cron_register
from nb_cron.web import get_fastapi_app

cron = NbCron("my_project", "redis://localhost:6379/0")

# 无参数任务
@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat():
    print("heartbeat OK")

# 有参数任务（必须在装饰器中传 args/kwargs）
@cron.job("0 */5 * * * *", trigger="cron", name="数据同步", args=(), kwargs={"source": "mysql", "target": "redis"})
@cron_register('sync_data')
def sync_data(source: str = "mysql", target: str = "redis"):
    print(f"sync from {source} to {target}")

# 有参数任务（装饰器中传参）
@cron.job("0 30 2 * * *", trigger="cron", name="每日备份", args=("prod_db",), kwargs={"compress": True})
@cron_register('daily_backup')
def daily_backup(db_name: str, compress: bool = False):
    print(f"backup {db_name}, compress={compress}")

# 非装饰器写法：第三方函数
def send_email(to: str, subject: str, body: str):
    """发送邮件（第三方库函数）"""
    print(f"邮件已发送到 {to}: {subject}")

cron_register('send_email', send_email)
cron.add_job(
    'send_email',
    "0 0 9 * * 1-5",
    trigger="cron",
    job_id="morning_report_email",
    name="晨报邮件",
    args=("admin@example.com", "每日晨报", "这是晨报内容"),
)

# 批量添加同函数不同参数的任务
def process_queue(queue_name: str):
    """处理队列"""
    print(f"processing queue: {queue_name}")

cron_register('process_queue', process_queue)
cron.add_job('process_queue', "@every 1m", job_id="process_queue_1", args=("queue_1",))
cron.add_job('process_queue', "@every 1m", job_id="process_queue_2", args=("queue_2",))
cron.add_job('process_queue', "@every 1m", job_id="process_queue_3", args=("queue_3",))

app = get_fastapi_app(cron)

@app.on_event("startup")
def startup():
    cron.start()

@app.on_event("shutdown")
def shutdown():
    cron.stop()
```

启动：

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

打开浏览器访问：

| 地址 | 说明 |
|---|---|
| http://localhost:8000/nb_cron/ui/ | 管理后台 UI 页面 |
| http://localhost:8000/nb_cron/api/jobs | REST API - 任务列表 |
| http://localhost:8000/nb_cron/api/health | 健康检查（含时区信息） |
| http://localhost:8000/nb_cron/api/dashboard/stats | 仪表盘统计数据 |
| http://localhost:8000/nb_cron/api/cron/explain?expression=0+*/5+*+*+*+* | Cron 翻译 |
| http://localhost:8000/docs | FastAPI 自动生成的 Swagger 文档 |

---

### 方式二：Flask 启动

```bash
pip install nb_cron_nb[redis,flask]
```

创建 `app.py`：

```python
from nb_cron import NbCron, cron_register
from nb_cron.web import get_flask_app

cron = NbCron("my_project", "redis://localhost:6379/0")

# 无参数任务
@cron.job("*/10 * * * * *", trigger="cron", name="心跳")
@cron_register('heartbeat')
def heartbeat():
    print("heartbeat OK")

# 有参数任务（必须在装饰器中传 args/kwargs）
@cron.job("0 */5 * * * *", trigger="cron", name="同步", kwargs={"source": "mysql", "target": "redis"})
@cron_register('sync_data')
def sync_data(source: str = "mysql", target: str = "redis"):
    print(f"sync from {source} to {target}")

# 非装饰器写法
def cleanup(days: int = 7):
    """清理日志"""
    print(f"cleanup logs older than {days} days")

cron_register('cleanup', cleanup)
cron.add_job(
    'cleanup',
    "0 0 3 * * 0",
    trigger="cron",
    job_id="weekly_cleanup",
    name="每周清理",
    kwargs={"days": 30},
)

app = get_flask_app(cron)

if __name__ == "__main__":
    cron.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
```

启动：

```bash
# 开发模式
python app.py

# 生产模式（注意: 只用 1 个 worker，或用 Redis 存储自动防重复）
gunicorn app:app -w 1 -b 0.0.0.0:5000
```

访问 http://localhost:5000/nb_cron/ui/

---

### 方式三：Django 启动

```bash
pip install nb_cron_nb[redis,django]
```

**Step 1** — 创建调度器配置文件 `your_project/cron_config.py`：

```python
from nb_cron import NbCron, cron_register

cron = NbCron("my_project", "redis://localhost:6379/0")

# 无参数任务
@cron.job("*/10 * * * * *", trigger="cron", name="心跳")
@cron_register('heartbeat')
def heartbeat():
    print("heartbeat OK")

# 有参数任务（必须在装饰器中传 args/kwargs）
@cron.job("0 */5 * * * *", trigger="cron", name="同步", kwargs={"source": "mysql", "target": "redis"})
@cron_register('sync_data')
def sync_data(source: str = "mysql", target: str = "redis"):
    print(f"sync from {source} to {target}")

# 非装饰器写法：批量添加任务
def process_order(order_id: int):
    """处理订单"""
    print(f"processing order {order_id}")

cron_register('process_order', process_order)
cron.add_job('process_order', "@every 5m", job_id="process_order_1", args=(1001,))
cron.add_job('process_order', "@every 5m", job_id="process_order_2", args=(1002,))
cron.add_job('process_order', "@every 5m", job_id="process_order_3", args=(1003,))
```

**Step 2** — 在 `urls.py` 中挂载路由：

```python
from django.contrib import admin
from django.urls import path
from your_project.cron_config import cron
from nb_cron.web import get_django_urls

urlpatterns = [
    path('admin/', admin.site.urls),
] + get_django_urls(cron)
```

**Step 3** — 在 `apps.py` 中启动调度器（防止 reload 重复启动）：

```python
import os
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'true':
            from your_project.cron_config import cron
            cron.start()
```

启动：

```bash
python manage.py runserver 0.0.0.0:8000
```

访问 http://localhost:8000/nb_cron/ui/

---

## 前端 UI 构建说明

nb_cron 的管理后台前端源码位于 `nb_cron_ui/` 目录，使用以下技术栈：

- **Vue 3** — 响应式前端框架
- **Element Plus** — UI 组件库
- **ECharts** — 图表库
- **Pinia** — 状态管理
- **Vue I18n** — 中英文国际化
- **Vue Router** — 路由管理
- **Vite** — 构建工具

### 构建前端（发布前必须执行）

```bash
cd nb_cron_ui
npm install          # 安装依赖
npm run build        # 编译，输出到 nb_cron/web/static/
```

构建完成后，`nb_cron/web/static/` 目录下会生成 `index.html` 和 `assets/` 目录，
Python 后端会自动读取并在 `/nb_cron/ui/` 路径下提供服务。

### 前端开发模式

如果你要修改前端代码：

```bash
# 终端 1：启动后端 API（以 FastAPI 为例）
uvicorn your_app:app --port 8000

# 终端 2：启动前端开发服务器（自动代理 API 到 8000 端口）
cd nb_cron_ui
npm run dev
```

Vite 开发服务器会自动将 `/nb_cron/api/` 请求代理到 `http://localhost:8000`，
实现前后端分离开发、热更新。

### 前端目录结构

```
nb_cron_ui/
├── package.json              # 依赖配置
├── vite.config.js            # Vite 配置（base路径、构建输出、API代理）
├── index.html                # 入口 HTML
├── src/
│   ├── main.js               # Vue 应用入口
│   ├── App.vue               # 根组件
│   ├── router/index.js       # 路由配置
│   ├── stores/app.js         # Pinia 状态管理（侧边栏、标签页、语言）
│   ├── i18n/                 # 国际化
│   │   ├── index.js          # i18n 配置
│   │   ├── zh.js             # 中文翻译
│   │   └── en.js             # 英文翻译
│   ├── api/index.js          # Axios API 封装
│   ├── views/
│   │   ├── Dashboard.vue     # 仪表盘（统计卡片 + ECharts 图表）
│   │   ├── JobList.vue       # 任务列表（搜索/操作/状态展示/新建任务）
│   │   ├── JobDetail.vue     # 任务详情（指标 + 执行记录 + 错误日志）
│   │   └── CronTool.vue      # Cron 表达式翻译工具
│   └── components/
│       ├── AppLayout.vue     # 整体布局（侧边栏 + 顶栏 + 内容区）
│       ├── Sidebar.vue       # 左侧导航栏
│       └── TabsBar.vue       # 右侧多标签栏
```

---

## Cron 表达式

nb_cron **强制 6 字段** cron 表达式，消除歧义：

```
┌──────────── 秒 (0-59)
│ ┌────────── 分 (0-59)
│ │ ┌──────── 时 (0-23)
│ │ │ ┌────── 日 (1-31)
│ │ │ │ ┌──── 月 (1-12)
│ │ │ │ │ ┌── 周 (0-6, 0=周日)
│ │ │ │ │ │
* * * * * *
```

**传入 5 字段会直接报错**，避免用户写错。

### 常用示例

| 表达式 | 含义 |
|---|---|
| `* * * * * *` | 每秒 |
| `0 * * * * *` | 每分钟整秒 |
| `*/10 * * * * *` | 每10秒 |
| `0 */5 * * * *` | 每5分钟 |
| `0 0 * * * *` | 每小时整点 |
| `0 30 9 * * *` | 每天 09:30:00 |
| `0 0 9 * * 1-5` | 工作日 09:00:00 |
| `0 0 0 1 * *` | 每月1号 00:00:00 |
| `0 0 2 * * 0` | 每周日 02:00:00 |

### 间隔表达式

除了 cron，也支持 `@every` 简写（trigger 自动推断为 `interval`）：

```python
@cron.job("@every 30s")                        # 每30秒（自动推断）
@cron.job("@every 5m", trigger="interval")     # 每5分钟（显式指定）
@cron.job("2h", trigger="interval")            # 每2小时（简写，显式指定时可省略 @every）
@cron.job("@every 1d")                         # 每天
@cron.job("@every 1w")                         # 每周
```

### 日期表达式（一次性任务）

支持多种日期格式（trigger 自动推断为 `date`），日期按调度器的时区解析：

```python
@cron.job("2026-10-01 09:00:00", trigger="date")     # ISO 格式
@cron.job("2026-10-01", trigger="date")               # 仅日期（当天 00:00:00）
@cron.job("2026/10/01 09:00:00", trigger="date")      # 斜线分隔
@cron.job("2026年10月01日", trigger="date")             # 中文日期
```

### Cron 翻译功能

```python
from nb_cron import explain_cron

print(explain_cron("0 30 9 * * *", "zh"))     # "每天09:30:00执行"
print(explain_cron("0 30 9 * * *", "en"))     # "At 09:30:00, every day"
print(explain_cron("0 0 9 * * 1-5", "zh"))    # "每周一至周五09:00:00执行"
print(explain_cron("*/5 * * * * *", "zh"))     # "每5秒执行"
```

REST API 也支持翻译：`GET /nb_cron/api/cron/explain?expression=0+*/5+*+*+*+*`

---

## 分布式部署

nb_cron 在 Redis/MongoDB/SQLAlchemy 存储模式下**自动支持分布式**：

```python
cron = NbCron("my_project", "redis://localhost:6379/0")
```

**原理：** 每次任务触发时，调度器先用 `SET NX PX` (Redis) 或 `findOneAndUpdate` (MongoDB) 获取分布式锁。锁的 key 包含任务 ID 和触发时间戳，确保同一次触发只有一个实例执行。

不需要额外配置，不需要 leader election，开箱即用。

---

## REST API

所有 API 前缀：`/nb_cron/api/`

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/jobs` | 获取所有任务（含指标） |
| GET | `/jobs/{job_id}` | 获取单个任务详情 |
| POST | `/jobs` | 创建任务 |
| DELETE | `/jobs/{job_id}` | 删除任务 |
| POST | `/jobs/{job_id}/pause` | 暂停任务 |
| POST | `/jobs/{job_id}/resume` | 恢复任务 |
| POST | `/jobs/{job_id}/trigger` | 立即触发一次 |
| GET | `/jobs/{job_id}/metrics` | 获取任务指标 |
| GET | `/dashboard/stats` | 仪表盘统计（含 error_count） |
| GET | `/cron/explain?expression=...` | Cron 表达式翻译 |
| GET | `/functions` | 获取已注册函数列表 |
| GET | `/health` | 健康检查（含时区信息） |

### 创建任务 API

`POST /nb_cron/api/jobs`

```json
{
    "func_ref": "daily_backup",
    "expression": "0 0 2 * * *",
    "trigger": "cron",
    "job_id": "my_job",
    "name": "我的任务",
    "args": ["backup_db"],
    "kwargs": {"compress": true},
    "max_instances": 1
}
```

- `func_ref`: 函数的 `cron_func_name`（通过 `@cron_register` 注册的稳定名称）
- `trigger`: 可选 `"cron"` / `"interval"` / `"date"`，不传则自动推断
- `args`: 位置参数列表，会按顺序传给函数
- `kwargs`: 关键字参数字典，会作为命名参数传给函数

### 创建带参数的任务示例

```json
// 发送邮件任务
POST /nb_cron/api/jobs
{
    "func_ref": "send_email",
    "expression": "0 9 * * * *",
    "trigger": "cron",
    "job_id": "morning_email",
    "name": "晨报邮件",
    "args": ["admin@example.com", "每日晨报"],
    "kwargs": {"body": "这是晨报内容"}
}

// 批量处理任务（同函数不同参数）
POST /nb_cron/api/jobs
{
    "func_ref": "process_queue",
    "expression": "@every 1m",
    "trigger": "interval",
    "job_id": "process_queue_1",
    "name": "处理队列 1",
    "args": ["queue_1"]
}

POST /nb_cron/api/jobs
{
    "func_ref": "process_queue",
    "expression": "@every 1m",
    "trigger": "interval",
    "job_id": "process_queue_2",
    "name": "处理队列 2",
    "args": ["queue_2"]
}
```

### 获取已注册函数

`GET /nb_cron/api/functions`

从存储后端（Redis/MongoDB/SQLAlchemy）读取所有已注册的函数名称列表，支持跨 Git 项目共享。

**跨项目工作原理：**
- 项目 A 中用 `@cron_register` 标记的函数，会在 `cron.start()` 时自动同步到 Redis
- 项目 B 的 Web UI 通过此 API 读取 Redis 中的函数列表
- 即使项目 A 没有运行，函数列表依然可用（持久化在 Redis 中）

**示例：**
```bash
# 项目 A：只标记函数，不添加定时任务
@cron_register('send_email')
def send_email(to, subject):
    ...

@cron_register('generate_report')
def generate_report(type):
    ...

cron.start()  # 函数名自动同步到 Redis

# 项目 B：Web UI 调用 API
GET /nb_cron/api/functions
# 返回：{"functions": ["send_email", "generate_report"]}

# Web UI 下拉框显示这些函数，用户可以选择并创建定时任务
```

---

## 存储后端

| 后端 | URL 格式 | 分布式锁 | 适用场景 |
|---|---|---|---|
| Memory | `None`（默认） | 进程内锁 | 开发/单实例 |
| Redis | `redis://host:port/db` | SET NX PX | 生产/分布式（推荐） |
| MongoDB | `mongodb://host:port/db` | findOneAndUpdate | 生产/分布式 |
| SQLAlchemy | `sqlite:///path` / `mysql+pymysql://...` | INSERT conflict | 生产/分布式 |

---

## 任务指标

nb_cron 自动收集每个任务的执行指标（固定大小，不爆内存）：

- `total_runs` - 总执行次数
- `success_count` / `fail_count` - 成功/失败次数
- `last_run_at` - 最后执行时间
- `last_error` - 最后一次错误信息（截断500字符）
- `avg_duration_ms` / `max_duration_ms` / `min_duration_ms` - 执行耗时统计
- `recent_results` - 最近10次执行结果（环形缓冲区）
- `hourly_stats` - 24小时逐时统计（固定24个槽位）

Redis 中单个任务的指标占用不超过 2KB。

---

## 任务状态

| 状态 | 含义 | 前端显示 |
|---|---|---|
| `active` | 正常运行中 | 绿色 `运行中` |
| `paused` | 已暂停 | 黄色 `已暂停` |
| `error` | 定时函数未找到 | 红色 `异常` |

当函数未找到时（如函数被删除、模块未导入），job 自动标记为 `error` 状态并计入失败次数。修复函数后，下次触发会自动恢复。

---

## API 参考

### `NbCron(name, store_url=None, max_workers=20, tick_seconds=1.0, misfire_grace_seconds=60, tz=None)`

创建调度器实例。

- `name`: **必传**，调度器名称。用于隔离不同项目的 Redis keys / MongoDB collections / SQL 表。多个项目共享同一个 Redis 时互不干扰。UI 侧边栏会显示此名称
- `store_url`: 存储后端 URL，None 表示内存存储
- `max_workers`: 线程池大小
- `tick_seconds`: 调度循环间隔（秒）
- `misfire_grace_seconds`: misfire 容忍时间（超过此时间的错过任务会被跳过）
- `tz`: 时区，默认 `None` 使用本地时区。接受任何 `datetime.tzinfo` 对象

### `@cron.job(expression, *, trigger=None, job_id=None, name=None, args=(), kwargs=None, max_instances=1)`

装饰器，注册定时任务。同时支持同步函数和 async 函数。**函数必须先用 `@cron_register` 注册。**

- `expression`: 触发表达式（cron / 间隔 / 日期时间）
- `trigger`: 触发器类型，可选 `"cron"` / `"interval"` / `"date"`，不传则自动推断

### `cron.add_job(func, expression, *, trigger=None, job_id=None, name=None, ...)`

编程方式添加任务，返回 Job 对象。

- `func`: 函数对象 **或** `cron_func_name` 字符串（通过 `@cron_register` 注册的名称）
- `expression`: 触发表达式
- `trigger`: 触发器类型，可选 `"cron"` / `"interval"` / `"date"`，不传则自动推断

### `@cron_register(cron_func_name)` / `add_cron_register(cron_func_name, func)` / `cron_register(cron_func_name, func)`

给函数绑定路径无关的稳定名称。被装饰的函数会多出 `.cron_func_name` 属性。

```python
from nb_cron import cron_register, add_cron_register
```

### `cron.start()` / `cron.stop(wait=True)`

- `start()` **不阻塞**，立即返回，后面的代码继续执行。
- 主线程跑完后进程**不会退出**，定时任务持续运行。
- `Ctrl+C` 优雅停止。
- 不需要任何 `sleep` / `join` / `input` / `block` 参数。

### `@every` 间隔任务首次何时执行

`@every 5s` 等 **IntervalTrigger** 首次 `next_run` 为「注册时刻的 `now`」，会在**下一个调度 tick 内**执行第一次，**不会**先空等 5 秒；之后每隔 5 秒一次。

### `cron.pause_job(job_id)` / `cron.resume_job(job_id)`

暂停/恢复任务。

### `cron.trigger_job(job_id)`

立即执行一次（不等待下次触发时间）。

### `cron.get_jobs()` / `cron.get_job(job_id)` / `cron.remove_job(job_id)`

查询/删除任务。

### `explain_cron(expression, lang="en")`

翻译 cron 表达式为人类可读文本。`lang` 支持 `"zh"`（中文）和 `"en"`（英文）。

### `get_fastapi_app(cron)` / `get_flask_app(cron)` / `get_django_urls(cron)`

一行创建带 Web UI 的应用，分别返回 FastAPI app、Flask app、Django URL 列表。

```python
from nb_cron.web import get_fastapi_app, get_flask_app, get_django_urls
```

---

## 示例代码

完整可运行的示例代码在 `examples/` 目录下：

| 文件 | 说明 |
|---|---|
| `example_fastapi_redis.py` | FastAPI + Redis 完整示例，含多个任务 |
| `example_flask_redis.py` | Flask + Redis 完整示例 |
| `example_django_redis.py` | Django + Redis 集成指南（分步说明） |
| `example_memory_simple.py` | 最简示例，内存存储，无需 Redis |
| `demo_cross_git_project_manage_corn_tasks/proj1.py` | **跨项目示例 - 项目 1**：函数定义与定时任务 |
| `demo_cross_git_project_manage_corn_tasks/proj2_fastapi_cron.py` | **跨项目示例 - 项目 2**：Web UI 管理后台 |

---

## 跨 Git 项目示例（重点）

nb_cron 的核心特性：函数定义与任务调度分离，支持跨 Git 项目管理。

- **项目 1**（`proj1.py`）：业务项目，用 `@cron_register` 标记函数，函数名自动同步到 Redis
- **项目 2**（`proj2_fastapi_cron.py`）：FastAPI 管理后台，通过 Web UI 为项目 1 的函数添加定时任务

### 快速开始

```bash
# 终端 1：启动项目 1
cd examples/demo_cross_git_project_manage_corn_tasks
python proj1.py

# 终端 2：启动项目 2
uvicorn proj2_fastapi_cron:app --reload

# 访问 Web UI：http://localhost:8000/nb_cron/ui/
```

### 工作原理

```
项目 1 (业务项目)          Redis              项目 2 (管理后台)
@cron_register('func')   →  函数名列表  →   GET /api/functions
cron.start() 同步        →  job 配置    ←   POST /api/jobs 创建
执行函数 (本地进程)       ←  调度任务    ←   Web UI 操作
```

### 优势

- **职责分离**：项目 1 专注业务，项目 2 专注调度
- **安全**：只有 `@cron_register` 标记的函数才暴露
- **灵活**：项目 2 动态创建任务，无需修改项目 1 的代码
- **可维护**：项目 1 重构不影响项目 2 的调度

### 应用场景

微服务架构、多租户 SaaS、DevOps 自动化、数据平台等。

---

## Funboost 执行器（核弹级能力）

关于funboost的教程请参考：[https://funboost.readthedocs.io/zh-cn/latest/index.html](https://funboost.readthedocs.io/zh-cn/latest/index.html)


nb_cron 默认的执行器是在本地线程池中直接调用函数。但如果你将 `executor` 指定为 `FunboostExecutor`，nb_cron 的任务触发时**不在本地执行**，而是通过 funboost 的 `.push()` 把任务推送到消息队列（Redis / RabbitMQ / Kafka / MEMORY_QUEUE 等），由 funboost worker 进程消费执行。

这意味着你**瞬间获得了 funboost 的全部能力**：

### 为什么 FunboostExecutor 这么强？

因为 funboost 的 `BoosterParams` 提供了**工业级**的任务消费能力，一个参数类就覆盖了 99% 的调度和函数运行控制需求：

| 能力 | BoosterParams 参数 | 说明 |
|---|---|---|
| **30+ 种消息队列** | `broker_kind` | Redis / RabbitMQ / Kafka / RocketMQ / Celery / SQS ... 30+ 种中间件随意切换 |
| **精准控频** | `qps` | 指定每秒执行次数，支持小数（如 `0.01` = 每100秒1次），无需关心并发数 |
| **分布式控频** | `is_using_distributed_frequency_control` | 多个消费者实例共享同一 qps 限额，总频率不超 |
| **智能并发池** | `concurrent_num` + `concurrent_mode` | 线程/协程/协程+多进程/单线程，自适应扩缩容，任务少时自动缩减线程 |
| **自动重试** | `max_retry_times` | 函数出错自动重试，支持指数退避（`is_using_advanced_retry`） |
| **指数退避重试** | `advanced_retry_config` | `1s → 2s → 4s → 8s → 16s → 32s → 60s...`，支持 sleep 模式和 requeue 模式 |
| **死信队列** | `is_push_to_dlx_queue_when_retry_max_times` | 重试耗尽后自动进入死信队列，不丢消息 |
| **函数超时** | `function_timeout` | 运行超时自动杀死，防止任务卡死 |
| **消息过期** | `msg_expire_seconds` | 消息超过指定时间自动丢弃，不执行过期任务 |
| **任务去重** | `do_task_filtering` + `task_filtering_expire_seconds` | 相同参数的任务自动去重，防止重复执行 |
| **运行时间限制** | `allow_run_time_cron` | 只在指定 cron 时间段内消费执行，如 `* 9-17 * * 1-5` 仅工作日上班时间 |
| **执行结果持久化** | `function_result_status_persistance_conf` | 保存函数入参、运行结果、运行状态到 MongoDB，可追溯 |
| **RPC 模式** | `is_using_rpc_mode` | 发布端可同步获取消费端的执行结果 |
| **多进程消费** | `mp_consume(process_num=N)` | 协程/线程 + 多进程叠加，性能炸裂 |
| **消费者分组** | `booster_group` | 按业务分组启动消费者，灵活管理 |
| **自定义并发池** | `specify_concurrent_pool` | 多个消费者共享一个线程池，节约资源 |
| **async 支持** | `specify_async_loop` | 指定 event loop，支持 aiohttp 等要求同 loop 的异步库 |

### 安装

```bash
pip install nb_cron_nb[redis] funboost
```

### 基本用法

```python
from funboost import BoosterParams, BrokerEnum
from nb_cron import NbCron, cron_register
from nb_cron.executors.funboost_executor import FunboostExecutor

# 创建 funboost 执行器，BoosterParams 的所有参数都支持 IDE 自动补全
funboost_executor = FunboostExecutor(
    BoosterParams(
        queue_name="nb_cron_dispatch",       # 消息队列名
        broker_kind=BrokerEnum.REDIS,         # 中间件类型，30+ 种可选
        concurrent_num=50,                    # 并发数
        qps=20,                               # 精准控频：每秒最多执行 20 次
        max_retry_times=3,                    # 失败自动重试 3 次
        is_using_distributed_frequency_control=True,  # 分布式控频
    )
)

# NbCron 构造时自动调用 executor.bind_cron(self)
# worker 执行完后直接用 cron.metrics.record() 写指标，无需重建 store
cron = NbCron("my_project", "redis://localhost:6379/0", executor=funboost_executor)

@cron.job("0 */5 * * * *", kwargs={"user_id": 42})
@cron_register('my_task')
def my_task(user_id: int):
    print(f"processing user {user_id}")

# 启动 funboost 消费者 + nb_cron 调度器
funboost_executor.consume()   # 单进程消费（非阻塞）
# funboost_executor.mp_consume(process_num=4)  # 多进程消费，性能炸裂
cron.start()
```

### 工作原理

```
nb_cron 调度器               funboost 消息队列              funboost worker
cron tick 触发任务  ─push()→  Redis/RabbitMQ/Kafka  ─consume()→  解析 cron_func_name
计算 next_run_time           持久化存储，不丢消息            FunctionRegistry.resolve()
分布式锁防重复                                               执行函数 + 上报 metrics
```

**关键区别**：默认执行器是「调度 + 执行在同一进程」，FunboostExecutor 是「调度端 push，消费端执行」，天然解耦。

### 高级用法

`BoosterParams` 的 入参非常丰富，各种函数控制功能都有，所以`nb_cron`的执行器可以充分借助`funboost`的威力，所以作者没有给`nb_cron`默认的本地线程池executor加太多功能，例如重试功能/超时杀死功能等。因为你即使没有安装任何消息队列，也可以 `BoosterParams(...,broker_kind=BrokerEnum.MEMORY_QUEUE)` 来使用funboost的内存队列。

#### 1. 指数退避重试

```python
funboost_executor = FunboostExecutor(
    BoosterParams(
        queue_name="nb_cron_dispatch",
        broker_kind=BrokerEnum.REDIS,
        max_retry_times=5,
        is_using_advanced_retry=True,
        advanced_retry_config={
            'retry_mode': 'requeue',          # requeue 模式：消息发回队列延迟重试，不占线程
            'retry_base_interval': 1.0,        # 基础间隔 1s
            'retry_multiplier': 2.0,           # 指数退避倍数
            'retry_max_interval': 60.0,        # 最大间隔 60s
            'retry_jitter': True,              # 随机抖动，防止惊群
        },
    )
)
# 重试间隔：1s → 2s → 4s → 8s → 16s → 32s → 60s → 60s...
```
#### 2. Worker 独立进程部署（横向扩展）

调度端和消费端可以完全分离部署，消费端可以独立横向扩展：

```python
# scheduler.py — 调度端（只 push，不消费）
from nb_cron import NbCron, cron_register
from nb_cron.executors.funboost_executor import FunboostExecutor
from funboost import BoosterParams, BrokerEnum

funboost_executor = FunboostExecutor(
    BoosterParams(queue_name="nb_cron_dispatch", broker_kind=BrokerEnum.REDIS)
)
cron = NbCron("my_project", "redis://localhost:6379/0", executor=funboost_executor)

@cron.job("0 */5 * * * *")
@cron_register('my_task')
def my_task():
    print("执行任务")

cron.start()  # 只调度，不消费

# worker.py — 消费端（独立进程，可部署多台机器）
from nb_cron import NbCron
from nb_cron.executors.funboost_executor import FunboostExecutor
from funboost import BoosterParams, BrokerEnum
import my_tasks  # 触发 @cron_register，让注册表生效

funboost_executor = FunboostExecutor(
    BoosterParams(queue_name="nb_cron_dispatch", broker_kind=BrokerEnum.REDIS)
)
cron = NbCron("my_project", "redis://localhost:6379/0", executor=funboost_executor)

funboost_executor.mp_consume(process_num=4)  # 4 进程消费
```

#### 3. 自定义指标回调

```python
def my_recorder(job_id, success, duration_ms, error):
    # 同时上报 Prometheus / 自定义监控系统
    prometheus_metrics.labels(job_id=job_id).observe(duration_ms)

funboost_executor = FunboostExecutor(
    BoosterParams(queue_name="nb_cron_dispatch", broker_kind=BrokerEnum.REDIS),
    metrics_recorder=my_recorder,
)
```

### FunboostExecutor vs 默认执行器

| 特性 | 默认 Executor | FunboostExecutor |
|---|---|---|
| 执行方式 | 本地线程池直接调用 | push 到消息队列，worker 消费执行 |
| 消息持久化 | ❌ 进程崩溃任务丢失 | ✅ 消息队列持久化，不丢任务 |
| 横向扩展 | ❌ 只能单进程 | ✅ worker 独立部署，无限扩展 |
| 精准控频 | ❌ | ✅ qps 参数，支持分布式控频 |
| 自动重试 | ❌ | ✅ max_retry_times + 指数退避 |
| 任务去重 | ❌ | ✅ do_task_filtering |
| 消息过期 | ❌ | ✅ msg_expire_seconds |
| 死信队列 | ❌ | ✅ 重试耗尽自动进入死信队列 |
| 函数超时 | ❌ | ✅ function_timeout |
| 运行时间限制 | ❌ | ✅ allow_run_time_cron |
| 30+ 种消息队列 | ❌ | ✅ broker_kind 一键切换 |
| 多进程消费 | ❌ | ✅ mp_consume(process_num=N) |
| 执行结果持久化 | ✅ (store) | ✅ (store + funboost MongoDB) |

---

## 运行示例

```bash
# FastAPI + Redis（推荐）
cd examples
pip install nb_cron_nb[redis,fastapi]
uvicorn example_fastapi_redis:app --reload

# Flask + Redis
pip install nb_cron_nb[redis,flask]
python example_flask_redis.py

# 最简示例（无需 Redis）
pip install nb_cron_nb[fastapi]
uvicorn example_memory_simple:app --reload

# 跨 Git 项目示例（重点推荐）
# 终端 1：启动项目 1（业务项目）
cd examples/demo_cross_git_project_manage_corn_tasks
python proj1.py

# 终端 2：启动项目 2（FastAPI 管理后台）
uvicorn proj2_fastapi_cron:app --reload
```

---

## License

MIT - ydf0509

`````

--- **end of file: README.md** (project: nb_cron) --- 

---


--- **start of file: pyproject.toml** (project: nb_cron) --- 

`````text
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "nb_cron_nb"
version = "0.1.1"
description = "A powerful and simple cron job scheduler that dominates APScheduler"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.7"
authors = [
    {name = "ydf0509"}
]
keywords = ["cron", "scheduler", "distributed", "job", "task"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries",
    "Topic :: System :: Distributed Computing",
]
dependencies = [
    "croniter>=1.0.0",
    "pydantic>=1.10.0",
]

[project.optional-dependencies]
redis = ["redis>=4.0.0"]
mongo = ["pymongo>=4.0.0"]
sqlalchemy = ["sqlalchemy>=1.4.0"]
fastapi = ["fastapi>=0.100.0", "uvicorn>=0.20.0"]
flask = ["flask>=2.0.0"]
django = ["django>=3.2.0", "django-ninja>=0.22.0"]
all = [
    "nb_cron_nb[redis,mongo,sqlalchemy,fastapi,flask,django]",
]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.20.0",
    "httpx>=0.24.0",
]

[project.urls]
Homepage = "https://github.com/ydf0509/nb_cron"
Repository = "https://github.com/ydf0509/nb_cron"

[tool.setuptools.packages.find]
include = ["nb_cron*"]

[tool.setuptools.package-data]
"nb_cron.web" = ["static/**/*"]

`````

--- **end of file: pyproject.toml** (project: nb_cron) --- 

---

# markdown content namespace: nb_cron examples 


## nb_cron File Tree (relative dir: `examples`)


`````

└── examples
    ├── demo1.py
    ├── demo_cross_git_project_manage_corn_tasks
    │   ├── proj1.py
    │   ├── proj2_fastapi_cron.py
    │   └── 跨项目定时任务管理说明文档.md
    ├── example_django_redis.py
    ├── example_fastapi_redis.py
    ├── example_flask_redis.py
    ├── example_memory_simple.py
    └── use_funboost
        ├── example_auto_execute_by_funboost.py
        ├── funboost_demo.py
        └── manual_funboost.py

`````

---


## nb_cron (relative dir: `examples`)  Included Files (total: 11 files)


- `examples/demo1.py`

- `examples/example_django_redis.py`

- `examples/example_fastapi_redis.py`

- `examples/example_flask_redis.py`

- `examples/example_memory_simple.py`

- `examples/demo_cross_git_project_manage_corn_tasks/proj1.py`

- `examples/demo_cross_git_project_manage_corn_tasks/proj2_fastapi_cron.py`

- `examples/demo_cross_git_project_manage_corn_tasks/跨项目定时任务管理说明文档.md`

- `examples/use_funboost/example_auto_execute_by_funboost.py`

- `examples/use_funboost/funboost_demo.py`

- `examples/use_funboost/manual_funboost.py`


---


--- **start of file: examples/demo1.py** (project: nb_cron) --- 

`````python
"""
demo1 — 最小调度示例

cron.start() 不阻塞，后面的代码继续执行。
主线程跑完后进程不会退出，定时任务继续运行。
Ctrl+C 优雅退出。
"""
from nb_cron import NbCron, cron_register, add_cron_register, explain_cron

cron = NbCron("demo")  # name 必传，隔离不同项目

@cron.job("0 */5 * * * *")
@cron_register('report')
def report_task():
    print("生成报告")

@cron.job("30 0 9 * * 1-5", trigger="cron")
@cron_register('async_work')
async def async_task():
    print("异步任务也支持！")

@cron.job("@every 1s", trigger="interval")
@cron_register('heartbeat')
def heartbeat():
    print("心跳", flush=True)

@cron.job("2026-12-31 23:59:59", trigger="date")
@cron_register('new_year')
def new_year_countdown():
    print("新年倒计时任务！")

def backup():
    print("备份数据库")
add_cron_register('backup', backup)

@cron.job("*/10 * * * * *")
@cron_register('report2')
def report_task2():
    print("生成报告2", flush=True)

cron.add_job('backup', "0 0 2 * * *", trigger="cron", job_id="daily_backup", name="每日备份")
cron.add_job(report_task.cron_func_name, "0 30 8 * * *", trigger="cron", job_id="morning_report", name="晨报")

print(explain_cron("0 30 9 * * *", "zh"))
print(explain_cron("0 30 9 * * *", "en"))

cron.start()

print("start() 后面的代码正常执行！")
print("定时任务在后台运行，进程不会退出")
print("按 Ctrl+C 退出")

`````

--- **end of file: examples/demo1.py** (project: nb_cron) --- 

---


--- **start of file: examples/example_django_redis.py** (project: nb_cron) --- 

`````python
"""
nb_cron + Django + Redis 集成指南

安装依赖:
    pip install nb_cron_nb[redis,django]

使用方式: 把以下代码集成到你的 Django 项目中

步骤:
    1. 在 your_project/cron_config.py 中配置调度器
    2. 在 your_project/urls.py 中挂载路由
    3. 在 your_project/apps.py 的 AppConfig.ready() 中启动调度器

访问地址:
    管理后台 UI:  http://localhost:8000/nb_cron/ui/
    REST API:     http://localhost:8000/nb_cron/api/jobs
"""

# ═══════════════════════════════════════════
# Step 1: cron_config.py - 配置调度器和任务
# ═══════════════════════════════════════════
"""
# your_project/cron_config.py

import logging
from nb_cron import NbCron, cron_register

logging.basicConfig(level=logging.INFO)

# name 必传，隔离不同项目
cron = NbCron("my_django_app", "redis://localhost:6379/0")

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat():
    logging.info("heartbeat OK")

@cron.job("0 */5 * * * *", trigger="cron", name="数据同步")
@cron_register('sync_data')
def sync_data():
    logging.info("data synced")

@cron.job("0 30 2 * * *", trigger="cron", name="每日备份")
@cron_register('daily_backup')
def daily_backup():
    logging.info("backup completed")
"""

# ═══════════════════════════════════════════
# Step 2: urls.py - 挂载 nb_cron 路由
# ═══════════════════════════════════════════
"""
# your_project/urls.py

from django.contrib import admin
from django.urls import path
from your_project.cron_config import cron
from nb_cron.web.app import get_django_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... 你的其他路由 ...
] + get_django_urls(cron)

# 访问:
#   UI:  http://localhost:8000/nb_cron/ui/
#   API: http://localhost:8000/nb_cron/api/jobs
"""

# ═══════════════════════════════════════════
# Step 3: apps.py - 在 Django 启动时启动调度器
# ═══════════════════════════════════════════
"""
# your_app/apps.py

from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        from your_project.cron_config import cron
        # 防止 Django reload 时重复启动
        import os
        if os.environ.get('RUN_MAIN') == 'true':
            cron.start()
"""

# ═══════════════════════════════════════════
# 启动 Django 开发服务器
# ═══════════════════════════════════════════
"""
python manage.py runserver 0.0.0.0:8000
"""

`````

--- **end of file: examples/example_django_redis.py** (project: nb_cron) --- 

---


--- **start of file: examples/example_fastapi_redis.py** (project: nb_cron) --- 

`````python
"""
nb_cron + FastAPI + Redis 完整示例

安装依赖:
    pip install nb_cron_nb[redis,fastapi]

启动方式:
    uvicorn example_fastapi_redis:app --host 0.0.0.0 --port 8000 --reload

访问地址:
    管理后台 UI:  http://localhost:8000/nb_cron/ui/
    REST API:     http://localhost:8000/nb_cron/api/jobs
    已注册函数:   http://localhost:8000/nb_cron/api/functions
    健康检查:     http://localhost:8000/nb_cron/api/health
    Cron 翻译:    http://localhost:8000/nb_cron/api/cron/explain?expression=0%20*/5%20*%20*%20*%20*
"""
import random
import logging

from nb_cron import NbCron, cron_register, add_cron_register
from nb_cron.web.app import get_fastapi_app

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

# ─── 创建调度器（name 隔离项目，Redis 存储 + 分布式锁） ───
cron = NbCron("example_fastapi很长很长很长", "redis://localhost:6379/0")


# ─── 用装饰器注册定时任务 ───

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat():
    """每10秒执行一次心跳"""
    logging.info("heartbeat OK")

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测2",kwargs={"x":100})
@cron_register('heartbeat2')
def heartbeat2(x):
    """每10秒执行一次心跳"""
    logging.info("heartbeat2 OK")
    

@cron.job("0 */1 * * * *", trigger="cron", name="数据同步")
@cron_register('sync_data')
def sync_data():
    """每分钟同步数据"""
    count = random.randint(10, 100)
    logging.info(f"synced {count} records")


@cron.job("0 0 */1 * * *", trigger="cron", name="缓存清理")
@cron_register('cleanup_cache')
def cleanup_cache():
    """每小时清理过期缓存"""
    logging.info("cache cleaned")


@cron.job("0 30 2 * * *", trigger="cron", name="每日备份")
@cron_register('daily_backup')
def daily_backup():
    """每天凌晨2:30执行数据库备份"""
    logging.info("backup completed")


@cron.job("0 0 9 * * 1-5", trigger="cron", name="工作日报告")
@cron_register('workday_report')
async def workday_report():
    """工作日早上9点生成日报"""
    logging.info("daily report generated")


# ─── 用 add_job + 注册名 方式 ───

def send_weekly_summary():
    """每周日发送周报"""
    logging.info("weekly summary sent")

add_cron_register('weekly_summary', send_weekly_summary)
cron.add_job(send_weekly_summary.cron_func_name, "0 0 10 * * 0", trigger="cron", job_id="weekly_summary", name="周报推送")


print(cron.get_jobs())

# ─── 创建 FastAPI app（自带 UI + API） ───
app = get_fastapi_app(cron)

# ─── 启动调度器 ───
@app.on_event("startup")
def startup():
    cron.start()
    logging.info("nb_cron scheduler started!")
    logging.info("UI:  http://localhost:8000/nb_cron/ui/")
    logging.info("API: http://localhost:8000/nb_cron/api/jobs")

@app.on_event("shutdown")
def shutdown():
    cron.stop()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("example_fastapi_redis:app", host="0.0.0.0", port=8000, reload=True)

`````

--- **end of file: examples/example_fastapi_redis.py** (project: nb_cron) --- 

---


--- **start of file: examples/example_flask_redis.py** (project: nb_cron) --- 

`````python
"""
nb_cron + Flask + Redis 完整示例

安装依赖:
    pip install nb_cron_nb[redis,flask]

启动方式（开发）:
    python example_flask_redis.py

启动方式（生产）:
    gunicorn example_flask_redis:app -w 1 -b 0.0.0.0:5000

访问地址:
    管理后台 UI:  http://localhost:5000/nb_cron/ui/
    REST API:     http://localhost:5000/nb_cron/api/jobs
    健康检查:     http://localhost:5000/nb_cron/api/health
"""
import random
import logging

from nb_cron import NbCron, cron_register, add_cron_register
from nb_cron.web.app import get_flask_app

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

# ─── 创建调度器（name 隔离项目，Redis 存储） ───
cron = NbCron("example_flask", "redis://localhost:6379/0")


@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat222():
    logging.info("heartbeat OK")


@cron.job("0 */1 * * * *", trigger="cron", name="数据同步")
@cron_register('sync_data')
def sync_data():
    count = random.randint(10, 100)
    logging.info(f"synced {count} records")


@cron.job("0 0 */1 * * *", trigger="cron", name="缓存清理")
@cron_register('cleanup_cache')
def cleanup_cache():
    logging.info("cache cleaned")


@cron.job("0 30 2 * * *", trigger="cron", name="每日备份")
@cron_register('daily_backup')
def daily_backup():
    logging.info("backup completed")


# ─── 创建 Flask app ───
app = get_flask_app(cron)

# ─── 启动 ───
if __name__ == "__main__":
    cron.start()
    logging.info("nb_cron scheduler started!")
    logging.info("UI:  http://localhost:5000/nb_cron/ui/")
    logging.info("API: http://localhost:5000/nb_cron/api/jobs")
    app.run(host="0.0.0.0", port=5000, debug=False)

`````

--- **end of file: examples/example_flask_redis.py** (project: nb_cron) --- 

---


--- **start of file: examples/example_memory_simple.py** (project: nb_cron) --- 

`````python
"""
nb_cron 最简示例（内存存储，无需 Redis）

安装:
    pip install nb_cron_nb[fastapi]

启动:
    uvicorn example_memory_simple:app --reload

访问:
    http://localhost:8000/nb_cron/ui/
"""
import logging
from nb_cron import NbCron, cron_register, explain_cron
from nb_cron.web.app import get_fastapi_app

logging.basicConfig(level=logging.INFO)

cron = NbCron("simple_demo")

@cron.job("*/5 * * * * *", trigger="cron", name="每5秒打印")
@cron_register('hello')
def print_hello():
    logging.info("Hello from nb_cron!")

@cron.job("0 */1 * * * *", trigger="cron", name="每分钟任务")
@cron_register('async_task')
async def async_task():
    logging.info("Async task running!")

app = get_fastapi_app(cron)

@app.on_event("startup")
def startup():
    cron.start()

    print("\n" + "=" * 50)
    print("nb_cron started!")
    print(f"  UI:  http://localhost:8000/nb_cron/ui/")
    print(f"  API: http://localhost:8000/nb_cron/api/jobs")
    print("=" * 50)

    print(f'\n  "*/5 * * * * *" => {explain_cron("*/5 * * * * *", "zh")}')
    print(f'  "0 */1 * * * *" => {explain_cron("0 */1 * * * *", "zh")}')
    print()

`````

--- **end of file: examples/example_memory_simple.py** (project: nb_cron) --- 

---


--- **start of file: examples/demo_cross_git_project_manage_corn_tasks/proj1.py** (project: nb_cron) --- 

`````python

"""
模拟跨git项目管理定时任务的项目
假设proj1.py 是一个单独的git项目1，
假设 proj2_fastapi_cron.py 是一个单独的git项目2，

只要 NbCron 的name 和 store_url 一样，项目2的 proj2_fastapi_cron.py 就能可视化管项目1的定时任务管理
"""

import random
import logging

from nb_cron import NbCron, cron_register, add_cron_register


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

# ─── 创建调度器（name 隔离项目，Redis 存储 + 分布式锁） ───
cron = NbCron("example_proj1b", "redis://localhost:6379/0")


# ─── 用装饰器注册定时任务 ───

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat():
    """每10秒执行一次心跳"""
    logging.info("heartbeat OK")

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测2",kwargs={"x":100})
@cron_register('heartbeat2')
def heartbeat2(x):
    """每10秒执行一次心跳"""
    logging.info("heartbeat2 OK")
    

@cron.job("0 */1 * * * *", trigger="cron", name="数据同步")
@cron_register('sync_data')
def sync_data():
    """每分钟同步数据"""
    count = random.randint(10, 100)
    logging.info(f"synced {count} records")


@cron.job("0 0 */1 * * *", trigger="cron", name="缓存清理")
@cron_register('cleanup_cache')
def cleanup_cache():
    """每小时清理过期缓存"""
    logging.info("cache cleaned")


@cron.job("0 30 2 * * *", trigger="cron", name="每日备份")
@cron_register('daily_backup')
def daily_backup():
    """每天凌晨2:30执行数据库备份"""
    logging.info("backup completed")


@cron.job("0 0 9 * * 1-5", trigger="cron", name="工作日报告")
@cron_register('workday_report')
async def workday_report():
    """工作日早上9点生成日报"""
    logging.info("daily report generated")

"""
只加一个cron_register标记，但没添加定时任务，那么这个函数就能从网页上被选择，从而夸项目能在网页添加定时任务

你大脑想想，如果不要 cron_register标记
如果a项目不同文件件重有100个函数， b项目的 nb_cron_ui前端网页中咋知道怎么选择哪个函数能加定时任务？难道手动在网页输入函数路径吗？
"""
@cron_register('to_be_add_timing_job_from_webui')
async def to_be_add_timing_job_from_webui():
    logging.info("to_be_add_timing_job_from_webui")


# ─── 用 add_job + 注册名 方式 ───

def send_weekly_summary():
    """每周日发送周报"""
    logging.info("weekly summary sent")

add_cron_register('weekly_summary', send_weekly_summary)
cron.add_job(send_weekly_summary.cron_func_name, "0 0 10 * * 0", trigger="cron", job_id="weekly_summary", name="周报推送")


print(cron.get_jobs())

cron.start()

`````

--- **end of file: examples/demo_cross_git_project_manage_corn_tasks/proj1.py** (project: nb_cron) --- 

---


--- **start of file: examples/demo_cross_git_project_manage_corn_tasks/proj2_fastapi_cron.py** (project: nb_cron) --- 

`````python
"""
模拟跨git项目管理定时任务的项目
假设proj1.py 是一个单独的git项目1，
假设 proj2_fastapi_cron.py 是一个单独的git项目2，

只要 NbCron 的name 和 store_url 一样，项目2的 proj2_fastapi_cron.py 就能可视化管项目1的定时任务管理
"""


"""
nb_cron + FastAPI + Redis 完整示例

安装依赖:
    pip install nb_cron_nb[redis,fastapi]

启动方式:
    uvicorn proj2_fastapi_cron:app --host 0.0.0.0 --port 8000 --reload

访问地址:
    管理后台 UI:  http://localhost:8000/nb_cron/ui/
    REST API:     http://localhost:8000/nb_cron/api/jobs
    已注册函数:   http://localhost:8000/nb_cron/api/functions
    健康检查:     http://localhost:8000/nb_cron/api/health
    Cron 翻译:    http://localhost:8000/nb_cron/api/cron/explain?expression=0%20*/5%20*%20*%20*%20*
"""

import logging

from nb_cron import NbCron
from nb_cron.web.app import get_fastapi_app

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

# ─── 创建调度器（name 隔离项目，Redis 存储 + 分布式锁） ───，只要 name 和 store_url 一样，就能可视化管项目1的定时任务管理
# proj2_fast_api_cron = NbCron("example_proj1b", "redis://localhost:6379/0")


proj2_fast_api_cron = NbCron("example_proj1b", "redis://localhost:6379/0")

# ─── 创建 FastAPI app（自带 UI + API） ───
app = get_fastapi_app(proj2_fast_api_cron)

# ─── 启动调度器 ───
@app.on_event("startup")
def startup():
    # proj2_fast_api_cron.start() #不需要start ，只作为管跨项目的可视化管理
    logging.info("nb_cron scheduler started!")
    logging.info("UI:  http://localhost:8000/nb_cron/ui/")
    logging.info("API: http://localhost:8000/nb_cron/api/jobs")

@app.on_event("shutdown")
def shutdown():
    pass
    # cron.stop() #不需要stop ，只作为管跨项目的可视化管理

# from nb_cron.api.handlers import handle_get_jobs
# print(handle_get_jobs(proj2_fast_api_cron))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("proj2_fastapi_cron:app", host="0.0.0.0", port=8000, reload=True)

`````

--- **end of file: examples/demo_cross_git_project_manage_corn_tasks/proj2_fastapi_cron.py** (project: nb_cron) --- 

---


--- **start of file: examples/demo_cross_git_project_manage_corn_tasks/跨项目定时任务管理说明文档.md** (project: nb_cron) --- 

`````markdown
# 跨 Git 项目定时任务管理说明文档

## 目录

1. [概述](#概述)
2. [核心概念](#核心概念)
3. [架构图](#架构图)
4. [环境准备](#环境准备)
5. [项目 1：业务项目详解](#项目 1 业务项目详解)
6. [项目 2：管理后台详解](#项目 2 管理后台详解)
7. [运行步骤](#运行步骤)
8. [Web UI 操作指南](#web-ui-操作指南)
9. [技术原理深度解析](#技术原理深度解析)
10. [最佳实践](#最佳实践)
11. [常见问题](#常见问题)

---

## 概述

### 什么是跨 Git 项目定时任务管理？

传统的定时任务框架（如 APScheduler）要求**函数定义**和**任务调度**必须在同一个进程中。这导致：

- ❌ 业务代码和调度代码耦合在一起
- ❌ 修改定时任务需要重启业务进程
- ❌ 无法通过 Web UI 统一管理多个项目的定时任务
- ❌ 函数路径依赖严重，代码重构后调度失效

nb_cron 创新性地提出了**跨 Git 项目定时任务管理**方案：

- ✅ **函数定义**（项目 1）和**任务调度**（项目 2）完全分离
- ✅ 项目 1 专注业务逻辑，项目 2 专注调度管理
- ✅ 通过 Web UI 统一管理所有项目的定时任务
- ✅ 使用 `@cron_register` 标记函数，与文件路径解耦

### 适用场景

| 场景 | 说明 | 价值 |
|------|------|------|
| **微服务架构** | 多个业务服务共享一个定时任务管理后台 | 统一管理，降低运维成本 |
| **多租户 SaaS** | 不同租户的业务函数独立，平台方统一调度 | 租户隔离，平台可控 |
| **DevOps 自动化** | 运维脚本仓库 + 运维管理后台 | 脚本与调度分离，安全可控 |
| **数据平台** | 数据处理函数 + 数据任务调度平台 | 函数复用，灵活调度 |
| **低代码平台** | 业务函数库 + 可视化任务编排 | 降低使用门槛 |

---

## 核心概念

### 1. `@cron_register`：函数注册装饰器

```python
from nb_cron import cron_register

@cron_register('send_email')
def send_email(to: str, subject: str):
    """发送邮件"""
    print(f"发送邮件到 {to}: {subject}")
```

**作用**：
- 给函数绑定一个**稳定名称**（`cron_func_name`）
- 函数名不依赖文件路径，支持代码重构
- 标记该函数"可以被外部调度"

**两种用法**：

```python
# 用法 1：装饰器（推荐）
@cron_register('func_name')
def my_func():
    ...

# 用法 2：函数调用
def my_func():
    ...
cron_register('func_name', my_func)
```

### 2. 函数注册表（FunctionRegistry）

nb_cron 在内存中维护一个全局函数注册表：

```python
# 内部实现（简化版）
FunctionRegistry._registry = {
    'heartbeat': <function heartbeat at 0x...>,
    'send_email': <function send_email at 0x...>,
    'sync_data': <function sync_data at 0x...>,
}
```

**特性**：
- 键：`cron_func_name`（稳定名称）
- 值：函数对象
- 支持跨模块、跨文件查找

### 3. 函数名持久化（Redis）

`cron.start()` 时，自动将函数名同步到 Redis：

```python
# Redis 数据结构
nb_cron:example_proj1b:functions = {
    "heartbeat",
    "heartbeat2",
    "sync_data",
    "cleanup_cache",
    "daily_backup",
    "workday_report",
    "weekly_summary",
    "to_be_add_timing_job_from_webui",
}
```

**意义**：
- 项目 2 可以通过 Redis 读取项目 1 的函数列表
- 即使项目 1 没有运行，函数列表依然在 Redis 中
- 支持跨 Git 项目、跨进程、跨机器

### 4. 任务配置持久化（Redis）

用户在 Web UI 创建的任务存储在 Redis：

```python
# Redis Hash 结构
nb_cron:example_proj1b:jobs:daily_backup = {
    "job_id": "daily_backup",
    "func_ref": "daily_backup",        # ← 函数稳定名称
    "expression": "0 30 2 * * *",      # ← Cron 表达式
    "trigger": "cron",
    "name": "每日备份",
    "args": "[]",
    "kwargs": "{}",
    "max_instances": "1",
    "status": "active",
}
```

**调度流程**：
1. 项目 1 的调度器从 Redis 读取任务配置
2. 根据 `func_ref` 在 FunctionRegistry 中查找函数
3. 调用函数，执行任务

---

## 架构图

### 整体架构

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Git 项目 1：业务项目（proj1.py）                                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  业务函数定义：                                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  @cron_register('heartbeat')                                     │   │
│  │  def heartbeat(): ...  # 心跳检测                                │   │
│  │                                                                  │   │
│  │  @cron_register('send_email')                                    │   │
│  │  def send_email(to, subject): ...  # 发送邮件                    │   │
│  │                                                                  │   │
│  │  @cron_register('sync_data')                                     │   │
│  │  def sync_data(): ...  # 数据同步                                │   │
│  │                                                                  │   │
│  │  @cron_register('to_be_add_timing_job_from_webui')               │   │
│  │  async def to_be_add_timing_job_from_webui(): ...                │   │
│  │  # ↑ 只标记，不添加任务，留给 Web UI 动态调度                      │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  调度器启动：                                                             │
│  cron.start() ──→ 函数名同步到 Redis                                      │
│                ──→ 从 Redis 读取任务配置                                  │
│                ──→ 后台运行定时任务                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              │ Redis（共享存储）
                              │ nb_cron:example_proj1b:*
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Git 项目 2：管理后台（proj2_fastapi_cron.py）                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  FastAPI + Web UI：                                                       │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │  GET /nb_cron/api/functions                                      │   │
│  │  → 从 Redis 读取函数列表：                                        │   │
│  │    ["heartbeat", "send_email", "sync_data", ...]                 │   │
│  │                                                                  │   │
│  │  POST /nb_cron/api/jobs                                          │   │
│  │  ← 创建任务：                                                     │   │
│  │    { func_ref: "send_email", expression: "0 9 * * * *" }         │   │
│  │                                                                  │   │
│  │  Web UI 界面：                                                    │   │
│  │  ┌──────────────────────────────────────────────────────────┐   │   │
│  │  │ 定时任务管理后台                                          │   │   │
│  │  │ ───────────────────────────────────────────────────────  │   │   │
│  │  │ 任务列表 | 新建任务 | 仪表盘 | Cron 工具                   │   │   │
│  │  │                                                          │   │   │
│  │  │ 新建任务：                                                │   │   │
│  │  │ 函数：[send_email ▼]                                     │   │   │
│  │  │ Cron: 0 9 * * * *                                        │   │   │
│  │  │ 参数：to="admin@example.com", subject="日报"              │   │   │
│  │  │ [创建]                                                    │   │   │
│  │  └──────────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 数据流

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   项目 1      │         │    Redis     │         │   项目 2      │
│  (业务项目)   │         │  (共享存储)   │         │  (管理后台)   │
└──────────────┘         └──────────────┘         └──────────────┘
       │                        │                        │
       │ @cron_register('func') │                        │
       │ ──────────────────────>│                        │
       │   函数名持久化          │                        │
       │                        │                        │
       │ cron.start()           │                        │
       │ ──────────────────────>│                        │
       │   同步函数名            │                        │
       │                        │                        │
       │                        │ GET /api/functions     │
       │                        │ <───────────────────── │
       │                        │ 返回函数列表           │
       │                        │ ──────────────────────>│
       │                        │                        │
       │                        │ POST /api/jobs         │
       │                        │ <───────────────────── │
       │                        │ 创建任务配置           │
       │                        │ ──────────────────────>│
       │                        │                        │
       │ 从 Redis 读取任务配置   │                        │
       │ <───────────────────── │                        │
       │                        │                        │
       │ 执行函数 (本地进程)     │                        │
       │                        │                        │
```

---

## 环境准备

### 1. 安装 Python 依赖

```bash
# 基础依赖（项目 1）
pip install nb_cron_nb[redis]

# 完整依赖（项目 2）
pip install nb_cron_nb[redis,fastapi]
```

### 2. 安装并启动 Redis

**Windows**：
```bash
# 下载 Redis for Windows
# https://github.com/microsoftarchive/redis/releases

# 启动 Redis
redis-server.exe
```

**Linux / macOS**：
```bash
# 使用 Docker
docker run -d -p 6379:6379 redis:latest

# 或使用包管理器
# Ubuntu/Debian
sudo apt-get install redis-server
sudo systemctl start redis

# macOS
brew install redis
brew services start redis
```

**验证 Redis 连接**：
```bash
redis-cli ping
# 输出：PONG
```

### 3. 目录结构

```
demo_cross_git_project_manage_corn_tasks/
├── proj1.py                          # 项目 1：业务项目
├── proj2_fastapi_cron.py             # 项目 2：管理后台
└── 跨项目定时任务管理说明文档.md       # 本文档
```

---

## 项目 1：业务项目详解

### 完整代码

```python
"""
模拟跨 git 项目管理定时任务的项目
假设 proj1.py 是一个单独的 git 项目 1，
假设 proj2_fastapi_cron.py 是一个单独的 git 项目 2，

只要 NbCron 的 name 和 store_url 一样，项目 2 的 proj2_fastapi_cron.py 就能可视化管项目 1 的定时任务管理
"""

import random
import logging

from nb_cron import NbCron, cron_register, add_cron_register


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

# ─── 创建调度器（name 隔离项目，Redis 存储 + 分布式锁） ───，只要 name 和 store_url 一样，就能可视化管项目1的定时任务管理
cron = NbCron("example_proj1b", "redis://localhost:6379/0")


# ─── 用装饰器注册定时任务 ───

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat():
    """每 10 秒执行一次心跳"""
    logging.info("heartbeat OK")

@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测 2",kwargs={"x":100})
@cron_register('heartbeat2')
def heartbeat2(x):
    """每 10 秒执行一次心跳"""
    logging.info("heartbeat2 OK")
    

@cron.job("0 */1 * * * *", trigger="cron", name="数据同步")
@cron_register('sync_data')
def sync_data():
    """每分钟同步数据"""
    count = random.randint(10, 100)
    logging.info(f"synced {count} records")


@cron.job("0 0 */1 * * *", trigger="cron", name="缓存清理")
@cron_register('cleanup_cache')
def cleanup_cache():
    """每小时清理过期缓存"""
    logging.info("cache cleaned")


@cron.job("0 30 2 * * *", trigger="cron", name="每日备份")
@cron_register('daily_backup')
def daily_backup():
    """每天凌晨 2:30 执行数据库备份"""
    logging.info("backup completed")


@cron.job("0 0 9 * * 1-5", trigger="cron", name="工作日报告")
@cron_register('workday_report')
async def workday_report():
    """工作日早上 9 点生成日报"""
    logging.info("daily report generated")

"""
只加一个 cron_register 标记，但没添加定时任务，那么这个函数就能从网页上被选择，从而跨项目能在网页添加定时任务

你大脑想想，如果不要 cron_register 标记
如果 a 项目不同文件件重有 100 个函数，b 项目的 nb_cron_ui 前端网页中咋知道怎么选择哪个函数能加定时任务？难道手动在网页输入函数路径吗？
"""
@cron_register('to_be_add_timing_job_from_webui')
async def to_be_add_timing_job_from_webui():
    logging.info("to_be_add_timing_job_from_webui")


# ─── 用 add_job + 注册名 方式 ───

def send_weekly_summary():
    """每周日发送周报"""
    logging.info("weekly summary sent")

add_cron_register('weekly_summary', send_weekly_summary)
cron.add_job(send_weekly_summary.cron_func_name, "0 0 10 * * 0", trigger="cron", job_id="weekly_summary", name="周报推送")


print(cron.get_jobs())

cron.start()
```

### 代码解析

#### 1. 创建调度器

```python
cron = NbCron("example_proj1b", "redis://localhost:6379/0")
```

**参数说明**：
- `"example_proj1b"`：**必传**，调度器名称
  - 用于隔离不同项目的 Redis keys
  - 格式：`nb_cron:{name}:*`
  - 项目 1 和项目 2 必须使用相同的 `name` 才能共享数据
- `"redis://localhost:6379/0"`：Redis 连接 URL
  - 支持 Redis、MongoDB、SQLAlchemy 等多种存储后端
  - 不传则使用内存存储（开发环境）

#### 2. 装饰器方式注册任务

```python
@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测")
@cron_register('heartbeat')
def heartbeat():
    """每 10 秒执行一次心跳"""
    logging.info("heartbeat OK")
```

**装饰器顺序**：
1. `@cron_register('heartbeat')`：**先注册函数**，绑定稳定名称
2. `@cron.job("*/10 * * * * *", ...)`：**再注册调度**，读取 `.cron_func_name`

**Cron 表达式**（6 字段，秒级精度）：
```
*/10 * * * * *
│    │ │ │ │ │
│    │ │ │ │ └─ 星期几 (0-6, 0=周日)
│    │ │ │ └─── 月份 (1-12)
│    │ │ └───── 日期 (1-31)
│    │ └─────── 小时 (0-23)
│    └───────── 分钟 (0-59)
└────────────── 秒 (0-59)
```

#### 3. 带参数的任务

```python
@cron.job("*/10 * * * * *", trigger="cron", name="心跳检测 2", kwargs={"x": 100})
@cron_register('heartbeat2')
def heartbeat2(x):
    """每 10 秒执行一次心跳"""
    logging.info("heartbeat2 OK")
```

**参数传递**：
- `args`：位置参数元组
- `kwargs`：关键字参数字典

#### 4. 只标记，不添加任务

```python
@cron_register('to_be_add_timing_job_from_webui')
async def to_be_add_timing_job_from_webui():
    logging.info("to_be_add_timing_job_from_webui")
```

**关键点**：
- 只用 `@cron_register` 标记，**不用** `@cron.job` 添加任务
- 函数名会同步到 Redis
- 项目 2 的 Web UI 可以看到这个函数
- 用户可以在 Web UI 上为这个函数创建定时任务

**为什么需要这样？**

想象一个场景：
- 项目 A 有 100 个函数，分布在 10 个文件中
- 只有 30 个函数需要被外部调度
- 项目 B 的 Web UI 怎么知道哪些函数可以被调度？

答案：`@cron_register` 标记！

```python
# 项目 A：tasks/email.py
@cron_register('send_email')
def send_email(to, subject):
    ...

# 项目 A：tasks/report.py
@cron_register('generate_report')
def generate_report(type):
    ...

# 项目 B：Web UI 下拉框
<select>
  <option>send_email</option>
  <option>generate_report</option>
  <!-- 只有被 @cron_register 标记的函数才会出现在这里 -->
</select>
```

#### 5. 非装饰器方式

```python
def send_weekly_summary():
    """每周日发送周报"""
    logging.info("weekly summary sent")

add_cron_register('weekly_summary', send_weekly_summary)
cron.add_job(
    send_weekly_summary.cron_func_name,
    "0 0 10 * * 0",
    trigger="cron",
    job_id="weekly_summary",
    name="周报推送",
)
```

**适用场景**：
- 第三方库函数（无法修改源码）
- 动态注册（运行时决定参数）
- 批量添加同函数不同参数的任务

#### 6. 启动调度器

```python
cron.start()
```

**特性**：
- **不阻塞**，立即返回
- 后台运行定时任务
- 进程不会退出
- 不需要 `sleep` / `join` / `input` 等阻塞操作

### 运行项目 1

```bash
cd examples/demo_cross_git_project_manage_corn_tasks
python proj1.py
```

**预期输出**：
```
[Job(job_id='heartbeat', ...), Job(job_id='heartbeat2', ...), ...]

2026-04-13 10:00:00,123 [__main__] INFO: heartbeat OK
2026-04-13 10:00:00,124 [__main__] INFO: heartbeat2 OK
2026-04-13 10:01:00,456 [__main__] INFO: synced 42 records
...
```

**验证 Redis 数据**：
```bash
redis-cli
127.0.0.1:6379> SMEMBERS nb_cron:example_proj1b:functions
1) "heartbeat"
2) "heartbeat2"
3) "sync_data"
4) "cleanup_cache"
5) "daily_backup"
6) "workday_report"
7) "weekly_summary"
8) "to_be_add_timing_job_from_webui"

127.0.0.1:6379> HGETALL nb_cron:example_proj1b:jobs:heartbeat
1) "job_id"
2) "heartbeat"
3) "func_ref"
4) "heartbeat"
5) "expression"
6) "*/10 * * * * *"
...
```

---

## 项目 2：管理后台详解

### 完整代码

```python
"""
模拟跨 git 项目管理定时任务的项目
假设 proj1.py 是一个单独的 git 项目 1，
假设 proj2_fastapi_cron.py 是一个单独的 git 项目 2，

只要 NbCron 的 name 和 store_url 一样，项目 2 的 proj2_fastapi_cron.py 就能可视化管项目 1 的定时任务管理
"""


"""
nb_cron + FastAPI + Redis 完整示例

安装依赖:
    pip install nb_cron_nb[redis,fastapi]

启动方式:
    uvicorn example_fastapi_redis:app --host 0.0.0.0 --port 8000 --reload

访问地址:
    管理后台 UI:  http://localhost:8000/nb_cron/ui/
    REST API:     http://localhost:8000/nb_cron/api/jobs
    已注册函数:   http://localhost:8000/nb_cron/api/functions
    健康检查:     http://localhost:8000/nb_cron/api/health
    Cron 翻译:    http://localhost:8000/nb_cron/api/cron/explain?expression=0%20*/5%20*%20*%20*%20*
"""

import logging

from nb_cron import NbCron
from nb_cron.web.app import get_fastapi_app

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

# ─── 创建调度器（name 隔离项目，Redis 存储 + 分布式锁） ───
proj2_fast_api_cron = NbCron("example_proj1b", "redis://localhost:6379/0")

# ─── 创建 FastAPI app（自带 UI + API） ───
app = get_fastapi_app(proj2_fast_api_cron)

# ─── 启动调度器 ───
@app.on_event("startup")
def startup():
    # proj2_fast_api_cron.start() #不需要 start，只作为管跨项目的可视化管理
    logging.info("nb_cron scheduler started!")
    logging.info("UI:  http://localhost:8000/nb_cron/ui/")
    logging.info("API: http://localhost:8000/nb_cron/api/jobs")

@app.on_event("shutdown")
def shutdown():
    pass
    # cron.stop() #不需要 stop，只作为管跨项目的可视化管理


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("proj2_fastapi_cron:app", host="0.0.0.0", port=8000, reload=True)
```

### 代码解析

#### 1. 创建调度器

```python
proj2_fast_api_cron = NbCron("example_proj1b", "redis://localhost:6379/0")
```

**关键点**：
- `name="example_proj1b"`：**必须与项目 1 相同**
  - 共享 Redis 中的函数列表和任务配置
  - 如果不同，项目 2 看不到项目 1 的函数
- `store_url="redis://localhost:6379/0"`：**必须与项目 1 相同**
  - 共享同一个 Redis 数据库

#### 2. 创建 FastAPI 应用

```python
app = get_fastapi_app(proj2_fast_api_cron)
```

**一行代码创建**：
- 自动注册所有 API 路由
- 自动挂载 Web UI 静态文件
- 自动生成 OpenAPI 文档

**API 路由**：
```
GET  /nb_cron/api/jobs              # 获取所有任务
GET  /nb_cron/api/jobs/{job_id}     # 获取单个任务
POST /nb_cron/api/jobs              # 创建任务
DELETE /nb_cron/api/jobs/{job_id}   # 删除任务
POST /nb_cron/api/jobs/{job_id}/pause    # 暂停任务
POST /nb_cron/api/jobs/{job_id}/resume   # 恢复任务
POST /nb_cron/api/jobs/{job_id}/trigger  # 立即触发
GET  /nb_cron/api/functions         # 获取已注册函数列表
GET  /nb_cron/api/health            # 健康检查
GET  /nb_cron/api/cron/explain      # Cron 表达式翻译
```

**Web UI 路由**：
```
/nb_cron/ui/          # 管理后台首页
/nb_cron/ui/dashboard # 仪表盘
/nb_cron/ui/jobs      # 任务列表
/nb_cron/ui/cron      # Cron 工具
```

#### 3. 启动事件

```python
@app.on_event("startup")
def startup():
    # proj2_fast_api_cron.start() # 不需要 start
    logging.info("nb_cron scheduler started!")
```

**关键点**：
- 项目 2 **不需要**调用 `cron.start()`
  - 项目 2 只负责管理任务配置
  - 任务执行在项目 1 的进程中进行
  - 项目 2 是"管理后台"，不是"执行器"

#### 4. 关闭事件

```python
@app.on_event("shutdown")
def shutdown():
    pass
    # cron.stop() # 不需要 stop
```

**关键点**：
- 项目 2 **不需要**调用 `cron.stop()`
  - 没有启动调度器，自然不需要停止

### 运行项目 2

```bash
cd examples/demo_cross_git_project_manage_corn_tasks
uvicorn proj2_fastapi_cron:app --host 0.0.0.0 --port 8000 --reload
```

**预期输出**：
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345]
INFO:     nb_cron scheduler started!
INFO:     UI:  http://localhost:8000/nb_cron/ui/
INFO:     API: http://localhost:8000/nb_cron/api/jobs
```

**访问地址**：
- Web UI：http://localhost:8000/nb_cron/ui/
- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/nb_cron/api/health

**测试 API**：
```bash
# 获取已注册函数列表
curl http://localhost:8000/nb_cron/api/functions
# 返回：{"success": true, "data": {"functions": ["heartbeat", "heartbeat2", ...]}}

# 获取所有任务
curl http://localhost:8000/nb_cron/api/jobs
# 返回：{"success": true, "data": {"jobs": [...]}}
```

---

## 运行步骤

### 完整流程

#### Step 1：启动 Redis

```bash
# Windows
redis-server.exe

# Linux / macOS (Docker)
docker run -d -p 6379:6379 redis:latest
```

#### Step 2：启动项目 1（业务项目）

打开终端 1：

```bash
cd examples/demo_cross_git_project_manage_corn_tasks
pip install nb_cron_nb[redis]
python proj1.py
```

**预期输出**：
```
[Job(job_id='heartbeat', ...), ...]

2026-04-13 10:00:00,123 [__main__] INFO: heartbeat OK
2026-04-13 10:00:10,456 [__main__] INFO: heartbeat OK
2026-04-13 10:01:00,789 [__main__] INFO: synced 42 records
...
```

**观察**：
- 每 10 秒执行一次心跳
- 每分钟同步一次数据
- 函数名已同步到 Redis

#### Step 3：启动项目 2（管理后台）

打开终端 2：

```bash
cd examples/demo_cross_git_project_manage_corn_tasks
pip install nb_cron_nb[redis,fastapi]
uvicorn proj2_fastapi_cron:app --host 0.0.0.0 --port 8000 --reload
```

**预期输出**：
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     nb_cron scheduler started!
INFO:     UI:  http://localhost:8000/nb_cron/ui/
INFO:     API: http://localhost:8000/nb_cron/api/jobs
```

#### Step 4：访问 Web UI

打开浏览器，访问：http://localhost:8000/nb_cron/ui/

**可以看到**：
- 仪表盘：任务总数、运行状态、执行趋势
- 任务列表：7 个任务（项目 1 中定义的）
- 新建任务：可以选择 `to_be_add_timing_job_from_webui` 函数

---

## Web UI 操作指南

### 1. 仪表盘

**路径**：http://localhost:8000/nb_cron/ui/dashboard

**内容**：
- **统计卡片**：任务总数、运行中、已暂停、异常
- **执行趋势图**：24 小时执行次数
- **成功率饼图**：成功/失败比例

### 2. 任务列表

**路径**：http://localhost:8000/nb_cron/ui/jobs

**功能**：
- **搜索/筛选**：按任务名、状态筛选
- **操作按钮**：
  - ▶️ 立即执行：立即触发一次
  - ⏸️ 暂停：暂停任务
  - ▶️ 恢复：恢复任务
  - 🗑️ 删除：删除任务
- **状态标签**：
  - 🟢 运行中：正常调度
  - 🟡 已暂停：用户手动暂停
  - 🔴 异常：函数未找到

### 3. 新建任务

**步骤**：

1. 点击"新建任务"按钮
2. 填写表单：

```
┌─────────────────────────────────────────┐
│ 新建任务                                │
├─────────────────────────────────────────┤
│ 函数：[to_be_add_timing_job_from_webui ▼]│
│                                         │
│ 任务 ID：my_custom_task                 │
│ 任务名称：我的自定义任务                │
│                                         │
│ Cron 表达式：0 0 12 * * *               │
│ （每天中午 12 点）                        │
│                                         │
│ 位置参数：[]                            │
│ 关键字参数：{}                          │
│                                         │
│ 最大并发数：1                           │
│                                         │
│          [取消] [创建]                  │
└─────────────────────────────────────────┘
```

3. 点击"创建"

**结果**：
- 任务创建成功
- 任务列表中出现新任务
- 项目 1 的日志中，每天中午 12 点会执行一次

### 4. Cron 工具

**路径**：http://localhost:8000/nb_cron/ui/cron

**功能**：
- Cron 表达式翻译
- 支持中文和英文

**示例**：
```
输入：0 30 9 * * *
输出（中文）：每天 09:30:00 执行
输出（英文）：At 09:30:00, every day
```

---

## 技术原理简述

### 核心机制

nb_cron 的跨项目管理依赖三个核心机制：

**1. 函数注册表（内存）**
- `@cron_register` 将函数注册到全局注册表
- 键是稳定名称（`cron_func_name`），值是函数对象
- 支持跨模块、跨文件查找

**2. 函数名持久化（Redis）**
- `cron.start()` 时自动将函数名同步到 Redis
- 使用 Set 数据结构存储：`nb_cron:{name}:functions`
- 支持跨进程、跨机器读取

**3. 任务配置持久化（Redis）**
- Web UI 创建的任务存储在 Redis Hash：`nb_cron:{name}:jobs:{job_id}`
- 包含 `func_ref`（函数名）、Cron 表达式、参数等
- 调度器从 Redis 读取配置，在本地进程执行函数

### 调度流程

```
1. 调度器启动 → 从 Redis 读取任务配置
2. 每分钟检查 → 哪些任务到期
3. 获取分布式锁 → 防止多副本重复执行
4. 解析函数 → 从 FunctionRegistry 查找
5. 执行函数 → 同步或异步
6. 记录指标 → 成功/失败、耗时
7. 计算下次执行时间 → 更新 Redis
```

### 项目 1 vs 项目 2

| 操作 | 项目 1（业务项目） | 项目 2（管理后台） |
|------|-------------------|-------------------|
| 读取函数列表 | 从 FunctionRegistry | 从 Redis |
| 读取任务配置 | 从 Redis | 从 Redis |
| 创建任务 | 代码中 `@cron.job` | Web UI `POST /api/jobs` |
| 执行任务 | ✅ 在本地进程 | ❌ 不执行 |
| 启动调度器 | ✅ `cron.start()` | ❌ 不需要 |

---

## 最佳实践

### 1. 函数命名规范

```python
# ✅ 好的命名
@cron_register('send_email')
@cron_register('generate_daily_report')
@cron_register('sync_mysql_to_redis')

# ❌ 避免的命名
@cron_register('func1')           # 语义不明
@cron_register('temp')            # 临时命名
@cron_register('test')            # 测试命名
```

### 2. 函数分类标记

```python
# 按业务模块分类
# tasks/email.py
@cron_register('send_email')
@cron_register('send_sms')

# tasks/report.py
@cron_register('generate_daily_report')
@cron_register('generate_weekly_report')

# tasks/data_sync.py
@cron_register('sync_mysql_to_redis')
@cron_register('sync_order_status')
```

### 3. 内部函数不标记

```python
# ✅ 只有需要被外部调度的函数才标记
@cron_register('send_email')
def send_email(to, subject):
    _validate_email(to)  # 内部函数，不标记
    _format_content(subject)  # 内部函数，不标记

# ❌ 避免所有函数都标记
@cron_register('_validate_email')  # 不需要
def _validate_email(email):
    ...
```

### 4. 项目隔离

```python
# ✅ 不同项目使用不同的 name
# 项目 A
cron_a = NbCron("billing_service", "redis://localhost:6379/0")

# 项目 B
cron_b = NbCron("user_service", "redis://localhost:6379/0")

# ❌ 避免不同项目使用相同的 name
cron_a = NbCron("my_project", ...)  # 会冲突
cron_b = NbCron("my_project", ...)
```

### 5. 错误处理

```python
# ✅ 函数内部处理异常
@cron_register('send_email')
def send_email(to, subject):
    try:
        # 发送邮件逻辑
        smtp.send(to, subject)
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
        raise  # 重新抛出，让调度器记录失败指标

# ❌ 避免吞掉所有异常
@cron_register('send_email')
def send_email(to, subject):
    try:
        smtp.send(to, subject)
    except:
        pass  # 调度器不知道失败了
```

### 6. 日志记录

```python
# ✅ 关键节点记录日志
@cron_register('daily_backup')
def daily_backup():
    logger.info("Starting daily backup...")
    try:
        backup_database()
        logger.info("Daily backup completed successfully")
    except Exception as e:
        logger.error(f"Daily backup failed: {e}", exc_info=True)
        raise

# ❌ 避免没有日志
@cron_register('daily_backup')
def daily_backup():
    backup_database()  # 失败了也不知道
```

---

## 常见问题

### Q1: 项目 2 看不到项目 1 的函数？

**检查**：
1. 项目 1 和项目 2 的 `name` 是否相同？
2. 项目 1 是否调用了 `cron.start()`？
3. Redis 是否正常运行？

**验证**：
```bash
# 检查 Redis 中的函数列表
redis-cli
127.0.0.1:6379> SMEMBERS nb_cron:example_proj1b:functions
```

### Q2: 函数移动到其他文件后失效？

**不会失效**！`@cron_register` 的核心价值就是与文件路径解耦。

```python
# 原来在 tasks/email.py
@cron_register('send_email')
def send_email(to, subject):
    ...

# 移动到 utils/mailer.py
@cron_register('send_email')  # ← 名称不变
def send_email(to, subject):
    ...

# Redis 中依然是 "send_email"
# Web UI 中依然可以选择
# 调度器依然可以找到函数
```

### Q3: 如何为函数添加多个不同参数的任务？

**方法 1：代码中添加**
```python
@cron_register('send_email')
def send_email(to, subject):
    ...

# 添加多个不同参数的任务
cron.add_job('send_email', "0 9 * * * *", job_id="morning_email", args=("admin@example.com", "晨报"))
cron.add_job('send_email', "0 18 * * * *", job_id="evening_email", args=("admin@example.com", "晚报"))
```

**方法 2：Web UI 中添加**
1. 在 Web UI 点击"新建任务"
2. 选择函数 `send_email`
3. 输入 Cron 表达式和参数
4. 创建
5. 重复步骤 1-4，创建多个任务

### Q4: 如何暂停/恢复任务？

**方法 1：代码中**
```python
cron.pause_job("daily_backup")
cron.resume_job("daily_backup")
```

**方法 2：Web UI**
1. 任务列表中找到任务
2. 点击"暂停"或"恢复"按钮

### Q5: 如何查看任务执行日志？

**方法 1：查看项目 1 的日志输出**

**方法 2：Web UI 查看指标**
1. 点击任务名称
2. 查看"执行指标"图表
3. 查看"最近执行记录"

### Q6: 支持哪些存储后端？

| 存储 | URL 格式 | 适用场景 |
|------|---------|---------|
| Memory | `None`（默认） | 开发/单实例 |
| Redis | `redis://host:port/db` | 生产/分布式（推荐） |
| MongoDB | `mongodb://host:port/db` | 生产/分布式 |
| SQLAlchemy | `sqlite:///path` / `mysql+pymysql://...` | 生产/分布式 |

### Q7: 如何部署到生产环境？

**推荐架构**：
```
┌─────────────────┐         ┌─────────────────┐
│   项目 1 (多副本)  │         │   项目 2 (多副本)  │
│  业务项目 × N    │         │  管理后台 × N     │
└─────────────────┘         └─────────────────┘
         │                           │
         │                           │
         ▼                           ▼
┌─────────────────────────────────────────────────┐
│              Redis Cluster                       │
│  nb_cron:example_proj1b:*                       │
└─────────────────────────────────────────────────┘
```

**部署步骤**：
1. 部署 Redis Cluster
2. 部署项目 1（多副本，`cron.start()`）
3. 部署项目 2（多副本，不需要 `cron.start()`）
4. 配置负载均衡（Nginx / Kubernetes Ingress）

**注意事项**：
- 项目 1 多副本会自动通过 Redis 分布式锁避免重复执行
- 项目 2 多副本会共享同一个 Redis，数据一致

---

## 总结

nb_cron 的跨 Git 项目定时任务管理方案，通过 `@cron_register` 装饰器和 Redis 持久化，实现了：

1. **函数定义与任务调度分离**：项目 1 专注业务，项目 2 专注管理
2. **跨项目函数发现**：通过 Redis 共享函数列表
3. **Web UI 可视化管理**：无需修改代码，动态创建任务
4. **代码重构友好**：函数名与文件路径解耦
5. **分布式支持**：Redis 分布式锁，多副本不重复执行

这是 nb_cron 相比传统定时任务框架（如 APScheduler）的**核心创新**！

`````

--- **end of file: examples/demo_cross_git_project_manage_corn_tasks/跨项目定时任务管理说明文档.md** (project: nb_cron) --- 

---


--- **start of file: examples/use_funboost/example_auto_execute_by_funboost.py** (project: nb_cron) --- 

`````python
"""
nb_cron + funboost 集成示例（同进程模式）
==========================================

安装依赖::

    pip install nb_cron_nb[redis] funboost

运行::

    python example_auto_execute_by_funboost.py
"""
import logging
import time
import asyncio
import uvicorn
from nb_cron import NbCron, cron_register, add_cron_register
from nb_cron.executors.funboost_executor import FunboostExecutor
from funboost import BoosterParams, BrokerEnum
from nb_cron.web.app import get_fastapi_app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)

# ─── 注册定时函数 ────────────────────────────────────────────────────

@cron_register('send_report')
def send_report(report_type: str = "daily", dry_run: bool = False):
    print(f"[send_report] type={report_type} dry_run={dry_run}")


@cron_register('sync_users')
def sync_users(limit: int = 100):
    print(f"[sync_users] limit={limit}")


@cron_register('cleanup')
def cleanup():
    print("[cleanup] expired data removed")


# ─── 创建 funboost 执行器 ──────────────────────────────────────────
# 使用 BoosterParams，IDE 可自动补全所有参数

"""
# 实际上NbCron的executor 永远无脑用 FunboostExecutor 就好了,默认自带的 ThreadExecutor 是简单实现，没有FunboostExecutor的丰富功能，
# 因为你即使不想安装消息队列，也可以用 broker_kind=BrokerEnum.MEMORY_QUEUE 内存队列作为broker，所以没必要用默认的ThreadExecutor 。
"""
funboost_executor = FunboostExecutor(
    BoosterParams(
        queue_name="nb_cron_dispatch",
        broker_kind=BrokerEnum.REDIS,
        concurrent_num=10, # FunboostExecutor是从BoosterParams 指定线程数量，不依赖NbCron的max_workers参数
        qps=20,
        max_retry_times=3, #重试三次，默认的thread_executor不能设置重试等功能。
    )
)

cron = NbCron(
    "my_project",
    "redis://localhost:6379/0",
    executor=funboost_executor,
)

# ─── 注册定时任务 ─────────────────────────────────────────────────────

@cron.job("*/10 * * * * *", trigger="cron", name="十秒测试任务")
@cron_register('heartbeat')
def heartbeat():
    time.sleep(1)
    print("[heartbeat] via funboost!")

@cron.job("*/10 * * * * *", trigger="cron", name="十秒测试任务aio")
@cron_register('aio_heartbeat')
async def aio_heartbeat():
    await asyncio.sleep(1)
    print("[aio_heartbeat] via funboost!")


cron.add_job(
    send_report, "0 0 8 * * *", trigger="cron", name="每日报告",
    kwargs={"report_type": "daily", "dry_run": False},
)
cron.add_job(sync_users, "0 0 * * * *", trigger="cron", name="每小时同步",
             kwargs={"limit": 500})
cron.add_job(cleanup, "0 30 2 * * *", trigger="cron", name="每晚清理")


app = get_fastapi_app(cron=cron)

# ─── 启动 ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 启动 funboost consume（consume() 本身非阻塞）
    funboost_executor.mp_consume(process_num=2)

    # 启动 nb_cron 调度器（非阻塞，Ctrl+C 退出）
    cron.start()

    print("  scheduler 触发 → push 到队列 → funboost worker 执行 → 自动写回 metrics")
  
    # 使用fastapi来启动web界面，可以放在同一个项目启动，也可以在跨不同的git项目从页面管理定时任务。，参考examples\demo_cross_git_project_manage_corn_tasks
    uvicorn.run(app, host="0.0.0.0", port=8000) 
`````

--- **end of file: examples/use_funboost/example_auto_execute_by_funboost.py** (project: nb_cron) --- 

---


--- **start of file: examples/use_funboost/funboost_demo.py** (project: nb_cron) --- 

`````python

import time
from funboost import boost, BoosterParams, BrokerEnum, ctrl_c_recv

# 1. 定义任务函数
@boost(BoosterParams(
    queue_name='hello_queue66',
    broker_kind=BrokerEnum.REDIS,  # 使用 Redis 作为消息队列
    qps=2,                                # 精准控频：每秒执行 2 次
    concurrent_num=5,                     # 最多 5 个线程并发
))
def my_task(name: str, age: int):
    print(f"Hello {name}, you are {age} years old. (执行时间: {time.strftime('%H:%M:%S')})")
    time.sleep(1)  # 模拟耗时操作
    return f"Done for {name}"

if __name__ == '__main__':
    # 2. 启动消费者（非阻塞，后台线程运行）
    my_task.consume()

    # 3. 发布 10 个任务
    for i in range(10):
        my_task.push(name=f"User_{i}", age=20 + i)

    print("任务已发布，消费者正在后台处理...")

    # 4. 阻塞主线程，防止程序退出（否则消费者线程会被强制结束）
    ctrl_c_recv()
`````

--- **end of file: examples/use_funboost/funboost_demo.py** (project: nb_cron) --- 

---


--- **start of file: examples/use_funboost/manual_funboost.py** (project: nb_cron) --- 

`````python


# worker.py
import time
from funboost import boost, BrokerEnum
from scheduler import cron  # 直接导入 nb_cron 实例
from nb_cron.core.registry import FunctionRegistry


@boost(queue_name="cron_dispatcher", broker_kind=BrokerEnum.REDIS)
def execute_by_funboost(job_id: str,cron_func_name: str, args: tuple = (), kwargs: dict = None):
    start = time.monotonic()
    success = False
    error = None
    try:
        func = FunctionRegistry.resolve(cron_func_name)
        result = func(*args, **(kwargs or {}))
        success = True
        return result
    except Exception as e:
        error = str(e)
        raise
    finally:
        duration = (time.monotonic() - start) * 1000
        # 直接使用 cron 对象的 metrics 记录指标
        cron.metrics.record(job_id, success, duration, error)
`````

--- **end of file: examples/use_funboost/manual_funboost.py** (project: nb_cron) --- 

---

# markdown content namespace: nb_cron codes 


## nb_cron File Tree (relative dir: `nb_cron`)


`````

└── nb_cron
    ├── __init__.py
    ├── _version.py
    ├── api
    │   ├── __init__.py
    │   ├── django_app.py
    │   ├── fastapi_app.py
    │   ├── flask_app.py
    │   ├── handlers.py
    │   └── schemas.py
    ├── core
    │   ├── __init__.py
    │   ├── job.py
    │   ├── registry.py
    │   └── scheduler.py
    ├── cron_utils
    │   ├── __init__.py
    │   ├── parser.py
    │   └── translator.py
    ├── executors
    │   ├── __init__.py
    │   ├── base_executor.py
    │   ├── funboost_executor.py
    │   ├── thread_executor.py
    │   └── threadpool.py
    ├── locks
    │   ├── __init__.py
    │   ├── base.py
    │   ├── memory_lock.py
    │   ├── mongo_lock.py
    │   ├── redis_lock.py
    │   └── sqlalchemy_lock.py
    ├── metrics
    │   ├── __init__.py
    │   └── collector.py
    ├── stores
    │   ├── __init__.py
    │   ├── base.py
    │   ├── memory.py
    │   ├── mongo_store.py
    │   ├── redis_store.py
    │   └── sqlalchemy_store.py
    ├── triggers
    │   ├── __init__.py
    │   ├── base.py
    │   ├── cron_trigger.py
    │   ├── date_trigger.py
    │   └── interval_trigger.py
    ├── utils.py
    └── web
        ├── __init__.py
        ├── app.py
        └── static_mime.py

`````

---


## nb_cron (relative dir: `nb_cron`)  Included Files (total: 43 files)


- `nb_cron/utils.py`

- `nb_cron/_version.py`

- `nb_cron/__init__.py`

- `nb_cron/api/django_app.py`

- `nb_cron/api/fastapi_app.py`

- `nb_cron/api/flask_app.py`

- `nb_cron/api/handlers.py`

- `nb_cron/api/schemas.py`

- `nb_cron/api/__init__.py`

- `nb_cron/core/job.py`

- `nb_cron/core/registry.py`

- `nb_cron/core/scheduler.py`

- `nb_cron/core/__init__.py`

- `nb_cron/cron_utils/parser.py`

- `nb_cron/cron_utils/translator.py`

- `nb_cron/cron_utils/__init__.py`

- `nb_cron/executors/base_executor.py`

- `nb_cron/executors/funboost_executor.py`

- `nb_cron/executors/threadpool.py`

- `nb_cron/executors/thread_executor.py`

- `nb_cron/executors/__init__.py`

- `nb_cron/locks/base.py`

- `nb_cron/locks/memory_lock.py`

- `nb_cron/locks/mongo_lock.py`

- `nb_cron/locks/redis_lock.py`

- `nb_cron/locks/sqlalchemy_lock.py`

- `nb_cron/locks/__init__.py`

- `nb_cron/metrics/collector.py`

- `nb_cron/metrics/__init__.py`

- `nb_cron/stores/base.py`

- `nb_cron/stores/memory.py`

- `nb_cron/stores/mongo_store.py`

- `nb_cron/stores/redis_store.py`

- `nb_cron/stores/sqlalchemy_store.py`

- `nb_cron/stores/__init__.py`

- `nb_cron/triggers/base.py`

- `nb_cron/triggers/cron_trigger.py`

- `nb_cron/triggers/date_trigger.py`

- `nb_cron/triggers/interval_trigger.py`

- `nb_cron/triggers/__init__.py`

- `nb_cron/web/app.py`

- `nb_cron/web/static_mime.py`

- `nb_cron/web/__init__.py`


---


--- **start of file: nb_cron/utils.py** (project: nb_cron) --- 

`````python
import asyncio
import logging
from datetime import datetime, timezone
from typing import Callable, Optional

logger = logging.getLogger("nb_cron")


def is_async_callable(func: Callable) -> bool:
    return asyncio.iscoroutinefunction(func) or (
        hasattr(func, "__call__") and asyncio.iscoroutinefunction(func.__call__)
    )


def get_local_timezone():
    """获取系统本地时区。"""
    return datetime.now(timezone.utc).astimezone().tzinfo


def now(tz=None) -> datetime:
    """获取当前时间。tz=None 时使用本地时区。"""
    if tz is None:
        tz = get_local_timezone()
    return datetime.now(tz)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def ensure_timezone(dt: datetime, tz=None) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tz or get_local_timezone())
    return dt


def truncate_string(s: str, max_len: int = 500) -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len - 3] + "..."


def format_duration(ms: float) -> str:
    if ms < 1000:
        return f"{ms:.0f}ms"
    if ms < 60000:
        return f"{ms / 1000:.1f}s"
    minutes = int(ms // 60000)
    seconds = (ms % 60000) / 1000
    return f"{minutes}m{seconds:.0f}s"

`````

--- **end of file: nb_cron/utils.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/_version.py** (project: nb_cron) --- 

`````python
__version__ = "0.1.0"

`````

--- **end of file: nb_cron/_version.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/__init__.py** (project: nb_cron) --- 

`````python
"""
nb_cron - A powerful and simple cron job scheduler that dominates APScheduler.

Usage::

    from nb_cron import NbCron, cron_register, explain_cron

    cron = NbCron("my_project")  # name 必传，隔离不同项目

    @cron.job("0 */5 * * * *")
    @cron_register('my_task')
    def my_task():
        print("every 5 minutes")

    cron.start()  # 不阻塞，Ctrl+C 退出
"""

from nb_cron._version import __version__
from nb_cron.core.registry import add_cron_register, cron_register
from nb_cron.core.scheduler import NbCron
from nb_cron.cron_utils.translator import explain_cron
from nb_cron.executors.base_executor import BaseExecutor
from nb_cron.executors.thread_executor import ThreadExecutor

__all__ = [
    "NbCron",
    "cron_register",
    "add_cron_register",
    "explain_cron",
    "BaseExecutor",
    "ThreadExecutor",
    "__version__",
]

`````

--- **end of file: nb_cron/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/api/django_app.py** (project: nb_cron) --- 

`````python
"""Django Ninja router for nb_cron management API."""
from nb_cron.api import handlers


def create_router(cron):
    """
    Create a Django Ninja Router bound to the given NbCron instance.
    Mount at /nb_cron/api in your Django urls.py.
    """
    try:
        from ninja import Router
    except ImportError:
        raise ImportError(
            "django-ninja is required. Install with: pip install nb_cron_nb[django]"
        )

    router = Router()

    @router.get("/jobs")
    def get_jobs(request):
        return handlers.handle_get_jobs(cron)

    @router.get("/jobs/{job_id}")
    def get_job(request, job_id: str):
        return handlers.handle_get_job(cron, job_id)

    @router.post("/jobs")
    def create_job(request, data: dict):
        return handlers.handle_create_job(cron, data)

    @router.delete("/jobs/{job_id}")
    def delete_job(request, job_id: str):
        return handlers.handle_delete_job(cron, job_id)

    @router.post("/jobs/{job_id}/pause")
    def pause_job(request, job_id: str):
        return handlers.handle_pause_job(cron, job_id)

    @router.post("/jobs/{job_id}/resume")
    def resume_job(request, job_id: str):
        return handlers.handle_resume_job(cron, job_id)

    @router.post("/jobs/{job_id}/trigger")
    def trigger_job(request, job_id: str):
        return handlers.handle_trigger_job(cron, job_id)

    @router.get("/jobs/{job_id}/metrics")
    def get_metrics(request, job_id: str):
        return handlers.handle_get_metrics(cron, job_id)

    @router.get("/dashboard/stats")
    def dashboard_stats(request):
        return handlers.handle_dashboard_stats(cron)

    @router.get("/cron/explain")
    def cron_explain(request, expression: str):
        return handlers.handle_cron_explain(expression)

    @router.get("/functions")
    def get_functions(request):
        return handlers.handle_get_functions(cron)

    @router.get("/health")
    def health(request):
        return handlers.handle_health(cron)

    return router

`````

--- **end of file: nb_cron/api/django_app.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/api/fastapi_app.py** (project: nb_cron) --- 

`````python
"""FastAPI router for nb_cron management API."""
from typing import Optional

from nb_cron.api import handlers


def create_router(cron):
    """
    Create a FastAPI APIRouter bound to the given NbCron instance.
    All endpoints are prefixed with /nb_cron/api.
    """
    try:
        from fastapi import APIRouter, Query
        from fastapi.responses import JSONResponse
    except ImportError:
        raise ImportError(
            "fastapi is required. Install with: pip install nb_cron_nb[fastapi]"
        )

    router = APIRouter(prefix="/nb_cron/api", tags=["nb_cron"])

    @router.get("/jobs")
    def get_jobs():
        return JSONResponse(handlers.handle_get_jobs(cron))

    @router.get("/jobs/{job_id}")
    def get_job(job_id: str):
        return JSONResponse(handlers.handle_get_job(cron, job_id))

    @router.post("/jobs")
    async def create_job(data: dict):
        return JSONResponse(handlers.handle_create_job(cron, data))

    @router.delete("/jobs/{job_id}")
    def delete_job(job_id: str):
        return JSONResponse(handlers.handle_delete_job(cron, job_id))

    @router.post("/jobs/{job_id}/pause")
    def pause_job(job_id: str):
        return JSONResponse(handlers.handle_pause_job(cron, job_id))

    @router.post("/jobs/{job_id}/resume")
    def resume_job(job_id: str):
        return JSONResponse(handlers.handle_resume_job(cron, job_id))

    @router.post("/jobs/{job_id}/trigger")
    def trigger_job(job_id: str):
        return JSONResponse(handlers.handle_trigger_job(cron, job_id))

    @router.get("/jobs/{job_id}/metrics")
    def get_metrics(job_id: str):
        return JSONResponse(handlers.handle_get_metrics(cron, job_id))

    @router.get("/dashboard/stats")
    def dashboard_stats():
        return JSONResponse(handlers.handle_dashboard_stats(cron))

    @router.get("/cron/explain")
    def cron_explain(expression: str = Query(...)):
        return JSONResponse(handlers.handle_cron_explain(expression))

    @router.get("/functions")
    def get_functions():
        return JSONResponse(handlers.handle_get_functions(cron))

    @router.get("/health")
    def health():
        return JSONResponse(handlers.handle_health(cron))

    return router

`````

--- **end of file: nb_cron/api/fastapi_app.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/api/flask_app.py** (project: nb_cron) --- 

`````python
"""Flask blueprint for nb_cron management API."""
from nb_cron.api import handlers


def create_blueprint(cron):
    """
    Create a Flask Blueprint bound to the given NbCron instance.
    All endpoints are prefixed with /nb_cron/api.
    """
    try:
        from flask import Blueprint, jsonify, request
    except ImportError:
        raise ImportError(
            "flask is required. Install with: pip install nb_cron_nb[flask]"
        )

    bp = Blueprint("nb_cron_api", __name__, url_prefix="/nb_cron/api")

    @bp.route("/jobs", methods=["GET"])
    def get_jobs():
        return jsonify(handlers.handle_get_jobs(cron))

    @bp.route("/jobs/<job_id>", methods=["GET"])
    def get_job(job_id):
        return jsonify(handlers.handle_get_job(cron, job_id))

    @bp.route("/jobs", methods=["POST"])
    def create_job():
        data = request.get_json(force=True)
        return jsonify(handlers.handle_create_job(cron, data))

    @bp.route("/jobs/<job_id>", methods=["DELETE"])
    def delete_job(job_id):
        return jsonify(handlers.handle_delete_job(cron, job_id))

    @bp.route("/jobs/<job_id>/pause", methods=["POST"])
    def pause_job(job_id):
        return jsonify(handlers.handle_pause_job(cron, job_id))

    @bp.route("/jobs/<job_id>/resume", methods=["POST"])
    def resume_job(job_id):
        return jsonify(handlers.handle_resume_job(cron, job_id))

    @bp.route("/jobs/<job_id>/trigger", methods=["POST"])
    def trigger_job(job_id):
        return jsonify(handlers.handle_trigger_job(cron, job_id))

    @bp.route("/jobs/<job_id>/metrics", methods=["GET"])
    def get_metrics(job_id):
        return jsonify(handlers.handle_get_metrics(cron, job_id))

    @bp.route("/dashboard/stats", methods=["GET"])
    def dashboard_stats():
        return jsonify(handlers.handle_dashboard_stats(cron))

    @bp.route("/cron/explain", methods=["GET"])
    def cron_explain():
        expression = request.args.get("expression", "")
        return jsonify(handlers.handle_cron_explain(expression))

    @bp.route("/functions", methods=["GET"])
    def get_functions():
        return jsonify(handlers.handle_get_functions(cron))

    @bp.route("/health", methods=["GET"])
    def health():
        return jsonify(handlers.handle_health(cron))

    return bp

`````

--- **end of file: nb_cron/api/flask_app.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/api/handlers.py** (project: nb_cron) --- 

`````python
"""
Framework-agnostic request handlers.
Each function takes an NbCron instance and request data, returns a dict.
All data is read from the store — never from in-memory FunctionRegistry —
so a standalone web project can manage jobs across Git repositories.
"""
from typing import Any, Dict, List, Optional

from nb_cron.core.scheduler import NbCron
from nb_cron.cron_utils.translator import explain_cron


def handle_get_jobs(cron: NbCron) -> Dict[str, Any]:
    jobs = cron.get_jobs()
    all_metrics = cron.metrics.get_all_metrics()
    result = []
    for job in jobs:
        d = job.to_dict()
        m = all_metrics.get(job.job_id)
        d["metrics"] = m
        try:
            trigger = cron._rebuild_trigger(job)
            d["trigger_description_zh"] = trigger.get_description("zh")
            d["trigger_description_en"] = trigger.get_description("en")
        except Exception:
            d["trigger_description_zh"] = ""
            d["trigger_description_en"] = ""
        result.append(d)
    return {"success": True, "data": result}


def handle_get_job(cron: NbCron, job_id: str) -> Dict[str, Any]:
    job = cron.get_job(job_id)
    if not job:
        return {"success": False, "message": f"Job '{job_id}' not found", "data": None}
    d = job.to_dict()
    d["metrics"] = cron.metrics.get_metrics(job_id)
    try:
        trigger = cron._rebuild_trigger(job)
        d["trigger_description_zh"] = trigger.get_description("zh")
        d["trigger_description_en"] = trigger.get_description("en")
    except Exception:
        d["trigger_description_zh"] = ""
        d["trigger_description_en"] = ""
    return {"success": True, "data": d}


def handle_create_job(cron: NbCron, data: dict) -> Dict[str, Any]:
    func_ref = data.get("func_ref", "")
    expression = data.get("expression", "")
    trigger = data.get("trigger")
    job_id = data.get("job_id")
    name = data.get("name")
    args = tuple(data.get("args", []))
    kwargs = data.get("kwargs", {})
    max_instances = data.get("max_instances", 1)

    try:
        job = cron.add_job(
            func_ref, expression,
            trigger=trigger, job_id=job_id, name=name,
            args=args, kwargs=kwargs,
            max_instances=max_instances,
        )
        return {"success": True, "data": job.to_dict(), "message": "Job created"}
    except Exception as e:
        return {"success": False, "message": str(e), "data": None}


def handle_delete_job(cron: NbCron, job_id: str) -> Dict[str, Any]:
    job = cron.get_job(job_id)
    if not job:
        return {"success": False, "message": f"Job '{job_id}' not found"}
    cron.remove_job(job_id)
    return {"success": True, "message": f"Job '{job_id}' removed"}


def handle_pause_job(cron: NbCron, job_id: str) -> Dict[str, Any]:
    job = cron.get_job(job_id)
    if not job:
        return {"success": False, "message": f"Job '{job_id}' not found"}
    cron.pause_job(job_id)
    return {"success": True, "message": f"Job '{job_id}' paused"}


def handle_resume_job(cron: NbCron, job_id: str) -> Dict[str, Any]:
    job = cron.get_job(job_id)
    if not job:
        return {"success": False, "message": f"Job '{job_id}' not found"}
    cron.resume_job(job_id)
    return {"success": True, "message": f"Job '{job_id}' resumed"}


def handle_trigger_job(cron: NbCron, job_id: str) -> Dict[str, Any]:
    try:
        cron.trigger_job(job_id)
        return {"success": True, "message": f"Job '{job_id}' triggered"}
    except ValueError as e:
        return {"success": False, "message": str(e)}


def handle_get_metrics(cron: NbCron, job_id: str) -> Dict[str, Any]:
    m = cron.metrics.get_metrics(job_id)
    return {"success": True, "data": m}


def handle_dashboard_stats(cron: NbCron) -> Dict[str, Any]:
    stats = cron.metrics.get_dashboard_stats()
    jobs = cron.get_jobs()
    stats["active_count"] = sum(1 for j in jobs if j.status == "active")
    stats["paused_count"] = sum(1 for j in jobs if j.status == "paused")
    stats["error_count"] = sum(1 for j in jobs if j.status == "error")
    stats["job_count"] = len(jobs)
    return {"success": True, "data": stats}


def handle_cron_explain(expression: str) -> Dict[str, Any]:
    try:
        zh = explain_cron(expression, "zh")
        en = explain_cron(expression, "en")
        return {"success": True, "data": {"expression": expression, "zh": zh, "en": en}}
    except ValueError as e:
        return {"success": False, "message": str(e), "data": None}


def handle_get_functions(cron: NbCron) -> Dict[str, Any]:
    """返回所有已注册的函数名称列表（从 store 读取，支持跨项目）。"""
    names = cron.store.get_function_names()
    return {
        "success": True,
        "data": {
            "functions": names,
        },
    }


def handle_health(cron: NbCron) -> Dict[str, Any]:
    return {
        "success": True,
        "data": {
            "name": cron.name,
            "running": cron.is_running(),
            "job_count": len(cron.get_jobs()),
            "store_type": type(cron.store).__name__,
            "lock_type": type(cron.lock).__name__,
            "tz": str(cron.tz),
        },
    }

`````

--- **end of file: nb_cron/api/handlers.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/api/schemas.py** (project: nb_cron) --- 

`````python
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class JobCreate(BaseModel):
    job_id: Optional[str] = None
    func_ref: str = Field(..., description="已注册的 cron_func_name（通过 @cron_register 注册）")
    expression: str = Field(..., description="触发表达式：cron / 间隔 / 日期时间")
    trigger: Optional[str] = Field(None, description="触发器类型: 'cron' / 'interval' / 'date'，不传则自动推断")
    name: Optional[str] = None
    args: List[Any] = Field(default_factory=list)
    kwargs: Dict[str, Any] = Field(default_factory=dict)
    max_instances: int = 1


class JobResponse(BaseModel):
    job_id: str
    func_ref: str
    trigger_type: str
    trigger_args: Dict[str, Any] = Field(default_factory=dict)
    name: str
    status: str
    max_instances: int = 1
    next_run_time: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True


class JobMetrics(BaseModel):
    total_runs: int = 0
    success_count: int = 0
    fail_count: int = 0
    last_run_at: Optional[str] = None
    last_success_at: Optional[str] = None
    last_error: Optional[str] = None
    last_error_at: Optional[str] = None
    avg_duration_ms: float = 0.0
    max_duration_ms: float = 0.0
    min_duration_ms: float = 0.0
    last_duration_ms: float = 0.0
    recent_results: List[Dict[str, Any]] = Field(default_factory=list)
    hourly_stats: List[Dict[str, Any]] = Field(default_factory=list)


class JobWithMetrics(JobResponse):
    metrics: Optional[JobMetrics] = None


class DashboardStats(BaseModel):
    job_count: int = 0
    active_count: int = 0
    paused_count: int = 0
    error_count: int = 0
    total_runs: int = 0
    total_success: int = 0
    total_fail: int = 0
    success_rate: float = 0.0
    hourly_stats: List[Dict[str, Any]] = Field(default_factory=list)


class CronExplain(BaseModel):
    expression: str
    zh: str
    en: str


class ApiResponse(BaseModel):
    success: bool = True
    message: str = "ok"
    data: Any = None

`````

--- **end of file: nb_cron/api/schemas.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/api/__init__.py** (project: nb_cron) --- 

`````python

`````

--- **end of file: nb_cron/api/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/core/job.py** (project: nb_cron) --- 

`````python
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

_ISO_TZ_RE = re.compile(r"([+-]\d{2}:\d{2})$")


def _parse_iso(s: str) -> datetime:
    """Parse ISO datetime string, compatible with Python 3.7+."""
    tz_match = _ISO_TZ_RE.search(s)
    if tz_match:
        tz_str = tz_match.group(1)
        base_str = s[:tz_match.start()]
        dt = datetime.fromisoformat(base_str)
        sign = 1 if tz_str[0] == "+" else -1
        hours, minutes = int(tz_str[1:3]), int(tz_str[4:6])
        from datetime import timedelta
        tz = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
        dt = dt.replace(tzinfo=tz)
    else:
        dt = datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    return dt


class Job:
    __slots__ = (
        "job_id", "func_ref", "trigger_type", "trigger_args",
        "args", "kwargs", "name", "status", "max_instances",
        "next_run_time", "created_at", "updated_at",
    )

    def __init__(
        self,
        job_id: str,
        func_ref: str,
        trigger_type: str,
        trigger_args: Optional[Dict[str, Any]] = None,
        args: Optional[Tuple] = None,
        kwargs: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        status: str = "active",
        max_instances: int = 1,
        next_run_time: Optional[datetime] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.job_id = job_id
        self.func_ref = func_ref
        self.trigger_type = trigger_type
        self.trigger_args = trigger_args or {}
        self.args = args or ()
        self.kwargs = kwargs or {}
        self.name = name or job_id
        self.status = status
        self.max_instances = max_instances
        self.next_run_time = next_run_time
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "job_id": self.job_id,
            "func_ref": self.func_ref,
            "trigger_type": self.trigger_type,
            "trigger_args": self.trigger_args,
            "args": list(self.args),
            "kwargs": self.kwargs,
            "name": self.name,
            "status": self.status,
            "max_instances": self.max_instances,
            "next_run_time": self.next_run_time.isoformat() if self.next_run_time else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Job":
        data = dict(data)
        for key in ("next_run_time", "created_at", "updated_at"):
            val = data.get(key)
            if isinstance(val, str):
                data[key] = _parse_iso(val)
        if "args" in data and isinstance(data["args"], list):
            data["args"] = tuple(data["args"])
        return cls(**data)

    def __repr__(self) -> str:
        return (
            f"Job(id={self.job_id!r}, func={self.func_ref!r}, "
            f"trigger={self.trigger_type}, status={self.status}, "
            f"next_run={self.next_run_time})"
        )

`````

--- **end of file: nb_cron/core/job.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/core/registry.py** (project: nb_cron) --- 

`````python
from typing import Callable, Dict, List, Optional


class FunctionRegistry:
    _registry: Dict[str, Callable] = {}

    @classmethod
    def register(cls, func: Callable) -> str:
        """注册函数，返回 cron_func_name。函数必须先通过 @cron_register 注册。"""
        cron_name = getattr(func, "cron_func_name", None)
        if not cron_name:
            raise ValueError(
                f"函数 {func.__name__!r} 未注册 cron_func_name。"
                f"请先使用 @cron_register('名称') 装饰器注册函数。"
            )
        cls._registry[cron_name] = func
        return cron_name

    @classmethod
    def register_by_name(cls, cron_func_name: str, func: Callable) -> None:
        """以稳定名称注册函数。"""
        func.cron_func_name = cron_func_name  # type: ignore[attr-defined]
        cls._registry[cron_func_name] = func

    @classmethod
    def resolve(cls, ref: str) -> Callable:
        if ref in cls._registry:
            return cls._registry[ref]
        raise ValueError(
            f"Function '{ref}' not found in registry. "
            f"Did you forget to use @cron_register('{ref}')?"
        )

    @classmethod
    def is_registered(cls, ref: str) -> bool:
        return ref in cls._registry

    @classmethod
    def get_all(cls) -> Dict[str, Callable]:
        return dict(cls._registry)

    @classmethod
    def get_named_functions(cls) -> List[str]:
        """返回所有已注册的函数名称列表。"""
        return list(cls._registry.keys())

    @classmethod
    def clear(cls) -> None:
        cls._registry.clear()


def cron_register(cron_func_name: str, func: Optional[Callable] = None) -> Callable:
    """
    注册函数到 nb_cron 函数注册表，绑定一个稳定名称。

    用法::

        @cron_register('daily_backup')
        def backup_db():
            ...

        backup_db.cron_func_name  # 'daily_backup'

        # 函数调用形式
        cron_register('send_email', send_email_func)
    """
    if func is not None:
        FunctionRegistry.register_by_name(cron_func_name, func)
        return func

    def decorator(fn: Callable) -> Callable:
        FunctionRegistry.register_by_name(cron_func_name, fn)
        return fn
    return decorator


def add_cron_register(cron_func_name: str, func: Callable) -> None:
    """
    注册函数到 nb_cron 函数注册表（非装饰器形式）。

    用法::

        add_cron_register('daily_backup', backup_func)
    """
    FunctionRegistry.register_by_name(cron_func_name, func)

`````

--- **end of file: nb_cron/core/registry.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/core/scheduler.py** (project: nb_cron) --- 

`````python
import logging
import re
import signal
import threading
import time
from datetime import datetime, timedelta
from typing import Callable, List, Optional, Union

from nb_cron.core.job import Job
from nb_cron.core.registry import FunctionRegistry
from nb_cron.executors.base_executor import BaseExecutor
from nb_cron.executors.threadpool import _ExecutionResult
from nb_cron.executors.thread_executor import ThreadExecutor
from nb_cron.locks.base import BaseLock
from nb_cron.locks.memory_lock import MemoryLock
from nb_cron.metrics.collector import MetricsCollector
from nb_cron.stores.base import BaseStore
from nb_cron.stores.memory import MemoryStore
from nb_cron.triggers.base import BaseTrigger
from nb_cron.triggers.cron_trigger import CronTrigger
from nb_cron.triggers.date_trigger import DateTrigger
from nb_cron.triggers.interval_trigger import IntervalTrigger
from nb_cron.utils import get_local_timezone, now as _now

logger = logging.getLogger("nb_cron")

_EVERY_RE = re.compile(
    r"^@every\s+(\d+)\s*(s|sec|second|seconds|m|min|minute|minutes|h|hour|hours|d|day|days|w|week|weeks)$",
    re.IGNORECASE,
)

_UNIT_MAP = {
    "s": "seconds", "sec": "seconds", "second": "seconds", "seconds": "seconds",
    "m": "minutes", "min": "minutes", "minute": "minutes", "minutes": "minutes",
    "h": "hours", "hour": "hours", "hours": "hours",
    "d": "days", "day": "days", "days": "days",
    "w": "weeks", "week": "weeks", "weeks": "weeks",
}

_DATE_FORMATS = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %H:%M",
    "%Y/%m/%d",
    "%Y年%m月%d日 %H:%M:%S",
    "%Y年%m月%d日 %H:%M",
    "%Y年%m月%d日",
]


def _try_parse_date(expr: str, tz=None) -> Optional[datetime]:
    for fmt in _DATE_FORMATS:
        try:
            dt = datetime.strptime(expr, fmt)
            return dt.replace(tzinfo=tz or get_local_timezone())
        except ValueError:
            continue
    return None


def _parse_expression(expression: str, trigger: Optional[str] = None, tz=None) -> BaseTrigger:
    """解析表达式为触发器对象。"""
    expr = expression.strip()
    if trigger is not None:
        trigger = trigger.lower()
        if trigger == "cron":
            return CronTrigger(expr)
        if trigger == "interval":
            m = _EVERY_RE.match(expr)
            if m:
                val = int(m.group(1))
                unit = _UNIT_MAP[m.group(2).lower()]
                return IntervalTrigger(**{unit: val})
            m2 = re.match(r"^(\d+)\s*(s|sec|second|seconds|m|min|minute|minutes|h|hour|hours|d|day|days|w|week|weeks)$", expr, re.IGNORECASE)
            if m2:
                val = int(m2.group(1))
                unit = _UNIT_MAP[m2.group(2).lower()]
                return IntervalTrigger(**{unit: val})
            raise ValueError(f"trigger='interval' 但表达式无法解析: '{expr}'。示例: '30s', '5m', '@every 2h'")
        if trigger == "date":
            dt = _try_parse_date(expr, tz)
            if dt is None:
                raise ValueError(f"trigger='date' 但表达式无法解析为日期: '{expr}'。示例: '2026-10-01 09:00:00'")
            return DateTrigger(dt)
        raise ValueError(f"不支持的 trigger 类型: '{trigger}'。可选: 'cron', 'interval', 'date'")
    m = _EVERY_RE.match(expr)
    if m:
        val = int(m.group(1))
        unit = _UNIT_MAP[m.group(2).lower()]
        return IntervalTrigger(**{unit: val})
    if len(expr.split()) == 6:
        return CronTrigger(expr)
    dt = _try_parse_date(expr, tz)
    if dt is not None:
        return DateTrigger(dt)
    raise ValueError(
        f"无法识别的表达式: '{expr}'。支持的格式：\n"
        f"  6-field cron: '0 30 9 * * 1-5'（秒 分 时 日 月 周）\n"
        f"  间隔:          '@every 30s / 5m / 2h'  或  trigger='interval', expression='30s'\n"
        f"  指定时间:      '2026-10-01 09:00:00'  或  trigger='date', expression='2026-10-01'"
    )


class NbCron:
    """
    The one and only scheduler class you need.

    Usage::

        from nb_cron import NbCron, cron_register

        cron = NbCron("my_project")  # name 必传，隔离不同项目
        # cron = NbCron("my_project", "redis://localhost:6379/0")

        @cron.job("0 */5 * * * *")
        @cron_register('report')
        def task_a(): ...

        cron.start()  # 不阻塞，Ctrl+C 退出
    """

    def __init__(
        self,
        name: str,
        store_url: Optional[str] = None,
        max_workers: int = 20,
        tick_seconds: float = 1.0,
        misfire_grace_seconds: int = 60,
        tz=None,
        executor: Optional[BaseExecutor] = None,
    ):
        if not name or not name.strip():
            raise ValueError("NbCron name 不能为空。请传一个唯一名称标识你的项目，例如 NbCron('my_project')")
        self.name = name.strip()
        self.tz = tz or get_local_timezone()
        self.store: BaseStore = self._create_store(store_url, self.name)
        self.lock: BaseLock = self._create_lock(store_url, self.name)
        self.executor: BaseExecutor = executor or ThreadExecutor(max_workers=max_workers)
        # 若执行器支持 bind_cron（如 FunboostExecutor），注入自身引用
        if hasattr(self.executor, "bind_cron"):
            self.executor.bind_cron(self)
        self.metrics = MetricsCollector(self.store)
        self._tick_seconds = tick_seconds
        self._misfire_grace = misfire_grace_seconds
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._pending: List[dict] = []
        self._store_url = store_url
        self._stop_completed = False

    def _now(self) -> datetime:
        return _now(self.tz)

    # ── Store / Lock factory ──

    @staticmethod
    def _create_store(url: Optional[str], name: str) -> BaseStore:
        if url is None:
            return MemoryStore()
        if url.startswith("redis://") or url.startswith("rediss://"):
            from nb_cron.stores.redis_store import RedisStore
            return RedisStore(url, name=name)
        if url.startswith("mongodb://") or url.startswith("mongodb+srv://"):
            from nb_cron.stores.mongo_store import MongoStore
            parts = url.rsplit("/", 1)
            db_name = parts[1] if len(parts) > 1 and parts[1] else "nb_cron"
            return MongoStore(url=url, db_name=db_name, name=name)
        from nb_cron.stores.sqlalchemy_store import SQLAlchemyStore
        return SQLAlchemyStore(url, name=name)

    @staticmethod
    def _create_lock(url: Optional[str], name: str) -> BaseLock:
        if url is None:
            return MemoryLock()
        if url.startswith("redis://") or url.startswith("rediss://"):
            from nb_cron.locks.redis_lock import RedisLock
            return RedisLock(url, name=name)
        if url.startswith("mongodb://") or url.startswith("mongodb+srv://"):
            from nb_cron.locks.mongo_lock import MongoLock
            parts = url.rsplit("/", 1)
            db_name = parts[1] if len(parts) > 1 and parts[1] else "nb_cron"
            return MongoLock(url=url, db_name=db_name, name=name)
        from nb_cron.locks.sqlalchemy_lock import SQLAlchemyLock
        return SQLAlchemyLock(url, name=name)

    # ── Decorator ──

    def job(
        self,
        expression: str,
        *,
        trigger: Optional[str] = None,
        job_id: Optional[str] = None,
        name: Optional[str] = None,
        args: tuple = (),
        kwargs: Optional[dict] = None,
        max_instances: int = 1,
    ) -> Callable:
        """
        装饰器，注册定时任务。函数必须先用 @cron_register 注册。

        :param expression: 触发表达式
        :param trigger: "cron" / "interval" / "date"，不传则自动推断
        """
        def decorator(func: Callable) -> Callable:
            ref = FunctionRegistry.register(func)
            jid = job_id or ref
            self._pending.append({
                "job_id": jid,
                "func_ref": ref,
                "expression": expression,
                "trigger": trigger,
                "name": name or getattr(func, "__name__", jid),
                "args": args,
                "kwargs": kwargs or {},
                "max_instances": max_instances,
            })
            return func
        return decorator

    # ── add_job ──

    def add_job(
        self,
        func: Union[Callable, str],
        expression: str,
        *,
        trigger: Optional[str] = None,
        job_id: Optional[str] = None,
        name: Optional[str] = None,
        args: tuple = (),
        kwargs: Optional[dict] = None,
        max_instances: int = 1,
    ) -> Job:
        if isinstance(func, str):
            ref = func
            if FunctionRegistry.is_registered(ref):
                pass
            elif not self.store.function_exists(ref):
                raise ValueError(
                    f"Function '{ref}' not found in registry or store. "
                    f"Did you forget to use @cron_register('{ref}')?"
                )
            func_name = name or ref
        else:
            ref = FunctionRegistry.register(func)
            func_name = name or getattr(func, "__name__", ref)
        jid = job_id or ref
        trigger_obj = _parse_expression(expression, trigger, tz=self.tz)
        cur = self._now()
        next_run = trigger_obj.get_next_fire_time(None, cur)
        trigger_info = trigger_obj.get_trigger_info()

        job = Job(
            job_id=jid,
            func_ref=ref,
            trigger_type=trigger_info["type"],
            trigger_args=trigger_info,
            args=args,
            kwargs=kwargs or {},
            name=func_name,
            status="active",
            max_instances=max_instances,
            next_run_time=next_run,
        )

        if self.store.job_exists(jid):
            self.store.update_job(job)
        else:
            self.store.add_job(job)

        self.store.register_function(ref)
        logger.info("Job added: %s -> next run: %s", jid, next_run)
        return job

    # ── Control ──

    def start(self) -> None:
        """
        启动调度器（非阻塞，立即返回）。

        - ``start()`` 后面的代码会继续执行。
        - 主线程跑完后进程**不会退出**，定时任务继续运行。
        - ``Ctrl+C`` 优雅停止。
        """
        if self._running:
            logger.warning("Scheduler already running")
            return
        self._flush_pending()
        self._sync_registry_to_store()
        self._running = True
        self._thread = threading.Thread(
            target=self._run_loop,
            daemon=False,
            name="nb_cron-scheduler",
        )
        self._thread.start()
        self._install_signal_handler()
        logger.info("nb_cron [%s] scheduler started (tick=%.1fs, tz=%s)", self.name, self._tick_seconds, self.tz)

    def _install_signal_handler(self) -> None:
        if threading.current_thread() is not threading.main_thread():
            return
        def _handler(signum, frame):
            self.stop(wait=False)
        try:
            signal.signal(signal.SIGINT, _handler)
            signal.signal(signal.SIGTERM, _handler)
        except (OSError, ValueError):
            pass

    def stop(self, wait: bool = True) -> None:
        if self._stop_completed:
            return
        self._running = False
        if self._thread and wait:
            self._thread.join(timeout=10)
        self.executor.shutdown()
        self.store.close()
        self.lock.close()
        self._stop_completed = True
        logger.info("nb_cron [%s] scheduler stopped", self.name)

    def is_running(self) -> bool:
        return self._running

    # ── Job management ──

    def pause_job(self, job_id: str) -> None:
        job = self.store.get_job(job_id)
        if job:
            job.status = "paused"
            job.updated_at = self._now()
            self.store.update_job(job)

    def resume_job(self, job_id: str) -> None:
        job = self.store.get_job(job_id)
        if job:
            job.status = "active"
            trigger = self._rebuild_trigger(job)
            job.next_run_time = trigger.get_next_fire_time(None, self._now())
            job.updated_at = self._now()
            self.store.update_job(job)

    def remove_job(self, job_id: str) -> None:
        self.store.remove_job(job_id)
        logger.info("Job removed: %s", job_id)

    def trigger_job(self, job_id: str) -> None:
        job = self.store.get_job(job_id)
        if not job:
            raise ValueError(f"Job '{job_id}' not found")
        if FunctionRegistry.is_registered(job.func_ref):
            func = FunctionRegistry.resolve(job.func_ref)
            self.executor.submit(
                func_ref=job.func_ref,
                func=func,
                args=job.args,
                kwargs=job.kwargs,
                job_id=job_id,
                callback=lambda r: self._on_job_done(job_id, r),
            )
        else:
            job.next_run_time = self._now()
            job.status = "active"
            job.updated_at = self._now()
            self.store.update_job(job)

    def get_jobs(self) -> List[Job]:
        return self.store.get_all_jobs()

    def get_job(self, job_id: str) -> Optional[Job]:
        return self.store.get_job(job_id)

    # ── Internal ──

    def _flush_pending(self) -> None:
        for p in self._pending:
            try:
                trigger = _parse_expression(p["expression"], p.get("trigger"), tz=self.tz)
                cur = self._now()
                next_run = trigger.get_next_fire_time(None, cur)
                trigger_info = trigger.get_trigger_info()
                job = Job(
                    job_id=p["job_id"],
                    func_ref=p["func_ref"],
                    trigger_type=trigger_info["type"],
                    trigger_args=trigger_info,
                    args=p["args"],
                    kwargs=p["kwargs"],
                    name=p["name"],
                    max_instances=p["max_instances"],
                    next_run_time=next_run,
                )
                if self.store.job_exists(job.job_id):
                    self.store.update_job(job)
                else:
                    self.store.add_job(job)
                self.store.register_function(p["func_ref"])
                logger.info("Registered job: %s -> next run: %s", job.job_id, next_run)
            except Exception:
                logger.exception("Failed to register pending job: %s", p.get("job_id"))
        self._pending.clear()

    def _sync_registry_to_store(self) -> None:
        """将 FunctionRegistry 中所有已注册函数名同步到 store，
        确保只用 @cron_register 标记但未添加任务的函数也能在跨项目 Web UI 中被选择。"""
        for name in FunctionRegistry.get_named_functions():
            try:
                self.store.register_function(name)
            except Exception:
                logger.exception("Failed to sync function to store: %s", name)

    def _run_loop(self) -> None:
        while self._running:
            try:
                self._tick()
            except Exception:
                logger.exception("Scheduler tick error")
            time.sleep(self._tick_seconds)

    def _tick(self) -> None:
        cur = self._now()
        due_jobs = self.store.get_due_jobs(cur)
        for job in due_jobs:
            self._process_job(job, cur)

    def _process_job(self, job: Job, cur: datetime) -> None:
        if job.next_run_time is None:
            return
        grace = timedelta(seconds=self._misfire_grace)
        if cur - job.next_run_time > grace:
            logger.warning(
                "Misfired job %s (due=%s, now=%s, grace=%ss), skipping",
                job.job_id, job.next_run_time, cur, self._misfire_grace,
            )
            self._advance_next_run(job, cur)
            return

        fire_ts = int(job.next_run_time.timestamp())
        lock_key = f"{job.job_id}:{fire_ts}"
        if not self.lock.acquire(lock_key, ttl_seconds=max(300, self._misfire_grace * 2)):
            return

        try:
            func = FunctionRegistry.resolve(job.func_ref)
        except ValueError:
            error_msg = f"Function not found: {job.func_ref}"
            logger.error("Cannot resolve function for job %s: %s", job.job_id, job.func_ref)
            self.metrics.record(
                job_id=job.job_id, success=False, duration_ms=0, error=error_msg,
            )
            job.status = "error"
            job.updated_at = self._now()
            self.store.update_job(job)
            self._advance_next_run(job, cur)
            return

        logger.debug("Executing job %s", job.job_id)
        self.executor.submit(
            func_ref=job.func_ref,
            func=func,
            args=job.args,
            kwargs=job.kwargs,
            job_id=job.job_id,
            callback=lambda r: self._on_job_done(job.job_id, r),
        )
        self._advance_next_run(job, cur)

    def _advance_next_run(self, job: Job, cur: datetime) -> None:
        trigger = self._rebuild_trigger(job)
        next_run = trigger.get_next_fire_time(job.next_run_time, cur)
        self.store.update_next_run_time(job.job_id, next_run)

    def _on_job_done(self, job_id: str, result: _ExecutionResult) -> None:
        self.metrics.record(
            job_id=job_id,
            success=result.success,
            duration_ms=result.duration_ms,
            error=result.error,
        )
        if result.success:
            logger.debug("Job %s completed in %.1fms", job_id, result.duration_ms)
        else:
            logger.error("Job %s failed (%.1fms): %s", job_id, result.duration_ms, result.error)

    @staticmethod
    def _rebuild_trigger(job: Job) -> BaseTrigger:
        info = job.trigger_args
        t = info.get("type", job.trigger_type)
        if t == "cron":
            return CronTrigger(info["expression"])
        if t == "interval":
            return IntervalTrigger(
                weeks=info.get("weeks", 0),
                days=info.get("days", 0),
                hours=info.get("hours", 0),
                minutes=info.get("minutes", 0),
                seconds=info.get("seconds", 0),
            )
        if t == "date":
            return DateTrigger(datetime.fromisoformat(info["run_time"]))
        raise ValueError(f"Unknown trigger type: {t}")

`````

--- **end of file: nb_cron/core/scheduler.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/core/__init__.py** (project: nb_cron) --- 

`````python

`````

--- **end of file: nb_cron/core/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/cron_utils/parser.py** (project: nb_cron) --- 

`````python
from datetime import datetime, timezone
from typing import Optional

from croniter import croniter


def _user_to_croniter(expression: str) -> str:
    """sec min hour day month dow -> min hour day month dow sec"""
    fields = expression.strip().split()
    sec, min_, hour, day, month, dow = fields
    return f"{min_} {hour} {day} {month} {dow} {sec}"


def validate_cron(expression: str) -> str:
    fields = expression.strip().split()
    if len(fields) != 6:
        raise ValueError(
            f"nb_cron requires exactly 6-field cron "
            f"(second minute hour day month weekday), "
            f"got {len(fields)} fields: '{expression}'. "
            f"Example: '0 */5 * * * *' means every 5 minutes at second 0."
        )
    croniter_expr = _user_to_croniter(expression)
    try:
        croniter(croniter_expr)
    except (ValueError, KeyError, TypeError) as e:
        raise ValueError(f"Invalid cron expression: '{expression}' ({e})")
    return expression


def next_fire_time(
    expression: str,
    base: Optional[datetime] = None,
) -> datetime:
    validate_cron(expression)
    croniter_expr = _user_to_croniter(expression)
    if base is None:
        base = datetime.now(timezone.utc)
    elif base.tzinfo is None:
        base = base.replace(tzinfo=timezone.utc)
    cron = croniter(croniter_expr, base)
    nxt = cron.get_next(datetime)
    if nxt.tzinfo is None:
        nxt = nxt.replace(tzinfo=timezone.utc)
    return nxt

`````

--- **end of file: nb_cron/cron_utils/parser.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/cron_utils/translator.py** (project: nb_cron) --- 

`````python
"""
Translate a 6-field cron expression to human-readable Chinese or English.

Format: second minute hour day_of_month month day_of_week
"""
from typing import List, Optional

WEEKDAY_EN = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
WEEKDAY_ZH = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
MONTH_EN = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
MONTH_ZH = [
    "", "1月", "2月", "3月", "4月", "5月", "6月",
    "7月", "8月", "9月", "10月", "11月", "12月",
]


def explain_cron(expression: str, lang: str = "en") -> str:
    fields = expression.strip().split()
    if len(fields) != 6:
        raise ValueError(
            f"nb_cron requires exactly 6-field cron "
            f"(second minute hour day month weekday), "
            f"got {len(fields)} fields: '{expression}'."
        )
    second, minute, hour, dom, month, dow = fields
    if lang == "zh":
        return _translate_zh(second, minute, hour, dom, month, dow)
    return _translate_en(second, minute, hour, dom, month, dow)


def _translate_en(sec: str, min_: str, hour: str, dom: str, month: str, dow: str) -> str:
    parts: List[str] = []

    if sec == "*" and min_ == "*" and hour == "*" and dom == "*" and month == "*" and dow == "*":
        return "Every second"

    time_desc = _time_desc_en(sec, min_, hour)
    when_desc = _when_desc_en(dom, month, dow)

    if when_desc:
        parts.append(time_desc)
        parts.append(when_desc)
    else:
        parts.append(time_desc)

    return ", ".join(parts)


def _time_desc_en(sec: str, min_: str, hour: str) -> str:
    if sec == "*" and min_ == "*" and hour == "*":
        return "Every second"
    if min_ == "*" and hour == "*":
        return _field_desc_en(sec, "second")
    if hour == "*":
        sec_part = _at_field_en(sec, "second") if sec != "0" else ""
        min_part = _field_desc_en(min_, "minute")
        return f"{min_part}{sec_part}" if sec_part else min_part

    if _is_specific(hour) and _is_specific(min_) and _is_specific(sec):
        return f"At {_pad(hour)}:{_pad(min_)}:{_pad(sec)}"

    parts = []
    parts.append(_field_desc_en(hour, "hour"))
    if min_ != "*" and min_ != "0":
        parts.append(_at_field_en(min_, "minute"))
    if sec != "*" and sec != "0":
        parts.append(_at_field_en(sec, "second"))
    return " ".join(parts)


def _when_desc_en(dom: str, month: str, dow: str) -> str:
    parts = []
    if dow != "*":
        parts.append(f"on {_weekday_desc_en(dow)}")
    if dom != "*":
        parts.append(f"on day {_list_desc(dom)} of the month")
    if month != "*":
        parts.append(f"in {_month_desc_en(month)}")
    return " ".join(parts)


def _field_desc_en(field: str, unit: str) -> str:
    if field == "*":
        return f"every {unit}"
    if field.startswith("*/"):
        n = field[2:]
        return f"every {n} {unit}s" if n != "1" else f"every {unit}"
    if "-" in field and "/" in field:
        range_part, step = field.split("/")
        start, end = range_part.split("-")
        return f"every {step} {unit}s from {start} through {end}"
    if "-" in field:
        start, end = field.split("-")
        return f"every {unit} from {start} through {end}"
    if "," in field:
        return f"at {unit} {field}"
    return f"at {unit} {field}"


def _at_field_en(field: str, unit: str) -> str:
    if field == "*":
        return ""
    if field.startswith("*/"):
        return f" every {field[2:]} {unit}s"
    return f" at {unit} {field}"


def _weekday_desc_en(field: str) -> str:
    if "," in field:
        days = [_single_weekday_en(d.strip()) for d in field.split(",")]
        return ", ".join(days)
    if "-" in field:
        start, end = field.split("-")
        return f"{_single_weekday_en(start)} through {_single_weekday_en(end)}"
    return _single_weekday_en(field)


def _single_weekday_en(val: str) -> str:
    try:
        idx = int(val) % 7
        return WEEKDAY_EN[idx]
    except ValueError:
        return val


def _month_desc_en(field: str) -> str:
    if "," in field:
        months = [_single_month_en(m.strip()) for m in field.split(",")]
        return ", ".join(months)
    if "-" in field:
        start, end = field.split("-")
        return f"{_single_month_en(start)} through {_single_month_en(end)}"
    return _single_month_en(field)


def _single_month_en(val: str) -> str:
    try:
        idx = int(val)
        if 1 <= idx <= 12:
            return MONTH_EN[idx]
    except ValueError:
        pass
    return val


# ── Chinese translation ──

def _translate_zh(sec: str, min_: str, hour: str, dom: str, month: str, dow: str) -> str:
    if sec == "*" and min_ == "*" and hour == "*" and dom == "*" and month == "*" and dow == "*":
        return "每秒执行"

    parts: List[str] = []
    when = _when_desc_zh(dom, month, dow)
    if when:
        parts.append(when)
    time_part = _time_desc_zh(sec, min_, hour)
    parts.append(time_part)
    parts.append("执行")
    return "".join(parts)


def _time_desc_zh(sec: str, min_: str, hour: str) -> str:
    if sec == "*" and min_ == "*" and hour == "*":
        return "每秒"
    if min_ == "*" and hour == "*":
        return _field_desc_zh(sec, "秒")
    if hour == "*":
        result = _field_desc_zh(min_, "分钟")
        if sec != "0" and sec != "*":
            result += _at_field_zh(sec, "秒")
        elif sec == "0":
            result += "的第0秒"
        return result

    if _is_specific(hour) and _is_specific(min_) and _is_specific(sec):
        return f"{_pad(hour)}:{_pad(min_)}:{_pad(sec)}"

    parts = []
    parts.append(_field_desc_zh(hour, "小时"))
    if min_ != "*":
        if _is_specific(min_):
            parts.append(f"第{min_}分")
        else:
            parts.append(_field_desc_zh(min_, "分钟"))
    if sec != "*" and sec != "0":
        if _is_specific(sec):
            parts.append(f"第{sec}秒")
        else:
            parts.append(_field_desc_zh(sec, "秒"))
    elif sec == "0":
        parts.append("第0秒")
    return "".join(parts)


def _when_desc_zh(dom: str, month: str, dow: str) -> str:
    parts = []
    if month != "*":
        parts.append(_month_desc_zh(month))
    if dom != "*":
        parts.append(_dom_desc_zh(dom))
    if dow != "*":
        parts.append(_weekday_desc_zh(dow))
    return "".join(parts)


def _field_desc_zh(field: str, unit: str) -> str:
    if field == "*":
        return f"每{unit}"
    if field.startswith("*/"):
        n = field[2:]
        return f"每{n}{unit}"
    if "-" in field and "/" in field:
        range_part, step = field.split("/")
        start, end = range_part.split("-")
        return f"从第{start}到第{end}{unit}, 每{step}{unit}"
    if "-" in field:
        start, end = field.split("-")
        return f"第{start}到第{end}{unit}"
    if "," in field:
        return f"第{field}{unit}"
    return f"第{field}{unit}"


def _at_field_zh(field: str, unit: str) -> str:
    if field == "*":
        return ""
    if field.startswith("*/"):
        return f"每{field[2:]}{unit}"
    return f"第{field}{unit}"


def _weekday_desc_zh(field: str) -> str:
    if "," in field:
        days = [_single_weekday_zh(d.strip()) for d in field.split(",")]
        return "每" + "、".join(days)
    if "-" in field:
        start, end = field.split("-")
        return f"每{_single_weekday_zh(start)}至{_single_weekday_zh(end)}"
    return f"每{_single_weekday_zh(field)}"


def _single_weekday_zh(val: str) -> str:
    try:
        idx = int(val) % 7
        return WEEKDAY_ZH[idx]
    except ValueError:
        return val


def _month_desc_zh(field: str) -> str:
    if "," in field:
        months = [_single_month_zh(m.strip()) for m in field.split(",")]
        return "、".join(months)
    if "-" in field:
        start, end = field.split("-")
        return f"{_single_month_zh(start)}至{_single_month_zh(end)}"
    return _single_month_zh(field)


def _single_month_zh(val: str) -> str:
    try:
        idx = int(val)
        if 1 <= idx <= 12:
            return MONTH_ZH[idx]
    except ValueError:
        pass
    return val


def _dom_desc_zh(field: str) -> str:
    if "," in field:
        return f"每月{field}日"
    if "-" in field:
        start, end = field.split("-")
        return f"每月{start}日至{end}日"
    if field.startswith("*/"):
        return f"每{field[2:]}天"
    return f"每月{field}日"


# ── helpers ──

def _is_specific(field: str) -> bool:
    try:
        int(field)
        return True
    except ValueError:
        return False


def _list_desc(field: str) -> str:
    return field


def _pad(val: str) -> str:
    try:
        return f"{int(val):02d}"
    except ValueError:
        return val

`````

--- **end of file: nb_cron/cron_utils/translator.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/cron_utils/__init__.py** (project: nb_cron) --- 

`````python
from nb_cron.cron_utils.parser import validate_cron, next_fire_time
from nb_cron.cron_utils.translator import explain_cron

__all__ = ["validate_cron", "next_fire_time", "explain_cron"]

`````

--- **end of file: nb_cron/cron_utils/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/executors/base_executor.py** (project: nb_cron) --- 

`````python
"""
执行器基类。

nb_cron 的调度器负责「到时间触发」，执行器负责「真正运行任务」。

内置两个实现：
  - ThreadExecutor  — 默认，本地自适应线程池
  - FunboostExecutor — 把任务推入 funboost 队列，由 funboost worker 消费执行

可自定义执行器，只需继承 BaseExecutor 实现 submit()。

用法::

    from nb_cron import NbCron
    from nb_cron.executors.funboost_executor import FunboostExecutor

    executor = FunboostExecutor(BoosterParams(queue_name="my_queue", broker_kind=BrokerEnum.REDIS))
    cron = NbCron("my_project", "redis://localhost:6379/0", executor=executor)
"""
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Optional, Tuple


class BaseExecutor(ABC):
    """
    执行器接口。

    调度器触发任务时调用 ``submit()``，执行器决定如何执行。
    - 本地执行：线程池直接运行
    - funboost：推送到队列，异步 worker 消费
    - 自定义：RQ / Celery / ... 任意消息队列
    """

    @abstractmethod
    def submit(
        self,
        func_ref: str,
        func: Callable,
        args: Tuple,
        kwargs: Dict[str, Any],
        job_id: str,
        callback: Optional[Callable] = None,
    ) -> None:
        """
        提交一次任务执行。

        Parameters
        ----------
        func_ref:
            函数的 cron_func_name，用于远程 worker 通过注册表重新解析。
        func:
            当前进程已解析的可调用对象（本地执行器直接用；远程执行器只用 func_ref）。
        args:
            位置参数。
        kwargs:
            关键字参数。
        job_id:
            任务 ID，用于 metrics 记录。
        callback:
            本地执行完成后的回调 ``callback(_ExecutionResult)``。
            远程执行器（如 funboost）执行发生在另一进程，此回调通常被忽略，
            由远程 worker 自行记录 metrics。
        """

    def shutdown(self, wait: bool = True) -> None:
        """释放资源（可选）。"""

`````

--- **end of file: nb_cron/executors/base_executor.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/executors/funboost_executor.py** (project: nb_cron) --- 

`````python
"""
Funboost 执行器。

任务触发时，nb_cron 不在本地执行函数，而是调用 funboost 的 .push() 把
(cron_func_name, args, kwargs, job_id) 推送到消息队列（Redis / RabbitMQ / ...），
由 funboost worker 进程消费执行，执行完毕后自动向 store 写入成功/失败指标。

安装依赖::

    pip install funboost

用法::

    from funboost import BoosterParams, BrokerEnum
    from nb_cron import NbCron, cron_register
    from nb_cron.executors.funboost_executor import FunboostExecutor

    executor = FunboostExecutor(
        BoosterParams(
            queue_name="nb_cron_dispatch",
            broker_kind=BrokerEnum.REDIS,
            concurrent_num=10,
            qps=20,
        )
    )
    # NbCron 构造时会自动把自身注入给 executor，worker 端直接复用 metrics
    cron = NbCron("my_project", "redis://localhost:6379/0", executor=executor)

    @cron.job("0 */5 * * * *", kwargs={"user_id": 42})
    @cron_register('my_task')
    def my_task(user_id: int):
        print(f"processing user {user_id}")

    # 启动 funboost consume（consume() 本身非阻塞）+ scheduler
    executor.consume()
    cron.start()

Worker 端单独进程（可横向扩展）::

    # worker.py
    from funboost import BoosterParams, BrokerEnum
    from nb_cron import NbCron
    from nb_cron.executors.funboost_executor import FunboostExecutor
    import my_tasks   # 触发 @cron_register，让注册表生效

    executor = FunboostExecutor(
        BoosterParams(queue_name="nb_cron_dispatch", broker_kind=BrokerEnum.REDIS)
    )
    cron = NbCron("my_project", "redis://localhost:6379/0", executor=executor)

    executor.consume()  # 或 executor.mp_consume(process_num=4)

自定义 metrics_recorder（高级，如同时上报 Prometheus）::

    def my_recorder(job_id, success, duration_ms, error):
        ...  # 自定义逻辑

    executor = FunboostExecutor(
        BoosterParams(...),
        metrics_recorder=my_recorder,
    )
"""
import logging
import time as _time
import traceback
from typing import Any, Callable, Dict, Optional, Tuple
import inspect

import asyncio
import threading



from nb_cron.executors.base_executor import BaseExecutor
from funboost import boost, BoosterParams, ConcurrentModeEnum

logger = logging.getLogger("nb_cron.funboost_executor")

tl = threading.local()


def _get_thread_local_loop() -> asyncio.AbstractEventLoop:
    if not hasattr(tl, 'asyncio_loop'):
        loop = asyncio.new_event_loop()
        tl.asyncio_loop = loop
    return tl.asyncio_loop

class FunboostExecutor(BaseExecutor):
    """
    将 nb_cron 任务推入 funboost 消息队列，由 funboost worker 异步消费执行。
    执行完毕后自动上报成功/失败指标。

    Parameters
    ----------
    booster_params:
        funboost ``BoosterParams`` 对象，支持 IDE 自动补全所有参数（queue_name、
        broker_kind、concurrent_num、qps、max_retry_times 等）。
    metrics_recorder:
        可选自定义指标回调，签名 ``(job_id, success, duration_ms, error_msg) -> None``。
        不传则使用 NbCron 注入的 metrics（推荐，自动写入 store）。
    """

    def __init__(
        self,
        booster_params: "BoosterParams",
        metrics_recorder: Optional[Callable[[str, bool, float, Optional[str]], None]] = None,
    ):
        self.booster_params = booster_params
        self.booster_params.concurrent_mode = ConcurrentModeEnum.THREADING # 用户无需指定并发模式，_nb_cron_dispatch函数内部自动处理asyncio和同步函数
        self._metrics_recorder = metrics_recorder
        # NbCron 构造时会自动赋值（见 NbCron.__init__）
        self._cron: Optional[Any] = None
        self.booster = self._build_booster()
        self.consume = self.booster.consume
        self.mp_consume = self.booster.mp_consume

    # ── NbCron 注入 ──────────────────────────────────────────────────

    def bind_cron(self, cron: Any) -> None:
        """由 NbCron.__init__ 自动调用，把 scheduler 实例注入进来，
        worker 端直接复用 cron.metrics.record() 写入指标，无需重建 store。"""
        self._cron = cron

    # ── 内部方法 ────────────────────────────────────────────────────

    def _get_metrics_recorder(self) -> Optional[Callable]:
        """
        指标记录器优先级：
          1. 自定义 metrics_recorder
          2. NbCron 注入的 cron.metrics.record（推荐）
          3. None（只打 debug 日志）
        """
        if self._metrics_recorder:
            return self._metrics_recorder
        if self._cron is not None:
            return self._cron.metrics.record
        return None

    def _build_booster(self):
        """构建 @boost 装饰的统一 dispatch 函数。"""
        booster_params = self.booster_params
        executor_ref = self

        @boost(booster_params)
        def _nb_cron_dispatch(
            cron_func_name: str,
            args: list,
            kwargs: dict,
            job_id: str,
        ):
            """
            funboost worker 消费的真正入口。
            解析 cron_func_name → 执行函数 → 上报成功/失败指标。
            """
            from nb_cron.core.registry import FunctionRegistry

            start = _time.monotonic()
            success = False
            error_msg: Optional[str] = None
            kwargs = kwargs or {}

            try:
                func = FunctionRegistry.resolve(cron_func_name)
                if inspect.iscoroutinefunction(func):
                    has_specify_async_loop = None
                    loop = booster_params.specify_async_loop
                    if loop is not None:
                        has_specify_async_loop = True
                    else:
                        has_specify_async_loop = False
                        loop = _get_thread_local_loop()
                    if has_specify_async_loop:
                        """
                        # 有些aio三方包，例如aiohttp的cleint需要确保实例化和发请求，必须在同一个loop运行，此时必须指定loop。 
                        # 如果指定了loop，用户记得还要去亲自去启动looploop.run_forever()，否则async def的函数不会被执行。
                        """
                        future = asyncio.run_coroutine_threadsafe(func(*args, **kwargs ), loop)
                        result = future.result()
                    else:
                        result = loop.run_until_complete(func(*args, **kwargs))
                else:
                    result = func(*args, **kwargs)
                success = True
                return result
            except Exception as exc:
                error_msg = str(exc)
                logger.error(
                    "funboost job FAILED: job_id=%s func=%s error=%s\n%s",
                    job_id, cron_func_name, exc, traceback.format_exc(),
                )
                raise
            finally:
                duration_ms = (_time.monotonic() - start) * 1000
                logger.debug(
                    "funboost job %s: func=%s success=%s duration=%.1fms",
                    job_id, cron_func_name, success, duration_ms,
                )
                recorder = executor_ref._get_metrics_recorder()
                if recorder:
                    try:
                        recorder(job_id, success, duration_ms, error_msg)
                    except Exception:
                        logger.warning(
                            "funboost metrics 上报失败: job_id=%s", job_id, exc_info=True
                        )
                else:
                    logger.debug(
                        "funboost metrics 未配置 recorder，跳过上报: job_id=%s", job_id
                    )

        return _nb_cron_dispatch

    # ── 公开接口 ────────────────────────────────────────────────────

    def submit(
        self,
        func_ref: str,
        func: Callable,
        args: Tuple,
        kwargs: Dict[str, Any],
        job_id: str,
        callback: Optional[Callable] = None,
    ) -> None:
        """推入 funboost 队列。callback 被忽略（执行在 worker 进程）。"""
        logger.debug(
            "push to funboost: job_id=%s func=%s queue=%s",
            job_id, func_ref, self.booster_params.queue_name,
        )
        self.booster.push(
            cron_func_name=func_ref,
            args=list(args),
            kwargs=kwargs or {},
            job_id=job_id,
        )

    
    def shutdown(self, wait: bool = True) -> None:
        pass

`````

--- **end of file: nb_cron/executors/funboost_executor.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/executors/threadpool.py** (project: nb_cron) --- 

`````python
import asyncio
import logging
import queue
import threading
import time
import traceback
from typing import Any, Callable, Optional

from nb_cron.utils import is_async_callable

logger = logging.getLogger("nb_cron.executor")

_SENTINEL = object()


class _ExecutionResult:
    __slots__ = ("success", "result", "error", "duration_ms")

    def __init__(self, success: bool, result: Any, error: Optional[str], duration_ms: float):
        self.success = success
        self.result = result
        self.error = error
        self.duration_ms = duration_ms


class AdaptiveThreadPool:
    """
    自适应线程池：按需创建 worker，空闲 idle_timeout 秒后自动退出。
    sync / async 任务共用同一池，并发统一受 max_workers 控制。
    不依赖 stdlib ThreadPoolExecutor（其 atexit 在 Python 3.9+ 会提前 shutdown）。
    """

    def __init__(self, max_workers: int = 20, idle_timeout: float = 5.0):
        self._max_workers = max_workers
        self._idle_timeout = idle_timeout
        self._queue: queue.Queue = queue.Queue()
        self._lock = threading.Lock()
        self._num_threads = 0
        self._num_idle = 0
        self._closed = False

    def submit(
        self,
        func: Callable,
        args: tuple = (),
        kwargs: Optional[dict] = None,
        callback: Optional[Callable[[_ExecutionResult], None]] = None,
    ) -> None:
        kwargs = kwargs or {}

        def _run():
            start = time.monotonic()
            try:
                if is_async_callable(func):
                    result = asyncio.run(func(*args, **kwargs))
                else:
                    result = func(*args, **kwargs)
                duration = (time.monotonic() - start) * 1000
                er = _ExecutionResult(True, result, None, duration)
            except Exception as e:
                duration = (time.monotonic() - start) * 1000
                tb = traceback.format_exc()
                logger.error("Job execution failed: %s\n%s", e, tb)
                er = _ExecutionResult(False, None, str(e), duration)
            if callback:
                try:
                    callback(er)
                except Exception:
                    logger.exception("Callback error")

        if self._closed:
            return
        self._queue.put(_run)
        with self._lock:
            if self._num_idle == 0 and self._num_threads < self._max_workers:
                self._num_threads += 1
                threading.Thread(
                    target=self._worker, name="nb_cron-worker",
                ).start()

    def _worker(self) -> None:
        with self._lock:
            self._num_idle += 1
        while True:
            try:
                task = self._queue.get(timeout=self._idle_timeout)
            except queue.Empty:
                with self._lock:
                    self._num_idle -= 1
                    self._num_threads -= 1
                return
            if task is _SENTINEL:
                self._queue.task_done()
                with self._lock:
                    self._num_idle -= 1
                    self._num_threads -= 1
                return
            with self._lock:
                self._num_idle -= 1
            try:
                task()
            except Exception:
                logger.exception("Unexpected error in worker")
            self._queue.task_done()
            with self._lock:
                self._num_idle += 1

    @property
    def num_threads(self) -> int:
        with self._lock:
            return self._num_threads

    def shutdown(self, wait: bool = True) -> None:
        self._closed = True
        if wait:
            self._queue.join()
        with self._lock:
            for _ in range(self._num_threads):
                self._queue.put(_SENTINEL)

`````

--- **end of file: nb_cron/executors/threadpool.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/executors/thread_executor.py** (project: nb_cron) --- 

`````python
"""
默认执行器：本地自适应线程池。
封装 AdaptiveThreadPool，实现 BaseExecutor 接口。
"""
from typing import Any, Callable, Dict, Optional, Tuple

from nb_cron.executors.base_executor import BaseExecutor
from nb_cron.executors.threadpool import AdaptiveThreadPool, _ExecutionResult


class ThreadExecutor(BaseExecutor):
    """
    本地线程池执行器（默认）。

    任务在当前进程的自适应线程池中直接执行，执行完成后触发 callback 记录 metrics。
    """

    def __init__(self, max_workers: int = 20, idle_timeout: float = 5.0):
        self._pool = AdaptiveThreadPool(max_workers=max_workers, idle_timeout=idle_timeout)

    def submit(
        self,
        func_ref: str,
        func: Callable,
        args: Tuple,
        kwargs: Dict[str, Any],
        job_id: str,
        callback: Optional[Callable[[_ExecutionResult], None]] = None,
    ) -> None:
        self._pool.submit(func, args=args, kwargs=kwargs, callback=callback)

    def shutdown(self, wait: bool = True) -> None:
        self._pool.shutdown(wait=wait)

`````

--- **end of file: nb_cron/executors/thread_executor.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/executors/__init__.py** (project: nb_cron) --- 

`````python

`````

--- **end of file: nb_cron/executors/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/locks/base.py** (project: nb_cron) --- 

`````python
from abc import ABC, abstractmethod


class BaseLock(ABC):

    @abstractmethod
    def acquire(self, lock_key: str, ttl_seconds: int = 60) -> bool:
        """
        Try to acquire a distributed lock.
        Returns True if acquired, False if already held by another instance.
        The lock auto-expires after ttl_seconds.
        """

    @abstractmethod
    def release(self, lock_key: str) -> None:
        """Release a previously acquired lock."""

    def close(self) -> None:
        """Release resources (optional override)."""

`````

--- **end of file: nb_cron/locks/base.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/locks/memory_lock.py** (project: nb_cron) --- 

`````python
import threading
import time
from typing import Dict, Tuple

from nb_cron.locks.base import BaseLock


class MemoryLock(BaseLock):
    """In-process lock for single-instance deployments."""

    def __init__(self):
        self._locks: Dict[str, float] = {}  # key -> expire_timestamp
        self._mutex = threading.Lock()

    def acquire(self, lock_key: str, ttl_seconds: int = 60) -> bool:
        now = time.time()
        with self._mutex:
            expire = self._locks.get(lock_key, 0)
            if expire > now:
                return False
            self._locks[lock_key] = now + ttl_seconds
            return True

    def release(self, lock_key: str) -> None:
        with self._mutex:
            self._locks.pop(lock_key, None)

    def _cleanup_expired(self) -> None:
        now = time.time()
        with self._mutex:
            expired = [k for k, v in self._locks.items() if v <= now]
            for k in expired:
                del self._locks[k]

`````

--- **end of file: nb_cron/locks/memory_lock.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/locks/mongo_lock.py** (project: nb_cron) --- 

`````python
import uuid
from datetime import datetime, timedelta, timezone

from nb_cron.locks.base import BaseLock


class MongoLock(BaseLock):
    """Distributed lock based on MongoDB unique index + TTL."""

    def __init__(self, url: str = "mongodb://localhost:27017", db_name: str = "nb_cron", name: str = "nb_cron"):
        try:
            from pymongo import MongoClient
            from pymongo.errors import DuplicateKeyError
        except ImportError:
            raise ImportError(
                "pymongo package is required for MongoLock. "
                "Install with: pip install nb_cron_nb[mongo]"
            )
        self._client = MongoClient(url)
        self._collection = self._client[db_name][f"nb_cron_{name}_locks"]
        self._collection.create_index("lock_key", unique=True)
        self._collection.create_index("expire_at", expireAfterSeconds=0)
        self._token = str(uuid.uuid4())
        self._DuplicateKeyError = DuplicateKeyError

    def acquire(self, lock_key: str, ttl_seconds: int = 60) -> bool:
        now = datetime.now(timezone.utc)
        expire_at = now + timedelta(seconds=ttl_seconds)
        self._collection.delete_many({
            "lock_key": lock_key,
            "expire_at": {"$lte": now},
        })
        try:
            self._collection.insert_one({
                "lock_key": lock_key,
                "token": self._token,
                "expire_at": expire_at,
                "acquired_at": now,
            })
            return True
        except self._DuplicateKeyError:
            return False

    def release(self, lock_key: str) -> None:
        self._collection.delete_one({
            "lock_key": lock_key,
            "token": self._token,
        })

    def close(self) -> None:
        self._client.close()

`````

--- **end of file: nb_cron/locks/mongo_lock.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/locks/redis_lock.py** (project: nb_cron) --- 

`````python
import uuid

from nb_cron.locks.base import BaseLock


class RedisLock(BaseLock):
    """
    Distributed lock based on Redis SET NX PX.
    Guarantees exactly-once execution across multiple instances.
    """

    def __init__(self, url: str = "redis://localhost:6379/0", name: str = "nb_cron"):
        try:
            import redis
        except ImportError:
            raise ImportError(
                "redis package is required for RedisLock. "
                "Install with: pip install nb_cron_nb[redis]"
            )
        self._client = redis.Redis.from_url(url, decode_responses=True)
        self._token = str(uuid.uuid4())
        self._prefix = f"nb_cron:{name}"

    def acquire(self, lock_key: str, ttl_seconds: int = 60) -> bool:
        key = f"{self._prefix}:lock:{lock_key}"
        acquired = self._client.set(key, self._token, nx=True, px=ttl_seconds * 1000)
        return bool(acquired)

    def release(self, lock_key: str) -> None:
        key = f"{self._prefix}:lock:{lock_key}"
        lua = """
        if redis.call("get", KEYS[1]) == ARGV[1] then
            return redis.call("del", KEYS[1])
        else
            return 0
        end
        """
        self._client.eval(lua, 1, key, self._token)

    def close(self) -> None:
        self._client.close()

`````

--- **end of file: nb_cron/locks/redis_lock.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/locks/sqlalchemy_lock.py** (project: nb_cron) --- 

`````python
import uuid
from datetime import datetime, timedelta, timezone

from nb_cron.locks.base import BaseLock


class SQLAlchemyLock(BaseLock):
    """Distributed lock using a SQL table with INSERT conflict detection."""

    def __init__(self, url: str = "sqlite:///nb_cron.db", name: str = "nb_cron"):
        try:
            from sqlalchemy import (
                Column, DateTime, MetaData, String, Table, create_engine,
            )
            from sqlalchemy.orm import sessionmaker
        except ImportError:
            raise ImportError(
                "sqlalchemy package is required for SQLAlchemyLock. "
                "Install with: pip install nb_cron_nb[sqlalchemy]"
            )
        self._engine = create_engine(url, pool_pre_ping=True)
        self._Session = sessionmaker(bind=self._engine)
        self._metadata = MetaData()
        self._table = Table(
            f"nb_cron_{name}_locks", self._metadata,
            Column("lock_key", String(512), primary_key=True),
            Column("token", String(64), nullable=False),
            Column("expire_at", DateTime(timezone=True), nullable=False),
        )
        self._metadata.create_all(self._engine)
        self._token = str(uuid.uuid4())

    def acquire(self, lock_key: str, ttl_seconds: int = 60) -> bool:
        now = datetime.now(timezone.utc)
        expire_at = now + timedelta(seconds=ttl_seconds)
        session = self._Session()
        try:
            session.execute(
                self._table.delete().where(self._table.c.expire_at <= now)
            )
            session.commit()

            existing = session.execute(
                self._table.select().where(self._table.c.lock_key == lock_key)
            ).fetchone()
            if existing:
                return False

            try:
                session.execute(
                    self._table.insert().values(
                        lock_key=lock_key,
                        token=self._token,
                        expire_at=expire_at,
                    )
                )
                session.commit()
                return True
            except Exception:
                session.rollback()
                return False
        finally:
            session.close()

    def release(self, lock_key: str) -> None:
        session = self._Session()
        try:
            session.execute(
                self._table.delete().where(
                    self._table.c.lock_key == lock_key,
                    self._table.c.token == self._token,
                )
            )
            session.commit()
        finally:
            session.close()

    def close(self) -> None:
        self._engine.dispose()

`````

--- **end of file: nb_cron/locks/sqlalchemy_lock.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/locks/__init__.py** (project: nb_cron) --- 

`````python
from nb_cron.locks.base import BaseLock

__all__ = ["BaseLock"]

`````

--- **end of file: nb_cron/locks/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/metrics/collector.py** (project: nb_cron) --- 

`````python
import threading
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from nb_cron.stores.base import BaseStore
from nb_cron.utils import truncate_string

MAX_RECENT_RESULTS = 10
HOURLY_SLOTS = 24


def _empty_metrics() -> Dict[str, Any]:
    return {
        "total_runs": 0,
        "success_count": 0,
        "fail_count": 0,
        "last_run_at": None,
        "last_success_at": None,
        "last_error": None,
        "last_error_at": None,
        "avg_duration_ms": 0.0,
        "max_duration_ms": 0.0,
        "min_duration_ms": 0.0,
        "last_duration_ms": 0.0,
        "recent_results": [],
        "hourly_stats": [{"hour": i, "success": 0, "fail": 0} for i in range(HOURLY_SLOTS)],
    }


class MetricsCollector:

    def __init__(self, store: BaseStore):
        self._store = store
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()

    def record(
        self,
        job_id: str,
        success: bool,
        duration_ms: float,
        error: Optional[str] = None,
    ) -> None:
        now = datetime.now(timezone.utc)
        with self._lock:
            m = self._cache.get(job_id)
            if m is None:
                stored = self._store.get_metrics(job_id)
                m = stored if stored else _empty_metrics()
                self._cache[job_id] = m

            m["total_runs"] += 1
            m["last_run_at"] = now.isoformat()
            m["last_duration_ms"] = round(duration_ms, 2)

            if success:
                m["success_count"] += 1
                m["last_success_at"] = now.isoformat()
            else:
                m["fail_count"] += 1
                m["last_error"] = truncate_string(error or "Unknown error")
                m["last_error_at"] = now.isoformat()

            total = m["total_runs"]
            prev_avg = m["avg_duration_ms"]
            m["avg_duration_ms"] = round(prev_avg + (duration_ms - prev_avg) / total, 2)
            m["max_duration_ms"] = round(max(m["max_duration_ms"], duration_ms), 2)
            if m["min_duration_ms"] == 0:
                m["min_duration_ms"] = round(duration_ms, 2)
            else:
                m["min_duration_ms"] = round(min(m["min_duration_ms"], duration_ms), 2)

            recent: list = m.get("recent_results", [])
            recent.append({
                "time": now.isoformat(),
                "success": success,
                "duration_ms": round(duration_ms, 2),
                "error": truncate_string(error) if error else None,
            })
            if len(recent) > MAX_RECENT_RESULTS:
                recent[:] = recent[-MAX_RECENT_RESULTS:]
            m["recent_results"] = recent

            hour_idx = now.hour % HOURLY_SLOTS
            hourly: list = m.get("hourly_stats", [])
            if len(hourly) < HOURLY_SLOTS:
                hourly = [{"hour": i, "success": 0, "fail": 0} for i in range(HOURLY_SLOTS)]
                m["hourly_stats"] = hourly
            if success:
                hourly[hour_idx]["success"] += 1
            else:
                hourly[hour_idx]["fail"] += 1

            self._store.save_metrics(job_id, m)

    def get_metrics(self, job_id: str) -> Dict[str, Any]:
        with self._lock:
            cached = self._cache.get(job_id)
            if cached:
                return dict(cached)
        stored = self._store.get_metrics(job_id)
        return stored if stored else _empty_metrics()

    def get_all_metrics(self) -> Dict[str, Dict[str, Any]]:
        stored = self._store.get_all_metrics()
        with self._lock:
            for jid, m in self._cache.items():
                stored[jid] = dict(m)
        return stored

    def get_dashboard_stats(self) -> Dict[str, Any]:
        all_m = self.get_all_metrics()
        total_runs = 0
        total_success = 0
        total_fail = 0
        job_count = len(all_m)
        for m in all_m.values():
            total_runs += m.get("total_runs", 0)
            total_success += m.get("success_count", 0)
            total_fail += m.get("fail_count", 0)

        hourly_agg = [{"hour": i, "success": 0, "fail": 0} for i in range(HOURLY_SLOTS)]
        for m in all_m.values():
            for slot in m.get("hourly_stats", []):
                idx = slot["hour"] % HOURLY_SLOTS
                hourly_agg[idx]["success"] += slot.get("success", 0)
                hourly_agg[idx]["fail"] += slot.get("fail", 0)

        return {
            "job_count": job_count,
            "total_runs": total_runs,
            "total_success": total_success,
            "total_fail": total_fail,
            "success_rate": round(total_success / total_runs * 100, 1) if total_runs else 0,
            "hourly_stats": hourly_agg,
        }

`````

--- **end of file: nb_cron/metrics/collector.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/metrics/__init__.py** (project: nb_cron) --- 

`````python

`````

--- **end of file: nb_cron/metrics/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/stores/base.py** (project: nb_cron) --- 

`````python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, List, Optional

from nb_cron.core.job import Job


class BaseStore(ABC):

    @abstractmethod
    def add_job(self, job: Job) -> None:
        """Persist a new job. Raises if job_id already exists."""

    @abstractmethod
    def update_job(self, job: Job) -> None:
        """Update an existing job in-place."""

    @abstractmethod
    def remove_job(self, job_id: str) -> None:
        """Remove a job by id."""

    @abstractmethod
    def get_job(self, job_id: str) -> Optional[Job]:
        """Return a single job or None."""

    @abstractmethod
    def get_all_jobs(self) -> List[Job]:
        """Return all jobs."""

    @abstractmethod
    def get_due_jobs(self, now: datetime) -> List[Job]:
        """Return active jobs whose next_run_time <= now."""

    @abstractmethod
    def update_next_run_time(self, job_id: str, next_run_time: Optional[datetime]) -> None:
        """Update only the next_run_time for a job."""

    @abstractmethod
    def save_metrics(self, job_id: str, metrics: Dict[str, Any]) -> None:
        """Persist metrics dict for a job."""

    @abstractmethod
    def get_metrics(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Load metrics dict for a job."""

    @abstractmethod
    def get_all_metrics(self) -> Dict[str, Dict[str, Any]]:
        """Load metrics for all jobs.  {job_id: metrics_dict}"""

    # ── Function registry (cross-project support) ──

    @abstractmethod
    def register_function(self, func_name: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Persist a registered function name so it's visible across projects."""

    @abstractmethod
    def get_function_names(self) -> List[str]:
        """Return all registered function names."""

    def function_exists(self, func_name: str) -> bool:
        return func_name in self.get_function_names()

    def close(self) -> None:
        """Release resources (optional override)."""

    def job_exists(self, job_id: str) -> bool:
        return self.get_job(job_id) is not None

`````

--- **end of file: nb_cron/stores/base.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/stores/memory.py** (project: nb_cron) --- 

`````python
import copy
import threading
from datetime import datetime
from typing import Any, Dict, List, Optional

from nb_cron.core.job import Job
from nb_cron.stores.base import BaseStore


class MemoryStore(BaseStore):

    def __init__(self):
        self._jobs: Dict[str, Job] = {}
        self._metrics: Dict[str, Dict[str, Any]] = {}
        self._functions: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()

    def add_job(self, job: Job) -> None:
        with self._lock:
            if job.job_id in self._jobs:
                raise ValueError(f"Job '{job.job_id}' already exists")
            self._jobs[job.job_id] = copy.deepcopy(job)

    def update_job(self, job: Job) -> None:
        with self._lock:
            if job.job_id not in self._jobs:
                raise ValueError(f"Job '{job.job_id}' not found")
            self._jobs[job.job_id] = copy.deepcopy(job)

    def remove_job(self, job_id: str) -> None:
        with self._lock:
            self._jobs.pop(job_id, None)
            self._metrics.pop(job_id, None)

    def get_job(self, job_id: str) -> Optional[Job]:
        with self._lock:
            job = self._jobs.get(job_id)
            return copy.deepcopy(job) if job else None

    def get_all_jobs(self) -> List[Job]:
        with self._lock:
            return [copy.deepcopy(j) for j in self._jobs.values()]

    def get_due_jobs(self, now: datetime) -> List[Job]:
        with self._lock:
            result = []
            for job in self._jobs.values():
                if (
                    job.status == "active"
                    and job.next_run_time is not None
                    and job.next_run_time <= now
                ):
                    result.append(copy.deepcopy(job))
            return result

    def update_next_run_time(self, job_id: str, next_run_time: Optional[datetime]) -> None:
        with self._lock:
            job = self._jobs.get(job_id)
            if job:
                job.next_run_time = next_run_time

    def save_metrics(self, job_id: str, metrics: Dict[str, Any]) -> None:
        with self._lock:
            self._metrics[job_id] = copy.deepcopy(metrics)

    def get_metrics(self, job_id: str) -> Optional[Dict[str, Any]]:
        with self._lock:
            m = self._metrics.get(job_id)
            return copy.deepcopy(m) if m else None

    def get_all_metrics(self) -> Dict[str, Dict[str, Any]]:
        with self._lock:
            return {k: copy.deepcopy(v) for k, v in self._metrics.items()}

    def register_function(self, func_name: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        with self._lock:
            self._functions[func_name] = metadata or {}

    def get_function_names(self) -> List[str]:
        with self._lock:
            return list(self._functions.keys())

`````

--- **end of file: nb_cron/stores/memory.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/stores/mongo_store.py** (project: nb_cron) --- 

`````python
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from nb_cron.core.job import Job
from nb_cron.stores.base import BaseStore


class MongoStore(BaseStore):

    def __init__(self, url: str = "mongodb://localhost:27017", db_name: str = "nb_cron", name: str = "nb_cron"):
        try:
            from pymongo import MongoClient
        except ImportError:
            raise ImportError(
                "pymongo package is required for MongoStore. "
                "Install with: pip install nb_cron_nb[mongo]"
            )
        self._client = MongoClient(url)
        self._db = self._client[db_name]
        self._jobs = self._db[f"nb_cron_{name}_jobs"]
        self._metrics_col = self._db[f"nb_cron_{name}_metrics"]
        self._functions_col = self._db[f"nb_cron_{name}_functions"]
        self._jobs.create_index("job_id", unique=True)
        self._jobs.create_index("next_run_time")
        self._functions_col.create_index("func_name", unique=True)

    def add_job(self, job: Job) -> None:
        doc = job.to_dict()
        doc["_id"] = job.job_id
        if self._jobs.find_one({"job_id": job.job_id}):
            raise ValueError(f"Job '{job.job_id}' already exists")
        self._jobs.insert_one(doc)

    def update_job(self, job: Job) -> None:
        doc = job.to_dict()
        self._jobs.replace_one({"job_id": job.job_id}, doc, upsert=True)

    def remove_job(self, job_id: str) -> None:
        self._jobs.delete_one({"job_id": job_id})
        self._metrics_col.delete_one({"job_id": job_id})

    def get_job(self, job_id: str) -> Optional[Job]:
        doc = self._jobs.find_one({"job_id": job_id})
        if doc is None:
            return None
        doc.pop("_id", None)
        return Job.from_dict(doc)

    def get_all_jobs(self) -> List[Job]:
        result = []
        for doc in self._jobs.find():
            doc.pop("_id", None)
            result.append(Job.from_dict(doc))
        return result

    def get_due_jobs(self, now: datetime) -> List[Job]:
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        query = {
            "status": "active",
            "next_run_time": {"$ne": None, "$lte": now.isoformat()},
        }
        result = []
        for doc in self._jobs.find(query):
            doc.pop("_id", None)
            result.append(Job.from_dict(doc))
        return result

    def update_next_run_time(self, job_id: str, next_run_time: Optional[datetime]) -> None:
        self._jobs.update_one(
            {"job_id": job_id},
            {"$set": {
                "next_run_time": next_run_time.isoformat() if next_run_time else None,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }},
        )

    def save_metrics(self, job_id: str, metrics: Dict[str, Any]) -> None:
        metrics["job_id"] = job_id
        self._metrics_col.replace_one({"job_id": job_id}, metrics, upsert=True)

    def get_metrics(self, job_id: str) -> Optional[Dict[str, Any]]:
        doc = self._metrics_col.find_one({"job_id": job_id})
        if doc is None:
            return None
        doc.pop("_id", None)
        doc.pop("job_id", None)
        return doc

    def get_all_metrics(self) -> Dict[str, Dict[str, Any]]:
        result = {}
        for doc in self._metrics_col.find():
            jid = doc.pop("job_id", None)
            doc.pop("_id", None)
            if jid:
                result[jid] = doc
        return result

    def register_function(self, func_name: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        doc = {"func_name": func_name, **(metadata or {})}
        self._functions_col.replace_one({"func_name": func_name}, doc, upsert=True)

    def get_function_names(self) -> List[str]:
        return [doc["func_name"] for doc in self._functions_col.find({}, {"func_name": 1})]

    def close(self) -> None:
        self._client.close()

`````

--- **end of file: nb_cron/stores/mongo_store.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/stores/redis_store.py** (project: nb_cron) --- 

`````python
import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from nb_cron.core.job import Job
from nb_cron.stores.base import BaseStore


class RedisStore(BaseStore):

    def __init__(self, url: str = "redis://localhost:6379/0", name: str = "nb_cron"):
        try:
            import redis
        except ImportError:
            raise ImportError(
                "redis package is required for RedisStore. "
                "Install with: pip install nb_cron_nb[redis]"
            )
        self._client = redis.Redis.from_url(url, decode_responses=True)
        self._jobs_key = f"nb_cron:{name}:jobs"
        self._metrics_key = f"nb_cron:{name}:metrics"
        self._due_key = f"nb_cron:{name}:due"
        self._functions_key = f"nb_cron:{name}:functions"

    def add_job(self, job: Job) -> None:
        if self._client.hexists(self._jobs_key, job.job_id):
            raise ValueError(f"Job '{job.job_id}' already exists")
        pipe = self._client.pipeline()
        pipe.hset(self._jobs_key, job.job_id, json.dumps(job.to_dict()))
        if job.next_run_time and job.status == "active":
            score = job.next_run_time.timestamp()
            pipe.zadd(self._due_key, {job.job_id: score})
        pipe.execute()

    def update_job(self, job: Job) -> None:
        pipe = self._client.pipeline()
        pipe.hset(self._jobs_key, job.job_id, json.dumps(job.to_dict()))
        pipe.zrem(self._due_key, job.job_id)
        if job.next_run_time and job.status == "active":
            score = job.next_run_time.timestamp()
            pipe.zadd(self._due_key, {job.job_id: score})
        pipe.execute()

    def remove_job(self, job_id: str) -> None:
        pipe = self._client.pipeline()
        pipe.hdel(self._jobs_key, job_id)
        pipe.hdel(self._metrics_key, job_id)
        pipe.zrem(self._due_key, job_id)
        pipe.execute()

    def get_job(self, job_id: str) -> Optional[Job]:
        raw = self._client.hget(self._jobs_key, job_id)
        if raw is None:
            return None
        return Job.from_dict(json.loads(raw))

    def get_all_jobs(self) -> List[Job]:
        raw_map = self._client.hgetall(self._jobs_key)
        return [Job.from_dict(json.loads(v)) for v in raw_map.values()]

    def get_due_jobs(self, now: datetime) -> List[Job]:
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        score = now.timestamp()
        job_ids = self._client.zrangebyscore(self._due_key, "-inf", score)
        jobs = []
        for jid in job_ids:
            job = self.get_job(jid)
            if job and job.status == "active":
                jobs.append(job)
        return jobs

    def update_next_run_time(self, job_id: str, next_run_time: Optional[datetime]) -> None:
        raw = self._client.hget(self._jobs_key, job_id)
        if raw is None:
            return
        data = json.loads(raw)
        data["next_run_time"] = next_run_time.isoformat() if next_run_time else None
        data["updated_at"] = datetime.now(timezone.utc).isoformat()

        pipe = self._client.pipeline()
        pipe.hset(self._jobs_key, job_id, json.dumps(data))
        pipe.zrem(self._due_key, job_id)
        if next_run_time:
            pipe.zadd(self._due_key, {job_id: next_run_time.timestamp()})
        pipe.execute()

    def save_metrics(self, job_id: str, metrics: Dict[str, Any]) -> None:
        self._client.hset(self._metrics_key, job_id, json.dumps(metrics, default=str))

    def get_metrics(self, job_id: str) -> Optional[Dict[str, Any]]:
        raw = self._client.hget(self._metrics_key, job_id)
        if raw is None:
            return None
        return json.loads(raw)

    def get_all_metrics(self) -> Dict[str, Dict[str, Any]]:
        raw_map = self._client.hgetall(self._metrics_key)
        return {k: json.loads(v) for k, v in raw_map.items()}

    def register_function(self, func_name: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        self._client.hset(self._functions_key, func_name, json.dumps(metadata or {}))

    def get_function_names(self) -> List[str]:
        return list(self._client.hkeys(self._functions_key))

    def close(self) -> None:
        self._client.close()

`````

--- **end of file: nb_cron/stores/redis_store.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/stores/sqlalchemy_store.py** (project: nb_cron) --- 

`````python
import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from nb_cron.core.job import Job
from nb_cron.stores.base import BaseStore


class SQLAlchemyStore(BaseStore):

    def __init__(self, url: str = "sqlite:///nb_cron.db", name: str = "nb_cron"):
        try:
            from sqlalchemy import (
                Column, DateTime, Integer, MetaData, String, Table, Text,
                create_engine,
            )
            from sqlalchemy.orm import sessionmaker
        except ImportError:
            raise ImportError(
                "sqlalchemy package is required for SQLAlchemyStore. "
                "Install with: pip install nb_cron_nb[sqlalchemy]"
            )

        self._engine = create_engine(url, pool_pre_ping=True)
        self._Session = sessionmaker(bind=self._engine)
        self._metadata = MetaData()

        self._jobs_table = Table(
            f"nb_cron_{name}_jobs", self._metadata,
            Column("job_id", String(255), primary_key=True),
            Column("data", Text, nullable=False),
            Column("next_run_time", DateTime(timezone=True), index=True, nullable=True),
            Column("status", String(32), default="active", index=True),
        )

        self._metrics_table = Table(
            f"nb_cron_{name}_metrics", self._metadata,
            Column("job_id", String(255), primary_key=True),
            Column("data", Text, nullable=False),
        )

        self._functions_table = Table(
            f"nb_cron_{name}_functions", self._metadata,
            Column("func_name", String(255), primary_key=True),
            Column("data", Text, nullable=False),
        )

        self._metadata.create_all(self._engine)

    def add_job(self, job: Job) -> None:
        session = self._Session()
        try:
            existing = session.execute(
                self._jobs_table.select().where(
                    self._jobs_table.c.job_id == job.job_id
                )
            ).fetchone()
            if existing:
                raise ValueError(f"Job '{job.job_id}' already exists")
            session.execute(
                self._jobs_table.insert().values(
                    job_id=job.job_id,
                    data=json.dumps(job.to_dict()),
                    next_run_time=job.next_run_time,
                    status=job.status,
                )
            )
            session.commit()
        finally:
            session.close()

    def update_job(self, job: Job) -> None:
        session = self._Session()
        try:
            session.execute(
                self._jobs_table.update()
                .where(self._jobs_table.c.job_id == job.job_id)
                .values(
                    data=json.dumps(job.to_dict()),
                    next_run_time=job.next_run_time,
                    status=job.status,
                )
            )
            session.commit()
        finally:
            session.close()

    def remove_job(self, job_id: str) -> None:
        session = self._Session()
        try:
            session.execute(
                self._jobs_table.delete().where(self._jobs_table.c.job_id == job_id)
            )
            session.execute(
                self._metrics_table.delete().where(self._metrics_table.c.job_id == job_id)
            )
            session.commit()
        finally:
            session.close()

    def get_job(self, job_id: str) -> Optional[Job]:
        session = self._Session()
        try:
            row = session.execute(
                self._jobs_table.select().where(self._jobs_table.c.job_id == job_id)
            ).fetchone()
            if row is None:
                return None
            data = json.loads(row.data if hasattr(row, "data") else row[1])
            return Job.from_dict(data)
        finally:
            session.close()

    def get_all_jobs(self) -> List[Job]:
        session = self._Session()
        try:
            rows = session.execute(self._jobs_table.select()).fetchall()
            result = []
            for row in rows:
                data = json.loads(row.data if hasattr(row, "data") else row[1])
                result.append(Job.from_dict(data))
            return result
        finally:
            session.close()

    def get_due_jobs(self, now: datetime) -> List[Job]:
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        session = self._Session()
        try:
            rows = session.execute(
                self._jobs_table.select().where(
                    self._jobs_table.c.status == "active",
                    self._jobs_table.c.next_run_time <= now,
                    self._jobs_table.c.next_run_time.isnot(None),
                )
            ).fetchall()
            result = []
            for row in rows:
                data = json.loads(row.data if hasattr(row, "data") else row[1])
                result.append(Job.from_dict(data))
            return result
        finally:
            session.close()

    def update_next_run_time(self, job_id: str, next_run_time: Optional[datetime]) -> None:
        session = self._Session()
        try:
            row = session.execute(
                self._jobs_table.select().where(self._jobs_table.c.job_id == job_id)
            ).fetchone()
            if row is None:
                return
            data = json.loads(row.data if hasattr(row, "data") else row[1])
            data["next_run_time"] = next_run_time.isoformat() if next_run_time else None
            data["updated_at"] = datetime.now(timezone.utc).isoformat()
            session.execute(
                self._jobs_table.update()
                .where(self._jobs_table.c.job_id == job_id)
                .values(
                    data=json.dumps(data),
                    next_run_time=next_run_time,
                )
            )
            session.commit()
        finally:
            session.close()

    def save_metrics(self, job_id: str, metrics: Dict[str, Any]) -> None:
        session = self._Session()
        try:
            existing = session.execute(
                self._metrics_table.select().where(
                    self._metrics_table.c.job_id == job_id
                )
            ).fetchone()
            payload = json.dumps(metrics, default=str)
            if existing:
                session.execute(
                    self._metrics_table.update()
                    .where(self._metrics_table.c.job_id == job_id)
                    .values(data=payload)
                )
            else:
                session.execute(
                    self._metrics_table.insert().values(job_id=job_id, data=payload)
                )
            session.commit()
        finally:
            session.close()

    def get_metrics(self, job_id: str) -> Optional[Dict[str, Any]]:
        session = self._Session()
        try:
            row = session.execute(
                self._metrics_table.select().where(
                    self._metrics_table.c.job_id == job_id
                )
            ).fetchone()
            if row is None:
                return None
            return json.loads(row.data if hasattr(row, "data") else row[1])
        finally:
            session.close()

    def get_all_metrics(self) -> Dict[str, Dict[str, Any]]:
        session = self._Session()
        try:
            rows = session.execute(self._metrics_table.select()).fetchall()
            result = {}
            for row in rows:
                jid = row.job_id if hasattr(row, "job_id") else row[0]
                data = row.data if hasattr(row, "data") else row[1]
                result[jid] = json.loads(data)
            return result
        finally:
            session.close()

    def register_function(self, func_name: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        session = self._Session()
        try:
            existing = session.execute(
                self._functions_table.select().where(
                    self._functions_table.c.func_name == func_name
                )
            ).fetchone()
            payload = json.dumps(metadata or {})
            if existing:
                session.execute(
                    self._functions_table.update()
                    .where(self._functions_table.c.func_name == func_name)
                    .values(data=payload)
                )
            else:
                session.execute(
                    self._functions_table.insert().values(func_name=func_name, data=payload)
                )
            session.commit()
        finally:
            session.close()

    def get_function_names(self) -> List[str]:
        session = self._Session()
        try:
            rows = session.execute(self._functions_table.select()).fetchall()
            return [row.func_name if hasattr(row, "func_name") else row[0] for row in rows]
        finally:
            session.close()

    def close(self) -> None:
        self._engine.dispose()

`````

--- **end of file: nb_cron/stores/sqlalchemy_store.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/stores/__init__.py** (project: nb_cron) --- 

`````python
from nb_cron.stores.base import BaseStore

__all__ = ["BaseStore"]

`````

--- **end of file: nb_cron/stores/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/triggers/base.py** (project: nb_cron) --- 

`````python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class BaseTrigger(ABC):

    @abstractmethod
    def get_next_fire_time(
        self,
        previous_fire_time: Optional[datetime],
        now: datetime,
    ) -> Optional[datetime]:
        """Calculate next fire time after `now`, given the previous fire time."""

    @abstractmethod
    def get_trigger_info(self) -> dict:
        """Return serializable trigger configuration."""

    @abstractmethod
    def get_description(self, lang: str = "en") -> str:
        """Return human-readable description of this trigger."""

`````

--- **end of file: nb_cron/triggers/base.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/triggers/cron_trigger.py** (project: nb_cron) --- 

`````python
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from croniter import croniter

from nb_cron.triggers.base import BaseTrigger


def _user_to_croniter(expression: str) -> str:
    """
    Convert user format (sec min hour day month dow)
    to croniter format (min hour day month dow sec).
    """
    fields = expression.strip().split()
    sec, min_, hour, day, month, dow = fields
    return f"{min_} {hour} {day} {month} {dow} {sec}"


def _croniter_to_user(expression: str) -> str:
    """
    Convert croniter format (min hour day month dow sec)
    back to user format (sec min hour day month dow).
    """
    fields = expression.strip().split()
    min_, hour, day, month, dow, sec = fields
    return f"{sec} {min_} {hour} {day} {month} {dow}"


class CronTrigger(BaseTrigger):
    """
    Cron trigger that REQUIRES exactly 6 fields:
        second  minute  hour  day_of_month  month  day_of_week

    5-field expressions will raise ValueError immediately.

    Internally converts to croniter's format (min hour day month dow sec)
    for calculation.
    """

    def __init__(self, expression: str):
        self.expression = self._validate(expression)
        self._croniter_expr = _user_to_croniter(self.expression)

    @staticmethod
    def _validate(expression: str) -> str:
        fields = expression.strip().split()
        if len(fields) != 6:
            raise ValueError(
                f"nb_cron requires exactly 6-field cron (second minute hour day month weekday), "
                f"got {len(fields)} fields: '{expression}'. "
                f"Example: '0 */5 * * * *' means every 5 minutes at second 0."
            )
        croniter_expr = _user_to_croniter(expression)
        try:
            croniter(croniter_expr)
        except (ValueError, KeyError, TypeError) as e:
            raise ValueError(f"Invalid cron expression: '{expression}' ({e})")
        return expression.strip()

    def get_next_fire_time(
        self,
        previous_fire_time: Optional[datetime],
        now: datetime,
    ) -> Optional[datetime]:
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        base = previous_fire_time if previous_fire_time else now
        if base.tzinfo is None:
            base = base.replace(tzinfo=timezone.utc)
        cron = croniter(self._croniter_expr, base)
        next_time = cron.get_next(datetime)
        if next_time.tzinfo is None:
            next_time = next_time.replace(tzinfo=timezone.utc)
        if next_time <= now and previous_fire_time:
            cron = croniter(self._croniter_expr, now)
            next_time = cron.get_next(datetime)
            if next_time.tzinfo is None:
                next_time = next_time.replace(tzinfo=timezone.utc)
        return next_time

    def get_trigger_info(self) -> Dict[str, Any]:
        return {"type": "cron", "expression": self.expression}

    def get_description(self, lang: str = "en") -> str:
        from nb_cron.cron_utils.translator import explain_cron
        return explain_cron(self.expression, lang)

    def __repr__(self) -> str:
        return f"CronTrigger('{self.expression}')"

`````

--- **end of file: nb_cron/triggers/cron_trigger.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/triggers/date_trigger.py** (project: nb_cron) --- 

`````python
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from nb_cron.triggers.base import BaseTrigger


class DateTrigger(BaseTrigger):
    """One-time trigger that fires at a specific datetime."""

    def __init__(self, run_time: datetime):
        if run_time.tzinfo is None:
            run_time = run_time.replace(tzinfo=timezone.utc)
        self.run_time = run_time

    def get_next_fire_time(
        self,
        previous_fire_time: Optional[datetime],
        now: datetime,
    ) -> Optional[datetime]:
        if previous_fire_time is not None:
            return None
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        if self.run_time > now:
            return self.run_time
        return None

    def get_trigger_info(self) -> Dict[str, Any]:
        return {"type": "date", "run_time": self.run_time.isoformat()}

    def get_description(self, lang: str = "en") -> str:
        time_str = self.run_time.strftime("%Y-%m-%d %H:%M:%S")
        if lang == "zh":
            return f"在 {time_str} 执行一次"
        return f"Run once at {time_str}"

    def __repr__(self) -> str:
        return f"DateTrigger({self.run_time.isoformat()})"

`````

--- **end of file: nb_cron/triggers/date_trigger.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/triggers/interval_trigger.py** (project: nb_cron) --- 

`````python
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from nb_cron.triggers.base import BaseTrigger


class IntervalTrigger(BaseTrigger):

    def __init__(
        self,
        weeks: int = 0,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        start_time: Optional[datetime] = None,
    ):
        self.interval = timedelta(
            weeks=weeks, days=days, hours=hours,
            minutes=minutes, seconds=seconds,
        )
        if self.interval.total_seconds() <= 0:
            raise ValueError("Interval must be positive")
        self.start_time = start_time
        self._weeks = weeks
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_next_fire_time(
        self,
        previous_fire_time: Optional[datetime],
        now: datetime,
    ) -> Optional[datetime]:
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        if previous_fire_time is not None:
            if previous_fire_time.tzinfo is None:
                previous_fire_time = previous_fire_time.replace(tzinfo=timezone.utc)
            next_time = previous_fire_time + self.interval
            if next_time <= now:
                skipped = int((now - next_time).total_seconds() / self.interval.total_seconds())
                next_time += self.interval * (skipped + 1)
                if next_time <= now:
                    next_time += self.interval
            return next_time
        if self.start_time is not None:
            st = self.start_time
            if st.tzinfo is None:
                st = st.replace(tzinfo=timezone.utc)
            if st > now:
                return st
            skipped = int((now - st).total_seconds() / self.interval.total_seconds())
            next_time = st + self.interval * (skipped + 1)
            if next_time <= now:
                next_time += self.interval
            return next_time
        # 首次调度：尽快执行（下一拍 tick 内），而不是先空等一个整周期。
        # 之后由 previous_fire_time 分支按 interval 推进。
        return now

    def get_trigger_info(self) -> Dict[str, Any]:
        return {
            "type": "interval",
            "weeks": self._weeks,
            "days": self._days,
            "hours": self._hours,
            "minutes": self._minutes,
            "seconds": self._seconds,
        }

    def get_description(self, lang: str = "en") -> str:
        parts_en = []
        parts_zh = []
        if self._weeks:
            parts_en.append(f"{self._weeks} week{'s' if self._weeks > 1 else ''}")
            parts_zh.append(f"{self._weeks}周")
        if self._days:
            parts_en.append(f"{self._days} day{'s' if self._days > 1 else ''}")
            parts_zh.append(f"{self._days}天")
        if self._hours:
            parts_en.append(f"{self._hours} hour{'s' if self._hours > 1 else ''}")
            parts_zh.append(f"{self._hours}小时")
        if self._minutes:
            parts_en.append(f"{self._minutes} minute{'s' if self._minutes > 1 else ''}")
            parts_zh.append(f"{self._minutes}分钟")
        if self._seconds:
            parts_en.append(f"{self._seconds} second{'s' if self._seconds > 1 else ''}")
            parts_zh.append(f"{self._seconds}秒")
        if lang == "zh":
            return "每" + "".join(parts_zh) + "执行一次"
        return "Every " + " ".join(parts_en)

    def __repr__(self) -> str:
        total = self.interval.total_seconds()
        return f"IntervalTrigger(every {total}s)"

`````

--- **end of file: nb_cron/triggers/interval_trigger.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/triggers/__init__.py** (project: nb_cron) --- 

`````python
from nb_cron.triggers.base import BaseTrigger
from nb_cron.triggers.cron_trigger import CronTrigger
from nb_cron.triggers.interval_trigger import IntervalTrigger
from nb_cron.triggers.date_trigger import DateTrigger

__all__ = ["BaseTrigger", "CronTrigger", "IntervalTrigger", "DateTrigger"]

`````

--- **end of file: nb_cron/triggers/__init__.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/web/app.py** (project: nb_cron) --- 

`````python
"""
One-line app factories for FastAPI / Flask / Django.

Usage::

    # FastAPI
    from nb_cron.web import get_fastapi_app
    app = get_fastapi_app(cron)          # uvicorn module:app

    # Flask
    from nb_cron.web import get_flask_app
    app = get_flask_app(cron)            # flask run / gunicorn module:app

    # Django - in urls.py
    from nb_cron.web import get_django_urls
    urlpatterns += get_django_urls(cron)
"""
from pathlib import Path

from nb_cron.web.static_mime import guess_asset_content_type, register_static_mimetypes

STATIC_DIR = Path(__file__).parent / "static"

# Fix Windows: .js must not be served as text/plain (breaks ES modules)
register_static_mimetypes()


def get_fastapi_app(cron, title: str = "nb_cron", **kwargs):
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        from fastapi.responses import FileResponse, HTMLResponse
    except ImportError:
        raise ImportError("Install with: pip install nb_cron_nb[fastapi]")

    from nb_cron.api.fastapi_app import create_router

    app = FastAPI(title=title, **kwargs)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(create_router(cron))

    @app.get("/")
    async def redirect_to_ui():
        from fastapi.responses import RedirectResponse
        return RedirectResponse(url="/nb_cron/ui/")

    if STATIC_DIR.exists():
        assets_root = (STATIC_DIR / "assets").resolve()

        @app.get("/nb_cron/ui/favicon.svg")
        async def serve_favicon():
            favicon = STATIC_DIR / "favicon.svg"
            if favicon.exists():
                return FileResponse(str(favicon), media_type="image/svg+xml")
            return HTMLResponse("", status_code=404)

        @app.get("/nb_cron/ui/assets/{asset_path:path}")
        async def serve_ui_assets(asset_path: str):
            """Explicit MIME types — Windows mimetypes often serve .js as text/plain."""
            from fastapi import HTTPException

            target = (STATIC_DIR / "assets" / asset_path).resolve()
            try:
                target.relative_to(assets_root)
            except ValueError:
                raise HTTPException(status_code=404, detail="Not found")
            if not target.is_file():
                raise HTTPException(status_code=404, detail="Not found")
            return FileResponse(
                str(target),
                media_type=guess_asset_content_type(asset_path),
            )

        @app.get("/nb_cron/ui/{rest_of_path:path}")
        async def serve_spa(rest_of_path: str = ""):
            index = STATIC_DIR / "index.html"
            if index.exists():
                return FileResponse(str(index))
            return HTMLResponse("<h1>nb_cron UI not built</h1><p>Run: cd nb_cron_ui && npm run build</p>")

        @app.get("/nb_cron/ui")
        async def serve_spa_root():
            index = STATIC_DIR / "index.html"
            if index.exists():
                return FileResponse(str(index))
            return HTMLResponse("<h1>nb_cron UI not built</h1><p>Run: cd nb_cron_ui && npm run build</p>")

    return app


def get_flask_app(cron, **kwargs):
    try:
        from flask import Flask, send_from_directory, send_file
        from flask_cors import CORS
    except ImportError:
        try:
            from flask import Flask, send_from_directory, send_file
        except ImportError:
            raise ImportError("Install with: pip install nb_cron_nb[flask]")

    from nb_cron.api.flask_app import create_blueprint

    app = Flask(__name__, **kwargs)
    try:
        from flask_cors import CORS
        CORS(app)
    except ImportError:
        pass

    app.register_blueprint(create_blueprint(cron))

    @app.route("/")
    def redirect_to_ui():
        from flask import redirect
        return redirect("/nb_cron/ui/")

    if STATIC_DIR.exists():
        @app.route("/nb_cron/ui/favicon.svg")
        def serve_favicon():
            return send_from_directory(str(STATIC_DIR), "favicon.svg", mimetype="image/svg+xml")

        @app.route("/nb_cron/ui/assets/<path:filename>")
        def serve_assets(filename):
            return send_from_directory(
                str(STATIC_DIR / "assets"),
                filename,
                mimetype=guess_asset_content_type(filename),
            )

        @app.route("/nb_cron/ui")
        @app.route("/nb_cron/ui/")
        @app.route("/nb_cron/ui/<path:path>")
        def serve_spa(path=""):
            index = STATIC_DIR / "index.html"
            if index.exists():
                return send_file(str(index))
            return "<h1>nb_cron UI not built</h1><p>Run: cd nb_cron_ui && npm run build</p>", 200

    return app


def get_django_urls(cron):
    try:
        from django.urls import path
        from django.http import FileResponse as DjFileResponse, HttpResponse
    except ImportError:
        raise ImportError("Install with: pip install nb_cron_nb[django]")

    from nb_cron.api.django_app import create_router

    try:
        from ninja import NinjaAPI
    except ImportError:
        raise ImportError("Install with: pip install nb_cron_nb[django]")

    api = NinjaAPI(urls_namespace="nb_cron")
    api.add_router("/nb_cron/api", create_router(cron))

    assets_dir = (STATIC_DIR / "assets").resolve()

    def serve_ui_asset(request, path):
        from django.http import Http404

        target = (STATIC_DIR / "assets" / path).resolve()
        try:
            target.relative_to(assets_dir)
        except ValueError:
            raise Http404("Not found")
        if not target.is_file():
            raise Http404("Not found")
        return DjFileResponse(
            str(target),
            content_type=guess_asset_content_type(path),
        )

    def serve_spa(request, rest=""):
        index = STATIC_DIR / "index.html"
        if index.exists():
            return DjFileResponse(str(index), content_type="text/html")
        return HttpResponse(
            "<h1>nb_cron UI not built</h1><p>Run: cd nb_cron_ui && npm run build</p>"
        )

    def redirect_to_ui(request):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect("/nb_cron/ui/")

    urls = [
        path("", redirect_to_ui),
        path("nb_cron/api/", api.urls),
        path("nb_cron/ui/assets/<path:path>", serve_ui_asset),
        path("nb_cron/ui/", serve_spa),
        path("nb_cron/ui/<path:rest>", serve_spa),
    ]
    return urls

`````

--- **end of file: nb_cron/web/app.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/web/static_mime.py** (project: nb_cron) --- 

`````python
"""
Ensure correct Content-Type for Vite-built assets.

On Windows, mimetypes.guess_type() often returns text/plain for .js,
which breaks <script type="module"> in browsers (strict MIME check).
"""
import mimetypes
from pathlib import Path

_STATIC_TYPES = (
    (".js", "application/javascript"),
    (".mjs", "application/javascript"),
    (".cjs", "application/javascript"),
    (".css", "text/css"),
    (".json", "application/json"),
    (".map", "application/json"),
    (".svg", "image/svg+xml"),
    (".wasm", "application/wasm"),
    (".woff2", "font/woff2"),
    (".woff", "font/woff"),
    (".ttf", "font/ttf"),
    (".ico", "image/x-icon"),
)


def register_static_mimetypes() -> None:
    """Register MIME types so Starlette StaticFiles / uvicorn serve correct headers."""
    for ext, ctype in _STATIC_TYPES:
        mimetypes.add_type(ctype, ext, strict=True)


def guess_asset_content_type(filename: str) -> str:
    """Return Content-Type for a file under assets/; safe for Windows."""
    ext = Path(filename).suffix.lower()
    for e, ctype in _STATIC_TYPES:
        if e == ext:
            return ctype
    guessed, _ = mimetypes.guess_type(filename)
    if guessed and guessed != "text/plain":
        return guessed
    return "application/octet-stream"


register_static_mimetypes()

`````

--- **end of file: nb_cron/web/static_mime.py** (project: nb_cron) --- 

---


--- **start of file: nb_cron/web/__init__.py** (project: nb_cron) --- 

`````python
from nb_cron.web.app import get_fastapi_app, get_flask_app, get_django_urls

__all__ = ["get_fastapi_app", "get_flask_app", "get_django_urls"]

`````

--- **end of file: nb_cron/web/__init__.py** (project: nb_cron) --- 

---

