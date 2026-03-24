
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
# markdown content namespace: nb_cache project summary 



- `nb_cache` is a powerful cache library for Python. 
- `cache(...)` is the main method for  user.


## 📋 nb_cache most core source files metadata (Entry Points)


以下是项目 nb_cache 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nb_cache most core source code files as follows: 
- `nb_cache/__init__.py`
- `nb_cache/wrapper.py`


### 📄 Python File Metadata: `nb_cache/__init__.py`

#### 📝 Module Docstring

`````
nb_cache — 更强的缓存装饰器

支持同步和异步函数，支持加锁防止缓存击穿，
支持内存和Redis作为缓存器，支持Redis+内存双缓存提高性能。

Usage::

    from nb_cache import Cache

    cache = Cache()
    cache.setup("mem://")

    @cache.cache(ttl=60)
    def get_data(key):
        return expensive_query(key)

    @cache.cache(ttl="1h", lock=True)
    async def get_data_async(key):
        return await expensive_query_async(key)
`````

#### 📦 Imports

- `from nb_cache.wrapper import Cache`
- `from nb_cache.wrapper import register_backend`
- `from nb_cache.condition import NOT_NONE`
- `from nb_cache.condition import with_exceptions`
- `from nb_cache.condition import only_exceptions`
- `from nb_cache.exceptions import CacheError`
- `from nb_cache.exceptions import BackendNotInitializedError`
- `from nb_cache.exceptions import CacheBackendInteractionError`
- `from nb_cache.exceptions import LockError`
- `from nb_cache.exceptions import LockedError`
- `from nb_cache.exceptions import CircuitBreakerOpen`
- `from nb_cache.exceptions import RateLimitError`
- `from nb_cache.exceptions import SerializationError`
- `from nb_cache.exceptions import TagError`
- `from nb_cache.transaction import TransactionMode`
- `from nb_cache.key import get_cache_key_template`
- `from nb_cache.helpers import noself`
- `from nb_cache.helpers import add_prefix`
- `from nb_cache.helpers import memory_limit`
- `from nb_cache.helpers import invalidate_further`
- `from nb_cache.serialize import Serializer`
- `from nb_cache.serialize import PickleSerializer`
- `from nb_cache.serialize import JsonSerializer`
- `from nb_cache.serialize import GzipCompressor`
- `from nb_cache.serialize import ZlibCompressor`
- `from nb_cache.serialize import HashSigner`
- `from nb_cache.ttl import ttl_to_seconds`
- `from nb_cache.backends.base import BaseBackend`
- `from nb_cache.backends.memory import MemoryBackend`


---




### 📄 Python File Metadata: `nb_cache/wrapper.py`

#### 📝 Module Docstring

`````
Cache wrapper — the main entry point for nb_cache.

Integrates backends, decorators, commands, tags, transactions,
and middleware into a single unified API.
`````

#### 📦 Imports

- `import contextlib`
- `import functools`
- `import threading`
- `from nb_cache._compat import is_coroutine_function`
- `from nb_cache.backends.memory import MemoryBackend`
- `from nb_cache.condition import NOT_NONE`
- `from nb_cache.condition import get_cache_condition`
- `from nb_cache.condition import with_exceptions`
- `from nb_cache.condition import only_exceptions`
- `from nb_cache.exceptions import BackendNotInitializedError`
- `from nb_cache.key import get_cache_key_template`
- `from nb_cache.serialize import Serializer`
- `from nb_cache.serialize import PickleSerializer`
- `from nb_cache.serialize import JsonSerializer`
- `from nb_cache.serialize import GzipCompressor`
- `from nb_cache.serialize import ZlibCompressor`
- `from nb_cache.serialize import NullCompressor`
- `from nb_cache.serialize import HashSigner`
- `from nb_cache.serialize import default_serializer`
- `from nb_cache.tags import TagRegistry`
- `from nb_cache.tags import get_default_tag_registry`
- `from nb_cache.transaction import Transaction`
- `from nb_cache.transaction import TransactionMode`
- `from nb_cache.ttl import ttl_to_seconds`
- `import importlib`
- `from urllib.parse import urlparse`
- `from urllib.parse import parse_qs`
- `import asyncio`
- `from nb_cache.decorators.cache import cache as _cache`
- `from nb_cache.decorators.failover import failover as _failover`
- `from nb_cache.decorators.early import early as _early`
- `from nb_cache.decorators.soft import soft as _soft`
- `from nb_cache.decorators.hit import hit as _hit`
- `from nb_cache.decorators.locked import locked as _locked`
- `from nb_cache.decorators.locked import thunder_protection as _tp`
- `from nb_cache.decorators.circuit_breaker import circuit_breaker as _cb`
- `from nb_cache.decorators.rate_limit import rate_limit as _rl`
- `from nb_cache.decorators.rate_limit import slice_rate_limit as _srl`
- `from nb_cache.decorators.bloom import bloom as _bloom`
- `from nb_cache.decorators.bloom import dual_bloom as _db`
- `from nb_cache.decorators.iterator import iterator as _iter`
- `import time`
- `import time`
- `from nb_cache.exceptions import LockedError`
- `from nb_cache.exceptions import LockedError`
- `from nb_cache.key import get_cache_key`
- `from nb_cache.key import get_cache_key`

#### 🏛️ Classes (1)

##### 📌 `class Cache(object)`
*Line: 124*

**Docstring:**
`````
Main cache interface. Integrates backend, decorators, tags, etc.

Usage::

    from nb_cache import cache

    # Setup with URL
    cache.setup("mem://")
    cache.setup("redis://localhost:6379/0")

    # Direct operations
    cache.set_sync("key", "value", ttl=60)
    val = cache.get_sync("key")

    # As decorator
    @cache.cache(ttl=60)
    def get_user(user_id):
        return db.query(user_id)
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self)`
  - **Parameters:**
    - `self`

**Public Methods (60):**
- `def setup(self, settings_url, middlewares = None, prefix = '', key_include_func = True, **kwargs)`
  - **Docstring:**
  `````
  Configure the cache backend from a URL.
  
  Args:
      settings_url: URL like 'mem://', 'redis://host:port/db'.
      middlewares: List of Middleware instances.
      prefix: Global key prefix.
      key_include_func: If False, the module path and function name are NOT
          included in auto-generated cache keys. Useful for short, business-logic-only
          keys. Default is True.
      **kwargs: Extra arguments passed to the backend.
  
  Supported URL schemes: mem://, redis://, rediss://, dual://
  `````
- `async def init(self)`
  - **Docstring:**
  `````
  Re-initialize the async client (only needed if you use setup() in a sync
  context but later need to swap to a freshly-created async event loop).
  `````
- `def init_sync(self)`
  - **Docstring:**
  `````
  Explicitly re-initialize the backend. Usually not needed — setup() calls
  this automatically.
  `````
- `async def close(self)`
- `def close_sync(self)`
- `async def ping(self)`
- `def ping_sync(self)`
- `async def get(self, key)`
- `async def set(self, key, value, ttl = None)`
- `async def delete(self, key)`
- `async def exists(self, key)`
- `async def expire(self, key, ttl)`
- `async def get_expire(self, key)`
- `async def clear(self)`
- `async def incr(self, key, amount = 1)`
- `async def get_many(self, *keys)`
- `async def set_many(self, pairs, ttl = None)`
- `async def delete_many(self, *keys)`
- `async def delete_match(self, pattern)`
- `async def scan(self, pattern)`
- `async def get_match(self, pattern)`
- `async def get_keys_count(self)`
- `async def get_size(self)`
- `async def set_lock(self, key, ttl)`
- `async def unlock(self, key)`
- `async def is_locked(self, key)`
- `def get_sync(self, key)`
- `def set_sync(self, key, value, ttl = None)`
- `def delete_sync(self, key)`
- `def exists_sync(self, key)`
- `def expire_sync(self, key, ttl)`
- `def get_expire_sync(self, key)`
- `def clear_sync(self)`
- `def incr_sync(self, key, amount = 1)`
- `def get_many_sync(self, *keys)`
- `def set_many_sync(self, pairs, ttl = None)`
- `def delete_many_sync(self, *keys)`
- `def delete_match_sync(self, pattern)`
- `def scan_sync(self, pattern)`
- `def get_match_sync(self, pattern)`
- `def lock(self, key, ttl = 60)` `contextlib.contextmanager`
  - **Docstring:**
  `````
  Sync lock context manager.
  
  Usage::
  
      with cache.lock("resource", ttl=10):
          do_something()
  `````
- `async def alock(self, key, ttl = 60)` `contextlib.asynccontextmanager`
  - **Docstring:**
  `````
  Async lock context manager.
  
  Usage::
  
      async with cache.alock("resource", ttl=10):
          await do_something()
  `````
- `def delete_tags_sync(self, *tags)`
  - *Delete all keys associated with the given tags (sync).*
- `async def delete_tags(self, *tags)`
  - *Delete all keys associated with the given tags (async).*
- `def transaction(self, mode = TransactionMode.FAST)`
  - **Docstring:**
  `````
  Create a transaction (works as both sync and async context manager).
  
  Usage::
  
      with cache.transaction() as tx:
          tx.set("k1", "v1")
          tx.set("k2", "v2")
  
      async with cache.transaction() as tx:
          tx.set("k1", "v1")
  `````
- `def cache(self, ttl, key = None, condition = None, prefix = '', lock = False, lock_ttl = None, tags = (), serializer = None, key_include_func: bool = None)`
- `def failover(self, ttl, key = None, exceptions = None, condition = None, prefix = 'fail', tags = (), serializer = None)`
- `def early(self, ttl, key = None, early_ttl = None, condition = None, prefix = 'early', tags = (), serializer = None)`
- `def soft(self, ttl, key = None, soft_ttl = None, condition = None, prefix = 'soft', tags = (), serializer = None)`
- `def hit(self, ttl, cache_hits, update_after = 0, key = None, condition = None, prefix = 'hit', tags = (), serializer = None)`
- `def locked(self, ttl = None, key = None, wait = True, prefix = 'locked', check_interval = 0.1)`
- `def thunder_protection(self, ttl = None, key = None, prefix = 'thunder')`
- `def circuit_breaker(self, errors_rate, period, ttl, half_open_ttl = None, exceptions = None, key = None, min_calls = 1, prefix = 'circuit_breaker')`
- `def rate_limit(self, limit, period, ttl = None, action = None, prefix = 'rate_limit', key = None)`
- `def slice_rate_limit(self, limit, period, key = None, action = None, prefix = 'srl')`
- `def bloom(self, capacity, name = None, false_positives = 1, prefix = 'bloom')`
- `def dual_bloom(self, capacity, name = None, false = 1, prefix = 'dual_bloom')`
- `def iterator(self, ttl, key = None, condition = None, prefix = 'iter', serializer = None)`
- `def invalidate(self, func_or_cache_instance, args_map = None)`
  - **Docstring:**
  `````
  Decorator that invalidates cache for a cached function.
  
  Usage::
  
      @cache.cache(ttl=60)
      def get_user(user_id):
          ...
  
      @cache.invalidate(get_user)
      def update_user(user_id, data):
          ...
  `````
- `def add_middleware(self, middleware)`

**Properties (3):**
- `@property is_setup`
- `@property is_init`
- `@property backend`

#### 🔧 Public Functions (1)

- `def register_backend(scheme, backend_path)`
  - *Line: 114*
  - **Docstring:**
  `````
  Register a custom backend class.
  
  Args:
      scheme: URL scheme (e.g. 'custom').
      backend_path: Dotted path like 'mymodule:MyBackend'.
  `````


---



## 🔗 nb_cache Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Core Files (imported by other files, sorted by import count):
  ◆ nb_cache/__init__.py (imported by 1 files)
  ◆ nb_cache/wrapper.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `nb_cache/__init__.py`

**Imports from project:**
- `nb_cache/wrapper.py`

**Imported by:**
- `nb_cache/wrapper.py`

#### `nb_cache/wrapper.py`

**Imports from project:**
- `nb_cache/__init__.py`

**Imported by:**
- `nb_cache/__init__.py`


---
# markdown content namespace: nb_cache Project Root Dir Some Files 


## nb_cache File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## nb_cache (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: nb_cache) --- 

`````markdown

# 🚀 nb_cache: Python 缓存界的“瑞士军刀”

[![Python Versions](https://img.shields.io/badge/python-3.6+-blue.svg)](https://pypi.org/project/nb-cache/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **`nb_cache` 不仅是一个基础的缓存装饰器，它在彻底抹平 Python 同步与异步代码差异的同时，开箱即用地提供了内存/Redis双层缓存、防击穿、防雪崩、限流与熔断等企业级高可用特性。**

在如今混杂着 Sync 和 Async 的 Python 项目中，开发者往往需要为同步代码和异步代码寻找不同的缓存解决方案。`nb_cache` 彻底抹平了这一差异——**只需同一个装饰器，即可完美兼容同步与异步函数**。

如果你曾经使用过 `cashews`，你会对 `nb_cache` 感到非常亲切。`nb_cache` 吸收了其优秀的特性，并弥补了其最大的短板：**全面支持同/异步场景，且所有底层操作兼具 Sync 和 Async 两种 API**。

## ✨ 核心特性

- ☯️ **同/异步无缝统一**：无需区分 `@cache` 或 `@acache`，同一个装饰器自动识别普通函数与协程，内部自动路由。同一套上下文管理器同时支持 `with` 和 `async with`。
- 🚀 **丰富的高级后端**：
  - **Memory (`mem://`)**: 极速的本地 LRU 内存缓存。
  - **Redis (`redis://`)**: 分布式 Redis 缓存，支持连接池。
  - **双层缓存 (`dual://`)**: **(杀手级特性)** 本地内存(L1) + Redis(L2) 的透明双重缓存。读取时优先击中内存，写入时双写，彻底释放 Redis 压力。
- 🛡️ **企业级高可用防护**：
  - **防缓存击穿 (Stampede)**：只需一个参数 `lock=True`，即可在并发未命中时让多余请求等待，只放行一个请求去查库。
  - **防缓存雪崩 (Avalanche)**：提供 `@cache.early` (提前后台刷新) 和 `@cache.soft` (软过期，返回旧值并异步刷新) 完美解决雪崩。
  - **服务降级与失败回退**：提供 `@cache.failover`，当数据库或下游接口挂掉时，自动返回缓存的旧值兜底。
- 🔧 **极其丰富的“微服务”级装饰器**：除了缓存，还内置了**限流** (`rate_limit`, `slice_rate_limit`)、**熔断** (`circuit_breaker`)、**并发防抖** (`thunder_protection`)、**布隆过滤器** (`bloom`, `dual_bloom`)。
- 🔑 **智能 Key 路由与模板**：告别繁琐的 key 拼接。支持 `{user_id}`、`{user.name}` (直接读取对象属性)、`{data:hash}` (自动对大字典算md5) 等高级格式化模板。
- 🔒 **数据安全与压缩**：自带序列化流水线。一行配置即可开启 JSON/Pickle 序列化、Gzip/Zlib 压缩，以及 HMAC 签名（防止缓存数据被恶意篡改）。
- 🏷️ **标签系统与事务**：支持给缓存打标签 (Tags) 实现按业务模块批量失效，支持类似数据库的缓存事务 (Transaction) 自动回滚。

## 💡 为什么选择 nb_cache？

| 特性 | 传统自带 `lru_cache` | `redis-py` 原生 | `cashews` | 🏆 `nb_cache` |
| :--- | :---: | :---: | :---: | :---: |
| **同步函数支持** | ✅ | ✅ | ❌ | **✅ 完美支持** |
| **异步函数 (Asyncio) 支持** | ❌ | ✅ | ✅ | **✅ 完美支持** |
| **内存/Redis 双重缓存** | ❌ | ❌ | ✅ | **✅ 开箱即用** |
| **防击穿 (分布式锁合并请求)** | ❌ | 需手写代码 | ✅ | **✅ `lock=True`** |
| **防雪崩/后台自动刷新** | ❌ | 需手写代码 | ✅ | **✅ `@cache.early`** |
| **限流与熔断** | ❌ | 需手写代码 | ✅ | **✅ 内置支持** |

---

### 👉 接下来，请看下方的【安装】与【快速开始】，体验一行代码带来的架构升级：

## 安装

```bash
pip install nb_cache

# 使用 Redis 后端
pip install nb_cache[redis]

# 全部可选依赖
pip install nb_cache[all]
```

## 快速开始

`setup()` 会自动完成初始化，无需手动调用 `init_sync()`。

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 同步函数缓存
@cache.cache(ttl=60)
def get_user(user_id):
    return db.query(user_id)

# 异步函数缓存（同一个装饰器，自动识别）
@cache.cache(ttl="1h")
async def get_user_async(user_id):
    return await db.query_async(user_id)

# 加锁防止缓存击穿,如果123这个入参没有缓存，但是同一秒请求123这个入参1万次，
# 加上lock=True后，只有第一次请求会真正执行函数，其余请求等待并复用第一次请求的结果，避免"击穿"。
@cache.cache(ttl=60, lock=True)
def get_hot_data(key):
    time.sleep(20)
    return expensive_query(key)
```

## 不想吃苦，如何使用ai掌握nb_cache？

`nb_cache_all_docs_and_codes.md` 这个文件包含了nb_cache 的教程和全部源码。 
你把这个文件发送给deepseek ai [https://chat.deepseek.com/](https://chat.deepseek.com/) ，ai就能自动帮你掌握 `nb_cache` 的用法。 


## 对比 cashews

如果你不懂 `nb_cache` 用法，可以参考 `cashews` 的用法。ai很熟练 `cashews`的用法。

`nb_cache` 对比 `cashews` 的优点：

- 装饰器支持同步和异步函数，通过同一个装饰器来支持。
- with 支持同步和异步上下文管理器。
- 所有操作支持asyncio和同步

`cashews` 最大缺点是 不支持同步，只能用于asyncio异步场景。



## 后端配置

### 内存缓存

```python
from nb_cache import Cache

cache = Cache().setup("mem://")
```

### Redis 缓存

```python
from nb_cache import Cache

cache = Cache().setup("redis://localhost:6379/0")
```

### Redis + 内存双缓存

```python
from nb_cache import Cache

# memory_size=1000: 内存最多存 1000 条; local_ttl=30: 内存层 TTL 30秒
cache = Cache().setup("dual://localhost:6379/0?memory_size=1000&local_ttl=30")
```

双缓存策略：读取时先查内存(L1)，miss 则查 Redis(L2) 并回填内存；写入时双写。

### 多实例

每个 `Cache()` 实例独立，可以配置不同后端：

```python
from nb_cache import Cache

mem_cache = Cache().setup("mem://")
redis_cache = Cache().setup("redis://localhost:6379/0")

@mem_cache.cache(ttl=60)
def local_data(key):
    ...

@redis_cache.cache(ttl=300)
def shared_data(key):
    ...
```

### setup() 参数详细介绍

`cache.setup(settings_url, middlewares=None, prefix="", **kwargs)` 是唯一需要调用的初始化方法。

#### 基本参数

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `settings_url` | str | 必填 | 后端连接 URL，决定使用哪种后端，见下文 |
| `middlewares` | list | `None` | 中间件列表，见 [中间件](#中间件) 章节 |
| `prefix` | str | `""` | 所有缓存 key 统一加前缀，方便多项目共用同一 Redis |

#### 序列化相关 kwargs（所有后端通用）

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `pickle_type` | str | `"pickle"` | 序列化方式：`"pickle"`（默认）或 `"json"` |
| `secret` | str | `""` | HMAC 签名密钥。设置后数据写入时签名，读取时校验，防止篡改 |
| `digestmod` | str | `"md5"` | 签名算法：`"md5"` / `"sha1"` / `"sha256"` |
| `compress_type` | str | `None` | 压缩方式：`None`（不压缩）/ `"gzip"` / `"zlib"` |

```python
from nb_cache import Cache

# 使用 JSON 序列化 + gzip 压缩 + HMAC 签名
cache = Cache().setup(
    "redis://localhost:6379/0",
    pickle_type="json",
    compress_type="gzip",
    secret="my-secret-key",
    digestmod="sha256",
)
```

#### 内存后端（`mem://`）专属 kwargs

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `size` | int | `0` | 最大缓存条数（LRU 淘汰）。`0` 表示不限 |
| `check_interval` | int | `60` | 被动过期清理的间隔秒数（仅影响后台清扫频率，不影响实时过期） |

```python
from nb_cache import Cache

# 最多 5000 条，每 30 秒清扫一次过期 key
cache = Cache().setup("mem://", size=5000, check_interval=30)
```

也可以通过 URL Query String 传递：

```python
cache.setup("mem://?size=5000&check_interval=30")
```

#### Redis 后端（`redis://` / `rediss://`）专属 kwargs

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `host` | str | `"localhost"` | Redis 主机（URL 中已包含时无需重复传） |
| `port` | int | `6379` | Redis 端口 |
| `db` | int | `0` | Redis 数据库编号（0–15） |
| `password` | str | `None` | Redis 认证密码 |
| `socket_timeout` | float | `None` | Socket 超时秒数，超时后抛出异常 |
| `max_connections` | int | `None` | 连接池最大连接数，`None` 表示不限 |
| `prefix` | str | `""` | Key 前缀（优先使用 `setup()` 的 `prefix` 参数） |

URL 中已经能表达 host、port、db、password，推荐优先用 URL：

```python
from nb_cache import Cache

# 等效写法一：URL 方式（推荐）
cache = Cache().setup("redis://:mypassword@192.168.1.100:6380/2")

# 等效写法二：URL + kwargs 混用（kwargs 会覆盖 URL 中的同名参数）
cache.setup("redis://192.168.1.100", port=6380, db=2, password="mypassword")

# 设置超时 + 连接池
cache.setup(
    "redis://localhost:6379/0",
    socket_timeout=2.0,
    max_connections=50,
)

# TLS 加密连接（rediss://）
cache.setup("rediss://localhost:6380/0", password="mypassword")

# 全局 key 前缀（同一个 Redis 服务不同项目隔离）
cache.setup("redis://localhost:6379/0", prefix="myapp:prod")
```

Query String 写法同样支持：

```python
cache.setup("redis://localhost:6379/0?socket_timeout=2&max_connections=50&prefix=myapp")
```

#### Redis+内存双缓存（`dual://`）专属 kwargs

在 Redis 参数基础上，额外支持：

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `memory_size` | int | `1000` | 内存层（L1）最大缓存条数 |
| `local_ttl` | float | `None` | 内存层统一 TTL（秒）。`None` 则与 Redis 层相同。建议设置较短（如 `5`~`30`），避免内存数据过期延迟 |

```python
from nb_cache import Cache

# 内存最多 2000 条，内存层 key 最多存 10 秒（Redis 层保持装饰器上的 ttl）
cache = Cache().setup(
    "dual://localhost:6379/0",
    memory_size=2000,
    local_ttl=10,
    max_connections=100,
    prefix="myapp",
)

# 等效 URL 写法
cache.setup("dual://localhost:6379/0?memory_size=2000&local_ttl=10&max_connections=100&prefix=myapp")
```

> **local_ttl 的作用**：双缓存场景下，数据先写 Redis，再写内存。若不设 `local_ttl`，内存层 TTL 与 Redis 相同，有可能造成内存里存放了大量长期未访问的数据。设置较短的 `local_ttl`（如 30 秒）可以让内存层快速自动清理冷数据，只保留热点。

## 缓存装饰器

### 基础缓存 `cache`

```python
from nb_cache import Cache, NOT_NONE

cache = Cache().setup("mem://")

# 自动生成 key（函数全名 + 参数）
@cache.cache(ttl=60)
def get_data(key):
    return query(key)

# 缓存条件：只缓存非 None 结果
@cache.cache(ttl=60, condition=NOT_NONE)
def get_data(key):
    return might_return_none(key)
```

#### cache() 参数详细介绍

`Cache().cache(ttl, key=None, condition=None, prefix="", lock=False, lock_ttl=None, tags=(), serializer=None)`

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `ttl` | int / float / str / timedelta | 必填 | 缓存过期时间，支持多种格式，见 [TTL 格式](#ttl-格式) |
| `key` | str / callable | `None` | 缓存 key 模板或生成函数，`None` 时自动从函数名+参数生成 |
| `condition` | callable | `None`（等同 `NOT_NONE`） | 决定结果是否缓存的条件函数，见下文 |
| `prefix` | str | `""` | 附加到 key 前的额外前缀，与 `setup(prefix=...)` 叠加 |
| `lock` | bool | `False` | 是否开启分布式锁防缓存击穿，见下文 |
| `lock_ttl` | int / float / str | `None`（等同 `ttl`） | 锁的超时时间，默认与 `ttl` 相同 |
| `tags` | tuple[str] | `()` | 缓存标签，用于 `delete_tags_sync()` 按标签批量失效 |
| `serializer` | Serializer | `None`（用全局默认） | 自定义序列化器，覆盖 `setup()` 中配置的序列化方式 |

---

**`ttl` — 过期时间**

```python
from nb_cache import Cache
from datetime import timedelta

cache = Cache().setup("mem://")

@cache.cache(ttl=60)            # 60 秒
@cache.cache(ttl=1.5)           # 1.5 秒
@cache.cache(ttl="30m")         # 30 分钟
@cache.cache(ttl="1h30m")       # 1 小时 30 分钟
@cache.cache(ttl="1d")          # 1 天
@cache.cache(ttl=timedelta(hours=2))
```

---

**`key` — 缓存键**

不传时自动使用"函数全限定名 + 所有参数值"作为 key。

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 自动生成（推荐大多数场景）
@cache.cache(ttl=60)
def get_user(user_id, role):
    ...
# 生成 key 类似: "mymodule:get_user:role=admin:user_id=1"

# 简单字符串模板：{参数名}
@cache.cache(ttl=60, key="{user_id}")
def get_user(user_id, role):
    ...
# 生成 key: "1"（只用 user_id）

# 组合模板
@cache.cache(ttl=60, key="user:{user_id}:role:{role}")
def get_user(user_id, role):
    ...

# 点号访问 dict / 对象属性
@cache.cache(ttl=60, key="user:{user.id}:{user.name}")
def get_user(user):
    ...
# user={"id": 1, "name": "Alice"} → key: "user:1:Alice"

# 格式修饰符：:hash（取 md5 前8位，适合 dict/list 等复杂参数）
@cache.cache(ttl=60, key="myproj1:search:{keyword:lower}:{filters:hash}")
def search(keyword, filters):
    ...

# callable：参数与被装饰函数完全相同，返回 key 字符串
def make_key(user, action):
    return "perm:{}:{}:{}".format(user["org"], user["id"], action)

@cache.cache(ttl=300, key=make_key)
def check_permission(user, action):
    ...
```

---

**`condition` — 缓存条件**

决定函数返回值是否应该被缓存。默认等同于 `NOT_NONE`（即返回 None 时不缓存）。

```python
from nb_cache import Cache, NOT_NONE, with_exceptions, only_exceptions

cache = Cache().setup("mem://")

# NOT_NONE（默认）：只缓存非 None 结果
@cache.cache(ttl=60, condition=NOT_NONE)
def get_data(key):
    return query(key)   # 返回 None 时不缓存

# 自定义条件：结果满足某个业务规则才缓存
@cache.cache(ttl=60, condition=lambda r: r is not None and r.get("status") == "ok")
def get_order(order_id):
    ...

# 永远缓存（包括 None）
@cache.cache(ttl=60, condition=lambda r: True)
def might_return_none(key):
    ...
```

---

**`lock` — 防缓存击穿**

`lock=True` 时，当缓存 miss 且有多个并发请求同时到达时，只有第一个请求会真正调用函数，其余请求等待并复用第一个请求的结果，避免"击穿"。

- **内存后端**：使用进程级别的互斥锁
- **Redis 后端**：使用 Redis `SET NX EX` 分布式锁，跨进程/跨节点生效

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 高并发热点数据，开锁防击穿
@cache.cache(ttl=60, lock=True)
def get_hot_ranking():
    return db.query_heavy()

# 自定义锁超时（避免函数执行过慢时锁过早释放）
@cache.cache(ttl=60, lock=True, lock_ttl=30)
def slow_query(key):
    return db.expensive_query(key)
```

> `lock_ttl` 默认等于 `ttl`。若函数执行时间可能超过 `ttl`，建议单独设置 `lock_ttl` 为更合理的值（如函数最长执行时间的 2 倍）。

---

**`tags` — 标签批量失效**

给缓存打标签，方便按业务维度批量删除一组缓存，无需记录每个具体的 key。

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.cache(ttl=300, tags=("user", "user_profile"))
def get_user_profile(user_id):
    ...

@cache.cache(ttl=300, tags=("user",))
def get_user_orders(user_id):
    ...

# 用户数据有更新时，一次性清除所有打了 "user" 标签的缓存
cache.delete_tags_sync("user")
# 或异步
await cache.delete_tags("user")
```

---

**`prefix` — key 前缀**

用于在同一后端内进一步区分不同模块/版本的缓存，与 `setup(prefix=...)` 叠加：

```python
from nb_cache import Cache

# setup 全局前缀 "prod"，装饰器额外前缀 "v2"
# 最终 key 形如: "prod:v2:mymodule:get_user:user_id=1"
cache = Cache().setup("redis://localhost:6379/0", prefix="prod")

@cache.cache(ttl=60, prefix="v2")
def get_user(user_id):
    ...
```

---

**`serializer` — 序列化器**

覆盖全局序列化配置，对单个函数使用不同的序列化策略：

```python
from nb_cache import Cache, Serializer, JsonSerializer, GzipCompressor

cache = Cache().setup("mem://")

# 该函数专用 JSON + gzip 序列化（适合大响应体压缩存储）
json_gz = Serializer(serializer=JsonSerializer(), compressor=GzipCompressor())

@cache.cache(ttl=3600, serializer=json_gz)
def get_large_report(report_id):
    return generate_report(report_id)
```

### 失败回退 `failover`

异常时返回缓存的旧值：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.failover(ttl=3600, exceptions=(ConnectionError, TimeoutError))
def get_remote_data(key):
    return remote_api.call(key)
```

### 提前刷新 `early`

剩余 TTL 低于 `early_ttl` 时在后台提前刷新，防止缓存雪崩：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.early(ttl=60, early_ttl=10)
def get_data(key):
    return query(key)
```

### 软过期 `soft`

`soft_ttl` 到期后后台刷新并立刻返回旧值，不阻塞请求：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.soft(ttl=120, soft_ttl=60)
def get_data(key):
    return query(key)
```

### 命中次数缓存 `hit`

N 次命中后自动失效，`update_after` 命中后提前后台刷新：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.hit(ttl=3600, cache_hits=100, update_after=50)
def get_data(key):
    return query(key)
```

### 加锁装饰器 `locked`

保证同一时间只有一个调用在执行：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.locked(ttl=30)
def critical_operation(resource_id):
    ...
```

### 熔断器 `circuit_breaker`

错误率超标时熔断，保护下游服务：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.circuit_breaker(errors_rate=0.5, period=60, ttl=30)
def unstable_service(key):
    return call_service(key)
```

### 限流 `rate_limit`

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 固定窗口限流（60秒内最多 100 次）
@cache.rate_limit(limit=100, period=60)
def api_endpoint(user_id):
    ...

# 滑动窗口限流（更平滑）
@cache.slice_rate_limit(limit=100, period=60)
def api_endpoint(user_id):
    ...
```

### 迭代器缓存 `iterator`

缓存生成器/异步生成器的全部结果：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.iterator(ttl=60)
def get_items():
    for item in query_all():
        yield item
```

## 缓存 Key 定制

### 简单模板（字符串占位符）

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 单参数
@cache.cache(ttl=60, key="{user_id}")
def get_user(user_id):
    ...

# 多参数组合
@cache.cache(ttl=60, key="order:{user_id}:{status}")
def get_orders(user_id, status):
    ...
```

### 点号访问对象/字典属性

当参数是 dict 或对象时，用 `{param.attr}` 取其中的字段：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.cache(ttl=60, key="user:{user.id}:{user.name}")
def get_user(user):
    ...

# 调用时 user={"id": 1, "name": "Alice"}
# 生成 key → "user:1:Alice"
```

### 格式修饰符

| 修饰符 | 作用 | 示例 |
|---|---|---|
| `:hash` | 取 md5 前8位，适合复杂对象/长字符串 | `{filters:hash}` |
| `:lower` | 转小写，适合大小写不敏感的场景 | `{keyword:lower}` |

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# dict 参数 hash 化，避免 key 过长
@cache.cache(ttl=60, key="search:{keyword:lower}:{filters:hash}")
def search(keyword, filters):
    ...
```

### 自定义函数生成 key

当逻辑复杂无法用模板表达时，传入一个可调用对象：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

def build_key(user, action):
    # 接收和被装饰函数相同的参数
    return "perm:{}:{}:{}".format(user['org_id'], user['id'], action)

@cache.cache(ttl=300, key=build_key)
def check_permission(user, action):
    return db.query_permission(user['id'], action)
```

### key_include_func 参数说明

默认情况下，`nb_cache` 会把 **模块路径 + 函数名** 自动拼入 cache key，以确保不同模块的同名函数不会冲突：

```
# 默认生成的 key（含函数信息）
testp2:myapp.services:get_user:user_id:42
```

如果你已经通过 `key=` 参数自己指定了业务 key 模板，这段模块+函数前缀往往是多余的噪音。
设置 `key_include_func=False` 后，key 只保留业务部分：

```
# key_include_func=False 后生成的 key
testp2:user:42
```

#### 设置级别

`key_include_func` 支持两个层级，**装饰器上的值优先于 `setup()` 的默认值**。

**1. `setup()` 级别 —— 影响该实例下所有装饰器**

```python
from nb_cache import Cache

cache = Cache().setup("redis://localhost:6379/0", prefix="myapp", key_include_func=False)

@cache.cache(ttl=300, key="user:{user_id}")
def get_user(user_id):
    return db.query(user_id)
# final_key → myapp:user:42

@cache.cache(ttl=60, key="order:{order_id}")
def get_order(order_id):
    return db.query_order(order_id)
# final_key → myapp:order:100
```

**2. 装饰器级别 —— 覆盖 `setup()` 的默认值，只影响当前函数**

```python
cache = Cache().setup("redis://localhost:6379/0", prefix="myapp")
# 默认 key_include_func=True

@cache.cache(ttl=300, key="user:{user_id}")
def get_user(user_id):
    ...
# final_key → myapp:mymodule:get_user:user:{user_id} → myapp:mymodule:get_user:user:42

@cache.cache(ttl=60, key="order:{order_id}", key_include_func=False)
def get_order(order_id):
    ...
# final_key → myapp:order:100  （单独关闭，不含函数名）
```

#### 不指定 key= 时的行为

当不传 `key=` 参数，`nb_cache` 会根据函数签名自动生成 key。
此时 `key_include_func=False` 意味着 key 只由参数值组成，**极易碰撞**，不推荐在此场景下使用：

```python
# 不推荐：不指定 key= 且 key_include_func=False
@cache.cache(ttl=60, key_include_func=False)
def get_user(user_id):
    ...
# final_key → myapp:user_id=42   ← 与其他相同签名函数会冲突
```

#### 如何预览生成的 key（不调用函数）

```python
from nb_cache.key import get_cache_key, get_cache_key_template

# 方式1：从已装饰函数取模板（推荐）
template = get_user._cache_key_template
logic_key = get_cache_key(get_user, template, (42,), {})
final_key = cache._backend._make_key(logic_key)
print(final_key)  # myapp:user:42

# 方式2：直接用工具函数生成（不需要先装饰）
tpl = get_cache_key_template(get_user, key="user:{user_id}", key_include_func=False)
key = get_cache_key(get_user, tpl, (42,), {})
print(key)  # user:42
```

---

## 锁（上下文管理器）

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 同步锁
with cache.lock("resource_key", ttl=10):
    do_critical_work()

# 异步锁
async with cache.alock("resource_key", ttl=10):
    await do_critical_work()
```

## 标签系统

按标签批量失效缓存：

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

@cache.cache(ttl=60, tags=("users",))
def get_user(user_id):
    ...

@cache.cache(ttl=60, tags=("users", "profiles"))
def get_profile(user_id):
    ...

# 同步：按标签清除
cache.delete_tags_sync("users")

# 异步
await cache.delete_tags("users")
```

## 事务

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 同步事务（自动提交，异常自动回滚）
with cache.transaction() as tx:
    tx.set("key1", "val1", ttl=60)
    tx.set("key2", "val2", ttl=60)

# 异步事务
async with cache.transaction() as tx:
    tx.set("key1", "val1")
    tx.set("key2", "val2")
```

## 直接操作缓存

```python
from nb_cache import Cache

cache = Cache().setup("mem://")

# 同步
cache.set_sync("key", "value", ttl=60)
val = cache.get_sync("key")
cache.delete_sync("key")
cache.exists_sync("key")
cache.incr_sync("counter")

# 异步
await cache.set("key", "value", ttl=60)
val = await cache.get("key")
await cache.delete("key")
```

## TTL 格式

```python
from nb_cache import Cache
from datetime import timedelta

cache = Cache().setup("mem://")

@cache.cache(ttl=60)               # 秒数
@cache.cache(ttl=1.5)              # 小数秒
@cache.cache(ttl="30m")            # 30分钟
@cache.cache(ttl="1h")             # 1小时
@cache.cache(ttl="1d12h30m")       # 1天12小时30分钟
@cache.cache(ttl=timedelta(hours=1))  # timedelta
```

## 序列化

默认使用 pickle，支持切换 JSON：

```python
from nb_cache import Cache, JsonSerializer, Serializer

cache = Cache().setup("mem://")

json_ser = Serializer(serializer=JsonSerializer())

@cache.cache(ttl=60, serializer=json_ser)
def get_data():
    return {"name": "test"}
```

## 常见问题解答

### 问题1：如何查看缓存最终生成的key是什么？ 


#### 方式一：通过日志查看
```
因为nb_cache 已经在 nb_cache.cache 日志命名空间，用debug 日志级别打印了最终生成的key。

所以你可以通过nb_log来查看：
 nb_log.get_logger('nb_cache.cache')

也可以通过 原生logging 来查看:
logger = logging.getLogger("nb_cache.cache")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
```

日志例子：
```
2026-02-28 18:46:01 - nb_cache.cache - "D:\codes\nb_cache\nb_cache\decorators\cache.py:61" - async_wrapper - DEBUG - [nb_cache] func=__main__:aio_fun  final_key=testp2:__main__:aio_fun:aiof:3_4  ttl=700.0
```

#### 方式二：不调用函数，直接预览 cache key

```python
# -*- coding: utf-8 -*-
"""nb_cache key 生成 Demo"""
import sys
import asyncio
from nb_cache import Cache
from nb_cache.key import get_cache_key, get_cache_key_template
import nb_log

nb_log.get_logger("nb_cache.cache")

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

cache = Cache()
cache.setup("redis://", prefix="testp2")


@cache.cache(ttl=700,key='sf:{a}_{b}')
def simple_func(a, b):
    return a + b

print(simple_func(1, 2))

# --- 不调用函数，直接预览 cache key ---
# 方式1：从装饰后的函数取模板属性（推荐）
template = simple_func._cache_key_template
logic_key = get_cache_key(simple_func, template, (1, 2), {})
final_key = cache._backend._make_key(logic_key)
print("logic_key:", logic_key)   # 不含 prefix
print("final_key:", final_key)   # 含 prefix，与 Redis 中一致

# 方式2：用工具函数直接生成，不需要先装饰
def raw_func(a, b):
    return a + b
tpl = get_cache_key_template(raw_func, key='sf:{a}_{b}')
key2 = get_cache_key(raw_func, tpl, (1, 2), {})
print("key2 (无prefix):", key2)
```

## 许可证

MIT License

`````

--- **end of file: README.md** (project: nb_cache) --- 

---


--- **start of file: pyproject.toml** (project: nb_cache) --- 

`````text
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "nb_cache"
version = "0.3"
description = "`nb_cache` 不仅是一个基础的缓存装饰器，它在彻底抹平 Python 同步与异步代码差异的同时，开箱即用地提供了内存/Redis双层缓存、防击穿、防雪崩、限流与熔断等企业级高可用特性。"
readme = "README.md"
# license = {text = "MIT"}
requires-python = ">=3.6"
authors = [
    {name = "ydf0509"},
]
keywords = ["cache", "redis", "memory", "async", "decorator", "lock"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries :: Python Modules",
    # "Topic :: System :: Caching",
]

[project.optional-dependencies]
redis = ["redis>=3.0"]
speedup = ["xxhash", "hiredis"]
all = ["redis>=3.0", "xxhash", "hiredis"]

[project.urls]
Homepage = "https://github.com/ydf0509/nb_cache"
Repository = "https://github.com/ydf0509/nb_cache"

[tool.setuptools.packages.find]
include = ["nb_cache*"]
exclude = ["tests*", "cashews*"]

[tool.setuptools]
license-files = []



# python -m build && twine upload dist/*
`````

--- **end of file: pyproject.toml** (project: nb_cache) --- 

---

# markdown content namespace: nb_cache codes 


## nb_cache File Tree (relative dir: `nb_cache`)


`````

└── nb_cache
    ├── __init__.py
    ├── _compat.py
    ├── backends
    │   ├── __init__.py
    │   ├── base.py
    │   ├── dual.py
    │   ├── memory.py
    │   └── redis.py
    ├── condition.py
    ├── decorators
    │   ├── __init__.py
    │   ├── bloom.py
    │   ├── cache.py
    │   ├── circuit_breaker.py
    │   ├── early.py
    │   ├── failover.py
    │   ├── hit.py
    │   ├── iterator.py
    │   ├── locked.py
    │   ├── rate_limit.py
    │   └── soft.py
    ├── exceptions.py
    ├── helpers.py
    ├── key.py
    ├── middleware.py
    ├── serialize.py
    ├── tags.py
    ├── transaction.py
    ├── ttl.py
    └── wrapper.py

`````

---


## nb_cache (relative dir: `nb_cache`)  Included Files (total: 28 files)


- `nb_cache/condition.py`

- `nb_cache/exceptions.py`

- `nb_cache/helpers.py`

- `nb_cache/key.py`

- `nb_cache/middleware.py`

- `nb_cache/serialize.py`

- `nb_cache/tags.py`

- `nb_cache/transaction.py`

- `nb_cache/ttl.py`

- `nb_cache/wrapper.py`

- `nb_cache/_compat.py`

- `nb_cache/__init__.py`

- `nb_cache/backends/base.py`

- `nb_cache/backends/dual.py`

- `nb_cache/backends/memory.py`

- `nb_cache/backends/redis.py`

- `nb_cache/backends/__init__.py`

- `nb_cache/decorators/bloom.py`

- `nb_cache/decorators/cache.py`

- `nb_cache/decorators/circuit_breaker.py`

- `nb_cache/decorators/early.py`

- `nb_cache/decorators/failover.py`

- `nb_cache/decorators/hit.py`

- `nb_cache/decorators/iterator.py`

- `nb_cache/decorators/locked.py`

- `nb_cache/decorators/rate_limit.py`

- `nb_cache/decorators/soft.py`

- `nb_cache/decorators/__init__.py`


---


--- **start of file: nb_cache/condition.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Cache condition utilities.

Conditions determine whether a function result should be cached.
"""

_SENTINEL = object()


def NOT_NONE(result):
    """Cache only if the result is not None."""
    return result is not None


def always_true(result):
    """Always cache the result."""
    return True


def with_exceptions(*exceptions):
    """Create a condition that caches results and specified exceptions.

    Usage::

        @cache(ttl=60, condition=with_exceptions(ValueError, KeyError))
        def my_func():
            ...
    """
    if not exceptions:
        exceptions = (Exception,)

    def _condition(result):
        return True

    _condition._cache_exceptions = exceptions
    return _condition


def only_exceptions(*exceptions):
    """Create a condition that only caches when an exception is raised.

    Usage::

        @cache(ttl=60, condition=only_exceptions(TimeoutError))
        def my_func():
            ...
    """
    if not exceptions:
        exceptions = (Exception,)

    def _condition(result):
        return False

    _condition._cache_exceptions = exceptions
    _condition._only_exceptions = True
    return _condition


def get_cache_condition(condition):
    """Normalize a condition argument into a callable."""
    if condition is None:
        return NOT_NONE
    if callable(condition):
        return condition
    raise TypeError("condition must be callable or None, got {!r}".format(type(condition)))

`````

--- **end of file: nb_cache/condition.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/exceptions.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Exception hierarchy for nb_cache."""


class CacheError(Exception):
    """Base exception for all cache errors."""
    pass


class BackendNotInitializedError(CacheError):
    """Raised when backend is not initialized."""
    pass


class CacheBackendInteractionError(CacheError):
    """Raised when a backend interaction fails."""
    pass


class LockError(CacheError):
    """Raised when a lock cannot be acquired."""
    pass


class LockedError(LockError):
    """Raised when a resource is already locked."""
    pass


class CircuitBreakerOpen(CacheError):
    """Raised when the circuit breaker is open."""
    pass


class RateLimitError(CacheError):
    """Raised when a rate limit is exceeded."""
    pass


class SerializationError(CacheError):
    """Raised when serialization/deserialization fails."""
    pass


class TagError(CacheError):
    """Raised on tag-related errors."""
    pass

`````

--- **end of file: nb_cache/exceptions.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/helpers.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Helper functions and utilities."""
from nb_cache.middleware import PrefixMiddleware, MemoryLimitMiddleware


def add_prefix(prefix):
    """Create a PrefixMiddleware that adds prefix to all keys."""
    return PrefixMiddleware(prefix)


def memory_limit(max_keys=10000):
    """Create a MemoryLimitMiddleware."""
    return MemoryLimitMiddleware(max_keys=max_keys)


def invalidate_further():
    """Context manager / marker for cascading invalidation.

    When used, invalidation triggered inside this context will
    also invalidate dependent caches.
    """
    import contextlib

    @contextlib.contextmanager
    def _ctx():
        yield

    return _ctx()


def noself(func):
    """Decorator that strips 'self' from cache key generation.

    Useful for methods where caching should be shared across instances.
    """
    func._noself = True
    return func

`````

--- **end of file: nb_cache/helpers.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/key.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Cache key generation and template utilities."""
import hashlib
import inspect
import re

# Matches {param}, {param:fmt}, {param.attr}, {param.attr:fmt}
_TEMPLATE_PARAM_RE = re.compile(r'\{([\w.]+)(?::(\w+))?\}')


def get_func_name(func):
    """Get a stable, qualified name for a function."""
    module = getattr(func, '__module__', '') or ''
    qualname = getattr(func, '__qualname__', '') or getattr(func, '__name__', '')
    return "{}:{}".format(module, qualname)


def get_cache_key(func, key_template, args, kwargs):
    """Build a concrete cache key from a function call and optional template.

    key_template can be:
      - None: auto-generate from function name + bound arguments
      - str: render as a template, supporting {param}, {param.attr}, {param:hash/lower}
      - callable: call with the same (args, kwargs) and return the key string
    """
    if key_template is None:
        key = _auto_key(func, args, kwargs)
    elif callable(key_template):
        bound = _bind_arguments(func, args, kwargs)
        positional = list(bound.values())
        key = str(key_template(*positional))
    else:
        key = _render_template(func, key_template, args, kwargs)

    return key


def get_cache_key_template(func, key=None, prefix="", key_include_func=True):
    """Build a key template (string or callable) for a function.

    When key is a callable, it is stored as-is and will be called at cache time.
    When key is a string template, it is prefixed with func_name (if include_func_name=True).
    When key is None, auto-generate a template from the function signature.

    Args:
        func: The decorated function.
        key: Key template string or callable. None means auto-generate.
        prefix: Key prefix string (from decorator or setup).
        key_include_func: If False, the module path and function name are NOT
            included in the generated key. Useful when you want a short,
            purely business-logic key (e.g. ``aiof:3_4`` instead of
            ``__main__:aio_fun:aiof:3_4``).
    """
    func_name = get_func_name(func)
    if key is not None:
        if callable(key):
            return key
        if key_include_func:
            if prefix:
                return "{}:{}:{}".format(prefix, func_name, key)
            return "{}:{}".format(func_name, key)
        else:
            if prefix:
                return "{}:{}".format(prefix, key)
            return key

    sig = inspect.signature(func)
    parts = []
    for name, param in sig.parameters.items():
        if name in ('self', 'cls'):
            continue
        parts.append("{{{name}}}".format(name=name))

    template = ":".join(parts) if parts else ""
    if key_include_func:
        if prefix:
            return "{}:{}:{}".format(prefix, func_name, template)
        return "{}:{}".format(func_name, template)
    else:
        if prefix:
            return "{}:{}".format(prefix, template) if template else prefix
        return template


def _resolve_attr(val, attr_path):
    """Resolve a dotted attribute path on a value.

    Supports both object attributes and dict key access.
    e.g. attr_path="id" on {"id": 1} returns 1
         attr_path="address.city" on obj.address.city returns city value
    """
    for part in attr_path.split('.'):
        if isinstance(val, dict):
            val = val.get(part, '')
        else:
            val = getattr(val, part, '')
    return val


def _render_template(func, template, args, kwargs):
    """Render a key template string with actual argument values.

    Supports:
      {param}           — plain value
      {param.attr}      — attribute/dict-key access
      {param:hash}      — md5 hash of value
      {param:lower}     — lowercase string
      {param.attr:hash} — hash of nested attribute
    """
    bound = _bind_arguments(func, args, kwargs)

    def _replacer(m):
        expr = m.group(1)   # e.g. "user", "user.id", "filters"
        fmt = m.group(2)    # e.g. "hash", "lower", or None

        parts = expr.split('.', 1)
        param_name = parts[0]
        attr_path = parts[1] if len(parts) > 1 else None

        val = bound.get(param_name, '')
        if attr_path:
            val = _resolve_attr(val, attr_path)

        if fmt == 'hash':
            return _hash_value(val)
        if fmt == 'lower':
            return str(val).lower()
        return str(val)

    return _TEMPLATE_PARAM_RE.sub(_replacer, template)


def _auto_key(func, args, kwargs):
    """Auto-generate a cache key from function name + arguments."""
    func_name = get_func_name(func)
    bound = _bind_arguments(func, args, kwargs)
    parts = [func_name]
    for name, val in sorted(bound.items()):
        if name == 'self' or name == 'cls':
            continue
        parts.append("{}={}".format(name, _safe_str(val)))
    return ":".join(parts)


def _bind_arguments(func, args, kwargs):
    """Bind positional and keyword arguments to parameter names."""
    try:
        sig = inspect.signature(func)
        ba = sig.bind(*args, **kwargs)
        ba.apply_defaults()
        return dict(ba.arguments)
    except (ValueError, TypeError):
        result = {}
        for i, v in enumerate(args):
            result["arg{}".format(i)] = v
        result.update(kwargs)
        return result


def _hash_value(val):
    return hashlib.md5(str(val).encode()).hexdigest()[:8]


def _safe_str(val):
    """Convert a value to a string safe for use in a cache key."""
    if isinstance(val, (list, tuple, set, frozenset)):
        return _hash_value(val)
    if isinstance(val, dict):
        return _hash_value(sorted(val.items()))
    return str(val)

`````

--- **end of file: nb_cache/key.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/middleware.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Middleware system for cache operations.

Middlewares wrap backend operations (get, set, delete, etc.)
and can modify keys, values, or behavior.
"""


class Middleware(object):
    """Base middleware class. Subclass and override methods."""

    def on_get(self, key, backend):
        """Called before get. Return modified key or None to skip."""
        return key

    def on_get_result(self, key, result, backend):
        """Called after get. Return modified result."""
        return result

    def on_set(self, key, value, ttl, backend):
        """Called before set. Return (key, value, ttl) or None to skip."""
        return key, value, ttl

    def on_delete(self, key, backend):
        """Called before delete. Return key or None to skip."""
        return key


class PrefixMiddleware(Middleware):
    """Adds a prefix to all cache keys."""

    def __init__(self, prefix):
        self._prefix = prefix

    def _add_prefix(self, key):
        return "{}:{}".format(self._prefix, key)

    def on_get(self, key, backend):
        return self._add_prefix(key)

    def on_set(self, key, value, ttl, backend):
        return self._add_prefix(key), value, ttl

    def on_delete(self, key, backend):
        return self._add_prefix(key)


class MemoryLimitMiddleware(Middleware):
    """Limits total memory usage of the cache.

    Only works with memory backends that support get_keys_count_sync.
    """

    def __init__(self, max_keys=10000):
        self._max_keys = max_keys

    def on_set(self, key, value, ttl, backend):
        try:
            count = backend.get_keys_count_sync()
            if count >= self._max_keys:
                return None
        except (NotImplementedError, AttributeError):
            pass
        return key, value, ttl

`````

--- **end of file: nb_cache/middleware.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/serialize.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Serialization, signing, and compression pipeline for cache values."""
import hashlib
import pickle
import json
import zlib
import gzip
import io

_SENTINEL = object()


class PickleSerializer(object):
    """Standard pickle serializer."""

    def dumps(self, obj):
        return pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)

    def loads(self, data):
        return pickle.loads(data)


class JsonSerializer(object):
    """JSON serializer for simple types."""

    def dumps(self, obj):
        return json.dumps(obj, ensure_ascii=False, default=str).encode('utf-8')

    def loads(self, data):
        if isinstance(data, (bytes, bytearray)):
            data = data.decode('utf-8')
        return json.loads(data)


class NullCompressor(object):
    def compress(self, data):
        return data

    def decompress(self, data):
        return data


class GzipCompressor(object):
    def __init__(self, level=6):
        self._level = level

    def compress(self, data):
        return gzip.compress(data, compresslevel=self._level)

    def decompress(self, data):
        return gzip.decompress(data)


class ZlibCompressor(object):
    def __init__(self, level=6):
        self._level = level

    def compress(self, data):
        return zlib.compress(data, self._level)

    def decompress(self, data):
        return zlib.decompress(data)


class HashSigner(object):
    """Signs serialized data with a hash to detect tampering."""

    def __init__(self, secret="", digestmod="md5"):
        self._secret = secret.encode('utf-8') if isinstance(secret, str) else secret
        self._digestmod = digestmod

    def sign(self, data):
        if not self._secret:
            return data
        import hmac
        sig = hmac.new(self._secret, data, self._digestmod).digest()
        return sig + data

    def unsign(self, data):
        if not self._secret:
            return data
        import hmac
        h = hmac.new(self._secret, b'', self._digestmod)
        sig_len = h.digest_size
        if len(data) < sig_len:
            return None
        sig = data[:sig_len]
        payload = data[sig_len:]
        expected = hmac.new(self._secret, payload, self._digestmod).digest()
        if not hmac.compare_digest(sig, expected):
            return None
        return payload


class Serializer(object):
    """Unified serialization pipeline: serialize -> sign -> compress."""

    def __init__(self, serializer=None, compressor=None, signer=None):
        self._serializer = serializer or PickleSerializer()
        self._compressor = compressor or NullCompressor()
        self._signer = signer or HashSigner()

    def encode(self, obj):
        data = self._serializer.dumps(obj)
        data = self._signer.sign(data)
        data = self._compressor.compress(data)
        return data

    def decode(self, data):
        if data is None:
            return _SENTINEL
        try:
            data = self._compressor.decompress(data)
            data = self._signer.unsign(data)
            if data is None:
                return _SENTINEL
            return self._serializer.loads(data)
        except Exception:
            return _SENTINEL

    @property
    def SENTINEL(self):
        return _SENTINEL


default_serializer = Serializer()

`````

--- **end of file: nb_cache/serialize.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/tags.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Tag-based cache invalidation system.

Tags allow grouping cache keys so they can be invalidated together.
"""
import threading


class TagRegistry(object):
    """Registry mapping tags to cache keys."""

    def __init__(self):
        self._tags = {}  # tag -> set of keys
        self._lock = threading.RLock()

    def register(self, key, tags):
        if not tags:
            return
        with self._lock:
            for tag in tags:
                if tag not in self._tags:
                    self._tags[tag] = set()
                self._tags[tag].add(key)

    def get_keys(self, tag):
        with self._lock:
            return set(self._tags.get(tag, set()))

    def get_all_keys(self, *tags):
        keys = set()
        for tag in tags:
            keys.update(self.get_keys(tag))
        return keys

    def remove_key(self, key):
        with self._lock:
            for tag in list(self._tags.keys()):
                self._tags[tag].discard(key)
                if not self._tags[tag]:
                    del self._tags[tag]

    def remove_tag(self, tag):
        with self._lock:
            self._tags.pop(tag, None)

    def clear(self):
        with self._lock:
            self._tags.clear()


_default_tag_registry = TagRegistry()


def get_default_tag_registry():
    return _default_tag_registry

`````

--- **end of file: nb_cache/tags.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/transaction.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Transaction support for cache operations.

Provides FAST, LOCKED, and SERIALIZABLE transaction modes.
"""
import enum
import threading


class TransactionMode(enum.Enum):
    FAST = "fast"
    LOCKED = "locked"
    SERIALIZABLE = "serializable"


class Transaction(object):
    """Cache transaction that buffers operations and commits/rollbacks.

    Usage::

        with cache.transaction() as tx:
            tx.set("key1", "val1")
            tx.set("key2", "val2")
        # auto-commits on exit

        # or with explicit rollback:
        tx = cache.transaction()
        tx.begin()
        tx.set("key1", "val1")
        tx.rollback()
    """

    def __init__(self, backend, mode=TransactionMode.FAST):
        self._backend = backend
        self._mode = mode
        self._buffer = []
        self._lock = threading.RLock() if mode != TransactionMode.FAST else None
        self._active = False

    def begin(self):
        if self._lock:
            self._lock.acquire()
        self._active = True
        self._buffer = []

    def set(self, key, value, ttl=None):
        self._buffer.append(('set', key, value, ttl))

    def delete(self, key):
        self._buffer.append(('delete', key, None, None))

    def commit_sync(self):
        try:
            for op, key, value, ttl in self._buffer:
                if op == 'set':
                    self._backend.set_sync(key, value, ttl=ttl)
                elif op == 'delete':
                    self._backend.delete_sync(key)
        finally:
            self._buffer = []
            self._active = False
            if self._lock:
                try:
                    self._lock.release()
                except RuntimeError:
                    pass

    async def commit(self):
        try:
            for op, key, value, ttl in self._buffer:
                if op == 'set':
                    await self._backend.set(key, value, ttl=ttl)
                elif op == 'delete':
                    await self._backend.delete(key)
        finally:
            self._buffer = []
            self._active = False
            if self._lock:
                try:
                    self._lock.release()
                except RuntimeError:
                    pass

    def rollback(self):
        self._buffer = []
        self._active = False
        if self._lock:
            try:
                self._lock.release()
            except RuntimeError:
                pass

    def __enter__(self):
        self.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            self.commit_sync()
        return False

    async def __aenter__(self):
        self.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
        else:
            await self.commit()
        return False

`````

--- **end of file: nb_cache/transaction.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/ttl.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""TTL (time-to-live) parsing and utilities.

Supports:
  - int/float (seconds)
  - datetime.timedelta
  - str like "1h", "30m", "1h30m", "2d", "1d12h30m10s"
  - callable that returns any of the above
"""
import re
from datetime import timedelta

_TTL_PATTERN = re.compile(
    r'(?:(\d+)\s*d(?:ays?)?)?'
    r'\s*(?:(\d+)\s*h(?:ours?)?)?'
    r'\s*(?:(\d+)\s*m(?:in(?:utes?)?)?)?'
    r'\s*(?:(\d+)\s*s(?:ec(?:onds?)?)?)?',
    re.IGNORECASE,
)

_SENTINEL = object()


def ttl_to_seconds(ttl):
    """Convert various TTL representations to seconds (float).

    Returns None if ttl is None or 0.
    """
    if ttl is None:
        return None

    if callable(ttl) and not isinstance(ttl, (int, float)):
        ttl = ttl()

    if isinstance(ttl, (int, float)):
        return float(ttl) if ttl > 0 else None

    if isinstance(ttl, timedelta):
        return ttl.total_seconds() or None

    if isinstance(ttl, str):
        return _parse_ttl_string(ttl)

    raise TypeError("Unsupported TTL type: {!r}".format(type(ttl)))


def _parse_ttl_string(s):
    s = s.strip()
    if not s:
        return None

    try:
        return float(s)
    except (ValueError, TypeError):
        pass

    m = _TTL_PATTERN.fullmatch(s)
    if m is None:
        raise ValueError("Invalid TTL string: {!r}".format(s))

    days = int(m.group(1) or 0)
    hours = int(m.group(2) or 0)
    minutes = int(m.group(3) or 0)
    seconds = int(m.group(4) or 0)

    total = days * 86400 + hours * 3600 + minutes * 60 + seconds
    return float(total) if total > 0 else None

`````

--- **end of file: nb_cache/ttl.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/wrapper.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Cache wrapper — the main entry point for nb_cache.

Integrates backends, decorators, commands, tags, transactions,
and middleware into a single unified API.
"""
import contextlib
import functools
import threading

from nb_cache._compat import is_coroutine_function
from nb_cache.backends.memory import MemoryBackend
from nb_cache.condition import NOT_NONE, get_cache_condition, with_exceptions, only_exceptions
from nb_cache.exceptions import BackendNotInitializedError
from nb_cache.key import get_cache_key_template
from nb_cache.serialize import (
    Serializer, PickleSerializer, JsonSerializer,
    GzipCompressor, ZlibCompressor, NullCompressor, HashSigner,
    default_serializer,
)
from nb_cache.tags import TagRegistry, get_default_tag_registry
from nb_cache.transaction import Transaction, TransactionMode
from nb_cache.ttl import ttl_to_seconds

_default_backend = [None]
_default_backend_lock = threading.Lock()


def _get_default_backend():
    """Get the global default backend, auto-initializing MemoryBackend if never set."""
    if _default_backend[0] is None:
        with _default_backend_lock:
            if _default_backend[0] is None:
                be = MemoryBackend()
                be.init_sync()
                _default_backend[0] = be
    return _default_backend[0]


def _set_default_backend(backend):
    _default_backend[0] = backend


_BACKEND_REGISTRY = {
    'mem': 'nb_cache.backends.memory:MemoryBackend',
    'memory': 'nb_cache.backends.memory:MemoryBackend',
    'redis': 'nb_cache.backends.redis:RedisBackend',
    'rediss': 'nb_cache.backends.redis:RedisBackend',
    'dual': 'nb_cache.backends.dual:DualBackend',
}


def _resolve_backend_class(scheme):
    path = _BACKEND_REGISTRY.get(scheme)
    if path is None:
        raise ValueError("Unknown backend scheme: {!r}".format(scheme))
    module_path, cls_name = path.rsplit(':', 1)
    import importlib
    module = importlib.import_module(module_path)
    return getattr(module, cls_name)


def _parse_settings_url(url):
    """Parse a settings URL like 'mem://', 'redis://host:port/db?opt=val'."""
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()

    kwargs = {}
    if parsed.hostname:
        kwargs['host'] = parsed.hostname
    if parsed.port:
        kwargs['port'] = parsed.port
    if parsed.password:
        kwargs['password'] = parsed.password
    if parsed.path and parsed.path.strip('/'):
        try:
            kwargs['db'] = int(parsed.path.strip('/'))
        except ValueError:
            pass

    qs = parse_qs(parsed.query)
    for k, v in qs.items():
        val = v[0] if len(v) == 1 else v
        if val == 'true':
            val = True
        elif val == 'false':
            val = False
        else:
            try:
                val = int(val)
            except (ValueError, TypeError):
                try:
                    val = float(val)
                except (ValueError, TypeError):
                    pass
        kwargs[k] = val

    if scheme in ('redis', 'rediss'):
        proto = 'rediss' if scheme == 'rediss' else 'redis'
        redis_url = "{}://".format(proto)
        if parsed.password:
            redis_url += ":{}@".format(parsed.password)
        redis_url += parsed.hostname or 'localhost'
        if parsed.port:
            redis_url += ":{}".format(parsed.port)
        if parsed.path:
            redis_url += parsed.path
        kwargs['url'] = redis_url

    return scheme, kwargs


def register_backend(scheme, backend_path):
    """Register a custom backend class.

    Args:
        scheme: URL scheme (e.g. 'custom').
        backend_path: Dotted path like 'mymodule:MyBackend'.
    """
    _BACKEND_REGISTRY[scheme] = backend_path


class Cache(object):
    """Main cache interface. Integrates backend, decorators, tags, etc.

    Usage::

        from nb_cache import cache

        # Setup with URL
        cache.setup("mem://")
        cache.setup("redis://localhost:6379/0")

        # Direct operations
        cache.set_sync("key", "value", ttl=60)
        val = cache.get_sync("key")

        # As decorator
        @cache.cache(ttl=60)
        def get_user(user_id):
            return db.query(user_id)
    """

    def __init__(self):
        self._backend = None
        self._middlewares = []
        self._tag_registry = get_default_tag_registry()
        self._serializer = default_serializer
        self._is_setup = False
        self._key_include_func = True

    @property
    def is_setup(self):
        return self._is_setup

    @property
    def is_init(self):
        return self._backend is not None and self._backend.is_init

    # --- Setup ---

    def setup(self, settings_url, middlewares=None, prefix="", key_include_func=True, **kwargs):
        """Configure the cache backend from a URL.

        Args:
            settings_url: URL like 'mem://', 'redis://host:port/db'.
            middlewares: List of Middleware instances.
            prefix: Global key prefix.
            key_include_func: If False, the module path and function name are NOT
                included in auto-generated cache keys. Useful for short, business-logic-only
                keys. Default is True.
            **kwargs: Extra arguments passed to the backend.

        Supported URL schemes: mem://, redis://, rediss://, dual://
        """
        scheme, parsed_kwargs = _parse_settings_url(settings_url)
        parsed_kwargs.update(kwargs)

        secret = parsed_kwargs.pop('secret', '')
        digestmod = parsed_kwargs.pop('digestmod', 'md5')
        compress = parsed_kwargs.pop('compress_type', None)
        pickle_type = parsed_kwargs.pop('pickle_type', 'pickle')

        if prefix:
            parsed_kwargs['prefix'] = prefix

        cls = _resolve_backend_class(scheme)
        self._backend = cls(**parsed_kwargs)

        if middlewares:
            self._middlewares = list(middlewares)

        signer = HashSigner(secret=secret, digestmod=digestmod)
        if pickle_type == 'json':
            ser = JsonSerializer()
        else:
            ser = PickleSerializer()
        if compress == 'gzip':
            comp = GzipCompressor()
        elif compress == 'zlib':
            comp = ZlibCompressor()
        else:
            comp = NullCompressor()
        self._serializer = Serializer(serializer=ser, compressor=comp, signer=signer)

        self._key_include_func = key_include_func
        self._backend.init_sync()
        self._is_setup = True
        return self

    # --- Init / Close ---

    async def init(self):
        """Re-initialize the async client (only needed if you use setup() in a sync
        context but later need to swap to a freshly-created async event loop)."""
        if self._backend is None:
            raise BackendNotInitializedError("Call setup() first")
        await self._backend.init()

    def init_sync(self):
        """Explicitly re-initialize the backend. Usually not needed — setup() calls
        this automatically."""
        if self._backend is None:
            raise BackendNotInitializedError("Call setup() first")
        self._backend.init_sync()

    async def close(self):
        if self._backend:
            await self._backend.close()

    def close_sync(self):
        if self._backend:
            self._backend.close_sync()

    async def ping(self):
        return await self._backend.ping()

    def ping_sync(self):
        return self._backend.ping_sync()

    def _ensure_backend(self):
        if self._backend is None:
            self.setup("mem://")
            self.init_sync()

    # --- Direct cache operations (async) ---

    async def get(self, key):
        self._ensure_backend()
        return await self._backend.get(key)

    async def set(self, key, value, ttl=None):
        self._ensure_backend()
        await self._backend.set(key, value, ttl=ttl)

    async def delete(self, key):
        self._ensure_backend()
        self._tag_registry.remove_key(key)
        return await self._backend.delete(key)

    async def exists(self, key):
        self._ensure_backend()
        return await self._backend.exists(key)

    async def expire(self, key, ttl):
        self._ensure_backend()
        return await self._backend.expire(key, ttl)

    async def get_expire(self, key):
        self._ensure_backend()
        return await self._backend.get_expire(key)

    async def clear(self):
        self._ensure_backend()
        self._tag_registry.clear()
        await self._backend.clear()

    async def incr(self, key, amount=1):
        self._ensure_backend()
        return await self._backend.incr(key, amount)

    async def get_many(self, *keys):
        self._ensure_backend()
        return await self._backend.get_many(*keys)

    async def set_many(self, pairs, ttl=None):
        self._ensure_backend()
        await self._backend.set_many(pairs, ttl=ttl)

    async def delete_many(self, *keys):
        self._ensure_backend()
        for k in keys:
            self._tag_registry.remove_key(k)
        await self._backend.delete_many(*keys)

    async def delete_match(self, pattern):
        self._ensure_backend()
        await self._backend.delete_match(pattern)

    async def scan(self, pattern):
        self._ensure_backend()
        return await self._backend.scan(pattern)

    async def get_match(self, pattern):
        self._ensure_backend()
        return await self._backend.get_match(pattern)

    async def get_keys_count(self):
        self._ensure_backend()
        return await self._backend.get_keys_count()

    async def get_size(self):
        self._ensure_backend()
        return await self._backend.get_size()

    async def set_lock(self, key, ttl):
        self._ensure_backend()
        return await self._backend.set_lock(key, ttl)

    async def unlock(self, key):
        self._ensure_backend()
        return await self._backend.unlock(key)

    async def is_locked(self, key):
        self._ensure_backend()
        return await self._backend.is_locked(key)

    # --- Direct cache operations (sync) ---

    def get_sync(self, key):
        self._ensure_backend()
        return self._backend.get_sync(key)

    def set_sync(self, key, value, ttl=None):
        self._ensure_backend()
        self._backend.set_sync(key, value, ttl=ttl)

    def delete_sync(self, key):
        self._ensure_backend()
        self._tag_registry.remove_key(key)
        return self._backend.delete_sync(key)

    def exists_sync(self, key):
        self._ensure_backend()
        return self._backend.exists_sync(key)

    def expire_sync(self, key, ttl):
        self._ensure_backend()
        return self._backend.expire_sync(key, ttl)

    def get_expire_sync(self, key):
        self._ensure_backend()
        return self._backend.get_expire_sync(key)

    def clear_sync(self):
        self._ensure_backend()
        self._tag_registry.clear()
        self._backend.clear_sync()

    def incr_sync(self, key, amount=1):
        self._ensure_backend()
        return self._backend.incr_sync(key, amount)

    def get_many_sync(self, *keys):
        self._ensure_backend()
        return self._backend.get_many_sync(*keys)

    def set_many_sync(self, pairs, ttl=None):
        self._ensure_backend()
        self._backend.set_many_sync(pairs, ttl=ttl)

    def delete_many_sync(self, *keys):
        self._ensure_backend()
        for k in keys:
            self._tag_registry.remove_key(k)
        self._backend.delete_many_sync(*keys)

    def delete_match_sync(self, pattern):
        self._ensure_backend()
        self._backend.delete_match_sync(pattern)

    def scan_sync(self, pattern):
        self._ensure_backend()
        return self._backend.scan_sync(pattern)

    def get_match_sync(self, pattern):
        self._ensure_backend()
        return self._backend.get_match_sync(pattern)

    # --- Lock context managers ---

    @contextlib.contextmanager
    def lock(self, key, ttl=60):
        """Sync lock context manager.

        Usage::

            with cache.lock("resource", ttl=10):
                do_something()
        """
        self._ensure_backend()
        _ttl = ttl_to_seconds(ttl) or 60
        acquired = self._backend.set_lock_sync(key, _ttl)
        if not acquired:
            import time
            deadline = time.time() + _ttl
            while time.time() < deadline:
                time.sleep(0.1)
                acquired = self._backend.set_lock_sync(key, _ttl)
                if acquired:
                    break
            if not acquired:
                from nb_cache.exceptions import LockedError
                raise LockedError("Cannot acquire lock: {}".format(key))
        try:
            yield
        finally:
            self._backend.unlock_sync(key)

    @contextlib.asynccontextmanager
    async def alock(self, key, ttl=60):
        """Async lock context manager.

        Usage::

            async with cache.alock("resource", ttl=10):
                await do_something()
        """
        import asyncio
        self._ensure_backend()
        _ttl = ttl_to_seconds(ttl) or 60
        acquired = await self._backend.set_lock(key, _ttl)
        if not acquired:
            import time
            deadline = time.time() + _ttl
            while time.time() < deadline:
                await asyncio.sleep(0.1)
                acquired = await self._backend.set_lock(key, _ttl)
                if acquired:
                    break
            if not acquired:
                from nb_cache.exceptions import LockedError
                raise LockedError("Cannot acquire lock: {}".format(key))
        try:
            yield
        finally:
            await self._backend.unlock(key)

    # --- Tags ---

    def delete_tags_sync(self, *tags):
        """Delete all keys associated with the given tags (sync)."""
        keys = self._tag_registry.get_all_keys(*tags)
        for k in keys:
            self._backend.delete_sync(k)
        for tag in tags:
            self._tag_registry.remove_tag(tag)

    async def delete_tags(self, *tags):
        """Delete all keys associated with the given tags (async)."""
        keys = self._tag_registry.get_all_keys(*tags)
        for k in keys:
            await self._backend.delete(k)
        for tag in tags:
            self._tag_registry.remove_tag(tag)

    # --- Transactions ---

    def transaction(self, mode=TransactionMode.FAST):
        """Create a transaction (works as both sync and async context manager).

        Usage::

            with cache.transaction() as tx:
                tx.set("k1", "v1")
                tx.set("k2", "v2")

            async with cache.transaction() as tx:
                tx.set("k1", "v1")
        """
        self._ensure_backend()
        return Transaction(self._backend, mode=mode)

    # --- Decorator shortcuts ---

    def cache(self, ttl, key=None, condition=None, prefix="", lock=False,
              lock_ttl=None, tags=(), serializer=None, key_include_func:bool=None):
        from nb_cache.decorators.cache import cache as _cache
        _kif = self._key_include_func if key_include_func is None else key_include_func
        return _cache(ttl, key=key, condition=condition, prefix=prefix,
                      lock=lock, lock_ttl=lock_ttl, tags=tags,
                      backend=self._backend, serializer=serializer or self._serializer,
                      tag_registry=self._tag_registry if tags else None,
                      key_include_func=_kif)

    def failover(self, ttl, key=None, exceptions=None, condition=None,
                 prefix="fail", tags=(), serializer=None):
        from nb_cache.decorators.failover import failover as _failover
        return _failover(ttl, key=key, exceptions=exceptions, condition=condition,
                         prefix=prefix, tags=tags, backend=self._backend,
                         serializer=serializer or self._serializer)

    def early(self, ttl, key=None, early_ttl=None, condition=None,
              prefix="early", tags=(), serializer=None):
        from nb_cache.decorators.early import early as _early
        return _early(ttl, key=key, early_ttl=early_ttl, condition=condition,
                      prefix=prefix, tags=tags, backend=self._backend,
                      serializer=serializer or self._serializer)

    def soft(self, ttl, key=None, soft_ttl=None, condition=None,
             prefix="soft", tags=(), serializer=None):
        from nb_cache.decorators.soft import soft as _soft
        return _soft(ttl, key=key, soft_ttl=soft_ttl, condition=condition,
                     prefix=prefix, tags=tags, backend=self._backend,
                     serializer=serializer or self._serializer)

    def hit(self, ttl, cache_hits, update_after=0, key=None, condition=None,
            prefix="hit", tags=(), serializer=None):
        from nb_cache.decorators.hit import hit as _hit
        return _hit(ttl, cache_hits=cache_hits, update_after=update_after,
                    key=key, condition=condition, prefix=prefix, tags=tags,
                    backend=self._backend, serializer=serializer or self._serializer)

    def locked(self, ttl=None, key=None, wait=True, prefix="locked",
               check_interval=0.1):
        from nb_cache.decorators.locked import locked as _locked
        return _locked(ttl=ttl, key=key, wait=wait, prefix=prefix,
                       check_interval=check_interval, backend=self._backend)

    def thunder_protection(self, ttl=None, key=None, prefix="thunder"):
        from nb_cache.decorators.locked import thunder_protection as _tp
        return _tp(ttl=ttl, key=key, prefix=prefix, backend=self._backend)

    def circuit_breaker(self, errors_rate, period, ttl, half_open_ttl=None,
                        exceptions=None, key=None, min_calls=1,
                        prefix="circuit_breaker"):
        from nb_cache.decorators.circuit_breaker import circuit_breaker as _cb
        return _cb(errors_rate=errors_rate, period=period, ttl=ttl,
                   half_open_ttl=half_open_ttl, exceptions=exceptions,
                   key=key, min_calls=min_calls, prefix=prefix,
                   backend=self._backend)

    def rate_limit(self, limit, period, ttl=None, action=None,
                   prefix="rate_limit", key=None):
        from nb_cache.decorators.rate_limit import rate_limit as _rl
        return _rl(limit=limit, period=period, ttl=ttl, action=action,
                   prefix=prefix, key=key, backend=self._backend)

    def slice_rate_limit(self, limit, period, key=None, action=None,
                         prefix="srl"):
        from nb_cache.decorators.rate_limit import slice_rate_limit as _srl
        return _srl(limit=limit, period=period, key=key, action=action,
                    prefix=prefix, backend=self._backend)

    def bloom(self, capacity, name=None, false_positives=1, prefix="bloom"):
        from nb_cache.decorators.bloom import bloom as _bloom
        return _bloom(capacity=capacity, name=name, false_positives=false_positives,
                      prefix=prefix, backend=self._backend)

    def dual_bloom(self, capacity, name=None, false=1, prefix="dual_bloom"):
        from nb_cache.decorators.bloom import dual_bloom as _db
        return _db(capacity=capacity, name=name, false=false,
                   prefix=prefix, backend=self._backend)

    def iterator(self, ttl, key=None, condition=None, prefix="iter",
                 serializer=None):
        from nb_cache.decorators.iterator import iterator as _iter
        return _iter(ttl=ttl, key=key, condition=condition, prefix=prefix,
                     backend=self._backend, serializer=serializer or self._serializer)

    # --- Invalidation decorator ---

    def invalidate(self, func_or_cache_instance, args_map=None):
        """Decorator that invalidates cache for a cached function.

        Usage::

            @cache.cache(ttl=60)
            def get_user(user_id):
                ...

            @cache.invalidate(get_user)
            def update_user(user_id, data):
                ...
        """
        def decorator(invalidating_func):
            if is_coroutine_function(invalidating_func):
                @functools.wraps(invalidating_func)
                async def async_wrapper(*args, **kwargs):
                    result = await invalidating_func(*args, **kwargs)
                    key_template = getattr(func_or_cache_instance, '_cache_key_template', None)
                    if key_template:
                        from nb_cache.key import get_cache_key
                        cache_key = get_cache_key(func_or_cache_instance.__wrapped__
                                                  if hasattr(func_or_cache_instance, '__wrapped__')
                                                  else invalidating_func,
                                                  key_template, args, kwargs)
                        await self.delete(cache_key)
                    return result
                return async_wrapper
            else:
                @functools.wraps(invalidating_func)
                def sync_wrapper(*args, **kwargs):
                    result = invalidating_func(*args, **kwargs)
                    key_template = getattr(func_or_cache_instance, '_cache_key_template', None)
                    if key_template:
                        from nb_cache.key import get_cache_key
                        cache_key = get_cache_key(func_or_cache_instance.__wrapped__
                                                  if hasattr(func_or_cache_instance, '__wrapped__')
                                                  else invalidating_func,
                                                  key_template, args, kwargs)
                        self.delete_sync(cache_key)
                    return result
                return sync_wrapper
        return decorator

    # --- Middleware ---

    def add_middleware(self, middleware):
        self._middlewares.append(middleware)

    # --- Backend access ---

    @property
    def backend(self):
        return self._backend

`````

--- **end of file: nb_cache/wrapper.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/_compat.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Python version compatibility utilities for Python 3.6+."""
import sys
import asyncio
import inspect

PY36 = sys.version_info[:2] == (3, 6)
PY37_PLUS = sys.version_info >= (3, 7)
PY38_PLUS = sys.version_info >= (3, 8)
PY310_PLUS = sys.version_info >= (3, 10)


def get_event_loop():
    if PY310_PLUS:
        try:
            return asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.new_event_loop()
    else:
        return asyncio.get_event_loop()


def is_coroutine_function(func):
    if hasattr(func, '__wrapped__'):
        return asyncio.iscoroutinefunction(func.__wrapped__)
    return asyncio.iscoroutinefunction(func)


def create_task(coro):
    loop = get_event_loop()
    if hasattr(loop, 'create_task'):
        return loop.create_task(coro)
    return asyncio.ensure_future(coro, loop=loop)


def run_sync(coro):
    """Run a coroutine synchronously. Works across Python versions."""
    if PY37_PLUS:
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                    future = pool.submit(asyncio.run, coro)
                    return future.result()
            else:
                return loop.run_until_complete(coro)
        except RuntimeError:
            return asyncio.run(coro)
    else:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                new_loop = asyncio.new_event_loop()
                future = pool.submit(new_loop.run_until_complete, coro)
                return future.result()
        return loop.run_until_complete(coro)

`````

--- **end of file: nb_cache/_compat.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/__init__.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""nb_cache — 更强的缓存装饰器

支持同步和异步函数，支持加锁防止缓存击穿，
支持内存和Redis作为缓存器，支持Redis+内存双缓存提高性能。

Usage::

    from nb_cache import Cache

    cache = Cache()
    cache.setup("mem://")

    @cache.cache(ttl=60)
    def get_data(key):
        return expensive_query(key)

    @cache.cache(ttl="1h", lock=True)
    async def get_data_async(key):
        return await expensive_query_async(key)
"""

__version__ = "0.1.0"

from nb_cache.wrapper import Cache, register_backend
from nb_cache.condition import NOT_NONE, with_exceptions, only_exceptions
from nb_cache.exceptions import (
    CacheError,
    BackendNotInitializedError,
    CacheBackendInteractionError,
    LockError,
    LockedError,
    CircuitBreakerOpen,
    RateLimitError,
    SerializationError,
    TagError,
)
from nb_cache.transaction import TransactionMode
from nb_cache.key import get_cache_key_template
from nb_cache.helpers import noself, add_prefix, memory_limit, invalidate_further
from nb_cache.serialize import (
    Serializer,
    PickleSerializer,
    JsonSerializer,
    GzipCompressor,
    ZlibCompressor,
    HashSigner,
)
from nb_cache.ttl import ttl_to_seconds
from nb_cache.backends.base import BaseBackend
from nb_cache.backends.memory import MemoryBackend

mem = Cache()
mem.setup("mem://")

__all__ = [
    '__version__',
    # Main class
    'Cache',
    'mem',
    # Conditions
    'NOT_NONE',
    'with_exceptions',
    'only_exceptions',
    # Exceptions
    'CacheError',
    'BackendNotInitializedError',
    'CacheBackendInteractionError',
    'LockError',
    'LockedError',
    'CircuitBreakerOpen',
    'RateLimitError',
    'SerializationError',
    'TagError',
    # Transaction
    'TransactionMode',
    # Key
    'get_cache_key_template',
    # Helpers
    'noself',
    'add_prefix',
    'memory_limit',
    'invalidate_further',
    # Serialization
    'Serializer',
    'PickleSerializer',
    'JsonSerializer',
    'GzipCompressor',
    'ZlibCompressor',
    'HashSigner',
    # TTL
    'ttl_to_seconds',
    # Backends
    'BaseBackend',
    'MemoryBackend',
    'register_backend',
]

`````

--- **end of file: nb_cache/__init__.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/backends/base.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Abstract base class for cache backends.

Every backend must provide both sync and async interfaces.
"""
import asyncio


class BaseBackend(object):
    """Abstract cache backend with sync and async interfaces."""

    def __init__(self, **kwargs):
        self._is_init = False

    @property
    def is_init(self):
        return self._is_init

    # --- Lifecycle ---

    async def init(self):
        self._is_init = True

    def init_sync(self):
        self._is_init = True

    async def close(self):
        self._is_init = False

    def close_sync(self):
        self._is_init = False

    async def ping(self):
        return True

    def ping_sync(self):
        return True

    # --- Core GET/SET/DELETE (async) ---

    async def get(self, key):
        raise NotImplementedError

    async def set(self, key, value, ttl=None):
        raise NotImplementedError

    async def delete(self, key):
        raise NotImplementedError

    async def exists(self, key):
        raise NotImplementedError

    async def expire(self, key, ttl):
        raise NotImplementedError

    async def get_expire(self, key):
        """Return remaining TTL in seconds, or -1 if no expiry, or None if key missing."""
        raise NotImplementedError

    async def clear(self):
        raise NotImplementedError

    async def incr(self, key, amount=1):
        raise NotImplementedError

    # --- Batch operations (async) ---

    async def get_many(self, *keys):
        results = []
        for k in keys:
            results.append(await self.get(k))
        return results

    async def set_many(self, pairs, ttl=None):
        for key, value in pairs.items():
            await self.set(key, value, ttl=ttl)

    async def delete_many(self, *keys):
        for k in keys:
            await self.delete(k)

    async def delete_match(self, pattern):
        raise NotImplementedError

    # --- Scan / Match (async) ---

    async def scan(self, pattern):
        raise NotImplementedError

    async def get_match(self, pattern):
        raise NotImplementedError

    async def get_keys_count(self):
        raise NotImplementedError

    async def get_size(self):
        raise NotImplementedError

    # --- Lock (async) ---

    async def set_lock(self, key, ttl):
        raise NotImplementedError

    async def unlock(self, key):
        raise NotImplementedError

    async def is_locked(self, key):
        raise NotImplementedError

    # --- Set operations (async) ---

    async def set_add(self, key, *values):
        raise NotImplementedError

    async def set_remove(self, key, *values):
        raise NotImplementedError

    async def set_pop(self, key, count=1):
        raise NotImplementedError

    # --- Core GET/SET/DELETE (sync) ---

    def get_sync(self, key):
        raise NotImplementedError

    def set_sync(self, key, value, ttl=None):
        raise NotImplementedError

    def delete_sync(self, key):
        raise NotImplementedError

    def exists_sync(self, key):
        raise NotImplementedError

    def expire_sync(self, key, ttl):
        raise NotImplementedError

    def get_expire_sync(self, key):
        raise NotImplementedError

    def clear_sync(self):
        raise NotImplementedError

    def incr_sync(self, key, amount=1):
        raise NotImplementedError

    # --- Batch (sync) ---

    def get_many_sync(self, *keys):
        return [self.get_sync(k) for k in keys]

    def set_many_sync(self, pairs, ttl=None):
        for key, value in pairs.items():
            self.set_sync(key, value, ttl=ttl)

    def delete_many_sync(self, *keys):
        for k in keys:
            self.delete_sync(k)

    def delete_match_sync(self, pattern):
        raise NotImplementedError

    # --- Scan (sync) ---

    def scan_sync(self, pattern):
        raise NotImplementedError

    def get_match_sync(self, pattern):
        raise NotImplementedError

    def get_keys_count_sync(self):
        raise NotImplementedError

    def get_size_sync(self):
        raise NotImplementedError

    # --- Lock (sync) ---

    def set_lock_sync(self, key, ttl):
        raise NotImplementedError

    def unlock_sync(self, key):
        raise NotImplementedError

    def is_locked_sync(self, key):
        raise NotImplementedError

`````

--- **end of file: nb_cache/backends/base.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/backends/dual.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Dual cache backend: memory (L1) + Redis (L2).

Reads check memory first, then Redis on miss.
Writes go to both memory and Redis.
"""
from nb_cache.backends.base import BaseBackend
from nb_cache.backends.memory import MemoryBackend
from nb_cache.backends.redis import RedisBackend
from nb_cache.ttl import ttl_to_seconds


class DualBackend(BaseBackend):
    """Two-layer cache: fast in-memory L1 + Redis L2.

    Args:
        memory_size: Max entries for the memory layer.
        local_ttl: Default TTL for local memory cache (seconds).
            If set, local cache uses this TTL regardless of the outer TTL,
            which is useful for keeping local cache short-lived.
        url/host/port/db/password: Redis connection parameters.
        prefix: Redis key prefix.
    """

    def __init__(self, memory_size=1000, local_ttl=None,
                 url=None, host="localhost", port=6379, db=0,
                 password=None, prefix="", **kwargs):
        super(DualBackend, self).__init__(**kwargs)
        self._local_ttl = local_ttl
        self._memory = MemoryBackend(size=memory_size)
        self._redis = RedisBackend(
            url=url, host=host, port=port, db=db,
            password=password, prefix=prefix, **kwargs,
        )

    def _local_ttl_val(self, ttl):
        if self._local_ttl is not None:
            return self._local_ttl
        return ttl

    # --- Lifecycle ---

    async def init(self):
        await self._memory.init()
        await self._redis.init()
        await super(DualBackend, self).init()

    def init_sync(self):
        self._memory.init_sync()
        self._redis.init_sync()
        super(DualBackend, self).init_sync()

    async def close(self):
        await self._memory.close()
        await self._redis.close()
        await super(DualBackend, self).close()

    def close_sync(self):
        self._memory.close_sync()
        self._redis.close_sync()
        super(DualBackend, self).close_sync()

    async def ping(self):
        return await self._redis.ping()

    def ping_sync(self):
        return self._redis.ping_sync()

    # --- Async interface ---

    async def get(self, key):
        val = await self._memory.get(key)
        if val is not None:
            return val
        val = await self._redis.get(key)
        if val is not None:
            local_ttl = self._local_ttl_val(None)
            await self._memory.set(key, val, ttl=local_ttl)
        return val

    async def set(self, key, value, ttl=None):
        await self._redis.set(key, value, ttl=ttl)
        await self._memory.set(key, value, ttl=self._local_ttl_val(ttl))

    async def delete(self, key):
        await self._memory.delete(key)
        return await self._redis.delete(key)

    async def exists(self, key):
        if await self._memory.exists(key):
            return True
        return await self._redis.exists(key)

    async def expire(self, key, ttl):
        await self._memory.expire(key, self._local_ttl_val(ttl))
        return await self._redis.expire(key, ttl)

    async def get_expire(self, key):
        return await self._redis.get_expire(key)

    async def clear(self):
        await self._memory.clear()
        await self._redis.clear()

    async def incr(self, key, amount=1):
        result = await self._redis.incr(key, amount)
        self._memory.set_sync(key, result, ttl=self._local_ttl_val(None))
        return result

    async def get_many(self, *keys):
        results = []
        missed_keys = []
        missed_indices = []
        for i, k in enumerate(keys):
            val = await self._memory.get(k)
            results.append(val)
            if val is None:
                missed_keys.append(k)
                missed_indices.append(i)
        if missed_keys:
            redis_vals = await self._redis.get_many(*missed_keys)
            for idx, val in zip(missed_indices, redis_vals):
                results[idx] = val
                if val is not None:
                    k = keys[idx]
                    await self._memory.set(k, val, ttl=self._local_ttl_val(None))
        return results

    async def set_many(self, pairs, ttl=None):
        await self._redis.set_many(pairs, ttl=ttl)
        await self._memory.set_many(pairs, ttl=self._local_ttl_val(ttl))

    async def delete_many(self, *keys):
        await self._memory.delete_many(*keys)
        await self._redis.delete_many(*keys)

    async def delete_match(self, pattern):
        self._memory.delete_match_sync(pattern)
        await self._redis.delete_match(pattern)

    async def scan(self, pattern):
        return await self._redis.scan(pattern)

    async def get_match(self, pattern):
        return await self._redis.get_match(pattern)

    async def get_keys_count(self):
        return await self._redis.get_keys_count()

    async def get_size(self):
        return await self._redis.get_size()

    async def set_lock(self, key, ttl):
        return await self._redis.set_lock(key, ttl)

    async def unlock(self, key):
        return await self._redis.unlock(key)

    async def is_locked(self, key):
        return await self._redis.is_locked(key)

    # --- Sync interface ---

    def get_sync(self, key):
        val = self._memory.get_sync(key)
        if val is not None:
            return val
        val = self._redis.get_sync(key)
        if val is not None:
            local_ttl = self._local_ttl_val(None)
            self._memory.set_sync(key, val, ttl=local_ttl)
        return val

    def set_sync(self, key, value, ttl=None):
        self._redis.set_sync(key, value, ttl=ttl)
        self._memory.set_sync(key, value, ttl=self._local_ttl_val(ttl))

    def delete_sync(self, key):
        self._memory.delete_sync(key)
        return self._redis.delete_sync(key)

    def exists_sync(self, key):
        if self._memory.exists_sync(key):
            return True
        return self._redis.exists_sync(key)

    def expire_sync(self, key, ttl):
        self._memory.expire_sync(key, self._local_ttl_val(ttl))
        return self._redis.expire_sync(key, ttl)

    def get_expire_sync(self, key):
        return self._redis.get_expire_sync(key)

    def clear_sync(self):
        self._memory.clear_sync()
        self._redis.clear_sync()

    def incr_sync(self, key, amount=1):
        result = self._redis.incr_sync(key, amount)
        self._memory.set_sync(key, result, ttl=self._local_ttl_val(None))
        return result

    def get_many_sync(self, *keys):
        results = []
        missed_keys = []
        missed_indices = []
        for i, k in enumerate(keys):
            val = self._memory.get_sync(k)
            results.append(val)
            if val is None:
                missed_keys.append(k)
                missed_indices.append(i)
        if missed_keys:
            redis_vals = self._redis.get_many_sync(*missed_keys)
            for idx, val in zip(missed_indices, redis_vals):
                results[idx] = val
                if val is not None:
                    k = keys[idx]
                    self._memory.set_sync(k, val, ttl=self._local_ttl_val(None))
        return results

    def set_many_sync(self, pairs, ttl=None):
        self._redis.set_many_sync(pairs, ttl=ttl)
        self._memory.set_many_sync(pairs, ttl=self._local_ttl_val(ttl))

    def delete_many_sync(self, *keys):
        self._memory.delete_many_sync(*keys)
        self._redis.delete_many_sync(*keys)

    def delete_match_sync(self, pattern):
        self._memory.delete_match_sync(pattern)
        self._redis.delete_match_sync(pattern)

    def scan_sync(self, pattern):
        return self._redis.scan_sync(pattern)

    def get_match_sync(self, pattern):
        return self._redis.get_match_sync(pattern)

    def get_keys_count_sync(self):
        return self._redis.get_keys_count_sync()

    def get_size_sync(self):
        return self._redis.get_size_sync()

    def set_lock_sync(self, key, ttl):
        return self._redis.set_lock_sync(key, ttl)

    def unlock_sync(self, key):
        return self._redis.unlock_sync(key)

    def is_locked_sync(self, key):
        return self._redis.is_locked_sync(key)

`````

--- **end of file: nb_cache/backends/dual.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/backends/memory.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""In-memory LRU cache backend with sync and async support."""
import asyncio
import fnmatch
import re
import threading
import time
from collections import OrderedDict

from nb_cache.backends.base import BaseBackend
from nb_cache.ttl import ttl_to_seconds


class MemoryBackend(BaseBackend):
    """Thread-safe in-memory LRU cache backend.

    Args:
        size: Maximum number of entries. 0 means unlimited.
        check_interval: How often (seconds) to run passive expiry cleanup.
    """

    def __init__(self, size=0, check_interval=60, **kwargs):
        super(MemoryBackend, self).__init__(**kwargs)
        self._size = size
        self._check_interval = check_interval
        self._store = OrderedDict()   # key -> value
        self._expiry = {}             # key -> expire_timestamp
        self._locks = {}              # key -> expire_timestamp (for locks)
        self._sets = {}               # key -> set (for set operations)
        self._lock = threading.RLock()
        self._last_cleanup = time.time()

    # --- Lifecycle ---

    async def init(self):
        await super(MemoryBackend, self).init()

    def init_sync(self):
        super(MemoryBackend, self).init_sync()

    async def close(self):
        self.clear_sync()
        await super(MemoryBackend, self).close()

    def close_sync(self):
        self.clear_sync()
        super(MemoryBackend, self).close_sync()

    async def ping(self):
        return True

    def ping_sync(self):
        return True

    # --- Internal helpers ---

    def _maybe_cleanup(self):
        now = time.time()
        if now - self._last_cleanup > self._check_interval:
            self._last_cleanup = now
            self._do_cleanup()

    def _do_cleanup(self):
        now = time.time()
        expired_keys = [k for k, exp in self._expiry.items() if exp <= now]
        for k in expired_keys:
            self._remove_key(k)

    def _remove_key(self, key):
        self._store.pop(key, None)
        self._expiry.pop(key, None)

    def _is_expired(self, key):
        exp = self._expiry.get(key)
        if exp is not None and exp <= time.time():
            self._remove_key(key)
            return True
        return False

    def _evict_if_needed(self):
        if self._size > 0:
            while len(self._store) >= self._size:
                self._store.popitem(last=False)

    def _pattern_to_regex(self, pattern):
        regex = fnmatch.translate(pattern)
        return re.compile(regex)

    # --- Sync interface ---

    def get_sync(self, key):
        with self._lock:
            self._maybe_cleanup()
            if key not in self._store or self._is_expired(key):
                return None
            self._store.move_to_end(key)
            return self._store[key]

    def set_sync(self, key, value, ttl=None):
        with self._lock:
            self._maybe_cleanup()
            ttl_sec = ttl_to_seconds(ttl)
            self._evict_if_needed()
            self._store[key] = value
            self._store.move_to_end(key)
            if ttl_sec and ttl_sec > 0:
                self._expiry[key] = time.time() + ttl_sec
            else:
                self._expiry.pop(key, None)

    def delete_sync(self, key):
        with self._lock:
            self._remove_key(key)
            return True

    def exists_sync(self, key):
        with self._lock:
            if key not in self._store or self._is_expired(key):
                return False
            return True

    def expire_sync(self, key, ttl):
        with self._lock:
            if key not in self._store or self._is_expired(key):
                return False
            ttl_sec = ttl_to_seconds(ttl)
            if ttl_sec and ttl_sec > 0:
                self._expiry[key] = time.time() + ttl_sec
            else:
                self._expiry.pop(key, None)
            return True

    def get_expire_sync(self, key):
        with self._lock:
            if key not in self._store or self._is_expired(key):
                return None
            exp = self._expiry.get(key)
            if exp is None:
                return -1
            remaining = exp - time.time()
            return max(0.0, remaining)

    def clear_sync(self):
        with self._lock:
            self._store.clear()
            self._expiry.clear()
            self._locks.clear()
            self._sets.clear()

    def incr_sync(self, key, amount=1):
        with self._lock:
            if key not in self._store or self._is_expired(key):
                self._store[key] = amount
                return amount
            val = self._store[key]
            new_val = val + amount
            self._store[key] = new_val
            return new_val

    def get_many_sync(self, *keys):
        return [self.get_sync(k) for k in keys]

    def set_many_sync(self, pairs, ttl=None):
        for key, value in pairs.items():
            self.set_sync(key, value, ttl=ttl)

    def delete_many_sync(self, *keys):
        for k in keys:
            self.delete_sync(k)

    def delete_match_sync(self, pattern):
        with self._lock:
            regex = self._pattern_to_regex(pattern)
            to_delete = [k for k in self._store if regex.match(k)]
            for k in to_delete:
                self._remove_key(k)

    def scan_sync(self, pattern):
        with self._lock:
            self._maybe_cleanup()
            regex = self._pattern_to_regex(pattern)
            return [k for k in list(self._store.keys()) if regex.match(k) and not self._is_expired(k)]

    def get_match_sync(self, pattern):
        with self._lock:
            self._maybe_cleanup()
            regex = self._pattern_to_regex(pattern)
            result = {}
            for k in list(self._store.keys()):
                if regex.match(k) and not self._is_expired(k):
                    result[k] = self._store[k]
            return result

    def get_keys_count_sync(self):
        with self._lock:
            self._maybe_cleanup()
            return len(self._store)

    def get_size_sync(self):
        return self.get_keys_count_sync()

    # --- Lock (sync) ---

    def set_lock_sync(self, key, ttl):
        with self._lock:
            lock_key = "__lock__:{}".format(key)
            now = time.time()
            exp = self._locks.get(lock_key)
            if exp is not None and exp > now:
                return False
            ttl_sec = ttl_to_seconds(ttl)
            self._locks[lock_key] = now + (ttl_sec or 60)
            return True

    def unlock_sync(self, key):
        with self._lock:
            lock_key = "__lock__:{}".format(key)
            self._locks.pop(lock_key, None)
            return True

    def is_locked_sync(self, key):
        with self._lock:
            lock_key = "__lock__:{}".format(key)
            exp = self._locks.get(lock_key)
            if exp is None:
                return False
            if exp <= time.time():
                self._locks.pop(lock_key, None)
                return False
            return True

    # --- Async interface (delegates to sync with lock) ---

    async def get(self, key):
        return self.get_sync(key)

    async def set(self, key, value, ttl=None):
        self.set_sync(key, value, ttl=ttl)

    async def delete(self, key):
        return self.delete_sync(key)

    async def exists(self, key):
        return self.exists_sync(key)

    async def expire(self, key, ttl):
        return self.expire_sync(key, ttl)

    async def get_expire(self, key):
        return self.get_expire_sync(key)

    async def clear(self):
        self.clear_sync()

    async def incr(self, key, amount=1):
        return self.incr_sync(key, amount)

    async def get_many(self, *keys):
        return self.get_many_sync(*keys)

    async def set_many(self, pairs, ttl=None):
        self.set_many_sync(pairs, ttl=ttl)

    async def delete_many(self, *keys):
        self.delete_many_sync(*keys)

    async def delete_match(self, pattern):
        self.delete_match_sync(pattern)

    async def scan(self, pattern):
        return self.scan_sync(pattern)

    async def get_match(self, pattern):
        return self.get_match_sync(pattern)

    async def get_keys_count(self):
        return self.get_keys_count_sync()

    async def get_size(self):
        return self.get_size_sync()

    async def set_lock(self, key, ttl):
        return self.set_lock_sync(key, ttl)

    async def unlock(self, key):
        return self.unlock_sync(key)

    async def is_locked(self, key):
        return self.is_locked_sync(key)

`````

--- **end of file: nb_cache/backends/memory.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/backends/redis.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Redis cache backend with sync and async support."""
import time

from nb_cache.backends.base import BaseBackend
from nb_cache.ttl import ttl_to_seconds


class RedisBackend(BaseBackend):
    """Redis backend supporting both sync and async operations.

    Args:
        url: Redis URL (e.g. "redis://localhost:6379/0")
        host: Redis host
        port: Redis port
        db: Redis database number
        password: Redis password
        socket_timeout: Socket timeout in seconds
        max_connections: Maximum connections in pool
        prefix: Key prefix for namespacing
        **kwargs: Extra arguments passed to redis client
    """

    def __init__(self, url=None, host="localhost", port=6379, db=0,
                 password=None, socket_timeout=None, max_connections=None,
                 prefix="", **kwargs):
        super(RedisBackend, self).__init__(**kwargs)
        self._url = url
        self._host = host
        self._port = port
        self._db = db
        self._password = password
        self._socket_timeout = socket_timeout
        self._max_connections = max_connections
        self._prefix = prefix
        self._async_client = None
        self._sync_client = None
        self._extra_kwargs = kwargs

    def _make_key(self, key):
        if self._prefix:
            return "{}:{}".format(self._prefix, key)
        return key

    # --- Lifecycle ---

    async def init(self):
        try:
            import redis.asyncio as aioredis
        except ImportError:
            import aioredis
        connect_kwargs = {}
        if self._socket_timeout:
            connect_kwargs['socket_timeout'] = self._socket_timeout
        if self._max_connections:
            connect_kwargs['max_connections'] = self._max_connections

        if self._url:
            self._async_client = aioredis.from_url(self._url, decode_responses=False, **connect_kwargs)
        else:
            self._async_client = aioredis.Redis(
                host=self._host, port=self._port, db=self._db,
                password=self._password, decode_responses=False,
                **connect_kwargs,
            )
        await super(RedisBackend, self).init()

    def init_sync(self):
        import redis as sync_redis
        connect_kwargs = {}
        if self._socket_timeout:
            connect_kwargs['socket_timeout'] = self._socket_timeout
        if self._max_connections:
            connect_kwargs['max_connections'] = self._max_connections

        if self._url:
            self._sync_client = sync_redis.from_url(self._url, decode_responses=False, **connect_kwargs)
        else:
            self._sync_client = sync_redis.Redis(
                host=self._host, port=self._port, db=self._db,
                password=self._password, decode_responses=False,
                **connect_kwargs,
            )

        if self._async_client is None:
            try:
                import redis.asyncio as aioredis
            except ImportError:
                aioredis = None
            if aioredis is not None:
                if self._url:
                    self._async_client = aioredis.from_url(self._url, decode_responses=False, **connect_kwargs)
                else:
                    self._async_client = aioredis.Redis(
                        host=self._host, port=self._port, db=self._db,
                        password=self._password, decode_responses=False,
                        **connect_kwargs,
                    )

        super(RedisBackend, self).init_sync()

    async def close(self):
        if self._async_client:
            await self._async_client.close()
            self._async_client = None
        await super(RedisBackend, self).close()

    def close_sync(self):
        if self._sync_client:
            self._sync_client.close()
            self._sync_client = None
        super(RedisBackend, self).close_sync()

    async def ping(self):
        if self._async_client:
            return await self._async_client.ping()
        return False

    def ping_sync(self):
        if self._sync_client:
            return self._sync_client.ping()
        return False

    # --- Async interface ---

    async def get(self, key):
        return await self._async_client.get(self._make_key(key))

    async def set(self, key, value, ttl=None):
        ttl_sec = ttl_to_seconds(ttl)
        rkey = self._make_key(key)
        if ttl_sec and ttl_sec > 0:
            await self._async_client.setex(rkey, int(ttl_sec), value)
        else:
            await self._async_client.set(rkey, value)

    async def delete(self, key):
        return await self._async_client.delete(self._make_key(key))

    async def exists(self, key):
        return bool(await self._async_client.exists(self._make_key(key)))

    async def expire(self, key, ttl):
        ttl_sec = ttl_to_seconds(ttl)
        if ttl_sec and ttl_sec > 0:
            return await self._async_client.expire(self._make_key(key), int(ttl_sec))
        return False

    async def get_expire(self, key):
        val = await self._async_client.ttl(self._make_key(key))
        if val == -2:
            return None
        return val

    async def clear(self):
        if self._prefix:
            await self.delete_match("*")
        else:
            await self._async_client.flushdb()

    async def incr(self, key, amount=1):
        return await self._async_client.incrby(self._make_key(key), amount)

    async def get_many(self, *keys):
        if not keys:
            return []
        rkeys = [self._make_key(k) for k in keys]
        return await self._async_client.mget(*rkeys)

    async def set_many(self, pairs, ttl=None):
        ttl_sec = ttl_to_seconds(ttl)
        pipe = self._async_client.pipeline()
        for key, value in pairs.items():
            rkey = self._make_key(key)
            if ttl_sec and ttl_sec > 0:
                pipe.setex(rkey, int(ttl_sec), value)
            else:
                pipe.set(rkey, value)
        await pipe.execute()

    async def delete_many(self, *keys):
        if keys:
            rkeys = [self._make_key(k) for k in keys]
            await self._async_client.delete(*rkeys)

    async def delete_match(self, pattern):
        rpattern = self._make_key(pattern)
        cursor = 0
        while True:
            cursor, keys = await self._async_client.scan(cursor, match=rpattern, count=100)
            if keys:
                await self._async_client.delete(*keys)
            if cursor == 0:
                break

    async def scan(self, pattern):
        rpattern = self._make_key(pattern)
        result = []
        cursor = 0
        prefix_len = len(self._prefix) + 1 if self._prefix else 0
        while True:
            cursor, keys = await self._async_client.scan(cursor, match=rpattern, count=100)
            for k in keys:
                kstr = k.decode('utf-8') if isinstance(k, bytes) else k
                if prefix_len:
                    kstr = kstr[prefix_len:]
                result.append(kstr)
            if cursor == 0:
                break
        return result

    async def get_match(self, pattern):
        keys = await self.scan(pattern)
        result = {}
        for k in keys:
            val = await self.get(k)
            if val is not None:
                result[k] = val
        return result

    async def get_keys_count(self):
        return await self._async_client.dbsize()

    async def get_size(self):
        return await self.get_keys_count()

    # --- Lock (async) ---

    async def set_lock(self, key, ttl):
        ttl_sec = ttl_to_seconds(ttl)
        rkey = self._make_key("__lock__:{}".format(key))
        result = await self._async_client.set(rkey, b"1", nx=True, ex=int(ttl_sec or 60))
        return result is not None and result is not False

    async def unlock(self, key):
        rkey = self._make_key("__lock__:{}".format(key))
        await self._async_client.delete(rkey)
        return True

    async def is_locked(self, key):
        rkey = self._make_key("__lock__:{}".format(key))
        return bool(await self._async_client.exists(rkey))

    # --- Sync interface ---

    def get_sync(self, key):
        return self._sync_client.get(self._make_key(key))

    def set_sync(self, key, value, ttl=None):
        ttl_sec = ttl_to_seconds(ttl)
        rkey = self._make_key(key)
        if ttl_sec and ttl_sec > 0:
            self._sync_client.setex(rkey, int(ttl_sec), value)
        else:
            self._sync_client.set(rkey, value)

    def delete_sync(self, key):
        return self._sync_client.delete(self._make_key(key))

    def exists_sync(self, key):
        return bool(self._sync_client.exists(self._make_key(key)))

    def expire_sync(self, key, ttl):
        ttl_sec = ttl_to_seconds(ttl)
        if ttl_sec and ttl_sec > 0:
            return self._sync_client.expire(self._make_key(key), int(ttl_sec))
        return False

    def get_expire_sync(self, key):
        val = self._sync_client.ttl(self._make_key(key))
        if val == -2:
            return None
        return val

    def clear_sync(self):
        if self._prefix:
            self.delete_match_sync("*")
        else:
            self._sync_client.flushdb()

    def incr_sync(self, key, amount=1):
        return self._sync_client.incrby(self._make_key(key), amount)

    def get_many_sync(self, *keys):
        if not keys:
            return []
        rkeys = [self._make_key(k) for k in keys]
        return self._sync_client.mget(*rkeys)

    def set_many_sync(self, pairs, ttl=None):
        ttl_sec = ttl_to_seconds(ttl)
        pipe = self._sync_client.pipeline()
        for key, value in pairs.items():
            rkey = self._make_key(key)
            if ttl_sec and ttl_sec > 0:
                pipe.setex(rkey, int(ttl_sec), value)
            else:
                pipe.set(rkey, value)
        pipe.execute()

    def delete_many_sync(self, *keys):
        if keys:
            rkeys = [self._make_key(k) for k in keys]
            self._sync_client.delete(*rkeys)

    def delete_match_sync(self, pattern):
        rpattern = self._make_key(pattern)
        cursor = 0
        while True:
            cursor, keys = self._sync_client.scan(cursor, match=rpattern, count=100)
            if keys:
                self._sync_client.delete(*keys)
            if cursor == 0:
                break

    def scan_sync(self, pattern):
        rpattern = self._make_key(pattern)
        result = []
        cursor = 0
        prefix_len = len(self._prefix) + 1 if self._prefix else 0
        while True:
            cursor, keys = self._sync_client.scan(cursor, match=rpattern, count=100)
            for k in keys:
                kstr = k.decode('utf-8') if isinstance(k, bytes) else k
                if prefix_len:
                    kstr = kstr[prefix_len:]
                result.append(kstr)
            if cursor == 0:
                break
        return result

    def get_match_sync(self, pattern):
        keys = self.scan_sync(pattern)
        result = {}
        for k in keys:
            val = self.get_sync(k)
            if val is not None:
                result[k] = val
        return result

    def get_keys_count_sync(self):
        return self._sync_client.dbsize()

    def get_size_sync(self):
        return self.get_keys_count_sync()

    # --- Lock (sync) ---

    def set_lock_sync(self, key, ttl):
        ttl_sec = ttl_to_seconds(ttl)
        rkey = self._make_key("__lock__:{}".format(key))
        result = self._sync_client.set(rkey, b"1", nx=True, ex=int(ttl_sec or 60))
        return result is not None and result is not False

    def unlock_sync(self, key):
        rkey = self._make_key("__lock__:{}".format(key))
        self._sync_client.delete(rkey)
        return True

    def is_locked_sync(self, key):
        rkey = self._make_key("__lock__:{}".format(key))
        return bool(self._sync_client.exists(rkey))

`````

--- **end of file: nb_cache/backends/redis.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/backends/__init__.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
from nb_cache.backends.base import BaseBackend
from nb_cache.backends.memory import MemoryBackend

__all__ = ['BaseBackend', 'MemoryBackend']

`````

--- **end of file: nb_cache/backends/__init__.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/bloom.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Bloom filter decorators.

- bloom: Check existence via a probabilistic bloom filter.
- dual_bloom: Two bloom filters for both positive and negative lookups.
"""
import functools
import hashlib
import math

from nb_cache._compat import is_coroutine_function
from nb_cache.key import get_cache_key, get_cache_key_template


def _optimal_params(capacity, false_positive_rate):
    """Calculate optimal bit array size and number of hash functions."""
    m = int(-capacity * math.log(false_positive_rate / 100.0) / (math.log(2) ** 2))
    k = max(1, int((m / capacity) * math.log(2)))
    return m, k


def _get_hash_indexes(key, m, k):
    """Generate k bit indexes from key using double hashing."""
    h1 = int(hashlib.md5(key.encode()).hexdigest(), 16)
    h2 = int(hashlib.sha1(key.encode()).hexdigest(), 16)
    return [(h1 + i * h2) % m for i in range(k)]


class BloomFilter(object):
    """Simple in-memory bloom filter backed by a cache backend."""

    def __init__(self, name, capacity, false_positive_rate, backend):
        self.name = name
        self.capacity = capacity
        self.m, self.k = _optimal_params(capacity, false_positive_rate)
        self._backend = backend
        self._bit_key = "__bloom__:{}".format(name)

    def _indexes(self, item):
        return _get_hash_indexes(str(item), self.m, self.k)

    def add_sync(self, item):
        be = self._backend
        for idx in self._indexes(item):
            key = "{}:{}".format(self._bit_key, idx)
            be.set_sync(key, b"1")

    async def add(self, item):
        be = self._backend
        for idx in self._indexes(item):
            key = "{}:{}".format(self._bit_key, idx)
            await be.set(key, b"1")

    def check_sync(self, item):
        be = self._backend
        for idx in self._indexes(item):
            key = "{}:{}".format(self._bit_key, idx)
            if be.get_sync(key) is None:
                return False
        return True

    async def check(self, item):
        be = self._backend
        for idx in self._indexes(item):
            key = "{}:{}".format(self._bit_key, idx)
            if await be.get(key) is None:
                return False
        return True


def bloom(capacity, name=None, false_positives=1, prefix="bloom", backend=None):
    """Bloom filter decorator.

    Wraps a function so that results are tracked in a bloom filter.
    Before calling, checks the bloom filter and skips execution if the
    item is definitely not present.

    Args:
        capacity: Expected number of elements.
        name: Bloom filter name (defaults to function name).
        false_positives: False positive rate percentage (1 = 1%).
        prefix: Key prefix.
        backend: Backend instance.
    """
    def decorator(func):
        _backend_ref = [backend]
        _name = name or "{}:{}".format(prefix, func.__qualname__)

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        _bf = [None]

        def _get_bf():
            if _bf[0] is None:
                _bf[0] = BloomFilter(_name, capacity, false_positives, _get_backend())
            return _bf[0]

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                bf = _get_bf()
                _key_template = get_cache_key_template(func, None, prefix)
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                if not await bf.check(cache_key):
                    return None
                result = await func(*args, **kwargs)
                await bf.add(cache_key)
                return result

            async_wrapper._bloom_filter = _get_bf
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                bf = _get_bf()
                _key_template = get_cache_key_template(func, None, prefix)
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                if not bf.check_sync(cache_key):
                    return None
                result = func(*args, **kwargs)
                bf.add_sync(cache_key)
                return result

            sync_wrapper._bloom_filter = _get_bf
            return sync_wrapper

    return decorator


def dual_bloom(capacity, name=None, false=1, prefix="dual_bloom", backend=None):
    """Dual bloom filter: one for positive, one for negative results.

    Args:
        capacity: Expected number of elements.
        name: Filter name.
        false: False positive rate percentage.
        prefix: Key prefix.
        backend: Backend instance.
    """
    def decorator(func):
        _backend_ref = [backend]
        _name = name or "{}:{}".format(prefix, func.__qualname__)

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        _bf_pos = [None]
        _bf_neg = [None]

        def _get_filters():
            be = _get_backend()
            if _bf_pos[0] is None:
                _bf_pos[0] = BloomFilter(_name + ":pos", capacity, false, be)
                _bf_neg[0] = BloomFilter(_name + ":neg", capacity, false, be)
            return _bf_pos[0], _bf_neg[0]

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                bf_pos, bf_neg = _get_filters()
                _key_template = get_cache_key_template(func, None, prefix)
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                if await bf_neg.check(cache_key):
                    return None
                result = await func(*args, **kwargs)
                if result is not None:
                    await bf_pos.add(cache_key)
                else:
                    await bf_neg.add(cache_key)
                return result

            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                bf_pos, bf_neg = _get_filters()
                _key_template = get_cache_key_template(func, None, prefix)
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                if bf_neg.check_sync(cache_key):
                    return None
                result = func(*args, **kwargs)
                if result is not None:
                    bf_pos.add_sync(cache_key)
                else:
                    bf_neg.add_sync(cache_key)
                return result

            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/bloom.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/cache.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Basic cache decorator with sync/async support and optional locking."""
import asyncio
import functools
import logging

from nb_cache._compat import is_coroutine_function
from nb_cache.condition import get_cache_condition
from nb_cache.key import get_cache_key, get_cache_key_template, get_func_name
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.ttl import ttl_to_seconds

logger = logging.getLogger("nb_cache.cache")


def _final_key(be, cache_key):
    """通过 backend 的 _make_key 方法获取最终写入存储的完整 key。"""
    if hasattr(be, '_make_key'):
        return be._make_key(cache_key)
    return cache_key


def cache(ttl, key=None, condition=None, prefix="", lock=False,
          lock_ttl=None, tags=(), backend=None, serializer=None,
          tag_registry=None, key_include_func=True):
    """Basic cache decorator.

    Supports both sync and async functions transparently.

    Args:
        ttl: Time to live (seconds, timedelta, or string like "1h").
        key: Key template string. If None, auto-generated from function signature.
        condition: Callable(result) -> bool, determines if result should be cached.
        prefix: Key prefix string.
        lock: If True, use locking to prevent cache stampede.
        lock_ttl: Lock TTL (defaults to ttl if not set).
        tags: Tuple of tag strings for tag-based invalidation.
        backend: Cache backend instance. If None, uses the global default.
        serializer: Serializer instance. If None, uses default.
        tag_registry: TagRegistry instance for tag-based invalidation.
        key_include_func: If False, module path and function name are excluded
            from the generated key. Default True.
    """
    _condition = get_cache_condition(condition)
    _serializer = serializer or default_serializer
    _ttl_seconds = ttl_to_seconds(ttl)
    _lock_ttl = ttl_to_seconds(lock_ttl) if lock_ttl else _ttl_seconds

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix, key_include_func=key_include_func)
        _backend_ref = [backend]
        _registry = tag_registry

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                logger.debug("[nb_cache] func=%s  final_key=%s  ttl=%s",
                             get_func_name(func), _final_key(be, cache_key), _ttl_seconds)

                raw = await be.get(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        return val

                if lock:
                    acquired = await be.set_lock(cache_key, _lock_ttl)
                    if not acquired:
                        for _ in range(50):
                            await asyncio.sleep(0.1)
                            raw = await be.get(cache_key)
                            if raw is not None:
                                val = _serializer.decode(raw)
                                if val is not _SENTINEL:
                                    return val
                        return await func(*args, **kwargs)

                try:
                    result = await func(*args, **kwargs)
                finally:
                    if lock:
                        await be.unlock(cache_key)

                if _condition(result):
                    encoded = _serializer.encode(result)
                    await be.set(cache_key, encoded, ttl=_ttl_seconds)
                    if tags and _registry is not None:
                        _registry.register(cache_key, tags)

                return result

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            async_wrapper._cache_tags = tags
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                logger.debug("[nb_cache] func=%s  final_key=%s  ttl=%s",
                             get_func_name(func), _final_key(be, cache_key), _ttl_seconds)

                raw = be.get_sync(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        return val

                if lock:
                    acquired = be.set_lock_sync(cache_key, _lock_ttl)
                    if not acquired:
                        import time as _time
                        for _ in range(50):
                            _time.sleep(0.1)
                            raw = be.get_sync(cache_key)
                            if raw is not None:
                                val = _serializer.decode(raw)
                                if val is not _SENTINEL:
                                    return val
                        return func(*args, **kwargs)

                try:
                    result = func(*args, **kwargs)
                finally:
                    if lock:
                        be.unlock_sync(cache_key)

                if _condition(result):
                    encoded = _serializer.encode(result)
                    be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                    if tags and _registry is not None:
                        _registry.register(cache_key, tags)

                return result

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            sync_wrapper._cache_tags = tags
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/cache.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/circuit_breaker.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Circuit breaker decorator.

Tracks error rate and opens the circuit when it exceeds a threshold,
preventing further calls for a cooldown period.

States: CLOSED -> OPEN -> HALF_OPEN -> CLOSED
"""
import functools
import time

from nb_cache._compat import is_coroutine_function
from nb_cache.exceptions import CircuitBreakerOpen
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.ttl import ttl_to_seconds


def circuit_breaker(errors_rate, period, ttl, half_open_ttl=None,
                    exceptions=None, key=None, min_calls=1,
                    prefix="circuit_breaker", backend=None):
    """Circuit breaker decorator.

    Args:
        errors_rate: Error rate threshold (0.0 to 1.0) to trip the breaker.
        period: Time window (seconds) to calculate error rate.
        ttl: How long the circuit stays OPEN.
        half_open_ttl: TTL for half-open state. Defaults to ttl/2.
        exceptions: Exception types to track. Defaults to (Exception,).
        min_calls: Minimum calls before error rate is evaluated.
        prefix: Key prefix.
        backend: Backend instance.
    """
    _period = ttl_to_seconds(period) or 60
    _ttl_seconds = ttl_to_seconds(ttl) or 60
    _half_open_ttl = ttl_to_seconds(half_open_ttl) if half_open_ttl else (_ttl_seconds / 2)
    _exceptions = tuple(exceptions) if exceptions else (Exception,)

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]

        _STATE_KEY = "__cb_state__:"
        _CALLS_KEY = "__cb_calls__:"
        _ERRORS_KEY = "__cb_errors__:"
        _TRIP_KEY = "__cb_trip__:"

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                base_key = get_cache_key(func, _key_template, args, kwargs)
                state_key = _STATE_KEY + base_key
                calls_key = _CALLS_KEY + base_key
                errors_key = _ERRORS_KEY + base_key
                trip_key = _TRIP_KEY + base_key

                state = await be.get(state_key)
                if state == b"open":
                    raise CircuitBreakerOpen(
                        "Circuit breaker is open for: {}".format(base_key))
                if state == b"half_open":
                    pass

                try:
                    result = await func(*args, **kwargs)
                except _exceptions:
                    await be.incr(errors_key)
                    await be.expire(errors_key, int(_period))
                    await be.incr(calls_key)
                    await be.expire(calls_key, int(_period))
                    await _check_and_trip(be, state_key, calls_key, errors_key, trip_key)
                    raise
                else:
                    await be.incr(calls_key)
                    await be.expire(calls_key, int(_period))
                    if state == b"half_open":
                        await be.delete(state_key)
                        await be.delete(calls_key)
                        await be.delete(errors_key)
                    return result

            async def _check_and_trip(be, state_key, calls_key, errors_key, trip_key):
                calls_raw = await be.get(calls_key)
                errors_raw = await be.get(errors_key)
                total = int(calls_raw) if calls_raw else 0
                errors = int(errors_raw) if errors_raw else 0
                if total >= min_calls and errors / max(total, 1) >= errors_rate:
                    await be.set(state_key, b"open", ttl=_ttl_seconds)
                    await _schedule_half_open(be, state_key)

            async def _schedule_half_open(be, state_key):
                import asyncio
                await asyncio.sleep(0)
                await be.set(state_key, b"open", ttl=_ttl_seconds)

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                base_key = get_cache_key(func, _key_template, args, kwargs)
                state_key = _STATE_KEY + base_key
                calls_key = _CALLS_KEY + base_key
                errors_key = _ERRORS_KEY + base_key
                trip_key = _TRIP_KEY + base_key

                state = be.get_sync(state_key)
                if state == b"open":
                    raise CircuitBreakerOpen(
                        "Circuit breaker is open for: {}".format(base_key))

                try:
                    result = func(*args, **kwargs)
                except _exceptions:
                    be.incr_sync(errors_key)
                    be.expire_sync(errors_key, int(_period))
                    be.incr_sync(calls_key)
                    be.expire_sync(calls_key, int(_period))
                    _check_and_trip_sync(be, state_key, calls_key, errors_key)
                    raise
                else:
                    be.incr_sync(calls_key)
                    be.expire_sync(calls_key, int(_period))
                    if state == b"half_open":
                        be.delete_sync(state_key)
                        be.delete_sync(calls_key)
                        be.delete_sync(errors_key)
                    return result

            def _check_and_trip_sync(be, state_key, calls_key, errors_key):
                calls_raw = be.get_sync(calls_key)
                errors_raw = be.get_sync(errors_key)
                total = int(calls_raw) if calls_raw else 0
                errors = int(errors_raw) if errors_raw else 0
                if total >= min_calls and errors / max(total, 1) >= errors_rate:
                    be.set_sync(state_key, b"open", ttl=_ttl_seconds)

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/circuit_breaker.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/early.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Early refresh cache decorator.

Refreshes the cache before expiry to prevent cache stampede.
When the remaining TTL drops below `early_ttl`, the next request triggers
a background refresh while returning the stale value.
"""
import asyncio
import functools
import threading

from nb_cache._compat import is_coroutine_function, create_task
from nb_cache.condition import get_cache_condition
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.ttl import ttl_to_seconds


def early(ttl, key=None, early_ttl=None, condition=None, prefix="early",
          tags=(), backend=None, serializer=None):
    """Cache with early background refresh.

    Args:
        ttl: Total time to live.
        early_ttl: When remaining TTL falls below this, trigger refresh.
            Defaults to ttl / 4.
        condition: Cache condition callable.
        prefix: Key prefix.
        tags: Tags for invalidation.
        backend: Backend instance.
        serializer: Serializer instance.
    """
    _condition = get_cache_condition(condition)
    _serializer = serializer or default_serializer
    _ttl_seconds = ttl_to_seconds(ttl)
    _early_ttl = ttl_to_seconds(early_ttl) if early_ttl else (_ttl_seconds / 4 if _ttl_seconds else None)

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]
        _refreshing = set()

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                raw = await be.get(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        remaining = await be.get_expire(cache_key)
                        if remaining is not None and _early_ttl and 0 < remaining < _early_ttl:
                            if cache_key not in _refreshing:
                                _refreshing.add(cache_key)

                                async def _refresh():
                                    try:
                                        result = await func(*args, **kwargs)
                                        if _condition(result):
                                            encoded = _serializer.encode(result)
                                            await be.set(cache_key, encoded, ttl=_ttl_seconds)
                                    finally:
                                        _refreshing.discard(cache_key)

                                create_task(_refresh())
                        return val

                result = await func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    await be.set(cache_key, encoded, ttl=_ttl_seconds)
                return result

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            async_wrapper._cache_tags = tags
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                raw = be.get_sync(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        remaining = be.get_expire_sync(cache_key)
                        if remaining is not None and _early_ttl and 0 < remaining < _early_ttl:
                            if cache_key not in _refreshing:
                                _refreshing.add(cache_key)

                                def _refresh():
                                    try:
                                        result = func(*args, **kwargs)
                                        if _condition(result):
                                            encoded = _serializer.encode(result)
                                            be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                                    finally:
                                        _refreshing.discard(cache_key)

                                t = threading.Thread(target=_refresh, daemon=True)
                                t.start()
                        return val

                result = func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                return result

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            sync_wrapper._cache_tags = tags
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/early.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/failover.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Failover cache decorator.

On exception, returns the cached value if available.
"""
import functools

from nb_cache._compat import is_coroutine_function
from nb_cache.condition import get_cache_condition
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.ttl import ttl_to_seconds


def failover(ttl, key=None, exceptions=None, condition=None, prefix="fail",
             tags=(), backend=None, serializer=None):
    """Cache with failover: on exception, return stale cached value.

    Args:
        ttl: Time to live for cached values.
        exceptions: Tuple of exception types to catch. Defaults to (Exception,).
        condition: Cache condition callable.
    """
    _condition = get_cache_condition(condition)
    _serializer = serializer or default_serializer
    _ttl_seconds = ttl_to_seconds(ttl)
    _exceptions = exceptions or (Exception,)

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                try:
                    result = await func(*args, **kwargs)
                    if _condition(result):
                        encoded = _serializer.encode(result)
                        await be.set(cache_key, encoded, ttl=_ttl_seconds)
                    return result
                except _exceptions:
                    raw = await be.get(cache_key)
                    if raw is not None:
                        val = _serializer.decode(raw)
                        if val is not _SENTINEL:
                            return val
                    raise

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            async_wrapper._cache_tags = tags
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                try:
                    result = func(*args, **kwargs)
                    if _condition(result):
                        encoded = _serializer.encode(result)
                        be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                    return result
                except _exceptions:
                    raw = be.get_sync(cache_key)
                    if raw is not None:
                        val = _serializer.decode(raw)
                        if val is not _SENTINEL:
                            return val
                    raise

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            sync_wrapper._cache_tags = tags
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/failover.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/hit.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Hit-based cache decorator.

Drops the cached value after N hits, forcing a refresh.
Optionally refreshes in background after `update_after` hits.
"""
import asyncio
import functools
import threading

from nb_cache._compat import is_coroutine_function, create_task
from nb_cache.condition import get_cache_condition
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.ttl import ttl_to_seconds

_HIT_COUNT_PREFIX = "__hit_cnt__:"


def hit(ttl, cache_hits, update_after=0, key=None, condition=None,
        prefix="hit", tags=(), backend=None, serializer=None):
    """Cache that invalidates after a number of hits.

    Args:
        ttl: Time to live.
        cache_hits: Number of hits before eviction.
        update_after: Trigger background update after this many hits (0=disabled).
        condition: Cache condition callable.
    """
    _condition = get_cache_condition(condition)
    _serializer = serializer or default_serializer
    _ttl_seconds = ttl_to_seconds(ttl)

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]
        _refreshing = set()

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                hit_key = _HIT_COUNT_PREFIX + cache_key

                raw = await be.get(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        count = await be.incr(hit_key)
                        if count >= cache_hits:
                            await be.delete(cache_key)
                            await be.delete(hit_key)
                        elif update_after and count >= update_after and cache_key not in _refreshing:
                            _refreshing.add(cache_key)

                            async def _refresh():
                                try:
                                    result = await func(*args, **kwargs)
                                    if _condition(result):
                                        encoded = _serializer.encode(result)
                                        await be.set(cache_key, encoded, ttl=_ttl_seconds)
                                        await be.delete(hit_key)
                                finally:
                                    _refreshing.discard(cache_key)

                            create_task(_refresh())
                        return val

                result = await func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    await be.set(cache_key, encoded, ttl=_ttl_seconds)
                    await be.delete(hit_key)
                return result

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            async_wrapper._cache_tags = tags
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                hit_key = _HIT_COUNT_PREFIX + cache_key

                raw = be.get_sync(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        count = be.incr_sync(hit_key)
                        if count >= cache_hits:
                            be.delete_sync(cache_key)
                            be.delete_sync(hit_key)
                        elif update_after and count >= update_after and cache_key not in _refreshing:
                            _refreshing.add(cache_key)

                            def _refresh():
                                try:
                                    result = func(*args, **kwargs)
                                    if _condition(result):
                                        encoded = _serializer.encode(result)
                                        be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                                        be.delete_sync(hit_key)
                                finally:
                                    _refreshing.discard(cache_key)

                            t = threading.Thread(target=_refresh, daemon=True)
                            t.start()
                        return val

                result = func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                    be.delete_sync(hit_key)
                return result

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            sync_wrapper._cache_tags = tags
            return sync_wrapper

    return decorator


def dynamic(ttl=86400, key=None, condition=None, prefix="dynamic",
            tags=(), backend=None, serializer=None):
    """Alias for hit with cache_hits=3, update_after=1."""
    return hit(ttl, cache_hits=3, update_after=1, key=key, condition=condition,
               prefix=prefix, tags=tags, backend=backend, serializer=serializer)

`````

--- **end of file: nb_cache/decorators/hit.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/iterator.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Iterator/generator cache decorator.

Caches the results of sync generators and async generators.
"""
import asyncio
import functools

from nb_cache._compat import is_coroutine_function
from nb_cache.condition import get_cache_condition
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.ttl import ttl_to_seconds
import inspect


def iterator(ttl, key=None, condition=None, prefix="iter",
             backend=None, serializer=None):
    """Cache decorator for generators and async generators.

    Collects all yielded items, caches them as a list, and replays
    from cache on subsequent calls.

    Args:
        ttl: Time to live.
        key: Key template.
        condition: Cache condition.
        prefix: Key prefix.
        backend: Backend instance.
        serializer: Serializer instance.
    """
    _condition = get_cache_condition(condition)
    _serializer = serializer or default_serializer
    _ttl_seconds = ttl_to_seconds(ttl)

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if inspect.isasyncgenfunction(func):
            @functools.wraps(func)
            async def async_gen_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                raw = await be.get(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL and isinstance(val, list):
                        for item in val:
                            yield item
                        return

                items = []
                async for item in func(*args, **kwargs):
                    items.append(item)
                    yield item

                if _condition(items):
                    encoded = _serializer.encode(items)
                    await be.set(cache_key, encoded, ttl=_ttl_seconds)

            async_gen_wrapper._cache_key_template = _key_template
            async_gen_wrapper._cache_backend_ref = _backend_ref
            return async_gen_wrapper

        elif inspect.isgeneratorfunction(func):
            @functools.wraps(func)
            def sync_gen_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                raw = be.get_sync(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL and isinstance(val, list):
                        for item in val:
                            yield item
                        return

                items = []
                for item in func(*args, **kwargs):
                    items.append(item)
                    yield item

                if _condition(items):
                    encoded = _serializer.encode(items)
                    be.set_sync(cache_key, encoded, ttl=_ttl_seconds)

            sync_gen_wrapper._cache_key_template = _key_template
            sync_gen_wrapper._cache_backend_ref = _backend_ref
            return sync_gen_wrapper

        elif is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                raw = await be.get(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        return val

                result = await func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    await be.set(cache_key, encoded, ttl=_ttl_seconds)
                return result

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                raw = be.get_sync(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        return val

                result = func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                return result

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/iterator.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/locked.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Lock decorator and thunder protection.

- locked: Ensures only one caller executes the function at a time.
- thunder_protection: Deduplicates concurrent calls with same key.
"""
import asyncio
import functools
import time

from nb_cache._compat import is_coroutine_function
from nb_cache.exceptions import LockedError
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.ttl import ttl_to_seconds


def locked(ttl=None, key=None, wait=True, prefix="locked",
           check_interval=0.1, backend=None):
    """Lock decorator to prevent concurrent execution.

    Args:
        ttl: Lock TTL. Defaults to 60 seconds.
        wait: If True, wait for lock. If False, raise LockedError.
        check_interval: Seconds between lock checks when waiting.
        backend: Backend instance.
    """
    _ttl_seconds = ttl_to_seconds(ttl) or 60
    _check_interval = check_interval or 0.1

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                lock_key = "__dlock__:{}".format(cache_key)

                acquired = await be.set_lock(lock_key, _ttl_seconds)
                if not acquired:
                    if not wait:
                        raise LockedError("Resource is locked: {}".format(lock_key))
                    deadline = time.time() + _ttl_seconds
                    while time.time() < deadline:
                        await asyncio.sleep(_check_interval)
                        acquired = await be.set_lock(lock_key, _ttl_seconds)
                        if acquired:
                            break
                    if not acquired:
                        raise LockedError("Timeout waiting for lock: {}".format(lock_key))

                try:
                    return await func(*args, **kwargs)
                finally:
                    await be.unlock(lock_key)

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                lock_key = "__dlock__:{}".format(cache_key)

                acquired = be.set_lock_sync(lock_key, _ttl_seconds)
                if not acquired:
                    if not wait:
                        raise LockedError("Resource is locked: {}".format(lock_key))
                    deadline = time.time() + _ttl_seconds
                    while time.time() < deadline:
                        time.sleep(_check_interval)
                        acquired = be.set_lock_sync(lock_key, _ttl_seconds)
                        if acquired:
                            break
                    if not acquired:
                        raise LockedError("Timeout waiting for lock: {}".format(lock_key))

                try:
                    return func(*args, **kwargs)
                finally:
                    be.unlock_sync(lock_key)

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            return sync_wrapper

    return decorator


def thunder_protection(ttl=None, key=None, prefix="thunder", backend=None):
    """Deduplicate concurrent calls with same arguments.

    The first caller executes the function; concurrent callers with the same
    key wait for the result instead of executing again.
    """
    _ttl_seconds = ttl_to_seconds(ttl) or 60

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]
        _pending_async = {}
        _pending_sync = {}
        import threading
        _sync_lock = threading.Lock()

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                if cache_key in _pending_async:
                    return await _pending_async[cache_key]

                future = asyncio.get_event_loop().create_future()
                _pending_async[cache_key] = future
                try:
                    result = await func(*args, **kwargs)
                    future.set_result(result)
                    return result
                except Exception as e:
                    future.set_exception(e)
                    raise
                finally:
                    _pending_async.pop(cache_key, None)

            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                with _sync_lock:
                    if cache_key in _pending_sync:
                        event, result_holder = _pending_sync[cache_key]
                        waiting = True
                    else:
                        waiting = False

                if waiting:
                    event.wait(timeout=_ttl_seconds)
                    if result_holder.get('error'):
                        raise result_holder['error']
                    return result_holder.get('result')

                event = threading.Event()
                result_holder = {}
                with _sync_lock:
                    _pending_sync[cache_key] = (event, result_holder)

                try:
                    result = func(*args, **kwargs)
                    result_holder['result'] = result
                    return result
                except Exception as e:
                    result_holder['error'] = e
                    raise
                finally:
                    event.set()
                    with _sync_lock:
                        _pending_sync.pop(cache_key, None)

            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/locked.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/rate_limit.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Rate limiting decorators.

- rate_limit: Fixed-window rate limiting.
- slice_rate_limit: Sliding-window rate limiting.
"""
import functools
import time

from nb_cache._compat import is_coroutine_function
from nb_cache.exceptions import RateLimitError
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.ttl import ttl_to_seconds


def rate_limit(limit, period, ttl=None, action=None, prefix="rate_limit",
               key=None, backend=None):
    """Fixed-window rate limiter.

    Args:
        limit: Maximum number of calls allowed in the period.
        period: Time window in seconds.
        ttl: TTL for the counter key. Defaults to period.
        action: Callable to invoke when rate is exceeded (instead of raising).
        prefix: Key prefix.
        key: Key template.
        backend: Backend instance.
    """
    _period = ttl_to_seconds(period) or 60
    _ttl_seconds = ttl_to_seconds(ttl) if ttl else _period

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                rate_key = "__rl__:{}".format(cache_key)

                count = await be.incr(rate_key)
                if count == 1:
                    await be.expire(rate_key, int(_period))

                if count > limit:
                    if action:
                        return action(*args, **kwargs)
                    raise RateLimitError(
                        "Rate limit exceeded: {} calls in {}s".format(limit, _period))

                return await func(*args, **kwargs)

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                rate_key = "__rl__:{}".format(cache_key)

                count = be.incr_sync(rate_key)
                if count == 1:
                    be.expire_sync(rate_key, int(_period))

                if count > limit:
                    if action:
                        return action(*args, **kwargs)
                    raise RateLimitError(
                        "Rate limit exceeded: {} calls in {}s".format(limit, _period))

                return func(*args, **kwargs)

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            return sync_wrapper

    return decorator


def slice_rate_limit(limit, period, key=None, action=None,
                     prefix="srl", backend=None):
    """Sliding-window rate limiter using multiple time slices.

    Divides the period into slices and tracks counts per slice for
    a smoother rate limiting behavior.

    Args:
        limit: Maximum number of calls allowed in the period.
        period: Time window in seconds.
        key: Key template.
        action: Callable to invoke when rate is exceeded.
        prefix: Key prefix.
        backend: Backend instance.
    """
    _period = ttl_to_seconds(period) or 60
    _num_slices = 10
    _slice_duration = _period / _num_slices

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        def _current_slice_key(cache_key):
            now = time.time()
            slice_index = int(now / _slice_duration) % _num_slices
            return "__srl__:{}:{}".format(cache_key, slice_index)

        def _all_slice_keys(cache_key):
            now = time.time()
            current_idx = int(now / _slice_duration)
            keys = []
            for i in range(_num_slices):
                idx = (current_idx - i) % _num_slices
                keys.append("__srl__:{}:{}".format(cache_key, idx))
            return keys

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                slice_keys = _all_slice_keys(cache_key)
                values = await be.get_many(*slice_keys)
                total = sum(int(v) for v in values if v is not None)

                if total >= limit:
                    if action:
                        return action(*args, **kwargs)
                    raise RateLimitError(
                        "Sliding rate limit exceeded: {} calls in {}s".format(limit, _period))

                current_key = _current_slice_key(cache_key)
                await be.incr(current_key)
                await be.expire(current_key, int(_period))

                return await func(*args, **kwargs)

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)

                slice_keys = _all_slice_keys(cache_key)
                values = be.get_many_sync(*slice_keys)
                total = sum(int(v) for v in values if v is not None)

                if total >= limit:
                    if action:
                        return action(*args, **kwargs)
                    raise RateLimitError(
                        "Sliding rate limit exceeded: {} calls in {}s".format(limit, _period))

                current_key = _current_slice_key(cache_key)
                be.incr_sync(current_key)
                be.expire_sync(current_key, int(_period))

                return func(*args, **kwargs)

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/rate_limit.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/soft.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Soft-expiration cache decorator.

Values have a soft TTL and a hard TTL. After soft TTL, the value is refreshed
on the next access but the stale value is returned. After hard TTL, the value
is truly gone and must be recomputed.
"""
import asyncio
import functools
import threading
import time

from nb_cache._compat import is_coroutine_function, create_task
from nb_cache.condition import get_cache_condition
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.ttl import ttl_to_seconds

_SOFT_META_PREFIX = "__soft_ts__:"


def soft(ttl, key=None, soft_ttl=None, condition=None, prefix="soft",
         tags=(), backend=None, serializer=None):
    """Cache with soft expiration.

    Args:
        ttl: Hard TTL - maximum time the value lives.
        soft_ttl: Soft TTL - after this, value is refreshed in background.
            Defaults to ttl / 2.
        condition: Cache condition callable.
    """
    _condition = get_cache_condition(condition)
    _serializer = serializer or default_serializer
    _ttl_seconds = ttl_to_seconds(ttl)
    _soft_ttl = ttl_to_seconds(soft_ttl) if soft_ttl else (_ttl_seconds / 2 if _ttl_seconds else None)

    def decorator(func):
        _key_template = get_cache_key_template(func, key, prefix)
        _backend_ref = [backend]
        _refreshing = set()

        def _get_backend():
            from nb_cache.wrapper import _get_default_backend
            return _backend_ref[0] or _get_default_backend()

        if is_coroutine_function(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                meta_key = _SOFT_META_PREFIX + cache_key

                raw = await be.get(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        ts_raw = await be.get(meta_key)
                        if ts_raw is not None:
                            try:
                                set_time = float(ts_raw)
                            except (ValueError, TypeError):
                                set_time = 0
                            elapsed = time.time() - set_time
                            if _soft_ttl and elapsed > _soft_ttl and cache_key not in _refreshing:
                                _refreshing.add(cache_key)

                                async def _refresh():
                                    try:
                                        result = await func(*args, **kwargs)
                                        if _condition(result):
                                            encoded = _serializer.encode(result)
                                            await be.set(cache_key, encoded, ttl=_ttl_seconds)
                                            await be.set(meta_key, str(time.time()).encode(), ttl=_ttl_seconds)
                                    finally:
                                        _refreshing.discard(cache_key)

                                create_task(_refresh())
                        return val

                result = await func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    await be.set(cache_key, encoded, ttl=_ttl_seconds)
                    await be.set(meta_key, str(time.time()).encode(), ttl=_ttl_seconds)
                return result

            async_wrapper._cache_key_template = _key_template
            async_wrapper._cache_backend_ref = _backend_ref
            async_wrapper._cache_tags = tags
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                be = _get_backend()
                cache_key = get_cache_key(func, _key_template, args, kwargs)
                meta_key = _SOFT_META_PREFIX + cache_key

                raw = be.get_sync(cache_key)
                if raw is not None:
                    val = _serializer.decode(raw)
                    if val is not _SENTINEL:
                        ts_raw = be.get_sync(meta_key)
                        if ts_raw is not None:
                            try:
                                set_time = float(ts_raw)
                            except (ValueError, TypeError):
                                set_time = 0
                            elapsed = time.time() - set_time
                            if _soft_ttl and elapsed > _soft_ttl and cache_key not in _refreshing:
                                _refreshing.add(cache_key)

                                def _refresh():
                                    try:
                                        result = func(*args, **kwargs)
                                        if _condition(result):
                                            encoded = _serializer.encode(result)
                                            be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                                            be.set_sync(meta_key, str(time.time()).encode(), ttl=_ttl_seconds)
                                    finally:
                                        _refreshing.discard(cache_key)

                                t = threading.Thread(target=_refresh, daemon=True)
                                t.start()
                        return val

                result = func(*args, **kwargs)
                if _condition(result):
                    encoded = _serializer.encode(result)
                    be.set_sync(cache_key, encoded, ttl=_ttl_seconds)
                    be.set_sync(meta_key, str(time.time()).encode(), ttl=_ttl_seconds)
                return result

            sync_wrapper._cache_key_template = _key_template
            sync_wrapper._cache_backend_ref = _backend_ref
            sync_wrapper._cache_tags = tags
            return sync_wrapper

    return decorator

`````

--- **end of file: nb_cache/decorators/soft.py** (project: nb_cache) --- 

---


--- **start of file: nb_cache/decorators/__init__.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
from nb_cache.decorators.cache import cache
from nb_cache.decorators.early import early
from nb_cache.decorators.soft import soft
from nb_cache.decorators.failover import failover
from nb_cache.decorators.hit import hit
from nb_cache.decorators.locked import locked, thunder_protection
from nb_cache.decorators.circuit_breaker import circuit_breaker
from nb_cache.decorators.rate_limit import rate_limit, slice_rate_limit
from nb_cache.decorators.bloom import bloom, dual_bloom
from nb_cache.decorators.iterator import iterator

__all__ = [
    'cache', 'early', 'soft', 'failover', 'hit',
    'locked', 'thunder_protection',
    'circuit_breaker', 'rate_limit', 'slice_rate_limit',
    'bloom', 'dual_bloom', 'iterator',
]

`````

--- **end of file: nb_cache/decorators/__init__.py** (project: nb_cache) --- 

---

# markdown content namespace: nb_cache examples 


## nb_cache File Tree (relative dir: `examples`)


`````

└── examples
    ├── __init__.py
    └── ex1.py

`````

---


## nb_cache (relative dir: `examples`)  Included Files (total: 2 files)


- `examples/ex1.py`

- `examples/__init__.py`


---


--- **start of file: examples/ex1.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""nb_cache 综合用法演示

体现:
  1. 内存缓存 / Redis缓存 / Redis+内存双缓存
  2. 同步函数 / 异步函数 共用同一装饰器
  3. 简单自定义 key / 复杂函数参数自动生成 key / hash格式key
"""
import asyncio
import time
import logging
from nb_cache import Cache

# import nb_log
# nb_log.get_logger('nb_cache')
logger = logging.getLogger("nb_cache.key")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# ================================================================
#  一、内存缓存（mem://）
# ================================================================
mem_cache = Cache().setup("mem://")

# ---------- 同步函数 + 自动生成 key ----------
@mem_cache.cache(ttl=10)
def get_user_from_db(user_id):
    """不指定 key，自动用 函数全名:user_id=xxx 作为缓存 key"""
    print("  [MEM][SYNC] 查询数据库 user_id={}".format(user_id))
    return {"id": user_id, "name": "张三"}


# ---------- 异步函数 + 简单自定义 key ----------
@mem_cache.cache(ttl=10, key="{user_id}")
async def get_user_async(user_id):
    """用 {user_id} 模板，缓存 key 就是 user_id 的值本身（如 '1001'）"""
    print("  [MEM][ASYNC] 异步查询 user_id={}".format(user_id))
    await asyncio.sleep(0.01)
    return {"id": user_id, "name": "李四"}


# ---------- 同步函数 + 复杂自定义 key（hash） ----------
@mem_cache.cache(ttl=10, key="order:{user_id}:{filters:hash}")
def query_orders(user_id, filters, page=1):
    """复杂 key: filters 是 dict，用 :hash 格式取 md5 前8位，避免 key 过长"""
    print("  [MEM][SYNC] 查询订单 user_id={} filters={} page={}".format(user_id, filters, page))
    return [{"order": 1001, "amount": 99.9}]


# ---------- 异步函数 + lock 防缓存击穿 ----------
@mem_cache.cache(ttl=10, lock=True)
async def get_hot_ranking():
    """热点数据加锁，并发请求时只有一个真正执行查询"""
    print("  [MEM][ASYNC][LOCK] 计算热门排行榜...")
    await asyncio.sleep(0.01)
    return ["item_a", "item_b", "item_c"]


# ================================================================
#  二、Redis 缓存（redis://）
# ================================================================
redis_ok = False
try:
    redis_cache = Cache().setup("redis://localhost:6379/0")
    redis_cache.ping_sync()
    redis_ok = True
    print("[OK] Redis 已连接\n")
except Exception as e:
    print("[SKIP] Redis 不可用 ({}), 跳过 Redis 示例\n".format(e))


# ---------- 同步函数 + 自动 key ----------
@redis_cache.cache(ttl=30)
def get_product_sync(product_id):
    print("  [REDIS][SYNC] 查询商品 product_id={}".format(product_id))
    return {"id": product_id, "title": "MacBook Pro", "price": 14999}


# ---------- 异步函数 + 简单自定义 key ----------
@redis_cache.cache(ttl=30, key="prod:{product_id}")
async def get_product_async(product_id):
    print("  [REDIS][ASYNC] 异步查询商品 product_id={}".format(product_id))
    await asyncio.sleep(0.01)
    return {"id": product_id, "title": "iPhone", "price": 7999}


# ---------- 同步 + 复杂 key + lock ----------
@redis_cache.cache(ttl=60, key="search:{keyword:lower}:{options:hash}", lock=True)
def search_products(keyword, options):
    """keyword 转小写做 key, options 用 hash, 加锁防击穿"""
    print("  [REDIS][SYNC][LOCK] 搜索: keyword={} options={}".format(keyword, options))
    return [{"id": 1, "title": keyword}]

# ----- 同步 + key 模板支持点号访问字典/对象属性 ----------
# {user.id} 和 {user.name} 会自动从 user 参数里取 user['id'] 和 user['name']
@redis_cache.cache(ttl=60, key="user:{user.id}:{user.name}")
def get_user(user):
    print("  [REDIS][SYNC] 查询用户 user.id={} user.name={}".format(user['id'], user['name']))
    return {"id": user['id'], "name": user['name']}


# ---- 异步 + key 通过自定义函数生成（适合复杂逻辑，无法用模板表达的情况）----------
def gen_user_key(user):
    """自定义 key 生成函数，接收和被装饰函数相同的参数，返回 key 字符串"""
    return "user:{}:{}".format(user['id'], user['name'])

@redis_cache.cache(ttl=60, key=gen_user_key)
async def get_user_async_gen_key(user):
    print("  [REDIS][ASYNC] 查询用户 user.id={} user.name={}".format(user['id'], user['name']))
    await asyncio.sleep(0.01)
    return {"id": user['id'], "name": user['name']}

# ================================================================
#  三、Redis + 内存双缓存（dual://）
# ================================================================
dual_ok = False
try:
    dual_cache = Cache().setup("dual://localhost:6379/0?memory_size=500&local_ttl=5")
    dual_cache.ping_sync()
    dual_ok = True
    print("[OK] Dual (Redis+内存) 已连接\n")
except Exception as e:
    print("[SKIP] Dual 不可用 ({}), 跳过双缓存示例\n".format(e))


# ---------- 同步 + 自动 key ----------
@dual_cache.cache(ttl=60)
def get_config_sync(config_key):
    """双缓存: 先查内存(~0ms)，miss则查Redis(~1ms)，写入时双写"""
    print("  [DUAL][SYNC] 读取配置 config_key={}".format(config_key))
    return {"key": config_key, "value": "some_config_value"}


# ---------- 异步 + 复杂 key ----------
@dual_cache.cache(ttl=60, key="session:{user_id}:{token:hash}")
async def get_session_async(user_id, token):
    print("  [DUAL][ASYNC] 查询会话 user_id={} token={}...".format(user_id, token[:8]))
    await asyncio.sleep(0.01)
    return {"user_id": user_id, "role": "admin", "login_time": "2026-02-28 10:00"}


# ================================================================
#  运行演示
# ================================================================
def demo_memory():
    print("=" * 60)
    print("【内存缓存】")
    print("=" * 60)

    print("\n--- 同步函数 (自动生成 key) ---")
    r1 = get_user_from_db(1001)
    print("  结果:", r1)
    r2 = get_user_from_db(1001)
    print("  结果(应走缓存，无SQL打印):", r2)
    r3 = get_user_from_db(1002)
    print("  结果(不同参数，重新查询):", r3)

    print("\n--- 同步函数 (复杂 key: hash格式) ---")
    f1 = {"status": "paid", "min_amount": 100}
    r4 = query_orders(1001, f1, page=1)
    print("  结果:", r4)
    r5 = query_orders(1001, f1, page=1)
    print("  结果(缓存命中):", r5)
    f2 = {"status": "shipped"}
    r6 = query_orders(1001, f2, page=1)
    print("  结果(filters不同，hash不同，重新查询):", r6)


async def demo_memory_async():
    print("\n--- 异步函数 (简单自定义 key: {user_id}) ---")
    r1 = await get_user_async(2001)
    print("  结果:", r1)
    r2 = await get_user_async(2001)
    print("  结果(缓存命中):", r2)

    print("\n--- 异步函数 (lock防击穿) ---")
    r3 = await get_hot_ranking()
    print("  结果:", r3)
    r4 = await get_hot_ranking()
    print("  结果(缓存命中):", r4)

    print("\n--- 异步函数 (自定义函数生成key) ---")
    r5 = await get_user_async_gen_key({"id": 2001, "name": "张三","description": "这是一个用户"})
    print("  结果:", r5)
    r6 = await get_user_async_gen_key({"id": 2001, "name": "张三","description": "这是一个用户"})
    print("  结果(缓存命中):", r6)

    print("\n--- 异步函数 (通过点号 . 访问一个对象或者字典的属性) ---")
    r7 =  get_user({"id": 2001, "name": "张三","description": "这是一个用户"})
    print("  结果:", r7)
    r8 =  get_user({"id": 2001, "name": "张三","description": "这是一个用户" , "age": 18})
    print("  结果(缓存命中):", r8)


def demo_redis():
    if not redis_ok:
        return
    print("\n" + "=" * 60)
    print("【Redis缓存】")
    print("=" * 60)

    print("\n--- 同步函数 (自动 key) ---")
    r1 = get_product_sync(5001)
    print("  结果:", r1)
    r2 = get_product_sync(5001)
    print("  结果(缓存命中):", r2)

    print("\n--- 同步函数 (复杂 key + lock) ---")
    opts = {"category": "electronics", "sort": "price_asc"}
    r3 = search_products("Laptop", opts)
    print("  结果:", r3)
    r4 = search_products("Laptop", opts)
    print("  结果(缓存命中):", r4)
    r5 = search_products("LAPTOP", opts)
    print("  结果(keyword转lower相同，缓存命中):", r5)


async def demo_redis_async():
    if not redis_ok:
        return
    print("\n--- 异步函数 (简单自定义 key) ---")
    r1 = await get_product_async(6001)
    print("  结果:", r1)
    r2 = await get_product_async(6001)
    print("  结果(缓存命中):", r2)


def demo_dual():
    if not dual_ok:
        return
    print("\n" + "=" * 60)
    print("【Redis+内存 双缓存】")
    print("=" * 60)

    print("\n--- 同步函数 (自动 key) ---")
    r1 = get_config_sync("app.max_retry")
    print("  结果:", r1)
    print("  第2次(内存L1命中):")
    r2 = get_config_sync("app.max_retry")
    print("  结果:", r2)


async def demo_dual_async():
    if not dual_ok:
        return
    print("\n--- 异步函数 (复杂 key: hash格式) ---")
    token = "abc123def456ghi789jkl"
    r1 = await get_session_async(9001, token)
    print("  结果:", r1)
    r2 = await get_session_async(9001, token)
    print("  结果(双缓存命中):", r2)


def main():
    demo_memory()
    asyncio.get_event_loop().run_until_complete(demo_memory_async())
    demo_redis()
    asyncio.get_event_loop().run_until_complete(demo_redis_async())
    demo_dual()
    asyncio.get_event_loop().run_until_complete(demo_dual_async())

    print("\n" + "=" * 60)
    print("演示完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()

`````

--- **end of file: examples/ex1.py** (project: nb_cache) --- 

---


--- **start of file: examples/__init__.py** (project: nb_cache) --- 

`````python

`````

--- **end of file: examples/__init__.py** (project: nb_cache) --- 

---

# markdown content namespace: nb_cache 测试用例 


## nb_cache File Tree (relative dir: `tests/ai_codes`)


`````

└── tests
    └── ai_codes
        └── test_core.py

`````

---


## nb_cache (relative dir: `tests/ai_codes`)  Included Files (total: 1 files)


- `tests/ai_codes/test_core.py`


---


--- **start of file: tests/ai_codes/test_core.py** (project: nb_cache) --- 

`````python
# -*- coding: utf-8 -*-
"""Core functionality tests for nb_cache."""
import asyncio
import time
import pytest

from nb_cache import Cache, NOT_NONE, ttl_to_seconds, MemoryBackend
from nb_cache.serialize import default_serializer, _SENTINEL
from nb_cache.key import get_cache_key, get_cache_key_template
from nb_cache.ttl import ttl_to_seconds as _ttl
from nb_cache.exceptions import LockedError, RateLimitError, CircuitBreakerOpen


# ============================================================
# TTL parsing tests
# ============================================================

class TestTTLParsing:
    def test_int(self):
        assert _ttl(60) == 60.0

    def test_float(self):
        assert _ttl(1.5) == 1.5

    def test_none(self):
        assert _ttl(None) is None

    def test_zero(self):
        assert _ttl(0) is None

    def test_timedelta(self):
        from datetime import timedelta
        assert _ttl(timedelta(hours=1)) == 3600.0

    def test_string_hours(self):
        assert _ttl("1h") == 3600.0

    def test_string_minutes(self):
        assert _ttl("30m") == 1800.0

    def test_string_combined(self):
        assert _ttl("1d12h30m10s") == 131410.0

    def test_string_seconds(self):
        assert _ttl("45s") == 45.0

    def test_string_numeric(self):
        assert _ttl("120") == 120.0

    def test_callable(self):
        assert _ttl(lambda: 42) == 42.0


# ============================================================
# Key generation tests
# ============================================================

class TestKeyGeneration:
    def test_auto_key(self):
        def my_func(a, b):
            pass
        key = get_cache_key(my_func, None, (1, 2), {})
        assert "my_func" in key
        assert "a=1" in key
        assert "b=2" in key

    def test_template_key(self):
        def my_func(user_id, name):
            pass
        template = "{user_id}:{name}"
        key = get_cache_key(my_func, template, (123, "alice"), {})
        assert key == "123:alice"

    def test_key_template_generation(self):
        def my_func(x, y):
            pass
        template = get_cache_key_template(my_func, prefix="test")
        assert "test" in template
        assert "{x}" in template
        assert "{y}" in template


# ============================================================
# Serialization tests
# ============================================================

class TestSerialization:
    def test_encode_decode(self):
        obj = {"key": "value", "num": 42}
        encoded = default_serializer.encode(obj)
        decoded = default_serializer.decode(encoded)
        assert decoded == obj

    def test_decode_none(self):
        result = default_serializer.decode(None)
        assert result is _SENTINEL

    def test_various_types(self):
        for val in [42, "hello", [1, 2, 3], {"a": 1}, (1, 2), True, None]:
            encoded = default_serializer.encode(val)
            decoded = default_serializer.decode(encoded)
            assert decoded == val


# ============================================================
# Memory backend tests
# ============================================================

class TestMemoryBackend:
    def setup_method(self):
        self.be = MemoryBackend(size=100)
        self.be.init_sync()

    def teardown_method(self):
        self.be.close_sync()

    def test_get_set(self):
        self.be.set_sync("k1", "v1")
        assert self.be.get_sync("k1") == "v1"

    def test_get_missing(self):
        assert self.be.get_sync("missing") is None

    def test_delete(self):
        self.be.set_sync("k1", "v1")
        self.be.delete_sync("k1")
        assert self.be.get_sync("k1") is None

    def test_exists(self):
        self.be.set_sync("k1", "v1")
        assert self.be.exists_sync("k1") is True
        assert self.be.exists_sync("k2") is False

    def test_ttl_expiry(self):
        self.be.set_sync("k1", "v1", ttl=0.2)
        assert self.be.get_sync("k1") == "v1"
        time.sleep(0.3)
        assert self.be.get_sync("k1") is None

    def test_incr(self):
        assert self.be.incr_sync("counter") == 1
        assert self.be.incr_sync("counter") == 2
        assert self.be.incr_sync("counter", 5) == 7

    def test_clear(self):
        self.be.set_sync("k1", "v1")
        self.be.set_sync("k2", "v2")
        self.be.clear_sync()
        assert self.be.get_sync("k1") is None
        assert self.be.get_sync("k2") is None

    def test_get_many(self):
        self.be.set_sync("a", 1)
        self.be.set_sync("b", 2)
        result = self.be.get_many_sync("a", "b", "c")
        assert result == [1, 2, None]

    def test_set_many(self):
        self.be.set_many_sync({"x": 10, "y": 20})
        assert self.be.get_sync("x") == 10
        assert self.be.get_sync("y") == 20

    def test_lru_eviction(self):
        be = MemoryBackend(size=3)
        be.init_sync()
        be.set_sync("a", 1)
        be.set_sync("b", 2)
        be.set_sync("c", 3)
        be.set_sync("d", 4)  # should evict 'a'
        assert be.get_sync("a") is None
        assert be.get_sync("d") == 4

    def test_lock(self):
        assert self.be.set_lock_sync("res", 5) is True
        assert self.be.is_locked_sync("res") is True
        assert self.be.set_lock_sync("res", 5) is False
        self.be.unlock_sync("res")
        assert self.be.is_locked_sync("res") is False

    def test_scan(self):
        self.be.set_sync("user:1", "a")
        self.be.set_sync("user:2", "b")
        self.be.set_sync("post:1", "c")
        keys = self.be.scan_sync("user:*")
        assert sorted(keys) == ["user:1", "user:2"]

    def test_delete_match(self):
        self.be.set_sync("user:1", "a")
        self.be.set_sync("user:2", "b")
        self.be.set_sync("post:1", "c")
        self.be.delete_match_sync("user:*")
        assert self.be.get_sync("user:1") is None
        assert self.be.get_sync("post:1") == "c"

    def test_expire(self):
        self.be.set_sync("k1", "v1")
        self.be.expire_sync("k1", 0.2)
        assert self.be.get_sync("k1") == "v1"
        time.sleep(0.3)
        assert self.be.get_sync("k1") is None

    def test_get_expire(self):
        self.be.set_sync("k1", "v1", ttl=10)
        remaining = self.be.get_expire_sync("k1")
        assert remaining is not None
        assert 9 <= remaining <= 10


# ============================================================
# Async memory backend tests
# ============================================================

class TestMemoryBackendAsync:
    def setup_method(self):
        self.be = MemoryBackend(size=100)
        self.be.init_sync()

    def teardown_method(self):
        self.be.close_sync()

    def test_async_get_set(self):
        async def _test():
            await self.be.set("k1", "v1")
            val = await self.be.get("k1")
            assert val == "v1"
        asyncio.get_event_loop().run_until_complete(_test())

    def test_async_lock(self):
        async def _test():
            assert await self.be.set_lock("res", 5) is True
            assert await self.be.is_locked("res") is True
            await self.be.unlock("res")
            assert await self.be.is_locked("res") is False
        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# Cache decorator tests (sync)
# ============================================================

class TestCacheDecoratorSync:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")  # setup() 自动初始化，无需调用 init_sync()
        self.call_count = 0

    def test_basic_cache(self):
        @self.c.cache(ttl=60)
        def get_data(x):
            self.call_count += 1
            return x * 2

        assert get_data(5) == 10
        assert self.call_count == 1
        assert get_data(5) == 10
        assert self.call_count == 1  # served from cache
        assert get_data(6) == 12
        assert self.call_count == 2  # different args

    def test_cache_with_lock(self):
        @self.c.cache(ttl=60, lock=True)
        def get_data(x):
            self.call_count += 1
            return x * 3

        assert get_data(5) == 15
        assert self.call_count == 1
        assert get_data(5) == 15
        assert self.call_count == 1

    def test_cache_ttl_expiry(self):
        @self.c.cache(ttl=0.3)
        def get_data(x):
            self.call_count += 1
            return x

        assert get_data(1) == 1
        assert self.call_count == 1
        time.sleep(0.4)
        assert get_data(1) == 1
        assert self.call_count == 2  # cache expired


# ============================================================
# Cache decorator tests (async)
# ============================================================

class TestCacheDecoratorAsync:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")
        self.call_count = 0

    def test_async_cache(self):
        @self.c.cache(ttl=60)
        async def get_data(x):
            self.call_count += 1
            return x * 2

        loop = asyncio.get_event_loop()
        assert loop.run_until_complete(get_data(5)) == 10
        assert self.call_count == 1
        assert loop.run_until_complete(get_data(5)) == 10
        assert self.call_count == 1


# ============================================================
# Failover decorator tests
# ============================================================

class TestFailoverSync:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")
        self.call_count = 0
        self.should_fail = False

    def test_failover(self):
        @self.c.failover(ttl=60, exceptions=(ValueError,))
        def get_data(x):
            self.call_count += 1
            if self.should_fail:
                raise ValueError("fail")
            return x * 2

        assert get_data(5) == 10
        self.should_fail = True
        assert get_data(5) == 10  # returns cached value

    def test_failover_no_cache(self):
        @self.c.failover(ttl=60, exceptions=(ValueError,))
        def get_data(x):
            raise ValueError("fail")

        with pytest.raises(ValueError):
            get_data(99)  # no cached value, re-raises


# ============================================================
# Rate limit tests
# ============================================================

class TestRateLimitSync:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")

    def test_rate_limit(self):
        @self.c.rate_limit(limit=3, period=60)
        def api_call():
            return "ok"

        assert api_call() == "ok"
        assert api_call() == "ok"
        assert api_call() == "ok"
        with pytest.raises(RateLimitError):
            api_call()  # 4th call exceeds limit


# ============================================================
# Locked decorator tests
# ============================================================

class TestLockedSync:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")

    def test_locked_wait_false(self):
        @self.c.locked(ttl=5, wait=False)
        def critical():
            return "done"

        assert critical() == "done"


# ============================================================
# Lock context manager tests
# ============================================================

class TestLockContextManager:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")

    def test_sync_lock(self):
        with self.c.lock("test_resource", ttl=5):
            assert self.c.backend.is_locked_sync("test_resource") is True
        assert self.c.backend.is_locked_sync("test_resource") is False

    def test_async_lock(self):
        async def _test():
            async with self.c.alock("test_resource", ttl=5):
                assert await self.c.backend.is_locked("test_resource") is True
            assert await self.c.backend.is_locked("test_resource") is False

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# Transaction tests
# ============================================================

class TestTransaction:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")

    def test_sync_transaction_commit(self):
        with self.c.transaction() as tx:
            tx.set("k1", "v1", ttl=60)
            tx.set("k2", "v2", ttl=60)
        assert self.c.get_sync("k1") == "v1"
        assert self.c.get_sync("k2") == "v2"

    def test_sync_transaction_rollback(self):
        try:
            with self.c.transaction() as tx:
                tx.set("k3", "v3")
                raise RuntimeError("oops")
        except RuntimeError:
            pass
        assert self.c.get_sync("k3") is None

    def test_async_transaction(self):
        async def _test():
            async with self.c.transaction() as tx:
                tx.set("ak1", "av1")
                tx.set("ak2", "av2")
            assert await self.c.get("ak1") == "av1"

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# Cache wrapper direct operations tests
# ============================================================

class TestCacheWrapperOperations:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")

    def test_set_get_sync(self):
        self.c.set_sync("key1", "val1", ttl=60)
        assert self.c.get_sync("key1") == "val1"

    def test_delete_sync(self):
        self.c.set_sync("key1", "val1")
        self.c.delete_sync("key1")
        assert self.c.get_sync("key1") is None

    def test_exists_sync(self):
        self.c.set_sync("key1", "val1")
        assert self.c.exists_sync("key1") is True
        assert self.c.exists_sync("key_missing") is False

    def test_incr_sync(self):
        assert self.c.incr_sync("cnt") == 1
        assert self.c.incr_sync("cnt") == 2

    def test_clear_sync(self):
        self.c.set_sync("a", 1)
        self.c.set_sync("b", 2)
        self.c.clear_sync()
        assert self.c.get_sync("a") is None

    def test_async_operations(self):
        async def _test():
            await self.c.set("akey", "aval", ttl=60)
            assert await self.c.get("akey") == "aval"
            assert await self.c.exists("akey") is True
            await self.c.delete("akey")
            assert await self.c.get("akey") is None

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# Iterator cache tests
# ============================================================

class TestIteratorCache:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")
        self.call_count = 0

    def test_sync_generator_cache(self):
        @self.c.iterator(ttl=60)
        def gen_items():
            self.call_count += 1
            for i in range(3):
                yield i

        result1 = list(gen_items())
        assert result1 == [0, 1, 2]
        assert self.call_count == 1

        result2 = list(gen_items())
        assert result2 == [0, 1, 2]
        assert self.call_count == 1  # from cache


# ============================================================
# URL parsing tests
# ============================================================

class TestURLParsing:
    def test_mem_url(self):
        c = Cache()
        c.setup("mem://")
        assert c.is_setup
        assert isinstance(c.backend, MemoryBackend)

    def test_setup_with_prefix(self):
        c = Cache()
        c.setup("mem://", prefix="myapp")
        assert c.is_setup

    def test_setup_auto_init(self):
        """setup() should auto-initialize — no need to call init_sync() manually."""
        c = Cache()
        c.setup("mem://")
        c.set_sync("auto_init_test", "ok")
        assert c.get_sync("auto_init_test") == "ok"


# ============================================================
# Key template tests — dot-access and callable key
# ============================================================

class TestKeyTemplates:
    def setup_method(self):
        self.c = Cache()
        self.c.setup("mem://")
        self.call_count = 0

    # --- dot-access ---

    def test_dot_access_dict(self):
        """key='{user.id}:{user.name}' reads user['id'] and user['name']."""
        @self.c.cache(ttl=60, key="{user.id}:{user.name}")
        def get_user(user):
            self.call_count += 1
            return user

        u1 = {"id": 1, "name": "Alice", "extra": "ignored"}
        u2 = {"id": 1, "name": "Alice", "extra": "different_extra"}

        r1 = get_user(u1)
        assert r1 == u1
        assert self.call_count == 1

        r2 = get_user(u2)
        assert self.call_count == 1  # same id+name → cache hit despite different extra

    def test_dot_access_different_values(self):
        """Different attribute values produce different cache keys."""
        @self.c.cache(ttl=60, key="{user.id}")
        def get_user(user):
            self.call_count += 1
            return user['id']

        get_user({"id": 10})
        get_user({"id": 20})
        assert self.call_count == 2  # different ids, two cache misses

    def test_dot_access_with_hash(self):
        """Dot-access combined with :hash modifier."""
        @self.c.cache(ttl=60, key="{obj.data:hash}")
        def get_result(obj):
            self.call_count += 1
            return obj['data']

        get_result({"data": [1, 2, 3]})
        get_result({"data": [1, 2, 3]})
        assert self.call_count == 1

    def test_dot_access_with_lower(self):
        """Dot-access combined with :lower modifier."""
        @self.c.cache(ttl=60, key="{user.name:lower}")
        def get_user(user):
            self.call_count += 1
            return user

        get_user({"name": "Alice"})
        get_user({"name": "ALICE"})
        assert self.call_count == 1  # both map to "alice"

    # --- callable key ---

    def test_callable_key(self):
        """key=callable receives the same args as the decorated function."""
        def make_key(user_id, role):
            return "perm:{}:{}".format(role, user_id)

        @self.c.cache(ttl=60, key=make_key)
        def check(user_id, role):
            self.call_count += 1
            return True

        check(1, "admin")
        check(1, "admin")
        assert self.call_count == 1  # cache hit

        check(1, "viewer")
        assert self.call_count == 2  # different role → different key

    def test_callable_key_complex_logic(self):
        """Callable key can encode business logic that templates cannot."""
        def make_key(items, page):
            sorted_ids = sorted(i['id'] for i in items)
            return "list:{}:p{}".format("-".join(str(x) for x in sorted_ids), page)

        @self.c.cache(ttl=60, key=make_key)
        def get_list(items, page):
            self.call_count += 1
            return items

        items_a = [{"id": 3}, {"id": 1}, {"id": 2}]
        items_b = [{"id": 1}, {"id": 2}, {"id": 3}]

        get_list(items_a, 1)
        get_list(items_b, 1)
        assert self.call_count == 1  # sorted IDs equal → same key → cache hit


# ============================================================
# condition 参数测试
# ============================================================

class TestCacheCondition:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_not_none_skips_none(self):
        """NOT_NONE：返回 None 时不缓存，下次仍会调用函数。"""
        @self.c.cache(ttl=60, condition=NOT_NONE)
        def get_data(x):
            self.call_count += 1
            return None if x == 0 else x

        get_data(0)
        get_data(0)
        assert self.call_count == 2  # None 不缓存，每次都执行

        get_data(1)
        get_data(1)
        assert self.call_count == 3  # 非 None，第二次走缓存

    def test_custom_condition_lambda(self):
        """自定义条件：只缓存 status=='ok' 的结果。"""
        @self.c.cache(ttl=60, condition=lambda r: r is not None and r.get("status") == "ok")
        def get_order(order_id):
            self.call_count += 1
            return {"status": "ok", "id": order_id} if order_id > 0 else {"status": "fail"}

        get_order(1)  # ok，应缓存
        get_order(1)
        assert self.call_count == 1  # 命中缓存

        get_order(-1)  # fail，不缓存
        get_order(-1)
        assert self.call_count == 3  # 每次都执行

    def test_always_cache_including_none(self):
        """condition=lambda r: True：包括 None 都缓存。"""
        @self.c.cache(ttl=60, condition=lambda r: True)
        def might_none(x):
            self.call_count += 1
            return None

        might_none(1)
        might_none(1)
        assert self.call_count == 1  # None 也被缓存，第二次命中


# ============================================================
# failover 装饰器测试
# ============================================================

class TestFailover:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0
        self.should_fail = False

    def test_failover_returns_cached_on_exception(self):
        """函数抛异常时，failover 返回缓存的旧值。"""
        @self.c.failover(ttl=60, exceptions=(ValueError,))
        def get_data(x):
            self.call_count += 1
            if self.should_fail:
                raise ValueError("fail")
            return x * 2

        assert get_data(5) == 10
        self.should_fail = True
        assert get_data(5) == 10  # 返回缓存旧值
        assert self.call_count == 2  # 第二次尝试执行了（异常后才回退）

    def test_failover_reraises_when_no_cache(self):
        """没有缓存时，failover 不能回退，直接抛出原始异常。"""
        @self.c.failover(ttl=60, exceptions=(RuntimeError,))
        def always_fail():
            raise RuntimeError("no cache available")

        with pytest.raises(RuntimeError):
            always_fail()

    def test_failover_async(self):
        """异步函数 failover。"""
        should_fail = [False]

        @self.c.failover(ttl=60, exceptions=(ValueError,))
        async def get_async(x):
            self.call_count += 1
            if should_fail[0]:
                raise ValueError("async fail")
            return x * 3

        async def _test():
            assert await get_async(4) == 12
            should_fail[0] = True
            assert await get_async(4) == 12  # 回退到缓存

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# early 装饰器测试
# ============================================================

class TestEarlyRefresh:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_early_basic_cache(self):
        """early 在 TTL 内正常命中缓存。"""
        @self.c.early(ttl=60, early_ttl=5)
        def get_data(x):
            self.call_count += 1
            return x * 2

        assert get_data(3) == 6
        assert self.call_count == 1
        assert get_data(3) == 6
        assert self.call_count == 1  # 命中缓存

    def test_early_cache_expires(self):
        """TTL 过期后重新计算。"""
        @self.c.early(ttl=0.2, early_ttl=0.05)
        def get_data(x):
            self.call_count += 1
            return x

        get_data(1)
        assert self.call_count == 1
        time.sleep(0.3)
        get_data(1)
        assert self.call_count == 2


# ============================================================
# soft 装饰器测试
# ============================================================

class TestSoftExpiry:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_soft_basic_cache(self):
        """soft_ttl 未到期时，直接返回缓存值。"""
        @self.c.soft(ttl=60, soft_ttl=30)
        def get_data(x):
            self.call_count += 1
            return x * 2

        assert get_data(5) == 10
        assert self.call_count == 1
        assert get_data(5) == 10
        assert self.call_count == 1


# ============================================================
# hit 装饰器测试
# ============================================================

class TestHitCache:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_hit_invalidates_after_n_hits(self):
        """cache_hits 次命中后自动失效，下次重新调用函数。"""
        @self.c.hit(ttl=60, cache_hits=2)
        def get_data(x):
            self.call_count += 1
            return x

        get_data(1)          # miss → 调用函数，缓存
        assert self.call_count == 1
        get_data(1)          # hit 1
        get_data(1)          # hit 2 → 达到上限，失效
        get_data(1)          # miss → 重新调用
        assert self.call_count == 2


# ============================================================
# circuit_breaker 装饰器测试
# ============================================================

class TestCircuitBreaker:
    def setup_method(self):
        self.c = Cache().setup("mem://")

    def test_circuit_breaker_opens_on_errors(self):
        """错误率超标后熔断，后续调用抛 CircuitBreakerOpen。"""
        call_count = [0]

        @self.c.circuit_breaker(errors_rate=0.5, period=10, ttl=5)
        def unstable():
            call_count[0] += 1
            raise RuntimeError("service error")

        # 多次调用触发熔断
        for _ in range(5):
            try:
                unstable()
            except (RuntimeError, CircuitBreakerOpen):
                pass

        # 熔断后应直接抛 CircuitBreakerOpen（不再调用函数）
        with pytest.raises(CircuitBreakerOpen):
            unstable()


# ============================================================
# slice_rate_limit 测试
# ============================================================

class TestSliceRateLimit:
    def setup_method(self):
        self.c = Cache().setup("mem://")

    def test_slice_rate_limit(self):
        """滑动窗口限流：超出限制后抛 RateLimitError。"""
        @self.c.slice_rate_limit(limit=3, period=60)
        def api_call():
            return "ok"

        assert api_call() == "ok"
        assert api_call() == "ok"
        assert api_call() == "ok"
        with pytest.raises(RateLimitError):
            api_call()


# ============================================================
# tags 标签批量失效测试
# ============================================================

class TestTags:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_delete_tags_invalidates_tagged_entries(self):
        """按标签批量删除后，下次调用重新执行函数。"""
        @self.c.cache(ttl=60, tags=("users",))
        def get_profile(user_id):
            self.call_count += 1
            return {"id": user_id}

        get_profile(1)
        get_profile(1)
        assert self.call_count == 1  # 命中缓存

        self.c.delete_tags_sync("users")

        get_profile(1)
        assert self.call_count == 2  # 标签失效，重新调用

    def test_delete_tags_multiple(self):
        """多个标签，删除其中一个标签使对应缓存失效。"""
        @self.c.cache(ttl=60, tags=("users", "profiles"))
        def get_user(user_id):
            self.call_count += 1
            return user_id

        get_user(10)
        assert self.call_count == 1

        self.c.delete_tags_sync("profiles")
        get_user(10)
        assert self.call_count == 2

    def test_delete_tags_async(self):
        """异步按标签删除。"""
        @self.c.cache(ttl=60, tags=("async_tag",))
        async def get_async(x):
            self.call_count += 1
            return x

        async def _test():
            await get_async(1)
            assert self.call_count == 1
            await self.c.delete_tags("async_tag")
            await get_async(1)
            assert self.call_count == 2

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# serializer 自定义序列化器测试
# ============================================================

class TestCustomSerializer:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_json_serializer(self):
        """使用 JsonSerializer 序列化，能正确存取 dict。"""
        from nb_cache.serialize import Serializer
        from nb_cache import JsonSerializer

        json_ser = Serializer(serializer=JsonSerializer())

        @self.c.cache(ttl=60, serializer=json_ser)
        def get_data(key):
            self.call_count += 1
            return {"key": key, "value": 42}

        r1 = get_data("x")
        assert r1 == {"key": "x", "value": 42}
        r2 = get_data("x")
        assert r2 == {"key": "x", "value": 42}
        assert self.call_count == 1  # 命中缓存


# ============================================================
# prefix 叠加测试
# ============================================================

class TestPrefix:
    def test_decorator_prefix_isolated_from_no_prefix(self):
        """装饰器级别 prefix 与无 prefix 的 key 互相隔离。"""
        c = Cache().setup("mem://")
        call_count = [0]

        @c.cache(ttl=60, prefix="v1")
        def get_data(x):
            call_count[0] += 1
            return x

        @c.cache(ttl=60, prefix="v2")
        def get_data_v2(x):
            call_count[0] += 1
            return x * 10

        get_data(1)    # key 含 v1 前缀
        get_data_v2(1) # key 含 v2 前缀，与上面不同
        assert call_count[0] == 2  # 两个都未命中对方缓存

    def test_setup_prefix_applied(self):
        """setup(prefix=...) 全局前缀：两个不同 prefix 的实例数据隔离。"""
        c1 = Cache().setup("mem://", prefix="app1")
        c2 = Cache().setup("mem://", prefix="app2")

        c1.set_sync("key", "from_app1")
        assert c2.get_sync("key") is None  # 前缀不同，隔离


# ============================================================
# TTL 多种格式测试（通过装饰器验证）
# ============================================================

class TestTTLFormats:
    def setup_method(self):
        self.c = Cache().setup("mem://")

    def test_ttl_int(self):
        @self.c.cache(ttl=60)
        def fn():
            return 1
        assert fn() == 1

    def test_ttl_float(self):
        @self.c.cache(ttl=0.5)
        def fn():
            return 2
        assert fn() == 2

    def test_ttl_string_seconds(self):
        @self.c.cache(ttl="10s")
        def fn():
            return 3
        assert fn() == 3

    def test_ttl_string_minutes(self):
        @self.c.cache(ttl="5m")
        def fn():
            return 4
        assert fn() == 4

    def test_ttl_string_hours(self):
        @self.c.cache(ttl="1h")
        def fn():
            return 5
        assert fn() == 5

    def test_ttl_string_combined(self):
        @self.c.cache(ttl="1h30m")
        def fn():
            return 6
        assert fn() == 6

    def test_ttl_timedelta(self):
        from datetime import timedelta

        @self.c.cache(ttl=timedelta(minutes=10))
        def fn():
            return 7
        assert fn() == 7


# ============================================================
# iterator 异步生成器测试
# ============================================================

class TestIteratorAsync:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_async_generator_cache(self):
        """异步生成器缓存：第二次调用从缓存还原，不重新执行。"""
        @self.c.iterator(ttl=60)
        async def gen_items():
            self.call_count += 1
            for i in range(3):
                yield i

        async def _collect(gen):
            return [x async for x in gen()]

        async def _test():
            r1 = await _collect(gen_items)
            assert r1 == [0, 1, 2]
            assert self.call_count == 1

            r2 = await _collect(gen_items)
            assert r2 == [0, 1, 2]
            assert self.call_count == 1  # 命中缓存

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# lock 上下文管理器测试（补充 async）
# ============================================================

class TestLockContextManagerAsync:
    def setup_method(self):
        self.c = Cache().setup("mem://")

    def test_async_lock_exclusion(self):
        """异步锁：持锁期间 is_locked 为 True，释放后为 False。"""
        async def _test():
            async with self.c.alock("res2", ttl=5):
                assert await self.c.backend.is_locked("res2") is True
            assert await self.c.backend.is_locked("res2") is False

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# DualBackend 测试（需要 Redis，不可用时自动跳过）
# ============================================================

def _redis_available():
    """检测 Redis 是否可用。"""
    try:
        import redis
        r = redis.Redis(host="localhost", port=6379, db=0, socket_timeout=1)
        r.ping()
        r.close()
        return True
    except Exception:
        return False


_skip_no_redis = pytest.mark.skipif(
    not _redis_available(), reason="Redis not available on localhost:6379"
)


@_skip_no_redis
class TestDualBackendDirect:
    """直接测试 DualBackend 底层操作（L1 内存 + L2 Redis）。"""

    def setup_method(self):
        from nb_cache.backends.dual import DualBackend
        self.be = DualBackend(memory_size=100, local_ttl=10,
                              host="localhost", port=6379, db=0)
        self.be.init_sync()
        self.be.clear_sync()

    def teardown_method(self):
        self.be.clear_sync()
        self.be.close_sync()

    def test_set_get_sync(self):
        self.be.set_sync("dk1", "dv1", ttl=60)
        assert self.be.get_sync("dk1") == "dv1"

    def test_get_miss(self):
        assert self.be.get_sync("nonexistent") is None

    def test_l1_hit(self):
        """写入后 L1 内存直接命中，不需要走 Redis。"""
        self.be.set_sync("dk2", "dv2", ttl=60)
        # L1 应该有（刚写入）
        assert self.be._memory.get_sync("dk2") == "dv2"
        assert self.be.get_sync("dk2") == "dv2"

    def test_l1_miss_l2_hit_and_backfill(self):
        """L1 没有但 L2 有时，读取后回填 L1。"""
        # 直接写 Redis（绕过 L1）— Redis 返回 bytes
        self.be._redis.set_sync("dk3", "dv3", ttl=60)
        assert self.be._memory.get_sync("dk3") is None  # L1 空

        val = self.be.get_sync("dk3")
        assert val is not None
        # 读完后 L1 应被回填（值可能是 bytes 或 str，取决于 Redis）
        assert self.be._memory.get_sync("dk3") is not None

    def test_delete_sync(self):
        self.be.set_sync("dk4", "dv4")
        self.be.delete_sync("dk4")
        assert self.be.get_sync("dk4") is None
        assert self.be._memory.get_sync("dk4") is None
        assert self.be._redis.get_sync("dk4") is None

    def test_exists_sync(self):
        self.be.set_sync("dk5", "dv5")
        assert self.be.exists_sync("dk5") is True
        assert self.be.exists_sync("nope") is False

    def test_incr_sync(self):
        assert self.be.incr_sync("dcnt") == 1
        assert self.be.incr_sync("dcnt") == 2
        assert self.be.incr_sync("dcnt", 3) == 5

    def test_clear_sync(self):
        self.be.set_sync("dk6", 1)
        self.be.set_sync("dk7", 2)
        self.be.clear_sync()
        assert self.be.get_sync("dk6") is None
        assert self.be.get_sync("dk7") is None

    def test_get_many_sync(self):
        self.be.set_sync("da", 10)
        self.be.set_sync("db", 20)
        result = self.be.get_many_sync("da", "db", "dc")
        assert result == [10, 20, None]

    def test_set_many_sync(self):
        self.be.set_many_sync({"dx": 100, "dy": 200})
        assert self.be.get_sync("dx") == 100
        assert self.be.get_sync("dy") == 200

    def test_lock_sync(self):
        assert self.be.set_lock_sync("dlock", 5) is True
        assert self.be.is_locked_sync("dlock") is True
        assert self.be.set_lock_sync("dlock", 5) is False
        self.be.unlock_sync("dlock")
        assert self.be.is_locked_sync("dlock") is False

    def test_async_get_set(self):
        async def _test():
            await self.be.set("adk1", "adv1", ttl=60)
            val = await self.be.get("adk1")
            assert val == "adv1"
        asyncio.get_event_loop().run_until_complete(_test())

    def test_async_l1_miss_l2_backfill(self):
        """异步：L1 miss → L2 hit → 回填 L1。"""
        async def _test():
            await self.be._redis.set("adk2", "adv2", ttl=60)
            assert await self.be._memory.get("adk2") is None
            val = await self.be.get("adk2")
            assert val is not None
            assert await self.be._memory.get("adk2") is not None
        asyncio.get_event_loop().run_until_complete(_test())


@_skip_no_redis
class TestDualCacheDecorator:
    """通过 Cache().setup("dual://") 使用装饰器的完整端到端测试。"""

    def setup_method(self):
        self.c = Cache().setup("dual://localhost:6379/0?memory_size=100&local_ttl=10")
        self.c.clear_sync()
        self.call_count = 0

    def teardown_method(self):
        self.c.clear_sync()

    def test_sync_cache_hit(self):
        @self.c.cache(ttl=60)
        def compute(x):
            self.call_count += 1
            return x * 2

        assert compute(5) == 10
        assert self.call_count == 1
        assert compute(5) == 10
        assert self.call_count == 1  # 命中双缓存

    def test_async_cache_hit(self):
        @self.c.cache(ttl=60)
        async def compute_async(x):
            self.call_count += 1
            return x * 3

        async def _test():
            assert await compute_async(4) == 12
            assert self.call_count == 1
            assert await compute_async(4) == 12
            assert self.call_count == 1

        asyncio.get_event_loop().run_until_complete(_test())

    def test_sync_cache_with_lock(self):
        @self.c.cache(ttl=60, lock=True)
        def compute_locked(x):
            self.call_count += 1
            return x * 5

        assert compute_locked(3) == 15
        assert self.call_count == 1
        assert compute_locked(3) == 15
        assert self.call_count == 1

    def test_direct_operations(self):
        self.c.set_sync("dkey", "dval", ttl=60)
        assert self.c.get_sync("dkey") == "dval"
        self.c.delete_sync("dkey")
        assert self.c.get_sync("dkey") is None

    def test_transaction_on_dual(self):
        with self.c.transaction() as tx:
            tx.set("dtx1", "v1", ttl=60)
            tx.set("dtx2", "v2", ttl=60)
        assert self.c.get_sync("dtx1") == "v1"
        assert self.c.get_sync("dtx2") == "v2"


# ============================================================
# setup() 序列化 kwargs 测试
# ============================================================

class TestSetupSerializationKwargs:
    def test_pickle_type_json(self):
        """setup(pickle_type='json') 应能正常工作。"""
        c = Cache().setup("mem://", pickle_type="json")
        c.set_sync("jk", {"a": 1}, ttl=60)
        assert c.get_sync("jk") == {"a": 1}

    def test_compress_type_gzip(self):
        """setup(compress_type='gzip') 数据压缩后仍能正确还原。"""
        c = Cache().setup("mem://", compress_type="gzip")
        c.set_sync("gk", "hello" * 100, ttl=60)
        assert c.get_sync("gk") == "hello" * 100

    def test_compress_type_zlib(self):
        """setup(compress_type='zlib') 同理。"""
        c = Cache().setup("mem://", compress_type="zlib")
        c.set_sync("zk", [1, 2, 3] * 50, ttl=60)
        assert c.get_sync("zk") == [1, 2, 3] * 50

    def test_secret_hmac_signing(self):
        """setup(secret=...) 数据签名，正常读取不报错。"""
        c = Cache().setup("mem://", secret="my-secret", digestmod="sha256")
        c.set_sync("sk", {"signed": True}, ttl=60)
        assert c.get_sync("sk") == {"signed": True}

    def test_json_gzip_secret_combined(self):
        """pickle_type + compress_type + secret 三者组合使用。"""
        c = Cache().setup("mem://", pickle_type="json",
                          compress_type="gzip", secret="combo-key")
        data = {"x": list(range(100))}
        c.set_sync("combo", data, ttl=60)
        assert c.get_sync("combo") == data


# ============================================================
# setup() 内存 kwargs 测试
# ============================================================

class TestSetupMemoryKwargs:
    def test_size_via_setup(self):
        """通过 setup() 传入 size 参数，LRU 淘汰正常工作。"""
        c = Cache().setup("mem://", size=3)
        c.set_sync("a", 1)
        c.set_sync("b", 2)
        c.set_sync("c", 3)
        c.set_sync("d", 4)  # 超过 size=3，淘汰最早的
        assert c.get_sync("a") is None
        assert c.get_sync("d") == 4

    def test_size_via_url_query(self):
        """通过 URL query string 传 size。"""
        c = Cache().setup("mem://?size=2")
        c.set_sync("x", 1)
        c.set_sync("y", 2)
        c.set_sync("z", 3)
        assert c.get_sync("x") is None
        assert c.get_sync("z") == 3


# ============================================================
# setup() 链式调用测试
# ============================================================

class TestSetupChain:
    def test_setup_returns_self(self):
        """Cache().setup() 返回 self，支持链式调用。"""
        c = Cache().setup("mem://")
        assert isinstance(c, Cache)
        assert c.is_setup

    def test_chained_decorator(self):
        """一行写法可以直接调装饰器。"""
        cache = Cache().setup("mem://")

        @cache.cache(ttl=60)
        def fn(x):
            return x + 1

        assert fn(1) == 2


# ============================================================
# Wrapper 批量操作测试
# ============================================================

class TestWrapperBatchOperations:
    def setup_method(self):
        self.c = Cache().setup("mem://")

    def test_get_many_sync(self):
        self.c.set_sync("bk1", "bv1")
        self.c.set_sync("bk2", "bv2")
        result = self.c.get_many_sync("bk1", "bk2", "bk3")
        assert result == ["bv1", "bv2", None]

    def test_set_many_sync(self):
        self.c.set_many_sync({"sm1": 10, "sm2": 20})
        assert self.c.get_sync("sm1") == 10
        assert self.c.get_sync("sm2") == 20

    def test_scan_sync(self):
        self.c.set_sync("user:100", "a")
        self.c.set_sync("user:200", "b")
        self.c.set_sync("order:1", "c")
        keys = self.c.scan_sync("user:*")
        assert sorted(keys) == ["user:100", "user:200"]

    def test_delete_match_sync(self):
        self.c.set_sync("tmp:1", "x")
        self.c.set_sync("tmp:2", "y")
        self.c.set_sync("keep:1", "z")
        self.c.delete_match_sync("tmp:*")
        assert self.c.get_sync("tmp:1") is None
        assert self.c.get_sync("keep:1") == "z"

    def test_async_batch_operations(self):
        async def _test():
            await self.c.set("ak1", "av1", ttl=60)
            await self.c.set("ak2", "av2", ttl=60)
            result = await self.c.get_many("ak1", "ak2", "ak3")
            assert result == ["av1", "av2", None]

        asyncio.get_event_loop().run_until_complete(_test())


# ============================================================
# lock_ttl 参数测试
# ============================================================

class TestLockTtl:
    def setup_method(self):
        self.c = Cache().setup("mem://")
        self.call_count = 0

    def test_lock_ttl_separate_from_cache_ttl(self):
        """lock_ttl 独立于 cache ttl，两者可以不同。"""
        @self.c.cache(ttl=60, lock=True, lock_ttl=5)
        def compute(x):
            self.call_count += 1
            return x * 2

        assert compute(1) == 2
        assert self.call_count == 1
        assert compute(1) == 2
        assert self.call_count == 1  # 命中缓存

    def test_lock_ttl_string_format(self):
        """lock_ttl 支持字符串格式。"""
        @self.c.cache(ttl="1h", lock=True, lock_ttl="30s")
        def compute(x):
            self.call_count += 1
            return x

        assert compute(5) == 5
        assert self.call_count == 1


# ============================================================
# register_backend 自定义后端注册测试
# ============================================================

class TestRegisterBackend:
    def test_register_and_use_custom_backend(self):
        """注册自定义后端 scheme，通过 URL 使用。"""
        from nb_cache import register_backend

        register_backend("mymem", "nb_cache.backends.memory:MemoryBackend")

        c = Cache().setup("mymem://")
        c.set_sync("custom_be_key", "ok")
        assert c.get_sync("custom_be_key") == "ok"
        assert isinstance(c.backend, MemoryBackend)


# ============================================================
# Wrapper 级别 expire / get_expire 测试
# ============================================================

class TestWrapperExpire:
    def setup_method(self):
        self.c = Cache().setup("mem://")

    def test_expire_sync(self):
        self.c.set_sync("ek", "ev")
        self.c.expire_sync("ek", 0.2)
        assert self.c.get_sync("ek") == "ev"
        time.sleep(0.3)
        assert self.c.get_sync("ek") is None

    def test_get_expire_sync(self):
        self.c.set_sync("ek2", "ev2", ttl=10)
        remaining = self.c.get_expire_sync("ek2")
        assert remaining is not None
        assert 9 <= remaining <= 10


# ============================================================
# ping 测试
# ============================================================

class TestPing:
    def test_memory_ping_sync(self):
        """内存后端 ping 不抛异常。"""
        c = Cache().setup("mem://")
        c.ping_sync()  # 不报错即通过

    def test_memory_ping_async(self):
        c = Cache().setup("mem://")

        async def _test():
            await c.ping()

        asyncio.get_event_loop().run_until_complete(_test())


if __name__ == '__main__':
    pytest.main([__file__, '-v'])


"""
python -m pytest tests/ai_codes/test_core.py -v -p no:logfire
"""
`````

--- **end of file: tests/ai_codes/test_core.py** (project: nb_cache) --- 

---

