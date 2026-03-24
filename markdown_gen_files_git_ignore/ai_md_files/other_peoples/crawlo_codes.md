# markdown content namespace: Crawlo  all files 


## File Tree


```

├── README.md
├── assets
│   └── README.md
└── crawlo
    ├── __init__.py
    ├── __version__.py
    ├── cli.py
    ├── commands
    │   ├── __init__.py
    │   ├── check.py
    │   ├── genspider.py
    │   ├── help.py
    │   ├── list.py
    │   ├── run.py
    │   ├── startproject.py
    │   ├── stats.py
    │   └── utils.py
    ├── config.py
    ├── config_validator.py
    ├── core
    │   ├── __init__.py
    │   ├── engine.py
    │   ├── processor.py
    │   └── scheduler.py
    ├── crawler.py
    ├── data
    │   ├── __init__.py
    │   └── user_agents.py
    ├── downloader
    │   ├── __init__.py
    │   ├── aiohttp_downloader.py
    │   ├── cffi_downloader.py
    │   ├── httpx_downloader.py
    │   ├── hybrid_downloader.py
    │   ├── playwright_downloader.py
    │   └── selenium_downloader.py
    ├── event.py
    ├── exceptions.py
    ├── extension
    │   ├── __init__.py
    │   ├── health_check.py
    │   ├── log_interval.py
    │   ├── log_stats.py
    │   ├── logging_extension.py
    │   ├── memory_monitor.py
    │   ├── performance_profiler.py
    │   └── request_recorder.py
    ├── factories
    │   ├── __init__.py
    │   ├── base.py
    │   ├── crawler.py
    │   ├── registry.py
    │   └── utils.py
    ├── filters
    │   ├── __init__.py
    │   ├── aioredis_filter.py
    │   └── memory_filter.py
    ├── framework.py
    ├── initialization
    │   ├── __init__.py
    │   ├── built_in.py
    │   ├── context.py
    │   ├── core.py
    │   ├── phases.py
    │   ├── registry.py
    │   └── utils.py
    ├── interfaces.py
    ├── items
    │   ├── __init__.py
    │   ├── base.py
    │   ├── fields.py
    │   └── items.py
    ├── logging
    │   ├── __init__.py
    │   ├── config.py
    │   ├── factory.py
    │   └── manager.py
    ├── middleware
    │   ├── __init__.py
    │   ├── default_header.py
    │   ├── download_delay.py
    │   ├── middleware_manager.py
    │   ├── offsite.py
    │   ├── proxy.py
    │   ├── request_ignore.py
    │   ├── response_code.py
    │   ├── response_filter.py
    │   └── retry.py
    ├── mode_manager.py
    ├── network
    │   ├── __init__.py
    │   ├── request.py
    │   └── response.py
    ├── pipelines
    │   ├── __init__.py
    │   ├── base_pipeline.py
    │   ├── bloom_dedup_pipeline.py
    │   ├── console_pipeline.py
    │   ├── csv_pipeline.py
    │   ├── database_dedup_pipeline.py
    │   ├── json_pipeline.py
    │   ├── memory_dedup_pipeline.py
    │   ├── mongo_pipeline.py
    │   ├── mysql_pipeline.py
    │   ├── pipeline_manager.py
    │   └── redis_dedup_pipeline.py
    ├── project.py
    ├── queue
    │   ├── __init__.py
    │   ├── pqueue.py
    │   ├── queue_manager.py
    │   └── redis_priority_queue.py
    ├── settings
    │   ├── __init__.py
    │   ├── default_settings.py
    │   └── setting_manager.py
    ├── spider
    │   └── __init__.py
    ├── stats_collector.py
    ├── subscriber.py
    ├── task_manager.py
    ├── tools
    │   ├── __init__.py
    │   ├── date_tools.py
    │   ├── distributed_coordinator.py
    │   ├── scenario_adapter.py
    │   └── text_cleaner.py
    └── utils
        ├── __init__.py
        ├── batch_processor.py
        ├── config_manager.py
        ├── controlled_spider_mixin.py
        ├── db_helper.py
        ├── error_handler.py
        ├── fingerprint.py
        ├── func_tools.py
        ├── large_scale_helper.py
        ├── leak_detector.py
        ├── log.py
        ├── misc.py
        ├── mongo_connection_pool.py
        ├── mysql_connection_pool.py
        ├── performance_monitor.py
        ├── queue_helper.py
        ├── redis_checker.py
        ├── redis_connection_pool.py
        ├── redis_key_validator.py
        ├── request.py
        ├── request_serializer.py
        ├── resource_manager.py
        ├── selector_helper.py
        ├── singleton.py
        ├── spider_loader.py
        ├── text_helper.py
        └── url_utils.py

```

---


## Included Files


- `README.md`

- `assets/README.md`

- `crawlo/cli.py`

- `crawlo/config.py`

- `crawlo/config_validator.py`

- `crawlo/crawler.py`

- `crawlo/event.py`

- `crawlo/exceptions.py`

- `crawlo/framework.py`

- `crawlo/interfaces.py`

- `crawlo/mode_manager.py`

- `crawlo/project.py`

- `crawlo/stats_collector.py`

- `crawlo/subscriber.py`

- `crawlo/task_manager.py`

- `crawlo/__init__.py`

- `crawlo/__version__.py`

- `crawlo/commands/check.py`

- `crawlo/commands/genspider.py`

- `crawlo/commands/help.py`

- `crawlo/commands/list.py`

- `crawlo/commands/run.py`

- `crawlo/commands/startproject.py`

- `crawlo/commands/stats.py`

- `crawlo/commands/utils.py`

- `crawlo/commands/__init__.py`

- `crawlo/core/engine.py`

- `crawlo/core/processor.py`

- `crawlo/core/scheduler.py`

- `crawlo/core/__init__.py`

- `crawlo/data/user_agents.py`

- `crawlo/data/__init__.py`

- `crawlo/downloader/aiohttp_downloader.py`

- `crawlo/downloader/cffi_downloader.py`

- `crawlo/downloader/httpx_downloader.py`

- `crawlo/downloader/hybrid_downloader.py`

- `crawlo/downloader/playwright_downloader.py`

- `crawlo/downloader/selenium_downloader.py`

- `crawlo/downloader/__init__.py`

- `crawlo/extension/health_check.py`

- `crawlo/extension/logging_extension.py`

- `crawlo/extension/log_interval.py`

- `crawlo/extension/log_stats.py`

- `crawlo/extension/memory_monitor.py`

- `crawlo/extension/performance_profiler.py`

- `crawlo/extension/request_recorder.py`

- `crawlo/extension/__init__.py`

- `crawlo/factories/base.py`

- `crawlo/factories/crawler.py`

- `crawlo/factories/registry.py`

- `crawlo/factories/utils.py`

- `crawlo/factories/__init__.py`

- `crawlo/filters/aioredis_filter.py`

- `crawlo/filters/memory_filter.py`

- `crawlo/filters/__init__.py`

- `crawlo/initialization/built_in.py`

- `crawlo/initialization/context.py`

- `crawlo/initialization/core.py`

- `crawlo/initialization/phases.py`

- `crawlo/initialization/registry.py`

- `crawlo/initialization/utils.py`

- `crawlo/initialization/__init__.py`

- `crawlo/items/base.py`

- `crawlo/items/fields.py`

- `crawlo/items/items.py`

- `crawlo/items/__init__.py`

- `crawlo/logging/config.py`

- `crawlo/logging/factory.py`

- `crawlo/logging/manager.py`

- `crawlo/logging/__init__.py`

- `crawlo/middleware/default_header.py`

- `crawlo/middleware/download_delay.py`

- `crawlo/middleware/middleware_manager.py`

- `crawlo/middleware/offsite.py`

- `crawlo/middleware/proxy.py`

- `crawlo/middleware/request_ignore.py`

- `crawlo/middleware/response_code.py`

- `crawlo/middleware/response_filter.py`

- `crawlo/middleware/retry.py`

- `crawlo/middleware/__init__.py`

- `crawlo/network/request.py`

- `crawlo/network/response.py`

- `crawlo/network/__init__.py`

- `crawlo/pipelines/base_pipeline.py`

- `crawlo/pipelines/bloom_dedup_pipeline.py`

- `crawlo/pipelines/console_pipeline.py`

- `crawlo/pipelines/csv_pipeline.py`

- `crawlo/pipelines/database_dedup_pipeline.py`

- `crawlo/pipelines/json_pipeline.py`

- `crawlo/pipelines/memory_dedup_pipeline.py`

- `crawlo/pipelines/mongo_pipeline.py`

- `crawlo/pipelines/mysql_pipeline.py`

- `crawlo/pipelines/pipeline_manager.py`

- `crawlo/pipelines/redis_dedup_pipeline.py`

- `crawlo/pipelines/__init__.py`

- `crawlo/queue/pqueue.py`

- `crawlo/queue/queue_manager.py`

- `crawlo/queue/redis_priority_queue.py`

- `crawlo/queue/__init__.py`

- `crawlo/settings/default_settings.py`

- `crawlo/settings/setting_manager.py`

- `crawlo/settings/__init__.py`

- `crawlo/spider/__init__.py`

- `crawlo/tools/date_tools.py`

- `crawlo/tools/distributed_coordinator.py`

- `crawlo/tools/scenario_adapter.py`

- `crawlo/tools/text_cleaner.py`

- `crawlo/tools/__init__.py`

- `crawlo/utils/batch_processor.py`

- `crawlo/utils/config_manager.py`

- `crawlo/utils/controlled_spider_mixin.py`

- `crawlo/utils/db_helper.py`

- `crawlo/utils/error_handler.py`

- `crawlo/utils/fingerprint.py`

- `crawlo/utils/func_tools.py`

- `crawlo/utils/large_scale_helper.py`

- `crawlo/utils/leak_detector.py`

- `crawlo/utils/log.py`

- `crawlo/utils/misc.py`

- `crawlo/utils/mongo_connection_pool.py`

- `crawlo/utils/mysql_connection_pool.py`

- `crawlo/utils/performance_monitor.py`

- `crawlo/utils/queue_helper.py`

- `crawlo/utils/redis_checker.py`

- `crawlo/utils/redis_connection_pool.py`

- `crawlo/utils/redis_key_validator.py`

- `crawlo/utils/request.py`

- `crawlo/utils/request_serializer.py`

- `crawlo/utils/resource_manager.py`

- `crawlo/utils/selector_helper.py`

- `crawlo/utils/singleton.py`

- `crawlo/utils/spider_loader.py`

- `crawlo/utils/text_helper.py`

- `crawlo/utils/url_utils.py`

- `crawlo/utils/__init__.py`


---


### code file start: README.md 

<p align="center">
  <img src="assets/logo.svg" alt="Crawlo Logo" width="150"/>
</p>

<h1 align="center">Crawlo</h1>

<p align="center">
  <strong>一个基于 asyncio 的现代化、高性能 Python 异步爬虫框架。</strong>
</p>

<p align="center">
  <a href="#核心特性">核心特性</a> •
  <a href="#项目架构">架构</a> •
  <a href="#安装">安装</a> •
  <a href="#配置模式详解">配置模式</a> •
  <a href="https://github.com/yourusername/crawlo">文档</a>
</p>

## 核心特性

- 🚀 **高性能异步架构**：基于 asyncio 和 aiohttp，充分利用异步 I/O 提升爬取效率
- 🎯 **智能调度系统**：优先级队列、并发控制、自动重试、智能限速
- 🔄 **灵活的配置模式**：
  - **Standalone 模式**：单机开发测试，使用内存队列
  - **Distributed 模式**：多节点分布式部署，严格要求 Redis（不允许降级）
  - **Auto 模式**：智能检测 Redis 可用性，自动选择最佳配置（推荐）
- 📦 **丰富的组件生态**：
  - 内置 Redis 和 MongoDB 支持
  - MySQL 异步连接池（基于 asyncmy）
  - 多种过滤器和去重管道（Memory/Redis）
  - 代理中间件支持（简单代理/动态代理）
  - 多种下载器（aiohttp、httpx、curl-cffi）
- 🛠 **开发友好**：
  - 类 Scrapy 的项目结构和 API 设计
  - 配置工厂模式（`CrawloConfig.auto()`）
  - 自动爬虫发现机制
  - 完善的日志系统

## 项目架构

Crawlo 框架采用模块化设计，核心组件包括：

![Crawlo 框架架构图](images/Crawlo%20框架架构图.png)

- **Engine**：核心引擎，协调各个组件工作
- **Scheduler**：调度器，管理请求队列和去重
- **Downloader**：下载器，支持多种 HTTP 客户端
- **Spider**：爬虫基类，定义数据提取逻辑
- **Pipeline**：数据管道，处理和存储数据
- **Middleware**：中间件，处理请求和响应

![Crawlo 数据流图](images/Crawlo%20数据流图.png)

## 示例项目

查看 [`examples/`](examples/) 目录下的完整示例项目：

- **ofweek_standalone** - Auto 模式示例（智能检测）
- **ofweek_spider** - Auto 模式示例
- **ofweek_distributed** - Distributed 模式示例（严格分布式）

## 安装

```bash
# 基础安装
pip install crawlo
```

## 配置模式详解

> ⚠️ **重要**：配置模式的选择直接影响爬虫的运行方式、性能和可靠性，请仔细阅读本节内容。

Crawlo 提供三种配置模式，满足不同场景需求：

### 三种模式对比

| 配置项 | Standalone | Distributed | Auto |
|--------|-----------|-------------|------|
| **RUN_MODE** | `standalone` | `distributed` | `auto` |
| **队列类型** | 内存队列 | Redis 队列 | 自动检测 |
| **Redis 要求** | 不需要 | **必需** | 可选 |
| **Redis 不可用时** | N/A | 🚫 **报错退出** | ✅ 降级到内存 |
| **配置自动更新** | ❌ 否 | ❌ 否 | ✅ 是 |
| **过滤器** | Memory | Redis | Redis/Memory |
| **去重管道** | Memory | Redis | Redis/Memory |
| **适用场景** | 开发测试 | 多节点部署 | 生产环境 |
| **并发数默认值** | 8 | 16 | 12 |
| **推荐指数** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

### 1. Auto 模式（推荐）

**智能检测，自动适配，推荐用于生产环境。**

```python
from crawlo.config import CrawloConfig

config = CrawloConfig.auto(
    project_name='myproject',
    concurrency=12,
    download_delay=1.0
)
locals().update(config.to_dict())
```

**运行机制**：
- 配置阶段不依赖 Redis
- 运行时才检测 Redis 可用性
- Redis 可用 → 使用 `RedisPriorityQueue` + `AioRedisFilter`
- Redis 不可用 → 降级到 `MemoryQueue` + `MemoryFilter`
- 自动更新配置（`QUEUE_TYPE`、`FILTER_CLASS`、`DEFAULT_DEDUP_PIPELINE`）

**优势**：
- ✅ 开发环境无需配置 Redis，直接启动
- ✅ 生产环境 Redis 故障时自动降级，保证系统可用性
- ✅ 同一份代码可在不同环境运行，无需修改配置
- ✅ 最佳的灵活性和可靠性

**适用场景**：
- 生产环境部署（首选）
- 需要在多种环境运行的项目
- 希望系统具备容错能力

### 2. Standalone 模式

**单机模式，适合开发测试和中小规模爬取。**

```python
config = CrawloConfig.standalone(
    project_name='myproject',
    concurrency=8
)
locals().update(config.to_dict())
```

**运行机制**：
- 固定使用 `MemoryQueue`（内存队列）
- 固定使用 `MemoryFilter`（内存过滤器）
- 固定使用 `MemoryDedupPipeline`（内存去重）
- 不进行 Redis 检测
- 配置不会自动更新

**优势**：
- ✅ 无需任何外部依赖
- ✅ 启动速度快
- ✅ 适合快速开发调试

**限制**：
- ❌ 不支持分布式部署
- ❌ 重启后队列数据丢失
- ❌ 不适合大规模数据采集

**适用场景**：
- 本地开发调试
- 学习框架特性
- 中小规模数据采集（< 10万条）
- 单机运行的简单爬虫

### 3. Distributed 模式

**分布式模式，严格要求 Redis 可用，适合多节点协同工作。**

```python
config = CrawloConfig.distributed(
    project_name='myproject',
    redis_host='redis.example.com',
    redis_port=6379,
    redis_password='your_password',
    concurrency=16
)
locals().update(config.to_dict())
```

**运行机制**：
- 必须使用 `RedisPriorityQueue`
- 必须使用 `AioRedisFilter`
- 必须使用 `RedisDedupPipeline`
- 启动时强制检查 Redis 连接
- **Redis 不可用时抛出 `RuntimeError` 并退出（不允许降级）**

**为什么要严格要求 Redis？**

1. **数据一致性**：防止不同节点使用不同的队列类型
2. **去重有效性**：确保多节点间的去重功能正常工作
3. **任务分配**：防止任务被重复执行
4. **问题早发现**：启动失败比运行时失败更容易发现和修复
5. **明确的意图**：分布式模式就应该是分布式的，不应该静默降级

**Redis 不可用时的错误信息**：

```bash
$ crawlo run my_spider

2025-10-25 22:00:00 - [queue_manager] - ERROR: 
Distributed 模式要求 Redis 可用，但无法连接到 Redis 服务器。
错误信息: Connection refused
Redis URL: redis://127.0.0.1:6379/0
请检查：
  1. Redis 服务是否正在运行
  2. Redis 连接配置是否正确
  3. 网络连接是否正常

RuntimeError: Distributed 模式要求 Redis 可用，但无法连接到 Redis 服务器。
```

**优势**：
- ✅ 支持多节点协同爬取
- ✅ 数据持久化，重启后可继续
- ✅ 严格的分布式一致性保证
- ✅ 适合大规模数据采集

**适用场景**：
- 多服务器协同采集
- 大规模数据采集（> 百万条）
- 需要严格保证分布式一致性
- 生产环境多节点部署

### 模式选择建议

| 场景 | 推荐模式 | 原因 |
|------|---------|------|
| 生产环境（单节点或多节点） | **Auto** | 自动适配，容错能力强 |
| 开发环境 | **Standalone** 或 **Auto** | 无需配置 Redis |
| 严格的多节点分布式部署 | **Distributed** | 保证分布式一致性 |
| 学习和测试 | **Standalone** | 最简单，无依赖 |
| 中小规模爬取 | **Standalone** 或 **Auto** | 简单高效 |
| 大规模爬取 | **Auto** 或 **Distributed** | 性能和可靠性 |

> 📖 **完整文档**：更多详细信息请参考 [配置模式完全指南](docs/tutorials/configuration_modes.md)

## 配置优先级

Crawlo 框架支持多层级的配置系统，了解配置优先级对于正确使用框架至关重要。

### 配置来源与优先级

从**低到高**的优先级顺序：

```
1. default_settings.py (框架默认配置)                    ⭐
   ↓
2. 环境变量 (CRAWLO_*)                                   ⭐⭐
   (在 default_settings.py 中通过 EnvConfigManager 读取)
   ↓
3. 用户 settings.py (项目配置文件)                       ⭐⭐⭐
   ↓
4. Spider.custom_settings (Spider 自定义配置)            ⭐⭐⭐⭐
   ↓
5. 运行时 settings 参数 (crawl() 传入的配置)             ⭐⭐⭐⭐⭐
```

### 环境变量配置

所有环境变量都使用 `CRAWLO_` 前缀：

```bash
# 基础配置
export CRAWLO_MODE=auto                    # 运行模式
export CRAWLO_PROJECT_NAME=myproject       # 项目名称
export CRAWLO_CONCURRENCY=16               # 并发数

# Redis 配置
export CRAWLO_REDIS_HOST=127.0.0.1         # Redis 主机
export CRAWLO_REDIS_PORT=6379              # Redis 端口
export CRAWLO_REDIS_PASSWORD=your_password # Redis 密码
export CRAWLO_REDIS_DB=0                   # Redis 数据库
```

### 配置合并策略

**普通配置**（如 `CONCURRENCY`）：采用**覆盖策略**
```python
# 假设各处都有定义
default_settings.py:  8   →
环境变量:  12  →
settings.py:  16  →
Spider.custom_settings:  24  →
crawl(settings={...}):  32  ✅ 最终值 = 32
```

**列表配置**（如 `MIDDLEWARES`、`PIPELINES`、`EXTENSIONS`）：采用**合并策略**
```python
# default_settings.py
PIPELINES = ['crawlo.pipelines.console_pipeline.ConsolePipeline']

# settings.py
PIPELINES = ['myproject.pipelines.MySQLPipeline']

# 最终结果（合并）
PIPELINES = [
    'crawlo.pipelines.console_pipeline.ConsolePipeline',  # 保留默认
    'myproject.pipelines.MySQLPipeline',                   # 追加用户
]
```

### Spider 级别配置

在 Spider 类中可以覆盖项目配置：

```python
class MySpider(Spider):
    name = 'myspider'
    
    custom_settings = {
        'CONCURRENCY': 32,           # 覆盖项目配置
        'DOWNLOAD_DELAY': 2.0,       # 覆盖项目配置
        'PIPELINES': [               # 会与默认管道合并
            'myproject.pipelines.SpecialPipeline',
        ]
    }
```

### 运行时动态配置

```python
from crawlo import CrawlerProcess

process = CrawlerProcess()
await process.crawl(
    MySpider,
    settings={
        'CONCURRENCY': 64,        # 最高优先级
        'DOWNLOAD_DELAY': 0.1,
    }
)
```

### ⚠️ 常见陷阱

**陷阱1：环境变量被项目配置覆盖**
```python
# 环境变量
export CRAWLO_REDIS_HOST=192.168.1.100

# settings.py（这会覆盖环境变量！）
REDIS_HOST = 'localhost'  # ❌ 会覆盖环境变量

# 解决方案：不在 settings.py 中重复设置，或使用 CrawloConfig.auto()
```

**陷阱2：误以为列表配置会被清空**
```python
# settings.py
PIPELINES = ['myproject.pipelines.MySQLPipeline']

# 实际结果（默认管道会被保留并合并）
PIPELINES = [
    'crawlo.pipelines.console_pipeline.ConsolePipeline',  # 默认保留
    'myproject.pipelines.MySQLPipeline',                   # 用户追加
]

# 如果想完全替换，需要先清空
PIPELINES = []  # 清空
PIPELINES.append('myproject.pipelines.MySQLPipeline')
```

> 📖 **详细文档**：完整的配置优先级说明请参考 [配置优先级详解](docs/配置优先级详解.md)

## 快速开始

### 1. 创建项目

```bash
# 创建新项目
crawlo startproject myproject
cd myproject

# 创建爬虫
crawlo genspider example example.com
```

### 2. 配置项目（推荐使用 Auto 模式）

```python
# myproject/settings.py
from crawlo.config import CrawloConfig

# 使用 Auto 模式：智能检测 Redis，自动选择最佳配置
config = CrawloConfig.auto(
    project_name='myproject',
    concurrency=12,          # 并发数
    download_delay=1.0       # 下载延迟（秒）
)

# 将配置应用到当前模块
locals().update(config.to_dict())

# 爬虫模块配置
SPIDER_MODULES = ['myproject.spiders']

# 日志配置
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/myproject.log'

# 可选：添加数据管道
# PIPELINES = [
#     'crawlo.pipelines.mysql_pipeline.AsyncmyMySQLPipeline',
# ]

# 可选：Redis 配置（Auto 模式会自动检测）
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
```

**其他配置模式：**

```python
# Standalone 模式：单机开发测试
config = CrawloConfig.standalone(
    project_name='myproject',
    concurrency=8
)

# Distributed 模式：多节点分布式（必须配置 Redis）
config = CrawloConfig.distributed(
    project_name='myproject',
    redis_host='redis.example.com',
    redis_port=6379,
    redis_password='your_password',
    concurrency=16
)
```

### 3. 编写爬虫

```python
# myproject/spiders/example.py
from crawlo import Spider
from crawlo.http import Request

class ExampleSpider(Spider):
    name = 'example'
    start_urls = ['https://example.com']
    
    async def parse(self, response):
        # 提取数据
        title = response.css('h1::text').get()
        
        # 返回数据
        yield {
            'title': title,
            'url': response.url
        }
        
        # 跟进链接
        for href in response.css('a::attr(href)').getall():
            yield Request(
                url=response.urljoin(href),
                callback=self.parse
            )
```

### 4. 运行爬虫

```bash
# 运行指定爬虫
crawlo run example

# 指定日志级别
crawlo run example --log-level DEBUG
```

## 核心功能

### Response 对象

Crawlo 的 [`Response`](crawlo/http/response.py) 对象提供了强大的网页处理能力：

**1. 智能编码检测**

```python
# 自动检测并正确解码页面内容
# 优先级：Content-Type → HTML meta → chardet → utf-8
response.text      # 已正确解码的文本
response.encoding  # 检测到的编码
```

**2. CSS/XPath 选择器**

```python
# CSS 选择器（推荐）
title = response.css('h1::text').get()
links = response.css('a::attr(href)').getall()

# XPath 选择器
title = response.xpath('//title/text()').get()
links = response.xpath('//a/@href').getall()

# 支持默认值
title = response.css('h1::text').get(default='无标题')
```

**3. URL 处理**

```python
response.url          # 自动规范化（移除 fragment）
response.original_url # 保留原始 URL

# 智能 URL 拼接
response.urljoin('/path')           # 绝对路径
response.urljoin('../path')         # 相对路径
response.urljoin('//cdn.com/img')   # 协议相对路径
```

**4. 便捷提取方法**

```python
# 提取单个/多个元素文本
title = response.extract_text('h1')
paragraphs = response.extract_texts('.content p')

# 提取单个/多个元素属性
link = response.extract_attr('a', 'href')
all_links = response.extract_attrs('a', 'href')
```

### 配置工厂模式

Crawlo 提供了便捷的配置工厂方法，无需手动配置繁琐的参数：

```python
from crawlo.config import CrawloConfig

# Auto 模式（推荐）：智能检测，自动适配
config = CrawloConfig.auto(
    project_name='myproject',
    concurrency=12,
    download_delay=1.0
)

# Standalone 模式：单机开发
config = CrawloConfig.standalone(
    project_name='myproject',
    concurrency=8
)

# Distributed 模式：严格分布式
config = CrawloConfig.distributed(
    project_name='myproject',
    redis_host='localhost',
    redis_port=6379,
    concurrency=16
)

# 应用到 settings.py
locals().update(config.to_dict())
```

**三种模式的核心区别**：

- **Auto**：智能检测 Redis，自动选择最佳配置，**推荐用于生产环境**
- **Standalone**：固定使用内存队列，适合开发测试，无外部依赖
- **Distributed**：严格要求 Redis，不允许降级，保证分布式一致性

> 💡 详细配置说明请查看前面的 [配置模式详解](#配置模式详解) 章节

### 日志系统

Crawlo 提供了完善的日志系统，支持控制台和文件双输出：

```python
from crawlo.logging import get_logger

logger = get_logger(__name__)

logger.debug('调试信息')
logger.info('普通信息')
logger.warning('警告信息')
logger.error('错误信息')
```

**日志配置：**

```python
# settings.py
LOG_LEVEL = 'INFO'          # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = 'logs/spider.log'
LOG_ENCODING = 'utf-8'      # 明确指定日志文件编码
STATS_DUMP = True           # 是否输出统计信息
```

**高级功能：**

```python
from crawlo.logging import configure_logging

# 分别配置控制台和文件日志级别
configure_logging(
    LOG_LEVEL='INFO',
    LOG_CONSOLE_LEVEL='WARNING',  # 控制台只显示 WARNING 及以上
    LOG_FILE_LEVEL='DEBUG',       # 文件记录 DEBUG 及以上
    LOG_FILE='logs/app.log',
    LOG_MAX_BYTES=10*1024*1024,   # 10MB
    LOG_BACKUP_COUNT=5
)
```

### 爬虫自动发现

Crawlo 支持自动发现爬虫，无需手动导入：

```bash
# 自动发现并运行（推荐）
crawlo run spider_name

# 指定文件路径运行
crawlo run -f path/to/spider.py -s SpiderClassName
```

框架会自动在 `SPIDER_MODULES` 配置的模块中查找爬虫。

### 跨平台支持

Crawlo 在 Windows、macOS、Linux 上均可无缝运行：

- **Windows**：自动使用 ProactorEventLoop，正确处理控制台编码
- **macOS/Linux**：使用默认的 SelectorEventLoop
- 兼容不同平台的路径格式

> 💡 **Windows 用户提示**：如需日志轮转功能，建议安装 `concurrent-log-handler`：
> ```bash
> pip install concurrent-log-handler
> ```

![Crawlo 核心架构图](images/Crawlo%20核心架构图.png)

## 文档

完整文档请查看 [`docs/`](docs/) 目录：

### 📚 核心教程

- [配置模式完全指南](docs/tutorials/configuration_modes.md) - **强烈推荐阅读**
- [架构概述](docs/modules/architecture/index.md)
- [运行模式](docs/modules/architecture/modes.md)
- [配置系统](docs/modules/configuration/index.md)

### 🔧 核心模块

- [引擎 (Engine)](docs/modules/core/engine.md)
- [调度器 (Scheduler)](docs/modules/core/scheduler.md)
- [处理器 (Processor)](docs/modules/core/processor.md)
- [爬虫基类 (Spider)](docs/modules/core/spider.md)

### 📦 功能模块

- [下载器 (Downloader)](docs/modules/downloader/index.md)
- [队列 (Queue)](docs/modules/queue/index.md)
- [过滤器 (Filter)](docs/modules/filter/index.md)
- [中间件 (Middleware)](docs/modules/middleware/index.md)
- [管道 (Pipeline)](docs/modules/pipeline/index.md)
- [扩展 (Extension)](docs/modules/extension/index.md)

### 🛠 命令行工具

- [CLI 概述](docs/modules/cli/index.md)
- [startproject](docs/modules/cli/startproject.md) - 项目初始化
- [genspider](docs/modules/cli/genspider.md) - 爬虫生成
- [run](docs/modules/cli/run.md) - 爬虫运行
- [list](docs/modules/cli/list.md) - 查看爬虫列表
- [check](docs/modules/cli/check.md) - 配置检查
- [stats](docs/modules/cli/stats.md) - 统计信息

### 🚀 高级主题

- [分布式部署](docs/modules/advanced/distributed.md)
- [性能优化](docs/modules/advanced/performance.md)
- [故障排除](docs/modules/advanced/troubleshooting.md)
- [最佳实践](docs/modules/advanced/best_practices.md)

### 📝 性能优化报告

- [初始化优化报告](docs/initialization_optimization_report.md)
- [MySQL 连接池优化](docs/mysql_connection_pool_optimization.md)
- [MongoDB 连接池优化](docs/mongo_connection_pool_optimization.md)

### 📖 API 参考

- [完整 API 文档](docs/api/)

---

**在线文档**：
- [中文文档](https://crawlo.readthedocs.io/en/latest/README_zh/)
- [English Documentation](https://crawlo.readthedocs.io/en/latest/)

**本地构建文档**：
```bash
mkdocs serve
# 浏览器访问 http://localhost:8000
```

## 常见问题

### 1. 如何选择配置模式？

- **开发测试**：使用 `CrawloConfig.standalone()`
- **生产环境**：使用 `CrawloConfig.auto()`（推荐）
- **多节点部署**：使用 `CrawloConfig.distributed()`

### 2. Distributed 模式 Redis 不可用怎么办？

Distributed 模式**严格要求 Redis**，不可用时会抛出 `RuntimeError` 并退出。这是为了保证分布式一致性和数据安全。

如果希望 Redis 不可用时自动降级，请使用 **Auto 模式**。

### 3. Auto 模式如何工作？

Auto 模式在运行时智能检测：
- Redis 可用 → 使用 RedisPriorityQueue + AioRedisFilter
- Redis 不可用 → 降级到 MemoryQueue + MemoryFilter

详见 [配置模式完全指南](docs/tutorials/configuration_modes.md)。

### 4. 如何启用 MySQL 或 MongoDB 支持？

```python
# settings.py
PIPELINES = [
    'crawlo.pipelines.mysql_pipeline.AsyncmyMySQLPipeline',  # MySQL
    # 或
    'crawlo.pipelines.mongo_pipeline.MongoDBPipeline',       # MongoDB
]

# MySQL 配置
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_DB = 'mydb'
MYSQL_TABLE = 'items'

# MongoDB 配置
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'mydb'
MONGO_COLLECTION = 'items'
```

### 5. 如何使用代理？

```python
# settings.py

# 简单代理列表
PROXY_LIST = [
    "http://proxy1:8080",
    "http://proxy2:8080"
]

# 或使用动态代理 API
PROXY_API_URL = "http://your-proxy-api.com/get-proxy"
```

## 学习路径

如果您是 Crawlo 的新用户，建议按以下顺序学习：

1. **入门** - 阅读快速开始指南，运行第一个示例
2. **配置模式** - 学习三种配置模式，选择适合的模式（[配置模式指南](docs/tutorials/configuration_modes.md)）
3. **核心概念** - 了解框架架构和基本概念
4. **核心模块** - 深入学习引擎、调度器、处理器等核嘿组件
5. **功能模块** - 根据需求学习下载器、队列、过滤器等模块
6. **高级主题** - 掌握分布式部署、性能优化等高级功能

## 贡献

欢迎贡献！如果您想为 Crawlo 做出贡献：

1. Fork 项目仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 发起 Pull Request

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

<p align="center">
  <i>如有问题或建议，欢迎提交 <a href="https://github.com/crawl-coder/Crawlo/issues">Issue</a></i>
</p>

**code file end: README.md**

---


### code file start: assets/README.md 

# Crawlo Logo 设计说明

## 📁 Logo 文件

本目录包含 Crawlo 框架的官方 Logo 设计文件：

### 文件列表

1. **`logo.svg`** - 标准 Logo（200x200px）
   - 完整版 Logo，包含所有设计元素
   - 适用于：文档封面、项目主页、演示文稿

2. **`logo-horizontal.svg`** - 横版 Logo（400x100px）
   - Logo + 文字组合的横向布局
   - 包含副标题："High-Performance Async Crawler Framework"
   - 适用于：网站 Header、GitHub README、文章标题

3. **`logo-icon.svg`** - 图标版 Logo（64x64px）
   - 简化版本，适合小尺寸显示
   - 圆角方形背景设计
   - 适用于：Favicon、应用图标、社交媒体头像

## 🎨 设计理念

### 核心元素

1. **蜘蛛图形**
   - 代表 "Crawler"（爬虫）的核心概念
   - 8条腿象征全方位的数据采集能力
   - 圆润的设计体现友好和易用性

2. **闪电符号** ⚡
   - 体现高速异步处理能力
   - 金色渐变代表性能和效率
   - 位于蜘蛛身体，象征核心优势

3. **分布式节点**
   - 四角的连接节点代表分布式架构
   - 连接线展示节点间的通信
   - 体现框架的可扩展性

### 配色方案

- **主色调**：Indigo 渐变 (#4F46E5 → #7C3AED)
  - 代表专业、技术、现代
  - 与 Python 生态的配色风格一致
  
- **强调色**：Amber 渐变 (#FBBF24 → #F59E0B)
  - 用于闪电符号
  - 代表速度、能量、活力
  
- **辅助色**：
  - 白色 (#FFFFFF) - 清晰、简洁
  - 灰色 (#64748B) - 副标题文字

## 📐 使用规范

### 最小尺寸

- 标准 Logo：不小于 80x80px
- 横版 Logo：不小于 200x50px
- 图标 Logo：不小于 32x32px

### 留白空间

Logo 周围应保留至少 Logo 高度 10% 的留白空间，确保视觉呼吸感。

### 背景使用

1. **浅色背景**（推荐）
   - 白色、浅灰色、浅蓝色
   - Logo 颜色保持原样

2. **深色背景**
   - 如需在深色背景使用，建议添加白色描边
   - 或使用反色版本（待创建）

### 禁止行为

❌ 不要改变 Logo 的颜色方案  
❌ 不要拉伸或压缩 Logo 比例  
❌ 不要旋转 Logo（除非特殊设计需要）  
❌ 不要在 Logo 上添加效果或滤镜  
❌ 不要将 Logo 放置在干扰视觉的背景上  

## 🖼️ 应用示例

### GitHub README

```markdown
<p align="center">
  <img src="assets/logo.svg" alt="Crawlo Logo" width="150"/>
</p>

<h1 align="center">Crawlo</h1>
<p align="center">High-Performance Async Crawler Framework</p>
```

### HTML 网站

```html
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="/assets/logo-icon.svg">

<!-- Header Logo -->
<img src="/assets/logo-horizontal.svg" alt="Crawlo" height="40">
```

### 文档标题

```markdown
![Crawlo](assets/logo-horizontal.svg)
```

## 🎯 设计特点

1. **可扩展性**
   - SVG 矢量格式，任意缩放不失真
   - 适配各种尺寸和场景

2. **现代感**
   - 渐变色设计符合现代审美
   - 简洁的图形语言
   - 发光效果增强科技感

3. **辨识度**
   - 独特的蜘蛛 + 闪电组合
   - 鲜明的配色方案
   - 清晰的视觉层次

4. **专业性**
   - 符合技术产品的视觉规范
   - 与 Python 生态风格统一
   - 适合开源项目的气质

## 📝 版本记录

- **v1.0** (2025-10-26)
  - 初始设计发布
  - 包含标准版、横版、图标版三个版本
  - 确定主配色方案和设计元素

## 📄 许可证

本 Logo 设计遵循 Crawlo 项目的开源许可证。在遵守许可证条款的前提下，可以自由使用。

---


**code file end: assets/README.md**

---


### code file start: crawlo/cli.py 

```python
# crawlo/cli.py
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import argparse
from crawlo.commands import get_commands
from crawlo.utils.config_manager import EnvConfigManager


def main():
    # 获取框架版本号
    VERSION = EnvConfigManager.get_version()

    # 获取所有可用命令
    commands = get_commands()

    # 创建主解析器
    parser = argparse.ArgumentParser(
        description="Crawlo: A lightweight web crawler framework.",
        usage="crawlo <command> [options]",
        add_help=False  # 禁用默认帮助，我们自己处理
    )
    
    # 添加帮助参数
    parser.add_argument('-h', '--help', action='store_true', help='显示帮助信息')
    parser.add_argument('-v', '--version', action='store_true', help='显示版本信息')
    parser.add_argument('command', nargs='?', help='可用命令: ' + ', '.join(commands.keys()))
    
    # 解析已知参数
    args, unknown = parser.parse_known_args()

    # 处理版本参数
    if args.version:
        print(f"Crawlo {VERSION}")
        sys.exit(0)

    # 处理帮助参数
    if args.help or (args.command is None and not unknown):
        # 导入并运行帮助命令
        try:
            module = __import__(commands['help'], fromlist=['main'])
            sys.exit(module.main([]))
        except ImportError as e:
            print(f"Failed to load help command: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Help command failed: {e}")
            sys.exit(1)

    # 检查命令是否存在
    if args.command not in commands:
        print(f"Unknown command: {args.command}")
        print(f"Available commands: {', '.join(commands.keys())}")
        # 显示帮助信息
        try:
            module = __import__(commands['help'], fromlist=['main'])
            module.main([])
        except:
            pass
        sys.exit(1)

    # 动态导入并执行命令
    try:
        module = __import__(commands[args.command], fromlist=['main'])
        # 将未知参数传递给子命令
        sys.exit(module.main(unknown))
    except ImportError as e:
        print(f"Failed to load command '{args.command}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Command '{args.command}' failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
```

**code file end: crawlo/cli.py**

---


### code file start: crawlo/config.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawlo 配置工厂
===============
提供优雅的配置方式，让用户能够轻松选择运行模式。

使用示例：
    # 单机模式（默认）
    config = CrawloConfig.standalone()
    
    # 分布式模式
    config = CrawloConfig.distributed(redis_host='192.168.1.100')
    
    # 自动检测模式
    config = CrawloConfig.auto()
    
    # 从环境变量
    config = CrawloConfig.from_env()
"""

from typing import Dict, Any, Optional

from crawlo.config_validator import validate_config
from crawlo.mode_manager import standalone_mode, distributed_mode, auto_mode, from_env
from crawlo.logging import get_logger


class CrawloConfig:
    """Crawlo 配置工厂类"""
    
    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        self.logger = get_logger(self.__class__.__name__)
        # 验证配置
        self._validate_settings()
    
    def _validate_settings(self):
        """验证配置"""
        is_valid, errors, warnings = validate_config(self.settings)
        if not is_valid:
            error_msg = "配置验证失败:\n" + "\n".join([f"  - {error}" for error in errors])
            raise ValueError(error_msg)
        
        if warnings:
            warning_msg = "配置警告:\n" + "\n".join([f"  - {warning}" for warning in warnings])
            self.logger.warning(warning_msg)
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any) -> 'CrawloConfig':
        """设置配置项（链式调用）
        
        注意：设置后会自动验证配置合法性
        """
        self.settings[key] = value
        self._validate_settings()  # 自动验证
        return self
    
    def update(self, settings: Dict[str, Any]) -> 'CrawloConfig':
        """更新配置（链式调用）
        
        注意：更新后会自动验证配置合法性
        """
        self.settings.update(settings)
        self._validate_settings()  # 自动验证
        return self
    
    def set_concurrency(self, concurrency: int) -> 'CrawloConfig':
        """设置并发数"""
        return self.set('CONCURRENCY', concurrency)
    
    def set_delay(self, delay: float) -> 'CrawloConfig':
        """设置请求延迟"""
        return self.set('DOWNLOAD_DELAY', delay)
    
    def enable_debug(self) -> 'CrawloConfig':
        """启用调试模式"""
        return self.set('LOG_LEVEL', 'DEBUG')
    
    def enable_mysql(self) -> 'CrawloConfig':
        """启用 MySQL 存储"""
        pipelines = self.get('PIPELINES', [])
        if 'crawlo.pipelines.mysql_pipeline.AsyncmyMySQLPipeline' not in pipelines:
            pipelines.append('crawlo.pipelines.mysql_pipeline.AsyncmyMySQLPipeline')
        return self.set('PIPELINES', pipelines)
    
    def set_redis_host(self, host: str) -> 'CrawloConfig':
        """设置 Redis 主机"""
        return self.set('REDIS_HOST', host)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return self.settings.copy()
    
    def print_summary(self) -> 'CrawloConfig':
        """打印配置摘要"""
        mode_info = {
            'memory': '单机模式',
            'redis': '分布式模式', 
            'auto': '自动检测模式'
        }
        
        queue_type = self.settings.get('QUEUE_TYPE', 'auto')
        filter_class = self.settings.get('FILTER_CLASS', '').split('.')[-1]
        concurrency = self.settings.get('CONCURRENCY', 8)
        
        print("=" * 50)
        print(f"Crawlo 配置摘要")
        print("=" * 50)
        print(f"运行模式: {mode_info.get(queue_type, queue_type)}")
        print(f"队列类型: {queue_type}")
        print(f"去重方式: {filter_class}")
        print(f"并发数量: {concurrency}")
        
        if queue_type == 'redis':
            redis_host = self.settings.get('REDIS_HOST', 'localhost')
            print(f"Redis 服务器: {redis_host}")
        
        print("=" * 50)
        return self
    
    def validate(self) -> bool:
        """验证当前配置"""
        is_valid, errors, warnings = validate_config(self.settings)
        if not is_valid:
            print("配置验证失败:")
            for error in errors:
                print(f"  - {error}")
            return False
        
        if warnings:
            print("配置警告:")
            for warning in warnings:
                print(f"  - {warning}")
        
        return True
    
    # ==================== 静态工厂方法 ====================
    
    @staticmethod
    def standalone(
        concurrency: int = 8,
        download_delay: float = 1.0,
        **kwargs
    ) -> 'CrawloConfig':
        """
        创建单机模式配置
        
        Args:
            concurrency: 并发数
            download_delay: 下载延迟
            **kwargs: 其他配置项
        """
        settings = standalone_mode(
            CONCURRENCY=concurrency,
            DOWNLOAD_DELAY=download_delay,
            **kwargs
        )
        return CrawloConfig(settings)
    
    @staticmethod
    def distributed(
        redis_host: str = '127.0.0.1',
        redis_port: int = 6379,
        redis_password: Optional[str] = None,
        redis_db: int = 0,  # 添加 redis_db 参数
        project_name: str = 'crawlo',
        concurrency: int = 16,
        download_delay: float = 1.0,
        **kwargs
    ) -> 'CrawloConfig':
        """
        创建分布式模式配置
        
        Args:
            redis_host: Redis 服务器地址
            redis_port: Redis 端口
            redis_password: Redis 密码
            redis_db: Redis 数据库编号
            project_name: 项目名称（用于命名空间）
            concurrency: 并发数
            download_delay: 下载延迟
            **kwargs: 其他配置项
        """
        settings = distributed_mode(
            redis_host=redis_host,
            redis_port=redis_port,
            redis_password=redis_password,
            redis_db=redis_db,  # 传递 redis_db 参数
            project_name=project_name,
            CONCURRENCY=concurrency,
            DOWNLOAD_DELAY=download_delay,
            **kwargs
        )
        return CrawloConfig(settings)
    
    @staticmethod
    def auto(
        concurrency: int = 12,
        download_delay: float = 1.0,
        **kwargs
    ) -> 'CrawloConfig':
        """
        创建自动检测模式配置
        
        Args:
            concurrency: 并发数
            download_delay: 下载延迟
            **kwargs: 其他配置项
        """
        settings = auto_mode(
            CONCURRENCY=concurrency,
            DOWNLOAD_DELAY=download_delay,
            **kwargs
        )
        return CrawloConfig(settings)
    
    @staticmethod
    def from_env(default_mode: str = 'standalone') -> 'CrawloConfig':
        """
        从环境变量创建配置
        
        支持的环境变量：
        - CRAWLO_MODE: 运行模式 (standalone/distributed/auto)
        - REDIS_HOST: Redis 主机
        - REDIS_PORT: Redis 端口
        - REDIS_PASSWORD: Redis 密码
        - CONCURRENCY: 并发数
        - PROJECT_NAME: 项目名称
        """
        settings = from_env(default_mode)
        return CrawloConfig(settings)
    
    @staticmethod
    def custom(settings: Dict[str, Any]) -> 'CrawloConfig':
        """
        创建自定义配置
        
        Args:
            settings: 自定义配置字典
        """
        return CrawloConfig(settings)
    
    @staticmethod
    def presets() -> 'Presets':
        """获取预设配置对象"""
        return Presets()


# ==================== 便利函数 ====================

def create_config(
    mode: str = 'standalone',
    **kwargs
) -> CrawloConfig:
    """
    便利函数：创建配置
    
    Args:
        mode: 运行模式 ('standalone', 'distributed', 'auto')
        **kwargs: 配置参数
    """
    if mode.lower() == 'standalone':
        return CrawloConfig.standalone(**kwargs)
    elif mode.lower() == 'distributed':
        return CrawloConfig.distributed(**kwargs)
    elif mode.lower() == 'auto':
        return CrawloConfig.auto(**kwargs)
    else:
        raise ValueError(f"不支持的运行模式: {mode}")


# ==================== 预设配置 ====================

class Presets:
    """预设配置类"""
    
    @staticmethod
    def development() -> CrawloConfig:
        """开发环境配置"""
        return CrawloConfig.standalone(
            concurrency=4,
            download_delay=2.0,
            LOG_LEVEL='DEBUG',
            STATS_DUMP=True
        )
    
    @staticmethod
    def production() -> CrawloConfig:
        """生产环境配置"""
        return CrawloConfig.auto(
            concurrency=16,
            download_delay=1.0,
            LOG_LEVEL='INFO',
            RETRY_TIMES=5
        )
    
    @staticmethod
    def large_scale(redis_host: str, project_name: str) -> CrawloConfig:
        """大规模分布式配置"""
        return CrawloConfig.distributed(
            redis_host=redis_host,
            project_name=project_name,
            concurrency=32,
            download_delay=0.5,
            SCHEDULER_MAX_QUEUE_SIZE=10000,
            LARGE_SCALE_BATCH_SIZE=2000
        )
    
    @staticmethod
    def gentle() -> CrawloConfig:
        """温和模式配置（避免被封）"""
        return CrawloConfig.standalone(
            concurrency=2,
            download_delay=3.0,
            RANDOMNESS=True,
            RANDOM_RANGE=(2.0, 5.0)
        )
```

**code file end: crawlo/config.py**

---


### code file start: crawlo/config_validator.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
配置验证器
==========
提供配置项的验证和默认值设置功能，确保配置的合理性和一致性。
"""
from typing import Dict, Any, List, Tuple

from crawlo.logging import get_logger


class ConfigValidator:
    """配置验证器"""
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self.errors = []
        self.warnings = []
    
    def validate(self, config: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        验证配置
        
        Args:
            config: 配置字典
            
        Returns:
            Tuple[bool, List[str], List[str]]: (是否有效, 错误列表, 警告列表)
        """
        self.errors = []
        self.warnings = []
        
        # 验证各个配置项
        self._validate_basic_settings(config)
        self._validate_network_settings(config)
        self._validate_concurrency_settings(config)
        self._validate_queue_settings(config)
        self._validate_storage_settings(config)
        self._validate_redis_settings(config)
        self._validate_middleware_settings(config)
        self._validate_pipeline_settings(config)
        self._validate_extension_settings(config)
        self._validate_logging_settings(config)
        
        is_valid = len(self.errors) == 0
        return is_valid, self.errors, self.warnings
    
    def _validate_basic_settings(self, config: Dict[str, Any]):
        """验证基本设置"""
        project_name = config.get('PROJECT_NAME', 'crawlo')
        if not isinstance(project_name, str) or not project_name.strip():
            self.errors.append("PROJECT_NAME 必须是非空字符串")
        
        version = config.get('VERSION', '1.0')
        if not isinstance(version, str):
            self.errors.append("VERSION 必须是字符串")
    
    def _validate_network_settings(self, config: Dict[str, Any]):
        """验证网络设置"""
        # 下载器验证
        downloader = config.get('DOWNLOADER', 'crawlo.downloader.aiohttp_downloader.AioHttpDownloader')
        if not isinstance(downloader, str):
            self.errors.append("DOWNLOADER 必须是字符串")
        
        # 超时设置验证
        timeout = config.get('DOWNLOAD_TIMEOUT', 30)
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            self.errors.append("DOWNLOAD_TIMEOUT 必须是正数")
        
        # 延迟设置验证
        delay = config.get('DOWNLOAD_DELAY', 1.0)
        if not isinstance(delay, (int, float)) or delay < 0:
            self.errors.append("DOWNLOAD_DELAY 必须是非负数")
        
        # 重试次数验证
        max_retries = config.get('MAX_RETRY_TIMES', 3)
        if not isinstance(max_retries, int) or max_retries < 0:
            self.errors.append("MAX_RETRY_TIMES 必须是非负整数")
        
        # 连接池限制验证
        pool_limit = config.get('CONNECTION_POOL_LIMIT', 50)
        if not isinstance(pool_limit, int) or pool_limit <= 0:
            self.errors.append("CONNECTION_POOL_LIMIT 必须是正整数")
    
    def _validate_concurrency_settings(self, config: Dict[str, Any]):
        """验证并发设置"""
        concurrency = config.get('CONCURRENCY', 8)
        if not isinstance(concurrency, int) or concurrency <= 0:
            self.errors.append("CONCURRENCY 必须是正整数")
        
        max_running_spiders = config.get('MAX_RUNNING_SPIDERS', 3)
        if not isinstance(max_running_spiders, int) or max_running_spiders <= 0:
            self.errors.append("MAX_RUNNING_SPIDERS 必须是正整数")
    
    def _validate_queue_settings(self, config: Dict[str, Any]):
        """验证队列设置"""
        queue_type = config.get('QUEUE_TYPE', 'memory')
        valid_queue_types = ['memory', 'redis', 'auto']
        if queue_type not in valid_queue_types:
            self.errors.append(f"QUEUE_TYPE 必须是以下值之一: {valid_queue_types}")
        
        # 队列大小验证
        max_queue_size = config.get('SCHEDULER_MAX_QUEUE_SIZE', 2000)
        if not isinstance(max_queue_size, int) or max_queue_size <= 0:
            self.errors.append("SCHEDULER_MAX_QUEUE_SIZE 必须是正整数")
        
        # 队列名称验证（如果是Redis队列）
        if queue_type == 'redis':
            queue_name = config.get('SCHEDULER_QUEUE_NAME', '')
            if not queue_name:
                self.errors.append("使用Redis队列时，SCHEDULER_QUEUE_NAME 不能为空")
            elif not self._is_valid_redis_key(queue_name):
                self.warnings.append(f"Redis队列名称 '{queue_name}' 不符合命名规范，建议使用 'crawlo:{config.get('PROJECT_NAME', 'project')}:queue:requests' 格式")
    
    def _validate_storage_settings(self, config: Dict[str, Any]):
        """验证存储设置"""
        # MySQL设置验证
        mysql_host = config.get('MYSQL_HOST')
        if mysql_host is not None and not isinstance(mysql_host, str):
            self.errors.append("MYSQL_HOST 必须是字符串")
        
        mysql_port = config.get('MYSQL_PORT')
        if mysql_port is not None and (not isinstance(mysql_port, int) or mysql_port <= 0 or mysql_port > 65535):
            self.errors.append("MYSQL_PORT 必须是1-65535之间的整数")
        
        # MongoDB设置验证
        mongo_uri = config.get('MONGO_URI')
        if mongo_uri is not None and not isinstance(mongo_uri, str):
            self.errors.append("MONGO_URI 必须是字符串")
    
    def _validate_redis_settings(self, config: Dict[str, Any]):
        """验证Redis设置"""
        queue_type = config.get('QUEUE_TYPE', 'memory')
        if queue_type == 'redis':
            # Redis主机验证
            redis_host = config.get('REDIS_HOST', '127.0.0.1')
            if not isinstance(redis_host, str) or not redis_host.strip():
                self.errors.append("REDIS_HOST 必须是非空字符串")
            
            # Redis端口验证
            redis_port = config.get('REDIS_PORT', 6379)
            if not isinstance(redis_port, int) or redis_port <= 0 or redis_port > 65535:
                self.errors.append("REDIS_PORT 必须是1-65535之间的整数")
            
            # Redis URL验证
            redis_url = config.get('REDIS_URL')
            if redis_url is not None and not isinstance(redis_url, str):
                self.errors.append("REDIS_URL 必须是字符串")
            
            # Redis队列名称验证（提供默认值）
            scheduler_queue_name = config.get('SCHEDULER_QUEUE_NAME')
            project_name = config.get('PROJECT_NAME', 'crawlo')
            if scheduler_queue_name is None:
                # 如果没有设置，使用默认值
                scheduler_queue_name = f'crawlo:{project_name}:queue:requests'
            
            if not scheduler_queue_name:
                self.errors.append("使用Redis队列时，SCHEDULER_QUEUE_NAME 不能为空")
            elif not self._is_valid_redis_key(scheduler_queue_name):
                self.warnings.append(f"Redis队列名称 '{scheduler_queue_name}' 不符合命名规范，建议使用 'crawlo:{project_name}:queue:requests' 格式")
    
    def _validate_middleware_settings(self, config: Dict[str, Any]):
        """验证中间件设置"""
        # 验证 MIDDLEWARES
        middlewares = config.get('MIDDLEWARES', [])
        if not isinstance(middlewares, list):
            self.errors.append("MIDDLEWARES 必须是列表")
        else:
            for i, middleware in enumerate(middlewares):
                if not isinstance(middleware, str):
                    self.errors.append(f"MIDDLEWARES[{i}] 必须是字符串")
    
    def _validate_pipeline_settings(self, config: Dict[str, Any]):
        """验证管道设置"""
        # 验证 PIPELINES
        pipelines = config.get('PIPELINES', [])
        if not isinstance(pipelines, list):
            self.errors.append("PIPELINES 必须是列表")
        else:
            for i, pipeline in enumerate(pipelines):
                if not isinstance(pipeline, str):
                    self.errors.append(f"PIPELINES[{i}] 必须是字符串")
    
    def _validate_extension_settings(self, config: Dict[str, Any]):
        """验证扩展设置"""
        # 验证 EXTENSIONS
        extensions = config.get('EXTENSIONS', [])
        if not isinstance(extensions, list):
            self.errors.append("EXTENSIONS 必须是列表")
        else:
            for i, extension in enumerate(extensions):
                if not isinstance(extension, str):
                    self.errors.append(f"EXTENSIONS[{i}] 必须是字符串")
    
    def _validate_logging_settings(self, config: Dict[str, Any]):
        """验证日志设置"""
        log_level = config.get('LOG_LEVEL', 'INFO')
        valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if log_level not in valid_log_levels:
            self.errors.append(f"LOG_LEVEL 必须是以下值之一: {valid_log_levels}")
        
        log_file = config.get('LOG_FILE')
        if log_file is not None and not isinstance(log_file, str):
            self.errors.append("LOG_FILE 必须是字符串")
    
    def _is_valid_redis_key(self, key: str) -> bool:
        """检查Redis key是否符合命名规范"""
        # 检查是否以 crawlo: 开头
        if not key.startswith('crawlo:'):
            return False
        
        # 检查是否包含必要的部分
        parts = key.split(':')
        if len(parts) < 3:
            return False
        
        # 检查是否包含 queue 部分
        return 'queue' in parts
    
    def get_validation_report(self, config: Dict[str, Any]) -> str:
        """
        获取验证报告
        
        Args:
            config: 配置字典
            
        Returns:
            str: 验证报告
        """
        is_valid, errors, warnings = self.validate(config)
        
        report = []
        report.append("=" * 50)
        report.append("配置验证报告")
        report.append("=" * 50)
        
        if is_valid:
            report.append("配置验证通过")
        else:
            report.append("配置验证失败")
            report.append("错误:")
            for error in errors:
                report.append(f"  - {error}")
        
        if warnings:
            report.append("警告:")
            for warning in warnings:
                report.append(f"  - {warning}")
        
        report.append("=" * 50)
        return "\n".join(report)


# 便利函数
def validate_config(config: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
    """
    验证配置
    
    Args:
        config: 配置字典
        
    Returns:
        Tuple[bool, List[str], List[str]]: (是否有效, 错误列表, 警告列表)
    """
    validator = ConfigValidator()
    return validator.validate(config)


def print_validation_report(config: Dict[str, Any]):
    """
    打印验证报告
    
    Args:
        config: 配置字典
    """
    validator = ConfigValidator()
    print(validator.get_validation_report(config))
```

**code file end: crawlo/config_validator.py**

---


### code file start: crawlo/crawler.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawler系统
==========

核心组件：
- Crawler: 爬虫核心控制器，负责单个爬虫的生命周期管理
- CrawlerProcess: 爬虫进程管理器，支持单个/多个爬虫运行

设计原则：
1. 单一职责 - 每个类只负责一个明确的功能
2. 依赖注入 - 通过工厂创建组件，便于测试
3. 状态管理 - 清晰的状态转换和生命周期
4. 错误处理 - 优雅的错误处理和恢复机制
5. 资源管理 - 统一的资源注册和清理机制
"""

import asyncio
import time
from enum import Enum
from dataclasses import dataclass
from contextlib import asynccontextmanager
from typing import Optional, Type, Dict, Any, List

from crawlo.logging import get_logger
from crawlo.factories import get_component_registry
from crawlo.initialization import initialize_framework, is_framework_ready
from crawlo.utils.resource_manager import ResourceManager, ResourceType


class CrawlerState(Enum):
    """Crawler状态枚举"""
    CREATED = "created"
    INITIALIZING = "initializing"
    READY = "ready"
    RUNNING = "running"
    CLOSING = "closing"
    CLOSED = "closed"
    ERROR = "error"


@dataclass
class CrawlerMetrics:
    """Crawler性能指标"""
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    initialization_duration: float = 0.0
    crawl_duration: float = 0.0
    request_count: int = 0
    success_count: int = 0
    error_count: int = 0
    
    def get_total_duration(self) -> float:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0.0
    
    def get_success_rate(self) -> float:
        total = self.success_count + self.error_count
        return (self.success_count / total * 100) if total > 0 else 0.0


class Crawler:
    """
    爬虫核心控制器
    
    特点：
    1. 清晰的状态管理
    2. 依赖注入
    3. 组件化架构
    4. 完善的错误处理
    5. 统一的资源管理
    """
    
    def __init__(self, spider_cls: Type, settings=None):
        self._spider_cls = spider_cls
        self._settings = settings
        self._state = CrawlerState.CREATED
        self._state_lock = asyncio.Lock()
        
        # 组件
        self._spider = None
        self._engine = None
        self._stats = None
        self._subscriber = None
        self._extension = None
        
        # 指标
        self._metrics = CrawlerMetrics()
        
        # 资源管理器
        self._resource_manager = ResourceManager(name=f"crawler.{spider_cls.__name__ if spider_cls else 'unknown'}")
        
        # 日志
        self._logger = get_logger(f'crawler.{spider_cls.__name__ if spider_cls else "unknown"}')
        
        # 确保框架已初始化
        self._ensure_framework_ready()
    
    def _ensure_framework_ready(self):
        """确保框架已准备就绪"""
        if not is_framework_ready():
            try:
                self._settings = initialize_framework(self._settings)
                self._logger.debug("Framework initialized successfully")
            except Exception as e:
                self._logger.warning(f"Framework initialization failed: {e}")
                # 使用降级策略
                if not self._settings:
                    from crawlo.settings.setting_manager import SettingManager
                    self._settings = SettingManager()
        
        # 确保是SettingManager实例
        if isinstance(self._settings, dict):
            from crawlo.settings.setting_manager import SettingManager
            settings_manager = SettingManager()
            settings_manager.update_attributes(self._settings)
            self._settings = settings_manager
    
    @property
    def state(self) -> CrawlerState:
        """获取当前状态"""
        return self._state
    
    @property
    def spider(self):
        """获取Spider实例"""
        return self._spider
    
    @property
    def stats(self):
        """获取Stats实例（向后兼容）"""
        return self._stats
    
    @property 
    def metrics(self) -> CrawlerMetrics:
        """获取性能指标"""
        return self._metrics
    
    @property
    def settings(self):
        """获取配置"""
        return self._settings
    
    @property
    def engine(self):
        """获取Engine实例（向后兼容）"""
        return self._engine
    
    @property
    def subscriber(self):
        """获取Subscriber实例（向后兼容）"""
        return self._subscriber
    
    @property
    def extension(self):
        """获取Extension实例（向后兼容）"""
        return self._extension
    
    @extension.setter
    def extension(self, value):
        """设置Extension实例（向后兼容）"""
        self._extension = value
    
    def _create_extension(self):
        """创建Extension管理器（向后兼容）"""
        if self._extension is None:
            try:
                registry = get_component_registry()
                self._extension = registry.create('extension_manager', crawler=self)
            except Exception as e:
                self._logger.warning(f"Failed to create extension manager: {e}")
        return self._extension
    
    async def close(self):
        """关闭爹虫（向后兼容）"""
        await self._cleanup()
    
    async def crawl(self):
        """执行爬取任务"""
        async with self._lifecycle_manager():
            await self._initialize_components()
            await self._run_crawler()
    
    @asynccontextmanager
    async def _lifecycle_manager(self):
        """生命周期管理"""
        self._metrics.start_time = time.time()
        
        try:
            yield
        except Exception as e:
            await self._handle_error(e)
            raise
        finally:
            await self._cleanup()
            self._metrics.end_time = time.time()
    
    async def _initialize_components(self):
        """初始化组件"""
        async with self._state_lock:
            if self._state != CrawlerState.CREATED:
                raise RuntimeError(f"Cannot initialize from state {self._state}")
            
            self._state = CrawlerState.INITIALIZING
        
        init_start = time.time()
        
        try:
            # 使用组件工厂创建组件
            registry = get_component_registry()
            
            # 创建Subscriber（无依赖）
            self._subscriber = registry.create('subscriber')
            
            # 创建Spider
            self._spider = self._create_spider()
            
            # 创建Engine（需要crawler参数）
            self._engine = registry.create('engine', crawler=self)
            # 注册Engine到资源管理器
            if self._engine and hasattr(self._engine, 'close'):
                self._resource_manager.register(
                    self._engine,
                    lambda e: e.close() if hasattr(e, 'close') else None,
                    ResourceType.OTHER,
                    name="engine"
                )
            
            # 创建Stats（需要crawler参数）
            self._stats = registry.create('stats', crawler=self)
            
            # 创建Extension Manager (可选，需要crawler参数)
            try:
                self._extension = registry.create('extension_manager', crawler=self)
            except Exception as e:
                self._logger.warning(f"Failed to create extension manager: {e}")
            
            self._metrics.initialization_duration = time.time() - init_start
            
            async with self._state_lock:
                self._state = CrawlerState.READY
            
            self._logger.debug(f"Crawler components initialized successfully in {self._metrics.initialization_duration:.2f}s")
            
        except Exception as e:
            async with self._state_lock:
                self._state = CrawlerState.ERROR
            raise RuntimeError(f"Component initialization failed: {e}")
    
    def _create_spider(self):
        """创建Spider实例"""
        if not self._spider_cls:
            raise ValueError("Spider class not provided")
        
        # 检查Spider类的有效性
        if not hasattr(self._spider_cls, 'name'):
            raise ValueError("Spider class must have 'name' attribute")
        
        # 创建Spider实例
        spider = self._spider_cls()
        
        # 设置crawler引用
        if hasattr(spider, 'crawler'):
            spider.crawler = self
        
        return spider
    
    async def _run_crawler(self):
        """运行爬虫引擎"""
        async with self._state_lock:
            if self._state != CrawlerState.READY:
                raise RuntimeError(f"Cannot run from state {self._state}")
            
            self._state = CrawlerState.RUNNING
        
        crawl_start = time.time()
        
        try:
            # 启动引擎
            if self._engine:
                await self._engine.start_spider(self._spider)
            else:
                raise RuntimeError("Engine not initialized")
            
            self._metrics.crawl_duration = time.time() - crawl_start
            
            self._logger.info(f"Crawler completed successfully in {self._metrics.crawl_duration:.2f}s")
            
        except Exception as e:
            self._metrics.crawl_duration = time.time() - crawl_start
            raise RuntimeError(f"Crawler execution failed: {e}")
    
    async def _handle_error(self, error: Exception):
        """处理错误"""
        async with self._state_lock:
            self._state = CrawlerState.ERROR
        
        self._metrics.error_count += 1
        self._logger.error(f"Crawler error: {error}", exc_info=True)
        
        # 这里可以添加错误恢复逻辑
    
    async def _cleanup(self):
        """清理资源"""
        async with self._state_lock:
            if self._state not in [CrawlerState.CLOSING, CrawlerState.CLOSED]:
                self._state = CrawlerState.CLOSING
        
        try:
            # 使用资源管理器统一清理
            self._logger.debug("开始清理Crawler资源...")
            cleanup_result = await self._resource_manager.cleanup_all()
            self._logger.debug(
                f"资源清理完成: {cleanup_result['success']}成功, "
                f"{cleanup_result['errors']}失败, 耗时{cleanup_result['duration']:.2f}s"
            )
            
            # 关闭各个组件（继续兼容旧逻辑）
            if self._engine and hasattr(self._engine, 'close'):
                try:
                    await self._engine.close()
                except Exception as e:
                    self._logger.warning(f"Engine cleanup failed: {e}")
            
            # 调用Spider的spider_closed方法
            if self._spider:
                try:
                    if asyncio.iscoroutinefunction(self._spider.spider_closed):
                        await self._spider.spider_closed()
                    else:
                        self._spider.spider_closed()
                except Exception as e:
                    self._logger.warning(f"Spider cleanup failed: {e}")
            
            # 调用StatsCollector的close_spider方法，设置reason和spider_name
            if self._stats and hasattr(self._stats, 'close_spider'):
                try:
                    # 使用默认的'finished'作为reason
                    self._stats.close_spider(self._spider, reason='finished')
                except Exception as e:
                    self._logger.warning(f"Stats close_spider failed: {e}")
            
            # 触发spider_closed事件，通知所有订阅者（包括扩展）
            # 传递reason参数，这里使用默认的'finished'作为reason
            if self.subscriber:
                from crawlo.event import CrawlerEvent
                await self.subscriber.notify(CrawlerEvent.SPIDER_CLOSED, reason='finished')
            
            if self._stats and hasattr(self._stats, 'close'):
                try:
                    close_result = self._stats.close()
                    if asyncio.iscoroutine(close_result):
                        await close_result
                except Exception as e:
                    self._logger.warning(f"Stats cleanup failed: {e}")
            
            async with self._state_lock:
                self._state = CrawlerState.CLOSED
            
            self._logger.debug("Crawler cleanup completed")
            
        except Exception as e:
            self._logger.error(f"Cleanup error: {e}")


class CrawlerProcess:
    """
    Crawler进程管理器 - 管理多个Crawler的执行
    
    简化版本，专注于核心功能
    """
    
    def __init__(self, settings=None, max_concurrency: int = 3, spider_modules=None):
        # 初始化框架配置
        self._settings = settings or initialize_framework()
        self._max_concurrency = max_concurrency
        self._crawlers: List[Crawler] = []
        self._semaphore = asyncio.Semaphore(max_concurrency)
        self._logger = get_logger('crawler.process')
        
        # 如果没有显式提供spider_modules，则从settings中获取
        if spider_modules is None and self._settings:
            spider_modules = self._settings.get('SPIDER_MODULES', [])
            self._logger.debug(f"从settings中获取SPIDER_MODULES: {spider_modules}")
        
        self._spider_modules = spider_modules or []  # 保存spider_modules
        
        # 如果提供了spider_modules，自动注册这些模块中的爬虫
        if self._spider_modules:
            self._register_spider_modules(self._spider_modules)
        
        # 指标
        self._start_time: Optional[float] = None
        self._end_time: Optional[float] = None
    
    def _register_spider_modules(self, spider_modules):
        """注册爬虫模块"""
        try:
            from crawlo.spider import get_global_spider_registry
            registry = get_global_spider_registry()
            
            self._logger.debug(f"Registering spider modules: {spider_modules}")
            
            initial_spider_count = len(registry)
            
            for module_path in spider_modules:
                try:
                    # 导入模块
                    __import__(module_path)
                    self._logger.debug(f"Successfully imported spider module: {module_path}")
                except ImportError as e:
                    self._logger.warning(f"Failed to import spider module {module_path}: {e}")
                    # 如果导入失败，尝试自动发现
                    self._auto_discover_spider_modules([module_path])
            
            # 检查注册表中的爬虫
            spider_names = list(registry.keys())
            self._logger.debug(f"Registered spiders after import: {spider_names}")
            
            # 如果导入模块后没有新的爬虫被注册，则尝试自动发现
            final_spider_count = len(registry)
            if final_spider_count == initial_spider_count:
                self._logger.debug("No new spiders registered after importing modules, attempting auto-discovery")
                self._auto_discover_spider_modules(spider_modules)
                spider_names = list(registry.keys())
                self._logger.debug(f"Registered spiders after auto-discovery: {spider_names}")
        except Exception as e:
            self._logger.warning(f"Error registering spider modules: {e}")
    
    def _auto_discover_spider_modules(self, spider_modules):
        """
        自动发现并导入爬虫模块中的所有爬虫
        这个方法会扫描指定模块目录下的所有Python文件并自动导入
        """
        try:
            from crawlo.spider import get_global_spider_registry
            import importlib
            from pathlib import Path
            import sys
            
            registry = get_global_spider_registry()
            initial_spider_count = len(registry)
            
            for module_path in spider_modules:
                try:
                    # 将模块路径转换为文件系统路径
                    # 例如: ofweek_standalone.spiders -> ofweek_standalone/spiders
                    package_parts = module_path.split('.')
                    if len(package_parts) < 2:
                        continue
                        
                    # 获取项目根目录
                    project_root = None
                    for path in sys.path:
                        if path and Path(path).exists():
                            possible_module_path = Path(path) / package_parts[0]
                            if possible_module_path.exists():
                                project_root = path
                                break
                    
                    if not project_root:
                        # 尝试使用当前工作目录
                        project_root = str(Path.cwd())
                    
                    # 构建模块目录路径
                    module_dir = Path(project_root)
                    for part in package_parts:
                        module_dir = module_dir / part
                    
                    # 如果目录存在，扫描其中的Python文件
                    if module_dir.exists() and module_dir.is_dir():
                        # 导入目录下的所有Python文件（除了__init__.py）
                        for py_file in module_dir.glob("*.py"):
                            if py_file.name.startswith('_'):
                                continue
                                
                            # 构造模块名
                            module_name = py_file.stem  # 文件名（不含扩展名）
                            full_module_path = f"{module_path}.{module_name}"
                            
                            try:
                                # 导入模块以触发Spider注册
                                importlib.import_module(full_module_path)
                            except ImportError as e:
                                self._logger.warning(f"Failed to auto-import spider module {full_module_path}: {e}")
                except Exception as e:
                    self._logger.warning(f"Error during auto-discovery for module {module_path}: {e}")
            
            # 检查是否有新的爬虫被注册
            final_spider_count = len(registry)
            if final_spider_count > initial_spider_count:
                new_spiders = list(registry.keys())
                self._logger.info(f"Auto-discovered {final_spider_count - initial_spider_count} new spiders: {new_spiders}")
                
        except Exception as e:
            self._logger.warning(f"Error during auto-discovery of spider modules: {e}")
    
    def is_spider_registered(self, name: str) -> bool:
        """检查爬虫是否已注册"""
        from crawlo.spider import get_global_spider_registry
        registry = get_global_spider_registry()
        return name in registry
    
    def get_spider_class(self, name: str):
        """获取爬虫类"""
        from crawlo.spider import get_global_spider_registry
        registry = get_global_spider_registry()
        return registry.get(name)
    
    def get_spider_names(self):
        """获取所有注册的爬虫名称"""
        from crawlo.spider import get_global_spider_registry
        registry = get_global_spider_registry()
        return list(registry.keys())
    
    async def crawl(self, spider_cls_or_name, settings=None):
        """运行单个爬虫"""
        spider_cls = self._resolve_spider_class(spider_cls_or_name)
        
        # 记录启动的爬虫名称（符合规范要求）
        from crawlo.logging import get_logger
        logger = get_logger('crawlo.framework')
        logger.info(f"Starting spider: {spider_cls.name}")
        
        merged_settings = self._merge_settings(settings)
        crawler = Crawler(spider_cls, merged_settings)
        
        async with self._semaphore:
            await crawler.crawl()
        
        return crawler
    
    async def crawl_multiple(self, spider_classes_or_names, settings=None):
        """运行多个爬虫"""
        self._start_time = time.time()
        
        try:
            spider_classes = []
            for cls_or_name in spider_classes_or_names:
                spider_cls = self._resolve_spider_class(cls_or_name)
                spider_classes.append(spider_cls)
            
            # 记录启动的爬虫名称（符合规范要求）
            spider_names = [cls.name for cls in spider_classes]
            from crawlo.logging import get_logger
            logger = get_logger('crawlo.framework')
            if len(spider_names) == 1:
                logger.info(f"Starting spider: {spider_names[0]}")
            else:
                logger.info(f"Starting spiders: {', '.join(spider_names)}")
            
            tasks = []
            for spider_cls in spider_classes:
                merged_settings = self._merge_settings(settings)
                crawler = Crawler(spider_cls, merged_settings)
                self._crawlers.append(crawler)
                
                task = asyncio.create_task(self._run_with_semaphore(crawler))
                tasks.append(task)
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # 处理结果
            successful = sum(1 for r in results if not isinstance(r, Exception))
            failed = len(results) - successful
            
            self._logger.info(f"Crawl completed: {successful} successful, {failed} failed")
            
            return results
            
        finally:
            # 清理所有crawler，防止资源累积
            self._logger.debug(f"Cleaning up {len(self._crawlers)} crawler(s)...")
            for crawler in self._crawlers:
                try:
                    # 确保每个crawler都被清理
                    if hasattr(crawler, '_resource_manager'):
                        await crawler._resource_manager.cleanup_all()
                except Exception as e:
                    self._logger.warning(f"Failed to cleanup crawler: {e}")
            
            # 清空crawlers列表，释放引用
            self._crawlers.clear()
            
            self._end_time = time.time()
            if self._start_time:
                duration = self._end_time - self._start_time
                self._logger.info(f"Total execution time: {duration:.2f}s")
    
    async def _run_with_semaphore(self, crawler: Crawler):
        """在信号量控制下运行爬虫"""
        async with self._semaphore:
            await crawler.crawl()
            return crawler
    
    def _resolve_spider_class(self, spider_cls_or_name):
        """解析Spider类"""
        if isinstance(spider_cls_or_name, str):
            # 从注册表中查找
            try:
                from crawlo.spider import get_global_spider_registry
                registry = get_global_spider_registry()
                if spider_cls_or_name in registry:
                    return registry[spider_cls_or_name]
                else:
                    # 如果在注册表中找不到，尝试通过spider_modules导入所有模块来触发注册
                    # 然后再次检查注册表
                    if hasattr(self, '_spider_modules') and self._spider_modules:
                        for module_path in self._spider_modules:
                            try:
                                # 导入模块来触发爬虫注册
                                __import__(module_path)
                            except ImportError:
                                pass  # 忽略导入错误
                        
                        # 再次检查注册表
                        if spider_cls_or_name in registry:
                            return registry[spider_cls_or_name]
                    
                    # 如果仍然找不到，尝试自动发现模式
                    if hasattr(self, '_spider_modules') and self._spider_modules:
                        self._auto_discover_spider_modules(self._spider_modules)
                        if spider_cls_or_name in registry:
                            return registry[spider_cls_or_name]
                    
                    # 如果仍然找不到，尝试直接导入模块
                    try:
                        # 假设格式为 module.SpiderClass
                        if '.' in spider_cls_or_name:
                            module_path, class_name = spider_cls_or_name.rsplit('.', 1)
                            module = __import__(module_path, fromlist=[class_name])
                            spider_class = getattr(module, class_name)
                            # 注册到全局注册表
                            registry[spider_class.name] = spider_class
                            return spider_class
                        else:
                            # 尝试在spider_modules中查找
                            if hasattr(self, '_spider_modules') and self._spider_modules:
                                for module_path in self._spider_modules:
                                    try:
                                        # 构造完整的模块路径
                                        full_module_path = f"{module_path}.{spider_cls_or_name}"
                                        module = __import__(full_module_path, fromlist=[spider_cls_or_name])
                                        # 获取模块中的Spider子类
                                        for attr_name in dir(module):
                                            attr_value = getattr(module, attr_name)
                                            if (isinstance(attr_value, type) and
                                                    issubclass(attr_value, registry.__class__.__bases__[0]) and
                                                    hasattr(attr_value, 'name') and
                                                    attr_value.name == spider_cls_or_name):
                                                # 注册到全局注册表
                                                registry[spider_cls_or_name] = attr_value
                                                return attr_value
                                    except ImportError:
                                        continue
                            raise ValueError(f"Spider '{spider_cls_or_name}' not found in registry")
                    except (ImportError, AttributeError):
                        raise ValueError(f"Spider '{spider_cls_or_name}' not found in registry")
            except ImportError:
                raise ValueError(f"Cannot resolve spider name '{spider_cls_or_name}'")
        else:
            return spider_cls_or_name
    
    def _merge_settings(self, additional_settings):
        """合并配置"""
        if not additional_settings:
            return self._settings
        
        # 这里可以实现更复杂的配置合并逻辑
        from crawlo.settings.setting_manager import SettingManager
        merged = SettingManager()
        
        # 复制基础配置
        if self._settings:
            merged.update_attributes(self._settings.__dict__)
        
        # 应用额外配置
        merged.update_attributes(additional_settings)
        
        return merged
    
    def get_metrics(self) -> Dict[str, Any]:
        """获取整体指标"""
        total_duration = 0.0
        if self._start_time and self._end_time:
            total_duration = self._end_time - self._start_time
        
        crawler_metrics = [crawler.metrics for crawler in self._crawlers]
        
        return {
            'total_duration': total_duration,
            'crawler_count': len(self._crawlers),
            'total_requests': sum(m.request_count for m in crawler_metrics),
            'total_success': sum(m.success_count for m in crawler_metrics),
            'total_errors': sum(m.error_count for m in crawler_metrics),
            'average_success_rate': sum(m.get_success_rate() for m in crawler_metrics) / len(crawler_metrics) if crawler_metrics else 0.0
        }
```

**code file end: crawlo/crawler.py**

---


### code file start: crawlo/event.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Crawlo 事件系统
==============
定义框架中的所有事件类型，支持类型安全和IDE自动补全。
"""
from enum import Enum


class CrawlerEvent(str, Enum):
    """
    爬虫事件枚举
    
    所有事件都应该使用此枚举类型，以获得：
    - 类型安全：避免拼写错误
    - IDE支持：自动补全和提示
    - 文档化：集中管理所有事件
    
    使用示例：
        >>> from crawlo.event import CrawlerEvent
        >>> await subscriber.notify(CrawlerEvent.SPIDER_OPENED, spider)
    """
    
    # 爬虫生命周期事件
    SPIDER_OPENED = "spider_opened"      # 爬虫启动
    SPIDER_CLOSED = "spider_closed"      # 爬虫关闭
    SPIDER_ERROR = "spider_error"        # 爬虫错误
    
    # 请求相关事件
    REQUEST_SCHEDULED = "request_scheduled"  # 请求已调度
    IGNORE_REQUEST = "ignore_request"        # 请求被忽略
    
    # 响应相关事件
    RESPONSE_RECEIVED = "response_received"  # 响应已接收
    
    # Item相关事件
    ITEM_SUCCESSFUL = "item_successful"  # Item处理成功
    ITEM_DISCARD = "item_discard"        # Item被丢弃


# 导出所有公共API
__all__ = [
    'CrawlerEvent',
]

```

**code file end: crawlo/event.py**

---


### code file start: crawlo/exceptions.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Crawlo 框架异常定义
===================
提供层次化的异常体系，便于统一处理和类型安全。

异常层次：
    CrawloException (基础异常)
    ├── SpiderException (爬虫相关)
    ├── ComponentInitException (组件初始化)
    ├── DataException (数据处理)
    ├── RequestException (请求/响应)
    ├── OutputException (输出)
    └── ConfigException (配置)

使用示例：
    >>> try:
    ...     # 代码
    ... except CrawloException as e:
    ...     # 捕获所有框架异常
    ... except Exception as e:
    ...     # 其他异常
"""


# ============= 基础异常 =============
class CrawloException(Exception):
    """Crawlo框架基础异常。所有框架异常都应继承此类。"""
    pass


# ============= 爬虫相关异常 =============
class SpiderException(CrawloException):
    """爬虫相关异常基类。"""
    pass


class SpiderTypeError(SpiderException, TypeError):
    """爬虫类型错误。当爬虫类型不符合预期时抛出。"""
    pass


class SpiderCreationError(SpiderException):
    """爬虫实例化失败异常。当无法创建爬虫实例时抛出。"""
    pass


# ============= 组件初始化异常 =============
class ComponentInitException(CrawloException):
    """组件初始化异常基类。"""
    pass


class MiddlewareInitError(ComponentInitException):
    """中间件初始化失败异常。"""
    pass


class PipelineInitError(ComponentInitException):
    """管道初始化失败异常。"""
    pass


class ExtensionInitError(ComponentInitException):
    """扩展初始化失败异常。"""
    pass


# ============= 数据处理异常 =============
class DataException(CrawloException):
    """数据处理异常基类。"""
    pass


class ItemInitError(DataException):
    """Item初始化错误。当Item实例创建失败时抛出。"""
    pass


class ItemAttributeError(DataException, AttributeError):
    """Item属性错误。当访问不存在的Item属性时抛出。"""
    pass


class ItemValidationError(DataException):
    """Item字段验证错误。当Item字段值不符合验证规则时抛出。"""
    pass


class ItemDiscard(DataException):
    """
    Item被丢弃异常。
    
    注意：这不是一个真正的错误，而是用于流程控制，
    表示Item应该被管道丢弃（例如重复数据）。
    """
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


# ============= 请求/响应异常 =============
class RequestException(CrawloException):
    """请求异常基类。"""
    pass


class RequestMethodError(RequestException):
    """请求方法错误。当使用不支持的HTTP方法时抛出。"""
    pass


class IgnoreRequestError(RequestException):
    """
    请求被忽略异常。
    
    用于流程控制，表示请求应该被跳过处理。
    """
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


class DecodeError(RequestException):
    """响应解码错误。当无法解码响应内容时抛出。"""
    pass


# ============= 输出异常 =============
class OutputException(CrawloException):
    """输出异常基类。"""
    pass


class OutputError(OutputException):
    """输出错误。当输出处理失败时抛出。"""
    pass


class InvalidOutputError(OutputException):
    """无效的输出错误。当输出类型或格式不符合预期时抛出。"""
    pass


# ============= 配置异常 =============
class ConfigException(CrawloException):
    """配置异常基类。"""
    pass


class NotConfigured(ConfigException):
    """组件未配置异常。当必需的配置缺失时抛出。"""
    pass


class NotConfiguredError(ConfigException):
    """配置错误异常。当配置值无效时抛出。"""
    pass


# ============= 类型异常 =============
class TransformTypeError(CrawloException, TypeError):
    """转换类型错误。当数据转换类型不匹配时抛出。"""
    pass


class ReceiverTypeError(CrawloException, TypeError):
    """接收者类型错误。当事件接收者类型不符合预期时抛出。"""
    pass


# ============= 导出所有异常 =============
__all__ = [
    # 基础异常
    'CrawloException',
    
    # 爬虫相关
    'SpiderException',
    'SpiderTypeError',
    'SpiderCreationError',
    
    # 组件初始化
    'ComponentInitException',
    'MiddlewareInitError',
    'PipelineInitError',
    'ExtensionInitError',
    
    # 数据处理
    'DataException',
    'ItemInitError',
    'ItemAttributeError',
    'ItemValidationError',
    'ItemDiscard',
    
    # 请求/响应
    'RequestException',
    'RequestMethodError',
    'IgnoreRequestError',
    'DecodeError',
    
    # 输出
    'OutputException',
    'OutputError',
    'InvalidOutputError',
    
    # 配置
    'ConfigException',
    'NotConfigured',
    'NotConfiguredError',
    
    # 类型
    'TransformTypeError',
    'ReceiverTypeError',
]
```

**code file end: crawlo/exceptions.py**

---


### code file start: crawlo/framework.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawlo框架统一入口
================

提供简洁、一致的API接口，隐藏内部复杂性
"""

import os
import sys
from typing import Type, Optional, List, Union

from .crawler import Crawler, CrawlerProcess
from .initialization import initialize_framework
from .logging import get_logger
from .utils.config_manager import EnvConfigManager


class CrawloFramework:
    """
    Crawlo框架门面类
    
    提供统一的框架入口点，简化使用复杂度
    """

    def __init__(self, settings=None, **kwargs):
        """
        初始化框架
        
        Args:
            settings: 配置对象
            **kwargs: 额外配置参数
        """
        # 合并配置
        config = {}
        if settings:
            if hasattr(settings, '__dict__'):
                config.update(settings.__dict__)
            elif isinstance(settings, dict):
                config.update(settings)
        config.update(kwargs)
        
        # 如果没有提供配置，尝试自动加载项目配置
        if not config:
            config = self._load_project_config()

        # 初始化框架
        self._settings = initialize_framework(config)
        self._logger = get_logger('crawlo.framework')

        # 获取版本号
        version = EnvConfigManager.get_version()

        # 创建进程管理器
        self._process = CrawlerProcess(self._settings)

        self._logger.info(f"Crawlo Framework Started {version}")
        
        # 获取运行模式和队列类型并记录日志
        run_mode = self._settings.get('RUN_MODE', 'unknown')
        queue_type = self._settings.get('QUEUE_TYPE', 'unknown')
        self._logger.info(f"RunMode: {run_mode}, QueueType: {queue_type}")
        
        # 记录项目名称
        project_name = self._settings.get('PROJECT_NAME', 'unknown')
        self._logger.info(f"Project: {project_name}")

    def _load_project_config(self):
        """
        自动加载项目配置
        """
        try:
            # 查找项目根目录
            project_root = self._find_project_root()
            if not project_root:
                print("警告: 未找到项目根目录，使用默认配置")
                return {}
            
            # 添加项目根目录到Python路径
            if project_root not in sys.path:
                sys.path.insert(0, project_root)
            
            # 读取crawlo.cfg配置文件
            cfg_file = os.path.join(project_root, "crawlo.cfg")
            if not os.path.exists(cfg_file):
                print(f"警告: 未找到配置文件 {cfg_file}，使用默认配置")
                return {}
            
            import configparser
            config_parser = configparser.ConfigParser()
            config_parser.read(cfg_file, encoding="utf-8")
            
            if not config_parser.has_section("settings") or not config_parser.has_option("settings", "default"):
                print("警告: 配置文件缺少 [settings] 部分或 'default' 选项，使用默认配置")
                return {}
            
            # 获取settings模块路径
            settings_module_path = config_parser.get("settings", "default")
            project_package = settings_module_path.split(".")[0]
            
            # 导入项目配置模块
            import importlib
            settings_module = importlib.import_module(settings_module_path)
            
            # 创建配置字典
            project_config = {}
            for key in dir(settings_module):
                if key.isupper():
                    project_config[key] = getattr(settings_module, key)
            
            # print(f"已加载项目配置: {settings_module_path}")
            return project_config
            
        except Exception as e:
            print(f"加载项目配置时出错: {e}")
            return {}

    def _find_project_root(self):
        """
        查找项目根目录（包含crawlo.cfg的目录）
        """
        current_path = os.getcwd()
        
        # 向上查找直到找到crawlo.cfg
        checked_paths = set()
        path = current_path
        
        while path not in checked_paths:
            checked_paths.add(path)
            
            # 检查crawlo.cfg
            cfg_file = os.path.join(path, "crawlo.cfg")
            if os.path.exists(cfg_file):
                return path
            
            # 向上一级目录
            parent = os.path.dirname(path)
            if parent == path:
                break
            path = parent
        
        return None

    @property
    def settings(self):
        """获取配置"""
        return self._settings

    @property
    def logger(self):
        """获取框架日志器"""
        return self._logger

    async def run(self, spider_cls_or_name, settings=None):
        """
        运行单个爬虫
        
        Args:
            spider_cls_or_name: Spider类或名称
            settings: 额外配置
            
        Returns:
            Crawler实例
        """
        # 记录启动的爬虫名称
        if isinstance(spider_cls_or_name, str):
            spider_name = spider_cls_or_name
        else:
            spider_name = getattr(spider_cls_or_name, 'name', spider_cls_or_name.__name__)
        
        self._logger.info(f"Starting spider: {spider_name}")
        
        return await self._process.crawl(spider_cls_or_name, settings)

    async def run_multiple(self, spider_classes_or_names: List[Union[Type, str]],
                           settings=None):
        """
        运行多个爬虫
        
        Args:
            spider_classes_or_names: Spider类或名称列表
            settings: 额外配置
            
        Returns:
            结果列表
        """
        # 记录启动的爬虫名称
        spider_names = []
        for spider_cls_or_name in spider_classes_or_names:
            if isinstance(spider_cls_or_name, str):
                spider_names.append(spider_cls_or_name)
            else:
                spider_names.append(getattr(spider_cls_or_name, 'name', spider_cls_or_name.__name__))
        
        self._logger.info(f"Starting spiders: {', '.join(spider_names)}")
        
        try:
            return await self._process.crawl_multiple(spider_classes_or_names, settings)
        finally:
            # 清理全局Redis连接池
            await self._cleanup_global_resources()

    def create_crawler(self, spider_cls: Type, settings=None) -> Crawler:
        """
        创建Crawler实例
        
        Args:
            spider_cls: Spider类
            settings: 额外配置
            
        Returns:
            Crawler实例
        """
        merged_settings = self._merge_settings(settings)
        return Crawler(spider_cls, merged_settings)

    def _merge_settings(self, additional_settings):
        """合并配置"""
        if not additional_settings:
            return self._settings

        from .settings.setting_manager import SettingManager
        merged = SettingManager()

        # 复制基础配置
        if self._settings:
            merged.update_attributes(self._settings.__dict__)

        # 应用额外配置
        if isinstance(additional_settings, dict):
            merged.update_attributes(additional_settings)
        elif hasattr(additional_settings, '__dict__'):
            merged.update_attributes(additional_settings.__dict__)

        return merged

    def get_metrics(self) -> dict:
        """获取框架指标"""
        return self._process.get_metrics()
    
    async def _cleanup_global_resources(self):
        """清理全局资源（Redis连接池等）"""
        try:
            # 清理全局Redis连接池
            from crawlo.utils.redis_connection_pool import close_all_pools
            await close_all_pools()
            self._logger.debug("Global resources cleaned up")
        except Exception as e:
            self._logger.warning(f"Failed to cleanup global resources: {e}")


# 全局框架实例
_global_framework: Optional[CrawloFramework] = None


def get_framework(settings=None, **kwargs) -> CrawloFramework:
    """
    获取全局框架实例（单例模式）
    
    Args:
        settings: 配置对象
        **kwargs: 额外配置参数
        
    Returns:
        CrawloFramework实例
    """
    global _global_framework

    if _global_framework is None:
        _global_framework = CrawloFramework(settings, **kwargs)

    return _global_framework


def reset_framework():
    """重置全局框架实例（主要用于测试）"""
    global _global_framework
    _global_framework = None


# 便捷函数
async def run_spider(spider_cls_or_name, settings=None, **kwargs):
    """运行单个爬虫的便捷函数"""
    framework = get_framework(settings, **kwargs)
    return await framework.run(spider_cls_or_name)


async def run_spiders(spider_classes_or_names: List[Union[Type, str]],
                      settings=None, **kwargs):
    """运行多个爬虫的便捷函数"""
    framework = get_framework(settings, **kwargs)
    return await framework.run_multiple(spider_classes_or_names)


def create_crawler(spider_cls: Type, settings=None, **kwargs) -> Crawler:
    """创建Crawler的便捷函数"""
    framework = get_framework(settings, **kwargs)
    return framework.create_crawler(spider_cls)


# 配置相关便捷函数
def configure_framework(settings=None, **kwargs):
    """配置框架的便捷函数"""
    if settings or kwargs:
        reset_framework()  # 重置以应用新配置
    return get_framework(settings, **kwargs)
```

**code file end: crawlo/framework.py**

---


### code file start: crawlo/interfaces.py 

```python
from abc import ABC, abstractmethod
from typing import List, Type, Protocol

from crawlo.spider import Spider
from crawlo.network.request import Request


class ISpiderLoader(Protocol):
    """Spider loader interface"""
    
    @abstractmethod
    def load(self, spider_name: str) -> Type[Spider]:
        """Load a spider by name"""
        pass
    
    @abstractmethod
    def list(self) -> List[str]:
        """List all available spider names"""
        pass
    
    @abstractmethod
    def find_by_request(self, request: Request) -> List[str]:
        """Find spider names that can handle the given request"""
        pass
```

**code file end: crawlo/interfaces.py**

---


### code file start: crawlo/mode_manager.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
运行模式管理器
==============
管理 Crawlo 框架的不同运行模式，提供优雅的配置方式。

支持的运行模式：
1. standalone - 单机模式（默认）
2. distributed - 分布式模式
3. auto - 自动检测模式
"""
import os
from enum import Enum
from typing import Dict, Any, Optional


class RunMode(Enum):
    """运行模式枚举"""
    STANDALONE = "standalone"  # 单机模式
    DISTRIBUTED = "distributed"  # 分布式模式
    AUTO = "auto"  # 自动检测模式


class ModeManager:
    """运行模式管理器"""

    def __init__(self):
        # 延迟初始化logger，避免循环依赖
        self._logger = None
        self._debug("运行模式管理器初始化完成")

    def _get_logger(self):
        """延迟获取logger实例"""
        if self._logger is None:
            try:
                from crawlo.logging import get_logger
                self._logger = get_logger(__name__)
            except Exception:
                # 如果日志系统尚未初始化，返回None
                pass
        return self._logger

    def _debug(self, message: str):
        """调试日志"""
        logger = self._get_logger()
        if logger:
            logger.debug(message)

    @staticmethod
    def get_standalone_settings() -> Dict[str, Any]:
        """获取单机模式配置"""
        return {
            'RUN_MODE': 'standalone',
            'QUEUE_TYPE': 'memory',
            'FILTER_CLASS': 'crawlo.filters.memory_filter.MemoryFilter',
            'DEFAULT_DEDUP_PIPELINE': 'crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline',
            'PROJECT_NAME': 'crawlo',
            'CONCURRENCY': 8,
            'MAX_RUNNING_SPIDERS': 1,
            'DOWNLOAD_DELAY': 1.0,
        }

    @staticmethod
    def get_distributed_settings(
            redis_host: str = '127.0.0.1',
            redis_port: int = 6379,
            redis_password: Optional[str] = None,
            redis_db: int = 0,
            project_name: str = 'crawlo'
    ) -> Dict[str, Any]:
        """获取分布式模式配置"""
        # 构建 Redis URL
        if redis_password:
            redis_url = f'redis://:{redis_password}@{redis_host}:{redis_port}/{redis_db}'
        else:
            redis_url = f'redis://{redis_host}:{redis_port}/{redis_db}'

        return {
            'RUN_MODE': 'distributed',
            'QUEUE_TYPE': 'redis',
            'FILTER_CLASS': 'crawlo.filters.aioredis_filter.AioRedisFilter',
            'DEFAULT_DEDUP_PIPELINE': 'crawlo.pipelines.redis_dedup_pipeline.RedisDedupPipeline',
            'REDIS_HOST': redis_host,
            'REDIS_PORT': redis_port,
            'REDIS_PASSWORD': redis_password,
            'REDIS_DB': redis_db,
            'REDIS_URL': redis_url,
            'PROJECT_NAME': project_name,
            'SCHEDULER_QUEUE_NAME': f'crawlo:{project_name}:queue:requests',
            'CONCURRENCY': 16,
            'MAX_RUNNING_SPIDERS': 10,
            'DOWNLOAD_DELAY': 1.0,
        }

    @staticmethod
    def get_auto_settings() -> Dict[str, Any]:
        """获取自动检测模式配置"""
        # 默认使用内存队列和过滤器
        settings = ModeManager.get_standalone_settings()
        settings['RUN_MODE'] = 'auto'
        settings['QUEUE_TYPE'] = 'auto'
        return settings

    def resolve_mode_settings(
            self,
            mode: str = 'standalone',
            **kwargs
    ) -> Dict[str, Any]:
        """
        解析运行模式并返回对应配置

        Args:
            mode: 运行模式 ('standalone', 'distributed', 'auto')
            **kwargs: 额外配置参数

        Returns:
            Dict[str, Any]: 配置字典
        """
        self._debug(f"解析运行模式: {mode}")
        mode = RunMode(mode.lower())
        mode_info = None

        if mode == RunMode.STANDALONE:
            mode_info = "使用单机模式 - 简单快速，适合开发和中小规模爬取"
            # 对于单机模式，如果用户设置了QUEUE_TYPE为'auto'，应该保留用户的设置
            settings = self.get_standalone_settings()
            self._debug("应用单机模式配置")

        elif mode == RunMode.DISTRIBUTED:
            mode_info = "使用分布式模式 - 支持多节点扩展，适合大规模爬取"
            settings = self.get_distributed_settings(
                redis_host=kwargs.get('redis_host', '127.0.0.1'),
                redis_port=kwargs.get('redis_port', 6379),
                redis_password=kwargs.get('redis_password'),
                redis_db=kwargs.get('redis_db', 0),  # 添加 redis_db 参数
                project_name=kwargs.get('project_name', 'crawlo')
            )
            self._debug("应用分布式模式配置")

        elif mode == RunMode.AUTO:
            mode_info = "使用自动检测模式 - 智能选择最佳运行方式"
            settings = self.get_auto_settings()
            self._debug("应用自动检测模式配置")

        else:
            raise ValueError(f"不支持的运行模式: {mode}")

        # 合并用户自定义配置
        # 对于分布式模式，过滤掉特定参数
        if mode == RunMode.DISTRIBUTED:
            user_settings = {
                k.upper(): v for k,
                v in kwargs.items() if k not in [
                    'redis_host',
                    'redis_port',
                    'redis_password',
                    'project_name']}
            # 特别处理project_name
            if 'project_name' in kwargs:
                settings['PROJECT_NAME'] = kwargs['project_name']
        else:
            # 对于单机模式和自动模式，只过滤Redis相关参数
            user_settings = {
                k.upper(): v for k,
                v in kwargs.items() if k not in [
                    'redis_host',
                    'redis_port',
                    'redis_password']}
            # 特别处理project_name
            if 'project_name' in kwargs:
                settings['PROJECT_NAME'] = kwargs['project_name']
        settings.update(user_settings)
        self._debug(f"合并用户自定义配置: {list(user_settings.keys())}")

        # 将模式信息添加到配置中，供后续使用
        settings['_mode_info'] = mode_info

        self._debug(f"运行模式解析完成: {mode}")
        return settings

    def from_environment(self) -> Dict[str, Any]:
        """从环境变量构建配置"""
        config = {}

        # 扫描 CRAWLO_ 前缀的环境变量
        for key, value in os.environ.items():
            if key.startswith('CRAWLO_'):
                config_key = key[7:]  # 去掉 'CRAWLO_' 前缀
                # 简单的类型转换
                if value.lower() in ('true', 'false'):
                    config[config_key] = value.lower() == 'true'
                elif value.isdigit():
                    config[config_key] = int(value)
                else:
                    try:
                        config[config_key] = float(value)
                    except ValueError:
                        config[config_key] = value

        return config


# 便利函数
def standalone_mode(
        project_name: str = 'crawlo',
        **kwargs
) -> Dict[str, Any]:
    """快速创建单机模式配置"""
    return ModeManager().resolve_mode_settings(
        'standalone',
        project_name=project_name,
        **kwargs
    )


def distributed_mode(
        redis_host: str = '127.0.0.1',
        redis_port: int = 6379,
        redis_password: Optional[str] = None,
        redis_db: int = 0,  # 添加 redis_db 参数
        project_name: str = 'crawlo',
        **kwargs
) -> Dict[str, Any]:
    """快速创建分布式模式配置"""
    return ModeManager().resolve_mode_settings(
        'distributed',
        redis_host=redis_host,
        redis_port=redis_port,
        redis_password=redis_password,
        redis_db=redis_db,  # 传递 redis_db 参数
        project_name=project_name,
        **kwargs
    )


def auto_mode(
        project_name: str = 'crawlo',
        **kwargs
) -> Dict[str, Any]:
    """快速创建自动检测模式配置"""
    return ModeManager().resolve_mode_settings(
        'auto',
        project_name=project_name,
        **kwargs
    )


# 环境变量支持
def from_env(default_mode: str = 'standalone') -> Dict[str, Any]:
    """从环境变量创建配置
    
    支持的环境变量：
    - CRAWLO_MODE: 运行模式 (standalone/distributed/auto)
    - CRAWLO_REDIS_HOST: Redis主机地址
    - CRAWLO_REDIS_PORT: Redis端口
    - CRAWLO_REDIS_PASSWORD: Redis密码
    - CRAWLO_REDIS_DB: Redis数据库编号
    - CRAWLO_PROJECT_NAME: 项目名称
    - CRAWLO_CONCURRENCY: 并发数
    
    Args:
        default_mode: 默认运行模式（当未设置环境变量时使用）
    
    Returns:
        配置字典
    """
    mode = os.getenv('CRAWLO_MODE', default_mode).lower()
    
    kwargs = {}
    
    # 分布式模式特有配置
    if mode == 'distributed':
        kwargs['redis_host'] = os.getenv('CRAWLO_REDIS_HOST', '127.0.0.1')
        kwargs['redis_port'] = int(os.getenv('CRAWLO_REDIS_PORT', '6379'))
        if password := os.getenv('CRAWLO_REDIS_PASSWORD'):
            kwargs['redis_password'] = password
        kwargs['redis_db'] = int(os.getenv('CRAWLO_REDIS_DB', '0'))
    
    # 通用配置
    if project_name := os.getenv('CRAWLO_PROJECT_NAME'):
        kwargs['project_name'] = project_name
    
    if concurrency := os.getenv('CRAWLO_CONCURRENCY'):
        kwargs['CONCURRENCY'] = int(concurrency)
    
    return ModeManager().resolve_mode_settings(mode, **kwargs)

```

**code file end: crawlo/mode_manager.py**

---


### code file start: crawlo/project.py 

```python
import configparser
import os
import sys
from inspect import iscoroutinefunction
from typing import Callable, Optional, Any

from crawlo.settings.setting_manager import SettingManager
from crawlo.logging import get_logger

# 使用全局logger，避免每个模块都创建自己的延迟初始化函数
# 延迟获取logger，确保在日志系统配置之后获取
_logger = None


def logger():
    """延迟获取logger实例，确保在日志系统配置之后获取"""
    global _logger
    if _logger is None:
        _logger = get_logger(__name__)
    return _logger


# 添加一个临时的日志函数，用于在日志系统配置之前输出信息
def _temp_debug(message):
    """临时调试函数，在日志系统配置之前使用"""
    # 直接输出到控制台，避免循环依赖
    import os
    if os.environ.get('CRAWLO_DEBUG'):
        print(f"[CRAWLO_DEBUG] {message}")


def load_class(path: str) -> Any:
    """
    动态加载类
    
    Args:
        path: 类的完整路径，如 'package.module.ClassName'
        
    Returns:
        加载的类对象
    """
    # 使用工具模块的实现，避免循环依赖
    from crawlo.utils.misc import load_object as _load_class
    return _load_class(path)


def merge_settings(spider, settings):
    """
    合并爬虫的自定义设置到全局设置中
    
    Args:
        spider: 爬虫实例
        settings: 全局设置管理器
    """
    spider_name = getattr(spider, 'name', 'UnknownSpider')
    # 检查 settings 是否为 SettingManager 实例
    if not hasattr(settings, 'update_attributes'):
        _temp_debug(f"merge_settings 接收到的 settings 不是 SettingManager 实例: {type(settings)}")
        # 如果是字典，创建一个新的 SettingManager 实例
        if isinstance(settings, dict):
            from crawlo.settings.setting_manager import SettingManager
            new_settings = SettingManager()
            new_settings.update_attributes(settings)
            settings = new_settings
        else:
            _temp_debug("无法处理的 settings 类型")
            return

    if hasattr(spider, 'custom_settings'):
        custom_settings = getattr(spider, 'custom_settings')
        settings.update_attributes(custom_settings)
    else:
        _temp_debug(f"爬虫 '{spider_name}' 无 custom_settings，跳过合并")


async def common_call(func: Callable, *args, **kwargs):
    """
    通用调用函数，自动处理同步和异步函数
    
    Args:
        func: 要调用的函数
        *args: 位置参数
        **kwargs: 关键字参数
        
    Returns:
        函数调用结果
    """
    if iscoroutinefunction(func):
        return await func(*args, **kwargs)
    else:
        return func(*args, **kwargs)


def _get_settings_module_from_cfg(cfg_path: str) -> str:
    """从 crawlo.cfg 读取 settings 模块路径"""
    config = configparser.ConfigParser()
    try:
        config.read(cfg_path, encoding="utf-8")
        if config.has_section("settings") and config.has_option("settings", "default"):
            module_path = config.get("settings", "default")
            _temp_debug(f"📄 从 crawlo.cfg 加载 settings 模块: {module_path}")
            return module_path
        else:
            raise RuntimeError(f"配置文件缺少 [settings] 或 default 选项: {cfg_path}")
    except Exception as e:
        raise RuntimeError(f"解析 crawlo.cfg 失败: {e}")


def _find_project_root(start_path: str = ".") -> Optional[str]:
    """
    从指定路径向上查找项目根目录。
    识别依据：
        1. 存在 'crawlo.cfg'
        2. 存在 '__init__.py' 和 'settings.py'（即 Python 包）
    """
    path = os.path.abspath(start_path)

    # 首先检查当前目录及其子目录
    for root, dirs, files in os.walk(path):
        if "crawlo.cfg" in files:
            cfg_path = os.path.join(root, "crawlo.cfg")
            _temp_debug(f"✅ 找到项目配置文件: {cfg_path}")
            return root

    # 向上查找直到找到 crawlo.cfg 或包含 settings.py 和 __init__.py 的目录
    original_path = path
    checked_paths = set()

    while True:
        # 避免无限循环
        if path in checked_paths:
            break
        checked_paths.add(path)

        # 检查 crawlo.cfg
        cfg_file = os.path.join(path, "crawlo.cfg")
        if os.path.isfile(cfg_file):
            _temp_debug(f"✅ 找到项目配置文件: {cfg_file}")
            return path

        # 检查 settings.py 和 __init__.py
        settings_file = os.path.join(path, "settings.py")
        init_file = os.path.join(path, "__init__.py")
        if os.path.isfile(settings_file) and os.path.isfile(init_file):
            _temp_debug(f"✅ 找到项目模块: {path}")
            # 即使找到了项目模块，也继续向上查找是否有 crawlo.cfg
            parent = os.path.dirname(path)
            if parent != path:
                parent_cfg = os.path.join(parent, "crawlo.cfg")
                if os.path.isfile(parent_cfg):
                    _temp_debug(f"✅ 在上层目录找到项目配置文件: {parent_cfg}")
                    return parent
            return path

        parent = os.path.dirname(path)
        if parent == path:
            break
        path = parent

    # 如果向上查找也没找到，尝试从脚本所在目录查找
    # 获取当前脚本文件的路径
    try:
        script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        if script_path != original_path:
            path = script_path
            checked_paths = set()  # 重置已检查路径
            while True:
                # 避免无限循环
                if path in checked_paths:
                    break
                checked_paths.add(path)

                cfg_file = os.path.join(path, "crawlo.cfg")
                if os.path.isfile(cfg_file):
                    _temp_debug(f"✅ 找到项目配置文件: {cfg_file}")
                    return path

                settings_file = os.path.join(path, "settings.py")
                init_file = os.path.join(path, "__init__.py")
                if os.path.isfile(settings_file) and os.path.isfile(init_file):
                    _temp_debug(f"✅ 找到项目模块: {path}")
                    # 即使找到了项目模块，也继续向上查找是否有 crawlo.cfg
                    parent = os.path.dirname(path)
                    if parent != path:
                        parent_cfg = os.path.join(parent, "crawlo.cfg")
                        if os.path.isfile(parent_cfg):
                            _temp_debug(f"✅ 在上层目录找到项目配置文件: {parent_cfg}")
                            return parent
                    return path

                parent = os.path.dirname(path)
                if parent == path:
                    break
                path = parent
    except Exception:
        pass

    # 最后尝试从当前工作目录查找
    try:
        cwd = os.getcwd()
        if cwd != original_path and cwd != script_path:
            path = cwd
            checked_paths = set()  # 重置已检查路径
            while True:
                # 避免无限循环
                if path in checked_paths:
                    break
                checked_paths.add(path)

                cfg_file = os.path.join(path, "crawlo.cfg")
                if os.path.isfile(cfg_file):
                    _temp_debug(f"找到项目配置文件: {cfg_file}")
                    return path

                settings_file = os.path.join(path, "settings.py")
                init_file = os.path.join(path, "__init__.py")
                if os.path.isfile(settings_file) and os.path.isfile(init_file):
                    _temp_debug(f"找到项目模块: {path}")
                    # 即使找到了项目模块，也继续向上查找是否有 crawlo.cfg
                    parent = os.path.dirname(path)
                    if parent != path:
                        parent_cfg = os.path.join(parent, "crawlo.cfg")
                        if os.path.isfile(parent_cfg):
                            _temp_debug(f"在上层目录找到项目配置文件: {parent_cfg}")
                            return parent
                    return path

                parent = os.path.dirname(path)
                if parent == path:
                    break
                path = parent
    except Exception:
        pass

    _temp_debug("未找到 Crawlo 项目根目录。请确保在包含 'crawlo.cfg' 或 'settings.py' 的目录运行。")
    return None


def _load_project_settings(custom_settings: Optional[dict] = None) -> SettingManager:
    """
    内部函数：加载项目配置（不处理日志初始化）
    这个函数专门负责配置加载逻辑，避免与初始化管理器产生循环依赖

    Args:
        custom_settings: 运行时自定义配置，会覆盖 settings.py

    Returns:
        SettingManager: 已加载配置的实例
    """
    _temp_debug("🚀 正在加载 Crawlo 项目配置...")

    # 1. 查找项目根
    project_root = _find_project_root()
    if not project_root:
        raise RuntimeError("未找到 Crawlo 项目，请检查项目结构")

    # 2. 确定 settings 模块
    settings_module_path = None
    cfg_file = os.path.join(project_root, "crawlo.cfg")

    if os.path.isfile(cfg_file):
        settings_module_path = _get_settings_module_from_cfg(cfg_file)
    else:
        # 推断：项目目录名.settings
        project_name = os.path.basename(project_root)
        settings_module_path = f"{project_name}.settings"
        _temp_debug(f"⚠️ 未找到 crawlo.cfg，推断 settings 模块为: {settings_module_path}")

    # 3. 注入 sys.path
    project_root_str = os.path.abspath(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)
        _temp_debug(f"📁 项目根目录已加入 sys.path: {project_root_str}")

    # 4. 加载 SettingManager
    _temp_debug(f"⚙️ 正在加载配置模块: {settings_module_path}")
    settings = SettingManager()

    try:
        settings.set_settings(settings_module_path)
        _temp_debug("✅ settings 模块加载成功")
    except Exception as e:
        raise ImportError(f"加载 settings 模块失败 '{settings_module_path}': {e}")

    # 5. 根据 RUN_MODE 获取相应配置
    run_mode = settings.get('RUN_MODE', 'standalone')
    if run_mode:
        from crawlo.mode_manager import ModeManager
        mode_manager = ModeManager()
        # 获取项目名称并传递给模式配置
        project_name = settings.get('PROJECT_NAME', 'crawlo')
        mode_settings = mode_manager.resolve_mode_settings(run_mode, project_name=project_name)
        
        # 特殊处理：如果用户在settings.py中明确设置了QUEUE_TYPE，
        # 应该尊重用户的设置，除非是standalone模式下的redis设置
        user_queue_type = settings.get('QUEUE_TYPE')
        if user_queue_type and run_mode == 'standalone' and user_queue_type != 'memory':
            # 在单机模式下，如果用户明确设置了QUEUE_TYPE（且不是memory），应该保留用户的设置
            # 但需要确保配置的一致性
            mode_settings['QUEUE_TYPE'] = user_queue_type
            
            # 根据QUEUE_TYPE更新其他相关配置
            if user_queue_type == 'redis':
                mode_settings['FILTER_CLASS'] = 'crawlo.filters.aioredis_filter.AioRedisFilter'
                mode_settings['DEFAULT_DEDUP_PIPELINE'] = 'crawlo.pipelines.redis_dedup_pipeline.RedisDedupPipeline'
            elif user_queue_type == 'auto':
                mode_settings['FILTER_CLASS'] = settings.get('FILTER_CLASS', 'crawlo.filters.memory_filter.MemoryFilter')
                mode_settings['DEFAULT_DEDUP_PIPELINE'] = settings.get('DEFAULT_DEDUP_PIPELINE', 'crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline')
        
        # 合并模式配置
        for key, value in mode_settings.items():
            # 对于特定的配置项，模式配置应该优先于用户配置
            # 特别是与运行模式密切相关的配置项
            # 但如果用户明确设置了某些关键配置且与运行模式不冲突，则应保留用户设置
            priority_keys = ['QUEUE_TYPE', 'FILTER_CLASS', 'DEFAULT_DEDUP_PIPELINE']
            if key in priority_keys or key not in settings.attributes:
                settings.set(key, value)
        _temp_debug(f"🔧 已应用 {run_mode} 模式配置")

    # 6. 合并运行时配置
    if custom_settings:
        settings.update_attributes(custom_settings)
        _temp_debug(f"🔧 已应用运行时自定义配置: {list(custom_settings.keys())}")

    _temp_debug("🎉 Crawlo 项目配置加载完成！")
    return settings


def get_settings(custom_settings: Optional[dict] = None) -> SettingManager:
    """
    获取配置管理器实例（主入口函数）
    
    注意：这个函数现在作为向后兼容的入口，实际的初始化逻辑已经移到
    crawlo.initialization 模块中。建议使用新的初始化方式：
    
    >>> from crawlo.initialization import initialize_framework
    >>> settings = initialize_framework(custom_settings)

    Args:
        custom_settings: 运行时自定义配置，会覆盖 settings.py

    Returns:
        SettingManager: 已加载配置的实例
    """
    # 使用新的统一初始化管理器
    from crawlo.initialization import initialize_framework
    return initialize_framework(custom_settings)

```

**code file end: crawlo/project.py**

---


### code file start: crawlo/stats_collector.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
# @Time    :    2025-05-17 09:57
# @Author  :   crawl-coder
# @Desc    :   统计信息收集器
"""
from pprint import pformat
from crawlo.logging import get_logger


class StatsCollector(object):

    def __init__(self, crawler):
        self.crawler = crawler
        self._dump = self.crawler.settings.get_bool('STATS_DUMP')
        self._stats = {}
        self.logger = get_logger(self.__class__.__name__)

    def inc_value(self, key, count=1, start=0):
        self._stats[key] = self._stats.setdefault(key, start) + count

    def get_value(self, key, default=None):
        return self._stats.get(key, default)

    def get_stats(self):
        return self._stats

    def set_stats(self, stats):
        self._stats = stats

    def clear_stats(self):
        self._stats.clear()

    def close_spider(self, spider, reason):
        self._stats['reason'] = reason

        # 首选：使用 spider.name
        # 次选：使用实例的类名
        # 最后：使用一个完全未知的占位符
        spider_name = (
                getattr(spider, 'name', None) or
                spider.__class__.__name__ or
                '<Unknown>'
        )

        self._stats['spider_name'] = spider_name

    def __getitem__(self, item):
        return self._stats[item]

    def __setitem__(self, key, value):
        self._stats[key] = value

    def __delitem__(self, key):
        del self._stats[key]

    def close(self):
        """关闭统计收集器并输出统计信息"""
        if self._dump:
            # 获取爬虫名称
            spider_name = self._stats.get('spider_name', 'unknown')
            
            # 如果还没有设置爬虫名称，尝试从crawler中获取
            if spider_name == 'unknown' and hasattr(self, 'crawler') and self.crawler:
                spider = getattr(self.crawler, 'spider', None)
                if spider and hasattr(spider, 'name'):
                    spider_name = spider.name
                    # 同时更新_stats中的spider_name
                    self._stats['spider_name'] = spider_name
            
            # 对统计信息中的浮点数进行四舍五入处理
            formatted_stats = {}
            for key, value in self._stats.items():
                if isinstance(value, float):
                    # 对浮点数进行四舍五入，保留2位小数
                    formatted_stats[key] = round(value, 2)
                else:
                    formatted_stats[key] = value
            
            # 输出统计信息（这是唯一输出统计信息的地方）
            self.logger.info(f'{spider_name} stats: \n{pformat(formatted_stats)}')
```

**code file end: crawlo/stats_collector.py**

---


### code file start: crawlo/subscriber.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import asyncio
from collections import defaultdict
from inspect import iscoroutinefunction
from typing import Dict, Callable, Coroutine, Any, TypeAlias, List, Tuple


class ReceiverTypeError(TypeError):
    """当订阅的接收者不是一个协程函数时抛出。"""
    pass


ReceiverCoroutine: TypeAlias = Callable[..., Coroutine[Any, Any, Any]]


class Subscriber:
    """
    一个支持异步协程的发布/订阅（Pub/Sub）模式实现。

    这个类允许你注册（订阅）协程函数来监听特定事件，并在事件发生时
    以并发的方式异步地通知所有订阅者。
    """

    def __init__(self):
        """初始化一个空的订阅者字典。"""
        # 使用弱引用字典避免内存泄漏
        self._subscribers: Dict[str, Dict[ReceiverCoroutine, int]] = defaultdict(dict)
        # 用于缓存排序后的订阅者列表，提高频繁事件的处理性能
        self._sorted_subscribers_cache: Dict[str, List[Tuple[ReceiverCoroutine, int]]] = {}

    def subscribe(self, receiver: ReceiverCoroutine, *, event: str, priority: int = 0) -> None:
        """
        订阅一个事件。

        Args:
            receiver: 一个协程函数 (例如 async def my_func(...))。
            event: 要订阅的事件名称。
            priority: 订阅者优先级，数值越小优先级越高，默认为0。

        Raises:
            ReceiverTypeError: 如果提供的 `receiver` 不是一个协程函数。
        """
        if not iscoroutinefunction(receiver):
            raise ReceiverTypeError(f"接收者 '{receiver.__qualname__}' 必须是一个协程函数。")
        
        # 使用弱引用避免内存泄漏
        self._subscribers[event][receiver] = priority
        # 清除缓存
        self._sorted_subscribers_cache.pop(event, None)

    def unsubscribe(self, receiver: ReceiverCoroutine, *, event: str) -> None:
        """
        取消订阅一个事件。

        如果事件或接收者不存在，将静默处理。

        Args:
            receiver: 要取消订阅的协程函数。
            event: 事件名称。
        """
        if event in self._subscribers:
            self._subscribers[event].pop(receiver, None)
            # 清除缓存
            self._sorted_subscribers_cache.pop(event, None)

    def _get_sorted_subscribers(self, event: str) -> List[Tuple[ReceiverCoroutine, int]]:
        """
        获取按优先级排序的订阅者列表。
        
        Args:
            event: 事件名称。
            
        Returns:
            按优先级排序的订阅者列表。
        """
        # 检查缓存
        if event in self._sorted_subscribers_cache:
            return self._sorted_subscribers_cache[event]
        
        # 获取有效的订阅者（使用弱引用检查）
        valid_subscribers = {}
        for receiver, priority in list(self._subscribers[event].items()):
            # 检查弱引用是否仍然有效
            if isinstance(receiver, Callable):
                valid_subscribers[receiver] = priority
        
        # 更新订阅者字典
        self._subscribers[event] = valid_subscribers
        
        # 按优先级排序（数值小的优先级高）
        sorted_subscribers = sorted(valid_subscribers.items(), key=lambda x: x[1])
        # 缓存结果
        self._sorted_subscribers_cache[event] = sorted_subscribers
        
        return sorted_subscribers

    async def notify(self, event: str, *args, **kwargs) -> List[Any]:
        """
        异步地、并发地通知所有订阅了该事件的接收者。

        此方法会等待所有订阅者任务完成后再返回，并收集所有结果或异常。
        订阅者按优先级顺序执行，优先级高的先执行。

        Args:
            event: 要触发的事件名称。
            *args: 传递给接收者的位置参数。
            **kwargs: 传递给接收者的关键字参数。

        Returns:
            一个列表，包含每个订阅者任务的返回结果或在执行期间捕获的异常。
        """
        sorted_subscribers = self._get_sorted_subscribers(event)
        if not sorted_subscribers:
            return []

        # 为频繁触发的事件重用任务对象以提高性能
        tasks = []
        for receiver, _ in sorted_subscribers:
            try:
                # 创建任务并添加到列表
                task = asyncio.create_task(receiver(*args, **kwargs))
                tasks.append(task)
            except Exception as e:
                # 如果创建任务失败，记录异常并继续处理其他订阅者
                tasks.append(asyncio.Future())  # 添加一个已完成的Future表示错误
                tasks[-1].set_exception(e)

        # 并发执行所有任务并返回结果列表（包括异常）
        return await asyncio.gather(*tasks, return_exceptions=True)
```

**code file end: crawlo/subscriber.py**

---


### code file start: crawlo/task_manager.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time
import asyncio
from typing import Set, Final
from collections import deque
from asyncio import Task, Future, Semaphore
from crawlo.logging import get_logger


class DynamicSemaphore(Semaphore):
    """支持动态调整的信号量"""
    
    def __init__(self, initial_value: int = 8):
        super().__init__(initial_value)
        self._initial_value = initial_value
        self._current_value = initial_value
        self._response_times = deque(maxlen=10)  # 存储最近10次响应时间
        self._last_adjust_time = time.time()
        
    def record_response_time(self, response_time: float):
        """记录响应时间"""
        self._response_times.append(response_time)
        
    def adjust_concurrency(self):
        """根据响应时间动态调整并发数"""
        current_time = time.time()
        # 限制调整频率，至少间隔1秒（从2秒减少到1秒）
        if current_time - self._last_adjust_time < 1:
            return
            
        self._last_adjust_time = current_time
        
        if len(self._response_times) < 2:  # 从3减少到2
            return
            
        # 计算平均响应时间
        avg_response_time = sum(self._response_times) / len(self._response_times)
        
        # 根据响应时间调整并发数
        if avg_response_time < 0.2:  # 响应很快，增加并发（从0.3降到0.2）
            new_concurrency = min(self._current_value + 5, self._initial_value * 3)  # 增加幅度从3提高到5，最大值从2倍提高到3倍
        elif avg_response_time > 1.0:  # 响应较慢，减少并发（从1.5降到1.0）
            new_concurrency = max(self._current_value - 5, max(1, self._initial_value // 3))  # 减少幅度从3提高到5，最小值从一半降低到三分之一
        else:
            return  # 保持当前并发数
            
        # 只有当变化较大时才调整
        if abs(new_concurrency - self._current_value) > 1:
            self._adjust_semaphore_value(new_concurrency)
    
    def _adjust_semaphore_value(self, new_value: int):
        """调整信号量的值"""
        if new_value > self._current_value:
            # 增加信号量
            for _ in range(new_value - self._current_value):
                self.release()
        elif new_value < self._current_value:
            # 减少信号量，这里只是记录新的目标值
            # 实际减少会在acquire时处理
            pass
            
        self._current_value = new_value
        # 注意：Python的Semaphore没有直接修改内部计数器的方法
        # 所以我们只能通过release()来增加，减少则需要在acquire时控制


class TaskManager:

    def __init__(self, total_concurrency: int = 8):
        self.current_task: Final[Set] = set()
        # 使用动态信号量替代普通信号量
        self.semaphore: DynamicSemaphore = DynamicSemaphore(max(1, total_concurrency))
        self.logger = get_logger(self.__class__.__name__)
        
        # 异常统计
        self._exception_count = 0
        self._total_tasks = 0

    async def create_task(self, coroutine) -> Task:
        # 等待信号量，控制并发数
        await self.semaphore.acquire()
        
        task = asyncio.create_task(coroutine)
        self.current_task.add(task)
        self._total_tasks += 1

        def done_callback(_future: Future) -> None:
            try:
                self.current_task.discard(task)  # 使用discard而不是remove，避免KeyError
                
                # 获取任务结果或异常 - 这是关键，必须调用result()或exception()来"获取"异常
                try:
                    # 尝试获取结果，如果有异常会被抛出
                    result = _future.result()
                    # 如果成功完成，可以在这里记录成功统计
                except Exception as exception:
                    # 异常被正确"获取"了，不会再出现"never retrieved"警告
                    self._exception_count += 1
                    
                    # 记录异常详情
                    self.logger.error(
                        f"Task completed with exception: {type(exception).__name__}: {exception}"
                    )
                    self.logger.debug("Task exception details:", exc_info=exception)
                    
                    # 可以在这里添加更多的异常处理逻辑，如发送到监控系统
                    
            except Exception as e:
                # 防止回调函数本身出现异常
                self.logger.error(f"Error in task done callback: {e}")
            finally:
                # 确保信号量始终被释放
                self.semaphore.release()
                
                # 定期调整并发数（从每3个任务调整一次改为每2个任务调整一次）
                if self._total_tasks % 2 == 0:
                    self.semaphore.adjust_concurrency()

        task.add_done_callback(done_callback)

        return task

    def all_done(self) -> bool:
        return len(self.current_task) == 0
    
    def record_response_time(self, response_time: float):
        """记录任务的响应时间，用于动态调整并发数"""
        self.semaphore.record_response_time(response_time)
    
    def get_stats(self) -> dict:
        """获取任务管理器统计信息"""
        return {
            'active_tasks': len(self.current_task),
            'total_tasks': self._total_tasks,
            'exception_count': self._exception_count,
            'success_rate': (self._total_tasks - self._exception_count) / max(1, self._total_tasks) * 100,
            'current_concurrency': self.semaphore._current_value
        }
```

**code file end: crawlo/task_manager.py**

---


### code file start: crawlo/__init__.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawlo - 一个异步爬虫框架
"""

# 为了向后兼容，从tools中导入cleaners相关的功能
import crawlo.tools as cleaners
from crawlo import tools
from crawlo.crawler import Crawler, CrawlerProcess
from crawlo.downloader import DownloaderBase
from crawlo.items import Item, Field
from crawlo.middleware import BaseMiddleware
from crawlo.network.request import Request
from crawlo.network.response import Response
from crawlo.spider import Spider
from crawlo.utils import (
    TimeUtils,
    parse_time,
    format_time,
    time_diff,
    to_timestamp,
    to_datetime,
    now,
    to_timezone,
    to_utc,
    to_local,
    from_timestamp_with_tz
)


# 延迟导入的辅助函数
def get_framework_initializer():
    """延迟导入CoreInitializer以避免循环依赖"""
    from crawlo.initialization import CoreInitializer
    return CoreInitializer()


def initialize_framework(custom_settings=None):
    """延迟导入initialize_framework以避免循环依赖"""
    from crawlo.initialization import initialize_framework as _initialize_framework
    return _initialize_framework(custom_settings)


# 向后兼容的别名
def get_bootstrap_manager():
    """向后兼容的别名"""
    return get_framework_initializer()


# 版本号：优先从元数据读取
try:
    from importlib.metadata import version

    __version__ = version("crawlo")
except Exception:
    # 开发模式下可能未安装，回退到 __version__.py 或 dev
    try:
        from crawlo.__version__ import __version__
    except ImportError:
        __version__ = "dev"

# 定义对外 API
__all__ = [
    'Spider',
    'Item',
    'Field',
    'Request',
    'Response',
    'DownloaderBase',
    'BaseMiddleware',
    'TimeUtils',
    'parse_time',
    'format_time',
    'time_diff',
    'to_timestamp',
    'to_datetime',
    'now',
    'to_timezone',
    'to_utc',
    'to_local',
    'from_timestamp_with_tz',
    'cleaners',
    'tools',
    'Crawler',
    'CrawlerProcess',
    'get_framework_initializer',
    'get_bootstrap_manager',
    '__version__',
]

```

**code file end: crawlo/__init__.py**

---


### code file start: crawlo/__version__.py 

```python
__version__ = '1.4.7'

```

**code file end: crawlo/__version__.py**

---


### code file start: crawlo/commands/check.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-08-31 22:35
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo check，检查所有爬虫定义是否合规。
"""
import sys
import ast
import astor
import re
import time
from pathlib import Path
import configparser
from importlib import import_module

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from crawlo.crawler import CrawlerProcess
from crawlo.logging import get_logger


logger = get_logger(__name__)
console = Console()


def get_project_root():
    """
    从当前目录向上查找 crawlo.cfg，确定项目根目录
    """
    current = Path.cwd()
    for _ in range(10):
        cfg = current / "crawlo.cfg"
        if cfg.exists():
            return current
        if current == current.parent:
            break
        current = current.parent
    return None


def auto_fix_spider_file(spider_cls, file_path: Path):
    """自动修复 spider 文件中的常见问题"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()

        fixed = False
        tree = ast.parse(source)

        # 查找 Spider 类定义
        class_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == spider_cls.__name__:
                class_node = node
                break

        if not class_node:
            return False, "在文件中找不到类定义。"

        # 1. 修复 name 为空或缺失
        name_assign = None
        for node in class_node.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "name":
                        name_assign = node
                        break

        if not name_assign or (
            isinstance(name_assign.value, ast.Constant) and not name_assign.value.value
        ):
            # 生成默认 name：类名转 snake_case
            default_name = re.sub(r'(?<!^)(?=[A-Z])', '_', spider_cls.__name__).lower().replace("_spider", "")
            new_assign = ast.Assign(
                targets=[ast.Name(id="name", ctx=ast.Store())],
                value=ast.Constant(value=default_name)
            )
            if name_assign:
                index = class_node.body.index(name_assign)
                class_node.body[index] = new_assign
            else:
                class_node.body.insert(0, new_assign)
            fixed = True

        # 2. 修复 start_urls 是字符串
        start_urls_assign = None
        for node in class_node.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "start_urls":
                        start_urls_assign = node
                        break

        if start_urls_assign and isinstance(start_urls_assign.value, ast.Constant) and isinstance(start_urls_assign.value.value, str):
            new_value = ast.List(elts=[ast.Constant(value=start_urls_assign.value.value)], ctx=ast.Load())
            start_urls_assign.value = new_value
            fixed = True

        # 3. 修复缺少 parse 方法
        has_parse = any(
            isinstance(node, ast.FunctionDef) and node.name == "parse"
            for node in class_node.body
        )
        if not has_parse:
            parse_method = ast.FunctionDef(
                name="parse",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[ast.arg(arg="self"), ast.arg(arg="response")],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                    vararg=None,
                    kwarg=None
                ),
                body=[
                    ast.Expr(value=ast.Constant(value="默认 parse 方法，返回 item 或继续请求")),
                    ast.Pass()
                ],
                decorator_list=[],
                returns=None
            )
            class_node.body.append(parse_method)
            fixed = True

        # 4. 修复 allowed_domains 是字符串
        allowed_domains_assign = None
        for node in class_node.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "allowed_domains":
                        allowed_domains_assign = node
                        break

        if allowed_domains_assign and isinstance(allowed_domains_assign.value, ast.Constant) and isinstance(allowed_domains_assign.value.value, str):
            new_value = ast.List(elts=[ast.Constant(value=allowed_domains_assign.value.value)], ctx=ast.Load())
            allowed_domains_assign.value = new_value
            fixed = True

        # 5. 修复缺失 custom_settings
        has_custom_settings = any(
            isinstance(node, ast.Assign) and
            any(isinstance(t, ast.Name) and t.id == "custom_settings" for t in node.targets)
            for node in class_node.body
        )
        if not has_custom_settings:
            new_assign = ast.Assign(
                targets=[ast.Name(id="custom_settings", ctx=ast.Store())],
                value=ast.Dict(keys=[], values=[])
            )
            # 插入在 name 之后
            insert_index = 1
            for i, node in enumerate(class_node.body):
                if isinstance(node, ast.Assign) and any(
                    isinstance(t, ast.Name) and t.id == "name" for t in node.targets
                ):
                    insert_index = i + 1
                    break
            class_node.body.insert(insert_index, new_assign)
            fixed = True

        # 6. 修复缺失 start_requests 方法
        has_start_requests = any(
            isinstance(node, ast.FunctionDef) and node.name == "start_requests"
            for node in class_node.body
        )
        if not has_start_requests:
            start_requests_method = ast.FunctionDef(
                name="start_requests",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[ast.arg(arg="self")],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[],
                    vararg=None,
                    kwarg=None
                ),
                body=[
                    ast.Expr(value=ast.Constant(value="默认 start_requests，从 start_urls 生成请求")),
                    ast.For(
                        target=ast.Name(id="url", ctx=ast.Store()),
                        iter=ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr="start_urls", ctx=ast.Load()),
                        body=[
                            ast.Expr(
                                value=ast.Call(
                                    func=ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr="make_request", ctx=ast.Load()),
                                    args=[ast.Name(id="url", ctx=ast.Load())],
                                    keywords=[]
                                )
                            )
                        ],
                        orelse=[]
                    )
                ],
                decorator_list=[],
                returns=None
            )
            # 插入在 custom_settings 或 name 之后，parse 之前
            insert_index = 2
            for i, node in enumerate(class_node.body):
                if isinstance(node, ast.FunctionDef) and node.name == "parse":
                    insert_index = i
                    break
                elif isinstance(node, ast.Assign) and any(
                    isinstance(t, ast.Name) and t.id in ("name", "custom_settings") for t in node.targets
                ):
                    insert_index = i + 1
            class_node.body.insert(insert_index, start_requests_method)
            fixed = True

        if fixed:
            fixed_source = astor.to_source(tree)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(fixed_source)
            return True, "文件自动修复成功。"
        else:
            return False, "未找到可修复的问题。"

    except Exception as e:
        return False, f"自动修复失败: {e}"


class SpiderChangeHandler(FileSystemEventHandler):
    def __init__(self, project_root, spider_modules, show_fix=False, console=None):
        self.project_root = project_root
        self.spider_modules = spider_modules
        self.show_fix = show_fix
        self.console = console or Console()

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".py") and "spiders" in event.src_path:
            file_path = Path(event.src_path)
            spider_name = file_path.stem
            self.console.print(f"\n[bold blue]检测到变更[/bold blue] [cyan]{file_path}[/cyan]")
            self.check_and_fix_spider(spider_name)

    def check_and_fix_spider(self, spider_name):
        try:
            process = CrawlerProcess(spider_modules=self.spider_modules)
            if spider_name not in process.get_spider_names():
                self.console.print(f"[yellow]{spider_name} 不是已注册的爬虫。[/yellow]")
                return

            cls = process.get_spider_class(spider_name)
            issues = []

            # 简化检查
            if not getattr(cls, "name", None):
                issues.append("缺少或为空的 'name' 属性")
            if not callable(getattr(cls, "start_requests", None)):
                issues.append("缺少 'start_requests' 方法")
            if hasattr(cls, "start_urls") and isinstance(cls.start_urls, str):
                issues.append("'start_urls' 是字符串")
            if hasattr(cls, "allowed_domains") and isinstance(cls.allowed_domains, str):
                issues.append("'allowed_domains' 是字符串")

            try:
                spider = cls.create_instance(None)
                if not callable(getattr(spider, "parse", None)):
                    issues.append("缺少 'parse' 方法")
            except Exception:
                issues.append("实例化失败")

            if issues:
                self.console.print(f"[red]{spider_name} 存在问题:[/red]")
                for issue in issues:
                    self.console.print(f"  • {issue}")

                if self.show_fix:
                    file_path = Path(cls.__file__)
                    fixed, msg = auto_fix_spider_file(cls, file_path)
                    if fixed:
                        self.console.print(f"[green]自动修复: {msg}[/green]")
                    else:
                        self.console.print(f"[yellow]无法修复: {msg}[/yellow]")
            else:
                self.console.print(f"[green]{spider_name} 合规。[/green]")

        except Exception as e:
            self.console.print(f"[red]检查 {spider_name} 时出错: {e}[/red]")


def watch_spiders(project_root: Path, project_package: str, show_fix: bool):
    """监听 spiders 目录变化并自动检查"""
    spider_path = project_root / project_package / "spiders"
    if not spider_path.exists():
        console.print(f"[bold red]Spider 目录未找到:[/bold red] {spider_path}")
        return

    spider_modules = [f"{project_package}.spiders"]
    event_handler = SpiderChangeHandler(project_root, spider_modules, show_fix, console)
    observer = Observer()
    observer.schedule(event_handler, str(spider_path), recursive=False)

    console.print(Panel(
        f"[bold blue]监听[/bold blue] [cyan]{spider_path}[/cyan] 中的变更\n"
        "编辑任何爬虫文件以触发自动检查...",
        title="已启动监听模式",
        border_style="blue"
    ))

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[bold red]🛑 监听模式已停止。[/bold red]")
        observer.stop()
    observer.join()


def main(args):
    """
    主函数：检查所有爬虫定义的合规性
    用法:
        crawlo check
        crawlo check --fix
        crawlo check --ci
        crawlo check --json
        crawlo check --watch
    """
    show_fix = "--fix" in args or "-f" in args
    show_ci = "--ci" in args
    show_json = "--json" in args
    show_watch = "--watch" in args

    valid_args = {"--fix", "-f", "--ci", "--json", "--watch"}
    if any(arg not in valid_args for arg in args):
        console.print("[bold red]错误:[/bold red] 用法: [blue]crawlo check[/blue] [--fix] [--ci] [--json] [--watch]")
        return 1

    try:
        # 1. 查找项目根目录
        project_root = get_project_root()
        if not project_root:
            msg = "[bold red]找不到 'crawlo.cfg'[/bold red]\n请在项目目录中运行此命令。"
            if show_json:
                console.print_json(data={"success": False, "error": "未找到项目根目录"})
                return 1
            elif show_ci:
                console.print("未找到项目根目录。缺少 crawlo.cfg。")
                return 1
            else:
                console.print(Panel(
                    Text.from_markup(msg),
                    title="非Crawlo项目",
                    border_style="red",
                    padding=(1, 2)
                ))
                return 1

        project_root_str = str(project_root)
        if project_root_str not in sys.path:
            sys.path.insert(0, project_root_str)

        # 2. 读取 crawlo.cfg
        cfg_file = project_root / "crawlo.cfg"
        if not cfg_file.exists():
            msg = f"配置文件未找到: {cfg_file}"
            if show_json:
                console.print_json(data={"success": False, "error": msg})
                return 1
            elif show_ci:
                console.print(f"{msg}")
                return 1
            else:
                console.print(Panel(msg, title="缺少配置文件", border_style="red"))
                return 1

        config = configparser.ConfigParser()
        config.read(cfg_file, encoding="utf-8")

        if not config.has_section("settings") or not config.has_option("settings", "default"):
            msg = "crawlo.cfg 中缺少 [settings] 部分或 'default' 选项"
            if show_json:
                console.print_json(data={"success": False, "error": msg})
                return 1
            elif show_ci:
                console.print(f"{msg}")
                return 1
            else:
                console.print(Panel(msg, title="无效配置", border_style="red"))
                return 1

        settings_module = config.get("settings", "default")
        project_package = settings_module.split(".")[0]

        # 3. 确保项目包可导入
        try:
            import_module(project_package)
        except ImportError as e:
            msg = f"导入项目包 '{project_package}' 失败: {e}"
            if show_json:
                console.print_json(data={"success": False, "error": msg})
                return 1
            elif show_ci:
                console.print(f"{msg}")
                return 1
            else:
                console.print(Panel(msg, title="导入错误", border_style="red"))
                return 1

        # 4. 加载爬虫
        spider_modules = [f"{project_package}.spiders"]
        process = CrawlerProcess(spider_modules=spider_modules)
        spider_names = process.get_spider_names()

        if not spider_names:
            msg = "未找到爬虫。"
            if show_json:
                console.print_json(data={"success": True, "warning": msg})
                return 0
            elif show_ci:
                console.print("未找到爬虫。")
                return 0
            else:
                console.print(Panel(
                    Text.from_markup(
                        "[bold]未找到爬虫[/bold]\n\n"
                        "[bold]确保:[/bold]\n"
                        "  • 爬虫定义于 '[cyan]spiders[/cyan]' 模块\n"
                        "  • 具有 [green]`name`[/green] 属性\n"
                        "  • 模块已正确导入"
                    ),
                    title="未找到爬虫",
                    border_style="yellow",
                    padding=(1, 2)
                ))
                return 0

        # 5. 如果启用 watch 模式，启动监听
        if show_watch:
            console.print("[bold blue]启动监听模式...[/bold blue]")
            watch_spiders(project_root, project_package, show_fix)
            return 0  # watch 是长期运行，不返回

        # 6. 开始检查（非 watch 模式）
        if not show_ci and not show_json:
            console.print(f"[bold]正在检查 {len(spider_names)} 个爬虫...[/bold]\n")

        issues_found = False
        results = []

        for name in sorted(spider_names):
            cls = process.get_spider_class(name)
            issues = []

            # 检查 name 属性
            if not getattr(cls, "name", None):
                issues.append("缺少或为空的 'name' 属性")
            elif not isinstance(cls.name, str):
                issues.append("'name' 不是字符串")

            # 检查 start_requests 是否可调用
            if not callable(getattr(cls, "start_requests", None)):
                issues.append("缺少或不可调用的 'start_requests' 方法")

            # 检查 start_urls 类型（不应是字符串）
            if hasattr(cls, "start_urls") and isinstance(cls.start_urls, str):
                issues.append("'start_urls' 是字符串；应为列表或元组")

            # 检查 allowed_domains 类型
            if hasattr(cls, "allowed_domains") and isinstance(cls.allowed_domains, str):
                issues.append("'allowed_domains' 是字符串；应为列表或元组")

            # 实例化并检查 parse 方法
            try:
                spider = cls.create_instance(None)
                if not callable(getattr(spider, "parse", None)):
                    issues.append("未定义 'parse' 方法（推荐）")
            except Exception as e:
                issues.append(f"实例化爬虫失败: {e}")

            # 自动修复（如果启用）
            if issues and show_fix:
                try:
                    file_path = Path(cls.__file__)
                    fixed, msg = auto_fix_spider_file(cls, file_path)
                    if fixed:
                        if not show_ci and not show_json:
                            console.print(f"[green]已自动修复 {name} → {msg}[/green]")
                        issues = []  # 认为已修复
                    else:
                        if not show_ci and not show_json:
                            console.print(f"[yellow]无法自动修复 {name}: {msg}[/yellow]")
                except Exception as e:
                    if not show_ci and not show_json:
                        console.print(f"[yellow]找不到 {name} 的源文件: {e}[/yellow]")

            results.append({
                "name": name,
                "class": cls.__name__,
                "file": getattr(cls, "__file__", "unknown"),
                "issues": issues
            })

            if issues:
                issues_found = True

        # 7. 生成报告数据
        report = {
            "success": not issues_found,
            "total_spiders": len(spider_names),
            "issues": [
                {"name": r["name"], "class": r["class"], "file": r["file"], "problems": r["issues"]}
                for r in results if r["issues"]
            ]
        }

        # 8. 输出（根据模式）
        if show_json:
            console.print_json(data=report)
            return 1 if issues_found else 0

        if show_ci:
            if issues_found:
                console.print("合规性检查失败。")
                for r in results:
                    if r["issues"]:
                        console.print(f"  • {r['name']}: {', '.join(r['issues'])}")
            else:
                console.print("所有爬虫合规。")
            return 1 if issues_found else 0

        # 9. 默认 rich 输出
        table = Table(
            title="爬虫合规性检查结果",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
            title_style="bold green"
        )
        table.add_column("状态", style="bold", width=4)
        table.add_column("名称", style="cyan")
        table.add_column("类名", style="green")
        table.add_column("问题", style="yellow", overflow="fold")

        for res in results:
            if res["issues"]:
                status = "[red]X[/red]"
                issues_text = "\n".join(f"• {issue}" for issue in res["issues"])
            else:
                status = "[green]√[/green]"
                issues_text = "—"

            table.add_row(status, res["name"], res["class"], issues_text)

        console.print(table)
        console.print()

        if issues_found:
            console.print(Panel(
                "[bold red]一些爬虫存在问题。[/bold red]\n请在运行前修复这些问题。",
                title="合规性检查失败",
                border_style="red",
                padding=(1, 2)
            ))
            return 1
        else:
            console.print(Panel(
                "[bold green]所有爬虫都合规且定义良好！[/bold green]\n准备开始爬取！ ",
                title="检查通过",
                border_style="green",
                padding=(1, 2)
            ))
            return 0

    except Exception as e:
        logger.exception("执行 'crawlo check' 时发生异常")
        if show_json:
            console.print_json(data={"success": False, "error": str(e)})
        elif show_ci:
            console.print(f"意外错误: {e}")
        else:
            console.print(f"[bold red]检查过程中发生意外错误:[/bold red] {e}")
        return 1


if __name__ == "__main__":
    """
    支持直接运行：
        python -m crawlo.commands.check
    """
    sys.exit(main(sys.argv[1:]))
```

**code file end: crawlo/commands/check.py**

---


### code file start: crawlo/commands/genspider.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-08-31 22:36
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo genspider baidu，创建爬虫。
"""
import sys
import re
from pathlib import Path
import configparser
import importlib
from rich.console import Console

from .utils import (
    get_project_root,
    validate_project_environment,
    show_error_panel,
    show_success_panel,
    validate_spider_name,
    is_valid_domain
)

# 初始化 rich 控制台
console = Console()

TEMPLATES_DIR = Path(__file__).parent.parent / 'templates'


def _render_template(tmpl_path, context):
    """读取模板文件，替换 {{key}} 为 context 中的值"""
    with open(tmpl_path, 'r', encoding='utf-8') as f:
        content = f.read()
    for key, value in context.items():
        content = content.replace(f'{{{{{key}}}}}', str(value))
    return content


def generate_class_name(spider_name):
    """
    根据爬虫名称生成类名
    规则：蛇形命名 → 大驼峰命名 + 'Spider'
    示例：
        'news_spider' → 'NewsSpider'
        'ofweek_standalone' → 'OfweekStandaloneSpider'
        'baidu' → 'BaiduSpider'
    """
    # 如果名称已包含 'spider' 后缀，先去除
    name_clean = spider_name
    
    # 定义要移除的后缀列表
    spider_suffixes = ['_spider', 'spider']
    
    # 检查并移除后缀
    for suffix in spider_suffixes:
        if spider_name.endswith(suffix):
            name_clean = spider_name[:-len(suffix)]
            break

    # 按分隔符拆分单词
    words = re.split(r'[_-]', name_clean)

    # 将每个单词首字母大写
    capitalized_words = [word.capitalize() for word in words if word]

    # 组合成类名
    class_name = ''.join(capitalized_words) + 'Spider'

    return class_name


def main(args):
    if len(args) < 2:
        console.print("[bold red]错误:[/bold red] 用法: [blue]crawlo genspider[/blue] <爬虫名称> <域名>")
        console.print("示例:")
        console.print("   [blue]crawlo genspider[/blue] news_spider news.example.com")
        console.print("   [blue]crawlo genspider[/blue] product_spider shop.example.com")
        return 1

    spider_name = args[0]
    domain = args[1]

    # 验证爬虫名称
    if not validate_spider_name(spider_name):
        show_error_panel(
            "无效的爬虫名称",
            f"爬虫名称 '[cyan]{spider_name}[/cyan]' 无效。\n"
            "爬虫名称应:\n"
            "  • 以小写字母开头\n"
            "  • 只能包含小写字母、数字和下划线\n"
            "  • 是有效的Python标识符"
        )
        return 1

    # 验证域名格式
    if not is_valid_domain(domain):
        show_error_panel(
            "无效的域名",
            f"域名 '[cyan]{domain}[/cyan]' 格式无效。\n"
            "请提供有效的域名，如 'example.com'"
        )
        return 1

    # 验证项目环境
    is_valid, project_package, error_msg = validate_project_environment()
    if not is_valid:
        show_error_panel("非Crawlo项目", error_msg)
        return 1

    project_root = get_project_root()

    # 确定 items 模块的路径
    items_module_path = f"{project_package}.items"

    # 尝试导入 items 模块
    default_item_class = "ExampleItem"  # 默认回退
    try:
        items_module = importlib.import_module(items_module_path)
        # 获取模块中所有大写开头的类
        item_classes = [
            cls for cls in items_module.__dict__.values()
            if isinstance(cls, type) and cls.__name__[0].isupper()  # 首字母大写
        ]

        if item_classes:
            default_item_class = item_classes[0].__name__
        else:
            console.print(
                "[yellow]警告:[/yellow] 在 [cyan]items.py[/cyan] 中未找到项目类，使用 [green]ExampleItem[/green]。")

    except ImportError as e:
        console.print(f"[yellow]警告:[/yellow] 导入 [cyan]{items_module_path}[/cyan] 失败: {e}")
        # 仍使用默认 ExampleItem，不中断流程

    # 创建爬虫文件
    spiders_dir = project_root / project_package / 'spiders'
    spiders_dir.mkdir(parents=True, exist_ok=True)

    spider_file = spiders_dir / f'{spider_name}.py'
    if spider_file.exists():
        show_error_panel(
            "爬虫已存在",
            f"爬虫 '[cyan]{spider_name}[/cyan]' 已存在于\n[green]{spider_file}[/green]"
        )
        return 1

    # 模板路径
    tmpl_path = TEMPLATES_DIR / 'spider' / 'spider.py.tmpl'
    if not tmpl_path.exists():
        show_error_panel(
            "模板未找到",
            f"模板文件未找到于 [cyan]{tmpl_path}[/cyan]"
        )
        return 1

    # 生成类名（使用新的转换函数）
    class_name = generate_class_name(spider_name)

    context = {
        'spider_name': spider_name,
        'domain': domain,
        'project_name': project_package,
        'item_class': default_item_class,
        'class_name': class_name
    }

    try:
        content = _render_template(tmpl_path, context)
        with open(spider_file, 'w', encoding='utf-8') as f:
            f.write(content)

        console.print(f"[green]爬虫 '[bold]{spider_name}[/bold]' 创建成功！[/green]")
        console.print(f"  → 位置: [cyan]{spider_file}[/cyan]")
        console.print(f"  → 类名: [yellow]{class_name}[/yellow]")
        console.print(f"  → 域名: [blue]{domain}[/blue]")
        console.print("\n[bold]下一步操作:[/bold]")
        console.print(f"  [blue]crawlo run[/blue] {spider_name}")
        console.print(f"  [blue]crawlo check[/blue] {spider_name}")

        return 0

    except Exception as e:
        show_error_panel(
            "创建失败",
            f"创建爬虫失败: {e}"
        )
        return 1
```

**code file end: crawlo/commands/genspider.py**

---


### code file start: crawlo/commands/help.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-09-12
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo -h|--help，显示帮助信息。
"""
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from crawlo.utils.config_manager import EnvConfigManager

# 获取框架版本号
VERSION = EnvConfigManager.get_version()

console = Console()


def main(args):
    """
    主函数：显示帮助信息
    用法:
        crawlo -h|--help
    """
    # 检查是否有无效参数
    if args and args[0] not in ['-h', '--help', 'help']:
        console.print("[bold red]无效参数:[/bold red] [yellow]{}[/yellow]".format(args[0]))
        console.print("[bold blue]提示:[/bold blue] 使用 [green]crawlo -h[/green] 或 [green]crawlo --help[/green] 查看帮助信息")
        return 1

    # 显示帮助信息
    show_help()
    return 0


def show_help():
    """显示完整的帮助信息"""
    # 显示框架标题和版本
    console.print(Panel(
        Text.from_markup(f"[bold blue]Crawlo[/bold blue] [bold white]v{VERSION}[/bold white] - 异步爬虫框架"),
        expand=False,
        border_style="blue"
    ))
    
    # 显示基本用法
    console.print("[bold green]基本用法:[/bold green]")
    console.print("  [blue]crawlo[/blue] [cyan]<command>[/cyan] [options]")
    console.print()
    
    # 显示可用命令
    console.print("[bold green]可用命令:[/bold green]")
    table = Table(box=box.SIMPLE, show_header=True, header_style="bold magenta")
    table.add_column("命令", style="cyan", width=15)
    table.add_column("描述", style="white")
    table.add_column("用法", style="yellow")
    
    table.add_row("startproject", "创建新项目", "crawlo startproject <project_name>")
    table.add_row("genspider", "生成爬虫模板", "crawlo genspider <spider_name> [domain]")
    table.add_row("run", "运行爬虫", "crawlo run <spider_name>|all [options]")
    table.add_row("check", "检查爬虫代码", "crawlo check [options]")
    table.add_row("list", "列出所有爬虫", "crawlo list")
    table.add_row("stats", "查看统计信息", "crawlo stats [spider_name]")
    table.add_row("help", "显示帮助信息", "crawlo -h|--help")
    
    console.print(table)
    console.print()
    
    # 显示全局选项
    console.print("[bold green]全局选项:[/bold green]")
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("选项", style="cyan", width=15)
    table.add_column("描述", style="white")
    
    table.add_row("-h, --help", "显示帮助信息")
    table.add_row("-v, --version", "显示版本信息")
    
    console.print(table)
    console.print()
    
    # 显示各命令的详细用法
    console.print("[bold green]命令详细用法:[/bold green]")
    
    # run 命令
    console.print("[bold cyan]run[/bold cyan] - 运行爬虫")
    console.print("  用法: crawlo run <spider_name>|all [--json] [--no-stats] [--log-level LEVEL] [--config CONFIG] [--concurrency NUM]")
    console.print("  示例:")
    console.print("    crawlo run myspider")
    console.print("    crawlo run all")
    console.print("    crawlo run all --json --no-stats")
    console.print("    crawlo run myspider --log-level DEBUG")
    console.print("    crawlo run myspider --concurrency 32")
    console.print()
    

    
    # check 命令
    console.print("[bold cyan]check[/bold cyan] - 检查爬虫代码")
    console.print("  用法: crawlo check [--fix] [--ci] [--json] [--watch]")
    console.print("  示例:")
    console.print("    crawlo check")
    console.print("    crawlo check --fix")
    console.print("    crawlo check --ci --json")
    console.print()
    
    # startproject 命令
    console.print("[bold cyan]startproject[/bold cyan] - 创建新项目")
    console.print("  用法: crawlo startproject <project_name>")
    console.print("  示例:")
    console.print("    crawlo startproject myproject")
    console.print()
    
    # genspider 命令
    console.print("[bold cyan]genspider[/bold cyan] - 生成爬虫模板")
    console.print("  用法: crawlo genspider <spider_name> [domain]")
    console.print("  示例:")
    console.print("    crawlo genspider myspider example.com")
    console.print()
    
    # list 命令
    console.print("[bold cyan]list[/bold cyan] - 列出所有爬虫")
    console.print("  用法: crawlo list")
    console.print("  示例:")
    console.print("    crawlo list")
    console.print()
    
    # stats 命令
    console.print("[bold cyan]stats[/bold cyan] - 查看统计信息")
    console.print("  用法: crawlo stats [spider_name]")
    console.print("  示例:")
    console.print("    crawlo stats")
    console.print("    crawlo stats myspider")
    console.print()
    
    # 显示更多信息
    # console.print("[bold green]更多信息:[/bold green]")
    # console.print("  文档: https://crawlo.readthedocs.io/")
    # console.print("  源码: https://github.com/crawl-coder/Crawlo")
    # console.print("  问题: https://github.com/crawl-coder/Crawlo/issues")
```

**code file end: crawlo/commands/help.py**

---


### code file start: crawlo/commands/list.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-08-31 22:33
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo list，用于列出所有已注册的爬虫
"""
import sys
from pathlib import Path
from importlib import import_module

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

from crawlo.crawler import CrawlerProcess
from crawlo.logging import get_logger
from .utils import validate_project_environment, show_error_panel

logger = get_logger(__name__)
console = Console()


def main(args):
    """
    主函数：列出所有可用爬虫
    用法: crawlo list [--json]
    """
    show_json = "--json" in args
    
    # 过滤掉参数后检查是否有额外参数
    filtered_args = [arg for arg in args if not arg.startswith('--')]
    if filtered_args:
        if show_json:
            console.print_json(data={"success": False, "error": "用法: crawlo list [--json]"})
        else:
            console.print("[bold red]错误:[/bold red] 用法: [blue]crawlo list[/blue] [--json]")
        return 1

    try:
        # 验证项目环境
        is_valid, project_package, error_msg = validate_project_environment()
        if not is_valid:
            if show_json:
                console.print_json(data={"success": False, "error": error_msg})
            else:
                show_error_panel("非Crawlo项目", error_msg)
            return 1

        # 初始化 CrawlerProcess 并加载爬虫模块
        spider_modules = [f"{project_package}.spiders"]
        process = CrawlerProcess(spider_modules=spider_modules)

        # 获取所有爬虫名称
        spider_names = process.get_spider_names()
        if not spider_names:
            if show_json:
                console.print_json(data={
                    "success": True, 
                    "spiders": [],
                    "message": "项目中未找到爬虫"
                })
            else:
                console.print(Panel(
                    Text.from_markup(
                        "[bold]未找到爬虫[/bold] 于 '[cyan]spiders/[/cyan]' 目录。\n\n"
                        "[bold]确保:[/bold]\n"
                        "  • 爬虫类继承自 [blue]`crawlo.spider.Spider`[/blue]\n"
                        "  • 每个爬虫都有 [green]`name`[/green] 属性\n"
                        "  • 爬虫已在 [cyan]`spiders/__init__.py`[/cyan] 中导入 (如果使用包)"
                    ),
                    title="未找到爬虫",
                    border_style="yellow",
                    padding=(1, 2)
                ))
            return 0

        # 准备爬虫信息
        spider_info = []
        for name in sorted(spider_names):
            spider_cls = process.get_spider_class(name)
            module_name = spider_cls.__module__.replace(f"{project_package}.", "")
            
            # 获取额外信息
            start_urls_count = len(getattr(spider_cls, 'start_urls', []))
            allowed_domains = getattr(spider_cls, 'allowed_domains', [])
            custom_settings = getattr(spider_cls, 'custom_settings', {})
            
            spider_info.append({
                "name": name,
                "class": spider_cls.__name__,
                "module": module_name,
                "start_urls_count": start_urls_count,
                "allowed_domains": allowed_domains,
                "has_custom_settings": bool(custom_settings)
            })

        # JSON 输出
        if show_json:
            console.print_json(data={
                "success": True,
                "count": len(spider_info),
                "spiders": spider_info
            })
            return 0

        # 表格输出
        table = Table(
            title=f"找到 {len(spider_names)} 个爬虫",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
            title_style="bold green"
        )
        table.add_column("名称", style="cyan", no_wrap=True)
        table.add_column("类名", style="green")
        table.add_column("模块", style="dim")
        table.add_column("URL数", style="blue", justify="center")
        table.add_column("域名", style="yellow")
        table.add_column("自定义设置", style="magenta", justify="center")

        for info in spider_info:
            domains_display = ", ".join(info["allowed_domains"][:2])  # 显示前2个域名
            if len(info["allowed_domains"]) > 2:
                domains_display += f" (+{len(info['allowed_domains'])-2})"
            elif not domains_display:
                domains_display = "-"
                
            table.add_row(
                info["name"],
                info["class"],
                info["module"],
                str(info["start_urls_count"]),
                domains_display,
                "✓" if info["has_custom_settings"] else "-"
            )

        console.print(table)
        
        # 显示使用提示
        console.print("\n[bold]下一步操作:[/bold]")
        console.print("  [blue]crawlo run[/blue] <爬虫名称>    # 运行指定爬虫")
        console.print("  [blue]crawlo run[/blue] all             # 运行所有爬虫")
        console.print("  [blue]crawlo check[/blue] <爬虫名称>  # 检查爬虫有效性")
        
        return 0

    except Exception as e:
        if show_json:
            console.print_json(data={"success": False, "error": str(e)})
        else:
            console.print(f"[bold red]意外错误:[/bold red] {e}")
        logger.exception("执行 'crawlo list' 时发生异常")
        return 1
```

**code file end: crawlo/commands/list.py**

---


### code file start: crawlo/commands/run.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-08-31 22:36
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo run <spider_name>|all，用于运行指定爬虫。
"""
import os
import sys
import asyncio
import configparser
from importlib import import_module

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from crawlo.commands.stats import record_stats
from crawlo.crawler import CrawlerProcess
from crawlo.project import get_settings, _find_project_root
# 使用新的统一初始化系统
from crawlo.initialization import initialize_framework
from crawlo.core import get_framework_initializer
from crawlo.logging import get_logger

# 延迟获取logger，确保在日志系统配置之后获取
_logger = None


def logger():
    """延迟获取logger实例，确保在日志系统配置之后获取"""
    global _logger
    if _logger is None:
        # 使用改进后的日志系统，可以安全地在任何时候创建
        _logger = get_logger(__name__)
    return _logger


console = Console()


def check_redis_connection(settings):
    """检查Redis连接（分布式模式下）"""
    try:
        # 检查是否为分布式模式
        run_mode = settings.get('RUN_MODE', 'standalone')
        queue_type = settings.get('QUEUE_TYPE', 'memory')

        if run_mode == 'distributed' or queue_type == 'redis':
            import redis.asyncio as redis
            redis_url = settings.get('REDIS_URL', 'redis://127.0.0.1:6379/0')
            redis_host = settings.get('REDIS_HOST', '127.0.0.1')
            redis_port = settings.get('REDIS_PORT', 6379)

            console.print(f"检查 Redis 连接: {redis_host}:{redis_port}")

            # 创建Redis连接进行测试
            async def _test_redis():
                try:
                    r = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)
                    await r.ping()
                    await r.close()
                    return True
                except Exception as e:
                    console.print(f"Redis 连接失败: {e}")
                    return False

            # 运行异步测试
            if not asyncio.run(_test_redis()):
                raise ConnectionError(f"无法连接到 Redis 服务器 {redis_host}:{redis_port}")

            console.print("Redis 连接正常")
            return True
        else:
            # 非分布式模式，跳过Redis检查
            return True
    except ImportError:
        console.print("Redis 客户端未安装，跳过连接检查")
        return True
    except Exception as e:
        console.print(f"Redis 连接检查失败: {e}")
        return False


def main(args):
    """
    主函数：运行指定爬虫
    用法:
        crawlo run <spider_name>|all [--json] [--no-stats] [--log-level LEVEL] [--config CONFIG] [--concurrency NUM]
    """
    # 确保框架已初始化
    init_manager = get_framework_initializer()

    # 添加调试信息
    logger().debug("DEBUG: 进入main函数")

    if len(args) < 1:
        console.print(
            "[bold red]用法:[/bold red] [blue]crawlo run[/blue] <爬虫名称>|all [bold yellow][--json] [--no-stats] [--log-level LEVEL] [--config CONFIG] [--concurrency NUM][/bold yellow]")
        console.print("示例:")
        console.print("   [blue]crawlo run baidu[/blue]")
        console.print("   [blue]crawlo run all[/blue]")
        console.print("   [blue]crawlo run all --json --no-stats[/blue]")
        return 1

    # 解析参数
    spider_arg = args[0]
    show_json = "--json" in args
    no_stats = "--no-stats" in args
    
    # 解析日志级别参数
    log_level = None
    if "--log-level" in args:
        try:
            log_level_index = args.index("--log-level")
            if log_level_index + 1 < len(args):
                log_level = args[log_level_index + 1]
        except (ValueError, IndexError):
            pass
    
    # 解析配置文件参数
    config_file = None
    if "--config" in args:
        try:
            config_index = args.index("--config")
            if config_index + 1 < len(args):
                config_file = args[config_index + 1]
        except (ValueError, IndexError):
            pass
    
    # 解析并发数参数
    concurrency = None
    if "--concurrency" in args:
        try:
            concurrency_index = args.index("--concurrency")
            if concurrency_index + 1 < len(args):
                concurrency = int(args[concurrency_index + 1])
        except (ValueError, IndexError, TypeError):
            pass

    try:
        # 1. 查找项目根目录
        project_root = _find_project_root()
        if not project_root:
            msg = "[bold red]找不到 'crawlo.cfg'[/bold red]\n请在项目目录中运行此命令。"
            if show_json:
                console.print_json(data={"success": False, "error": "未找到项目根目录"})
                return 1
            else:
                console.print(Panel(
                    Text.from_markup(msg),
                    title="非Crawlo项目",
                    border_style="red",
                    padding=(1, 2)
                ))
                return 1

        project_root_str = str(project_root)
        if project_root_str not in sys.path:
            sys.path.insert(0, project_root_str)

        # 2. 读取 crawlo.cfg 获取 settings 模块
        cfg_file = os.path.join(project_root, "crawlo.cfg")
        if not os.path.exists(cfg_file):
            msg = f"在 {project_root} 中未找到 crawlo.cfg"
            if show_json:
                console.print_json(data={"success": False, "error": msg})
                return 1
            else:
                console.print(Panel(msg, title="缺少配置文件", border_style="red"))
                return 1

        config = configparser.ConfigParser()
        config.read(cfg_file, encoding="utf-8")

        if not config.has_section("settings") or not config.has_option("settings", "default"):
            msg = "crawlo.cfg 中缺少 [settings] 部分或 'default' 选项"
            if show_json:
                console.print_json(data={"success": False, "error": msg})
                return 1
            else:
                console.print(Panel(msg, title="无效配置", border_style="red"))
                return 1

        settings_module = config.get("settings", "default")
        project_package = settings_module.split(".")[0]

        # 3. 确保项目包可导入
        try:
            import_module(project_package)
        except ImportError as e:
            msg = f"导入项目包 '{project_package}' 失败: {e}"
            if show_json:
                console.print_json(data={"success": False, "error": msg})
                return 1
            else:
                console.print(Panel(msg, title="导入错误", border_style="red"))
                return 1

        # 4. 启动框架并加载 settings
        # 如果指定了日志级别，则添加到自定义设置中
        custom_settings = {}
        if log_level:
            custom_settings['LOG_LEVEL'] = log_level
        if concurrency:
            custom_settings['CONCURRENCY'] = concurrency
        
        settings = initialize_framework(custom_settings if custom_settings else None)

        # 检查Redis连接（如果是分布式模式）
        if not check_redis_connection(settings):
            if show_json:
                console.print_json(data={"success": False, "error": "Redis连接检查失败"})
                return 1
            else:
                return 1

        # 从配置中获取SPIDER_MODULES
        spider_modules = settings.get('SPIDER_MODULES', [f"{project_package}.spiders"])
        # 合并重复的调试信息
        process = CrawlerProcess(settings=settings, spider_modules=spider_modules)
        
        # 不再需要手动导入爬虫模块，框架内部会自动处理
        # 检查注册表中的爬虫
        from crawlo.spider import get_global_spider_registry
        registry = get_global_spider_registry()
        spider_names = list(registry.keys())
        # 减少重复的调试日志输出
        # logger().debug(f"SPIDER_MODULES from settings: {spider_modules}")
        # logger().debug(f"Registered spiders after import: {spider_names}")
        # logger().debug(f"SPIDER_MODULES: {spider_modules}")
        # logger().debug(f"Available spiders: {process.get_spider_names()}")

        # === 情况1：运行所有爬虫 ===
        if spider_arg.lower() == "all":
            spider_names = process.get_spider_names()
            if not spider_names:
                msg = "未找到爬虫。"
                if show_json:
                    console.print_json(data={"success": False, "error": msg})
                    return 1
                else:
                    console.print(Panel(
                        Text.from_markup(
                            "[bold red]未找到爬虫。[/bold red]\n\n"
                            "[bold]确保:[/bold]\n"
                            "  • 爬虫定义于 '[cyan]spiders/[/cyan]' 目录\n"
                            "  • 具有 [green]`name`[/green] 属性\n"
                            "  • 模块已导入 (例如通过 [cyan]__init__.py[/cyan])"
                        ),
                        title="未找到爬虫",
                        border_style="red",
                        padding=(1, 2)
                    ))
                    return 1

            # 显示即将运行的爬虫列表
            # 根据用户要求，不再显示详细的爬虫列表信息

            # 并行运行所有爬虫
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    transient=True,
            ) as progress:
                task = progress.add_task("正在运行所有爬虫...", total=None)
                asyncio.run(process.crawl_multiple(spider_names))

            if show_json:
                console.print_json(data={"success": True, "spiders": spider_names})
            else:
                console.print(Panel(
                    "[bold green]所有爬虫运行完成！[/bold green]",
                    title="全部完成",
                    border_style="green"
                ))
            return 0

        # === 情况2：运行单个爬虫 ===
        spider_name = spider_arg
        if not process.is_spider_registered(spider_name):
            available = process.get_spider_names()
            msg = f"爬虫 '[cyan]{spider_name}[/cyan]' 未找到。"
            if show_json:
                console.print_json(data={
                    "success": False,
                    "error": msg,
                    "available": available
                })
                return 1
            else:
                panel_content = Text.from_markup(msg + "\n")
                if available:
                    panel_content.append("\n可用爬虫:\n")
                    for name in sorted(available):
                        cls = process.get_spider_class(name)
                        class_name = cls.__name__ if cls else 'Unknown'
                        panel_content.append(f"  • [cyan]{name}[/cyan] ([green]{class_name}[/green])\n")
                else:
                    panel_content.append("\n未找到爬虫。请检查爬虫模块。")

                console.print(Panel(
                    panel_content,
                    title="爬虫未找到",
                    border_style="red",
                    padding=(1, 2)
                ))
                return 1

        spider_class = process.get_spider_class(spider_name)

        # 显示启动信息
        # 根据用户要求，不再显示项目启动信息
        # if not show_json:
        #     info_table = Table(
        #         title=f"启动爬虫: [bold cyan]{spider_name}[/bold cyan]",
        #         box=box.SIMPLE,
        #         show_header=False,
        #         title_style="bold green"
        #     )
        #     info_table.add_column("Key", style="yellow")
        #     info_table.add_column("Value", style="cyan")
        #     info_table.add_row("Project", project_package)
        #     info_table.add_row("Class", spider_class.__name__)
        #     info_table.add_row("Module", spider_class.__module__)
        #     console.print(info_table)
        #     console.print()

        # 注册 stats 记录
        # 注意：CrawlerProcess没有crawlers属性，我们需要在运行时注册
        # if not no_stats:
        #     for crawler in process.crawlers:
        #         crawler.signals.connect(record_stats, signal="spider_closed")

        # 运行爬虫
        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
        ) as progress:
            task = progress.add_task(f"正在运行 {spider_name}...", total=None)
            asyncio.run(process.crawl(spider_name))

        if show_json:
            console.print_json(data={"success": True, "spider": spider_name})
        else:
            console.print(Panel(
                f"[bold green]爬虫 '[cyan]{spider_name}[/cyan]' 运行完成！[/bold green]",
                title="完成",
                border_style="green"
            ))
        return 0

    except KeyboardInterrupt:
        msg = "爬虫被用户中断。"
        if show_json:
            console.print_json(data={"success": False, "error": msg})
        else:
            console.print(f"[bold yellow]{msg}[/bold yellow]")
        return 1
    except Exception as e:
        logger().exception("Exception during 'crawlo run'")
        msg = f"意外错误: {e}"
        if show_json:
            console.print_json(data={"success": False, "error": msg})
        else:
            console.print(f"[bold red]{msg}[/bold red]")
        return 1


if __name__ == "__main__":
    """
    支持直接运行：
        python -m crawlo.commands.run spider_name
    """
    sys.exit(main(sys.argv[1:]))

```

**code file end: crawlo/commands/run.py**

---


### code file start: crawlo/commands/startproject.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-08-31 22:36
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo startproject baidu，创建项目。
"""
import shutil
import re
import sys
import os
from pathlib import Path
from typing import Optional, List

# 添加项目根目录到路径，以便能够导入utils模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

try:
    from .utils import show_error_panel, show_success_panel
    UTILS_AVAILABLE = True
except ImportError:
    # 如果相对导入失败，尝试绝对导入
    try:
        from crawlo.commands.utils import show_error_panel, show_success_panel
        UTILS_AVAILABLE = True
    except ImportError:
        UTILS_AVAILABLE = False

# 初始化 rich 控制台（如果可用）
if RICH_AVAILABLE:
    console = Console()
else:
    # 简单的控制台输出替代
    class Console:
        def print(self, text):
            print(text)
    console = Console()

TEMPLATES_DIR = Path(__file__).parent.parent / 'templates'

# 可用的模板类型
TEMPLATE_TYPES = {
    'default': '默认模板 - 通用配置，适合大多数项目',
    'simple': '简化模板 - 最小配置，适合快速开始',
    'distributed': '分布式模板 - 针对分布式爬取优化',
    'high-performance': '高性能模板 - 针对大规模高并发优化',
    'gentle': '温和模板 - 低负载配置，对目标网站友好'
}

# 可选的模块组件
OPTIONAL_MODULES = {
    'mysql': 'MySQL数据库支持',
    'mongodb': 'MongoDB数据库支持',
    'redis': 'Redis支持（分布式队列和去重）',
    'proxy': '代理支持',
    'monitoring': '监控和性能分析',
    'dedup': '去重功能',
    'httpx': 'HttpX下载器',
    'aiohttp': 'AioHttp下载器',
    'curl': 'CurlCffi下载器'
}


def show_error_panel(title, content):
    """显示错误面板的简单实现"""
    if RICH_AVAILABLE:
        from rich.panel import Panel
        console.print(Panel(content, title=title, border_style="red"))
    else:
        print(f"{title}")
        print(content)

def show_success_panel(title, content):
    """显示成功面板的简单实现"""
    if RICH_AVAILABLE:
        from rich.panel import Panel
        console.print(Panel(content, title=title, border_style="green"))
    else:
        print(f"{title}")
        print(content)

def _render_template(tmpl_path, context):
    """读取模板文件，替换 {{key}} 为 context 中的值"""
    with open(tmpl_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 处理简单的过滤器语法 {{key|filter}}
    import re
    
    def apply_filter(value, filter_name):
        if filter_name == 'title':
            # 将 snake_case 转换为 TitleCase
            words = value.replace('_', ' ').split()
            return ''.join(word.capitalize() for word in words)
        return value
    
    # 查找并替换 {{key|filter}} 格式的占位符
    pattern = r'\{\{([^}|]+)\|([^}]+)\}\}'
    def replace_filter_match(match):
        key = match.group(1).strip()
        filter_name = match.group(2).strip()
        if key in context:
            return str(apply_filter(context[key], filter_name))
        return match.group(0)  # 如果找不到key，保持原样
    
    content = re.sub(pattern, replace_filter_match, content)
    
    # 处理普通的 {{key}} 占位符
    for key, value in context.items():
        content = content.replace(f'{{{{{key}}}}}', str(value))
    
    return content


def _copytree_with_templates(src, dst, context, template_type='default', modules: List[str] = None):
    """
    递归复制目录，将 .tmpl 文件渲染后复制（去除 .tmpl 后缀），其他文件直接复制。
    支持选择性模块复制。
    """
    src_path = Path(src)
    dst_path = Path(dst)
    dst_path.mkdir(parents=True, exist_ok=True)

    for item in src_path.rglob('*'):
        rel_path = item.relative_to(src_path)
        # 对于run.py.tmpl文件，需要特殊处理，将其放到项目根目录
        if item.name == 'run.py.tmpl':
            dst_item = dst_path.parent / rel_path  # 放到项目根目录
        else:
            dst_item = dst_path / rel_path

        # 检查是否应该包含此文件
        path_str = str(rel_path).replace('\\', '/')
        
        # 所有文件根据模块选择决定是否包含
        if not _should_include_file(rel_path, modules):
            continue

        if item.is_dir():
            dst_item.mkdir(parents=True, exist_ok=True)
        else:
            if item.suffix == '.tmpl':
                rendered_content = None
                # 处理特定模板类型的设置文件
                if item.name == 'settings.py.tmpl':
                    # 对于设置文件，根据模板类型选择相应的内容模板
                    if template_type != 'default':
                        # 使用特定模板类型的设置文件
                        template_file_name = f'settings_{template_type}.py.tmpl'
                        template_file_path = src_path / template_file_name
                        if template_file_path.exists():
                            rendered_content = _render_template(template_file_path, context)
                        else:
                            # 如果特定模板不存在，使用默认模板
                            rendered_content = _render_template(item, context)
                    else:
                        # 使用默认模板
                        rendered_content = _render_template(item, context)
                # 跳过其他以 settings_ 开头的模板文件，避免重复处理
                elif item.name.startswith('settings_') and item.name.endswith('.py.tmpl'):
                    continue
                else:
                    rendered_content = _render_template(item, context)
                
                # 确保设置文件始终命名为 settings.py
                if item.name == 'settings.py.tmpl':
                    # 特殊处理设置模板文件，统一生成为 settings.py
                    final_dst = dst_item.parent / 'settings.py'
                # 特殊处理run.py.tmpl文件
                elif item.name == 'run.py.tmpl':
                    final_dst = dst_item.with_suffix('')  # 去掉.tmpl后缀
                else:
                    final_dst = dst_item.with_suffix('')
                    
                final_dst.parent.mkdir(parents=True, exist_ok=True)
                with open(final_dst, 'w', encoding='utf-8') as f:
                    f.write(rendered_content)
            else:
                shutil.copy2(item, dst_item)


def _should_include_file(rel_path, modules: List[str]) -> bool:
    """
    根据选择的模块决定是否包含文件
    """
    if modules is None:
        # 如果没有指定模块，则包含所有文件
        return True
    
    # 基础文件始终包含
    basic_files = [
        '__init__.py.tmpl',
        'settings.py.tmpl',
        'spiders/__init__.py.tmpl',
        'items.py.tmpl',
        'middlewares.py.tmpl'
        # 移除了'run.py.tmpl'，因为它现在在模板根目录
    ]
    
    path_str = str(rel_path).replace('\\', '/')
    
    # 始终包含基础文件
    if path_str in basic_files:
        return True
    
    # 根据模块选择包含特定文件
    if 'mysql' in modules and 'mysql' in path_str:
        return True
    if 'mongodb' in modules and 'mongo' in path_str:
        return True
    if 'redis' in modules and 'redis' in path_str:
        return True
    if 'proxy' in modules and 'proxy' in path_str:
        return True
    if 'monitoring' in modules and ('monitor' in path_str or 'stats' in path_str):
        return True
    if 'dedup' in modules and 'dedup' in path_str:
        return True
    if 'httpx' in modules and 'httpx' in path_str:
        return True
    if 'aiohttp' in modules and 'aiohttp' in path_str:
        return True
    if 'curl' in modules and 'cffi' in path_str:
        return True
    
    # 默认不包含特定模块文件
    return False


def validate_project_name(project_name: str) -> tuple[bool, str]:
    """
    验证项目名称是否有效
    
    Returns:
        tuple[bool, str]: (是否有效, 错误信息)
    """
    # 检查是否为空
    if not project_name or not project_name.strip():
        return False, "项目名称不能为空"
    
    project_name = project_name.strip()
    
    # 检查长度
    if len(project_name) > 50:
        return False, "项目名称太长（最多50个字符）"
    
    # 检查是否为Python关键字
    python_keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
        'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
        'while', 'with', 'yield'
    }
    if project_name in python_keywords:
        return False, f"'{project_name}' 是Python关键字，不能用作项目名称"
    
    # 检查是否为有效的Python标识符
    if not project_name.isidentifier():
        return False, "项目名称必须是有效的Python标识符"
    
    # 检查格式（建议使用snake_case）
    if not re.match(r'^[a-z][a-z0-9_]*$', project_name):
        return False, (
            "项目名称应以小写字母开头，只能包含小写字母、数字和下划线"
        )
    
    # 检查是否以数字结尾（不推荐）
    if project_name[-1].isdigit():
        return False, "项目名称不应以数字结尾"
    
    return True, ""


def show_template_options():
    """显示可用的模板选项"""
    if RICH_AVAILABLE:
        table = Table(title="可用模板类型", show_header=True, header_style="bold magenta")
        table.add_column("模板类型", style="cyan", no_wrap=True)
        table.add_column("描述", style="green")
        
        for template_type, description in TEMPLATE_TYPES.items():
            table.add_row(template_type, description)
        
        console.print(table)
    else:
        print("可用模板类型:")
        for template_type, description in TEMPLATE_TYPES.items():
            print(f"  {template_type}: {description}")


def show_module_options():
    """显示可用的模块选项"""
    if RICH_AVAILABLE:
        table = Table(title="可选模块组件", show_header=True, header_style="bold magenta")
        table.add_column("模块", style="cyan", no_wrap=True)
        table.add_column("描述", style="green")
        
        for module, description in OPTIONAL_MODULES.items():
            table.add_row(module, description)
        
        console.print(table)
    else:
        print("可选模块组件:")
        for module, description in OPTIONAL_MODULES.items():
            print(f"  {module}: {description}")


def main(args):
    if len(args) < 1:
        console.print("[bold red]错误:[/bold red] 用法: [blue]crawlo startproject[/blue] <项目名称> [模板类型] [--modules 模块1,模块2]")
        console.print("示例:")
        console.print("   [blue]crawlo startproject[/blue] my_spider_project")
        console.print("   [blue]crawlo startproject[/blue] news_crawler simple")
        console.print("   [blue]crawlo startproject[/blue] ecommerce_spider distributed --modules mysql,proxy")
        show_template_options()
        show_module_options()
        return 1

    # 解析参数
    project_name = args[0]
    template_type = 'default'
    modules = None
    
    # 解析可选参数
    if len(args) > 1:
        for i, arg in enumerate(args[1:], 1):
            if arg.startswith('--modules='):
                modules_str = arg.split('=', 1)[1]
                modules = [m.strip() for m in modules_str.split(',') if m.strip()]
            elif arg.startswith('--modules'):
                # 处理 --modules module1,module2 格式
                if i + 1 < len(args):
                    modules_str = args[i + 1]
                    modules = [m.strip() for m in modules_str.split(',') if m.strip()]
            elif not arg.startswith('--') and arg in TEMPLATE_TYPES:
                template_type = arg
    
    # 验证模板类型
    if template_type not in TEMPLATE_TYPES:
        show_error_panel(
            "无效的模板类型",
            f"不支持模板类型 '[cyan]{template_type}[/cyan]'。\n"
        )
        show_template_options()
        return 1
    
    # 验证项目名称
    is_valid, error_msg = validate_project_name(project_name)
    if not is_valid:
        show_error_panel(
            "无效的项目名称", 
            f"[cyan]{project_name}[/cyan] 不是有效的项目名称。\n"
            f"{error_msg}\n\n"
            "项目名称应:\n"
            "  • 以小写字母开头\n"
            "  • 只能包含小写字母、数字和下划线\n"
            "  • 是有效的Python标识符\n"
            "  • 不能是Python关键字"
        )
        return 1
    
    project_dir = Path(project_name)

    if project_dir.exists():
        show_error_panel(
            "目录已存在",
            f"目录 '[cyan]{project_dir}[/cyan]' 已存在。\n"
            "请选择不同的项目名称或删除现有目录。"
        )
        return 1

    context = {'project_name': project_name}
    template_dir = TEMPLATES_DIR / 'project'

    try:
        # 1. 创建项目根目录
        project_dir.mkdir()

        # 2. 渲染 crawlo.cfg.tmpl
        cfg_template = TEMPLATES_DIR / 'crawlo.cfg.tmpl'
        if cfg_template.exists():
            cfg_content = _render_template(cfg_template, context)
            (project_dir / 'crawlo.cfg').write_text(cfg_content, encoding='utf-8')
            console.print(f"已创建 [green]{project_dir / 'crawlo.cfg'}[/green]")
        else:
            console.print("[yellow]警告:[/yellow] 找不到模板 'crawlo.cfg.tmpl'。")

        # 3. 渲染 run.py.tmpl (放在项目根目录)
        run_template = TEMPLATES_DIR / 'run.py.tmpl'
        if run_template.exists():
            run_content = _render_template(run_template, context)
            (project_dir / 'run.py').write_text(run_content, encoding='utf-8')
            console.print(f"已创建 [green]{project_dir / 'run.py'}[/green]")
        else:
            console.print("[yellow]警告:[/yellow] 找不到模板 'run.py.tmpl'。")

        # 4. 复制并渲染项目包内容
        package_dir = project_dir / project_name
        _copytree_with_templates(template_dir, package_dir, context, template_type, modules)
        console.print(f"已创建项目包: [green]{package_dir}[/green]")

        # 5. 创建 logs 目录
        (project_dir / 'logs').mkdir(exist_ok=True)
        console.print("已创建 logs 目录")
        
        # 6. 创建 output 目录（用于数据输出）
        (project_dir / 'output').mkdir(exist_ok=True)
        console.print("已创建 output 目录")

        # 成功面板
        success_text = Text.from_markup(f"项目 '[bold cyan]{project_name}[/bold cyan]' 创建成功！")
        console.print(Panel(success_text, title="成功", border_style="green", padding=(1, 2)))
        
        # 显示使用的模板类型
        if template_type != 'default':
            console.print(f"使用模板类型: [bold blue]{template_type}[/bold blue] - {TEMPLATE_TYPES[template_type]}")
        
        # 显示选择的模块
        if modules:
            console.print(f"选择的模块: [bold blue]{', '.join(modules)}[/bold blue]")

        # 下一步操作提示（对齐美观 + 语法高亮）
        next_steps = f"""
        [bold]下一步操作:[/bold]
        [blue]cd[/blue] {project_name}
        [blue]crawlo genspider[/blue] example example.com
        [blue]crawlo run[/blue] example
        
        [bold]了解更多:[/bold]
        [blue]crawlo list[/blue]                    # 列出所有爬虫
        [blue]crawlo check[/blue] example          # 检查爬虫有效性
        [blue]crawlo stats[/blue]                  # 查看统计信息
        """.strip()
        console.print(next_steps)

        return 0

    except Exception as e:
        show_error_panel(
            "创建失败",
            f"创建项目失败: {e}"
        )
        if project_dir.exists():
            shutil.rmtree(project_dir, ignore_errors=True)
            console.print("[red]已清理部分创建的项目。[/red]")
        return 1

if __name__ == "__main__":
    import sys
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
```

**code file end: crawlo/commands/startproject.py**

---


### code file start: crawlo/commands/stats.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-08-31 22:36
# @Author  : crawl-coder
# @Desc    : 命令行入口：crawlo stats，查看最近运行的爬虫统计信息。
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

from crawlo.logging import get_logger


logger = get_logger(__name__)
console = Console()

# 默认存储目录（相对于项目根目录）
STATS_DIR = "logs/stats"


def get_stats_dir() -> Path:
    """
    获取统计文件存储目录，优先使用项目根下的 logs/stats/
    如果不在项目中，回退到当前目录
    """
    current = Path.cwd()
    for _ in range(10):
        if (current / "crawlo.cfg").exists():
            return current / STATS_DIR
        if current == current.parent:
            break
        current = current.parent
    return Path.cwd() / STATS_DIR


def record_stats(crawler):
    """
    【供爬虫运行时调用】记录爬虫结束后的统计信息到 JSON 文件
    需在 Crawler 的 closed 回调中调用
    """
    spider_name = getattr(crawler.spider, "name", "unknown")
    stats = crawler.stats.get_stats() if crawler.stats else {}

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    stats_dir = Path(get_stats_dir())
    stats_dir.mkdir(parents=True, exist_ok=True)

    filename = stats_dir / f"{spider_name}_{timestamp}.json"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({
                "spider": spider_name,
                "timestamp": datetime.now().isoformat(),
                "stats": stats
            }, f, ensure_ascii=False, indent=2, default=str)
        logger.info(f"Stats for spider '{spider_name}' saved to {filename}")
    except Exception as e:
        logger.error(f"保存 '{spider_name}' 的统计信息失败: {e}")


def load_all_stats() -> Dict[str, list]:
    """
    加载所有已保存的统计文件，按 spider name 分组
    返回: {spider_name: [stats_record, ...]}
    """
    stats_dir = get_stats_dir()
    if not stats_dir.exists():
        return {}

    result = {}
    json_files = sorted(stats_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True)

    for file in json_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
            spider_name = data.get("spider", "unknown")
            result.setdefault(spider_name, []).append(data)
        except Exception as e:
            logger.warning(f"加载统计文件 {file} 失败: {e}")
    return result


def format_value(v: Any) -> str:
    """格式化值，防止太长或不可打印"""
    if isinstance(v, float):
        return f"{v:.4f}"
    s = str(v)
    if len(s) > 80:
        return s[:77] + "..."
    return s


def display_stats_table(stats_data: dict, title: str = "统计信息"):
    """通用函数：用 rich.table 展示统计数据"""
    table = Table(title=title, box=box.ROUNDED, show_header=True, header_style="bold magenta")
    table.add_column("键", style="cyan", no_wrap=True)
    table.add_column("值", style="green")

    for k in sorted(stats_data.keys()):
        table.add_row(k, format_value(stats_data[k]))

    console.print(table)


def main(args):
    """
    主函数：查看统计信息
    用法:
        crawlo stats                 → 显示所有爬虫最近一次运行
        crawlo stats myspider        → 显示指定爬虫所有历史记录
        crawlo stats myspider --all  → 显示所有历史（同上）
    """
    if len(args) > 2:
        console.print("[bold red]错误:[/bold red] 用法: [blue]crawlo stats[/blue] [爬虫名称] [--all]")
        return 1

    spider_name = None
    show_all = False

    if args:
        spider_name = args[0]
        show_all = "--all" in args or "-a" in args

    all_stats = load_all_stats()

    if not all_stats:
        console.print(Panel(
            Text.from_markup(
                "[bold]未找到统计信息。[/bold]\n"
                "先运行一个爬虫以生成统计信息。\n"
                f"统计目录: [cyan]{get_stats_dir()}[/cyan]"
            ),
            title="统计信息",
            border_style="yellow",
            padding=(1, 2)
        ))
        return 0

    # 显示所有爬虫最近一次运行
    if not spider_name:
        console.print(Panel(
            "[bold]最近的爬虫统计信息（上次运行）[/bold]",
            title="爬虫统计概览",
            border_style="green",
            padding=(0, 1)
        ))

        for name, runs in all_stats.items():
            latest = runs[0]
            ts = latest['timestamp'][:19]
            console.print(f" [bold cyan]{name}[/bold cyan] ([green]{ts}[/green])")
            display_stats_table(latest["stats"], title=f"{name} 的统计信息")
            console.print()  # 空行分隔

        return 0

    # 显示指定爬虫的历史
    if spider_name not in all_stats:
        console.print(f"[bold red]未找到爬虫 '[cyan]{spider_name}[/cyan]' 的统计信息[/bold red]")
        available = ', '.join(all_stats.keys())
        if available:
            console.print(f"可用爬虫: [green]{available}[/green]")
        return 1

    runs = all_stats[spider_name]
    if show_all:
        console.print(f"[bold]'[cyan]{spider_name}[/cyan]' 的所有运行记录 ({len(runs)} 次):[/bold]")
    else:
        runs = runs[:1]
        console.print(f"[bold]'[cyan]{spider_name}[/cyan]' 的上次运行:[/bold]")

    for i, run in enumerate(runs, 1):
        ts = run['timestamp']
        subtitle = f"运行 #{i} · {ts}" if show_all else f"上次运行 · {ts}"
        display_stats_table(run["stats"], title=f"{spider_name} 的统计信息 — {subtitle}")
        if i < len(runs):
            console.print("─" * 60)

    return 0
```

**code file end: crawlo/commands/stats.py**

---


### code file start: crawlo/commands/utils.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
命令行工具公共模块
提供命令行工具的公共函数和工具
"""
import sys
import configparser
from pathlib import Path
from importlib import import_module
from typing import Optional, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def get_project_root() -> Optional[Path]:
    """
    自动检测项目根目录：从当前目录向上查找 crawlo.cfg
    
    Returns:
        Path: 项目根目录路径，如果未找到返回 None
    """
    current = Path.cwd()
    for _ in range(10):  # 最多向上查找10层
        cfg_file = current / "crawlo.cfg"
        if cfg_file.exists():
            return current
        if current == current.parent:
            break
        current = current.parent
    return None


def validate_project_environment() -> Tuple[bool, Optional[str], Optional[str]]:
    """
    验证项目环境，确保在正确的 Crawlo 项目中
    
    Returns:
        Tuple[bool, Optional[str], Optional[str]]: 
        (是否有效, 项目包名, 错误信息)
    """
    # 1. 查找项目根目录
    project_root = get_project_root()
    if not project_root:
        return False, None, "找不到 'crawlo.cfg'。请在项目目录中运行此命令。"
    
    # 2. 将项目根加入 Python 路径
    project_root_str = str(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)
    
    # 3. 读取配置文件
    cfg_file = project_root / "crawlo.cfg"
    config = configparser.ConfigParser()
    
    try:
        config.read(cfg_file, encoding="utf-8")
    except Exception as e:
        return False, None, f"读取 crawlo.cfg 失败: {e}"
    
    if not config.has_section("settings") or not config.has_option("settings", "default"):
        return False, None, "无效的 crawlo.cfg：缺少 [settings] 部分或 'default' 选项"
    
    # 4. 获取项目包名
    settings_module = config.get("settings", "default")
    project_package = settings_module.split(".")[0]
    
    # 5. 验证项目包是否可导入
    try:
        import_module(project_package)
    except ImportError as e:
        return False, None, f"导入项目包 '{project_package}' 失败: {e}"
    
    return True, project_package, None


def show_error_panel(title: str, message: str, show_json: bool = False) -> None:
    """
    显示错误面板或JSON格式错误
    
    Args:
        title: 错误标题
        message: 错误消息
        show_json: 是否以JSON格式输出
    """
    if show_json:
        console.print_json(data={"success": False, "error": message})
    else:
        console.print(Panel(
            Text.from_markup(f"[bold red]{message}[/bold red]"),
            title=f"{title}",
            border_style="red",
            padding=(1, 2)
        ))


def show_success_panel(title: str, message: str, show_json: bool = False, data: dict = None) -> None:
    """
    显示成功面板或JSON格式结果
    
    Args:
        title: 成功标题
        message: 成功消息
        show_json: 是否以JSON格式输出
        data: JSON数据（当show_json=True时）
    """
    if show_json:
        result = {"success": True, "message": message}
        if data:
            result.update(data)
        console.print_json(data=result)
    else:
        console.print(Panel(
            Text.from_markup(f"[bold green]{message}[/bold green]"),
            title=f"{title}",
            border_style="green",
            padding=(1, 2)
        ))


def validate_spider_name(spider_name: str) -> bool:
    """
    验证爬虫名称是否符合规范
    
    Args:
        spider_name: 爬虫名称
        
    Returns:
        bool: 是否有效
    """
    import re
    # 清理爬虫名称中的不可见字符
    cleaned_name = ''.join(c for c in spider_name if not unicodedata.category(c).startswith('C'))
    
    # 爬虫名称应该是有效的Python标识符
    return cleaned_name.isidentifier() and re.match(r'^[a-z][a-z0-9_]*$', cleaned_name)


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小
    
    Args:
        size_bytes: 字节数
        
    Returns:
        str: 格式化后的大小字符串
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def truncate_text(text: str, max_length: int = 80) -> str:
    """
    截断过长的文本
    
    Args:
        text: 原始文本
        max_length: 最大长度
        
    Returns:
        str: 截断后的文本
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def is_valid_domain(domain: str) -> bool:
    """
    验证域名格式是否正确
    
    Args:
        domain: 域名
        
    Returns:
        bool: 是否有效
    """
    import re
    # 清理域名中的不可见字符
    cleaned_domain = ''.join(c for c in domain if not unicodedata.category(c).startswith('C'))
    
    pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
    )
    return bool(pattern.match(cleaned_domain))


# 添加导入
import unicodedata
```

**code file end: crawlo/commands/utils.py**

---


### code file start: crawlo/commands/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-

_commands = {
    'startproject': 'crawlo.commands.startproject',
    'genspider': 'crawlo.commands.genspider',
    'run': 'crawlo.commands.run',
    'check': 'crawlo.commands.check',
    'list': 'crawlo.commands.list',
    'stats': 'crawlo.commands.stats',
    'help': 'crawlo.commands.help'
}

def get_commands():
    return _commands
```

**code file end: crawlo/commands/__init__.py**

---


### code file start: crawlo/core/engine.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import asyncio
import time
from inspect import iscoroutine
from typing import Optional, Generator, Callable

from crawlo import Request, Item
from crawlo.core.processor import Processor
from crawlo.core.scheduler import Scheduler
from crawlo.downloader import DownloaderBase
from crawlo.event import CrawlerEvent
from crawlo.exceptions import OutputError
from crawlo.utils.misc import load_object
from crawlo.spider import Spider
from crawlo.task_manager import TaskManager
from crawlo.utils.func_tools import transform
from crawlo.logging import get_logger


class Engine(object):

    def __init__(self, crawler):
        self.running = False
        self.normal = True
        self.crawler = crawler
        self.settings = crawler.settings
        self.spider: Optional[Spider] = None
        self.downloader: Optional[DownloaderBase] = None
        self.scheduler: Optional[Scheduler] = None
        self.processor: Optional[Processor] = None
        self.start_requests: Optional[Generator] = None
        self.task_manager: Optional[TaskManager] = TaskManager(self.settings.get_int('CONCURRENCY'))

        # 增强控制参数
        self.max_queue_size = self.settings.get_int('SCHEDULER_MAX_QUEUE_SIZE', 200)
        self.generation_batch_size = self.settings.get_int('REQUEST_GENERATION_BATCH_SIZE', 10)
        self.generation_interval = self.settings.get_float('REQUEST_GENERATION_INTERVAL', 0.01)  # 优化默认值
        self.backpressure_ratio = self.settings.get_float('BACKPRESSURE_RATIO', 0.9)  # 优化默认值
        
        # 状态跟踪
        self._generation_paused = False
        self._last_generation_time = 0
        self._generation_stats = {
            'total_generated': 0,
            'backpressure_events': 0
        }

        self.logger = get_logger(name=self.__class__.__name__)

    def _get_downloader_cls(self):
        """获取下载器类，支持多种配置方法"""
        # 方式1: 使用 DOWNLOADER_TYPE 简化名称（推荐）
        downloader_type = self.settings.get('DOWNLOADER_TYPE')
        if downloader_type:
            try:
                from crawlo.downloader import get_downloader_class
                downloader_cls = get_downloader_class(downloader_type)
                self.logger.debug(f"使用下载器类型: {downloader_type} -> {downloader_cls.__name__}")
                return downloader_cls
            except (ImportError, ValueError) as e:
                self.logger.warning(f"无法使用下载器类型 '{downloader_type}': {e}，回退到默认配置")
        
        # 方式2: 使用 DOWNLOADER 完整类路径（兼容旧版本）
        downloader_cls = load_object(self.settings.get('DOWNLOADER'))
        if not issubclass(downloader_cls, DownloaderBase):
            raise TypeError(f'下载器 {downloader_cls.__name__} 不是 DownloaderBase 的子类。')
        return downloader_cls

    def engine_start(self):
        self.running = True
        # 获取版本号，如果获取失败则使用默认值
        version = self.settings.get('VERSION', '1.0.0')
        if not version or version == 'None':
            version = '1.0.0'
        # 将INFO级别日志改为DEBUG级别，避免与CrawlerProcess启动日志重复
        self.logger.debug(f"Crawlo框架已启动 {version}")

    async def start_spider(self, spider):
        self.spider = spider

        self.scheduler = Scheduler.create_instance(self.crawler)
        if hasattr(self.scheduler, 'open'):
            if asyncio.iscoroutinefunction(self.scheduler.open):
                await self.scheduler.open()
            else:
                self.scheduler.open()

        downloader_cls = self._get_downloader_cls()
        self.downloader = downloader_cls(self.crawler)
        if hasattr(self.downloader, 'open'):
            if asyncio.iscoroutinefunction(self.downloader.open):
                self.downloader.open()
            else:
                # DownloaderBase.open() 是同步方法，直接调用而不是await
                self.downloader.open()
        
        # 注册下载器到资源管理器
        if hasattr(self.crawler, '_resource_manager') and self.downloader:
            from crawlo.utils.resource_manager import ResourceType
            self.crawler._resource_manager.register(
                self.downloader,
                lambda d: d.close() if hasattr(d, 'close') else None,
                ResourceType.DOWNLOADER,
                name=f"downloader.{downloader_cls.__name__}"
            )
            self.logger.debug(f"Downloader registered to resource manager: {downloader_cls.__name__}")

        self.processor = Processor(self.crawler)
        if hasattr(self.processor, 'open'):
            if asyncio.iscoroutinefunction(self.processor.open):
                await self.processor.open()
            else:
                # Processor.open() 是同步方法
                self.processor.open()

        # 在处理器初始化之后初始化扩展管理器，确保日志输出顺序正确
        # 中间件 -> 管道 -> 扩展
        if not hasattr(self.crawler, 'extension') or not self.crawler.extension:
            self.crawler.extension = self.crawler._create_extension()

        # 启动引擎
        self.engine_start()
        
        self.logger.debug("开始创建start_requests迭代器")
        try:
            # 先收集所有请求到列表中，避免在检查时消耗迭代器
            requests_list = list(spider.start_requests())
            self.logger.debug(f"收集到 {len(requests_list)} 个请求")
            self.start_requests = iter(requests_list)
            self.logger.debug("start_requests迭代器创建成功")
        except Exception as e:
            self.logger.error(f"创建start_requests迭代器失败: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
        await self._open_spider()

    async def crawl(self):
        """
        支持智能请求生成和背压控制
        """
        generation_task = None
        
        try:
            # 启动请求生成任务（如果启用了受控生成）
            if (self.start_requests and 
                self.settings.get_bool('ENABLE_CONTROLLED_REQUEST_GENERATION', False)):
                self.logger.debug("创建受控请求生成任务")
                generation_task = asyncio.create_task(
                    self._controlled_request_generation()
                )
            else:
                # 传统方式处理启动请求
                self.logger.debug("创建传统请求生成任务")
                generation_task = asyncio.create_task(
                    self._traditional_request_generation()
                )
            
            self.logger.debug("请求生成任务创建完成")
            
            # 主爬取循环
            loop_count = 0
            last_exit_check = 0  # 记录上次检查退出条件的时间
            exit_check_interval = 1  # 每1次循环检查一次退出条件，进一步提高检查频率
            
            while self.running:
                loop_count += 1
                # 获取并处理请求
                if request := await self._get_next_request():
                    await self._crawl(request)
                
                # 优化退出条件检查频率
                if loop_count - last_exit_check >= exit_check_interval:
                    should_exit = await self._should_exit()
                    if should_exit:
                        self.logger.debug("满足退出条件，准备退出循环")
                        break
                    last_exit_check = loop_count
                
                # 短暂休息避免忙等，但减少休息时间以提高效率
                await asyncio.sleep(0.000001)  # 从0.00001减少到0.000001
            
            self.logger.debug(f"主爬取循环结束，总共执行了 {loop_count} 次")
        
        finally:
            # 确保请求生成任务完成
            if generation_task and not generation_task.done():
                try:
                    await generation_task
                except asyncio.CancelledError:
                    pass
            
            await self.close_spider()

    async def _traditional_request_generation(self):
        """传统请求生成方法（兼容旧版本）"""
        self.logger.debug("开始处理传统请求生成")
        processed_count = 0
        while self.running:
            try:
                start_request = next(self.start_requests)
                # 将过于频繁的debug日志合并，减少输出
                # self.logger.debug(f"获取到请求: {getattr(start_request, 'url', 'Unknown URL')}")
                # 请求入队
                await self.enqueue_request(start_request)
                processed_count += 1
                # 减少过于频繁的日志输出
                # self.logger.debug(f"已处理请求数量: {processed_count}")
            except StopIteration:
                self.logger.debug("所有起始请求处理完成")
                self.start_requests = None
                break
            except Exception as exp:
                self.logger.error(f"处理请求时发生异常: {exp}")
                import traceback
                self.logger.error(traceback.format_exc())
                # 1. All requests have been processed
                # 2. Is scheduler idle
                # 3. Is downloader idle
                if not await self._exit():
                    continue
                self.running = False
                if self.start_requests is not None:
                    self.logger.error(f"Error occurred while starting request: {str(exp)}")
            # 减少等待时间以提高效率
            await asyncio.sleep(0.00001)  # 从0.0001减少到0.00001
        self.logger.debug(f"传统请求生成完成，总共处理了 {processed_count} 个请求")

    async def _controlled_request_generation(self):
        """Controlled request generation (enhanced features)"""
        self.logger.debug("Starting controlled request generation")
        
        batch = []
        total_generated = 0
        
        try:
            for request in self.start_requests:
                batch.append(request)
                
                # 批量处理
                if len(batch) >= self.generation_batch_size:
                    generated = await self._process_generation_batch(batch)
                    total_generated += generated
                    batch = []
                
                # 背压检查
                if await self._should_pause_generation():
                    await self._wait_for_capacity()
            
            # 处理剩余请求
            if batch:
                generated = await self._process_generation_batch(batch)
                total_generated += generated
        
        except Exception as e:
            self.logger.error(f"Request generation failed: {e}")
        
        finally:
            self.start_requests = None
            self.logger.debug(f"Request generation completed, total: {total_generated}")

    async def _process_generation_batch(self, batch) -> int:
        """Process a batch of requests"""
        generated = 0
        
        for request in batch:
            if not self.running:
                break
            
            # 等待队列有空间
            while await self._is_queue_full() and self.running:
                await asyncio.sleep(0.01)  # 减少等待时间
            
            if self.running:
                await self.enqueue_request(request)
                generated += 1
                self._generation_stats['total_generated'] += 1
            
            # 控制生成速度，但使用更小的间隔
            if self.generation_interval > 0:
                await asyncio.sleep(self.generation_interval)
        
        return generated

    async def _should_pause_generation(self) -> bool:
        """Determine whether generation should be paused"""
        # 检查队列大小
        if await self._is_queue_full():
            return True
        
        # 检查任务管理器负载
        if self.task_manager:
            current_tasks = len(self.task_manager.current_task)
            if hasattr(self.task_manager, 'semaphore'):
                max_concurrency = getattr(self.task_manager.semaphore, '_initial_value', 8)
                if current_tasks >= max_concurrency * self.backpressure_ratio:
                    return True
        
        return False

    async def _is_queue_full(self) -> bool:
        """Check if queue is full"""
        if not self.scheduler:
            return False
        
        queue_size = len(self.scheduler)
        return queue_size >= self.max_queue_size * self.backpressure_ratio

    async def _wait_for_capacity(self):
        """Wait for system to have sufficient capacity"""
        self._generation_stats['backpressure_events'] += 1
        self.logger.debug("Backpressure triggered, pausing request generation")
        
        wait_time = 0.01  # 减少初始等待时间
        max_wait = 1.0  # 减少最大等待时间
        
        while await self._should_pause_generation() and self.running:
            await asyncio.sleep(wait_time)
            wait_time = min(wait_time * 1.1, max_wait)

    async def _open_spider(self):
        asyncio.create_task(self.crawler.subscriber.notify(CrawlerEvent.SPIDER_OPENED))
        # 直接调用crawl方法而不是创建任务，确保等待完成
        await self.crawl()

    async def _crawl(self, request):
        async def crawl_task():
            start_time = time.time()
            try:
                outputs = await self._fetch(request)
                # 记录响应时间
                response_time = time.time() - start_time
                if self.task_manager:
                    self.task_manager.record_response_time(response_time)
                
                # TODO 处理output
                if outputs:
                    await self._handle_spider_output(outputs)
            except Exception as e:
                # 记录详细的异常信息
                self.logger.error(
                    f"处理请求失败: {getattr(request, 'url', 'Unknown URL')} - {type(e).__name__}: {e}"
                )
                self.logger.debug(f"详细异常信息", exc_info=True)
                
                # 发送统计事件
                if hasattr(self.crawler, 'stats'):
                    self.crawler.stats.inc_value('downloader/exception_count')
                    self.crawler.stats.inc_value(f'downloader/exception_type_count/{type(e).__name__}')
                    if hasattr(request, 'url'):
                        self.crawler.stats.inc_value(f'downloader/failed_urls_count')
                
                # 不再重新抛出异常，避免未处理的Task异常
                return None

        # 使用异步任务创建，遵守并发限制
        await self.task_manager.create_task(crawl_task())

    async def _fetch(self, request):
        async def _successful(_response):
            callback: Callable = request.callback or self.spider.parse
            if _outputs := callback(_response):
                if iscoroutine(_outputs):
                    await _outputs
                else:
                    return transform(_outputs, _response)

        _response = await self.downloader.fetch(request)
        if _response is None:
            return None
        output = await _successful(_response)
        return output

    async def enqueue_request(self, start_request):
        await self._schedule_request(start_request)

    async def _schedule_request(self, request):
        # TODO 去重
        if await self.scheduler.enqueue_request(request):
            asyncio.create_task(self.crawler.subscriber.notify(CrawlerEvent.REQUEST_SCHEDULED, request, self.crawler.spider))

    async def _get_next_request(self):
        return await self.scheduler.next_request()

    async def _handle_spider_output(self, outputs):
        async for spider_output in outputs:
            if isinstance(spider_output, (Request, Item)):
                await self.processor.enqueue(spider_output)
            elif isinstance(spider_output, Exception):
                asyncio.create_task(
                    self.crawler.subscriber.notify(CrawlerEvent.SPIDER_ERROR, spider_output, self.spider)
                )
                raise spider_output
            else:
                raise OutputError(f'{type(self.spider)} must return `Request` or `Item`.')

    async def _exit(self):
        if self.scheduler.idle() and self.downloader.idle() and self.task_manager.all_done() and self.processor.idle():
            return True
        return False

    async def _should_exit(self) -> bool:
        """检查是否应该退出"""
        self.logger.debug(f"检查退出条件: start_requests={self.start_requests is not None}")
        # 没有启动请求，且所有队列都空闲
        if self.start_requests is None:
            self.logger.debug("start_requests 为 None，检查其他组件状态")
            # 使用异步的idle检查方法以获得更精确的结果
            scheduler_idle = await self.scheduler.async_idle() if hasattr(self.scheduler, 'async_idle') else self.scheduler.idle()
            downloader_idle = self.downloader.idle()
            task_manager_done = self.task_manager.all_done()
            processor_idle = self.processor.idle()
            
            self.logger.debug(f"组件状态 - Scheduler: {scheduler_idle}, Downloader: {downloader_idle}, TaskManager: {task_manager_done}, Processor: {processor_idle}")
            
            if (scheduler_idle and 
                downloader_idle and 
                task_manager_done and 
                processor_idle):
                # 立即进行二次检查，不等待
                scheduler_idle = await self.scheduler.async_idle() if hasattr(self.scheduler, 'async_idle') else self.scheduler.idle()
                downloader_idle = self.downloader.idle()
                task_manager_done = self.task_manager.all_done()
                processor_idle = self.processor.idle()
                
                self.logger.debug(f"二次检查组件状态 - Scheduler: {scheduler_idle}, Downloader: {downloader_idle}, TaskManager: {task_manager_done}, Processor: {processor_idle}")
                
                if (scheduler_idle and 
                    downloader_idle and 
                    task_manager_done and 
                    processor_idle):
                    self.logger.info("所有组件都空闲，准备退出")
                    return True
        else:
            self.logger.debug("start_requests 不为 None，不退出")
        
        return False

    async def close_spider(self):
        # 不再调用crawler.close()，避免重复清理
        # 清理工作应该由crawler的_lifecycle_manager上下文管理器来处理
        await asyncio.gather(*self.task_manager.current_task)
        await self.scheduler.close()
        await self.downloader.close()
    
    def get_generation_stats(self) -> dict:
        """获取生成统计"""
        return {
            **self._generation_stats,
            'queue_size': len(self.scheduler) if self.scheduler else 0,
            'active_tasks': len(self.task_manager.current_task) if self.task_manager else 0
        }
```

**code file end: crawlo/core/engine.py**

---


### code file start: crawlo/core/processor.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
from asyncio import Queue, create_task
from typing import Union, Optional

from crawlo import Request, Item
from crawlo.event import CrawlerEvent
from crawlo.exceptions import ItemDiscard
from crawlo.pipelines.pipeline_manager import PipelineManager


class Processor(object):

    def __init__(self, crawler):
        self.crawler = crawler
        self.queue: Queue = Queue()
        self.pipelines: Optional[PipelineManager] = None

    def open(self):
        self.pipelines = PipelineManager.from_crawler(self.crawler)

    async def process(self):
        while not self.idle():
            result = await self.queue.get()
            if isinstance(result, Request):
                await self.crawler.engine.enqueue_request(result)
            else:
                assert isinstance(result, Item)
                await self._process_item(result)

    async def _process_item(self, item):
        try:
            await self.pipelines.process_item(item=item)
        except ItemDiscard as exc:
            # 项目被管道丢弃（例如，去重管道）
            # 我们忽略这个项目，不传递给后续管道
            # 统计系统已在PipelineManager中通知，无需再次通知
            pass

    async def enqueue(self, output: Union[Request, Item]):
        await self.queue.put(output)
        await self.process()

    def idle(self) -> bool:
        return len(self) == 0

    def __len__(self):
        return self.queue.qsize()
```

**code file end: crawlo/core/processor.py**

---


### code file start: crawlo/core/scheduler.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import traceback
from typing import Optional, Callable

from crawlo.logging import get_logger
from crawlo.utils.request import set_request
from crawlo.utils.error_handler import ErrorHandler
from crawlo.utils.misc import load_object
from crawlo.project import common_call
from crawlo.utils.request_serializer import RequestSerializer
from crawlo.queue.queue_manager import QueueManager, QueueConfig, QueueType


class Scheduler:
    def __init__(self, crawler, dupe_filter, stats, priority):
        self.crawler = crawler
        self.queue_manager: Optional[QueueManager] = None
        self.request_serializer = RequestSerializer()

        self.logger = get_logger(self.__class__.__name__)
        self.error_handler = ErrorHandler(self.__class__.__name__)
        self.stats = stats
        self.dupe_filter = dupe_filter
        self.priority = priority

    @classmethod
    def create_instance(cls, crawler):
        filter_cls = load_object(crawler.settings.get('FILTER_CLASS'))
        o = cls(
            crawler=crawler,
            dupe_filter=filter_cls.create_instance(crawler),
            stats=crawler.stats,
            priority=crawler.settings.get('DEPTH_PRIORITY')
        )
        return o

    async def open(self):
        """Initialize scheduler and queue"""
        self.logger.debug("开始初始化调度器...")
        try:
            # 创建队列配置
            queue_config = QueueConfig.from_settings(self.crawler.settings)
            
            # 创建队列管理器
            self.queue_manager = QueueManager(queue_config)
            
            # 初始化队列
            needs_config_update = await self.queue_manager.initialize()
            
            # 检查是否需要更新过滤器配置
            updated_configs = []
            if needs_config_update:
                # 如果返回True，说明队列类型发生了变化，需要检查当前队列类型来决定更新方向
                if self.queue_manager._queue_type == QueueType.REDIS:
                    self._switch_to_redis_config()
                    updated_configs.append("Redis")
                else:
                    self._switch_to_memory_config()
                    updated_configs.append("内存")
            else:
                # 检查是否需要更新配置（即使队列管理器没有要求更新）
                # 当 QUEUE_TYPE 明确设置为 redis 时，也应该检查配置一致性
                queue_type_setting = self.crawler.settings.get('QUEUE_TYPE', 'memory')
                if queue_type_setting == 'redis' or needs_config_update:
                    updated_configs = self._check_filter_config()
                else:
                    updated_configs = []
            
            # 处理过滤器配置更新
            await self._process_filter_updates(needs_config_update, updated_configs)
            
            # 输出关键的调度器初始化完成信息
            status = self.queue_manager.get_status()
            current_filter = self.crawler.settings.get('FILTER_CLASS')
            
            self.logger.info(f"enabled filters: \n  {current_filter}")
            
            # 优化日志输出，将多条日志合并为1条关键信息
            queue_type_setting = self.crawler.settings.get('QUEUE_TYPE', 'memory')
            if queue_type_setting in ['auto', 'redis'] and updated_configs:
                concurrency = self.crawler.settings.get('CONCURRENCY', 8)
                delay = self.crawler.settings.get('DOWNLOAD_DELAY', 1.0)
                self.logger.debug(f"Scheduler initialized [Queue type: {status['type']}, Status: {status['health']}, Concurrency: {concurrency}, Delay: {delay}s]")
            else:
                self.logger.debug(f"Scheduler initialized [Queue type: {status['type']}, Status: {status['health']}]")
        except Exception as e:
            self.logger.error(f"Scheduler initialization failed: {e}")
            self.logger.debug(f"Detailed error information:\n{traceback.format_exc()}")
            raise
    
    def _check_filter_config(self):
        """检查并更新过滤器配置"""
        updated_configs = []
        
        if self.queue_manager._queue_type == QueueType.REDIS:
            # 检查当前过滤器是否为内存过滤器
            current_filter_class = self.crawler.settings.get('FILTER_CLASS', '')
            if 'memory_filter' in current_filter_class:
                self._switch_to_redis_config()
                updated_configs.append("Redis")
        elif self.queue_manager._queue_type == QueueType.MEMORY:
            # 检查当前过滤器是否为Redis过滤器
            current_filter_class = self.crawler.settings.get('FILTER_CLASS', '')
            if 'aioredis_filter' in current_filter_class or 'redis_filter' in current_filter_class:
                self._switch_to_memory_config()
                updated_configs.append("内存")
                
        return updated_configs
    
    async def _process_filter_updates(self, needs_config_update, updated_configs):
        """处理过滤器更新逻辑"""
        # 检查配置是否与队列类型匹配
        current_filter_class = self.crawler.settings.get('FILTER_CLASS', '')
        filter_matches_queue_type = self._is_filter_matching_queue_type(current_filter_class)
        
        # 只有在配置不匹配且需要更新时才重新创建过滤器实例
        if needs_config_update or not filter_matches_queue_type:
            # 如果需要更新配置，则执行更新
            if needs_config_update:
                # 重新创建过滤器实例，确保使用更新后的配置
                filter_cls = load_object(self.crawler.settings.get('FILTER_CLASS'))
                self.dupe_filter = filter_cls.create_instance(self.crawler)
                
                # 记录警告信息
                original_mode = "standalone" if 'memory_filter' in current_filter_class else "distributed"
                new_mode = "distributed" if self.queue_manager._queue_type == QueueType.REDIS else "standalone"
                if original_mode != new_mode:
                    self.logger.warning(f"runtime mode inconsistency detected: switched from {original_mode} to {new_mode} mode")
            elif not filter_matches_queue_type:
                # 配置不匹配，需要更新
                if self.queue_manager._queue_type == QueueType.REDIS:
                    self._switch_to_redis_config()
                elif self.queue_manager._queue_type == QueueType.MEMORY:
                    self._switch_to_memory_config()
                
                # 重新创建过滤器实例
                filter_cls = load_object(self.crawler.settings.get('FILTER_CLASS'))
                self.dupe_filter = filter_cls.create_instance(self.crawler)
    
    def _is_filter_matching_queue_type(self, current_filter_class):
        """检查过滤器配置是否与队列类型匹配"""
        return (
            (self.queue_manager._queue_type == QueueType.REDIS and 
             ('aioredis_filter' in current_filter_class or 'redis_filter' in current_filter_class)) or
            (self.queue_manager._queue_type == QueueType.MEMORY and 
             'memory_filter' in current_filter_class)
        )
    
    def _switch_to_redis_config(self):
        """切换到Redis配置"""
        if self.queue_manager and self.queue_manager._queue_type == QueueType.REDIS:
            # 检查当前过滤器是否为内存过滤器
            current_filter_class = self.crawler.settings.get('FILTER_CLASS', '')
            updated_configs = []
            
            if 'memory_filter' in current_filter_class:
                # 更新为Redis过滤器
                self.crawler.settings.set('FILTER_CLASS', 'crawlo.filters.aioredis_filter.AioRedisFilter')
                updated_configs.append("filter")
            
            # 检查当前去重管道是否为内存去重管道
            current_dedup_pipeline = self.crawler.settings.get('DEFAULT_DEDUP_PIPELINE', '')
            if 'memory_dedup_pipeline' in current_dedup_pipeline:
                # 更新为Redis去重管道
                self.crawler.settings.set('DEFAULT_DEDUP_PIPELINE', 'crawlo.pipelines.redis_dedup_pipeline.RedisDedupPipeline')
                # 同时更新PIPELINES列表中的去重管道
                pipelines = self.crawler.settings.get('PIPELINES', [])
                if current_dedup_pipeline in pipelines:
                    # 找到并替换内存去重管道为Redis去重管道
                    index = pipelines.index(current_dedup_pipeline)
                    pipelines[index] = 'crawlo.pipelines.redis_dedup_pipeline.RedisDedupPipeline'
                    self.crawler.settings.set('PIPELINES', pipelines)
                updated_configs.append("dedup pipeline")
            
            # 合并日志输出
            if updated_configs:
                self.logger.info(f"configuration updated: {', '.join(updated_configs)} -> redis mode")

    def _switch_to_memory_config(self):
        """切换到内存配置"""
        if self.queue_manager and self.queue_manager._queue_type == QueueType.MEMORY:
            # 检查当前过滤器是否为Redis过滤器
            current_filter_class = self.crawler.settings.get('FILTER_CLASS', '')
            updated_configs = []
            
            if 'aioredis_filter' in current_filter_class or 'redis_filter' in current_filter_class:
                # 更新为内存过滤器
                self.crawler.settings.set('FILTER_CLASS', 'crawlo.filters.memory_filter.MemoryFilter')
                updated_configs.append("filter")
            
            # 检查当前去重管道是否为Redis去重管道
            current_dedup_pipeline = self.crawler.settings.get('DEFAULT_DEDUP_PIPELINE', '')
            if 'redis_dedup_pipeline' in current_dedup_pipeline:
                # 更新为内存去重管道
                self.crawler.settings.set('DEFAULT_DEDUP_PIPELINE', 'crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline')
                # 同时更新PIPELINES列表中的去重管道
                pipelines = self.crawler.settings.get('PIPELINES', [])
                if current_dedup_pipeline in pipelines:
                    # 找到并替换Redis去重管道为内存去重管道
                    index = pipelines.index(current_dedup_pipeline)
                    pipelines[index] = 'crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline'
                    self.crawler.settings.set('PIPELINES', pipelines)
                updated_configs.append("dedup pipeline")
            
            # 合并日志输出
            if updated_configs:
                self.logger.debug(f"configuration updated: {', '.join(updated_configs)} -> memory mode")

    async def next_request(self):
        """Get next request"""
        if not self.queue_manager:
            return None
            
        try:
            request = await self.queue_manager.get()
            
            # 恢复 callback（从 Redis 队列取出时）
            if request:
                spider = getattr(self.crawler, 'spider', None)
                request = self.request_serializer.restore_after_deserialization(request, spider)
            
            return request
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="Failed to get next request", 
                raise_error=False
            )
            return None

    async def enqueue_request(self, request):
        """Add request to queue"""
        if not request.dont_filter and await common_call(self.dupe_filter.requested, request):
            self.dupe_filter.log_stats(request)
            return False

        if not self.queue_manager:
            self.logger.error("Queue manager not initialized")
            return False

        set_request(request, self.priority)
        
        try:
            # 使用统一的队列接口
            success = await self.queue_manager.put(request, priority=getattr(request, 'priority', 0))
            
            if success:
                self.logger.debug(f"Request enqueued successfully: {request.url}")
            
            return success
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="Failed to enqueue request", 
                raise_error=False
            )
            return False

    def idle(self) -> bool:
        """Check if queue is empty"""
        return len(self) == 0

    async def async_idle(self) -> bool:
        """Asynchronously check if queue is empty (more accurate)"""
        if not self.queue_manager:
            return True
        # 使用队列管理器的异步empty方法
        return await self.queue_manager.async_empty()

    async def close(self):
        """Close scheduler"""
        try:
            if isinstance(closed := getattr(self.dupe_filter, 'closed', None), Callable):
                await closed()
            
            if self.queue_manager:
                await self.queue_manager.close()
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="Failed to close scheduler", 
                raise_error=False
            )

    def __len__(self):
        """Get queue size"""
        if not self.queue_manager:
            return 0
        # 返回同步的近似值，实际大小需要异步获取
        return 0 if self.queue_manager.empty() else 1
```

**code file end: crawlo/core/scheduler.py**

---


### code file start: crawlo/core/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-

# Crawlo核心模块
# 提供框架的核心组件和初始化功能

# 使用新的初始化系统
from ..initialization import (
    initialize_framework,
    is_framework_ready
)


# 向后兼容的别名
def async_initialize_framework(*args, **kwargs):
    """Async wrapper for framework initialization"""
    return initialize_framework(*args, **kwargs)


def get_framework_initializer():
    """Get framework initializer - compatibility function"""
    from ..initialization.core import CoreInitializer
    return CoreInitializer()


def get_framework_logger(name='crawlo.core'):
    """Get framework logger - compatibility function"""
    from ..logging import get_logger
    return get_logger(name)


# 向后兼容
def bootstrap_framework(*args, **kwargs):
    """Bootstrap framework - compatibility function"""
    return initialize_framework(*args, **kwargs)


def get_bootstrap_manager():
    """Get bootstrap manager - compatibility function"""
    return get_framework_initializer()


__all__ = [
    'initialize_framework',
    'async_initialize_framework',
    'get_framework_initializer',
    'is_framework_ready',
    'get_framework_logger',
    # 向后兼容
    'bootstrap_framework',
    'get_bootstrap_manager'
]

```

**code file end: crawlo/core/__init__.py**

---


### code file start: crawlo/data/user_agents.py 

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
User-Agent列表
包含各种设备和浏览器的User-Agent字符串，用于爬虫伪装
"""

# 桌面浏览器User-Agent
DESKTOP_USER_AGENTS = [
    # Chrome (最新版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    
    # Chrome (较新版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    
    # Chrome (常用版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    
    # Firefox (最新版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Mozilla/5.0 (X11; Linux i686; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
    
    # Firefox (较新版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (X11; Linux i686; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
    
    # Safari (最新版本)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
    
    # Safari (较新版本)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    
    # Edge (最新版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.2917.92",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/135.0.2916.12",
    
    # Edge (较新版本)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.2915.72",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.2914.89",
    
    # Opera
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/122.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/122.0.0.0",
]

# 移动设备User-Agent
MOBILE_USER_AGENTS = [
    # iPhone (最新版本)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1",
    
    # iPhone (较新版本)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    
    # iPad (最新版本)
    "Mozilla/5.0 (iPad; CPU OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1",
    
    # iPad (较新版本)
    "Mozilla/5.0 (iPad; CPU OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    
    # Android (最新版本)
    "Mozilla/5.0 (Linux; Android 15; SM-S921B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6367.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6367.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6367.118 Mobile Safari/537.36",
    
    # Android (较新版本)
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6367.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6367.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.6367.118 Mobile Safari/537.36",
    
    # Android平板
    "Mozilla/5.0 (Linux; Android 14; SM-X916C Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/136.0.6367.118 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-X906C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/136.0.6367.118 Safari/537.36",
    
    # 其他移动浏览器
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36 EdgA/136.0.2917.92",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1 EdgiOS/136.2917.92",
]

# 爬虫/机器人User-Agent (用于测试)
BOT_USER_AGENTS = [
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "Mozilla/5.0 (compatible; DuckDuckBot/1.1; +http://duckduckgo.com/duckduckbot.html)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Mozilla/5.0 (compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php)",
    "Mozilla/5.0 (compatible; Twitterbot/1.0)",
]

# 按浏览器分类的User-Agent
CHROME_USER_AGENTS = [
    ua for ua in DESKTOP_USER_AGENTS + MOBILE_USER_AGENTS 
    if "Chrome" in ua and "Edg" not in ua and "OPR" not in ua
]

FIREFOX_USER_AGENTS = [
    ua for ua in DESKTOP_USER_AGENTS + MOBILE_USER_AGENTS 
    if "Firefox" in ua
]

SAFARI_USER_AGENTS = [
    ua for ua in DESKTOP_USER_AGENTS + MOBILE_USER_AGENTS 
    if "Safari" in ua and "Chrome" not in ua
]

EDGE_USER_AGENTS = [
    ua for ua in DESKTOP_USER_AGENTS + MOBILE_USER_AGENTS 
    if "Edg" in ua
]

OPERA_USER_AGENTS = [
    ua for ua in DESKTOP_USER_AGENTS + MOBILE_USER_AGENTS 
    if "OPR" in ua
]

# 所有User-Agent的组合列表
ALL_USER_AGENTS = DESKTOP_USER_AGENTS + MOBILE_USER_AGENTS

# 按设备类型分类的User-Agent字典
USER_AGENTS_BY_TYPE = {
    "desktop": DESKTOP_USER_AGENTS,
    "mobile": MOBILE_USER_AGENTS,
    "bot": BOT_USER_AGENTS,
    "all": ALL_USER_AGENTS,
    "chrome": CHROME_USER_AGENTS,
    "firefox": FIREFOX_USER_AGENTS,
    "safari": SAFARI_USER_AGENTS,
    "edge": EDGE_USER_AGENTS,
    "opera": OPERA_USER_AGENTS,
}


def get_user_agents(device_type="all"):
    """
    获取指定类型的User-Agent列表
    
    Args:
        device_type (str): 设备类型，可选值: "desktop", "mobile", "bot", "all", "chrome", "firefox", "safari", "edge", "opera"
        
    Returns:
        list: User-Agent字符串列表
    """
    return USER_AGENTS_BY_TYPE.get(device_type, ALL_USER_AGENTS)


def get_random_user_agent(device_type="all"):
    """
    获取随机User-Agent
    
    Args:
        device_type (str): 设备类型，可选值: "desktop", "mobile", "bot", "all", "chrome", "firefox", "safari", "edge", "opera"
        
    Returns:
        str: 随机User-Agent字符串
    """
    import random
    user_agents = get_user_agents(device_type)
    return random.choice(user_agents) if user_agents else ""


# 导出常用的User-Agent列表
__all__ = [
    "DESKTOP_USER_AGENTS",
    "MOBILE_USER_AGENTS",
    "BOT_USER_AGENTS",
    "CHROME_USER_AGENTS",
    "FIREFOX_USER_AGENTS",
    "SAFARI_USER_AGENTS",
    "EDGE_USER_AGENTS",
    "OPERA_USER_AGENTS",
    "ALL_USER_AGENTS",
    "USER_AGENTS_BY_TYPE",
    "get_user_agents",
    "get_random_user_agent"
]
```

**code file end: crawlo/data/user_agents.py**

---


### code file start: crawlo/data/__init__.py 

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Crawlo 数据模块
包含用户代理、字典等数据文件
"""
```

**code file end: crawlo/data/__init__.py**

---


### code file start: crawlo/downloader/aiohttp_downloader.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import asyncio
from yarl import URL
from typing import Optional
from aiohttp import (
    ClientSession,
    TCPConnector,
    ClientTimeout,
    TraceConfig,
    ClientResponse,
    ClientError,
    BasicAuth,
)

from crawlo.network.response import Response
from crawlo.logging import get_logger
from crawlo.downloader import DownloaderBase


class AioHttpDownloader(DownloaderBase):
    """
    高性能异步下载器
    - 基于持久化 ClientSession
    - 智能识别 Request 的高层语义（json_body/form_data）
    - 支持 GET/POST/PUT/DELETE 等方法
    - 支持中间件设置的 IP 代理（HTTP/HTTPS）
    - 内存安全防护
    """

    def __init__(self, crawler):
        super().__init__(crawler)
        self.session: Optional[ClientSession] = None
        self.max_download_size: int = 0
        self.logger = get_logger(self.__class__.__name__)

    def open(self):
        super().open()
        # 恢复关键的下载器启动信息为INFO级别
        # 读取配置
        timeout_secs = self.crawler.settings.get_int("DOWNLOAD_TIMEOUT", 30)
        verify_ssl = self.crawler.settings.get_bool("VERIFY_SSL", True)
        pool_limit = self.crawler.settings.get_int("CONNECTION_POOL_LIMIT", 300)  # 从200增加到300
        pool_per_host = self.crawler.settings.get_int("CONNECTION_POOL_LIMIT_PER_HOST", 100)  # 从50增加到100
        self.max_download_size = self.crawler.settings.get_int("DOWNLOAD_MAXSIZE", 10 * 1024 * 1024)  # 10MB

        # 创建连接器
        connector = TCPConnector(
            verify_ssl=verify_ssl,
            limit=pool_limit,
            limit_per_host=pool_per_host,
            ttl_dns_cache=300,
            keepalive_timeout=15,
            force_close=False,
            use_dns_cache=True,  # 启用DNS缓存
            family=0,  # 允许IPv4和IPv6
        )

        # 超时控制 - 增加更多超时设置
        timeout = ClientTimeout(
            total=timeout_secs,
            connect=timeout_secs/2,  # 连接超时
            sock_read=timeout_secs,  # 读取超时
            sock_connect=timeout_secs/2  # socket连接超时
        )

        # 请求追踪
        trace_config = TraceConfig()
        trace_config.on_request_start.append(self._on_request_start)
        trace_config.on_request_end.append(self._on_request_end)
        trace_config.on_request_exception.append(self._on_request_exception)

        # 创建全局 session
        self.session = ClientSession(
            connector=connector,
            timeout=timeout,
            trace_configs=[trace_config],
            auto_decompress=True,
        )

        # 输出下载器配置摘要
        spider_name = getattr(self.crawler.spider, 'name', 'Unknown')
        concurrency = self.crawler.settings.get('CONCURRENCY', 4)

    async def download(self, request) -> Optional[Response]:
        """下载请求并返回响应"""
        if not self.session or self.session.closed:
            raise RuntimeError("AioHttpDownloader session is not open.")

        start_time = None
        if self.crawler.settings.get_bool("DOWNLOAD_STATS", True):
            import time
            start_time = time.time()

        try:
            # 使用通用发送逻辑（支持所有 HTTP 方法）
            async with await self._send_request(self.session, request) as resp:
                # 安全检查：防止大响应体导致 OOM
                content_length = resp.headers.get("Content-Length")
                if content_length and int(content_length) > self.max_download_size:
                    raise OverflowError(f"Response too large: {content_length} > {self.max_download_size}")

                body = await resp.read()
                response = self._structure_response(request, resp, body)
                
                # 记录下载统计
                if start_time:
                    download_time = time.time() - start_time
                    self.logger.debug(f"Downloaded {request.url} in {download_time:.3f}s, size: {len(body)} bytes")
                
                return response

        except ClientError as e:
            self.logger.error(f"Client error for {request.url}: {e}")
            raise
        except Exception as e:
            self.logger.critical(f"Unexpected error for {request.url}: {e}", exc_info=True)
            raise

    @staticmethod
    async def _send_request(session: ClientSession, request) -> ClientResponse:
        """
        根据请求方法和高层语义智能发送请求。
        支持中间件设置的 proxy，兼容以下格式：
            - str: "http://user:pass@host:port"
            - dict: {"http": "...", "https": "..."} （自动取 http 或 https 字段）
        """
        method = request.method.lower()
        if not hasattr(session, method):
            raise ValueError(f"Unsupported HTTP method: {request.method}")

        method_func = getattr(session, method)

        # 构造参数
        kwargs = {
            "headers": request.headers,
            "cookies": request.cookies,
            "allow_redirects": request.allow_redirects,
        }

        # === 处理代理（proxy）===
        proxy = getattr(request, "proxy", None)
        proxy_auth = None

        if proxy:
            # 兼容字典格式：{"http": "http://...", "https": "http://..."}
            if isinstance(proxy, dict):
                # 优先使用 https，否则用 http
                proxy = proxy.get("https") or proxy.get("http")

            if not isinstance(proxy, (str, URL)):
                raise ValueError(f"proxy must be str or URL, got {type(proxy)}")

            try:
                proxy_url = URL(proxy)
                if proxy_url.scheme not in ("http", "https"):
                    raise ValueError(f"Unsupported proxy scheme: {proxy_url.scheme}, only HTTP/HTTPS supported.")

                # 提取认证信息
                if proxy_url.user and proxy_url.password:
                    proxy_auth = BasicAuth(proxy_url.user, proxy_url.password)
                    # 去掉用户密码的 URL
                    proxy = str(proxy_url.with_user(None))
                else:
                    proxy = str(proxy_url)

                kwargs["proxy"] = proxy
                if proxy_auth:
                    kwargs["proxy_auth"] = proxy_auth

            except Exception as e:
                raise ValueError(f"Invalid proxy URL: {proxy}") from e

        # 处理通过meta传递的代理认证信息
        meta_proxy_auth = request.meta.get("proxy_auth")
        if meta_proxy_auth and isinstance(meta_proxy_auth, dict):
            username = meta_proxy_auth.get("username")
            password = meta_proxy_auth.get("password")
            if username and password:
                kwargs["proxy_auth"] = BasicAuth(username, password)

        # === 处理请求体 ===
        if hasattr(request, "_json_body") and request._json_body is not None:
            kwargs["json"] = request._json_body
        elif isinstance(request.body, (dict, list)):
            kwargs["json"] = request.body
        else:
            if request.body is not None:
                kwargs["data"] = request.body

        return await method_func(request.url, **kwargs)

    @staticmethod
    def _structure_response(request, resp: ClientResponse, body: bytes) -> Response:
        """构造框架所需的 Response 对象"""
        return Response(
            url=str(resp.url),
            headers=dict(resp.headers),
            status_code=resp.status,
            body=body,
            request=request,
        )

    # --- 请求追踪日志 ---
    async def _on_request_start(self, session, trace_config_ctx, params):
        """请求开始时的回调。"""
        pass

    async def _on_request_end(self, session, trace_config_ctx, params):
        """请求成功结束时的回调。"""
        pass

    async def _on_request_exception(self, session, trace_config_ctx, params):
        """请求发生异常时的回调。"""
        pass

    async def close(self) -> None:
        """关闭会话资源"""
        if self.session and not self.session.closed:
            self.logger.info("Closing AioHttpDownloader session...")
            try:
                # 关闭 session
                await self.session.close()
                
                # 等待一小段时间确保连接完全关闭
                # 参考: https://docs.aiohttp.org/en/stable/client_advanced.html#graceful-shutdown
                await asyncio.sleep(0.25)
            except Exception as e:
                self.logger.warning(f"Error during session close: {e}")
            finally:
                self.session = None
        
        self.logger.debug("AioHttpDownloader closed.")

```

**code file end: crawlo/downloader/aiohttp_downloader.py**

---


### code file start: crawlo/downloader/cffi_downloader.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import asyncio
import random
import time
from typing import Optional, Dict, Any
from curl_cffi import CurlError
from curl_cffi.requests import AsyncSession

from crawlo.network.response import Response
from crawlo.downloader import DownloaderBase
from crawlo.logging import get_logger

class CurlCffiDownloader(DownloaderBase):
    """
    基于 curl-cffi 的高性能异步下载器
    - 支持真实浏览器指纹模拟，绕过Cloudflare等反爬虫检测
    - 高性能的异步HTTP客户端，基于libcurl
    - 内存安全的响应处理
    - 自动代理和Cookie管理
    - 支持请求延迟、重试、警告大小检查等高级功能
    """

    def __init__(self, crawler):
        # 调用父类初始化方法，确保 _closed 等属性被正确初始化
        super().__init__(crawler)
        
        self.logger = get_logger(self.__class__.__name__)
        self._active_requests = set()

        # --- 基础配置 ---
        timeout_secs = crawler.settings.get_int("DOWNLOAD_TIMEOUT", 180)
        verify_ssl = crawler.settings.get_bool("VERIFY_SSL", True)
        pool_size = crawler.settings.get_int("CONNECTION_POOL_LIMIT", 20)
        self.max_download_size = crawler.settings.get_int("DOWNLOAD_MAXSIZE", 10 * 1024 * 1024)  # 10MB
        self.download_warn_size = crawler.settings.get_int("DOWNLOAD_WARN_SIZE", 1024 * 1024)  # 1MB
        self.download_delay = crawler.settings.get_float("DOWNLOAD_DELAY", 0)
        self.randomize_delay = crawler.settings.get_bool("RANDOMIZE_DOWNLOAD_DELAY",
                                                              crawler.settings.get_bool("RANDOMNESS", False))
        # 不再使用DEFAULT_REQUEST_HEADERS配置项
        self.default_headers = {}

        # --- 浏览器指纹模拟配置 ---
        user_browser_map = crawler.settings.get_dict("CURL_BROWSER_VERSION_MAP", {})
        default_browser_map = self._get_default_browser_map()
        effective_browser_map = {**default_browser_map, **user_browser_map}

        raw_browser_type_str = crawler.settings.get("CURL_BROWSER_TYPE", "chrome")
        self.browser_type_str = effective_browser_map.get(raw_browser_type_str.lower(), raw_browser_type_str)

        # 创建会话配置
        session_config = {
            "timeout": timeout_secs,
            "verify": verify_ssl,
            "max_clients": pool_size,
            "impersonate": self.browser_type_str,
        }

        # 创建全局 session
        self.session = AsyncSession(**session_config)

        self.logger.info(f"CurlCffiDownloader 初始化完成 | 浏览器模拟: {self.browser_type_str} | "
                         f"并发: {pool_size} | 延迟: {self.download_delay}s")

    @staticmethod
    def _get_default_browser_map() -> Dict[str, str]:
        """获取代码中硬编码的默认浏览器映射"""
        return {
            "chrome": "chrome136",
            "edge": "edge101",
            "safari": "safari184",
            "firefox": "firefox135",
        }

    async def download(self, request) -> Optional[Response]:
        if not self.session:
            raise RuntimeError("CurlCffiDownloader 会话未打开")

        await self._apply_download_delay()

        max_retries = self.crawler.settings.get_int("DOWNLOAD_RETRY_TIMES",
                                                    self.crawler.settings.get_int("MAX_RETRY_TIMES", 1))
        last_exception = None

        for attempt in range(max_retries + 1):
            request_id = id(request)
            self._active_requests.add(request_id)
            try:
                result = await self._execute_request(request)
                return result

            except (CurlError, asyncio.TimeoutError) as e:
                last_exception = e
                if attempt < max_retries:
                    retry_delay = 2 ** attempt
                    self.logger.warning(
                        f"第 {attempt + 1}/{max_retries} 次重试 {request.url}，等待 {retry_delay}s，原因: {type(e).__name__}")
                    await asyncio.sleep(retry_delay)
                else:
                    self.logger.error(
                        f"请求 {request.url} 在 {max_retries} 次重试后失败: {type(e).__name__}: {e}")
            except Exception as e:
                last_exception = e
                self.logger.critical(f"请求 {request.url} 发生未预期错误: {e}", exc_info=True)
                break  # 不可恢复错误，不再重试
            finally:
                self._active_requests.discard(request_id)

        if last_exception:
            raise last_exception
        raise RuntimeError(f"下载 {request.url} 失败，已重试或发生不可重试错误")

    async def _apply_download_delay(self):
        """应用下载延迟"""
        if self.download_delay > 0:
            current_time = time.time()
            elapsed = current_time - getattr(self, '_last_request_time', float('inf'))

            if elapsed < self.download_delay:
                delay = self.download_delay - elapsed
                if self.randomize_delay:
                    range_tuple = self.crawler.settings.get("RANDOM_RANGE", (0.75, 1.25))
                    if isinstance(range_tuple, (list, tuple)) and len(range_tuple) == 2:
                        delay *= random.uniform(range_tuple[0], range_tuple[1])
                    else:
                        delay *= random.uniform(0.5, 1.5)
                await asyncio.sleep(max(0.0, delay))
            self._last_request_time = time.time()

    async def _execute_request(self, request) -> Response:
        """执行单个请求"""
        if not self.session:
            raise RuntimeError("会话未初始化")

        start_time = None
        if self.crawler.settings.get_bool("DOWNLOAD_STATS", True):
            import time
            start_time = time.time()

        kwargs = self._build_request_kwargs(request)
        method = request.method.lower()

        if not hasattr(self.session, method):
            raise ValueError(f"不支持的 HTTP 方法: {request.method}")

        method_func = getattr(self.session, method)

        try:
            response = await method_func(request.url, **kwargs)
        except Exception as e:
            raise  # 由外层处理重试

        # 检查 Content-Length
        content_length = response.headers.get("Content-Length")
        if content_length:
            try:
                cl = int(content_length)
                if cl > self.max_download_size:
                    raise OverflowError(f"响应过大 (Content-Length): {cl} > {self.max_download_size}")
            except ValueError:
                self.logger.warning(f"无效的 Content-Length 头部: {content_length}")

        body = response.content
        actual_size = len(body)

        if actual_size > self.max_download_size:
            raise OverflowError(f"响应体过大: {actual_size} > {self.max_download_size}")

        if actual_size > self.download_warn_size:
            self.logger.warning(f"响应体较大: {actual_size} 字节，来自 {request.url}")

        # 记录下载统计
        if start_time:
            download_time = time.time() - start_time
            self.logger.debug(f"Downloaded {request.url} in {download_time:.3f}s, size: {actual_size} bytes")

        return self._structure_response(request, response, body)

    def _build_request_kwargs(self, request) -> Dict[str, Any]:
        """构造curl-cffi请求参数（支持 str 和 dict 格式 proxy）"""
        request_headers = getattr(request, 'headers', {}) or {}
        headers = {**self.default_headers, **request_headers}

        kwargs = {
            "headers": headers,
            "cookies": getattr(request, 'cookies', {}) or {},
            "allow_redirects": getattr(request, 'allow_redirects', True),
        }

        # 处理代理（兼容 str 和 dict）
        proxy = getattr(request, 'proxy', None)
        if proxy is not None:
            if isinstance(proxy, str):
                if proxy.startswith(('http://', 'https://', 'socks5://', 'socks4://')):
                    kwargs["proxies"] = {"http": proxy, "https": proxy}
                else:
                    self.logger.warning(f"代理协议未知，尝试直接使用: {proxy}")
                    kwargs["proxies"] = {"http": proxy, "https": proxy}
            elif isinstance(proxy, dict):
                kwargs["proxies"] = proxy
            else:
                self.logger.error(f"不支持的 proxy 类型: {type(proxy)}，值: {proxy}")

        # 处理通过meta传递的代理认证信息
        proxy_auth_header = request.headers.get("Proxy-Authorization") or request.meta.get("proxy_auth_header")
        if proxy_auth_header:
            kwargs["headers"]["Proxy-Authorization"] = proxy_auth_header

        # 请求体处理
        if hasattr(request, "_json_body") and request._json_body is not None:
            kwargs["json"] = request._json_body
        elif isinstance(getattr(request, 'body', None), (dict, list)):
            kwargs["json"] = request.body
        elif getattr(request, 'body', None) is not None:
            kwargs["data"] = request.body

        return kwargs

    @staticmethod
    def _structure_response(request, response, body: bytes) -> Response:
        """构造框架所需的 Response 对象"""
        return Response(
            url=str(response.url),
            headers=dict(response.headers),
            status_code=response.status_code,
            body=body,
            request=request,
        )

    async def close(self) -> None:
        """关闭会话资源"""
        if self.session:
            self.logger.info("正在关闭 CurlCffiDownloader 会话...")
            try:
                await self.session.close()
            except Exception as e:
                self.logger.warning(f"关闭 curl-cffi 会话时出错: {e}")
            finally:
                self.session = None
                # 清空活跃请求跟踪
                self._active_requests.clear()
        
        self.logger.debug("CurlCffiDownloader 已关闭")

    def idle(self) -> bool:
        """检查是否空闲"""
        return len(self._active_requests) == 0

    def __len__(self) -> int:
        """返回活跃请求数"""
        return len(self._active_requests)
```

**code file end: crawlo/downloader/cffi_downloader.py**

---


### code file start: crawlo/downloader/httpx_downloader.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import httpx
from typing import Optional
from httpx import AsyncClient, Timeout, Limits

from crawlo.network.response import Response
from crawlo.downloader import DownloaderBase
from crawlo.logging import get_logger

# 尝试导入 httpx 异常，用于更精确地捕获
try:
    # httpx 0.23.0+ 将异常移到了 _exceptions
    from httpx import ConnectError, TimeoutException, NetworkError, HTTPStatusError
except ImportError:
    try:
        # 旧版本可能在 httpcore 或顶层
        from httpcore import ConnectError
        from httpx import TimeoutException, NetworkError, HTTPStatusError
    except ImportError:
        ConnectError = httpx.ConnectError
        TimeoutException = httpx.TimeoutException
        NetworkError = httpx.NetworkError
        HTTPStatusError = httpx.HTTPStatusError

# 定义我们认为是网络问题，应该触发降级的异常
NETWORK_EXCEPTIONS = (ConnectError, TimeoutException, NetworkError)


class HttpXDownloader(DownloaderBase):
    """
    基于 httpx 的高性能异步下载器
    - 使用持久化 AsyncClient（推荐做法）
    - 支持连接池、HTTP/2、透明代理
    - 智能处理 Request 的 json_body 和 form_data
    - 支持代理失败后自动降级为直连
    """

    def __init__(self, crawler):
        super().__init__(crawler)
        self._client: Optional[AsyncClient] = None
        self._client_timeout: Optional[Timeout] = None
        self._client_limits: Optional[Limits] = None
        self._client_verify: bool = True
        self._client_http2: bool = False
        self.max_download_size: Optional[int] = None
        # ------------------------
        self._timeout: Optional[Timeout] = None
        self._limits: Optional[Limits] = None
        # --- 获取 logger 实例 ---
        self.logger = get_logger(self.__class__.__name__)

    def open(self):
        super().open()
        self.logger.info("Opening HttpXDownloader")

        # 读取配置
        timeout_total = self.crawler.settings.get_int("DOWNLOAD_TIMEOUT", 30)
        pool_limit = self.crawler.settings.get_int("CONNECTION_POOL_LIMIT", 100)
        pool_per_host = self.crawler.settings.get_int("CONNECTION_POOL_LIMIT_PER_HOST", 20)
        max_download_size = self.crawler.settings.get_int("DOWNLOAD_MAXSIZE", 10 * 1024 * 1024)  # 10MB

        # 保存配置
        self.max_download_size = max_download_size

        # --- 保存客户端配置以便复用 ---
        self._client_timeout = Timeout(
            connect=10.0,  # 建立连接超时
            read=timeout_total - 10.0 if timeout_total > 10 else timeout_total / 2,  # 读取数据超时
            write=10.0,  # 发送数据超时
            pool=1.0  # 从连接池获取连接的超时
        )
        self._client_limits = Limits(
            max_connections=pool_limit,
            max_keepalive_connections=pool_per_host
        )
        self._client_verify = self.crawler.settings.get_bool("VERIFY_SSL", True)
        self._client_http2 = True  # 启用 HTTP/2 支持
        # ----------------------------

        # 创建持久化客户端 (不在此处设置全局代理)
        self._client = AsyncClient(
            timeout=self._client_timeout,
            limits=self._client_limits,
            verify=self._client_verify,
            http2=self._client_http2,
            follow_redirects=True,  # 自动跟随重定向
            # 注意：此处不设置 proxy 或 proxies
        )

        self.logger.debug("HttpXDownloader initialized.")

    async def download(self, request) -> Optional[Response]:
        """下载请求并返回响应，支持代理失败后的优雅降级"""
        if not self._client:
            raise RuntimeError("HttpXDownloader client is not available.")

        start_time = None
        if self.crawler.settings.get_bool("DOWNLOAD_STATS", True):
            import time
            start_time = time.time()

        # --- 1. 确定要使用的 client 实例 ---
        effective_client = self._client  # 默认使用共享的主 client
        temp_client = None  # 用于可能创建的临时 client
        used_proxy = None  # 记录当前尝试使用的代理

        try:
            # --- 2. 构造发送参数 (不包含 proxy/proxies) ---
            kwargs = {
                "method": request.method,
                "url": request.url,
                "headers": request.headers,
                "cookies": request.cookies,
                "follow_redirects": request.allow_redirects,
            }

            # 智能处理 body（关键优化）
            if hasattr(request, "_json_body") and request._json_body is not None:
                kwargs["json"] = request._json_body  # 让 httpx 处理序列化
            elif isinstance(request.body, (dict, list)):
                kwargs["json"] = request.body
            else:
                kwargs["content"] = request.body  # 使用 content 而不是 data

            # --- 3. 处理代理 ---
            httpx_proxy_config = None  # 用于初始化临时 client 的代理配置
            if request.proxy:
                # 根据 request.proxy 的类型准备 httpx 的 proxy 参数
                if isinstance(request.proxy, str):
                    # 直接是代理 URL 字符串
                    httpx_proxy_config = request.proxy
                elif isinstance(request.proxy, dict):
                    # 从字典中选择合适的代理 URL
                    # 优先选择与请求协议匹配的，否则 fallback 到 http
                    from urllib.parse import urlparse
                    request_scheme = urlparse(request.url).scheme
                    if request_scheme == "https" and request.proxy.get("https"):
                        httpx_proxy_config = request.proxy["https"]
                    elif request.proxy.get("http"):
                        httpx_proxy_config = request.proxy["http"]
                    else:
                        # 如果没有匹配的，尝试使用任意一个
                        httpx_proxy_config = next(iter(request.proxy.values()), None)
                        if httpx_proxy_config:
                            self.logger.warning(
                                f"No specific proxy for scheme '{request_scheme}', using '{httpx_proxy_config}'"
                            )

                # 如果成功解析出代理配置，则创建临时 client
                if httpx_proxy_config:
                    try:
                        # --- 4. 创建临时 client，配置代理 ---
                        # 使用在 open() 中保存的配置
                        temp_client = AsyncClient(
                            timeout=self._client_timeout,
                            limits=self._client_limits,
                            verify=self._client_verify,
                            http2=self._client_http2,
                            follow_redirects=True,  # 确保继承
                            proxy=httpx_proxy_config,  # 设置代理
                        )
                        effective_client = temp_client
                        used_proxy = httpx_proxy_config  # 记录使用的代理
                        self.logger.debug(f"Using temporary client with proxy: {httpx_proxy_config} for {request.url}")
                    except Exception as e:
                        self.logger.error(
                            f"Failed to create temporary client with proxy {httpx_proxy_config} for {request.url}: {e}")
                        # 出错则回退到使用主 client（无代理）
                        # 可以选择抛出异常或继续
                        # raise # 如果希望代理失败导致请求失败，取消注释

            # --- 5. 发送请求 (带降级逻辑) ---
            try:
                httpx_response = await effective_client.request(**kwargs)
            except NETWORK_EXCEPTIONS as proxy_error:
                # --- 优雅降级逻辑 ---
                # 如果我们刚刚尝试使用了代理 (temp_client) 并且失败了
                if temp_client is not None and effective_client is temp_client:
                    # 记录警告日志
                    self.logger.warning(
                        f"代理请求失败 ({used_proxy}), 正在尝试直连: {request.url} | 错误: {repr(proxy_error)}"
                    )
                    # 关闭失败的临时客户端
                    await temp_client.aclose()
                    temp_client = None  # 防止 finally 再次关闭

                    # 切换到主客户端（直连）
                    effective_client = self._client
                    # 再次尝试发送请求
                    httpx_response = await effective_client.request(**kwargs)
                else:
                    # 如果是主客户端（直连）失败，或者不是网络错误，则重新抛出
                    raise

            # --- 6. 安全检查：防止大响应体 ---
            content_length = httpx_response.headers.get("Content-Length")
            if content_length and int(content_length) > self.max_download_size:
                await httpx_response.aclose()  # 立即关闭连接，释放资源
                raise OverflowError(f"Response too large: {content_length} > {self.max_download_size}")

            # --- 7. 读取响应体 ---
            body = await httpx_response.aread()

            # --- 8. 记录下载统计 ---
            if start_time:
                download_time = time.time() - start_time
                self.logger.debug(f"Downloaded {request.url} in {download_time:.3f}s, size: {len(body)} bytes")

            # --- 9. 构造并返回 Response ---
            return self.structure_response(request=request, response=httpx_response, body=body)

        except httpx.TimeoutException as e:
            self.logger.error(f"Timeout error for {request.url}: {e}")
            raise
        except httpx.NetworkError as e:
            self.logger.error(f"Network error for {request.url}: {e}")
            raise
        except httpx.HTTPStatusError as e:
            self.logger.warning(f"HTTP {e.response.status_code} for {request.url}: {e}")
            # 即使是 4xx/5xx，也返回 Response，由上层逻辑（如 spider）处理
            # 如果需要在此处 raise，可取消注释下一行
            # raise
            # 读取响应体以便 structure_response 处理
            try:
                error_body = await e.response.aread()
            except Exception:
                error_body = b""  # 如果读取错误响应体失败，则为空
            return self.structure_response(request=request, response=e.response, body=error_body)
        except Exception as e:
            self.logger.critical(f"Unexpected error for {request.url}: {e}", exc_info=True)
            raise

        finally:
            # --- 10. 清理：关闭临时 client ---
            # 如果创建了临时 client，则关闭它
            if temp_client:
                try:
                    await temp_client.aclose()
                    # self.logger.debug("Closed temporary client.")
                except Exception as e:
                    self.logger.warning(f"Error closing temporary client: {e}")

    @staticmethod
    def structure_response(request, response: httpx.Response, body: bytes) -> Response:
        return Response(
            url=str(response.url),  # httpx 的 URL 是对象，需转字符串
            headers=dict(response.headers),
            status_code=response.status_code,  # 注意：使用 status_code
            body=body,
            request=request
        )

    async def close(self) -> None:
        """关闭主客户端"""
        if self._client:
            self.logger.info("Closing HttpXDownloader client...")
            try:
                await self._client.aclose()
            except Exception as e:
                self.logger.warning(f"Error during client close: {e}")
            finally:
                self._client = None
        
        self.logger.debug("HttpXDownloader closed.")

```

**code file end: crawlo/downloader/httpx_downloader.py**

---


### code file start: crawlo/downloader/hybrid_downloader.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
混合下载器
=========
智能选择合适的下载器处理不同类型的请求，支持协议请求和动态加载内容。

支持的场景:
1. 列表页、详情页都要动态加载
2. 列表页使用协议请求、详情页使用动态加载
3. 列表页使用动态加载，详情页使用协议请求

功能特性:
1. 智能检测内容类型并选择合适的下载器
2. 支持基于URL模式的下载器选择
3. 支持基于请求标记的下载器选择
4. 统一的接口和响应格式
5. 自动资源管理和优化
"""
from typing import Optional, Dict, Type
from urllib.parse import urlparse

from crawlo.downloader import DownloaderBase
from crawlo.network.request import Request
from crawlo.network.response import Response
from crawlo.logging import get_logger

# 动态导入下载器（避免循环导入）
try:
    from .aiohttp_downloader import AioHttpDownloader
except ImportError:
    AioHttpDownloader = None

try:
    from .httpx_downloader import HttpXDownloader
except ImportError:
    HttpXDownloader = None

try:
    from .cffi_downloader import CurlCffiDownloader
except ImportError:
    CurlCffiDownloader = None

try:
    from .selenium_downloader import SeleniumDownloader
except ImportError:
    SeleniumDownloader = None

try:
    from .playwright_downloader import PlaywrightDownloader
except ImportError:
    PlaywrightDownloader = None


class HybridDownloader(DownloaderBase):
    """
    混合下载器 - 根据请求特征智能选择合适的下载器
    """

    def __init__(self, crawler):
        super().__init__(crawler)
        self.logger = get_logger(self.__class__.__name__)
        
        # 下载器实例缓存
        self._downloaders: Dict[str, DownloaderBase] = {}
        
        # 配置选项
        self.default_protocol_downloader = crawler.settings.get("HYBRID_DEFAULT_PROTOCOL_DOWNLOADER", "aiohttp")
        self.default_dynamic_downloader = crawler.settings.get("HYBRID_DEFAULT_DYNAMIC_DOWNLOADER", "playwright")
        
        # URL模式配置
        self.dynamic_url_patterns = set(crawler.settings.get_list("HYBRID_DYNAMIC_URL_PATTERNS", []))
        self.protocol_url_patterns = set(crawler.settings.get_list("HYBRID_PROTOCOL_URL_PATTERNS", []))
        
        # 域名配置
        self.dynamic_domains = set(crawler.settings.get_list("HYBRID_DYNAMIC_DOMAINS", []))
        self.protocol_domains = set(crawler.settings.get_list("HYBRID_PROTOCOL_DOMAINS", []))

    def open(self):
        super().open()
        self.logger.info("Opening HybridDownloader")
        
        # 初始化默认下载器
        self._initialize_default_downloaders()

    def _initialize_default_downloaders(self):
        """初始化默认下载器"""
        # 初始化协议下载器
        protocol_downloader_cls = self._get_downloader_class(self.default_protocol_downloader)
        if protocol_downloader_cls:
            self._downloaders["protocol"] = protocol_downloader_cls(self.crawler)
            self._downloaders["protocol"].open()
            
        # 初始化动态下载器
        dynamic_downloader_cls = self._get_downloader_class(self.default_dynamic_downloader)
        if dynamic_downloader_cls:
            self._downloaders["dynamic"] = dynamic_downloader_cls(self.crawler)
            # 使用标准的 open 方法初始化下载器
            self._downloaders["dynamic"].open()
                
        self.logger.debug("Default downloaders initialized")

    def _get_downloader_class(self, downloader_type: str) -> Optional[Type[DownloaderBase]]:
        """根据类型获取下载器类"""
        downloader_map = {
            "aiohttp": AioHttpDownloader,
            "httpx": HttpXDownloader,
            "curl_cffi": CurlCffiDownloader,
            "selenium": SeleniumDownloader,
            "playwright": PlaywrightDownloader
        }
        return downloader_map.get(downloader_type.lower())

    async def download(self, request: Request) -> Optional[Response]:
        """根据请求特征选择合适的下载器并下载"""
        # 确定应该使用的下载器类型
        downloader_type = self._determine_downloader_type(request)
        
        # 获取对应的下载器
        downloader = self._get_or_create_downloader(downloader_type)
        if not downloader:
            raise RuntimeError(f"No downloader available for type: {downloader_type}")
        
        self.logger.debug(f"Using {downloader_type} downloader for {request.url}")
        
        # 执行下载
        return await downloader.download(request)

    def _determine_downloader_type(self, request: Request) -> str:
        """根据请求特征确定下载器类型"""
        url = request.url
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        
        # 1. 检查请求标记
        if request.meta.get("use_dynamic_loader"):
            return "dynamic"
        elif request.meta.get("use_protocol_loader"):
            return "protocol"
            
        # 2. 检查URL模式
        for pattern in self.dynamic_url_patterns:
            if pattern in url:
                return "dynamic"
                
        for pattern in self.protocol_url_patterns:
            if pattern in url:
                return "protocol"
                
        # 3. 检查域名
        if domain in self.dynamic_domains:
            return "dynamic"
            
        if domain in self.protocol_domains:
            return "protocol"
            
        # 4. 检查文件扩展名（动态内容通常没有特定扩展名）
        path = parsed_url.path.lower()
        static_extensions = {'.js', '.css', '.jpg', '.jpeg', '.png', '.gif', '.ico', '.pdf', '.zip', '.doc', '.docx'}
        if any(path.endswith(ext) for ext in static_extensions):
            return "protocol"
            
        # 5. 检查请求方法（POST请求更可能需要动态加载）
        if request.method.upper() == "POST":
            return "dynamic"
            
        # 6. 默认策略：根据内容类型推测
        # 如果URL中包含典型的动态内容标识符
        dynamic_indicators = ['ajax', 'api', 'dynamic', 'spa', 'react', 'vue', 'angular']
        if any(indicator in url.lower() for indicator in dynamic_indicators):
            return "dynamic"
            
        # 默认使用协议下载器
        return "protocol"

    def _get_or_create_downloader(self, downloader_type: str) -> Optional[DownloaderBase]:
        """获取或创建下载器实例"""
        # 如果已经存在，直接返回
        if downloader_type in self._downloaders:
            return self._downloaders[downloader_type]
            
        # 创建新的下载器实例
        if downloader_type == "protocol":
            downloader_cls = self._get_downloader_class(self.default_protocol_downloader)
        elif downloader_type == "dynamic":
            downloader_cls = self._get_downloader_class(self.default_dynamic_downloader)
        else:
            return None
            
        if not downloader_cls:
            return None
            
        downloader = downloader_cls(self.crawler)
        # 使用标准的 open 方法初始化下载器
        downloader.open()
            
        self._downloaders[downloader_type] = downloader
        return downloader

    async def close(self) -> None:
        """关闭所有下载器"""
        for name, downloader in self._downloaders.items():
            try:
                if hasattr(downloader, 'close_async'):
                    await downloader.close_async()
                else:
                    await downloader.close()
                self.logger.debug(f"Closed {name} downloader")
            except Exception as e:
                self.logger.warning(f"Error closing {name} downloader: {e}")
                
        self._downloaders.clear()
        self.logger.info("HybridDownloader closed.")
```

**code file end: crawlo/downloader/hybrid_downloader.py**

---


### code file start: crawlo/downloader/playwright_downloader.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Playwright 下载器
===============
支持动态加载内容的下载器，基于 Playwright 实现。

功能特性:
- 支持 Chromium/Firefox/WebKit 浏览器引擎
- 异步非阻塞操作
- 智能等待页面加载完成
- 支持自定义浏览器上下文和选项
- 内存安全的资源管理
- 自动处理 Cookie 和本地存储
- 支持翻页操作（鼠标滑动、点击翻页）
- 单浏览器多标签页模式
"""
import time
from typing import Optional, Dict, List
from urllib.parse import urlparse

from playwright.async_api import async_playwright, Playwright, Browser, Page, BrowserContext

from crawlo.downloader import DownloaderBase
from crawlo.network.response import Response
from crawlo.logging import get_logger


class PlaywrightDownloader(DownloaderBase):
    """
    基于 Playwright 的动态内容下载器
    支持处理 JavaScript 渲染的网页内容，性能优于 Selenium
    """

    def __init__(self, crawler):
        super().__init__(crawler)
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.logger = get_logger(self.__class__.__name__)
        self.default_timeout = crawler.settings.get_int("PLAYWRIGHT_TIMEOUT", 30000)  # 毫秒
        self.load_timeout = crawler.settings.get_int("PLAYWRIGHT_LOAD_TIMEOUT", 10000)  # 毫秒
        self.browser_type = crawler.settings.get("PLAYWRIGHT_BROWSER_TYPE", "chromium").lower()
        self.headless = crawler.settings.get_bool("PLAYWRIGHT_HEADLESS", True)
        self.wait_for_element = crawler.settings.get("PLAYWRIGHT_WAIT_FOR_ELEMENT", None)
        self.viewport_width = crawler.settings.get_int("PLAYWRIGHT_VIEWPORT_WIDTH", 1920)
        self.viewport_height = crawler.settings.get_int("PLAYWRIGHT_VIEWPORT_HEIGHT", 1080)
        
        # 单浏览器多标签页模式
        self.single_browser_mode = crawler.settings.get_bool("PLAYWRIGHT_SINGLE_BROWSER_MODE", True)
        self.max_pages_per_browser = crawler.settings.get_int("PLAYWRIGHT_MAX_PAGES_PER_BROWSER", 10)
        self._page_pool: List[Page] = []
        self._used_pages: set = set()

    def open(self):
        super().open()
        self.logger.info("Opening PlaywrightDownloader")

    async def download(self, request) -> Optional[Response]:
        """下载动态内容"""
        if not self.playwright or not self.browser or not self.context:
            await self._initialize_playwright()

        start_time = None
        if self.crawler.settings.get_bool("DOWNLOAD_STATS", True):
            start_time = time.time()

        page: Optional[Page] = None
        try:
            # 获取页面（支持单浏览器多标签页模式）
            page = await self._get_page()
            
            # 设置超时
            page.set_default_timeout(self.default_timeout)
            page.set_default_navigation_timeout(self.load_timeout)
            
            # 设置视口
            await page.set_viewport_size({
                "width": self.viewport_width,
                "height": self.viewport_height
            })
            
            # 应用请求特定的设置
            await self._apply_request_settings(page, request)
            
            # 访问页面
            response = await page.goto(request.url, wait_until="networkidle")
            
            # 等待页面加载完成
            await self._wait_for_page_load(page)
            
            # 执行自定义操作（如果有）
            await self._execute_custom_actions(page, request)
            
            # 执行翻页操作（如果有）
            await self._execute_pagination_actions(page, request)
            
            # 获取页面内容
            page_content = await page.content()
            page_url = page.url
            
            # 获取响应信息
            status_code = response.status if response else 200
            headers = dict(response.headers) if response else {}
            
            # 获取 Cookies
            cookies = await self._get_cookies()
            
            # 构造响应对象
            crawlo_response = Response(
                url=page_url,
                headers=headers,
                status_code=status_code,
                body=page_content.encode('utf-8'),
                request=request
            )
            
            # 添加 Cookies 到响应
            crawlo_response.cookies = cookies
            
            # 记录下载统计
            if start_time:
                download_time = time.time() - start_time
                self.logger.debug(f"Downloaded {request.url} in {download_time:.3f}s")
                
            return crawlo_response

        except Exception as e:
            self.logger.error(f"Error downloading {request.url}: {e}")
            raise
        finally:
            # 归还页面到池中
            if page:
                await self._release_page(page)

    async def _initialize_playwright(self):
        """初始化 Playwright"""
        try:
            self.playwright = await async_playwright().start()
            
            # 获取代理配置
            proxy_config = self.crawler.settings.get("PLAYWRIGHT_PROXY")
            launch_kwargs = {
                "headless": self.headless
            }
            
            # 如果配置了代理，则添加代理参数
            if proxy_config:
                if isinstance(proxy_config, str):
                    # 简单的代理URL
                    launch_kwargs["proxy"] = {
                        "server": proxy_config
                    }
                elif isinstance(proxy_config, dict):
                    # 完整的代理配置
                    launch_kwargs["proxy"] = proxy_config
            
            # 根据配置选择浏览器类型
            if self.browser_type == "chromium":
                self.browser = await self.playwright.chromium.launch(**launch_kwargs)
            elif self.browser_type == "firefox":
                self.browser = await self.playwright.firefox.launch(**launch_kwargs)
            elif self.browser_type == "webkit":
                self.browser = await self.playwright.webkit.launch(**launch_kwargs)
            else:
                raise ValueError(f"Unsupported browser type: {self.browser_type}")
            
            # 创建浏览器上下文
            self.context = await self.browser.new_context()
            
            # 应用全局设置
            await self._apply_global_settings()
            
            self.logger.debug(f"PlaywrightDownloader initialized with {self.browser_type}")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Playwright: {e}")
            raise

    async def _apply_global_settings(self):
        """应用全局浏览器设置"""
        if not self.context:
            return
            
        # 设置用户代理
        user_agent = self.crawler.settings.get("USER_AGENT")
        if user_agent:
            await self.context.set_extra_http_headers({"User-Agent": user_agent})
            
        # 设置代理
        proxy = self.crawler.settings.get("PLAYWRIGHT_PROXY")
        if proxy:
            # Playwright 的代理设置在启动浏览器时配置
            pass

    async def _apply_request_settings(self, page: Page, request):
        """应用请求特定的设置"""
        # 设置请求头
        if request.headers:
            await page.set_extra_http_headers(request.headers)
            
        # 设置 Cookies
        if request.cookies:
            cookies = []
            for name, value in request.cookies.items():
                # 需要确定域名和路径
                parsed_url = urlparse(request.url)
                cookies.append({
                    "name": name,
                    "value": value,
                    "domain": parsed_url.netloc,
                    "path": "/"
                })
            await page.context.add_cookies(cookies)

    async def _wait_for_page_load(self, page: Page):
        """等待页面加载完成"""
        try:
            # 等待网络空闲
            await page.wait_for_load_state("networkidle")
            
            # 如果配置了等待特定元素，则等待该元素出现
            if self.wait_for_element:
                await page.wait_for_selector(self.wait_for_element, timeout=self.load_timeout)
                
        except Exception as e:
            self.logger.warning(f"Page load wait timeout, continuing with current content: {e}")

    async def _execute_custom_actions(self, page: Page, request):
        """执行自定义操作"""
        # 从请求的 meta 中获取自定义操作
        custom_actions = request.meta.get("playwright_actions", [])
        
        for action in custom_actions:
            try:
                if isinstance(action, dict):
                    action_type = action.get("type")
                    action_params = action.get("params", {})
                    
                    if action_type == "click":
                        selector = action_params.get("selector")
                        if selector:
                            await page.click(selector)
                    elif action_type == "fill":
                        selector = action_params.get("selector")
                        value = action_params.get("value")
                        if selector and value is not None:
                            await page.fill(selector, value)
                    elif action_type == "wait":
                        timeout = action_params.get("timeout", 1000)
                        await page.wait_for_timeout(timeout)
                    elif action_type == "evaluate":
                        script = action_params.get("script")
                        if script:
                            await page.evaluate(script)
                    elif action_type == "scroll":
                        position = action_params.get("position", "bottom")
                        if position == "bottom":
                            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        elif position == "top":
                            await page.evaluate("window.scrollTo(0, 0)")
                            
            except Exception as e:
                self.logger.warning(f"Failed to execute custom action: {e}")

    async def _execute_pagination_actions(self, page: Page, request):
        """执行翻页操作"""
        # 从请求的 meta 中获取翻页操作
        pagination_actions = request.meta.get("pagination_actions", [])
        
        for action in pagination_actions:
            try:
                if isinstance(action, dict):
                    action_type = action.get("type")
                    action_params = action.get("params", {})
                    
                    if action_type == "scroll":
                        # 鼠标滑动翻页
                        scroll_count = action_params.get("count", 1)
                        scroll_delay = action_params.get("delay", 1000)
                        scroll_distance = action_params.get("distance", 500)
                        
                        for _ in range(scroll_count):
                            await page.mouse.wheel(0, scroll_distance)
                            await page.wait_for_timeout(scroll_delay)
                            
                    elif action_type == "click":
                        # 鼠标点击翻页
                        selector = action_params.get("selector")
                        click_count = action_params.get("count", 1)
                        click_delay = action_params.get("delay", 1000)
                        
                        if selector:
                            for _ in range(click_count):
                                await page.click(selector)
                                await page.wait_for_timeout(click_delay)
                                
                    elif action_type == "evaluate":
                        # 执行自定义脚本翻页
                        script = action_params.get("script")
                        if script:
                            await page.evaluate(script)
                            
            except Exception as e:
                self.logger.warning(f"Failed to execute pagination action: {e}")

    async def _get_cookies(self) -> Dict[str, str]:
        """获取 Cookies"""
        try:
            if self.context:
                playwright_cookies = await self.context.cookies()
                return {cookie['name']: cookie['value'] for cookie in playwright_cookies}
            return {}
        except Exception as e:
            self.logger.warning(f"Failed to get cookies: {e}")
            return {}

    async def close(self) -> None:
        """关闭 Playwright 资源"""
        try:
            # 关闭所有页面
            if self._page_pool:
                self.logger.debug(f"Closing {len(self._page_pool)} page(s)...")
                for page in self._page_pool:
                    try:
                        await page.close()
                    except Exception as e:
                        self.logger.warning(f"Error closing page: {e}")
                
                self._page_pool.clear()
                self._used_pages.clear()
            
            # 关闭上下文
            if self.context:
                try:
                    await self.context.close()
                except Exception as e:
                    self.logger.warning(f"Error closing context: {e}")
                finally:
                    self.context = None
            
            # 关闭浏览器
            if self.browser:
                try:
                    await self.browser.close()
                except Exception as e:
                    self.logger.warning(f"Error closing browser: {e}")
                finally:
                    self.browser = None
            
            # 停止 Playwright
            if self.playwright:
                try:
                    await self.playwright.stop()
                except Exception as e:
                    self.logger.warning(f"Error stopping playwright: {e}")
                finally:
                    self.playwright = None
                    
            self.logger.info("PlaywrightDownloader closed.")
        except Exception as e:
            self.logger.error(f"Error during Playwright cleanup: {e}", exc_info=True)
            # 确保资源被清空
            self.context = None
            self.browser = None
            self.playwright = None

    async def _get_page(self) -> Page:
        """获取页面实例（支持单浏览器多标签页模式）"""
        # 如果启用了单浏览器模式且页面池中有可用页面
        if self.single_browser_mode and self._page_pool:
            # 检查是否需要创建新页面
            if len(self._page_pool) < self.max_pages_per_browser:
                # 创建新页面
                if not self.context:
                    raise RuntimeError("Browser context not initialized")
                new_page = await self.context.new_page()
                self._page_pool.append(new_page)
                self._used_pages.add(id(new_page))
                return new_page
            
            # 尝试从池中获取未使用的页面
            for page in self._page_pool:
                if id(page) not in self._used_pages:
                    self._used_pages.add(id(page))
                    return page
        
        # 创建新页面
        if not self.context:
            raise RuntimeError("Browser context not initialized")
            
        page = await self.context.new_page()
        
        # 如果启用了单浏览器模式，将页面添加到池中
        if self.single_browser_mode:
            self._page_pool.append(page)
            self._used_pages.add(id(page))
            
            # 如果超过最大页面数，移除最早的页面
            if len(self._page_pool) > self.max_pages_per_browser:
                old_page = self._page_pool.pop(0)
                self._used_pages.discard(id(old_page))
                try:
                    await old_page.close()
                except:
                    pass
        
        return page

    async def _release_page(self, page: Page):
        """归还页面到池中"""
        if self.single_browser_mode:
            page_id = id(page)
            if page_id in self._used_pages:
                self._used_pages.discard(page_id)
                # 清空页面内容，准备下次使用
                try:
                    await page.goto("about:blank")
                except:
                    pass
        else:
            # 非单浏览器模式，直接关闭页面
            try:
                await page.close()
            except:
                pass
```

**code file end: crawlo/downloader/playwright_downloader.py**

---


### code file start: crawlo/downloader/selenium_downloader.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Selenium 下载器
==============
支持动态加载内容的下载器，基于 Selenium WebDriver 实现。

功能特性:
- 支持 Chrome/Firefox/Edge 等主流浏览器
- 智能等待页面加载完成
- 支持自定义浏览器选项和插件
- 内存安全的资源管理
- 自动处理 Cookie 和本地存储
- 支持翻页操作（鼠标滑动、点击翻页）
- 单浏览器多标签页模式
"""
import os
import time
import asyncio
from typing import Optional, Dict, List

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from crawlo.downloader import DownloaderBase
from crawlo.network.response import Response
from crawlo.logging import get_logger


class SeleniumDownloader(DownloaderBase):
    """
    基于 Selenium 的动态内容下载器
    支持处理 JavaScript 渲染的网页内容
    """

    def __init__(self, crawler):
        super().__init__(crawler)
        self.driver: Optional[webdriver.Chrome] = None
        self.logger = get_logger(self.__class__.__name__)
        self.default_timeout = crawler.settings.get_int("SELENIUM_TIMEOUT", 30)
        self.load_timeout = crawler.settings.get_int("SELENIUM_LOAD_TIMEOUT", 10)
        self.window_width = crawler.settings.get_int("SELENIUM_WINDOW_WIDTH", 1920)
        self.window_height = crawler.settings.get_int("SELENIUM_WINDOW_HEIGHT", 1080)
        self.browser_type = crawler.settings.get("SELENIUM_BROWSER_TYPE", "chrome").lower()
        self.headless = crawler.settings.get_bool("SELENIUM_HEADLESS", True)
        self.wait_for_element = crawler.settings.get("SELENIUM_WAIT_FOR_ELEMENT", None)
        
        # 单浏览器多标签页模式
        self.single_browser_mode = crawler.settings.get_bool("SELENIUM_SINGLE_BROWSER_MODE", True)
        self.max_tabs_per_browser = crawler.settings.get_int("SELENIUM_MAX_TABS_PER_BROWSER", 10)
        self._window_handles: List[str] = []
        self._current_handle_index = 0

    def open(self):
        super().open()
        self.logger.info("Opening SeleniumDownloader")

        try:
            if self.browser_type == "chrome":
                self.driver = self._create_chrome_driver()
            elif self.browser_type == "firefox":
                self.driver = self._create_firefox_driver()
            elif self.browser_type == "edge":
                self.driver = self._create_edge_driver()
            else:
                raise ValueError(f"Unsupported browser type: {self.browser_type}")

            # 设置窗口大小
            self.driver.set_window_size(self.window_width, self.window_height)
            self.logger.debug(f"SeleniumDownloader initialized with {self.browser_type}")

        except Exception as e:
            self.logger.error(f"Failed to initialize SeleniumDownloader: {e}")
            raise

    def _create_chrome_driver(self):
        """创建 Chrome WebDriver"""
        options = ChromeOptions()
        
        if self.headless:
            options.add_argument("--headless")
        
        # 基本配置
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-images")
        options.add_argument("--disable-javascript") if not self.crawler.settings.get_bool("SELENIUM_ENABLE_JS", True) else None
        
        # 用户代理
        user_agent = self.crawler.settings.get("USER_AGENT")
        if user_agent:
            options.add_argument(f"--user-agent={user_agent}")
            
        # 代理设置
        proxy = self.crawler.settings.get("SELENIUM_PROXY")
        if proxy:
            # 处理带认证的代理
            if isinstance(proxy, str) and "@" in proxy and "://" in proxy:
                # 解析带认证的代理URL
                from urllib.parse import urlparse
                parsed = urlparse(proxy)
                if parsed.username and parsed.password:
                    # 对于带认证的代理，需要特殊处理
                    # 这里我们使用一个扩展来处理认证
                    # 创建一个临时的代理配置文件
                    import tempfile
                    import json
                    
                    proxy_config = {
                        "mode": "fixed_servers",
                        "rules": {
                            "proxyForHttp": {
                                "scheme": parsed.scheme,
                                "host": parsed.hostname,
                                "port": parsed.port or (80 if parsed.scheme == "http" else 443)
                            },
                            "proxyForHttps": {
                                "scheme": parsed.scheme,
                                "host": parsed.hostname,
                                "port": parsed.port or (80 if parsed.scheme == "http" else 443)
                            },
                            "bypassList": []
                        }
                    }
                    
                    # 创建临时目录和文件
                    temp_dir = tempfile.mkdtemp()
                    proxy_file = os.path.join(temp_dir, "proxy.json")
                    with open(proxy_file, 'w') as f:
                        json.dump(proxy_config, f)
                    
                    # 设置代理配置文件
                    options.add_argument(f"--proxy-server={parsed.scheme}://{parsed.hostname}:{parsed.port or (80 if parsed.scheme == 'http' else 443)}")
                    
                    # 设置认证信息（需要通过其他方式处理）
                    # 这里我们简单地清理URL中的认证信息
                    clean_proxy = f"{parsed.scheme}://{parsed.hostname}:{parsed.port or (80 if parsed.scheme == 'http' else 443)}"
                    options.add_argument(f"--proxy-server={clean_proxy}")
                else:
                    options.add_argument(f"--proxy-server={proxy}")
            else:
                options.add_argument(f"--proxy-server={proxy}")
            
        # 创建驱动
        return webdriver.Chrome(options=options)

    def _create_firefox_driver(self):
        """创建 Firefox WebDriver"""
        options = FirefoxOptions()
        
        if self.headless:
            options.add_argument("--headless")
            
        # 基本配置
        options.set_preference("network.http.use-cache", False)
        options.set_preference("browser.cache.disk.enable", False)
        options.set_preference("browser.cache.memory.enable", False)
        
        # 用户代理
        user_agent = self.crawler.settings.get("USER_AGENT")
        if user_agent:
            options.set_preference("general.useragent.override", user_agent)
            
        # 代理设置
        proxy = self.crawler.settings.get("SELENIUM_PROXY")
        if proxy:
            # 处理带认证的代理
            if isinstance(proxy, str) and "@" in proxy and "://" in proxy:
                # 解析带认证的代理URL
                from urllib.parse import urlparse
                parsed = urlparse(proxy)
                if parsed.username and parsed.password:
                    # 设置代理服务器
                    options.set_preference("network.proxy.type", 1)  # 手动配置
                    options.set_preference("network.proxy.http", parsed.hostname)
                    options.set_preference("network.proxy.http_port", parsed.port or 80)
                    options.set_preference("network.proxy.ssl", parsed.hostname)
                    options.set_preference("network.proxy.ssl_port", parsed.port or 443)
                    options.set_preference("network.proxy.ftp", parsed.hostname)
                    options.set_preference("network.proxy.ftp_port", parsed.port or 21)
                    options.set_preference("network.proxy.socks", parsed.hostname)
                    options.set_preference("network.proxy.socks_port", parsed.port or 1080)
                    
                    # 认证信息需要通过其他方式处理（例如使用扩展）
                    # 这里我们简单地清理URL中的认证信息
                    clean_proxy = f"{parsed.scheme}://{parsed.hostname}:{parsed.port or (80 if parsed.scheme == 'http' else 443)}"
                else:
                    options.add_argument(f"--proxy-server={proxy}")
            else:
                # 简单的代理配置
                options.set_preference("network.proxy.type", 1)
                # 这里需要根据代理URL的具体格式来解析
                from urllib.parse import urlparse
                parsed = urlparse(proxy)
                if parsed.scheme in ["http", "https"]:
                    options.set_preference("network.proxy.http", parsed.hostname)
                    options.set_preference("network.proxy.http_port", parsed.port or 80)
                    options.set_preference("network.proxy.ssl", parsed.hostname)
                    options.set_preference("network.proxy.ssl_port", parsed.port or 443)
                elif parsed.scheme == "socks5":
                    options.set_preference("network.proxy.socks", parsed.hostname)
                    options.set_preference("network.proxy.socks_port", parsed.port or 1080)
                    options.set_preference("network.proxy.socks_version", 5)
                elif parsed.scheme == "socks4":
                    options.set_preference("network.proxy.socks", parsed.hostname)
                    options.set_preference("network.proxy.socks_port", parsed.port or 1080)
                    options.set_preference("network.proxy.socks_version", 4)
            
        return webdriver.Firefox(options=options)

    def _create_edge_driver(self):
        """创建 Edge WebDriver"""
        options = EdgeOptions()
        
        if self.headless:
            options.add_argument("--headless")
            
        # 基本配置
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        # 用户代理
        user_agent = self.crawler.settings.get("USER_AGENT")
        if user_agent:
            options.add_argument(f"--user-agent={user_agent}")
            
        # 代理设置
        proxy = self.crawler.settings.get("SELENIUM_PROXY")
        if proxy:
            # 处理带认证的代理
            if isinstance(proxy, str) and "@" in proxy and "://" in proxy:
                # 解析带认证的代理URL
                from urllib.parse import urlparse
                parsed = urlparse(proxy)
                if parsed.username and parsed.password:
                    # 清理URL中的认证信息
                    clean_proxy = f"{parsed.scheme}://{parsed.hostname}:{parsed.port or (80 if parsed.scheme == 'http' else 443)}"
                    options.add_argument(f"--proxy-server={clean_proxy}")
                else:
                    options.add_argument(f"--proxy-server={proxy}")
            else:
                options.add_argument(f"--proxy-server={proxy}")
            
        return webdriver.Edge(options=options)

    async def download(self, request) -> Optional[Response]:
        """下载动态内容"""
        if not self.driver:
            raise RuntimeError("SeleniumDownloader driver is not available")

        start_time = None
        if self.crawler.settings.get_bool("DOWNLOAD_STATS", True):
            start_time = time.time()

        try:
            # 切换到合适的标签页或创建新标签页
            await self._switch_or_create_tab()
            
            # 访问页面
            self.driver.get(request.url)
            
            # 等待页面加载完成
            await self._wait_for_page_load()
            
            # 执行自定义脚本（如果有）
            await self._execute_custom_scripts(request)
            
            # 执行翻页操作（如果有）
            await self._execute_pagination_actions(request)
            
            # 获取页面内容
            page_source = self.driver.page_source
            page_url = self.driver.current_url
            
            # 获取响应头信息（Selenium 无法直接获取，需要模拟）
            headers = self._get_response_headers()
            
            # 获取状态码（Selenium 无法直接获取，需要通过执行脚本）
            status_code = await self._get_status_code()
            
            # 获取 Cookies
            cookies = self._get_cookies()
            
            # 构造响应对象
            response = Response(
                url=page_url,
                headers=headers,
                status_code=status_code,
                body=page_source.encode('utf-8'),
                request=request
            )
            
            # 添加 Cookies 到响应
            response.cookies = cookies
            
            # 记录下载统计
            if start_time:
                download_time = time.time() - start_time
                self.logger.debug(f"Downloaded {request.url} in {download_time:.3f}s")
                
            return response

        except TimeoutException as e:
            self.logger.error(f"Timeout error for {request.url}: {e}")
            raise
        except WebDriverException as e:
            self.logger.error(f"WebDriver error for {request.url}: {e}")
            raise
        except Exception as e:
            self.logger.critical(f"Unexpected error for {request.url}: {e}", exc_info=True)
            raise

    async def _switch_or_create_tab(self):
        """切换到合适的标签页或创建新标签页"""
        if not self.single_browser_mode:
            return
            
        # 如果还没有窗口句柄，保存当前窗口
        if not self._window_handles:
            self._window_handles.append(self.driver.current_window_handle)
            return
            
        # 检查是否需要创建新标签页
        if len(self._window_handles) < self.max_tabs_per_browser:
            # 创建新标签页
            self.driver.execute_script("window.open('');")
            # 切换到新标签页
            self.driver.switch_to.window(self.driver.window_handles[-1])
            # 保存新标签页句柄
            self._window_handles.append(self.driver.current_window_handle)
            return
            
        # 循环使用现有的标签页
        self._current_handle_index = (self._current_handle_index + 1) % len(self._window_handles)
        self.driver.switch_to.window(self._window_handles[self._current_handle_index])
        
        # 清空当前页面内容
        self.driver.execute_script("document.body.innerHTML = '';")

    async def _wait_for_page_load(self):
        """等待页面加载完成"""
        try:
            # 等待 document.readyState 为 complete
            WebDriverWait(self.driver, self.load_timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            
            # 如果配置了等待特定元素，则等待该元素出现
            if self.wait_for_element:
                WebDriverWait(self.driver, self.load_timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.wait_for_element))
                )
                
        except TimeoutException:
            self.logger.warning("Page load timeout, continuing with current content")

    async def _execute_custom_scripts(self, request):
        """执行自定义脚本"""
        # 从请求的 meta 中获取自定义脚本
        custom_scripts = request.meta.get("selenium_scripts", [])
        
        for script in custom_scripts:
            try:
                if isinstance(script, str):
                    self.driver.execute_script(script)
                elif isinstance(script, dict):
                    script_type = script.get("type", "js")
                    script_content = script.get("content", "")
                    
                    if script_type == "js":
                        self.driver.execute_script(script_content)
                    elif script_type == "wait":
                        # 等待特定时间
                        await asyncio.sleep(script_content)
                        
            except Exception as e:
                self.logger.warning(f"Failed to execute custom script: {e}")

    async def _execute_pagination_actions(self, request):
        """执行翻页操作"""
        # 从请求的 meta 中获取翻页操作
        pagination_actions = request.meta.get("pagination_actions", [])
        
        for action in pagination_actions:
            try:
                if isinstance(action, dict):
                    action_type = action.get("type")
                    action_params = action.get("params", {})
                    
                    if action_type == "scroll":
                        # 鼠标滑动翻页
                        scroll_count = action_params.get("count", 1)
                        scroll_delay = action_params.get("delay", 1)
                        scroll_distance = action_params.get("distance", 500)
                        
                        action_chains = ActionChains(self.driver)
                        for _ in range(scroll_count):
                            action_chains.scroll_by_amount(0, scroll_distance).perform()
                            time.sleep(scroll_delay)
                            
                    elif action_type == "click":
                        # 鼠标点击翻页
                        selector = action_params.get("selector")
                        click_count = action_params.get("count", 1)
                        click_delay = action_params.get("delay", 1)
                        
                        if selector:
                            element = WebDriverWait(self.driver, self.load_timeout).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                            )
                            for _ in range(click_count):
                                element.click()
                                time.sleep(click_delay)
                                
                    elif action_type == "evaluate":
                        # 执行自定义脚本翻页
                        script = action_params.get("script")
                        if script:
                            self.driver.execute_script(script)
                            
            except Exception as e:
                self.logger.warning(f"Failed to execute pagination action: {e}")

    def _get_response_headers(self) -> Dict[str, str]:
        """获取响应头信息"""
        # Selenium 无法直接获取响应头，这里返回一些基本的模拟信息
        return {
            "Content-Type": "text/html; charset=utf-8",
            "Server": "Selenium WebDriver"
        }

    async def _get_status_code(self) -> int:
        """获取状态码"""
        try:
            # 通过执行脚本获取状态码
            status_code = self.driver.execute_script(
                "return window.performance.getEntriesByType('navigation')[0].responseStart > 0 ? 200 : 404;"
            )
            return status_code if isinstance(status_code, int) else 200
        except Exception:
            return 200  # 默认成功

    def _get_cookies(self) -> Dict[str, str]:
        """获取 Cookies"""
        try:
            selenium_cookies = self.driver.get_cookies()
            return {cookie['name']: cookie['value'] for cookie in selenium_cookies}
        except Exception as e:
            self.logger.warning(f"Failed to get cookies: {e}")
            return {}

    async def close(self) -> None:
        """关闭浏览器资源"""
        if self.driver:
            self.logger.info("Closing SeleniumDownloader driver...")
            try:
                # 关闭所有标签页
                if self._window_handles:
                    self.logger.debug(f"Closing {len(self._window_handles)} tab(s)...")
                    for handle in self._window_handles[1:]:  # 保留第一个，其他关闭
                        try:
                            self.driver.switch_to.window(handle)
                            self.driver.close()
                        except Exception as e:
                            self.logger.warning(f"Error closing tab {handle}: {e}")
                    
                    self._window_handles.clear()
                
                # 退出浏览器
                self.driver.quit()
            except Exception as e:
                self.logger.warning(f"Error closing Selenium driver: {e}")
            finally:
                self.driver = None
        
        self.logger.debug("SeleniumDownloader closed.")
```

**code file end: crawlo/downloader/selenium_downloader.py**

---


### code file start: crawlo/downloader/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Crawlo Downloader Module
========================
提供多种高性能异步下载器实现。

下载器类型:
- AioHttpDownloader: 基于aiohttp的高性能下载器
- CurlCffiDownloader: 支持浏览器指纹模拟的curl-cffi下载器  
- HttpXDownloader: 支持HTTP/2的httpx下载器

核心类:
- DownloaderBase: 下载器基类
- ActivateRequestManager: 活跃请求管理器
"""
from abc import abstractmethod, ABCMeta
from typing import Final, Set, Optional, TYPE_CHECKING
from contextlib import asynccontextmanager

from crawlo.logging import get_logger
from crawlo.middleware.middleware_manager import MiddlewareManager

if TYPE_CHECKING:
    from crawlo import Response


class ActivateRequestManager:
    """活跃请求管理器 - 跟踪和管理正在处理的请求"""

    def __init__(self):
        self._active: Final[Set] = set()
        self._total_requests: int = 0
        self._completed_requests: int = 0
        self._failed_requests: int = 0

    def add(self, request):
        """添加活跃请求"""
        self._active.add(request)
        self._total_requests += 1
        return request

    def remove(self, request, success: bool = True):
        """移除活跃请求并更新统计"""
        self._active.discard(request)  # 使用discard避免KeyError
        if success:
            self._completed_requests += 1
        else:
            self._failed_requests += 1

    @asynccontextmanager
    async def __call__(self, request):
        """上下文管理器用法"""
        self.add(request)
        success = False
        try:
            yield request
            success = True
        except Exception:
            success = False
            raise
        finally:
            self.remove(request, success)

    def __len__(self):
        """返回当前活跃请求数"""
        return len(self._active)
    
    def get_stats(self) -> dict:
        """获取请求统计信息"""
        completed = self._completed_requests + self._failed_requests
        return {
            'active_requests': len(self._active),
            'total_requests': self._total_requests,
            'completed_requests': self._completed_requests,
            'failed_requests': self._failed_requests,
            'success_rate': (
                self._completed_requests / completed * 100 
                if completed > 0 else 100.0  # 无完成请求时返回100%
            )
        }
    
    def reset_stats(self):
        """重置统计信息"""
        self._total_requests = 0
        self._completed_requests = 0
        self._failed_requests = 0
        # 注意：不清空 _active，因为可能有正在进行的请求


class DownloaderMeta(ABCMeta):
    def __subclasscheck__(self, subclass):
        required_methods = ('fetch', 'download', 'create_instance', 'close')
        is_subclass = all(
            hasattr(subclass, method) and callable(getattr(subclass, method, None)) for method in required_methods
        )
        return is_subclass


class DownloaderBase(metaclass=DownloaderMeta):
    """
    下载器基类 - 提供通用的下载器功能和接口
    
    所有下载器实现都应该继承此基类。
    """
    
    def __init__(self, crawler):
        self.crawler = crawler
        self._active = ActivateRequestManager()
        self.middleware: Optional[MiddlewareManager] = None
        self.logger = get_logger(self.__class__.__name__)
        self._closed = False
        self._stats_enabled = crawler.settings.get_bool("DOWNLOADER_STATS", True)

    @classmethod
    def create_instance(cls, *args, **kwargs):
        """创建下载器实例"""
        return cls(*args, **kwargs)

    def open(self) -> None:
        """初始化下载器"""
        if self._closed:
            raise RuntimeError(f"{self.__class__.__name__} 已关闭，无法重新打开")
            
        # 获取下载器类的完整路径
        downloader_class = f"{type(self).__module__}.{type(self).__name__}"
        
        # 输出启用的下载器信息（类似MiddlewareManager的格式）
        self.logger.info(f"enabled downloader: \n  {downloader_class}")
        
        # 输出下载器配置摘要
        self.logger.debug(
            f"{self.crawler.spider} <下载器类：{downloader_class}> "
            f"<并发数：{self.crawler.settings.get_int('CONCURRENCY')}>"
        )
        
        try:
            self.middleware = MiddlewareManager.create_instance(self.crawler)
            self.logger.debug(f"{self.__class__.__name__} 中间件初始化完成")
        except Exception as e:
            self.logger.error(f"中间件初始化失败: {e}")
            raise

    async def fetch(self, request) -> 'Optional[Response]':
        """获取请求响应（经过中间件处理）"""
        if self._closed:
            raise RuntimeError(f"{self.__class__.__name__} 已关闭")
            
        if not self.middleware:
            raise RuntimeError("中间件未初始化")
            
        async with self._active(request):
            try:
                response = await self.middleware.download(request)
                return response
            except Exception as e:
                self.logger.error(f"下载请求 {request.url} 失败: {e}")
                raise

    @abstractmethod
    async def download(self, request) -> 'Response':
        """子类必须实现的下载方法"""
        pass

    async def close(self) -> None:
        """关闭下载器并清理资源"""
        if not self._closed:
            self._closed = True
            if self._stats_enabled:
                stats = self.get_stats()
                self.logger.info(f"{self.__class__.__name__} 统计: {stats}")
            self.logger.debug(f"{self.__class__.__name__} 已关闭")

    def idle(self) -> bool:
        """检查是否空闲（无活跃请求）"""
        return len(self._active) == 0

    def __len__(self) -> int:
        """返回活跃请求数"""
        return len(self._active)
    
    def get_stats(self) -> dict:
        """获取下载器统计信息"""
        base_stats = {
            'downloader_class': self.__class__.__name__,
            'is_idle': self.idle(),
            'is_closed': self._closed
        }
        
        if self._stats_enabled:
            base_stats.update(self._active.get_stats())
            
        return base_stats
    
    def reset_stats(self):
        """重置统计信息"""
        if self._stats_enabled:
            self._active.reset_stats()
    
    def health_check(self) -> dict:
        """健康检查"""
        return {
            'status': 'healthy' if not self._closed and self.middleware else 'unhealthy',
            'active_requests': len(self._active),
            'middleware_ready': self.middleware is not None,
            'closed': self._closed
        }


# 导入具体的下载器实现
try:
    from .aiohttp_downloader import AioHttpDownloader
except ImportError:
    AioHttpDownloader = None

try:
    from .cffi_downloader import CurlCffiDownloader
except ImportError:
    CurlCffiDownloader = None

try:
    from .httpx_downloader import HttpXDownloader
except ImportError:
    HttpXDownloader = None

try:
    from .selenium_downloader import SeleniumDownloader
except ImportError:
    SeleniumDownloader = None

try:
    from .playwright_downloader import PlaywrightDownloader
except ImportError:
    PlaywrightDownloader = None

try:
    from .hybrid_downloader import HybridDownloader
except ImportError:
    HybridDownloader = None

# 导出所有可用的类
__all__ = [
    'DownloaderBase',
    'DownloaderMeta', 
    'ActivateRequestManager',
]

# 添加可用的下载器
if AioHttpDownloader:
    __all__.append('AioHttpDownloader')
if CurlCffiDownloader:
    __all__.append('CurlCffiDownloader')
if HttpXDownloader:
    __all__.append('HttpXDownloader')
if SeleniumDownloader:
    __all__.append('SeleniumDownloader')
if PlaywrightDownloader:
    __all__.append('PlaywrightDownloader')
if HybridDownloader:
    __all__.append('HybridDownloader')

# 提供便捷的下载器映射
DOWNLOADER_MAP = {
    'aiohttp': AioHttpDownloader,
    'httpx': HttpXDownloader, 
    'curl_cffi': CurlCffiDownloader,
    'cffi': CurlCffiDownloader,  # 别名
    'selenium': SeleniumDownloader,
    'playwright': PlaywrightDownloader,
    'hybrid': HybridDownloader,
}

# 过滤掉不可用的下载器
DOWNLOADER_MAP = {k: v for k, v in DOWNLOADER_MAP.items() if v is not None}

def get_downloader_class(name: str):
    """根据名称获取下载器类"""
    if name in DOWNLOADER_MAP:
        return DOWNLOADER_MAP[name]
    raise ValueError(f"未知的下载器类型: {name}。可用类型: {list(DOWNLOADER_MAP.keys())}")

```

**code file end: crawlo/downloader/__init__.py**

---


### code file start: crawlo/extension/health_check.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import asyncio
from datetime import datetime
from typing import Any, Optional, Dict

from crawlo.event import CrawlerEvent
from crawlo.logging import get_logger


class HealthCheckExtension:
    """
    健康检查扩展
    监控爬虫的健康状态，包括响应时间、错误率等指标
    """

    def __init__(self, crawler: Any):
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        # 获取配置参数
        self.enabled = self.settings.get_bool('HEALTH_CHECK_ENABLED', True)
        self.check_interval = self.settings.get_int('HEALTH_CHECK_INTERVAL', 60)  # 默认60秒
        
        # 健康状态统计
        self.stats: Dict[str, Any] = {
            'start_time': None,
            'total_requests': 0,
            'total_responses': 0,
            'error_responses': 0,
            'last_check_time': None,
            'response_times': [],  # 存储最近的响应时间
        }
        
        self.task: Optional[asyncio.Task] = None

    @classmethod
    def create_instance(cls, crawler: Any) -> 'HealthCheckExtension':
        # 只有当配置启用时才创建实例
        if not crawler.settings.get_bool('HEALTH_CHECK_ENABLED', True):
            from crawlo.exceptions import NotConfigured
            raise NotConfigured("HealthCheckExtension: HEALTH_CHECK_ENABLED is False")
        
        o = cls(crawler)
        if o.enabled:
            crawler.subscriber.subscribe(o.spider_opened, event=CrawlerEvent.SPIDER_OPENED)
            crawler.subscriber.subscribe(o.spider_closed, event=CrawlerEvent.SPIDER_CLOSED)
            crawler.subscriber.subscribe(o.response_received, event=CrawlerEvent.RESPONSE_RECEIVED)
            crawler.subscriber.subscribe(o.request_scheduled, event=CrawlerEvent.REQUEST_SCHEDULED)
        return o

    async def spider_opened(self) -> None:
        """爬虫启动时初始化健康检查"""
        if not self.enabled:
            return
            
        self.stats['start_time'] = datetime.now()
        self.task = asyncio.create_task(self._health_check_loop())
        self.logger.info("Health check extension started.")

    async def spider_closed(self) -> None:
        """爬虫关闭时停止健康检查"""
        if not self.enabled:
            return
            
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        
        # 输出最终健康状态
        await self._check_health()
        self.logger.info("Health check extension stopped.")

    async def request_scheduled(self, request: Any, spider: Any) -> None:
        """记录调度的请求"""
        if not self.enabled:
            return
        self.stats['total_requests'] += 1

    async def response_received(self, response: Any, spider: Any) -> None:
        """记录接收到的响应"""
        if not self.enabled:
            return
            
        self.stats['total_responses'] += 1
        
        # 记录错误响应
        if hasattr(response, 'status_code') and response.status_code >= 400:
            self.stats['error_responses'] += 1

    async def _health_check_loop(self) -> None:
        """健康检查循环"""
        while True:
            try:
                await asyncio.sleep(self.check_interval)
                await self._check_health()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Error in health check loop: {e}")

    async def _check_health(self) -> None:
        """执行健康检查并输出报告"""
        try:
            now_time = datetime.now()
            self.stats['last_check_time'] = now_time
            
            # 计算基本统计信息
            runtime = (now_time - self.stats['start_time']).total_seconds() if self.stats['start_time'] else 0
            requests_per_second = self.stats['total_requests'] / runtime if runtime > 0 else 0
            responses_per_second = self.stats['total_responses'] / runtime if runtime > 0 else 0
            
            # 计算错误率
            error_rate = (
                self.stats['error_responses'] / self.stats['total_responses'] 
                if self.stats['total_responses'] > 0 else 0
            )
            
            # 输出健康报告
            health_report = {
                'runtime_seconds': round(runtime, 2),
                'total_requests': self.stats['total_requests'],
                'total_responses': self.stats['total_responses'],
                'requests_per_second': round(requests_per_second, 2),
                'responses_per_second': round(responses_per_second, 2),
                'error_responses': self.stats['error_responses'],
                'error_rate': f"{error_rate:.2%}",
            }
            
            # 根据错误率判断健康状态
            if error_rate > 0.1:  # 错误率超过10%
                self.logger.warning(f"Health check report: {health_report}")
            elif error_rate > 0.05:  # 错误率超过5%
                self.logger.info(f"Health check report: {health_report}")
            else:
                self.logger.debug(f"Health check report: {health_report}")
                
        except Exception as e:
            self.logger.error(f"Error in health check: {e}")
```

**code file end: crawlo/extension/health_check.py**

---


### code file start: crawlo/extension/logging_extension.py 

```python
from typing import Any
from crawlo.exceptions import NotConfigured
from crawlo.logging import get_logger

# 获取logger实例
_logger = get_logger(__name__)


class CustomLoggerExtension:
    """
    日志系统初始化扩展
    遵循与 ExtensionManager 一致的接口规范：使用 create_instance
    """

    def __init__(self, settings: Any):
        self.settings = settings
        # 使用新的日志系统，但要简化配置传递
        try:
            from crawlo.logging import configure_logging
            # 直接传递settings对象，让日志系统内部处理
            configure_logging(settings)
        except Exception as e:
            # 如果日志系统配置失败，不应该阻止扩展加载
            # 使用基本日志输出错误信息
            import logging
            logging.getLogger(__name__).warning(f"Failed to configure logging system: {e}")
            # 不抛出异常，让扩展继续加载

    @classmethod
    def create_instance(cls, crawler: Any, *args: Any, **kwargs: Any) -> 'CustomLoggerExtension':
        """
        工厂方法：兼容 ExtensionManager 的创建方式
        被 ExtensionManager 调用
        """
        # 可以通过 settings 控制是否启用
        log_file = crawler.settings.get('LOG_FILE')
        log_enable_custom = crawler.settings.get('LOG_ENABLE_CUSTOM', False)
        
        # 只有当没有配置日志文件且未启用自定义日志时才禁用
        if not log_file and not log_enable_custom:
            raise NotConfigured("CustomLoggerExtension: LOG_FILE not set and LOG_ENABLE_CUSTOM=False")

        return cls(crawler.settings)

    def spider_opened(self, spider: Any) -> None:
        try:
            _logger.info(
                f"CustomLoggerExtension: Logging initialized. "
                f"LOG_FILE={self.settings.get('LOG_FILE')}, "
                f"LOG_LEVEL={self.settings.get('LOG_LEVEL')}"
            )
        except Exception as e:
            # 即使日志初始化信息无法打印，也不应该影响程序运行
            pass
```

**code file end: crawlo/extension/logging_extension.py**

---


### code file start: crawlo/extension/log_interval.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import asyncio
from typing import Any, Optional

from crawlo.logging import get_logger
from crawlo.event import CrawlerEvent


class LogIntervalExtension:

    def __init__(self, crawler: Any):
        self.task: Optional[asyncio.Task] = None
        self.stats = crawler.stats
        self.item_count = 0
        self.response_count = 0
        self.seconds = crawler.settings.get('INTERVAL', 60)  # 默认60秒
        
        # 修复时间单位计算逻辑
        if self.seconds % 60 == 0:
            self.interval = int(self.seconds / 60)
            self.unit = 'min'
        else:
            self.interval = self.seconds
            self.unit = 's'
        
        # 处理单数情况
        if self.interval == 1 and self.unit == 'min':
            self.interval_display = ""
        else:
            self.interval_display = str(self.interval)

        self.logger = get_logger(self.__class__.__name__)
        self.logger.info(f"LogIntervalExtension initialized with interval: {self.seconds} seconds")

    @classmethod
    def create_instance(cls, crawler: Any) -> 'LogIntervalExtension':
        o = cls(crawler)
        crawler.subscriber.subscribe(o.spider_opened, event=CrawlerEvent.SPIDER_OPENED)
        crawler.subscriber.subscribe(o.spider_closed, event=CrawlerEvent.SPIDER_CLOSED)
        return o

    async def spider_opened(self) -> None:
        self.logger.info("Spider opened, starting interval logging task")
        self.task = asyncio.create_task(self.interval_log())
        self.logger.info("Interval logging task started")

    async def spider_closed(self) -> None:
        self.logger.info("Spider closed, stopping interval logging task")
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
            self.task = None

    async def interval_log(self) -> None:
        iteration = 0
        while True:
            try:
                iteration += 1
                self.logger.debug(f"Interval log iteration {iteration} starting")
                last_item_count = self.stats.get_value('item_successful_count', default=0)
                last_response_count = self.stats.get_value('response_received_count', default=0)
                item_rate = last_item_count - self.item_count
                response_rate = last_response_count - self.response_count
                
                # 添加调试信息
                self.logger.debug(f"Debug info - Iteration: {iteration}, Last item count: {last_item_count}, Last response count: {last_response_count}")
                self.logger.debug(f"Debug info - Previous item count: {self.item_count}, Previous response count: {self.response_count}")
                self.logger.debug(f"Debug info - Item rate: {item_rate}, Response rate: {response_rate}")
                
                self.item_count, self.response_count = last_item_count, last_response_count
                
                # 修复效率计算，确保使用正确的单位
                if self.unit == 'min' and self.seconds > 0:
                    # 转换为每分钟速率
                    pages_per_min = response_rate * 60 / self.seconds if self.seconds > 0 else 0
                    items_per_min = item_rate * 60 / self.seconds if self.seconds > 0 else 0
                    self.logger.info(
                        f'Crawled {last_response_count} pages (at {pages_per_min:.0f} pages/min),'
                        f' Got {last_item_count} items (at {items_per_min:.0f} items/min).'
                    )
                else:
                    # 使用原始单位
                    self.logger.info(
                        f'Crawled {last_response_count} pages (at {response_rate} pages/{self.interval_display}{self.unit}),'
                        f' Got {last_item_count} items (at {item_rate} items/{self.interval_display}{self.unit}).'
                    )
                self.logger.debug(f"Interval log iteration {iteration} completed, sleeping for {self.seconds} seconds")
                await asyncio.sleep(self.seconds)
            except Exception as e:
                self.logger.error(f"Error in interval logging: {e}")
                await asyncio.sleep(self.seconds)  # 即使出错也继续执行
```

**code file end: crawlo/extension/log_interval.py**

---


### code file start: crawlo/extension/log_stats.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
日志统计扩展
提供详细的爬虫运行统计信息
"""
import asyncio
from typing import Any

from crawlo.logging import get_logger
from crawlo.utils import now, time_diff


class LogStats:
    """
    日志统计扩展，记录和输出爬虫运行过程中的各种统计信息
    """

    def __init__(self, crawler):
        self.crawler = crawler
        self.logger = get_logger(self.__class__.__name__)
        self._stats = crawler.stats
        self._stats['start_time'] = now(fmt='%Y-%m-%d %H:%M:%S')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    @classmethod
    def create_instance(cls, crawler):
        return cls.from_crawler(crawler)

    async def spider_closed(self, reason: str = 'finished') -> None:
        try:
            self._stats['end_time'] = now(fmt='%Y-%m-%d %H:%M:%S')
            self._stats['cost_time(s)'] = time_diff(start=self._stats['start_time'], end=self._stats['end_time'])
            self._stats['reason'] = reason
        except Exception as e:
            # 添加日志以便调试
            self.logger.error(f"Error in spider_closed: {e}")
            # 静默处理，避免影响爬虫运行
            pass

    async def item_successful(self, _item: Any, _spider: Any) -> None:
        try:
            self._stats.inc_value('item_successful_count')
        except Exception as e:
            # 静默处理，避免影响爬虫运行
            pass

    async def item_discard(self, _item: Any, exc: Any, _spider: Any) -> None:
        try:
            # 只增加总的丢弃计数，不记录每个丢弃项目的原因详情
            self._stats.inc_value('item_discard_count')
        except Exception as e:
            # 静默处理，避免影响爬虫运行
            pass

    async def response_received(self, _response: Any, _spider: Any) -> None:
        try:
            self._stats.inc_value('response_received_count')
        except Exception as e:
            # 静默处理，避免影响爬虫运行
            pass

    async def request_scheduled(self, _request: Any, _spider: Any) -> None:
        try:
            self._stats.inc_value('request_scheduler_count')
        except Exception as e:
            # 静默处理，避免影响爬虫运行
            pass
```

**code file end: crawlo/extension/log_stats.py**

---


### code file start: crawlo/extension/memory_monitor.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import asyncio
import psutil
from typing import Any, Optional

from crawlo.logging import get_logger
from crawlo.utils.error_handler import ErrorHandler
from crawlo.event import CrawlerEvent


class MemoryMonitorExtension:
    """
    内存监控扩展
    定期监控爬虫进程的内存使用情况，并在超出阈值时发出警告
    """

    def __init__(self, crawler: Any):
        self.task: Optional[asyncio.Task] = None
        self.process = psutil.Process()
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        self.error_handler = ErrorHandler(self.__class__.__name__, crawler.settings.get('LOG_LEVEL'))
        
        # 获取配置参数
        self.interval = self.settings.get_int('MEMORY_MONITOR_INTERVAL', 60)  # 默认60秒检查一次
        self.warning_threshold = self.settings.get_float('MEMORY_WARNING_THRESHOLD', 80.0)  # 默认80%警告阈值
        self.critical_threshold = self.settings.get_float('MEMORY_CRITICAL_THRESHOLD', 90.0)  # 默认90%严重阈值

    @classmethod
    def create_instance(cls, crawler: Any) -> 'MemoryMonitorExtension':
        # 只有当配置启用时才创建实例
        if not crawler.settings.get_bool('MEMORY_MONITOR_ENABLED', False):
            from crawlo.exceptions import NotConfigured
            raise NotConfigured("MemoryMonitorExtension: MEMORY_MONITOR_ENABLED is False")
        
        o = cls(crawler)
        crawler.subscriber.subscribe(o.spider_opened, event=CrawlerEvent.SPIDER_OPENED)
        crawler.subscriber.subscribe(o.spider_closed, event=CrawlerEvent.SPIDER_CLOSED)
        return o

    async def spider_opened(self) -> None:
        """爬虫启动时开始监控"""
        try:
            self.task = asyncio.create_task(self._monitor_loop())
            self.logger.info(
                f"Memory monitor started. Interval: {self.interval}s, "
                f"Warning threshold: {self.warning_threshold}%, Critical threshold: {self.critical_threshold}%"
            )
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="启动内存监控失败", 
                raise_error=False
            )

    async def spider_closed(self) -> None:
        """爬虫关闭时停止监控"""
        try:
            if self.task:
                self.task.cancel()
                try:
                    await self.task
                except asyncio.CancelledError:
                    pass
                self.task = None
                self.logger.info("Memory monitor stopped.")
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="停止内存监控失败", 
                raise_error=False
            )

    async def _monitor_loop(self) -> None:
        """内存监控循环"""
        while True:
            try:
                # 获取内存使用信息
                memory_info = self.process.memory_info()
                memory_percent = self.process.memory_percent()
                
                # 记录内存使用情况
                self.logger.debug(
                    f"Memory usage: {memory_percent:.2f}% "
                    f"(RSS: {memory_info.rss / 1024 / 1024:.2f} MB, "
                    f"VMS: {memory_info.vms / 1024 / 1024:.2f} MB)"
                )
                
                # 检查是否超过阈值
                if memory_percent >= self.critical_threshold:
                    self.logger.critical(
                        f"Memory usage critical: {memory_percent:.2f}% "
                        f"(RSS: {memory_info.rss / 1024 / 1024:.2f} MB)"
                    )
                elif memory_percent >= self.warning_threshold:
                    self.logger.warning(
                        f"Memory usage high: {memory_percent:.2f}% "
                        f"(RSS: {memory_info.rss / 1024 / 1024:.2f} MB)"
                    )
                
                await asyncio.sleep(self.interval)
            except Exception as e:
                self.logger.error(f"Error in memory monitoring: {e}")
                await asyncio.sleep(self.interval)
```

**code file end: crawlo/extension/memory_monitor.py**

---


### code file start: crawlo/extension/performance_profiler.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import io
import os
import pstats
import asyncio
import cProfile
from typing import Any, Optional

from crawlo.logging import get_logger
from crawlo.utils.error_handler import ErrorHandler
from crawlo.event import CrawlerEvent


class PerformanceProfilerExtension:
    """
    性能分析扩展
    在爬虫运行期间进行性能分析，帮助优化爬虫性能
    """

    def __init__(self, crawler: Any):
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        self.error_handler = ErrorHandler(self.__class__.__name__, crawler.settings.get('LOG_LEVEL'))
        
        # 获取配置参数
        self.enabled = self.settings.get_bool('PERFORMANCE_PROFILER_ENABLED', False)
        self.output_dir = self.settings.get('PERFORMANCE_PROFILER_OUTPUT_DIR', 'profiling')
        self.interval = self.settings.get_int('PERFORMANCE_PROFILER_INTERVAL', 300)  # 默认5分钟
        
        self.profiler: Optional[cProfile.Profile] = None
        self.task: Optional[asyncio.Task] = None
        
        # 创建输出目录
        if self.enabled:
            os.makedirs(self.output_dir, exist_ok=True)

    @classmethod
    def create_instance(cls, crawler: Any) -> 'PerformanceProfilerExtension':
        # 只有当配置启用时才创建实例
        if not crawler.settings.get_bool('PERFORMANCE_PROFILER_ENABLED', False):
            from crawlo.exceptions import NotConfigured
            raise NotConfigured("PerformanceProfilerExtension: PERFORMANCE_PROFILER_ENABLED is False")
        
        o = cls(crawler)
        if o.enabled:
            crawler.subscriber.subscribe(o.spider_opened, event=CrawlerEvent.SPIDER_OPENED)
            crawler.subscriber.subscribe(o.spider_closed, event=CrawlerEvent.SPIDER_CLOSED)
        return o

    async def spider_opened(self) -> None:
        """爬虫启动时开始性能分析"""
        if not self.enabled:
            return
            
        try:
            self.profiler = cProfile.Profile()
            self.profiler.enable()
            
            # 启动定期保存分析结果的任务
            self.task = asyncio.create_task(self._periodic_save())
            
            self.logger.info("Performance profiler started.")
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="启动性能分析器失败", 
                raise_error=False
            )

    async def spider_closed(self) -> None:
        """爬虫关闭时停止性能分析并保存结果"""
        if not self.enabled or not self.profiler:
            return
            
        try:
            # 停止定期保存任务
            if self.task:
                self.task.cancel()
                try:
                    await self.task
                except asyncio.CancelledError:
                    pass
            
            # 停止分析器并保存最终结果
            self.profiler.disable()
            
            # 保存分析结果
            await self._save_profile("final")
            self.logger.info("Performance profiler stopped and results saved.")
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="停止性能分析器失败", 
                raise_error=False
            )

    async def _periodic_save(self) -> None:
        """定期保存分析结果"""
        counter = 1
        while True:
            try:
                await asyncio.sleep(self.interval)
                if self.profiler:
                    # 临时禁用分析器以保存结果
                    self.profiler.disable()
                    await self._save_profile(f"periodic_{counter}")
                    counter += 1
                    # 重新启用分析器
                    self.profiler.enable()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Error in periodic profiling save: {e}")

    async def _save_profile(self, name: str) -> None:
        """保存分析结果到文件"""
        try:
            # 创建内存中的字符串流
            s = io.StringIO()
            ps = pstats.Stats(self.profiler, stream=s)
            
            # 排序并打印统计信息
            ps.sort_stats('cumulative')
            ps.print_stats()
            
            # 保存到文件
            filename = os.path.join(self.output_dir, f'profile_{name}.txt')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(s.getvalue())
            
            self.logger.info(f"Performance profile saved to {filename}")
        except Exception as e:
            self.logger.error(f"Error saving performance profile: {e}")
```

**code file end: crawlo/extension/performance_profiler.py**

---


### code file start: crawlo/extension/request_recorder.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
import json
from typing import Any
from datetime import datetime

from crawlo.event import CrawlerEvent
from crawlo.logging import get_logger


class RequestRecorderExtension:
    """
    请求记录扩展
    记录所有发送的请求信息到文件，便于调试和分析
    """

    def __init__(self, crawler: Any):
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        # 获取配置参数
        self.enabled = self.settings.get_bool('REQUEST_RECORDER_ENABLED', False)
        self.output_dir = self.settings.get('REQUEST_RECORDER_OUTPUT_DIR', 'requests_log')
        self.max_file_size = self.settings.get_int('REQUEST_RECORDER_MAX_FILE_SIZE', 10 * 1024 * 1024)  # 默认10MB
        
        # 创建输出目录
        if self.enabled:
            os.makedirs(self.output_dir, exist_ok=True)
            
        self.current_file = None
        self.current_file_size = 0

    @classmethod
    def create_instance(cls, crawler: Any) -> 'RequestRecorderExtension':
        # 只有当配置启用时才创建实例
        if not crawler.settings.get_bool('REQUEST_RECORDER_ENABLED', False):
            from crawlo.exceptions import NotConfigured
            raise NotConfigured("RequestRecorderExtension: REQUEST_RECORDER_ENABLED is False")
        
        o = cls(crawler)
        if o.enabled:
            crawler.subscriber.subscribe(o.request_scheduled, event=CrawlerEvent.REQUEST_SCHEDULED)
            crawler.subscriber.subscribe(o.response_received, event=CrawlerEvent.RESPONSE_RECEIVED)
            crawler.subscriber.subscribe(o.spider_closed, event=CrawlerEvent.SPIDER_CLOSED)
        return o

    async def request_scheduled(self, request: Any, spider: Any) -> None:
        """记录调度的请求"""
        if not self.enabled:
            return
            
        try:
            request_info = {
                'timestamp': datetime.now().isoformat(),
                'type': 'request',
                'url': request.url,
                'method': request.method,
                'headers': dict(request.headers),
                'meta': getattr(request, 'meta', {}),
            }
            
            await self._write_record(request_info)
        except Exception as e:
            self.logger.error(f"Error recording request: {e}")

    async def response_received(self, response: Any, spider: Any) -> None:
        """记录接收到的响应"""
        if not self.enabled:
            return
            
        try:
            response_info = {
                'timestamp': datetime.now().isoformat(),
                'type': 'response',
                'url': response.url,
                'status_code': response.status_code,
                'headers': dict(response.headers),
            }
            
            await self._write_record(response_info)
        except Exception as e:
            self.logger.error(f"Error recording response: {e}")

    async def spider_closed(self, spider: Any) -> None:
        """爬虫关闭时清理资源"""
        if self.current_file:
            self.current_file.close()
            self.current_file = None
        self.logger.info("Request recorder closed.")

    async def _write_record(self, record: dict) -> None:
        """写入记录到文件"""
        # 检查是否需要创建新文件
        if not self.current_file or self.current_file_size > self.max_file_size:
            if self.current_file:
                self.current_file.close()
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = os.path.join(self.output_dir, f'requests_{timestamp}.jsonl')
            self.current_file = open(filename, 'a', encoding='utf-8')
            self.current_file_size = 0
        
        # 写入记录
        line = json.dumps(record, ensure_ascii=False) + '\n'
        self.current_file.write(line)
        self.current_file.flush()
        self.current_file_size += len(line.encode('utf-8'))
```

**code file end: crawlo/extension/request_recorder.py**

---


### code file start: crawlo/extension/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
from typing import List, Any
from pprint import pformat

from crawlo.logging import get_logger
from crawlo.utils.misc import load_object
from crawlo.exceptions import ExtensionInitError


class ExtensionManager:

    def __init__(self, crawler: Any):
        self.crawler = crawler
        self.extensions: List = []
        extensions = self.crawler.settings.get_list('EXTENSIONS')
        self.logger = get_logger(self.__class__.__name__)
        self._add_extensions(extensions)
        self._subscribe_extensions()

    @classmethod
    def create_instance(cls, *args: Any, **kwargs: Any) -> 'ExtensionManager':
        return cls(*args, **kwargs)

    def _add_extensions(self, extensions: List[str]) -> None:
        for extension_path in extensions:
            try:
                extension_cls = load_object(extension_path)
                if not hasattr(extension_cls, 'create_instance'):
                    raise ExtensionInitError(
                        f"Extension '{extension_path}' init failed: Must have method 'create_instance()'"
                    )
                self.extensions.append(extension_cls.create_instance(self.crawler))
            except Exception as e:
                self.logger.error(f"Failed to load extension '{extension_path}': {e}")
                raise ExtensionInitError(f"Failed to load extension '{extension_path}': {e}")
        
        if extensions:
            # 恢复INFO级别日志，保留关键的启用信息
            self.logger.info(f"Enabled extensions: \n{pformat(extensions)}")

    def _subscribe_extensions(self) -> None:
        """订阅扩展方法到相应的事件"""
        from crawlo.event import CrawlerEvent
        
        for extension in self.extensions:
            # 订阅 spider_closed 方法
            if hasattr(extension, 'spider_closed'):
                self.crawler.subscriber.subscribe(extension.spider_closed, event=CrawlerEvent.SPIDER_CLOSED)
            
            # 订阅 item_successful 方法
            if hasattr(extension, 'item_successful'):
                self.crawler.subscriber.subscribe(extension.item_successful, event=CrawlerEvent.ITEM_SUCCESSFUL)
            
            # 订阅 item_discard 方法
            if hasattr(extension, 'item_discard'):
                self.crawler.subscriber.subscribe(extension.item_discard, event=CrawlerEvent.ITEM_DISCARD)
            
            # 订阅 response_received 方法
            if hasattr(extension, 'response_received'):
                self.crawler.subscriber.subscribe(extension.response_received, event=CrawlerEvent.RESPONSE_RECEIVED)
            
            # 订阅 request_scheduled 方法
            if hasattr(extension, 'request_scheduled'):
                self.crawler.subscriber.subscribe(extension.request_scheduled, event=CrawlerEvent.REQUEST_SCHEDULED)
```

**code file end: crawlo/extension/__init__.py**

---


### code file start: crawlo/factories/base.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
组件工厂基类和规范
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, Any, Dict, Callable


@dataclass
class ComponentSpec:
    """组件规范 - 定义如何创建组件"""
    
    name: str
    component_type: Type
    factory_func: Callable[..., Any]
    dependencies: list = None
    singleton: bool = False
    config_key: str = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


class ComponentFactory(ABC):
    """组件工厂基类"""
    
    @abstractmethod
    def create(self, spec: ComponentSpec, **kwargs) -> Any:
        """创建组件实例"""
        pass
    
    @abstractmethod
    def supports(self, component_type: Type) -> bool:
        """检查是否支持指定类型的组件"""
        pass


class DefaultComponentFactory(ComponentFactory):
    """默认组件工厂实现"""
    
    def __init__(self):
        self._instances: Dict[str, Any] = {}
    
    def create(self, spec: ComponentSpec, **kwargs) -> Any:
        """创建组件实例"""
        # 单例模式检查
        if spec.singleton and spec.name in self._instances:
            return self._instances[spec.name]
        
        # 调用工厂函数创建实例
        instance = spec.factory_func(**kwargs)
        
        # 保存单例实例
        if spec.singleton:
            self._instances[spec.name] = instance
        
        return instance
    
    def supports(self, component_type: Type) -> bool:
        """支持所有类型"""
        return True
    
    def clear_singletons(self):
        """清除单例实例（测试用）"""
        self._instances.clear()
```

**code file end: crawlo/factories/base.py**

---


### code file start: crawlo/factories/crawler.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawler组件工厂 - 专门用于创建Crawler相关组件
"""

from typing import Any, Type

from .base import ComponentFactory, ComponentSpec
from .registry import get_component_registry


class CrawlerComponentFactory(ComponentFactory):
    """Crawler组件工厂"""
    
    def create(self, spec: ComponentSpec, **kwargs) -> Any:
        """创建Crawler相关组件"""
        # 检查是否需要crawler依赖
        if 'crawler' in spec.dependencies and 'crawler' not in kwargs:
            raise ValueError(f"Crawler instance required for component {spec.name}")
        
        return spec.factory_func(**kwargs)
    
    def supports(self, component_type: Type) -> bool:
        """检查是否支持指定类型"""
        # 这里可以根据需要定义支持的组件类型
        supported_types = [
            'Engine', 'Scheduler', 'StatsCollector', 
            'Subscriber', 'ExtensionManager'
        ]
        return component_type.__name__ in supported_types


# Engine组件
def create_engine(crawler, **kwargs):
    from crawlo.core.engine import Engine
    return Engine(crawler)

# Scheduler组件
def create_scheduler(crawler, **kwargs):
    from crawlo.core.scheduler import Scheduler
    return Scheduler.create_instance(crawler)

# StatsCollector组件
def create_stats(crawler, **kwargs):
    from crawlo.stats_collector import StatsCollector
    return StatsCollector(crawler)

# Subscriber组件
def create_subscriber(**kwargs):
    from crawlo.subscriber import Subscriber
    return Subscriber()

# ExtensionManager组件
def create_extension_manager(crawler, **kwargs):
    from crawlo.extension import ExtensionManager
    return ExtensionManager.create_instance(crawler)

def register_crawler_components():
    """注册Crawler相关组件"""
    from .utils import register_components
    
    # 注册工厂
    registry = get_component_registry()
    registry.register_factory(CrawlerComponentFactory())
    
    # 批量注册组件
    component_list = [
        {
            'name': 'engine',
            'component_type': 'Engine',
            'factory_func': create_engine,
            'dependencies': ['crawler']
        },
        {
            'name': 'scheduler',
            'component_type': 'Scheduler',
            'factory_func': create_scheduler,
            'dependencies': ['crawler']
        },
        {
            'name': 'stats',
            'component_type': 'StatsCollector',
            'factory_func': create_stats,
            'dependencies': ['crawler']
        },
        {
            'name': 'subscriber',
            'component_type': 'Subscriber',
            'factory_func': create_subscriber,
            'dependencies': []
        },
        {
            'name': 'extension_manager',
            'component_type': 'ExtensionManager',
            'factory_func': create_extension_manager,
            'dependencies': ['crawler']
        }
    ]
    
    register_components(component_list)


# 自动注册
register_crawler_components()
```

**code file end: crawlo/factories/crawler.py**

---


### code file start: crawlo/factories/registry.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
组件注册表 - 管理所有组件的注册和创建
"""

import threading
from typing import Dict, List, Type, Any, Optional

from .base import ComponentFactory, ComponentSpec, DefaultComponentFactory


class ComponentRegistry:
    """
    组件注册表
    
    职责：
    1. 管理组件规范的注册
    2. 根据类型查找合适的工厂
    3. 处理依赖关系
    4. 创建组件实例
    """
    
    def __init__(self):
        self._specs: Dict[str, ComponentSpec] = {}
        self._factories: List[ComponentFactory] = []
        self._default_factory = DefaultComponentFactory()
        self._lock = threading.RLock()
    
    def register(self, spec: ComponentSpec):
        """注册组件规范"""
        with self._lock:
            self._specs[spec.name] = spec
    
    def register_factory(self, factory: ComponentFactory):
        """注册组件工厂"""
        with self._lock:
            self._factories.append(factory)
    
    def get_spec(self, name: str) -> Optional[ComponentSpec]:
        """获取组件规范"""
        with self._lock:
            return self._specs.get(name)
    
    def get_factory(self, component_type: Type) -> ComponentFactory:
        """获取支持指定类型的工厂"""
        with self._lock:
            for factory in self._factories:
                if factory.supports(component_type):
                    return factory
            return self._default_factory
    
    def create(self, name: str, **kwargs) -> Any:
        """创建组件实例"""
        spec = self.get_spec(name)
        if not spec:
            raise ValueError(f"Component spec '{name}' not found")
        
        factory = self.get_factory(spec.component_type)
        return factory.create(spec, **kwargs)
    
    def get(self, name: str, **kwargs) -> Any:
        """获取组件实例（create的别名）"""
        return self.create(name, **kwargs)
    
    def list_components(self) -> List[str]:
        """列出所有已注册的组件"""
        with self._lock:
            return list(self._specs.keys())
    
    def clear(self):
        """清空注册表"""
        with self._lock:
            self._specs.clear()
            self._factories.clear()
            self._default_factory.clear_singletons()


# 全局组件注册表
_global_registry = ComponentRegistry()


def get_component_registry() -> ComponentRegistry:
    """获取全局组件注册表"""
    return _global_registry
```

**code file end: crawlo/factories/registry.py**

---


### code file start: crawlo/factories/utils.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
工厂工具模块 - 提供通用的组件注册和创建工具
"""

from typing import Any, Callable, List, Optional, Type, Union
from .base import ComponentSpec
from .registry import get_component_registry


def register_component(
    name: str,
    component_type: Union[Type, str],
    factory_func: Callable[..., Any],
    dependencies: Optional[List[str]] = None,
    singleton: bool = False,
    config_key: Optional[str] = None
) -> None:
    """
    注册组件的便捷函数
    
    Args:
        name: 组件名称
        component_type: 组件类型
        factory_func: 工厂函数
        dependencies: 依赖列表
        singleton: 是否单例
        config_key: 配置键名
    """
    registry = get_component_registry()
    
    # 如果component_type是字符串，创建一个动态类型
    if isinstance(component_type, str):
        component_type = type(component_type, (), {})
    
    spec_kwargs = {
        'name': name,
        'component_type': component_type,
        'factory_func': factory_func,
        'dependencies': dependencies or [],
        'singleton': singleton
    }
    
    # 只有当config_key不为None时才添加
    if config_key is not None:
        spec_kwargs['config_key'] = config_key
    
    spec = ComponentSpec(**spec_kwargs)
    
    registry.register(spec)


def register_components(component_list: List[dict]) -> None:
    """
    批量注册组件
    
    Args:
        component_list: 组件定义列表，每个元素是一个包含组件信息的字典
    """
    for component_info in component_list:
        register_component(**component_info)


def create_component_factory(
    component_name: str,
    module_path: str,
    class_name: str,
    dependencies: Optional[List[str]] = None,
    singleton: bool = False
) -> Callable[..., Any]:
    """
    创建组件工厂函数的便捷函数
    
    Args:
        component_name: 组件名称（用于错误信息）
        module_path: 模块路径
        class_name: 类名
        dependencies: 依赖列表
        singleton: 是否单例
        
    Returns:
        工厂函数
    """
    def factory_func(*args, **kwargs):
        try:
            # 动态导入模块
            module = __import__(module_path, fromlist=[class_name])
            component_class = getattr(module, class_name)
            
            # 检查是否需要调用create_instance方法
            if hasattr(component_class, 'create_instance'):
                return component_class.create_instance(*args, **kwargs)
            else:
                return component_class(*args, **kwargs)
        except Exception as e:
            raise RuntimeError(f"Failed to create {component_name}: {e}")
    
    return factory_func


def create_crawler_component_factory(
    component_name: str,
    module_path: str,
    class_name: str
) -> Callable[..., Any]:
    """
    创建需要crawler依赖的组件工厂函数
    
    Args:
        component_name: 组件名称
        module_path: 模块路径
        class_name: 类名
        
    Returns:
        工厂函数
    """
    def factory_func(crawler=None, **kwargs):
        if crawler is None:
            raise ValueError(f"Crawler instance required for component {component_name}")
        
        try:
            # 动态导入模块
            module = __import__(module_path, fromlist=[class_name])
            component_class = getattr(module, class_name)
            
            # 检查是否需要调用create_instance方法
            if hasattr(component_class, 'create_instance'):
                return component_class.create_instance(crawler, **kwargs)
            else:
                return component_class(crawler, **kwargs)
        except Exception as e:
            raise RuntimeError(f"Failed to create {component_name}: {e}")
    
    return factory_func
```

**code file end: crawlo/factories/utils.py**

---


### code file start: crawlo/factories/__init__.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawlo组件工厂系统
==================

提供统一的组件创建和依赖注入机制
"""

from .registry import ComponentRegistry, get_component_registry
from .base import ComponentFactory, ComponentSpec
from .crawler import CrawlerComponentFactory

# 公共接口
register_component = get_component_registry().register
get_component = get_component_registry().get
create_component = get_component_registry().create

__all__ = [
    'ComponentRegistry',
    'ComponentFactory', 
    'ComponentSpec',
    'CrawlerComponentFactory',
    'get_component_registry',
    'register_component',
    'get_component',
    'create_component'
]
```

**code file end: crawlo/factories/__init__.py**

---


### code file start: crawlo/filters/aioredis_filter.py 

```python
from typing import Optional, Dict, Any, Union, Awaitable, Literal
import redis.asyncio as aioredis
import asyncio
from inspect import iscoroutinefunction

# 尝试导入Redis集群支持
try:
    from redis.asyncio.cluster import RedisCluster
    REDIS_CLUSTER_AVAILABLE = True
except ImportError:
    RedisCluster = None
    REDIS_CLUSTER_AVAILABLE = False

from crawlo.filters import BaseFilter
from crawlo.logging import get_logger
from crawlo.utils.redis_connection_pool import get_redis_pool, RedisConnectionPool


class AioRedisFilter(BaseFilter):
    """
    基于Redis集合实现的异步请求去重过滤器
    
    支持特性:
    - 分布式爬虫多节点共享去重数据
    - TTL 自动过期清理机制
    - Pipeline 批量操作优化性能
    - 容错设计和连接池管理
    - Redis集群支持
    """

    def __init__(
            self,
            redis_key: str,
            client: Optional[aioredis.Redis] = None,
            stats: Optional[Dict[str, Any]] = None,
            debug: bool = False,
            log_level: int = 20,  # logging.INFO
            cleanup_fp: bool = False,
            ttl: Optional[int] = None
    ):
        """
        初始化Redis过滤器
        
        :param redis_key: Redis中存储指纹的键名
        :param client: Redis客户端实例（可以为None，稍后初始化）
        :param stats: 统计信息存储
        :param debug: 是否启用调试模式
        :param log_level: 日志级别
        :param cleanup_fp: 关闭时是否清理指纹
        :param ttl: 指纹过期时间（秒）
        """
        self.logger = get_logger(self.__class__.__name__)
        super().__init__(self.logger, stats, debug)

        self.redis_key = redis_key
        self.redis = client
        self.cleanup_fp = cleanup_fp
        self.ttl = ttl
        
        # 保存连接池引用（用于延迟初始化）
        self._redis_pool: Optional[RedisConnectionPool] = None
        
        # 性能计数器
        self._redis_operations = 0
        self._pipeline_operations = 0
        
        # 连接状态标记，避免重复尝试连接失败的Redis
        self._connection_failed = False

    @classmethod
    def create_instance(cls, crawler) -> 'BaseFilter':
        """从爬虫配置创建过滤器实例"""
        redis_url = crawler.settings.get('REDIS_URL', 'redis://localhost:6379')
        # 确保 decode_responses=False 以避免编码问题
        decode_responses = False  # crawler.settings.get_bool('DECODE_RESPONSES', False)
        ttl_setting = crawler.settings.get_int('REDIS_TTL')

        # 处理TTL设置
        ttl = None
        if ttl_setting is not None:
            ttl = max(0, int(ttl_setting)) if ttl_setting > 0 else None

        try:
            # 使用优化的连接池，确保 decode_responses=False
            redis_pool = get_redis_pool(
                redis_url,
                max_connections=20,
                socket_connect_timeout=5,
                socket_timeout=30,
                health_check_interval=30,
                retry_on_timeout=True,
                decode_responses=decode_responses,  # 确保不自动解码响应
                encoding='utf-8'
            )
            
            # 注意：这里不应该使用 await，因为 create_instance 不是异步方法
            # 我们将在实际使用时获取连接
            redis_client = None  # 延迟初始化
        except Exception as e:
            raise RuntimeError(f"Redis连接池初始化失败: {redis_url} - {str(e)}")

        # 使用统一的Redis key命名规范: crawlo:{project_name}:filter:fingerprint
        project_name = crawler.settings.get('PROJECT_NAME', 'default')
        redis_key = f"crawlo:{project_name}:filter:fingerprint"

        instance = cls(
            redis_key=redis_key,
            client=redis_client,
            stats=crawler.stats,
            cleanup_fp=crawler.settings.get_bool('CLEANUP_FP', False),
            ttl=ttl,
            debug=crawler.settings.get_bool('FILTER_DEBUG', False),
            log_level=getattr(crawler.settings, 'LOG_LEVEL_NUM', 20)  # 默认INFO级别
        )
        
        # 保存连接池引用，以便在需要时获取连接
        instance._redis_pool = redis_pool
        return instance

    async def _get_redis_client(self):
        """获取Redis客户端实例（延迟初始化）"""
        # 如果之前连接失败，直接返回None
        if self._connection_failed:
            return None
            
        if self.redis is None and self._redis_pool is not None:
            try:
                connection = await self._redis_pool.get_connection()
                # 确保返回的是Redis客户端而不是连接池本身
                if hasattr(connection, 'ping'):
                    self.redis = connection
                else:
                    self.redis = connection
            except Exception as e:
                self._connection_failed = True
                self.logger.error(f"Redis连接失败，将使用本地去重: {e}")
                return None
        return self.redis

    def _is_cluster_mode(self) -> bool:
        """检查是否为集群模式"""
        if REDIS_CLUSTER_AVAILABLE and RedisCluster is not None:
            # 检查 redis 是否为 RedisCluster 实例
            if self.redis is not None and isinstance(self.redis, RedisCluster):
                return True
        return False

    def requested(self, request) -> bool:
        """
        检查请求是否已存在（同步方法）
        
        :param request: 请求对象
        :return: True 表示重复，False 表示新请求
        """
        # 这个方法需要同步实现，但Redis操作是异步的
        # 在实际使用中，应该通过异步方式调用 _requested_async
        # 由于BaseFilter要求同步方法，我们在这里返回False表示不重复
        return False

    async def requested_async(self, request) -> bool:
        """
        异步检查请求是否已存在
        
        :param request: 请求对象
        :return: True 表示重复，False 表示新请求
        """
        try:
            # 确保Redis客户端已初始化
            redis_client = await self._get_redis_client()
            
            # 如果Redis不可用，返回False表示不重复（避免丢失请求）
            if redis_client is None:
                return False
            
            # 使用基类的指纹生成方法
            fp = str(self._get_fingerprint(request))
            self._redis_operations += 1

            # 检查指纹是否存在
            if self._is_cluster_mode():
                # 集群模式下使用哈希标签确保键在同一个slot
                hash_tag = "{filter}"
                redis_key_with_tag = f"{self.redis_key}{hash_tag}"
                # 直接调用异步方法
                result = redis_client.sismember(redis_key_with_tag, fp)
                if asyncio.iscoroutine(result):
                    exists = await result
                else:
                    exists = result
            else:
                # 直接调用异步方法
                result = redis_client.sismember(self.redis_key, fp)
                if asyncio.iscoroutine(result):
                    exists = await result
                else:
                    exists = result
            
            self._pipeline_operations += 1

            if exists:
                if self.debug:
                    self.logger.debug(f"发现重复请求: {fp[:20]}...")
                return bool(exists)

            # 如果不存在，添加指纹并设置TTL
            await self._add_fingerprint_async(fp)
            return False

        except Exception as e:
            self.logger.error(f"请求检查失败: {getattr(request, 'url', '未知URL')} - {e}")
            # 在网络异常时返回False，避免丢失请求
            return False

    def add_fingerprint(self, fp: str) -> None:
        """
        添加新指纹到Redis集合（同步方法）
        
        :param fp: 请求指纹字符串
        """
        # 这个方法需要同步实现，但Redis操作是异步的
        # 在实际使用中，应该通过异步方式调用 _add_fingerprint_async
        pass

    async def _add_fingerprint_async(self, fp: str) -> bool:
        """
        异步添加新指纹到Redis集合
        
        :param fp: 请求指纹字符串
        :return: 是否成功添加（True 表示新添加，False 表示已存在）
        """
        try:
            # 确保Redis客户端已初始化
            redis_client = await self._get_redis_client()
            
            # 如果Redis不可用，返回False表示添加失败
            if redis_client is None:
                return False
            
            fp = str(fp)
            
            # 添加指纹
            if self._is_cluster_mode():
                # 集群模式下使用哈希标签确保键在同一个slot
                hash_tag = "{filter}"
                redis_key_with_tag = f"{self.redis_key}{hash_tag}"
                # 直接调用异步方法
                result = redis_client.sadd(redis_key_with_tag, fp)
                if asyncio.iscoroutine(result):
                    added = await result
                else:
                    added = result
                if self.ttl and self.ttl > 0:
                    expire_result = redis_client.expire(redis_key_with_tag, self.ttl)
                    if asyncio.iscoroutine(expire_result):
                        await expire_result
                    else:
                        expire_result  # 不需要等待同步结果
                added = added == 1  # sadd 返回 1 表示新添加
            else:
                # 直接调用异步方法
                result = redis_client.sadd(self.redis_key, fp)
                if asyncio.iscoroutine(result):
                    added = await result
                else:
                    added = result
                if self.ttl and self.ttl > 0:
                    expire_result = redis_client.expire(self.redis_key, self.ttl)
                    if asyncio.iscoroutine(expire_result):
                        await expire_result
                    else:
                        expire_result  # 不需要等待同步结果
            
            self._pipeline_operations += 1
            
            if self.debug and added:
                self.logger.debug(f"添加新指纹: {fp[:20]}...")
            
            return bool(added)
            
        except Exception as e:
            self.logger.error(f"添加指纹失败: {fp[:20]}... - {e}")
            return False

    def __contains__(self, fp: str) -> bool:
        """
        检查指纹是否存在于Redis集合中（同步方法）
        
        注意：Python的魔术方法__contains__不能是异步的，
        所以这个方法提供同步接口，仅用于基本的存在性检查。
        对于需要异步检查的场景，请使用 contains_async() 方法。
        
        :param fp: 请求指纹字符串
        :return: 是否存在
        """
        # 由于__contains__不能是异步的，我们只能提供一个基本的同步检查
        # 如果Redis客户端未初始化，返回False
        if self.redis is None:
            return False
            
        # 对于同步场景，我们无法进行真正的Redis查询
        # 所以返回False，避免阻塞调用
        # 真正的异步检查应该使用 contains_async() 方法
        return False
    
    async def contains_async(self, fp: str) -> bool:
        """
        异步检查指纹是否存在于Redis集合中
        
        这是真正的异步检查方法，应该优先使用这个方法而不是__contains__
        
        :param fp: 请求指纹字符串
        :return: 是否存在
        """
        try:
            # 确保Redis客户端已初始化
            redis_client = await self._get_redis_client()
            
            # 如果Redis不可用，返回False表示不存在
            if redis_client is None:
                return False
            
            # 检查指纹是否存在
            if self._is_cluster_mode():
                # 集群模式下使用哈希标签确保键在同一个slot
                hash_tag = "{filter}"
                redis_key_with_tag = f"{self.redis_key}{hash_tag}"
                # 直接调用异步方法
                result = redis_client.sismember(redis_key_with_tag, str(fp))
                if asyncio.iscoroutine(result):
                    exists = await result
                else:
                    exists = result
            else:
                # 直接调用异步方法
                result = redis_client.sismember(self.redis_key, str(fp))
                if asyncio.iscoroutine(result):
                    exists = await result
                else:
                    exists = result
            return bool(exists)
        except Exception as e:
            self.logger.error(f"检查指纹存在性失败: {fp[:20]}... - {e}")
            # 在网络异常时返回False，避免丢失请求
            return False


# 为了兼容性，确保导出类
__all__ = ['AioRedisFilter']
```

**code file end: crawlo/filters/aioredis_filter.py**

---


### code file start: crawlo/filters/memory_filter.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
内存过滤器实现
================
提供基于内存的高效请求去重功能。

支持的过滤器:
- MemoryFilter: 纯内存去重，性能最佳
- MemoryFileFilter: 内存+文件持久化，支持重启恢复
"""
import os
import threading
from weakref import WeakSet
from typing import Set, TextIO, Optional

from crawlo.filters import BaseFilter
from crawlo.logging import get_logger


class MemoryFilter(BaseFilter):
    """
    基于内存的高效请求去重过滤器
    
    特点:
    - 高性能: 基于 Python set() 的 O(1) 查找效率
    - 内存优化: 支持弱引用临时存储
    - 统计信息: 提供详细的性能统计
    - 线程安全: 支持多线程并发访问
    
    适用场景:
    - 单机爬虫
    - 中小规模数据集
    - 对性能要求较高的场景
    """

    def __init__(self, crawler):
        """
        初始化内存过滤器

        :param crawler: 爬虫实例，用于获取配置
        """
        self.fingerprints: Set[str] = set()  # 主指纹存储
        self._temp_weak_refs = WeakSet()     # 弱引用临时存储
        self._lock = threading.RLock()       # 线程安全锁

        # 初始化日志和统计
        debug = crawler.settings.get_bool('FILTER_DEBUG', False)
        logger = get_logger(self.__class__.__name__)
        super().__init__(logger, crawler.stats, debug)

        # 性能计数器
        self._dupe_count = 0
        self._unique_count = 0
        
        # 内存优化配置
        self._max_capacity = crawler.settings.get_int('MEMORY_FILTER_MAX_CAPACITY', 1000000)
        self._cleanup_threshold = crawler.settings.get_float('MEMORY_FILTER_CLEANUP_THRESHOLD', 0.8)

    def add_fingerprint(self, fp: str) -> None:
        """
        线程安全地添加请求指纹

        :param fp: 请求指纹字符串
        :raises TypeError: 如果指纹不是字符串类型
        """
        if not isinstance(fp, str):
            raise TypeError(f"指纹必须是字符串类型，得到 {type(fp)}")

        with self._lock:
            if fp not in self.fingerprints:
                # 检查容量限制
                if len(self.fingerprints) >= self._max_capacity:
                    self._cleanup_old_fingerprints()
                
                self.fingerprints.add(fp)
                self._unique_count += 1
                
                if self.debug:
                    self.logger.debug(f"添加指纹: {fp[:20]}...")
    
    def _cleanup_old_fingerprints(self) -> None:
        """清理老旧指纹释放内存空间"""
        cleanup_count = int(len(self.fingerprints) * (1 - self._cleanup_threshold))
        if cleanup_count > 0:
            # 随机清理一部分指纹（简单策略）
            fingerprints_list = list(self.fingerprints)
            import random
            to_remove = random.sample(fingerprints_list, cleanup_count)
            self.fingerprints.difference_update(to_remove)
            self.logger.info(f"清理了 {cleanup_count} 个老旧指纹")

    def requested(self, request) -> bool:
        """
        线程安全地检查请求是否重复（主要接口）

        :param request: 请求对象
        :return: 是否重复
        """
        with self._lock:
            # 使用基类的指纹生成方法
            fp = self._get_fingerprint(request)
            if fp in self.fingerprints:
                self._dupe_count += 1
                return True

            self.add_fingerprint(fp)
            return False

    def __contains__(self, item: str) -> bool:
        """
        线程安全地支持 in 操作符检查

        :param item: 要检查的指纹
        :return: 是否已存在
        """
        with self._lock:
            return item in self.fingerprints

    @property
    def stats_summary(self) -> dict:
        """获取过滤器统计信息"""
        with self._lock:
            return {
                'filter_type': 'MemoryFilter',
                'capacity': len(self.fingerprints),
                'max_capacity': self._max_capacity,
                'duplicates': self._dupe_count,
                'uniques': self._unique_count,
                'total_processed': self._dupe_count + self._unique_count,
                'duplicate_rate': f"{self._dupe_count / max(1, self._dupe_count + self._unique_count) * 100:.2f}%",
                'memory_usage': self._estimate_memory(),
                'capacity_usage': f"{len(self.fingerprints) / self._max_capacity * 100:.2f}%"
            }

    def _estimate_memory(self) -> str:
        """估算内存使用量（近似值）"""
        if not self.fingerprints:
            return "0 MB"
        
        avg_item_size = sum(len(x) for x in self.fingerprints) / len(self.fingerprints)
        total = len(self.fingerprints) * (avg_item_size + 50)  # 50字节额外开销
        
        if total < 1024:
            return f"{total:.1f} B"
        elif total < 1024 * 1024:
            return f"{total / 1024:.1f} KB" 
        else:
            return f"{total / (1024 * 1024):.2f} MB"

    def clear(self) -> None:
        """线程安全地清空所有指纹数据"""
        with self._lock:
            self.fingerprints.clear()
            self._dupe_count = 0
            self._unique_count = 0
            if self.debug:
                self.logger.debug("已清空所有指纹")

    def close(self) -> None:
        """关闭过滤器（清理资源）"""
        self.clear()

    # 兼容旧版异步接口
    async def closed(self):
        """兼容异步接口"""
        self.close()


class MemoryFileFilter(BaseFilter):
    """基于内存的请求指纹过滤器，支持原子化文件持久化"""

    def __init__(self, crawler):
        """
        初始化过滤器
        :param crawler: 爬虫框架Crawler对象，用于获取配置
        """
        self.fingerprints: Set[str] = set()  # 主存储集合
        self._lock = threading.RLock()  # 线程安全锁
        self._file: Optional[TextIO] = None  # 文件句柄

        debug = crawler.settings.get_bool("FILTER_DEBUG", False)
        logger = get_logger(self.__class__.__name__)
        super().__init__(logger, crawler.stats, debug)

        # 初始化文件存储
        request_dir = crawler.settings.get("REQUEST_DIR")
        if request_dir:
            self._init_file_store(request_dir)

    def _init_file_store(self, request_dir: str) -> None:
        """原子化初始化文件存储"""
        with self._lock:
            try:
                os.makedirs(request_dir, exist_ok=True)
                file_path = os.path.join(request_dir, 'request_fingerprints.txt')

                # 原子化操作：读取现有指纹
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        self.fingerprints.update(
                            line.strip() for line in f
                            if line.strip()
                        )

                # 以追加模式打开文件
                self._file = open(file_path, 'a+', encoding='utf-8')
                self.logger.info(f"Initialized fingerprint file: {file_path}")

            except Exception as e:
                self.logger.error(f"Failed to init file store: {str(e)}")
                raise

    def add_fingerprint(self, fp: str) -> None:
        """
        线程安全的指纹添加操作
        :param fp: 请求指纹字符串
        """
        with self._lock:
            if fp not in self.fingerprints:
                self.fingerprints.add(fp)
                self._persist_fp(fp)

    def _persist_fp(self, fp: str) -> None:
        """持久化指纹到文件（需在锁保护下调用）"""
        if self._file:
            try:
                self._file.write(f"{fp}\n")
                self._file.flush()
                os.fsync(self._file.fileno())  # 确保写入磁盘
            except IOError as e:
                self.logger.error(f"Failed to persist fingerprint: {str(e)}")

    def __contains__(self, item: str) -> bool:
        """
        线程安全的指纹检查
        :param item: 要检查的指纹
        :return: 是否已存在
        """
        with self._lock:
            return item in self.fingerprints

    def close(self) -> None:
        """安全关闭资源（同步方法）"""
        with self._lock:
            if self._file and not self._file.closed:
                try:
                    self._file.flush()
                    os.fsync(self._file.fileno())
                finally:
                    self._file.close()
                self.logger.info(f"Closed fingerprint file: {self._file.name}")

    def __del__(self):
        """析构函数双保险"""
        self.close()

    # 兼容异步接口
    async def closed(self):
        """标准的关闭入口"""
        self.close()

```

**code file end: crawlo/filters/memory_filter.py**

---


### code file start: crawlo/filters/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Crawlo过滤器模块
================
提供多种请求去重过滤器实现。

过滤器类型:
- MemoryFilter: 基于内存的高效去重，适合单机模式
- AioRedisFilter: 基于Redis的分布式去重，适合分布式模式
- MemoryFileFilter: 内存+文件持久化，适合需要重启恢复的场景

核心接口:
- BaseFilter: 所有过滤器的基类
- requested(): 检查请求是否重复的主要方法
"""
from abc import ABC, abstractmethod
from typing import Optional

from crawlo.utils.fingerprint import FingerprintGenerator


class BaseFilter(ABC):
    """
    请求去重过滤器基类
    
    提供统一的去重接口和统计功能。
    所有过滤器实现都应该继承此类。
    """

    def __init__(self, logger, stats, debug: bool = False):
        """
        初始化过滤器
        
        :param logger: 日志器实例
        :param stats: 统计信息存储
        :param debug: 是否启用调试日志
        """
        self.logger = logger
        self.stats = stats
        self.debug = debug
        self._request_count = 0
        self._duplicate_count = 0

    @classmethod
    def create_instance(cls, *args, **kwargs) -> 'BaseFilter':
        return cls(*args, **kwargs)

    def _get_fingerprint(self, request) -> str:
        """
        获取请求指纹（内部辅助方法）
        
        使用统一的 FingerprintGenerator 生成请求指纹。
        子类可以直接调用此方法，避免重复实现。
        
        :param request: 请求对象
        :return: 请求指纹字符串
        """
        return FingerprintGenerator.request_fingerprint(
            request.method,
            request.url,
            request.body or b'',
            dict(request.headers) if hasattr(request, 'headers') else {}
        )

    def requested(self, request) -> bool:
        """
        检查请求是否重复（主要接口）
        
        :param request: 请求对象
        :return: True 表示重复，False 表示新请求
        """
        self._request_count += 1
        fp = self._get_fingerprint(request)
        
        if fp in self:
            self._duplicate_count += 1
            self.log_stats(request)
            return True
            
        self.add_fingerprint(fp)
        return False

    @abstractmethod
    def add_fingerprint(self, fp: str) -> None:
        """
        添加请求指纹（子类必须实现）
        
        :param fp: 请求指纹字符串
        """
        pass
    
    @abstractmethod
    def __contains__(self, item: str) -> bool:
        """
        检查指纹是否存在（支持 in 操作符）
        
        :param item: 要检查的指纹
        :return: 是否已存在
        """
        pass

    def log_stats(self, request) -> None:
        """
        记录统计信息
        
        :param request: 重复的请求对象
        """
        if self.debug:
            self.logger.debug(f'过滤重复请求: {request}')
        self.stats.inc_value(f'{self}/filtered_count')
    
    def get_stats(self) -> dict:
        """
        获取过滤器统计信息
        
        :return: 统计信息字典
        """
        return {
            'total_requests': self._request_count,
            'duplicate_requests': self._duplicate_count,
            'unique_requests': self._request_count - self._duplicate_count,
            'duplicate_rate': f"{self._duplicate_count / max(1, self._request_count) * 100:.2f}%"
        }
    
    def reset_stats(self) -> None:
        """重置统计信息"""
        self._request_count = 0
        self._duplicate_count = 0
    
    def close(self) -> None:
        """关闭过滤器并清理资源"""
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'


# 导出所有可用的过滤器
__all__ = ['BaseFilter']

# 动态导入具体实现
try:
    from .memory_filter import MemoryFilter, MemoryFileFilter
    __all__.extend(['MemoryFilter', 'MemoryFileFilter'])
except ImportError:
    MemoryFilter = None
    MemoryFileFilter = None

try:
    from .aioredis_filter import AioRedisFilter
    __all__.append('AioRedisFilter')
except ImportError:
    AioRedisFilter = None

# 提供便捷的过滤器映射
FILTER_MAP = {
    'memory': MemoryFilter,
    'memory_file': MemoryFileFilter,
    'redis': AioRedisFilter,
    'aioredis': AioRedisFilter,  # 别名
}

# 过滤掉不可用的过滤器
FILTER_MAP = {k: v for k, v in FILTER_MAP.items() if v is not None}

def get_filter_class(name: str):
    """根据名称获取过滤器类"""
    if name in FILTER_MAP:
        return FILTER_MAP[name]
    raise ValueError(f"未知的过滤器类型: {name}。可用类型: {list(FILTER_MAP.keys())}")
```

**code file end: crawlo/filters/__init__.py**

---


### code file start: crawlo/initialization/built_in.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
内置初始化器 - 提供框架核心组件的初始化实现
"""

import time
from typing import TYPE_CHECKING

from .registry import BaseInitializer, register_initializer
from .phases import InitializationPhase, PhaseResult
from .context import InitializationContext

if TYPE_CHECKING:
    from crawlo.logging import LogConfig


class LoggingInitializer(BaseInitializer):
    """日志系统初始化器"""
    
    def __init__(self):
        super().__init__(InitializationPhase.LOGGING)
    
    def initialize(self, context: InitializationContext) -> PhaseResult:
        """初始化日志系统"""
        start_time = time.time()
        
        try:
            # 导入日志模块
            from crawlo.logging import configure_logging, LogConfig
            
            # 获取日志配置
            log_config = self._get_log_config(context)
            
            # 确保日志目录存在
            if log_config and log_config.file_path and log_config.file_enabled:
                import os
                log_dir = os.path.dirname(log_config.file_path)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir, exist_ok=True)
            
            # 配置日志系统
            configure_logging(log_config)
            
            # 存储到共享数据
            context.add_shared_data('log_config', log_config)
            
            # 创建框架logger
            from crawlo.logging import get_logger
            framework_logger = get_logger('crawlo.framework')
            context.add_shared_data('framework_logger', framework_logger)
            
            return self._create_result(
                success=True,
                duration=time.time() - start_time,
                artifacts={'log_config': log_config}
            )
            
        except Exception as e:
            return self._create_result(
                success=False,
                duration=time.time() - start_time,
                error=e
            )
    
    def _get_log_config(self, context: InitializationContext) -> 'LogConfig | None':
        """
        获取日志配置
        
        Args:
            context: 初始化上下文
            
        Returns:
            LogConfig: 日志配置对象
        """
        # 导入日志配置类
        from crawlo.logging import LogConfig
        from crawlo.utils.config_manager import ConfigUtils
        
        # 按优先级获取配置：自定义配置 > 上下文配置 > 项目配置 > 默认配置
        config_sources = [
            context.custom_settings,
            context.settings,
            self._load_project_config()
        ]
        
        # 遍历配置源
        for config_source in config_sources:
            if config_source and ConfigUtils.has_config_prefix(config_source, 'LOG_'):
                log_config = self._create_log_config_from_source(config_source)
                if log_config:
                    return log_config
        
        # 使用默认配置
        return LogConfig()
    
    def _create_log_config_from_source(self, config_source) -> 'LogConfig | None':
        """
        从配置源创建日志配置
        
        Args:
            config_source: 配置源
            
        Returns:
            LogConfig: 日志配置对象，如果配置源无效则返回None
        """
        # 导入日志配置类
        from crawlo.logging import LogConfig
        from crawlo.utils.config_manager import ConfigUtils
        
        # 检查配置源是否有效
        if not config_source:
            return None
            
        # 检查是否有日志相关配置
        if not ConfigUtils.has_config_prefix(config_source, 'LOG_'):
            return None
            
        # 从配置源获取日志配置
        log_level = ConfigUtils.get_config_value([config_source], 'LOG_LEVEL', 'INFO')
        log_file = ConfigUtils.get_config_value([config_source], 'LOG_FILE')
        log_format = ConfigUtils.get_config_value([config_source], 'LOG_FORMAT', '%(asctime)s - [%(name)s] - %(levelname)s: %(message)s')
        log_encoding = ConfigUtils.get_config_value([config_source], 'LOG_ENCODING', 'utf-8')
        log_max_bytes = ConfigUtils.get_config_value([config_source], 'LOG_MAX_BYTES', 10 * 1024 * 1024, int)
        log_backup_count = ConfigUtils.get_config_value([config_source], 'LOG_BACKUP_COUNT', 5, int)
        log_console_enabled = ConfigUtils.get_config_value([config_source], 'LOG_CONSOLE_ENABLED', True, bool)
        log_file_enabled = ConfigUtils.get_config_value([config_source], 'LOG_FILE_ENABLED', True, bool)
        
        # 创建日志配置
        return LogConfig(
            level=log_level,
            format=log_format,
            encoding=log_encoding,
            file_path=log_file,
            max_bytes=log_max_bytes,
            backup_count=log_backup_count,
            console_enabled=log_console_enabled,
            file_enabled=log_file_enabled
        )
    
    def _load_project_config(self):
        """
        自动加载项目配置以获取日志设置
        """
        try:
            # 查找项目根目录
            import os
            import sys
            import configparser
            
            current_path = os.getcwd()
            
            # 向上查找直到找到crawlo.cfg
            checked_paths = set()
            path = current_path
            
            while path not in checked_paths:
                checked_paths.add(path)
                
                # 检查crawlo.cfg
                cfg_file = os.path.join(path, "crawlo.cfg")
                if os.path.exists(cfg_file):
                    # 读取配置文件
                    config_parser = configparser.ConfigParser()
                    config_parser.read(cfg_file, encoding="utf-8")
                    
                    if config_parser.has_section("settings") and config_parser.has_option("settings", "default"):
                        # 获取settings模块路径
                        settings_module_path = config_parser.get("settings", "default")
                        
                        # 添加项目根目录到Python路径
                        if path not in sys.path:
                            sys.path.insert(0, path)
                        
                        # 导入项目配置模块
                        import importlib
                        settings_module = importlib.import_module(settings_module_path)
                        
                        # 创建配置字典
                        from crawlo.utils.config_manager import ConfigUtils
                        project_config = ConfigUtils.merge_config_sources([settings_module])
                        
                        return project_config
                    
                # 向上一级目录
                parent = os.path.dirname(path)
                if parent == path:
                    break
                path = parent
            
            return {}
            
        except Exception as e:
            return {}


class SettingsInitializer(BaseInitializer):
    """配置系统初始化器"""
    
    def __init__(self):
        super().__init__(InitializationPhase.SETTINGS)
    
    def initialize(self, context: InitializationContext) -> PhaseResult:
        """初始化配置系统"""
        start_time = time.time()
        
        try:
            # 导入配置管理器
            from crawlo.settings.setting_manager import SettingManager
            from crawlo.project import _load_project_settings
            
            # 如果上下文中已有设置，则使用它作为基础配置
            if context.settings:
                # 使用用户传递的设置作为基础配置
                settings = context.settings
                # 加载项目配置并合并
                project_settings = _load_project_settings(context.custom_settings)
                # 合并配置，用户配置优先
                settings.update_attributes(project_settings.attributes)
            else:
                # 创建配置管理器并加载项目配置
                settings = _load_project_settings(context.custom_settings)
            
            # 存储到上下文
            context.settings = settings
            context.add_shared_data('settings', settings)
            
            return self._create_result(
                success=True,
                duration=time.time() - start_time,
                artifacts={'settings': settings}
            )
            
        except Exception as e:
            return self._create_result(
                success=False,
                duration=time.time() - start_time,
                error=e
            )


class CoreComponentsInitializer(BaseInitializer):
    """核心组件初始化器"""
    
    def __init__(self):
        super().__init__(InitializationPhase.CORE_COMPONENTS)
    
    def initialize(self, context: InitializationContext) -> PhaseResult:
        """初始化核心组件"""
        start_time = time.time()
        
        try:
            # 在核心组件初始化阶段，大多数组件需要crawler参数
            # 因此我们只初始化那些完全独立的组件
            # 或者只记录需要初始化的组件类型，实际初始化在crawler创建时进行
            
            return self._create_result(
                success=True,
                duration=time.time() - start_time,
                artifacts={}
            )
            
        except Exception as e:
            return self._create_result(
                success=False,
                duration=time.time() - start_time,
                error=e
            )
    
# 注意：核心组件需要crawler参数，不能在此阶段初始化
        # 实际初始化将在crawler创建时进行


class ExtensionsInitializer(BaseInitializer):
    """扩展组件初始化器"""
    
    def __init__(self):
        super().__init__(InitializationPhase.EXTENSIONS)
    
    def initialize(self, context: InitializationContext) -> PhaseResult:
        """初始化扩展组件"""
        start_time = time.time()
        
        try:
            # 初始化扩展组件
            self._initialize_extensions(context)
            
            return self._create_result(
                success=True,
                duration=time.time() - start_time,
                artifacts={}
            )
            
        except Exception as e:
            return self._create_result(
                success=False,
                duration=time.time() - start_time,
                error=e
            )
    
    def _initialize_extensions(self, context: InitializationContext):
        """初始化扩展组件"""
        try:
            # 获取扩展配置
            extensions = []
            if context.settings:
                extensions = context.settings.get('EXTENSIONS', [])
            elif context.custom_settings:
                extensions = context.custom_settings.get('EXTENSIONS', [])
            
            # 初始化每个扩展
            initialized_extensions = []
            for extension_path in extensions:
                try:
                    from crawlo.utils.misc import load_object
                    extension_class = load_object(extension_path)
                    extension_instance = extension_class()
                    initialized_extensions.append(extension_instance)
                except Exception as e:
                    if context.settings and context.settings.get('EXTENSIONS_STRICT', False):
                        raise
                    else:
                        # 非严格模式下记录警告但继续
                        context.add_warning(f"Failed to initialize extension {extension_path}: {e}")
            
            # 存储到上下文
            context.add_shared_data('extensions', initialized_extensions)
        except Exception as e:
            context.add_error(f"Failed to initialize extensions: {e}")
            raise


class FrameworkStartupLogger(BaseInitializer):
    """框架启动日志记录器"""
    
    def __init__(self):
        # 使用新的FRAMEWORK_STARTUP_LOG阶段
        super().__init__(InitializationPhase.FRAMEWORK_STARTUP_LOG)
    
    def initialize(self, context: InitializationContext) -> PhaseResult:
        """记录框架启动日志"""
        start_time = time.time()
        
        try:
            # 获取框架logger
            from crawlo.logging import get_logger
            logger = get_logger('crawlo.framework')
            
            # 获取框架版本
            version = self._get_framework_version()
            
            # 记录框架启动信息（符合规范要求）
            logger.info(f"Crawlo Framework Started {version}")
            
            # 获取运行模式
            run_mode = "unknown"
            if context.settings:
                run_mode = context.settings.get('RUN_MODE', 'standalone')
            logger.info(f"Run mode: {run_mode}")
            
            # 注意：爬虫名称信息将在实际启动爬虫时记录，而不是在框架初始化时
            
            return self._create_result(
                success=True,
                duration=time.time() - start_time,
                artifacts={}
            )
            
        except Exception as e:
            # 即使日志记录失败，也不应该影响框架初始化
            return self._create_result(
                success=True,  # 不影响初始化成功与否
                duration=time.time() - start_time,
                error=e
            )
    
    def _get_framework_version(self):
        """获取框架版本"""
        try:
            from crawlo import __version__
            return __version__
        except Exception:
            return "unknown"


def register_built_in_initializers():
    """注册所有内置初始化器"""
    register_initializer(LoggingInitializer())
    register_initializer(SettingsInitializer())
    register_initializer(CoreComponentsInitializer())
    register_initializer(ExtensionsInitializer())
    register_initializer(FrameworkStartupLogger())  # 添加框架启动日志记录器
```

**code file end: crawlo/initialization/built_in.py**

---


### code file start: crawlo/initialization/context.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
初始化上下文 - 保存初始化过程中的状态和数据
"""

import time
import threading
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

from .phases import InitializationPhase, PhaseResult


@dataclass
class InitializationContext:
    """
    初始化上下文
    
    保存初始化过程中的状态、数据和结果
    """
    
    # 基本信息
    start_time: float = field(default_factory=time.time)
    end_time: Optional[float] = None
    
    # 当前状态
    current_phase: InitializationPhase = InitializationPhase.PREPARING
    completed_phases: List[InitializationPhase] = field(default_factory=list)
    failed_phases: List[InitializationPhase] = field(default_factory=list)
    
    # 阶段结果
    phase_results: Dict[InitializationPhase, PhaseResult] = field(default_factory=dict)
    
    # 共享数据
    shared_data: Dict[str, Any] = field(default_factory=dict)
    
    # 配置信息
    settings: Optional[Any] = None
    custom_settings: Optional[Dict[str, Any]] = None
    
    # 错误信息
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    
    # 线程安全
    _lock: threading.RLock = field(default_factory=threading.RLock, init=False)
    
    def set_current_phase(self, phase: InitializationPhase):
        """设置当前阶段"""
        with self._lock:
            self.current_phase = phase
    
    def mark_phase_completed(self, phase: InitializationPhase, result: PhaseResult):
        """标记阶段完成"""
        with self._lock:
            if result.success:
                self.completed_phases.append(phase)
            else:
                self.failed_phases.append(phase)
            
            self.phase_results[phase] = result
    
    def add_shared_data(self, key: str, value: Any):
        """添加共享数据"""
        with self._lock:
            self.shared_data[key] = value
    
    def get_shared_data(self, key: str, default=None):
        """获取共享数据"""
        with self._lock:
            return self.shared_data.get(key, default)
    
    def add_error(self, message: str):
        """添加错误信息"""
        with self._lock:
            self.errors.append(message)
    
    def add_warning(self, message: str):
        """添加警告信息"""
        with self._lock:
            self.warnings.append(message)
    
    def is_phase_completed(self, phase: InitializationPhase) -> bool:
        """检查阶段是否完成"""
        with self._lock:
            return phase in self.completed_phases
    
    def is_phase_failed(self, phase: InitializationPhase) -> bool:
        """检查阶段是否失败"""
        with self._lock:
            return phase in self.failed_phases
    
    def get_phase_result(self, phase: InitializationPhase) -> Optional[PhaseResult]:
        """获取阶段结果"""
        with self._lock:
            return self.phase_results.get(phase)
    
    def get_total_duration(self) -> float:
        """获取总耗时"""
        end = self.end_time or time.time()
        return end - self.start_time
    
    def get_phase_durations(self) -> Dict[InitializationPhase, float]:
        """获取各阶段耗时"""
        with self._lock:
            return {
                phase: result.duration 
                for phase, result in self.phase_results.items()
            }
    
    def get_success_rate(self) -> float:
        """获取成功率"""
        with self._lock:
            total = len(self.completed_phases) + len(self.failed_phases)
            if total == 0:
                return 0.0
            return len(self.completed_phases) / total * 100
    
    def finish(self):
        """标记初始化完成"""
        with self._lock:
            self.end_time = time.time()
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        with self._lock:
            return {
                'start_time': self.start_time,
                'end_time': self.end_time,
                'total_duration': self.get_total_duration(),
                'current_phase': self.current_phase.value,
                'completed_phases': [p.value for p in self.completed_phases],
                'failed_phases': [p.value for p in self.failed_phases],
                'success_rate': self.get_success_rate(),
                'error_count': len(self.errors),
                'warning_count': len(self.warnings),
                'phase_durations': {
                    p.value: duration 
                    for p, duration in self.get_phase_durations().items()
                }
            }
```

**code file end: crawlo/initialization/context.py**

---


### code file start: crawlo/initialization/core.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
核心初始化器 - 协调整个初始化过程
"""

import threading
import time
import signal
from typing import Optional, Any

from .built_in import register_built_in_initializers
from .context import InitializationContext
from .phases import InitializationPhase, PhaseResult, get_execution_order, get_phase_definition, validate_phase_dependencies
from .registry import get_global_registry


from crawlo.utils.singleton import singleton

@singleton
class CoreInitializer:
    """
    核心初始化器 - 协调整个框架的初始化过程
    
    职责：
    1. 管理初始化阶段的执行顺序
    2. 处理阶段间的依赖关系
    3. 提供统一的初始化入口
    4. 错误处理和降级策略
    """
    
    def __init__(self):
        self._context: Optional[InitializationContext] = None
        self._is_ready = False
        self._init_lock = threading.RLock()
        
        # 在注册内置初始化器之前，先验证阶段依赖关系
        is_valid, error_msg = validate_phase_dependencies()
        if not is_valid:
            raise RuntimeError(f"初始化阶段配置错误: {error_msg}")
        
        # 注册内置初始化器
        register_built_in_initializers()
    
    @property
    def context(self) -> Optional[InitializationContext]:
        """获取初始化上下文"""
        return self._context
    
    @property  
    def is_ready(self) -> bool:
        """检查框架是否已准备就绪"""
        return self._is_ready
    
    def initialize(self, settings=None, **kwargs) -> Any:
        """
        执行框架初始化
        
        Args:
            settings: 配置对象
            **kwargs: 额外的配置参数
            
        Returns:
            初始化后的配置管理器
        """
        with self._init_lock:
            # 如果已经初始化完成，直接返回
            if self._is_ready and self._context and self._context.settings:
                return self._context.settings
            
            # 创建初始化上下文
            context = InitializationContext()
            context.custom_settings = kwargs
            context.settings = settings
            self._context = context
            
            try:
                # 执行初始化阶段
                self._execute_initialization_phases(context)
                
                # 检查关键阶段是否完成
                if not context.is_phase_completed(InitializationPhase.SETTINGS):
                    raise RuntimeError("Settings initialization failed")
                
                self._is_ready = True
                context.finish()
                
                return context.settings
                
            except Exception as e:
                context.add_error(f"Framework initialization failed: {e}")
                context.finish()
                
                # 降级策略
                return self._fallback_initialization(settings, **kwargs)
    
    def _execute_initialization_phases(self, context: InitializationContext):
        """执行初始化阶段"""
        registry = get_global_registry()
        execution_order = get_execution_order()
        
        # 只执行已注册的阶段
        registered_phases = set(registry.get_all_phases())
        
        for phase in execution_order:
            if phase == InitializationPhase.ERROR:
                continue
                
            # 只执行已注册的阶段
            if phase not in registered_phases:
                continue
                
            context.set_current_phase(phase)
            
            # 检查依赖关系
            if not self._check_dependencies(phase, context):
                phase_def = get_phase_definition(phase)
                if not (phase_def and phase_def.optional):
                    raise RuntimeError(f"Dependencies not satisfied for phase {phase}")
                else:
                    # 可选阶段，跳过
                    continue
            
            # 执行阶段（带超时控制）
            start_time = time.time()
            try:
                result = self._execute_phase_with_timeout(phase, context, registry)
                result.duration = time.time() - start_time
                
                context.mark_phase_completed(phase, result)
                
                if not result.success and not self._is_phase_optional(phase):
                    raise RuntimeError(f"Phase {phase} failed: {result.error}")
                    
            except Exception as e:
                duration = time.time() - start_time
                result = PhaseResult(
                    phase=phase,
                    success=False,
                    duration=duration,
                    error=e
                )
                context.mark_phase_completed(phase, result)
                
                if not self._is_phase_optional(phase):
                    raise
    
    def _execute_phase_with_timeout(self, phase: InitializationPhase, 
                                    context: InitializationContext,
                                    registry) -> PhaseResult:
        """
        执行阶段并支持超时控制
        
        Args:
            phase: 初始化阶段
            context: 初始化上下文
            registry: 初始化器注册表
            
        Returns:
            PhaseResult: 阶段执行结果
            
        Raises:
            TimeoutError: 阶段执行超时
        """
        phase_def = get_phase_definition(phase)
        timeout = phase_def.timeout if phase_def else 30.0
        
        # 使用线程执行，支持超时
        result_container: list[Optional[PhaseResult]] = [None]
        exception_container: list[Optional[Exception]] = [None]
        
        def execute_in_thread():
            try:
                result_container[0] = registry.execute_phase(phase, context)
            except Exception as e:
                exception_container[0] = e
        
        thread = threading.Thread(target=execute_in_thread, daemon=True)
        thread.start()
        thread.join(timeout=timeout)
        
        if thread.is_alive():
            # 超时了
            error_msg = f"Phase {phase.value} execution timeout after {timeout} seconds"
            context.add_warning(error_msg)
            return PhaseResult(
                phase=phase,
                success=False,
                error=TimeoutError(error_msg)
            )
        
        # 检查是否有异常
        if exception_container[0]:
            raise exception_container[0]
        
        # 返回结果（已经确保不为None）
        if result_container[0] is None:
            raise RuntimeError(f"Phase {phase.value} returned None result")
        return result_container[0]
    
    def _check_dependencies(self, phase: InitializationPhase, 
                          context: InitializationContext) -> bool:
        """检查阶段依赖关系"""
        phase_def = get_phase_definition(phase)
        if not phase_def:
            return True
        
        for dependency in phase_def.dependencies:
            if not context.is_phase_completed(dependency):
                return False
        
        return True
    
    def _is_phase_optional(self, phase: InitializationPhase) -> bool:
        """检查阶段是否可选"""
        phase_def = get_phase_definition(phase)
        return phase_def.optional if phase_def else False
    
    def _fallback_initialization(self, settings=None, **kwargs):
        """降级初始化策略"""
        try:
            # 尝试创建基本的配置管理器
            from crawlo.settings.setting_manager import SettingManager
            
            if settings:
                return settings
            else:
                fallback_settings = SettingManager()
                if kwargs:
                    fallback_settings.update_attributes(kwargs)
                return fallback_settings
                
        except Exception:
            # 如果连降级都失败，返回None
            return None
    
    def reset(self):
        """重置初始化状态（主要用于测试）"""
        with self._init_lock:
            self._context = None
            self._is_ready = False
```

**code file end: crawlo/initialization/core.py**

---


### code file start: crawlo/initialization/phases.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
初始化阶段定义
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict


class InitializationPhase(Enum):
    """初始化阶段枚举"""
    
    # 阶段0：准备阶段
    PREPARING = "preparing"
    
    # 阶段1：日志系统初始化
    LOGGING = "logging"
    
    # 阶段2：配置系统初始化  
    SETTINGS = "settings"
    
    # 阶段3：核心组件初始化
    CORE_COMPONENTS = "core_components"
    
    # 阶段4：扩展组件初始化
    EXTENSIONS = "extensions"
    
    # 阶段5：框架启动日志记录
    FRAMEWORK_STARTUP_LOG = "framework_startup_log"
    
    # 阶段6：完成
    COMPLETED = "completed"
    
    # 错误状态
    ERROR = "error"


@dataclass
class PhaseResult:
    """阶段执行结果"""
    phase: InitializationPhase
    success: bool
    duration: float = 0.0
    error: Optional[Exception] = None
    artifacts: dict = None  # 阶段产生的工件
    
    def __post_init__(self):
        if self.artifacts is None:
            self.artifacts = {}


@dataclass 
class PhaseDefinition:
    """阶段定义"""
    phase: InitializationPhase
    name: str
    description: str
    dependencies: List[InitializationPhase] = None
    optional: bool = False
    timeout: float = 30.0  # 超时时间（秒）
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


# 预定义的初始化阶段
PHASE_DEFINITIONS = [
    PhaseDefinition(
        phase=InitializationPhase.PREPARING,
        name="准备阶段",
        description="初始化基础环境和检查前置条件",
        dependencies=[],
        timeout=5.0
    ),
    PhaseDefinition(
        phase=InitializationPhase.LOGGING,
        name="日志系统",
        description="配置和初始化日志系统",
        dependencies=[],  # 移除对PREPARING的依赖
        timeout=10.0
    ),
    PhaseDefinition(
        phase=InitializationPhase.SETTINGS,
        name="配置系统", 
        description="加载和验证配置",
        dependencies=[InitializationPhase.LOGGING],
        timeout=15.0
    ),
    PhaseDefinition(
        phase=InitializationPhase.CORE_COMPONENTS,
        name="核心组件",
        description="初始化框架核心组件",
        dependencies=[InitializationPhase.SETTINGS],
        timeout=20.0
    ),
    PhaseDefinition(
        phase=InitializationPhase.EXTENSIONS,
        name="扩展组件",
        description="加载和初始化扩展组件",
        dependencies=[InitializationPhase.CORE_COMPONENTS],
        optional=True,
        timeout=15.0
    ),
    PhaseDefinition(
        phase=InitializationPhase.FRAMEWORK_STARTUP_LOG,
        name="框架启动日志",
        description="记录框架启动相关信息",
        dependencies=[InitializationPhase.LOGGING, InitializationPhase.SETTINGS],
        timeout=5.0
    ),
    PhaseDefinition(
        phase=InitializationPhase.COMPLETED,
        name="初始化完成",
        description="框架初始化完成",
        dependencies=[
            InitializationPhase.CORE_COMPONENTS,
            InitializationPhase.FRAMEWORK_STARTUP_LOG
        ],  # Extensions是可选的
        timeout=5.0
    )
]


def get_phase_definition(phase: InitializationPhase) -> Optional[PhaseDefinition]:
    """获取阶段定义"""
    for definition in PHASE_DEFINITIONS:
        if definition.phase == phase:
            return definition
    return None


def get_execution_order() -> List[InitializationPhase]:
    """获取执行顺序"""
    return [definition.phase for definition in PHASE_DEFINITIONS]


def validate_dependencies() -> bool:
    """验证阶段依赖关系的正确性"""
    phases = {definition.phase for definition in PHASE_DEFINITIONS}
    
    for definition in PHASE_DEFINITIONS:
        for dependency in definition.dependencies:
            if dependency not in phases:
                return False
    
    return True


def detect_circular_dependencies() -> Optional[List[InitializationPhase]]:
    """
    检测循环依赖
    
    使用DFS（深度优先搜索）算法检测初始化阶段的循环依赖。
    
    Returns:
        Optional[List[InitializationPhase]]: 如果存在循环，返回循环路径；否则返回None
    
    算法说明：
        使用三色标记法：
        - 白色(0)：未访问
        - 灰色(1)：正在访问（在当前DFS路径中）
        - 黑色(2)：已完成访问
        
        如果在DFS过程中遇到灰色节点，说明存在循环依赖。
    """
    # 构建依赖图
    dependency_graph: Dict[InitializationPhase, List[InitializationPhase]] = {}
    for definition in PHASE_DEFINITIONS:
        dependency_graph[definition.phase] = definition.dependencies.copy()
    
    # 三色标记：0-白色(未访问)，1-灰色(访问中)，2-黑色(已完成)
    color: Dict[InitializationPhase, int] = {phase: 0 for phase in dependency_graph}
    parent: Dict[InitializationPhase, Optional[InitializationPhase]] = {phase: None for phase in dependency_graph}
    
    def dfs(node: InitializationPhase) -> Optional[List[InitializationPhase]]:
        """DFS遍历检测循环"""
        color[node] = 1  # 标记为灰色（访问中）
        
        for neighbor in dependency_graph.get(node, []):
            if color[neighbor] == 1:  # 遇到灰色节点，发现循环
                # 重建循环路径
                cycle = [neighbor]
                current: Optional[InitializationPhase] = node
                while current is not None and current != neighbor:
                    cycle.append(current)
                    current = parent.get(current)
                cycle.append(neighbor)
                cycle.reverse()
                return cycle
            
            if color[neighbor] == 0:  # 未访问的节点
                parent[neighbor] = node
                result = dfs(neighbor)
                if result:
                    return result
        
        color[node] = 2  # 标记为黑色（已完成）
        return None
    
    # 对所有未访问的节点执行DFS
    for phase in dependency_graph:
        if color[phase] == 0:
            cycle = dfs(phase)
            if cycle:
                return cycle
    
    return None


def validate_phase_dependencies() -> tuple[bool, Optional[str]]:
    """
    全面验证阶段依赖关系
    
    Returns:
        tuple[bool, Optional[str]]: (是否有效, 错误信息)
    """
    # 1. 检查依赖是否存在
    if not validate_dependencies():
        return False, "存在未定义的依赖阶段"
    
    # 2. 检查循环依赖
    cycle = detect_circular_dependencies()
    if cycle:
        cycle_path = ' -> '.join([phase.value for phase in cycle])
        return False, f"检测到循环依赖: {cycle_path}"
    
    return True, None
```

**code file end: crawlo/initialization/phases.py**

---


### code file start: crawlo/initialization/registry.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
初始化器注册表 - 管理所有初始化器的注册和执行
"""

import threading
from typing import Dict, Optional, Callable, List
from .context import InitializationContext
from .phases import InitializationPhase, PhaseResult


class Initializer:
    """初始化器基类"""
    
    def __init__(self, phase: InitializationPhase):
        self._phase = phase
    
    @property
    def phase(self) -> InitializationPhase:
        """获取初始化阶段"""
        return self._phase
    
    def initialize(self, context: InitializationContext) -> PhaseResult:
        """执行初始化 - 子类必须实现"""
        raise NotImplementedError("Subclasses must implement initialize method")


class BaseInitializer(Initializer):
    """基础初始化器类 - 为向后兼容保留"""
    
    def __init__(self, phase: InitializationPhase):
        super().__init__(phase)
    
    def _create_result(self, success: bool, duration: float = 0.0, 
                      artifacts: Optional[Dict] = None, error: Optional[Exception] = None) -> PhaseResult:
        """创建初始化结果"""
        from .utils import create_initialization_result
        return create_initialization_result(
            phase=self.phase,
            success=success,
            duration=duration,
            artifacts=artifacts,
            error=error
        )


class InitializerRegistry:
    """
    初始化器注册表 - 管理所有初始化器的注册和执行
    
    特点：
    1. 线程安全的注册和执行
    2. 支持函数式和类式初始化器
    3. 统一的结果处理
    """
    
    def __init__(self):
        self._initializers: Dict[InitializationPhase, Initializer] = {}
        self._lock = threading.RLock()
    
    def register(self, initializer: Initializer):
        """注册初始化器"""
        with self._lock:
            phase = initializer.phase
            if phase in self._initializers:
                raise ValueError(f"Initializer for phase {phase} already registered")
            self._initializers[phase] = initializer
    
    def register_function(self, phase: InitializationPhase, 
                         init_func: Callable[[InitializationContext], PhaseResult]):
        """注册函数式初始化器"""
        
        class FunctionInitializer(Initializer):
            def __init__(self, phase: InitializationPhase, func: Callable):
                super().__init__(phase)
                self._phase = phase
                self._func = func
            
            def initialize(self, context: InitializationContext) -> PhaseResult:
                return self._func(context)
        
        self.register(FunctionInitializer(phase, init_func))
    
    def get_initializer(self, phase: InitializationPhase) -> Optional[Initializer]:
        """获取指定阶段的初始化器"""
        with self._lock:
            return self._initializers.get(phase)
    
    def get_all_phases(self) -> List[InitializationPhase]:
        """获取所有已注册的阶段"""
        with self._lock:
            return list(self._initializers.keys())
    
    def has_initializer(self, phase: InitializationPhase) -> bool:
        """检查是否有指定阶段的初始化器"""
        with self._lock:
            return phase in self._initializers
    
    def clear(self):
        """清空注册表"""
        with self._lock:
            self._initializers.clear()
    
    def execute_phase(self, phase: InitializationPhase, 
                     context: InitializationContext) -> PhaseResult:
        """执行指定阶段的初始化"""
        initializer = self.get_initializer(phase)
        if not initializer:
            error = ValueError(f"No initializer registered for phase {phase}")
            return PhaseResult(
                phase=phase,
                success=False,
                error=error
            )
        
        try:
            return initializer.initialize(context)
        except Exception as e:
            return PhaseResult(
                phase=phase,
                success=False,
                error=e
            )


# 全局注册表实例
_global_registry = InitializerRegistry()


def get_global_registry() -> InitializerRegistry:
    """获取全局注册表"""
    return _global_registry


def register_initializer(initializer: Initializer):
    """注册初始化器到全局注册表"""
    _global_registry.register(initializer)


def register_phase_function(phase: InitializationPhase, 
                           init_func: Callable[[InitializationContext], PhaseResult]):
    """注册函数式初始化器到全局注册表"""
    _global_registry.register_function(phase, init_func)
```

**code file end: crawlo/initialization/registry.py**

---


### code file start: crawlo/initialization/utils.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
初始化工具模块 - 提供通用的初始化工具函数
"""

import time
from typing import Optional, Dict, Any
from .phases import PhaseResult, InitializationPhase


def create_initialization_result(
    phase: 'InitializationPhase',
    success: bool, 
    duration: float = 0.0,
    artifacts: Optional[Dict[str, Any]] = None, 
    error: Optional[Exception] = None
) -> PhaseResult:
    """
    创建标准化的初始化结果
    
    Args:
        phase: 初始化阶段
        success: 是否成功
        duration: 执行时长
        artifacts: 产生的工件数据
        error: 异常对象
        
    Returns:
        PhaseResult: 标准化的初始化结果
    """
    return PhaseResult(
        phase=phase,
        success=success,
        duration=duration,
        artifacts=artifacts or {},
        error=error
    )


class InitializationTimer:
    """初始化计时器"""
    
    def __init__(self):
        self.start_time = time.time()
    
    def get_duration(self) -> float:
        """获取经过的时间"""
        return time.time() - self.start_time
```

**code file end: crawlo/initialization/utils.py**

---


### code file start: crawlo/initialization/__init__.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawlo框架统一初始化系统
=======================

设计原则：
1. 单一职责 - 每个初始化器负责特定领域
2. 依赖清晰 - 明确的初始化顺序和依赖关系
3. 可测试性 - 支持依赖注入和模拟
4. 健壮性 - 优雅的错误处理和降级策略
"""

from .registry import InitializerRegistry
from .context import InitializationContext
from .core import CoreInitializer
from .phases import InitializationPhase


# 公共接口
def initialize_framework(settings=None, **kwargs):
    """初始化框架的主要入口"""
    return CoreInitializer().initialize(settings, **kwargs)


def is_framework_ready():
    """检查框架是否已准备就绪"""
    return CoreInitializer().is_ready


def get_framework_context():
    """获取框架初始化上下文"""
    return CoreInitializer().context


__all__ = [
    'InitializerRegistry',
    'InitializationContext',
    'CoreInitializer',
    'InitializationPhase',
    'initialize_framework',
    'is_framework_ready',
    'get_framework_context'
]

```

**code file end: crawlo/initialization/__init__.py**

---


### code file start: crawlo/items/base.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
基础元类定义
"""
from abc import ABCMeta
from .fields import Field


class ItemMeta(ABCMeta):
    def __new__(mcs, name, bases, attrs):
        fields = {}
        cls_attrs = {}

        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value
            else:
                cls_attrs[attr_name] = attr_value

        cls_instance = super().__new__(mcs, name, bases, cls_attrs)
        cls_instance.FIELDS = fields
        return cls_instance

```

**code file end: crawlo/items/base.py**

---


### code file start: crawlo/items/fields.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Field 类定义
"""
from typing import Any, Optional, Type


class Field:
    """
    字段定义类，用于定义 Item 的字段属性和验证规则
    """
    def __init__(
        self,
        nullable: bool = True,
        *,
        default: Any = None,
        field_type: Optional[Type] = None,
        max_length: Optional[int] = None,
        description: str = ""
    ):
        self.nullable = nullable
        self.default = default
        self.field_type = field_type
        self.max_length = max_length
        self.description = description

    def validate(self, value: Any, field_name: str = "") -> Any:
        """
        验证字段值是否符合规则
        """
        if value is None or (isinstance(value, str) and value.strip() == ""):
            if self.default is not None:
                return self.default
            elif not self.nullable:
                raise ValueError(
                    f"字段 '{field_name}' 不允许为空。"
                )

        if value is not None and not (isinstance(value, str) and value.strip() == ""):
            if self.field_type and not isinstance(value, self.field_type):
                raise TypeError(
                    f"字段 '{field_name}' 类型错误：期望类型 {self.field_type}, 得到 {type(value)}，值：{value!r}"
                )
            if self.max_length and len(str(value)) > self.max_length:
                raise ValueError(
                    f"字段 '{field_name}' 长度超限：最大长度 {self.max_length}，当前长度 {len(str(value))}，值：{value!r}"
                )

        return value

    def __repr__(self):
        return f"<Field nullable={self.nullable} type={self.field_type} default={self.default}>"
```

**code file end: crawlo/items/fields.py**

---


### code file start: crawlo/items/items.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Item 类定义
"""
from copy import deepcopy
from pprint import pformat
from typing import Any, Iterator, Dict
from collections.abc import MutableMapping

from .base import ItemMeta
from crawlo.exceptions import ItemInitError, ItemAttributeError


class Item(MutableMapping, metaclass=ItemMeta):
    """
    数据项基类，用于定义结构化数据
    """
    FIELDS: Dict[str, Any] = {}

    def __init__(self, *args, **kwargs):
        if args:
            raise ItemInitError(f"{self.__class__.__name__} 不支持位置参数：{args}，请使用关键字参数初始化。")

        self._values: Dict[str, Any] = {}

        # 初始化字段，默认值填充
        for field_name, field_obj in self.FIELDS.items():
            if field_obj.default is not None:
                self._values[field_name] = field_obj.default

        # 覆盖默认值或设置新值
        for key, value in kwargs.items():
            self[key] = value

    def __getitem__(self, item: str) -> Any:
        return self._values[item]

    def __setitem__(self, key: str, value: Any) -> None:
        if key not in self.FIELDS:
            raise KeyError(f"{self.__class__.__name__} 不包含字段：{key}")

        field = self.FIELDS[key]
        try:
            validated_value = field.validate(value, field_name=key)
            self._values[key] = validated_value
        except Exception as e:
            error_lines = [
                "",
                "【字段校验失败】",
                f"字段名称: {key}",
                f"数据类型: {type(value)}",
                f"原始值:   {repr(value)}",
                f"是否允许空值: {field.nullable}",
                f"错误原因: {str(e)}",
                ""
            ]
            detailed_error = "\n".join(error_lines)
            raise type(e)(detailed_error) from e

    def __delitem__(self, key: str) -> None:
        del self._values[key]

    def __setattr__(self, key: str, value: Any) -> None:
        if not key.startswith("_"):
            raise AttributeError(
                f"设置字段值请使用 item[{key!r}] = {value!r}"
            )
        super().__setattr__(key, value)

    def __getattr__(self, item: str) -> Any:
        raise AttributeError(
            f"{self.__class__.__name__} 不支持字段：{item}。"
            f"请先在 `{self.__class__.__name__}` 中声明该字段，再通过 item[{item!r}] 获取。"
        )

    def __getattribute__(self, item: str) -> Any:
        try:
            field = super().__getattribute__("FIELDS")
            if isinstance(field, dict) and item in field:
                raise ItemAttributeError(
                    f"获取字段值请使用 item[{item!r}]"
                )
        except AttributeError:
            pass  # 如果 FIELDS 尚未定义，继续执行后续逻辑
        return super().__getattribute__(item)

    def __repr__(self) -> str:
        return pformat(dict(self))

    __str__ = __repr__

    def __iter__(self) -> Iterator[str]:
        return iter(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return dict(self)

    def copy(self) -> "Item":
        """深拷贝当前 Item"""
        return deepcopy(self)
```

**code file end: crawlo/items/items.py**

---


### code file start: crawlo/items/__init__.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
crawlo.items 包
===============
提供 Item 和 Field 类用于数据定义和验证。
"""
from .items import Item
from .fields import Field
from .base import ItemMeta

from crawlo.exceptions import ItemInitError, ItemAttributeError

__all__ = [
    'Item',
    'Field',
    'ItemMeta',
    'ItemInitError',
    'ItemAttributeError'
]




```

**code file end: crawlo/items/__init__.py**

---


### code file start: crawlo/logging/config.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
日志配置管理
"""

import os
from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class LogConfig:
    """日志配置数据类 - 简单明确的配置结构"""
    
    # 预设配置模板
    TEMPLATES = {
        'minimal': {
            'level': 'INFO',
            'format': '%(asctime)s - %(levelname)s: %(message)s',
            'console_enabled': True,
            'file_enabled': False
        },
        'standard': {
            'level': 'INFO',
            'format': '%(asctime)s - [%(name)s] - %(levelname)s: %(message)s',
            'console_enabled': True,
            'file_enabled': True,
            'file_path': 'logs/crawlo.log'
        },
        'detailed': {
            'level': 'DEBUG',
            'format': '%(asctime)s - [%(name)s] - %(levelname)s - %(pathname)s:%(lineno)d: %(message)s',
            'console_enabled': True,
            'file_enabled': True,
            'file_path': 'logs/crawlo.log',
            'max_bytes': 20 * 1024 * 1024,
            'backup_count': 10
        },
        'production': {
            'level': 'WARNING',
            'format': '%(asctime)s - [%(name)s] - %(levelname)s: %(message)s',
            'console_enabled': False,
            'file_enabled': True,
            'file_path': 'logs/crawlo.log',
            'max_bytes': 50 * 1024 * 1024,
            'backup_count': 20
        }
    }
    
    # 基本配置
    level: str = "INFO"
    format: str = "%(asctime)s - [%(name)s] - %(levelname)s: %(message)s"
    encoding: str = "utf-8"
    
    # 文件配置
    file_path: Optional[str] = None
    max_bytes: int = 10 * 1024 * 1024  # 10MB
    backup_count: int = 5
    
    # 控制台配置
    console_enabled: bool = True
    file_enabled: bool = True
    
    # 分别控制台和文件的日志级别
    console_level: Optional[str] = None
    file_level: Optional[str] = None
    
    # 上下文信息配置
    include_thread_id: bool = False
    include_process_id: bool = False
    include_module_path: bool = False
    
    # 模块级别配置
    module_levels: Dict[str, str] = field(default_factory=dict)
    
    @classmethod
    def from_settings(cls, settings) -> 'LogConfig':
        """从settings对象创建配置"""
        if not settings:
            return cls()
            
        # 使用settings的get方法而不是getattr
        if hasattr(settings, 'get'):
            get_val = settings.get
        else:
            get_val = lambda k, d=None: getattr(settings, k, d)
        
        # 获取默认值
        format_default_value = "%(asctime)s - [%(name)s] - %(levelname)s: %(message)s"
        
        # 确保类型安全
        def safe_get_str(key: str, default: str = '') -> str:
            value = get_val(key, default)
            return str(value) if value is not None else default
        
        def safe_get_int(key: str, default: int) -> int:
            value = get_val(key, default)
            try:
                return int(value) if value is not None else default
            except (ValueError, TypeError):
                return default
        
        def safe_get_bool(key: str, default: bool) -> bool:
            value = get_val(key, default)
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in ('1', 'true', 'yes', 'on')
            return bool(value) if value is not None else default
        
        def safe_get_dict(key: str, default: dict) -> dict:
            value = get_val(key, default)
            return value if isinstance(value, dict) else default
        
        return cls(
            level=safe_get_str('LOG_LEVEL', 'INFO'),
            format=safe_get_str('LOG_FORMAT', format_default_value),
            encoding=safe_get_str('LOG_ENCODING', 'utf-8'),
            file_path=safe_get_str('LOG_FILE'),
            max_bytes=safe_get_int('LOG_MAX_BYTES', 10 * 1024 * 1024),
            backup_count=safe_get_int('LOG_BACKUP_COUNT', 5),
            console_enabled=safe_get_bool('LOG_CONSOLE_ENABLED', True),
            file_enabled=safe_get_bool('LOG_FILE_ENABLED', True),
            console_level=safe_get_str('LOG_CONSOLE_LEVEL'),  # 允许单独设置控制台级别
            file_level=safe_get_str('LOG_FILE_LEVEL'),  # 允许单独设置文件级别
            include_thread_id=safe_get_bool('LOG_INCLUDE_THREAD_ID', False),
            include_process_id=safe_get_bool('LOG_INCLUDE_PROCESS_ID', False),
            include_module_path=safe_get_bool('LOG_INCLUDE_MODULE_PATH', False),
            module_levels=safe_get_dict('LOG_LEVELS', {})
        )
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'LogConfig':
        """从字典创建配置"""
        # 映射字典键到类属性名
        key_mapping = {
            'LOG_LEVEL': 'level',
            'LOG_FORMAT': 'format',
            'LOG_ENCODING': 'encoding',
            'LOG_FILE': 'file_path',
            'LOG_MAX_BYTES': 'max_bytes',
            'LOG_BACKUP_COUNT': 'backup_count',
            'LOG_CONSOLE_ENABLED': 'console_enabled',
            'LOG_FILE_ENABLED': 'file_enabled',
            'LOG_CONSOLE_LEVEL': 'console_level',
            'LOG_FILE_LEVEL': 'file_level',
            'LOG_INCLUDE_THREAD_ID': 'include_thread_id',
            'LOG_INCLUDE_PROCESS_ID': 'include_process_id',
            'LOG_INCLUDE_MODULE_PATH': 'include_module_path',
            'LOG_LEVELS': 'module_levels'
        }
        
        # 应用键映射
        mapped_dict = {}
        for k, v in config_dict.items():
            mapped_key = key_mapping.get(k, k)
            if mapped_key in cls.__annotations__:
                mapped_dict[mapped_key] = v
                
        return cls(**mapped_dict)
    
    @classmethod
    def from_template(cls, template_name: str) -> 'LogConfig':
        """从模板创建配置
        
        Args:
            template_name: 模板名称 (minimal, standard, detailed, production)
            
        Returns:
            LogConfig: 配置对象
        """
        if template_name not in cls.TEMPLATES:
            raise ValueError(f"未知的模板名称: {template_name}，可用模板: {', '.join(cls.TEMPLATES.keys())}")
            
        template_config = cls.TEMPLATES[template_name]
        return cls(**template_config)
    
    def get_module_level(self, module_name: str) -> str:
        """获取模块的日志级别"""
        # 先查找精确匹配
        if module_name in self.module_levels:
            return self.module_levels[module_name]
        
        # 查找父模块匹配
        parts = module_name.split('.')
        for i in range(len(parts) - 1, 0, -1):
            parent_module = '.'.join(parts[:i])
            if parent_module in self.module_levels:
                return self.module_levels[parent_module]
        
        # 返回默认级别
        return self.level
    
    def get_console_level(self) -> str:
        """获取控制台日志级别"""
        return self.console_level or self.level
    
    def get_file_level(self) -> str:
        """获取文件日志级别"""
        return self.file_level or self.level
    
    def get_format(self) -> str:
        """
        获取日志格式，包含上下文信息
        
        Returns:
            日志格式字符串
        """
        base_format = self.format
        
        # 添加线程ID
        if self.include_thread_id:
            if '[%(thread)d]' not in base_format:
                # 在时间戳后添加线程ID
                base_format = base_format.replace(
                    '%(asctime)s', 
                    '%(asctime)s [%(thread)d]'
                )
                
        # 添加进程ID
        if self.include_process_id:
            if '[%(process)d]' not in base_format:
                # 在时间戳后添加进程ID（如果已经有线程ID，则在线程ID后添加）
                if '[%(thread)d]' in base_format:
                    base_format = base_format.replace(
                        '%(asctime)s [%(thread)d]', 
                        '%(asctime)s [%(thread)d] [%(process)d]'
                    )
                else:
                    base_format = base_format.replace(
                        '%(asctime)s', 
                        '%(asctime)s [%(process)d]'
                    )
                
        # 添加模块路径
        if self.include_module_path:
            if '%(pathname)s:%(lineno)d' not in base_format:
                # 在消息前添加文件路径和行号
                base_format = base_format.replace(
                    '%(message)s', 
                    '%(pathname)s:%(lineno)d - %(message)s'
                )
                
        return base_format
    
    def validate(self) -> tuple[bool, str]:
        """验证配置有效性
        
        Returns:
            tuple[bool, str]: (是否有效, 错误信息)
        """
        valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
        
        # 验证主级别
        if self.level.upper() not in valid_levels:
            return False, f"无效的日志级别: {self.level}，有效级别为: {', '.join(valid_levels)}"
        
        # 验证控制台级别
        if self.console_level and self.console_level.upper() not in valid_levels:
            return False, f"无效的控制台日志级别: {self.console_level}，有效级别为: {', '.join(valid_levels)}"
        
        # 验证文件级别
        if self.file_level and self.file_level.upper() not in valid_levels:
            return False, f"无效的文件日志级别: {self.file_level}，有效级别为: {', '.join(valid_levels)}"
        
        # 确保日志目录存在
        if self.file_path and self.file_enabled:
            try:
                log_dir = os.path.dirname(self.file_path)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir, exist_ok=True)
            except (OSError, PermissionError) as e:
                log_dir = os.path.dirname(self.file_path) if self.file_path else "未知"
                return False, f"无法创建日志目录 {log_dir}: {e}"
        
        return True, "配置有效"
```

**code file end: crawlo/logging/config.py**

---


### code file start: crawlo/logging/factory.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
日志器工厂 - 创建和缓存Logger实例
"""

import logging
import os
import sys
import threading
from weakref import WeakValueDictionary

# 尝试导入concurrent-log-handler，如果不可用则回退到标准库
try:
    from concurrent_log_handler import ConcurrentRotatingFileHandler
    USE_CONCURRENT_HANDLER = True
    RotatingFileHandler = ConcurrentRotatingFileHandler  # 别名以避免未绑定错误
except ImportError:
    from logging.handlers import RotatingFileHandler
    USE_CONCURRENT_HANDLER = False
    ConcurrentRotatingFileHandler = RotatingFileHandler  # 别名以避免未绑定错误

from .manager import get_config, is_configured, configure
from .config import LogConfig


class LoggerFactory:
    """
    Logger工厂类 - 负责创建和缓存Logger实例
    
    特点：
    1. 使用WeakValueDictionary避免内存泄漏
    2. 线程安全的Logger创建
    3. 自动配置管理
    4. 简单的缓存策略
    5. Windows兼容的日志轮转处理
    """
    
    # Logger缓存 - 使用弱引用避免内存泄漏
    _logger_cache: WeakValueDictionary = WeakValueDictionary()
    _cache_lock = threading.RLock()
    
    @classmethod
    def get_logger(cls, name: str = 'crawlo') -> logging.Logger:
        """
        获取Logger实例
        
        Args:
            name: Logger名称
            
        Returns:
            logging.Logger: 配置好的Logger实例
        """
        # 确保日志系统已配置
        if not is_configured():
            configure()  # 使用默认配置
        
        # 检查缓存
        with cls._cache_lock:
            if name in cls._logger_cache:
                return cls._logger_cache[name]
            
            # 创建新的Logger
            logger = cls._create_logger(name)
            cls._logger_cache[name] = logger
            return logger
    
    @classmethod
    def _create_logger(cls, name: str) -> logging.Logger:
        """创建新的Logger实例"""
        config = get_config()
        if not config:
            raise RuntimeError("日志系统未配置，请先调用 configure_logging() 进行配置")
        
        # 创建Logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)  # Logger本身设为最低级别
        
        # 清除现有handlers（避免重复添加）
        logger.handlers.clear()
        
        # 获取模块级别
        module_level = config.get_module_level(name)
        
        # 创建formatter
        formatter = logging.Formatter(config.get_format())
        
        # 添加控制台Handler
        if config.console_enabled:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            # 使用专门的控制台级别或模块级别
            console_level = config.get_console_level()
            level = getattr(logging, console_level.upper(), logging.INFO)
            console_handler.setLevel(level)
            logger.addHandler(console_handler)
        
        # 添加文件Handler
        if config.file_enabled and config.file_path:
            try:
                # 确保日志目录存在
                log_dir = os.path.dirname(config.file_path)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir, exist_ok=True)
                
                # 根据平台选择合适的Handler
                file_handler = None
                if USE_CONCURRENT_HANDLER:
                    file_handler = ConcurrentRotatingFileHandler(
                        filename=config.file_path,
                        maxBytes=config.max_bytes,
                        backupCount=config.backup_count,
                        encoding=config.encoding
                    )
                else:
                    # 在Windows上给出警告信息
                    if sys.platform.startswith('win'):
                        # 检查是否已经有同名的日志文件被其他进程使用
                        try:
                            # 尝试以独占模式打开文件来检查是否被占用
                            with open(config.file_path, 'a'):
                                pass
                        except (PermissionError, OSError):
                            # 如果文件被占用，记录警告信息
                            console_handler = logging.StreamHandler()
                            console_handler.setFormatter(formatter)
                            console_handler.setLevel(logging.WARNING)
                            logger.addHandler(console_handler)
                            logger.warning(f"日志文件 {config.file_path} 可能正在被其他进程使用，这可能导致日志轮转失败。建议安装 concurrent-log-handler 库以获得更好的Windows兼容性。")
                    
                    file_handler = RotatingFileHandler(
                        filename=config.file_path,
                        maxBytes=config.max_bytes,
                        backupCount=config.backup_count,
                        encoding=config.encoding
                    )
                
                # 添加文件处理器（如果创建成功）
                if file_handler is not None:
                    file_handler.setFormatter(formatter)
                    # 使用专门的文件级别或模块级别
                    file_level = config.get_file_level()
                    level = getattr(logging, file_level.upper(), logging.INFO)
                    file_handler.setLevel(level)
                    logger.addHandler(file_handler)
            except Exception as e:
                # 文件Handler创建失败时，至少保证控制台输出
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
                console_handler.setLevel(logging.WARNING)
                logger.addHandler(console_handler)
                logger.warning(f"无法创建文件日志处理器: {e}，仅使用控制台输出。")
        
        # 防止向上传播（避免重复输出）
        logger.propagate = False
        
        return logger
    
    @classmethod
    def clear_cache(cls):
        """清空Logger缓存"""
        with cls._cache_lock:
            cls._logger_cache.clear()
    
    @classmethod
    def refresh_loggers(cls, new_config: LogConfig):
        """刷新所有缓存的Logger（配置更新时使用）"""
        with cls._cache_lock:
            # 清空缓存，强制重新创建
            cls._logger_cache.clear()


# 便捷函数
def get_logger(name: str = 'crawlo') -> logging.Logger:
    """获取Logger实例的便捷函数"""
    return LoggerFactory.get_logger(name)
```

**code file end: crawlo/logging/factory.py**

---


### code file start: crawlo/logging/manager.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
日志管理器 - 核心组件
"""

import threading
from typing import Optional
from .config import LogConfig
from crawlo.utils.singleton import singleton


@singleton
class LogManager:
    """
    日志管理器 - 单例模式
    
    职责：
    1. 全局日志配置管理
    2. 配置状态跟踪
    3. 线程安全的配置更新
    """

    def __init__(self):
        self._config: Optional[LogConfig] = None
        self._configured = False
        self._config_lock = threading.RLock()

    @property
    def config(self) -> Optional[LogConfig]:
        """获取当前配置"""
        with self._config_lock:
            return self._config

    @property
    def is_configured(self) -> bool:
        """检查是否已配置"""
        return self._configured

    def configure(self, settings=None, **kwargs) -> LogConfig:
        """
        配置日志系统
        
        Args:
            settings: 配置对象或None
            **kwargs: 关键字参数配置
            
        Returns:
            LogConfig: 生效的配置对象
        """
        with self._config_lock:
            # 总是重新配置，即使已经配置过
            # 从不同来源创建配置
            if settings is not None:
                # 检查settings是否已经是LogConfig对象
                if isinstance(settings, LogConfig):
                    config = settings
                else:
                    config = LogConfig.from_settings(settings)
            elif kwargs:
                config = LogConfig.from_dict(kwargs)
            else:
                config = LogConfig()  # 使用默认配置

            # 验证配置
            is_valid, error_msg = config.validate()
            if not is_valid:
                raise ValueError(f"Invalid log configuration: {error_msg}")

            self._config = config
            self._configured = True

            return config

    def reset(self):
        """重置配置（主要用于测试）"""
        with self._config_lock:
            self._config = None
            self._configured = False


# 全局实例
_log_manager = LogManager()


# 模块级便捷函数
def configure(settings=None, **kwargs) -> LogConfig:
    """配置日志系统"""
    return _log_manager.configure(settings, **kwargs)


def is_configured() -> bool:
    """检查是否已配置"""
    return _log_manager.is_configured


def get_config() -> Optional[LogConfig]:
    """获取当前配置"""
    return _log_manager.config


def reset():
    """重置配置"""
    _log_manager.reset()

```

**code file end: crawlo/logging/manager.py**

---


### code file start: crawlo/logging/__init__.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Crawlo统一日志系统
=================

设计原则：
1. 简单优先 - 避免过度设计
2. 性能优先 - 减少锁竞争和复杂逻辑  
3. 一致性 - 统一的日志接口
4. 可靠性 - 确保日志始终可用
"""

from .manager import LogManager
from .factory import LoggerFactory
from .config import LogConfig


# 统一的公共接口
def get_logger(name: str = 'default'):
    """获取logger实例"""
    return LoggerFactory.get_logger(name)


def configure_logging(settings=None, **kwargs):
    """配置日志系统"""
    return LogManager().configure(settings, **kwargs)


def is_configured() -> bool:
    """检查日志系统是否已配置"""
    return LogManager().is_configured


__all__ = [
    'LogManager',
    'LoggerFactory',
    'LogConfig',
    'get_logger',
    'configure_logging',
    'is_configured'
]

```

**code file end: crawlo/logging/__init__.py**

---


### code file start: crawlo/middleware/default_header.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
DefaultHeaderMiddleware 中间件
用于为所有请求添加默认请求头，支持随机更换User-Agent等功能
"""

import random
from crawlo.logging import get_logger
from crawlo.exceptions import NotConfiguredError
# 导入User-Agent数据
from crawlo.data.user_agents import get_user_agents


class DefaultHeaderMiddleware(object):
    """
    DefaultHeaderMiddleware 中间件
    用于为所有请求添加默认请求头，包括User-Agent等，支持随机更换功能
    """

    def __init__(self, settings, log_level):
        """
        初始化中间件
        """
        self.logger = get_logger(self.__class__.__name__)

        # 获取默认请求头配置
        self.headers = settings.get_dict('DEFAULT_REQUEST_HEADERS', {})

        # 获取User-Agent配置
        self.user_agent = settings.get('USER_AGENT')

        # 获取随机User-Agent列表
        self.user_agents = settings.get_list('USER_AGENTS', [])

        # 获取随机请求头配置
        self.random_headers = settings.get_dict('RANDOM_HEADERS', {})

        # 获取随机性配置
        self.randomness = settings.get_bool("RANDOMNESS", False)

        # 检查是否启用随机User-Agent
        self.random_user_agent_enabled = settings.get_bool("RANDOM_USER_AGENT_ENABLED", False)

        # 获取User-Agent设备类型
        self.user_agent_device_type = settings.get("USER_AGENT_DEVICE_TYPE", "all")

        # 如果没有配置默认请求头、User-Agent且没有启用随机功能，则禁用此中间件
        if not self.headers and not self.user_agent and not self.user_agents and not self.random_headers:
            raise NotConfiguredError(
                "未配置DEFAULT_REQUEST_HEADERS、USER_AGENT或随机头部配置，DefaultHeaderMiddleware已禁用")

        # 如果配置了User-Agent，将其添加到默认请求头中
        if self.user_agent:
            self.headers.setdefault('User-Agent', self.user_agent)

        # 如果启用了随机User-Agent但没有提供User-Agent列表，使用内置列表
        if self.random_user_agent_enabled and not self.user_agents:
            self.user_agents = get_user_agents(self.user_agent_device_type)

        self.logger.debug(f"DefaultHeaderMiddleware已启用 [默认请求头={len(self.headers)}, "
                          f"User-Agent列表={len(self.user_agents)}, "
                          f"随机头部={len(self.random_headers)}, "
                          f"随机功能={'启用' if self.randomness else '禁用'}]")

    @classmethod
    def create_instance(cls, crawler):
        """
        创建中间件实例
        """
        o = cls(
            settings=crawler.settings,
            log_level=crawler.settings.get('LOG_LEVEL')
        )
        return o

    def _get_random_user_agent(self):
        """
        获取随机User-Agent
        """
        if self.user_agents:
            return random.choice(self.user_agents)
        return None

    def _apply_random_headers(self, request):
        """
        应用随机请求头
        """
        if not self.random_headers:
            return

        for header_name, header_values in self.random_headers.items():
            # 如果header_values是列表，随机选择一个值
            if isinstance(header_values, (list, tuple)):
                header_value = random.choice(header_values)
            else:
                header_value = header_values

            # 只有当请求中没有该头部时才添加
            if header_name not in request.headers:
                request.headers[header_name] = header_value
                self.logger.debug(f"为请求 {request.url} 添加随机头部: {header_name}={header_value[:50]}...")

    def process_request(self, request, _spider):
        """
        处理请求，添加默认请求头
        """
        # 添加默认请求头
        if self.headers:
            added_headers = []
            for key, value in self.headers.items():
                # 只有当请求中没有该头部时才添加
                if key not in request.headers:
                    request.headers[key] = value
                    added_headers.append(key)

            # 记录添加的请求头（仅在调试模式下）
            if added_headers and self.logger.isEnabledFor(10):  # DEBUG level
                self.logger.debug(f"为请求 {request.url} 添加了 {len(added_headers)} 个默认请求头: {added_headers}")

        # 处理随机User-Agent
        if self.random_user_agent_enabled and 'User-Agent' not in request.headers:
            random_ua = self._get_random_user_agent()
            if random_ua:
                request.headers['User-Agent'] = random_ua
                self.logger.debug(f"为请求 {request.url} 设置随机User-Agent: {random_ua[:50]}...")

        # 处理随机请求头
        if self.randomness:
            self._apply_random_headers(request)

        return None

```

**code file end: crawlo/middleware/default_header.py**

---


### code file start: crawlo/middleware/download_delay.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
DownloadDelayMiddleware 中间件
用于控制请求之间的延迟时间，支持固定延迟和随机延迟
"""

from asyncio import sleep
from random import uniform
from crawlo.logging import get_logger
from crawlo.exceptions import NotConfiguredError


class DownloadDelayMiddleware(object):
    """
    DownloadDelayMiddleware 中间件
    用于控制请求之间的延迟时间，支持固定延迟和随机延迟
    
    功能特性:
    - 支持固定延迟时间
    - 支持随机延迟时间
    - 提供详细的日志信息
    - 记录延迟统计信息
    """

    def __init__(self, settings, log_level, stats=None):
        """
        初始化中间件
        
        Args:
            settings: 设置管理器
            log_level: 日志级别
            stats: 统计信息收集器（可选）
        """
        self.delay = settings.get_float("DOWNLOAD_DELAY")
        if not self.delay:
            raise NotConfiguredError("DOWNLOAD_DELAY not set or is zero")
            
        self.randomness = settings.get_bool("RANDOMNESS", False)
        
        # 安全地获取随机范围配置
        random_range = settings.get_list("RANDOM_RANGE")
        if len(random_range) >= 2:
            try:
                self.floor = float(random_range[0])
                self.upper = float(random_range[1])
            except (ValueError, TypeError):
                # 如果配置无效，使用默认值
                self.floor, self.upper = 0.5, 1.5
        else:
            # 如果配置不完整，使用默认值
            self.floor, self.upper = 0.5, 1.5
            
        self.logger = get_logger(self.__class__.__name__)
        self.stats = stats

    @classmethod
    def create_instance(cls, crawler):
        """
        创建中间件实例
        
        Args:
            crawler: 爬虫实例
            
        Returns:
            DownloadDelayMiddleware: 中间件实例
        """
        o = cls(
            settings=crawler.settings, 
            log_level=crawler.settings.get('LOG_LEVEL'),
            stats=getattr(crawler, 'stats', None)
        )
        return o

    async def process_request(self, _request, _spider):
        """
        处理请求，添加延迟
        
        Args:
            _request: 请求对象
            _spider: 爬虫实例
        """
        if self.randomness:
            # 计算随机延迟时间
            delay_time = uniform(self.delay * self.floor, self.delay * self.upper)
            await sleep(delay_time)
            
            # 记录统计信息
            if self.stats:
                self.stats.inc_value('download_delay/random_count')
                self.stats.inc_value('download_delay/random_total_time', delay_time)
                
            # 记录日志
            self.logger.debug(f"应用随机延迟: {delay_time:.2f}秒 (范围: {self.delay * self.floor:.2f} - {self.delay * self.upper:.2f})")
        else:
            # 应用固定延迟
            await sleep(self.delay)
            
            # 记录统计信息
            if self.stats:
                self.stats.inc_value('download_delay/fixed_count')
                self.stats.inc_value('download_delay/fixed_total_time', self.delay)
                
            # 记录日志
            self.logger.debug(f"应用固定延迟: {self.delay:.2f}秒")
```

**code file end: crawlo/middleware/download_delay.py**

---


### code file start: crawlo/middleware/middleware_manager.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
from pprint import pformat
from types import MethodType
from asyncio import create_task
from collections import defaultdict
from typing import List, Dict, Callable, Optional, TYPE_CHECKING

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from crawlo import Request, Response
else:
    # 为 isinstance 检查导入实际的类
    from crawlo.network.request import Request
    from crawlo.network.response import Response
from crawlo.logging import get_logger
from crawlo.utils.misc import load_object
from crawlo.middleware import BaseMiddleware
from crawlo.project import common_call
from crawlo.event import CrawlerEvent
from crawlo.exceptions import MiddlewareInitError, InvalidOutputError, RequestMethodError, IgnoreRequestError, \
    NotConfiguredError


class MiddlewareManager:

    def __init__(self, crawler):
        self.crawler = crawler
        self.logger = get_logger(self.__class__.__name__)
        self.middlewares: List = []
        self.methods: Dict[str, List[MethodType]] = defaultdict(list)
        middlewares = self.crawler.settings.get_list('MIDDLEWARES')
        self._add_middleware(middlewares)
        self._add_method()

        self.download_method: Callable = crawler.engine.downloader.download
        self._stats = crawler.stats

    async def _process_request(self, request: 'Request'):
        for method in self.methods['process_request']:
            result = await common_call(method, request, self.crawler.spider)
            if result is None:
                continue
            if isinstance(result, (Request, Response)):
                return result
            raise InvalidOutputError(
                f"{method.__self__.__class__.__name__}. must return None or Request or Response, got {type(result).__name__}"
            )
        return await self.download_method(request)

    async def _process_response(self, request: 'Request', response: 'Response'):
        for method in reversed(self.methods['process_response']):
            try:
                response = await common_call(method, request, response, self.crawler.spider)
            except IgnoreRequestError as exp:
                create_task(self.crawler.subscriber.notify(CrawlerEvent.IGNORE_REQUEST, exp, request, self.crawler.spider))
            if isinstance(response, Request):
                return response
            if isinstance(response, Response):
                continue
            raise InvalidOutputError(
                f"{method.__self__.__class__.__name__}. must return Request or Response, got {type(response).__name__}"
            )
        return response

    async def _process_exception(self, request: 'Request', exp: Exception):
        for method in self.methods['process_exception']:
            response = await common_call(method, request, exp, self.crawler.spider)
            if response is None:
                continue
            if isinstance(response, (Request, Response)):
                return response
            if response:
                break
            raise InvalidOutputError(
                f"{method.__self__.__class__.__name__}. must return None or Request or Response, got {type(response).__name__}"
            )
        else:
            raise exp

    async def download(self, request) -> 'Optional[Response]':
        """ called in the download method. """
        try:
            response = await self._process_request(request)
        except KeyError:
            raise RequestMethodError(f"{request.method.lower()} is not supported")
        except IgnoreRequestError as exp:
            create_task(self.crawler.subscriber.notify(CrawlerEvent.IGNORE_REQUEST, exp, request, self.crawler.spider))
            response = await self._process_exception(request, exp)
        except Exception as exp:
            self._stats.inc_value(f'download_error/{exp.__class__.__name__}')
            response = await self._process_exception(request, exp)
        else:
            create_task(self.crawler.subscriber.notify(CrawlerEvent.RESPONSE_RECEIVED, response, self.crawler.spider))
            self._stats.inc_value('response_received_count')
        if isinstance(response, Response):
            response = await self._process_response(request, response)
        if isinstance(response, Request):
            await self.crawler.engine.enqueue_request(request)
            return None
        return response

    @classmethod
    def create_instance(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    def _add_middleware(self, middlewares):
        enabled_middlewares = [m for m in middlewares if self._validate_middleware(m)]
        if enabled_middlewares:
            # 恢复INFO级别日志，保留关键的启用信息
            self.logger.info(f'Enabled middlewares:\n {pformat(enabled_middlewares)}')

    def _validate_middleware(self, middleware):
        middleware_cls = load_object(middleware)
        if not hasattr(middleware_cls, 'create_instance'):
            raise MiddlewareInitError(
                f"Middleware init failed, must inherit from `BaseMiddleware` or have a `create_instance` method"
            )
        try:
            instance = middleware_cls.create_instance(self.crawler)
            self.middlewares.append(instance)
            return True
        except NotConfiguredError:
            return False

    def _add_method(self):
        for middleware in self.middlewares:
            if hasattr(middleware, 'process_request'):
                if self._validate_middleware_method(method_name='process_request', middleware=middleware):
                    self.methods['process_request'].append(middleware.process_request)
            if hasattr(middleware, 'process_response'):
                if self._validate_middleware_method(method_name='process_response', middleware=middleware):
                    self.methods['process_response'].append(middleware.process_response)
            if hasattr(middleware, 'process_exception'):
                if self._validate_middleware_method(method_name='process_exception', middleware=middleware):
                    self.methods['process_exception'].append(middleware.process_exception)

    @staticmethod
    def _validate_middleware_method(method_name, middleware) -> bool:
        method = getattr(type(middleware), method_name)
        base_method = getattr(BaseMiddleware, method_name)
        return False if method == base_method else True
```

**code file end: crawlo/middleware/middleware_manager.py**

---


### code file start: crawlo/middleware/offsite.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
OffsiteMiddleware 中间件
用于过滤掉不在指定域名范围内的请求
"""
import re
from urllib.parse import urlparse

from crawlo.logging import get_logger
from crawlo.exceptions import IgnoreRequestError


class OffsiteMiddleware:
    """
    OffsiteMiddleware 中间件
    用于过滤掉不在指定域名范围内的请求，防止爬虫爬取到不相关的网站
    """

    def __init__(self, stats, log_level, allowed_domains=None):
        self.logger = get_logger(self.__class__.__name__)
        self.stats = stats
        self.allowed_domains = allowed_domains or []

    @classmethod
    def create_instance(cls, crawler):
        """
        创建中间件实例
        从爬虫设置中获取允许的域名列表
        """
        # 优先使用 Spider 实例的 allowed_domains，回退到全局设置中的 ALLOWED_DOMAINS
        allowed_domains = []
        
        # 检查当前爬虫实例是否有 allowed_domains 属性
        if hasattr(crawler, 'spider') and crawler.spider and hasattr(crawler.spider, 'allowed_domains'):
            allowed_domains = getattr(crawler.spider, 'allowed_domains', [])
        
        # 如果 Spider 实例没有设置 allowed_domains，则从全局设置中获取
        if not allowed_domains:
            allowed_domains = crawler.settings.get_list('ALLOWED_DOMAINS')
        
        # 如果没有配置允许的域名，则禁用此中间件
        if not allowed_domains:
            from crawlo.exceptions import NotConfiguredError
            raise NotConfiguredError("未配置ALLOWED_DOMAINS，OffsiteMiddleware已禁用")
            
        o = cls(
            stats=crawler.stats, 
            log_level=crawler.settings.get('LOG_LEVEL'),
            allowed_domains=allowed_domains
        )
        
        # 编译域名正则表达式以提高性能
        o._compile_domains()
        
        # 使用中间件自己的logger而不是crawler.logger
        o.logger.debug(f"OffsiteMiddleware 已启用，允许的域名: {allowed_domains}")
        return o

    def _compile_domains(self):
        """
        编译域名正则表达式
        """
        self._domain_regexes = []
        for domain in self.allowed_domains:
            # 转义域名中的特殊字符
            escaped_domain = re.escape(domain)
            # 创建匹配域名的正则表达式（支持子域名）
            regex = re.compile(r'(^|.*\.)' + escaped_domain + '$', re.IGNORECASE)
            self._domain_regexes.append(regex)

    def _is_offsite_request(self, request):
        """
        判断请求是否为站外请求
        """
        try:
            parsed_url = urlparse(request.url)
            hostname = parsed_url.hostname
            
            if not hostname:
                return True  # 无效URL
                
            # 检查是否匹配允许的域名
            for regex in self._domain_regexes:
                if regex.match(hostname):
                    return False  # 匹配允许的域名
                    
            return True  # 不匹配任何允许的域名
        except Exception:
            # URL解析失败，视为站外请求
            return True

    async def process_request(self, request, spider):
        """
        处理请求，过滤站外请求
        """
        if self._is_offsite_request(request):
            # 记录被过滤的请求
            self.stats.inc_value('offsite_request_count')
            
            # 记录被过滤的域名
            try:
                parsed_url = urlparse(request.url)
                hostname = parsed_url.hostname or "unknown"
                self.stats.inc_value(f'offsite_request_count/{hostname}')
            except:
                self.stats.inc_value('offsite_request_count/invalid_url')
            
            self.logger.debug(f"过滤站外请求: {request.url}")
            
            # 抛出异常以忽略该请求
            raise IgnoreRequestError(f"站外请求被过滤: {request.url}")
            
        return None

    def process_exception(self, request, exception, spider):
        """
        处理异常
        """
        # 如果是IgnoreRequestError且是我们产生的，则处理它
        if isinstance(exception, IgnoreRequestError) and "站外请求被过滤" in str(exception):
            self.logger.debug(f"已过滤站外请求: {request.url}")
            return True  # 表示异常已被处理
        return None
```

**code file end: crawlo/middleware/offsite.py**

---


### code file start: crawlo/middleware/proxy.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
通用代理中间件
支持静态代理列表和动态代理API两种模式
"""
import random
from urllib.parse import urlparse
from typing import Optional, List

from crawlo.network import Request, Response
from crawlo.logging import get_logger


class ProxyMiddleware:
    """通用代理中间件"""

    def __init__(self, settings, log_level):
        self.logger = get_logger(self.__class__.__name__)

        # 获取代理列表和API URL
        self.proxies: List[str] = settings.get("PROXY_LIST", [])
        self.api_url = settings.get("PROXY_API_URL")
        # 获取代理提取配置
        self.proxy_extractor = settings.get("PROXY_EXTRACTOR", "proxy")  # 默认从"proxy"字段提取
        
        # 记录失败的代理，避免重复使用
        self.failed_proxies = set()
        # 最大失败次数，超过这个次数的代理将被标记为失效
        self.max_failed_attempts = settings.get("PROXY_MAX_FAILED_ATTEMPTS", 3)
        # 失效代理记录
        self.proxy_failure_count = {}
        
        # 根据配置决定启用哪种模式
        if self.proxies:
            self.mode = "static"  # 静态代理模式
            self.enabled = True
            self.logger.info(f"ProxyMiddleware enabled (static mode) with {len(self.proxies)} proxies")
        elif self.api_url:
            self.mode = "dynamic"  # 动态代理模式
            self.enabled = True
            self.logger.info(f"ProxyMiddleware enabled (dynamic mode) | API: {self.api_url}")
        else:
            self.mode = None
            self.enabled = False
            self.logger.info("ProxyMiddleware disabled (no proxy configuration)")

    @classmethod
    def create_instance(cls, crawler):
        return cls(settings=crawler.settings, log_level=crawler.settings.get("LOG_LEVEL"))

    async def _fetch_proxy_from_api(self) -> Optional[str]:
        """从代理API获取代理"""
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(self.api_url) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        # 支持多种代理提取方式
                        proxy = self._extract_proxy_from_data(data)
                        if proxy and isinstance(proxy, str) and (proxy.startswith("http://") or proxy.startswith("https://")):
                            return proxy
                    else:
                        self.logger.warning(f"Proxy API returned status {resp.status}")
        except Exception as e:
            self.logger.warning(f"Failed to fetch proxy from API: {repr(e)}")
        return None

    def _extract_proxy_from_data(self, data) -> Optional[str]:
        """
        从API返回的数据中提取代理
        
        支持多种提取方式：
        1. 字符串: 直接作为字段名使用
        2. 字典: 包含type和value字段，type支持"field"和"jsonpath"
        3. 函数: 用户自定义提取函数
        """
        if isinstance(self.proxy_extractor, str):
            # 简单字段名提取（向后兼容）
            if self.proxy_extractor in data:
                proxy_value = data[self.proxy_extractor]
                # 如果返回的是字典，尝试提取http或https字段
                if isinstance(proxy_value, dict):
                    if "http" in proxy_value:
                        return proxy_value["http"]
                    elif "https" in proxy_value:
                        return proxy_value["https"]
                return proxy_value
        elif isinstance(self.proxy_extractor, dict):
            # 复杂提取规则
            extractor_type = self.proxy_extractor.get("type", "field")
            extractor_value = self.proxy_extractor.get("value", "proxy")
            
            if extractor_type == "field":
                # 字段提取
                if extractor_value in data:
                    proxy_value = data[extractor_value]
                    # 如果返回的是字典，尝试提取http或https字段
                    if isinstance(proxy_value, dict):
                        if "http" in proxy_value:
                            return proxy_value["http"]
                        elif "https" in proxy_value:
                            return proxy_value["https"]
                    return proxy_value
            elif extractor_type == "jsonpath":
                # JSON路径提取（需要安装jsonpath库）
                try:
                    import jsonpath
                    matches = jsonpath.jsonpath(data, extractor_value)
                    if matches:
                        return matches[0]
                except ImportError:
                    self.logger.warning("jsonpath library not installed, falling back to default extraction")
                    if "proxy" in data:
                        proxy_value = data["proxy"]
                        if isinstance(proxy_value, dict):
                            if "http" in proxy_value:
                                return proxy_value["http"]
                            elif "https" in proxy_value:
                                return proxy_value["https"]
                        return proxy_value
            elif extractor_type == "custom":
                # 自定义提取函数（需要用户提供）
                custom_func = self.proxy_extractor.get("function")
                if callable(custom_func):
                    return custom_func(data)
        elif callable(self.proxy_extractor):
            # 直接调用用户提供的函数
            return self.proxy_extractor(data)
        
        # 默认提取方式（向后兼容）
        if "proxy" in data:
            proxy_value = data["proxy"]
            # 如果返回的是字典，尝试提取http或https字段
            if isinstance(proxy_value, dict):
                if "http" in proxy_value:
                    return proxy_value["http"]
                elif "https" in proxy_value:
                    return proxy_value["https"]
            return proxy_value
        
        return None

    async def process_request(self, request: Request, spider) -> Optional[Request]:
        """为请求分配代理"""
        if not self.enabled:
            return None

        if request.proxy:
            # 请求已指定代理，不覆盖
            return None

        proxy = None
        if self.mode == "static" and self.proxies:
            # 静态代理模式：随机选择一个代理，排除已知失败的代理
            available_proxies = [p for p in self.proxies if p not in self.failed_proxies]
            if available_proxies:
                proxy = random.choice(available_proxies)
            else:
                self.logger.warning("所有静态代理都已失效，将使用直连")
        elif self.mode == "dynamic" and self.api_url:
            # 动态代理模式：从API获取代理
            proxy = await self._fetch_proxy_from_api()

        if proxy:
            # 检查代理是否在失败列表中
            if proxy in self.failed_proxies:
                self.logger.warning(f"尝试使用已知失败的代理: {proxy}，但仍会尝试")
            
            request.proxy = proxy
            self.logger.debug(f"Assigned proxy {proxy} to {request.url}")
        else:
            self.logger.warning(f"No proxy available, request connecting directly: {request.url}")

        return None

    def process_response(self, request: Request, response: Response, spider) -> Response:
        """处理响应"""
        if request.proxy:
            self.logger.debug(f"Proxy request successful: {request.proxy} | {request.url}")
            # 代理请求成功，从失败列表中移除（如果存在）
            self.failed_proxies.discard(request.proxy)
            # 重置失败计数
            if request.proxy in self.proxy_failure_count:
                del self.proxy_failure_count[request.proxy]
        return response

    def process_exception(self, request: Request, exception: Exception, spider) -> Optional[Request]:
        """处理异常"""
        if request.proxy:
            error_msg = f"Proxy request failed: {request.proxy} | {request.url} | {repr(exception)}"
            self.logger.warning(error_msg)
            
            # 记录代理失败次数
            if request.proxy not in self.proxy_failure_count:
                self.proxy_failure_count[request.proxy] = 0
            self.proxy_failure_count[request.proxy] += 1
            
            # 如果失败次数超过阈值，将代理标记为失效
            if self.proxy_failure_count[request.proxy] >= self.max_failed_attempts:
                self.failed_proxies.add(request.proxy)
                self.logger.warning(f"代理 {request.proxy} 已失败 {self.max_failed_attempts} 次，标记为失效")
                
                # 从代理列表中移除（仅适用于静态代理模式）
                if self.mode == "static" and request.proxy in self.proxies:
                    self.proxies.remove(request.proxy)
                    self.logger.info(f"已从静态代理列表中移除失效代理: {request.proxy}")
        return None

```

**code file end: crawlo/middleware/proxy.py**

---


### code file start: crawlo/middleware/request_ignore.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
RequestIgnoreMiddleware 中间件
用于处理和记录被忽略的请求
"""
from crawlo.logging import get_logger
from crawlo.exceptions import IgnoreRequestError
from crawlo.event import CrawlerEvent


class RequestIgnoreMiddleware(object):
    """
    RequestIgnoreMiddleware 中间件
    用于处理和记录被忽略的请求，提供详细的统计信息
    """

    def __init__(self, stats, log_level):
        """
        初始化中间件
        
        Args:
            stats: 统计信息收集器
            log_level: 日志级别
        """
        self.logger = get_logger(self.__class__.__name__)
        self.stats = stats

    @classmethod
    def create_instance(cls, crawler):
        """
        创建中间件实例
        
        Args:
            crawler: 爬虫实例
            
        Returns:
            RequestIgnoreMiddleware: 中间件实例
        """
        o = cls(stats=crawler.stats, log_level=crawler.settings.get('LOG_LEVEL'))
        crawler.subscriber.subscribe(o.request_ignore, event=CrawlerEvent.IGNORE_REQUEST)
        return o

    async def request_ignore(self, exc, request, _spider):
        """
        处理被忽略的请求事件
        
        Args:
            exc: 异常对象
            request: 被忽略的请求
            _spider: 爬虫实例
        """
        # 记录被忽略的请求
        self.logger.info(f'请求被忽略: {request.url}')
        self.stats.inc_value('request_ignore_count')
        
        # 记录忽略原因
        reason = getattr(exc, 'msg', 'unknown')
        if reason:
            self.stats.inc_value(f'request_ignore_count/reason/{reason}')
            
        # 记录请求的域名分布
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(request.url)
            domain = parsed_url.netloc
            if domain:
                self.stats.inc_value(f'request_ignore_count/domain/{domain}')
        except Exception:
            self.stats.inc_value('request_ignore_count/domain/invalid_url')

    @staticmethod
    def process_exception(_request, exc, _spider):
        """
        处理异常，识别IgnoreRequestError
        
        Args:
            _request: 请求对象
            exc: 异常对象
            _spider: 爬虫实例
            
        Returns:
            bool: 如果是IgnoreRequestError则返回True，否则返回None
        """
        if isinstance(exc, IgnoreRequestError):
            return True
        return None
```

**code file end: crawlo/middleware/request_ignore.py**

---


### code file start: crawlo/middleware/response_code.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
ResponseCodeMiddleware 中间件
用于处理HTTP响应状态码，记录统计信息并支持特殊状态码处理
"""
from crawlo.logging import get_logger


class ResponseCodeMiddleware(object):
    """
    ResponseCodeMiddleware 中间件
    用于处理HTTP响应状态码，记录统计信息并支持特殊状态码处理
    
    功能特性:
    - 记录各种HTTP状态码的出现次数
    - 支持特殊状态码的详细处理
    - 提供详细的日志信息
    - 支持状态码分类统计(2xx, 3xx, 4xx, 5xx)
    """

    def __init__(self, stats, log_level):
        """
        初始化中间件
        
        Args:
            stats: 统计信息收集器
            log_level: 日志级别
        """
        self.logger = get_logger(self.__class__.__name__)
        self.stats = stats

    @classmethod
    def create_instance(cls, crawler):
        """
        创建中间件实例
        
        Args:
            crawler: 爬虫实例
            
        Returns:
            ResponseCodeMiddleware: 中间件实例
        """
        o = cls(stats=crawler.stats, log_level=crawler.settings.get('LOG_LEVEL'))
        return o

    def _get_status_category(self, status_code):
        """
        获取状态码分类
        
        Args:
            status_code (int): HTTP状态码
            
        Returns:
            str: 状态码分类 (2xx, 3xx, 4xx, 5xx, other)
        """
        if 200 <= status_code < 300:
            return "2xx"
        elif 300 <= status_code < 400:
            return "3xx"
        elif 400 <= status_code < 500:
            return "4xx"
        elif 500 <= status_code < 600:
            return "5xx"
        else:
            return "other"

    def _is_success_response(self, status_code):
        """
        判断是否为成功响应
        
        Args:
            status_code (int): HTTP状态码
            
        Returns:
            bool: 是否为成功响应
        """
        return 200 <= status_code < 300

    def _is_redirect_response(self, status_code):
        """
        判断是否为重定向响应
        
        Args:
            status_code (int): HTTP状态码
            
        Returns:
            bool: 是否为重定向响应
        """
        return 300 <= status_code < 400

    def _is_client_error(self, status_code):
        """
        判断是否为客户端错误
        
        Args:
            status_code (int): HTTP状态码
            
        Returns:
            bool: 是否为客户端错误
        """
        return 400 <= status_code < 500

    def _is_server_error(self, status_code):
        """
        判断是否为服务器错误
        
        Args:
            status_code (int): HTTP状态码
            
        Returns:
            bool: 是否为服务器错误
        """
        return 500 <= status_code < 600

    def process_response(self, request, response, spider):
        """
        处理响应，记录状态码统计信息
        
        Args:
            request: 请求对象
            response: 响应对象
            spider: 爬虫实例
            
        Returns:
            response: 响应对象
        """
        status_code = response.status_code
        
        # 只记录总的统计信息，不记录每个域名和每个状态码的详细信息
        # 记录状态码分类统计
        category = self._get_status_category(status_code)
        self.stats.inc_value(f'response_status_code/category/{category}')
        
        # 记录成功/失败统计
        if self._is_success_response(status_code):
            self.stats.inc_value('response_status_code/success_count')
        elif self._is_client_error(status_code) or self._is_server_error(status_code):
            self.stats.inc_value('response_status_code/error_count')
            
        # 记录响应大小统计
        if hasattr(response, 'content_length') and response.content_length:
            self.stats.inc_value('response_total_bytes', response.content_length)
        
        # 详细日志记录
        self.logger.debug(
            f'收到响应: {status_code} {response.url} '
            f'(分类: {category}, 大小: {getattr(response, "content_length", "unknown")} bytes)'
        )
        
        return response
```

**code file end: crawlo/middleware/response_code.py**

---


### code file start: crawlo/middleware/response_filter.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
ResponseFilterMiddleware 中间件
用于过滤不符合要求的HTTP响应，支持自定义允许的状态码
"""
from crawlo.logging import get_logger
from crawlo.exceptions import IgnoreRequestError


class ResponseFilterMiddleware:
    """
    ResponseFilterMiddleware 中间件
    用于过滤不符合要求的HTTP响应，支持自定义允许的状态码
    
    功能特性:
    - 默认允许2xx状态码
    - 支持自定义允许的状态码列表
    - 支持拒绝特定状态码
    - 提供详细的日志信息
    - 支持按域名配置不同的过滤规则
    """

    def __init__(self, allowed_codes, denied_codes, log_level):
        """
        初始化中间件
        
        Args:
            allowed_codes: 允许的状态码列表
            denied_codes: 拒绝的状态码列表
            log_level: 日志级别
        """
        # 确保状态码是整数类型
        self.allowed_codes = set()
        if allowed_codes:
            for code in allowed_codes:
                try:
                    self.allowed_codes.add(int(code))
                except (ValueError, TypeError):
                    pass  # 忽略无效的状态码
                    
        self.denied_codes = set()
        if denied_codes:
            for code in denied_codes:
                try:
                    self.denied_codes.add(int(code))
                except (ValueError, TypeError):
                    pass  # 忽略无效的状态码
                    
        self.logger = get_logger(self.__class__.__name__)

    @classmethod
    def create_instance(cls, crawler):
        """
        创建中间件实例
        
        Args:
            crawler: 爬虫实例
            
        Returns:
            ResponseFilterMiddleware: 中间件实例
        """
        o = cls(
            allowed_codes=crawler.settings.get_list('ALLOWED_RESPONSE_CODES'),
            denied_codes=crawler.settings.get_list('DENIED_RESPONSE_CODES'),
            log_level=crawler.settings.get('LOG_LEVEL')
        )
        return o

    def _is_response_allowed(self, response):
        """
        判断响应是否被允许
        
        Args:
            response: 响应对象
            
        Returns:
            bool: 是否被允许
        """
        status_code = response.status_code
        
        # 首先检查是否被明确拒绝
        if status_code in self.denied_codes:
            return False
            
        # 检查是否被明确允许
        if status_code in self.allowed_codes:
            return True
            
        # 默认允许2xx状态码
        if 200 <= status_code < 300:
            return True
            
        # 默认拒绝其他状态码
        return False

    def _get_filter_reason(self, status_code):
        """
        获取过滤原因描述
        
        Args:
            status_code (int): HTTP状态码
            
        Returns:
            str: 过滤原因描述
        """
        if status_code in self.denied_codes:
            return f"状态码 {status_code} 被明确拒绝"
        elif status_code not in self.allowed_codes and not (200 <= status_code < 300):
            return f"状态码 {status_code} 不在允许列表中"
        else:
            return f"状态码 {status_code} 被过滤"

    def process_response(self, request, response, spider):
        """
        处理响应，过滤不符合要求的响应
        
        Args:
            request: 请求对象
            response: 响应对象
            spider: 爬虫实例
            
        Returns:
            response: 响应对象（如果被允许）
            
        Raises:
            IgnoreRequestError: 如果响应被过滤
        """
        if self._is_response_allowed(response):
            return response
            
        # 响应被过滤
        reason = self._get_filter_reason(response.status_code)
        self.logger.debug(f"过滤响应: {response.status_code} {response.url} - {reason}")
        
        # 抛出异常以忽略该响应
        raise IgnoreRequestError(f"response filtered: {reason} - {response.status_code} {response.url}")
```

**code file end: crawlo/middleware/response_filter.py**

---


### code file start: crawlo/middleware/retry.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
import asyncio
from typing import List

try:
    from anyio import EndOfStream
except ImportError:
    # 如果 anyio 不可用或者 EndOfStream 不存在，创建一个占位符
    class EndOfStream(Exception):
        pass

try:
    from httpcore import ReadError
except ImportError:
    class ReadError(Exception):
        pass

try:
    from httpx import RemoteProtocolError, ConnectError, ReadTimeout
except ImportError:
    class RemoteProtocolError(Exception):
        pass
    class ConnectError(Exception):
        pass
    class ReadTimeout(Exception):
        pass

try:
    from aiohttp.client_exceptions import ClientConnectionError, ClientPayloadError
    from aiohttp import ClientConnectorError, ClientTimeout, ClientConnectorSSLError, ClientResponseError
except ImportError:
    class ClientConnectionError(Exception):
        pass
    class ClientPayloadError(Exception):
        pass
    class ClientConnectorError(Exception):
        pass
    class ClientTimeout(Exception):
        pass
    class ClientConnectorSSLError(Exception):
        pass
    class ClientResponseError(Exception):
        pass

from crawlo.logging import get_logger
from crawlo.stats_collector import StatsCollector

_retry_exceptions = [
    EndOfStream,
    ReadError,
    asyncio.TimeoutError,
    ConnectError,
    ReadTimeout,
    ClientConnectorError,
    ClientResponseError,
    RemoteProtocolError,
    ClientTimeout,
    ClientConnectorSSLError,
    ClientPayloadError,
    ClientConnectionError
]


class RetryMiddleware(object):

    def __init__(
            self,
            *,
            retry_http_codes: List,
            ignore_http_codes: List,
            max_retry_times: int,
            retry_exceptions: List,
            stats: StatsCollector,
            retry_priority: int
    ):
        self.retry_http_codes = retry_http_codes
        self.ignore_http_codes = ignore_http_codes
        self.max_retry_times = max_retry_times
        self.retry_exceptions = tuple(retry_exceptions + _retry_exceptions)
        self.retry_priority = retry_priority
        self.stats = stats
        self.logger = get_logger(self.__class__.__name__)

    @classmethod
    def create_instance(cls, crawler):
        o = cls(
            retry_http_codes=crawler.settings.get_list('RETRY_HTTP_CODES'),
            ignore_http_codes=crawler.settings.get_list('IGNORE_HTTP_CODES'),
            max_retry_times=crawler.settings.get_int('MAX_RETRY_TIMES'),
            retry_exceptions=crawler.settings.get_list('RETRY_EXCEPTIONS'),
            stats=crawler.stats,
            retry_priority=crawler.settings.get_int('RETRY_PRIORITY')
        )
        return o

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status_code in self.ignore_http_codes:
            return response
        if response.status_code in self.retry_http_codes:
            # 重试逻辑
            reason = f"response code {response.status_code}"
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exc, spider):
        if isinstance(exc, self.retry_exceptions) and not request.meta.get('dont_retry', False):
            return self._retry(request=request, reason=type(exc).__name__, spider=spider)

    def _retry(self, request, reason, spider):
        retry_times = request.meta.get('retry_times', 0)
        if retry_times < self.max_retry_times:
            retry_times += 1
            self.logger.info(f"{spider} {request} {reason} retrying {retry_times} time...")
            request.meta['retry_times'] = retry_times
            # request.dont_retry = True
            request.meta['dont_retry'] = True
            request.priority = request.priority + self.retry_priority
            self.stats.inc_value("retry_count")
            return request
        else:
            self.logger.warning(f"{spider} {request} {reason} retry max {self.max_retry_times} times, give up.")
            return None
```

**code file end: crawlo/middleware/retry.py**

---


### code file start: crawlo/middleware/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from crawlo import Request, Response


class BaseMiddleware:
    """中间件基类
    
    定义了中间件的标准接口，所有自定义中间件都应该继承此类。
    
    中间件处理流程：
    1. process_request: 请求发送前处理
    2. process_response: 响应接收后处理
    3. process_exception: 异常发生时处理
    """
    
    def process_request(
        self, 
        request: 'Request', 
        spider
    ) -> Optional[Union['Request', 'Response']]:
        """处理请求
        
        Args:
            request: 待处理的请求对象
            spider: 当前爬虫实例
            
        Returns:
            None: 继续处理
            Request: 替换原请求
            Response: 跳过下载，直接返回响应
        """
        pass

    def process_response(
        self, 
        request: 'Request', 
        response: 'Response', 
        spider
    ) -> Union['Request', 'Response']:
        """处理响应
        
        Args:
            request: 原始请求对象
            response: 接收到的响应对象
            spider: 当前爬虫实例
            
        Returns:
            Request: 重新发起请求
            Response: 返回响应（可能是修改后的）
        """
        return response

    def process_exception(
        self, 
        request: 'Request', 
        exp: Exception, 
        spider
    ) -> Optional[Union['Request', 'Response']]:
        """处理异常
        
        Args:
            request: 发生异常的请求
            exp: 捕获的异常对象
            spider: 当前爬虫实例
            
        Returns:
            None: 继续传递异常
            Request: 重新发起请求
            Response: 返回响应
        """
        pass

    @classmethod
    def create_instance(cls, crawler):
        """创建中间件实例
        
        Args:
            crawler: Crawler实例，包含settings等配置
            
        Returns:
            中间件实例
        """
        return cls()

```

**code file end: crawlo/middleware/__init__.py**

---


### code file start: crawlo/network/request.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
HTTP Request 封装模块
====================
提供功能完善的HTTP请求封装，支持:
- JSON/表单数据自动处理
- GET请求参数处理
- 优先级排序机制
- 安全的深拷贝操作
- 灵活的请求配置
"""
import json
from copy import deepcopy
from enum import IntEnum
from w3lib.url import safe_url_string
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl
from typing import Dict, Optional, Callable, Union, Any, TypeVar, List

from crawlo.utils.url_utils import escape_ajax


_Request = TypeVar("_Request", bound="Request")


class RequestPriority(IntEnum):
    """
    请求优先级枚举。
    
    数值越小，优先级越高。使用 IntEnum 确保可以直接当作整数使用。
    
    Examples:
        >>> request = Request(url, priority=RequestPriority.HIGH)
        >>> request.priority = RequestPriority.URGENT
    """
    URGENT = -200      # 紧急任务
    HIGH = -100        # 高优先级  
    NORMAL = 0         # 正常优先级(默认)
    LOW = 100          # 低优先级
    BACKGROUND = 200   # 后台任务


class Request:
    """
    封装一个 HTTP 请求对象，用于爬虫框架中表示一个待抓取的请求任务。
    支持 JSON、表单、GET参数、原始 body 提交，自动处理 Content-Type 与编码。
    不支持文件上传（multipart/form-data），保持轻量。
    """

    __slots__ = (
        '_url',
        '_meta',
        'callback',
        'cb_kwargs',
        'err_back',
        'headers',
        'body',
        'method',
        'cookies',
        'priority',
        'encoding',
        'dont_filter',
        'timeout',
        'proxy',
        'allow_redirects',
        'auth',
        'verify',
        'flags',
        '_json_body',
        '_form_data',
        '_params',
        'use_dynamic_loader',
        'dynamic_loader_options'
    )

    def __init__(
        self,
        url: str,
        callback: Optional[Callable] = None,
        err_back: Optional[Callable] = None,
        method: Optional[str] = 'GET',
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Union[bytes, str, Dict[Any, Any]]] = None,
        form_data: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        cb_kwargs: Optional[Dict[str, Any]] = None,
        cookies: Optional[Dict[str, str]] = None,
        meta: Optional[Dict[str, Any]] = None,
        priority: int = RequestPriority.NORMAL,
        dont_filter: bool = False,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        allow_redirects: bool = True,
        auth: Optional[tuple] = None,
        verify: bool = True,
        flags: Optional[List[str]] = None,
        encoding: str = 'utf-8',
        # 动态加载相关参数
        use_dynamic_loader: bool = False,
        dynamic_loader_options: Optional[Dict[str, Any]] = None
    ):
        """
        初始化请求对象。

        :param url: 请求 URL（必须）
        :param callback: 成功回调函数
        :param err_back: 错误回调函数
        :param method: HTTP 方法，默认 GET
        :param headers: 请求头
        :param body: 原始请求体（bytes/str），若为 dict 且未使用 json_body/form_data，则自动转为 JSON
        :param form_data: 表单数据，POST请求时自动转为 application/x-www-form-urlencoded
        :param json_body: JSON 数据，自动序列化并设置 Content-Type
        :param params: GET请求参数，会自动附加到URL上
        :param cb_kwargs: 传递给 callback 的额外参数
        :param cookies: Cookies 字典
        :param meta: 元数据（跨中间件传递数据）
        :param priority: 优先级（数值越小越优先）
        :param dont_filter: 是否跳过去重
        :param timeout: 超时时间（秒）
        :param proxy: 代理地址，如 http://127.0.0.1:8080
        :param allow_redirects: 是否允许重定向
        :param auth: 认证元组 (username, password)
        :param verify: 是否验证 SSL 证书
        :param flags: 标记（用于调试或分类）
        :param encoding: 字符编码，默认 utf-8
        """
        self.callback = callback
        self.err_back = err_back
        self.method = str(method).upper()
        self.headers = headers or {}
        self.cookies = cookies or {}
        self.priority = -priority  # 用于排序：值越小优先级越高
        
        # 安全处理 meta，移除 logger 后再 deepcopy
        self._meta = self._safe_deepcopy_meta(meta) if meta is not None else {}
        
        self.timeout = self._meta.get('download_timeout', timeout)
        self.proxy = proxy
        self.allow_redirects = allow_redirects
        self.auth = auth
        self.verify = verify
        self.flags = flags or []
        self.encoding = encoding
        self.cb_kwargs = cb_kwargs or {}
        self.body = body
        # 保存高层语义参数（用于 copy）
        self._json_body = json_body
        self._form_data = form_data
        self._params = params
        
        # 动态加载相关属性
        self.use_dynamic_loader = use_dynamic_loader
        self.dynamic_loader_options = dynamic_loader_options or {}

        # 处理GET参数
        if params is not None and self.method == 'GET':
            # 将GET参数附加到URL上
            self._url = self._add_params_to_url(url, params)
        else:
            self._url = url

        # 构建 body
        if json_body is not None:
            if 'Content-Type' not in self.headers:
                self.headers['Content-Type'] = 'application/json'
            self.body = json.dumps(json_body, ensure_ascii=False).encode(encoding)
            if self.method == 'GET':
                self.method = 'POST'

        elif form_data is not None:
            if self.method == 'GET':
                # 对于GET请求，将form_data作为GET参数处理
                self._url = self._add_params_to_url(self._url, form_data)
            else:
                # 对于POST等请求，将form_data作为请求体处理
                if 'Content-Type' not in self.headers:
                    self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
                query_str = urlencode(form_data)
                self.body = query_str.encode(encoding)  # 显式编码为 bytes


        else:
            # 处理原始 body
            if isinstance(self.body, dict):
                if 'Content-Type' not in self.headers:
                    self.headers['Content-Type'] = 'application/json'
                self.body = json.dumps(self.body, ensure_ascii=False).encode(encoding)
            elif isinstance(self.body, str):
                self.body = self.body.encode(encoding)

        self.dont_filter = dont_filter
        self._set_url(self._url)

    @staticmethod
    def _add_params_to_url(url: str, params: Dict[str, Any]) -> str:
        """将参数添加到URL中"""
        if not params:
            return url
            
        # 解析URL
        parsed = urlparse(url)
        # 解析现有查询参数
        query_params = parse_qsl(parsed.query, keep_blank_values=True)
        # 添加新参数
        for key, value in params.items():
            query_params.append((str(key), str(value)))
        # 重新构建查询字符串
        new_query = urlencode(query_params)
        # 构建新的URL
        return urlunparse((
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            new_query,
            parsed.fragment
        ))

    @staticmethod
    def _safe_deepcopy_meta(meta: Dict[str, Any]) -> Dict[str, Any]:
        """安全地 deepcopy meta，移除 logger 后再复制"""
        import logging
        
        def clean_logger_recursive(obj: Any) -> Any:
            """递归移除 logger 对象"""
            if isinstance(obj, logging.Logger):
                return None
            elif isinstance(obj, dict):
                cleaned = {}
                for k, v in obj.items():
                    if not (k == 'logger' or isinstance(v, logging.Logger)):
                        cleaned[k] = clean_logger_recursive(v)
                return cleaned
            elif isinstance(obj, (list, tuple)):
                cleaned_list = []
                for item in obj:
                    cleaned_item = clean_logger_recursive(item)
                    if cleaned_item is not None:
                        cleaned_list.append(cleaned_item)
                return type(obj)(cleaned_list)
            else:
                return obj
        
        # 先清理 logger，再 deepcopy
        cleaned_meta = clean_logger_recursive(meta)
        # 确保返回字典类型
        if not isinstance(cleaned_meta, dict):
            return {}
        return deepcopy(cleaned_meta)

    def copy(self: _Request) -> _Request:
        """
        创建当前请求的副本，保留所有高层语义（json_body/form_data/params）。
        """
        return type(self)(
            url=self.url,
            callback=self.callback,
            method=self.method,
            headers=self.headers.copy(),
            body=None,  # 由 form_data/json_body/params 重新生成
            form_data=self._form_data,
            json_body=self._json_body,
            params=self._params,
            cb_kwargs=deepcopy(self.cb_kwargs),
            err_back=self.err_back,
            cookies=self.cookies.copy(),
            meta=deepcopy(self._meta),
            priority=-self.priority,
            dont_filter=self.dont_filter,
            timeout=self.timeout,
            proxy=self.proxy,
            allow_redirects=self.allow_redirects,
            auth=self.auth,
            verify=self.verify,
            flags=self.flags.copy(),
            encoding=self.encoding,
            use_dynamic_loader=self.use_dynamic_loader,
            dynamic_loader_options=deepcopy(self.dynamic_loader_options)
        )

    def set_meta(self, key: str, value: Any) -> 'Request':
        """设置 meta 中的某个键值，支持链式调用。"""
        self._meta[key] = value
        return self
    
    def add_header(self, key: str, value: str) -> 'Request':
        """添加请求头，支持链式调用。"""
        self.headers[key] = value
        return self
    
    def add_headers(self, headers: Dict[str, str]) -> 'Request':
        """批量添加请求头，支持链式调用。"""
        self.headers.update(headers)
        return self
    
    def set_proxy(self, proxy: str) -> 'Request':
        """设置代理，支持链式调用。"""
        self.proxy = proxy
        return self
    
    def set_timeout(self, timeout: float) -> 'Request':
        """设置超时时间，支持链式调用。"""
        self.timeout = timeout
        return self
    
    def add_flag(self, flag: str) -> 'Request':
        """添加标记，支持链式调用。"""
        if flag not in self.flags:
            self.flags.append(flag)
        return self
    
    def remove_flag(self, flag: str) -> 'Request':
        """移除标记，支持链式调用。"""
        if flag in self.flags:
            self.flags.remove(flag)
        return self
    
    def set_dynamic_loader(self, use_dynamic: bool = True, options: Optional[Dict[str, Any]] = None) -> 'Request':
        """设置使用动态加载器，支持链式调用。"""
        self.use_dynamic_loader = use_dynamic
        if options:
            self.dynamic_loader_options = options
        # 同时在meta中设置标记，供混合下载器使用
        self._meta['use_dynamic_loader'] = use_dynamic
        return self
    
    def set_protocol_loader(self) -> 'Request':
        """强制使用协议加载器，支持链式调用。"""
        self.use_dynamic_loader = False
        self._meta['use_dynamic_loader'] = False
        self._meta['use_protocol_loader'] = True
        return self

    def _set_url(self, url: str) -> None:
        """安全设置 URL，确保格式正确。"""
        if not isinstance(url, str):
            raise TypeError(f"Request url 必须为字符串，当前类型: {type(url).__name__}")
        
        if not url.strip():
            raise ValueError("URL 不能为空")
        
        # 检查危险的 URL scheme
        dangerous_schemes = ['file://', 'ftp://', 'javascript:', 'data:']
        if any(url.lower().startswith(scheme) for scheme in dangerous_schemes):
            raise ValueError(f"URL scheme 不安全: {url[:20]}...")

        s = safe_url_string(url, self.encoding)
        escaped_url = escape_ajax(s)
        
        if not escaped_url.startswith(('http://', 'https://')):
            raise ValueError(f"URL 缺少 HTTP(S) scheme: {escaped_url[:50]}...")
        
        # 检查 URL 长度
        if len(escaped_url) > 8192:  # 大多数服务器支持的最大 URL 长度
            raise ValueError(f"URL 过长 (超过 8192 字符): {len(escaped_url)} 字符")
        
        self._url = escaped_url

    @property
    def url(self) -> str:
        return self._url

    @property
    def meta(self) -> Dict[str, Any]:
        return self._meta

    def __str__(self) -> str:
        return f'<Request url={self.url} method={self.method}>'

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other: _Request) -> bool:
        """用于按优先级排序"""
        return self.priority < other.priority
```

**code file end: crawlo/network/request.py**

---


### code file start: crawlo/network/response.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
HTTP Response 封装模块
=====================
提供功能丰富的HTTP响应封装，支持:
- 智能编码检测和解码
- XPath/CSS 选择器
- JSON 解析和缓存
- 正则表达式支持
- Cookie 处理
"""
import re
from http.cookies import SimpleCookie
from typing import Dict, Any, List, Optional, Tuple
from urllib.parse import urljoin as _urljoin, urlparse as _urlparse, urlsplit as _urlsplit, parse_qs as _parse_qs, \
    urlencode as _urlencode, quote as _quote, unquote as _unquote, urldefrag as _urldefrag

import ujson
from parsel import Selector, SelectorList

# 尝试导入 w3lib 编码检测函数
try:
    from w3lib.encoding import (
        html_body_declared_encoding,
        html_to_unicode,
        http_content_type_encoding,
        read_bom,
        resolve_encoding,
    )
    W3LIB_AVAILABLE = True
except ImportError:
    W3LIB_AVAILABLE = False

from crawlo.exceptions import DecodeError
from crawlo.utils import (
    extract_text,
    extract_texts,
    extract_attr,
    extract_attrs,
    is_xpath
)


def memoize_method_noargs(func):
    """
    装饰器，用于缓存无参数方法的结果
    """
    cache_attr = f'_cache_{func.__name__}'
    
    def wrapper(self):
        if not hasattr(self, cache_attr):
            setattr(self, cache_attr, func(self))
        return getattr(self, cache_attr)
    
    return wrapper


class Response:
    """
    HTTP响应的封装，提供数据解析的便捷方法。
    
    功能特性:
    - 智能编码检测和缓存
    - 懒加载 Selector 实例
    - JSON 解析和缓存
    - 多类型数据提取
    """

    # 默认编码
    _DEFAULT_ENCODING = "ascii"

    def __init__(
            self,
            url: str,
            *,
            headers: Dict[str, Any] = None,
            body: bytes = b"",
            method: str = 'GET',
            request: 'Request' = None,  # 使用字符串注解避免循环导入
            status_code: int = 200,
    ):
        # 基本属性
        self.url = url
        self.headers = headers or {}
        self.body = body
        self.method = method.upper()
        self.request = request
        self.status_code = status_code

        # 编码处理
        self.encoding = self._determine_encoding()

        # 缓存属性
        self._text_cache = None
        self._json_cache = None
        self._selector_instance = None

        # 状态标记
        self._is_success = 200 <= status_code < 300
        self._is_redirect = 300 <= status_code < 400
        self._is_client_error = 400 <= status_code < 500
        self._is_server_error = status_code >= 500

    # ==================== 编码检测相关方法 ====================
    
    def _determine_encoding(self) -> str:
        """
        智能检测响应编码
        
        编码检测优先级：
        1. Request 中指定的编码
        2. BOM 字节顺序标记
        3. HTTP Content-Type 头部
        4. HTML meta 标签声明
        5. 内容自动检测
        6. 默认编码 (utf-8)
        """
        # 1. 优先使用声明的编码
        declared_encoding = self._declared_encoding()
        if declared_encoding:
            return declared_encoding
            
        # 2. 使用 w3lib 进行编码检测（如果可用）
        if W3LIB_AVAILABLE:
            return self._body_inferred_encoding()
        else:
            # 如果 w3lib 不可用，使用原有的检测逻辑
            # 从 Content-Type 头中检测
            content_type = self.headers.get("content-type", "") or self.headers.get("Content-Type", "")
            if content_type:
                charset_match = re.search(r"charset=([\w-]+)", content_type, re.I)
                if charset_match:
                    return charset_match.group(1).lower()

            # 从 HTML meta 标签中检测(仅对HTML内容)
            if b'<html' in self.body[:1024].lower():
                # 查找 <meta charset="xxx"> 或 <meta http-equiv="Content-Type" content="...charset=xxx">
                html_start = self.body[:4096]  # 只检查前4KB
                try:
                    html_text = html_start.decode('ascii', errors='ignore')
                    # <meta charset="utf-8">
                    charset_match = re.search(r'<meta[^>]+charset=["\']?([\w-]+)', html_text, re.I)
                    if charset_match:
                        return charset_match.group(1).lower()

                    # <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    content_match = re.search(r'<meta[^>]+content=["\'][^"\'>]*charset=([\w-]+)', html_text, re.I)
                    if content_match:
                        return content_match.group(1).lower()
                except Exception:
                    pass

        # 3. 默认使用 utf-8
        return 'utf-8'

    def _declared_encoding(self) -> Optional[str]:
        """
        获取声明的编码
        优先级：Request编码 > BOM > HTTP头部 > HTML meta标签
        """
        # 1. Request 中指定的编码
        if self.request and getattr(self.request, 'encoding', None):
            return self.request.encoding
            
        # 2. BOM 字节顺序标记
        bom_encoding = self._bom_encoding()
        if bom_encoding:
            return bom_encoding
            
        # 3. HTTP Content-Type 头部
        headers_encoding = self._headers_encoding()
        if headers_encoding:
            return headers_encoding
            
        # 4. HTML meta 标签声明编码
        body_declared_encoding = self._body_declared_encoding()
        if body_declared_encoding:
            return body_declared_encoding
            
        return None

    @memoize_method_noargs
    def _bom_encoding(self) -> Optional[str]:
        """BOM 字节顺序标记编码检测"""
        if not W3LIB_AVAILABLE:
            return None
        return read_bom(self.body)[0]

    @memoize_method_noargs
    def _headers_encoding(self) -> Optional[str]:
        """HTTP Content-Type 头部编码检测"""
        if not W3LIB_AVAILABLE:
            return None
        content_type = self.headers.get(b"Content-Type", b"") or self.headers.get("content-type", b"")
        if isinstance(content_type, bytes):
            content_type = content_type.decode('latin-1')
        return http_content_type_encoding(content_type)

    @memoize_method_noargs
    def _body_declared_encoding(self) -> Optional[str]:
        """HTML meta 标签声明编码检测"""
        if not W3LIB_AVAILABLE:
            return None
        return html_body_declared_encoding(self.body)

    @memoize_method_noargs
    def _body_inferred_encoding(self) -> str:
        """内容自动检测编码"""
        if not W3LIB_AVAILABLE:
            # 回退到简单的自动检测
            for enc in (self._DEFAULT_ENCODING, "utf-8", "cp1252"):
                try:
                    self.body.decode(enc)
                except UnicodeError:
                    continue
                return enc
            return self._DEFAULT_ENCODING

        content_type = self.headers.get(b"Content-Type", b"") or self.headers.get("content-type", b"")
        if isinstance(content_type, bytes):
            content_type = content_type.decode('latin-1')
        
        # 使用 w3lib 的 html_to_unicode 函数进行编码检测
        benc, _ = html_to_unicode(
            content_type,
            self.body,
            auto_detect_fun=self._auto_detect_fun,
            default_encoding=self._DEFAULT_ENCODING,
        )
        return benc

    def _auto_detect_fun(self, text: bytes) -> Optional[str]:
        """自动检测编码的回调函数"""
        if not W3LIB_AVAILABLE:
            return None
        for enc in (self._DEFAULT_ENCODING, "utf-8", "cp1252"):
            try:
                text.decode(enc)
            except UnicodeError:
                continue
            return resolve_encoding(enc)
        return None

    @property
    def text(self) -> str:
        """将响应体(body)以正确的编码解码为字符串，并缓存结果。"""
        if self._text_cache is not None:
            return self._text_cache

        if not self.body:
            self._text_cache = ""
            return self._text_cache

        # 如果可用，使用 w3lib 进行更准确的解码
        if W3LIB_AVAILABLE:
            try:
                content_type = self.headers.get(b"Content-Type", b"") or self.headers.get("content-type", b"")
                if isinstance(content_type, bytes):
                    content_type = content_type.decode('latin-1')
                
                # 使用 w3lib 的 html_to_unicode 函数
                _, self._text_cache = html_to_unicode(
                    content_type,
                    self.body,
                    default_encoding=self.encoding
                )
                return self._text_cache
            except Exception:
                # 如果 w3lib 解码失败，回退到原有方法
                pass

        # 尝试多种编码
        encodings_to_try = [self.encoding]
        if self.encoding != 'utf-8':
            encodings_to_try.append('utf-8')
        if 'gbk' not in encodings_to_try:
            encodings_to_try.append('gbk')
        if 'gb2312' not in encodings_to_try:
            encodings_to_try.append('gb2312')
        encodings_to_try.append('latin1')  # 最后的回退选项

        for encoding in encodings_to_try:
            if not encoding:
                continue
            try:
                self._text_cache = self.body.decode(encoding)
                return self._text_cache
            except (UnicodeDecodeError, LookupError):
                continue

        # 所有编码都失败，使用容错解码
        try:
            self._text_cache = self.body.decode('utf-8', errors='replace')
            return self._text_cache
        except Exception as e:
            raise DecodeError(f"Failed to decode response from {self.url}: {e}")

    # ==================== 状态检查相关属性 ====================
    
    @property
    def is_success(self) -> bool:
        """检查响应是否成功 (2xx)"""
        return self._is_success

    @property
    def is_redirect(self) -> bool:
        """检查响应是否为重定向 (3xx)"""
        return self._is_redirect

    @property
    def is_client_error(self) -> bool:
        """检查响应是否为客户端错误 (4xx)"""
        return self._is_client_error

    @property
    def is_server_error(self) -> bool:
        """检查响应是否为服务器错误 (5xx)"""
        return self._is_server_error

    # ==================== 响应头相关属性 ====================
    
    @property
    def content_type(self) -> str:
        """获取响应的 Content-Type"""
        return self.headers.get('content-type', '') or self.headers.get('Content-Type', '')

    @property
    def content_length(self) -> Optional[int]:
        """获取响应的 Content-Length"""
        length = self.headers.get('content-length') or self.headers.get('Content-Length')
        return int(length) if length else None

    # ==================== JSON处理方法 ====================
    
    def json(self, default: Any = None) -> Any:
        """将响应文本解析为 JSON 对象。"""
        if self._json_cache is not None:
            return self._json_cache

        try:
            self._json_cache = ujson.loads(self.text)
            return self._json_cache
        except (ujson.JSONDecodeError, ValueError) as e:
            if default is not None:
                return default
            raise DecodeError(f"Failed to parse JSON from {self.url}: {e}")

    # ==================== URL处理方法 ====================
    
    def urljoin(self, url: str) -> str:
        """拼接 URL，自动处理相对路径。"""
        return _urljoin(self.url, url)

    # ==================== 选择器相关方法 ====================

    @property
    def _selector(self) -> Selector:
        """懒加载 Selector 实例"""
        if self._selector_instance is None:
            self._selector_instance = Selector(self.text)
        return self._selector_instance

    def xpath(self, query: str) -> SelectorList:
        """使用 XPath 选择器查询文档。"""
        return self._selector.xpath(query)

    def css(self, query: str) -> SelectorList:
        """使用 CSS 选择器查询文档。"""
        return self._selector.css(query)

    def _is_xpath(self, query: str) -> bool:
        """判断查询语句是否为XPath"""
        return is_xpath(query)

    def _extract_text(self, elements: SelectorList, join_str: str = " ") -> str:
        """
        从元素列表中提取文本并拼接
        
        :param elements: SelectorList元素列表
        :param join_str: 文本拼接分隔符
        :return: 拼接后的文本
        """
        return extract_text(elements, join_str)

    def extract_text(self, xpath_or_css: str, join_str: str = " ", default: str = '') -> str:
        """
        提取单个元素的文本内容，支持CSS和XPath选择器

        参数:
            xpath_or_css: XPath或CSS选择器
            join_str: 文本拼接分隔符(默认为空格)
            default: 默认返回值，当未找到元素时返回

        返回:
            拼接后的纯文本字符串
            
        示例:
            # 使用CSS选择器
            title = response.extract_text('title')
            content = response.extract_text('.content p', join_str=' ')
            
            # 使用XPath选择器
            title = response.extract_text('//title')
            content = response.extract_text('//div[@class="content"]//p', join_str=' ')
        """
        try:
            elements = self.xpath(xpath_or_css) if self._is_xpath(xpath_or_css) else self.css(xpath_or_css)
            if not elements:
                return default
            return self._extract_text(elements, join_str)
        except Exception:
            return default

    def extract_texts(self, xpath_or_css: str, join_str: str = " ", default: List[str] = None) -> List[str]:
        """
        提取多个元素的文本内容列表，支持CSS和XPath选择器

        参数:
            xpath_or_css: XPath或CSS选择器
            join_str: 单个节点内文本拼接分隔符
            default: 默认返回值，当未找到元素时返回

        返回:
            纯文本列表(每个元素对应一个节点的文本)
            
        示例:
            # 使用CSS选择器
            paragraphs = response.extract_texts('.content p')
            titles = response.extract_texts('h1, h2, h3')
            
            # 使用XPath选择器
            paragraphs = response.extract_texts('//div[@class="content"]//p')
            titles = response.extract_texts('//h1 | //h2 | //h3')
        """
        if default is None:
            default = []
            
        try:
            elements = self.xpath(xpath_or_css) if self._is_xpath(xpath_or_css) else self.css(xpath_or_css)
            if not elements:
                return default
                
            result = extract_texts(elements, join_str)
            return result if result else default
        except Exception:
            return default

    def extract_attr(self, xpath_or_css: str, attr_name: str, default: Any = None) -> Any:
        """
        提取单个元素的属性值，支持CSS和XPath选择器

        参数:
            xpath_or_css: XPath或CSS选择器
            attr_name: 属性名称
            default: 默认返回值

        返回:
            属性值或默认值
            
        示例:
            # 使用CSS选择器
            link_href = response.extract_attr('a', 'href')
            img_src = response.extract_attr('.image', 'src')
            
            # 使用XPath选择器
            link_href = response.extract_attr('//a[@class="link"]', 'href')
            img_src = response.extract_attr('//img[@alt="example"]', 'src')
        """
        try:
            elements = self.xpath(xpath_or_css) if self._is_xpath(xpath_or_css) else self.css(xpath_or_css)
            if not elements:
                return default
            return extract_attr(elements, attr_name, default)
        except Exception:
            return default

    def extract_attrs(self, xpath_or_css: str, attr_name: str, default: List[Any] = None) -> List[Any]:
        """
        提取多个元素的属性值列表，支持CSS和XPath选择器

        参数:
            xpath_or_css: XPath或CSS选择器
            attr_name: 属性名称
            default: 默认返回值

        返回:
            属性值列表
            
        示例:
            # 使用CSS选择器
            links = response.extract_attrs('a', 'href')
            images = response.extract_attrs('img', 'src')
            
            # 使用XPath选择器
            links = response.extract_attrs('//a[@class="link"]', 'href')
            images = response.extract_attrs('//img[@alt]', 'src')
        """
        if default is None:
            default = []
            
        try:
            elements = self.xpath(xpath_or_css) if self._is_xpath(xpath_or_css) else self.css(xpath_or_css)
            if not elements:
                return default
                
            result = extract_attrs(elements, attr_name)
            return result if result else default
        except Exception:
            return default

    # ==================== 正则表达式相关方法 ====================
    
    def re_search(self, pattern: str, flags: int = re.DOTALL) -> Optional[re.Match]:
        """在响应文本上执行正则表达式搜索。"""
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        return re.search(pattern, self.text, flags=flags)

    def re_findall(self, pattern: str, flags: int = re.DOTALL) -> List[Any]:
        """在响应文本上执行正则表达式查找。"""
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        return re.findall(pattern, self.text, flags=flags)

    # ==================== Cookie处理方法 ====================
    
    def get_cookies(self) -> Dict[str, str]:
        """从响应头中解析并返回Cookies。"""
        cookie_header = self.headers.get("Set-Cookie", "")
        if isinstance(cookie_header, list):
            cookie_header = ", ".join(cookie_header)
        cookies = SimpleCookie()
        cookies.load(cookie_header)
        return {key: morsel.value for key, morsel in cookies.items()}

    # ==================== 请求相关方法 ====================
    
    def follow(self, url: str, callback=None, **kwargs):
        """
        创建一个跟随链接的请求。
        
        Args:
            url: 要跟随的URL（可以是相对URL）
            callback: 回调函数
            **kwargs: 传递给Request的其他参数
            
        Returns:
            Request: 新的请求对象
        """
        # 延迟导入Request以避免循环导入
        from ..network.request import Request
        
        # 使用urljoin处理相对URL
        absolute_url = self.urljoin(url)
        
        # 创建新的请求
        return Request(
            url=absolute_url,
            callback=callback or getattr(self.request, 'callback', None),
            **kwargs
        )

    @property
    def meta(self) -> Dict:
        """获取关联的 Request 对象的 meta 字典。"""
        return self.request.meta if self.request else {}

    def __str__(self):
        return f"<{self.status_code} {self.url}>"
```

**code file end: crawlo/network/response.py**

---


### code file start: crawlo/network/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Crawlo Network Module
====================
提供HTTP请求和响应对象的封装。

主要组件:
- Request: HTTP请求封装
- Response: HTTP响应封装
- RequestPriority: 请求优先级常量
"""

from .request import Request, RequestPriority
from .response import Response

__all__ = [
    'Request',
    'RequestPriority', 
    'Response',
]

```

**code file end: crawlo/network/__init__.py**

---


### code file start: crawlo/pipelines/base_pipeline.py 

```python
# -*- coding: utf-8 -*-
"""
Pipeline基类 - 提供统一的资源管理
====================================

Pipeline体系说明：
- BasePipeline: 基础抽象类，定义Pipeline接口规范
- ResourceManagedPipeline: 提供资源管理功能的基类（推荐）
- FileBasedPipeline: 文件操作专用基类
- DatabasePipeline: 数据库操作专用基类
- CacheBasedPipeline: 缓存操作专用基类

与 PipelineManager 的关系：
- base_pipeline.py: 定义单个Pipeline的实现规范（本文件）
- pipeline_manager.py: 协调多个Pipeline的执行流程
- 两者分工明确，互相配合，不是重复设计

使用方法:
    # 简单场景 - 直接继承BasePipeline
    class SimplePipeline(BasePipeline):
        @classmethod
        def from_crawler(cls, crawler):
            return cls()
        
        async def process_item(self, item, spider):
            return item
    
    # 复杂场景 - 使用ResourceManagedPipeline（推荐）
    class MyPipeline(ResourceManagedPipeline):
        async def _initialize_resources(self):
            # 初始化资源
            pass
            
        async def _cleanup_resources(self):
            # 清理资源
            pass
            
        async def process_item(self, item, spider):
            # 处理逻辑
            return item
"""

import asyncio
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Any, Callable

from crawlo.items import Item
from crawlo.spider import Spider
from crawlo.logging import get_logger
from crawlo.utils.resource_manager import ResourceManager, ResourceType


class BasePipeline(ABC):
    """
    Pipeline基础抽象类
    
    所有Pipeline都应继承此基类，确保统一的接口规范。
    简单场景可直接使用，复杂场景建议使用ResourceManagedPipeline。
    """

    @classmethod
    @abstractmethod
    def from_crawler(cls, crawler):
        """从Crawler创建Pipeline实例"""
        raise NotImplementedError("子类必须实现from_crawler方法")
    
    @abstractmethod
    async def process_item(self, item: Item, spider: Spider, **kwargs) -> Optional[Item]:
        """处理Item的核心方法"""
        raise NotImplementedError("子类必须实现process_item方法")
    
    @classmethod
    def create_instance(cls, crawler):
        """兼容旧版本的创建方法，内部调用from_crawler"""
        return cls.from_crawler(crawler)


class ResourceManagedPipeline(BasePipeline):
    """
    资源管理Pipeline基类
    
    提供统一的资源管理功能，自动注册到ResourceManager
    
    特性：
    - 自动资源清理
    - LIFO清理顺序
    - 异常容错
    - 批量数据刷新
    """
    
    def __init__(self, crawler):
        """
        初始化Pipeline
        
        Args:
            crawler: Crawler实例
        """
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(
            self.__class__.__name__, 
            self.settings.get('LOG_LEVEL')
        )
        
        # 资源管理器
        self._resource_manager = ResourceManager(
            name=f"pipeline.{self.__class__.__name__}"
        )
        
        # 初始化标志
        self._initialized = False
        self._init_lock = asyncio.Lock()
        
        # 批量缓冲区（子类可选使用）
        self.batch_buffer = []
        self.batch_size = self.settings.get_int('PIPELINE_BATCH_SIZE', 100)
        self.use_batch = self.settings.get_bool('PIPELINE_USE_BATCH', False)
        
        # 注册关闭事件
        crawler.subscriber.subscribe(self._on_spider_closed, event='spider_closed')
        
        self.logger.debug(f"{self.__class__.__name__} 已初始化")
    
    async def _ensure_initialized(self):
        """确保资源已初始化（线程安全）"""
        if self._initialized:
            return
        
        async with self._init_lock:
            if not self._initialized:
                try:
                    await self._initialize_resources()
                    self._initialized = True
                    self.logger.info(f"{self.__class__.__name__} 资源初始化完成")
                except Exception as e:
                    self.logger.error(f"资源初始化失败: {e}")
                    raise
    
    @abstractmethod
    async def _initialize_resources(self):
        """
        初始化资源（子类实现）
        
        示例：
            # 初始化数据库连接池
            self.pool = await create_pool(...)
            
            # 注册到资源管理器
            self._resource_manager.register(
                resource=self.pool,
                cleanup_func=self._close_pool,
                resource_type=ResourceType.DATABASE,
                name="db_pool"
            )
        """
        pass
    
    @abstractmethod
    async def _cleanup_resources(self):
        """
        清理资源（子类实现）
        
        通常由ResourceManager自动调用，但也可以手动实现额外清理逻辑
        """
        pass
    
    async def _flush_batch(self, spider: Spider):
        """
        刷新批量缓冲区（子类可重写）
        
        Args:
            spider: Spider实例
        """
        if not self.batch_buffer:
            return
        
        self.logger.warning(
            f"批量缓冲区还有 {len(self.batch_buffer)} 条数据，"
            f"但未实现 _flush_batch 方法"
        )
    
    async def _on_spider_closed(self):
        """
        爬虫关闭事件处理
        
        自动执行：
        1. 刷新批量数据
        2. 清理所有注册的资源
        3. 生成统计报告
        """
        self.logger.info(f"{self.__class__.__name__} 开始清理资源...")
        
        try:
            # 1. 刷新批量数据
            if self.use_batch and self.batch_buffer:
                spider = self.crawler.spider
                await self._flush_batch(spider)
                self.logger.info(f"批量数据已刷新，共 {len(self.batch_buffer)} 条")
            
            # 2. 调用子类的清理方法
            await self._cleanup_resources()
            
            # 3. 使用资源管理器统一清理
            cleanup_result = await self._resource_manager.cleanup_all()
            
            # 4. 记录清理结果
            if cleanup_result['success_count'] > 0:
                self.logger.info(
                    f"资源清理完成: 成功 {cleanup_result['success_count']} 个, "
                    f"失败 {cleanup_result['failed_count']} 个"
                )
            
            if cleanup_result['errors']:
                self.logger.warning(f"清理时出现错误: {cleanup_result['errors']}")
            
        except Exception as e:
            self.logger.error(f"资源清理失败: {e}", exc_info=True)
    
    def register_resource(
        self,
        resource: Any,
        cleanup_func: Callable,
        resource_type: ResourceType = ResourceType.OTHER,
        name: Optional[str] = None
    ):
        """
        注册需要清理的资源
        
        Args:
            resource: 资源对象
            cleanup_func: 清理函数
            resource_type: 资源类型
            name: 资源名称
        """
        self._resource_manager.register(
            resource=resource,
            cleanup_func=cleanup_func,
            resource_type=resource_type,
            name=name or str(id(resource))
        )
        self.logger.debug(f"注册资源: {name} ({resource_type})")


class FileBasedPipeline(ResourceManagedPipeline):
    """
    文件型Pipeline基类
    
    提供文件操作的通用功能：
    - 自动创建目录
    - 文件句柄管理
    - 自动刷新缓冲区
    """
    
    def __init__(self, crawler):
        super().__init__(crawler)
        self.file_handle: Optional[Any] = None
        self.file_path: Optional[Path] = None
        self._file_lock = asyncio.Lock()
    
    def _get_file_path(self, config_key: str, default_prefix: str, extension: str) -> Path:
        """
        获取输出文件路径
        
        Args:
            config_key: 配置键名
            default_prefix: 默认前缀
            extension: 文件扩展名
        
        Returns:
            Path对象
        """
        from datetime import datetime
        
        file_path = (
            self.settings.get(config_key) or
            getattr(self.crawler.spider, config_key.lower(), None) or
            f"output/{self.crawler.spider.name}_{default_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    async def _open_file(self, mode: str = 'w', **kwargs):
        """
        打开文件并注册到资源管理器
        
        Args:
            mode: 文件打开模式
            **kwargs: 传递给open()的其他参数
        """
        if self.file_handle is not None:
            return
        
        async with self._file_lock:
            if self.file_handle is None:
                if self.file_path is None:
                    raise ValueError("文件路径未设置")
                
                self.file_handle = open(
                    self.file_path, 
                    mode, 
                    encoding=kwargs.get('encoding', 'utf-8'),
                    **{k: v for k, v in kwargs.items() if k != 'encoding'}
                )
                
                # 注册文件句柄到资源管理器
                self.register_resource(
                    resource=self.file_handle,
                    cleanup_func=self._close_file,
                    resource_type=ResourceType.OTHER,  # 使用OTHER类型
                    name=str(self.file_path)
                )
                
                self.logger.info(f"文件已打开: {self.file_path}")
    
    async def _close_file(self, file_handle):
        """关闭文件句柄"""
        if file_handle and not file_handle.closed:
            file_handle.close()
            self.logger.info(f"文件已关闭: {self.file_path}")
    
    async def _initialize_resources(self):
        """初始化文件资源"""
        # 子类应该调用 _open_file() 来打开文件
        pass
    
    async def _cleanup_resources(self):
        """清理由ResourceManager管理的资源"""
        # 文件句柄由ResourceManager自动清理
        pass


class DatabasePipeline(ResourceManagedPipeline):
    """
    数据库Pipeline基类
    
    提供数据库操作的通用功能：
    - 连接池管理
    - 自动重连
    - 批量写入优化
    - 事务支持
    """
    
    def __init__(self, crawler):
        super().__init__(crawler)
        self.pool = None
        self._pool_lock = asyncio.Lock()
        self._pool_initialized = False
    
    async def _ensure_pool_initialized(self):
        """确保连接池已初始化"""
        if self._pool_initialized and self.pool:
            return
        
        async with self._pool_lock:
            if not self._pool_initialized:
                await self._create_pool()
                self._pool_initialized = True
                self.logger.info(f"{self.__class__.__name__} 连接池已初始化")
    
    @abstractmethod
    async def _create_pool(self):
        """
        创建数据库连接池（子类实现）
        
        示例：
            self.pool = await create_pool(...)
            
            # 注册到资源管理器
            self.register_resource(
                resource=self.pool,
                cleanup_func=self._close_pool,
                resource_type=ResourceType.DATABASE,
                name="db_pool"
            )
        """
        raise NotImplementedError("子类必须实现 _create_pool 方法")
    
    @abstractmethod
    async def _close_pool(self, pool):
        """关闭连接池（子类实现）"""
        raise NotImplementedError("子类必须实现 _close_pool 方法")
    
    async def _initialize_resources(self):
        """初始化数据库资源"""
        await self._ensure_pool_initialized()
    
    async def _cleanup_resources(self):
        """清理由ResourceManager管理的资源"""
        # 连接池由ResourceManager自动清理
        pass


class CacheBasedPipeline(ResourceManagedPipeline):
    """
    缓存型Pipeline基类
    
    提供缓存操作的通用功能：
    - Redis/Memcached连接管理
    - 自动关闭连接
    """
    
    def __init__(self, crawler):
        super().__init__(crawler)
        self.client = None
        self._client_lock = asyncio.Lock()
        self._client_initialized = False
    
    async def _ensure_client_initialized(self):
        """确保缓存客户端已初始化"""
        if self._client_initialized and self.client:
            return
        
        async with self._client_lock:
            if not self._client_initialized:
                await self._create_client()
                self._client_initialized = True
                self.logger.info(f"{self.__class__.__name__} 缓存客户端已初始化")
    
    @abstractmethod
    async def _create_client(self):
        """
        创建缓存客户端（子类实现）
        
        示例：
            self.client = redis.Redis(...)
            
            # 注册到资源管理器
            self.register_resource(
                resource=self.client,
                cleanup_func=self._close_client,
                resource_type=ResourceType.NETWORK,
                name="cache_client"
            )
        """
        raise NotImplementedError("子类必须实现 _create_client 方法")
    
    @abstractmethod
    async def _close_client(self, client):
        """关闭缓存客户端（子类实现）"""
        raise NotImplementedError("子类必须实现 _close_client 方法")
    
    async def _initialize_resources(self):
        """初始化缓存资源"""
        await self._ensure_client_initialized()
    
    async def _cleanup_resources(self):
        """清理由ResourceManager管理的资源"""
        # 客户端由ResourceManager自动清理
        pass

```

**code file end: crawlo/pipelines/base_pipeline.py**

---


### code file start: crawlo/pipelines/bloom_dedup_pipeline.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
基于 Bloom Filter 的数据项去重管道
=============================
提供大规模数据采集场景下的高效去重功能，使用概率性数据结构节省内存。

特点:
- 内存效率高: 相比传统集合节省大量内存
- 高性能: 快速的插入和查找操作
- 可扩展: 支持自定义容量和误判率
- 适用性广: 特别适合大规模数据采集

注意: Bloom Filter 有误判率，可能会错误地丢弃一些未见过的数据项。
"""

import hashlib
try:
    from pybloom_live import BloomFilter
    BLOOM_FILTER_AVAILABLE = True
except ImportError:
    # 如果没有安装 pybloom_live，使用简单的替代方案
    BLOOM_FILTER_AVAILABLE = False
    
    class BloomFilter:
        def __init__(self, capacity, error_rate):
            self._data = set()
        
        def add(self, item):
            if item in self._data:
                return False
            else:
                self._data.add(item)
                return True
        
        def __contains__(self, item):
            return item in self._data

from crawlo import Item
from crawlo.spider import Spider
from crawlo.utils.fingerprint import FingerprintGenerator
from crawlo.logging import get_logger
from crawlo.exceptions import ItemDiscard


class BloomDedupPipeline:
    """基于 Bloom Filter 的数据项去重管道"""

    def __init__(
            self,
            capacity: int = 1000000,
            error_rate: float = 0.001,
            log_level: str = "INFO"
    ):
        """
        初始化 Bloom Filter 去重管道
        
        :param capacity: 预期存储的元素数量
        :param error_rate: 误判率 (例如 0.001 表示 0.1%)
        :param log_level: 日志级别
        """
        self.logger = get_logger(self.__class__.__name__)
        
        # 初始化 Bloom Filter
        try:
            self.bloom_filter = BloomFilter(capacity=capacity, error_rate=error_rate)
            self.logger.info(f"Bloom filter deduplication pipeline initialized (Capacity: {capacity}, Error rate: {error_rate})")
        except Exception as e:
            self.logger.error(f"Bloom filter initialization failed: {e}")
            raise RuntimeError(f"Bloom Filter 初始化失败: {e}")

        self.capacity = capacity
        self.error_rate = error_rate
        self.dropped_count = 0
        self.added_count = 0

    @classmethod
    def from_crawler(cls, crawler):
        """从爬虫配置创建管道实例"""
        settings = crawler.settings
        
        return cls(
            capacity=settings.get_int('BLOOM_FILTER_CAPACITY', 1000000),
            error_rate=settings.get_float('BLOOM_FILTER_ERROR_RATE', 0.001),
            log_level=settings.get('LOG_LEVEL', 'INFO')
        )

    def process_item(self, item: Item, spider: Spider) -> Item:
        """
        处理数据项，进行去重检查
        
        :param item: 要处理的数据项
        :param spider: 爬虫实例
        :return: 处理后的数据项或抛出 ItemDiscard 异常
        """
        try:
            # 生成数据项指纹
            fingerprint = self._generate_item_fingerprint(item)
            
            # 检查指纹是否已存在
            if fingerprint in self.bloom_filter:
                # 如果可能已存在（Bloom Filter 可能有误判），丢弃这个数据项
                self.dropped_count += 1
                self.logger.debug(f"Possibly dropping duplicate item: {fingerprint[:20]}...")
                raise ItemDiscard(f"可能重复的数据项: {fingerprint}")
            else:
                # 添加指纹到 Bloom Filter
                self.bloom_filter.add(fingerprint)
                self.added_count += 1
                self.logger.debug(f"Processing new item: {fingerprint[:20]}...")
                return item
                
        except ItemDiscard:
            # 重新抛出ItemDiscard异常，确保管道管理器能正确处理
            raise
        except Exception as e:
            self.logger.error(f"Error processing item: {e}")
            # 在错误时继续处理，避免丢失数据
            return item

    def _generate_item_fingerprint(self, item: Item) -> str:
        """
        生成数据项指纹
        
        基于数据项的所有字段生成唯一指纹，用于去重判断。
        
        :param item: 数据项
        :return: 指纹字符串
        """
        return FingerprintGenerator.item_fingerprint(item)

    def close_spider(self, spider: Spider) -> None:
        """
        爬虫关闭时的清理工作
        
        :param spider: 爬虫实例
        """
        self.logger.info(f"Spider {spider.name} closed:")
        self.logger.info(f"  - Processed items: {self.added_count}")
        self.logger.info(f"  - Possibly dropped duplicate items: {self.dropped_count}")
        
        if BLOOM_FILTER_AVAILABLE:
            # 注意：Bloom Filter 无法准确统计元素数量
            self.logger.info(f"  - Bloom filter capacity: {self.capacity}")
            self.logger.info(f"  - Bloom filter error rate: {self.error_rate}")
        else:
            self.logger.warning("  - pybloom_live not installed, using memory set as fallback")
```

**code file end: crawlo/pipelines/bloom_dedup_pipeline.py**

---


### code file start: crawlo/pipelines/console_pipeline.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
from typing import Dict, Any

from crawlo import Item
from crawlo.spider import Spider
from crawlo.logging import get_logger


class ConsolePipeline:
    """将Item内容输出到控制台的管道"""

    def __init__(self, log_level: str = "DEBUG"):
        self.logger = get_logger(self.__class__.__name__)

    @classmethod
    def from_crawler(cls, crawler):
        """从crawler实例创建管道"""
        return cls(
            log_level=crawler.settings.get('LOG_LEVEL', 'DEBUG')
        )

    async def process_item(self, item: Item, spider: Spider) -> Item:
        """处理Item并输出到日志"""
        try:
            item_dict = self._convert_to_serializable(item)
            self.logger.info(f"Item processed: {item_dict}")
            return item
        except Exception as e:
            self.logger.error(f"Error processing item: {e}", exc_info=True)
            raise

    @staticmethod
    def _convert_to_serializable(item: Item) -> Dict[str, Any]:
        """将Item转换为可序列化的字典"""
        try:
            return item.to_dict()
        except AttributeError:
            # 兼容没有to_dict方法的Item实现
            return dict(item)
```

**code file end: crawlo/pipelines/console_pipeline.py**

---


### code file start: crawlo/pipelines/csv_pipeline.py 

```python
# -*- coding: utf-8 -*-
import csv
import asyncio
from pathlib import Path
from typing import Optional, List
from datetime import datetime
from crawlo.logging import get_logger
from crawlo.exceptions import ItemDiscard


class CsvPipeline:
    """CSV文件输出管道"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        # 配置文件路径
        self.file_path = self._get_file_path()
        self.file_handle = None
        self.csv_writer = None
        self.headers_written = False
        self.lock = asyncio.Lock()  # 异步锁保证线程安全
        
        # CSV配置
        self.delimiter = self.settings.get('CSV_DELIMITER', ',')
        self.quotechar = self.settings.get('CSV_QUOTECHAR', '"')
        self.include_headers = self.settings.get_bool('CSV_INCLUDE_HEADERS', True)
        
        # 注册关闭事件
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    def _get_file_path(self) -> Path:
        """获取输出文件路径"""
        file_path = (
            self.settings.get('CSV_FILE') or
            getattr(self.crawler.spider, 'csv_file', None) or
            f"output/{self.crawler.spider.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    async def _ensure_file_open(self):
        """确保文件已打开"""
        if self.file_handle is None:
            self.file_handle = open(self.file_path, 'w', newline='', encoding='utf-8')
            self.csv_writer = csv.writer(
                self.file_handle,
                delimiter=self.delimiter,
                quotechar=self.quotechar,
                quoting=csv.QUOTE_MINIMAL
            )
            self.logger.info(f"CSV文件已创建: {self.file_path}")
    
    async def _write_headers(self, item_dict: dict):
        """写入CSV表头"""
        if not self.headers_written and self.include_headers:
            headers = list(item_dict.keys())
            self.csv_writer.writerow(headers)
            self.headers_written = True
            self.logger.debug(f"CSV表头已写入: {headers}")
    
    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item的核心方法"""
        try:
            async with self.lock:
                await self._ensure_file_open()
                
                # 转换为字典
                item_dict = dict(item)
                
                # 写入表头（仅第一次）
                await self._write_headers(item_dict)
                
                # 写入数据行
                values = [str(v) if v is not None else '' for v in item_dict.values()]
                self.csv_writer.writerow(values)
                self.file_handle.flush()  # 立即刷新到磁盘
                
                # 统计
                self.crawler.stats.inc_value('csv_pipeline/items_written')
                self.logger.debug(f"写入CSV行: {len(item_dict)} 字段")
                
            return item
            
        except Exception as e:
            self.crawler.stats.inc_value('csv_pipeline/items_failed')
            self.logger.error(f"CSV写入失败: {e}")
            raise ItemDiscard(f"CSV Pipeline处理失败: {e}")
    
    async def spider_closed(self):
        """关闭爬虫时清理资源"""
        if self.file_handle:
            self.file_handle.close()
            self.logger.info(f"CSV文件已关闭: {self.file_path}")


class CsvDictPipeline:
    """CSV字典写入器管道（使用DictWriter，支持字段映射）"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        self.file_path = self._get_file_path()
        self.file_handle = None
        self.csv_writer = None
        self.fieldnames = None
        self.headers_written = False
        self.lock = asyncio.Lock()
        
        # 配置选项
        self.delimiter = self.settings.get('CSV_DELIMITER', ',')
        self.quotechar = self.settings.get('CSV_QUOTECHAR', '"')
        self.include_headers = self.settings.get_bool('CSV_INCLUDE_HEADERS', True)
        self.extrasaction = self.settings.get('CSV_EXTRASACTION', 'ignore')  # ignore, raise
        
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    def _get_file_path(self) -> Path:
        """获取输出文件路径"""
        file_path = (
            self.settings.get('CSV_DICT_FILE') or
            getattr(self.crawler.spider, 'csv_dict_file', None) or
            f"output/{self.crawler.spider.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_dict.csv"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    def _get_fieldnames(self, item_dict: dict) -> List[str]:
        """获取字段名列表"""
        # 优先使用配置的字段名
        configured_fields = self.settings.get('CSV_FIELDNAMES')
        if configured_fields:
            return configured_fields if isinstance(configured_fields, list) else configured_fields.split(',')
        
        # 使用爬虫定义的字段名
        spider_fields = getattr(self.crawler.spider, 'csv_fieldnames', None)
        if spider_fields:
            return spider_fields if isinstance(spider_fields, list) else spider_fields.split(',')
        
        # 使用item的字段名
        return list(item_dict.keys())
    
    async def _ensure_file_open(self, item_dict: dict):
        """确保文件已打开"""
        if self.file_handle is None:
            self.fieldnames = self._get_fieldnames(item_dict)
            
            self.file_handle = open(self.file_path, 'w', newline='', encoding='utf-8')
            self.csv_writer = csv.DictWriter(
                self.file_handle,
                fieldnames=self.fieldnames,
                delimiter=self.delimiter,
                quotechar=self.quotechar,
                quoting=csv.QUOTE_MINIMAL,
                extrasaction=self.extrasaction
            )
            
            # 写入表头
            if self.include_headers:
                self.csv_writer.writeheader()
                self.headers_written = True
            
            self.logger.info(f"CSV字典文件已创建: {self.file_path}，字段: {self.fieldnames}")
    
    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item方法"""
        try:
            async with self.lock:
                item_dict = dict(item)
                await self._ensure_file_open(item_dict)
                
                # 写入数据行
                self.csv_writer.writerow(item_dict)
                self.file_handle.flush()
                
                self.crawler.stats.inc_value('csv_dict_pipeline/items_written')
                self.logger.debug(f"写入CSV字典行，字段数: {len(item_dict)}")
                
            return item
            
        except Exception as e:
            self.crawler.stats.inc_value('csv_dict_pipeline/items_failed')
            self.logger.error(f"CSV字典写入失败: {e}")
            raise ItemDiscard(f"CSV Dict Pipeline处理失败: {e}")
    
    async def spider_closed(self):
        """资源清理"""
        if self.file_handle:
            self.file_handle.close()
            self.logger.info(f"CSV字典文件已关闭: {self.file_path}")


class CsvBatchPipeline:
    """CSV批量写入管道（内存缓存，批量写入，提高性能）"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        self.file_path = self._get_file_path()
        self.file_handle = None
        self.csv_writer = None
        self.batch_buffer = []
        self.headers_written = False
        self.lock = asyncio.Lock()
        
        # 批量配置
        self.batch_size = self.settings.get_int('CSV_BATCH_SIZE', 100)
        self.delimiter = self.settings.get('CSV_DELIMITER', ',')
        self.quotechar = self.settings.get('CSV_QUOTECHAR', '"')
        self.include_headers = self.settings.get_bool('CSV_INCLUDE_HEADERS', True)
        
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    def _get_file_path(self) -> Path:
        """获取输出文件路径"""
        file_path = (
            self.settings.get('CSV_BATCH_FILE') or
            getattr(self.crawler.spider, 'csv_batch_file', None) or
            f"output/{self.crawler.spider.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_batch.csv"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    async def _ensure_file_open(self):
        """确保文件已打开"""
        if self.file_handle is None:
            self.file_handle = open(self.file_path, 'w', newline='', encoding='utf-8')
            self.csv_writer = csv.writer(
                self.file_handle,
                delimiter=self.delimiter,
                quotechar=self.quotechar,
                quoting=csv.QUOTE_MINIMAL
            )
            self.logger.info(f"CSV批量文件已创建: {self.file_path}")
    
    async def _flush_batch(self):
        """刷新批量缓存到文件"""
        if not self.batch_buffer:
            return
        
        await self._ensure_file_open()
        
        for row in self.batch_buffer:
            self.csv_writer.writerow(row)
        
        self.file_handle.flush()
        items_count = len(self.batch_buffer)
        self.batch_buffer.clear()
        
        self.crawler.stats.inc_value('csv_batch_pipeline/batches_written')
        self.crawler.stats.inc_value('csv_batch_pipeline/items_written', count=items_count)
        self.logger.info(f"批量写入 {items_count} 行到CSV文件")
    
    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item方法"""
        try:
            async with self.lock:
                item_dict = dict(item)
                
                # 写入表头（仅第一次）
                if not self.headers_written and self.include_headers:
                    headers = list(item_dict.keys())
                    self.batch_buffer.append(headers)
                    self.headers_written = True
                
                # 添加数据到缓存
                values = [str(v) if v is not None else '' for v in item_dict.values()]
                self.batch_buffer.append(values)
                
                # 检查是否需要刷新批量缓存
                if len(self.batch_buffer) >= self.batch_size:
                    await self._flush_batch()
                
            return item
            
        except Exception as e:
            self.crawler.stats.inc_value('csv_batch_pipeline/items_failed')
            self.logger.error(f"CSV批量处理失败: {e}")
            raise ItemDiscard(f"CSV Batch Pipeline处理失败: {e}")
    
    async def spider_closed(self):
        """关闭时刷新剩余缓存"""
        try:
            # 刷新剩余的批量数据
            async with self.lock:
                await self._flush_batch()
            
            if self.file_handle:
                self.file_handle.close()
                self.logger.info(f"CSV批量文件已关闭: {self.file_path}")
                
        except Exception as e:
            self.logger.error(f"关闭CSV批量管道时出错: {e}")
```

**code file end: crawlo/pipelines/csv_pipeline.py**

---


### code file start: crawlo/pipelines/database_dedup_pipeline.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
基于数据库的数据项去重管道
=======================
提供持久化去重功能，适用于需要长期运行或断点续爬的场景。

特点:
- 持久化存储: 重启爬虫后仍能保持去重状态
- 可靠性高: 数据库事务保证一致性
- 适用性广: 支持多种数据库后端
- 可扩展: 支持自定义表结构和字段
"""
import hashlib
import aiomysql

from crawlo import Item
from crawlo.exceptions import ItemDiscard
from crawlo.spider import Spider
from crawlo.utils.fingerprint import FingerprintGenerator
from crawlo.logging import get_logger


class DatabaseDedupPipeline:
    """基于数据库的数据项去重管道"""

    def __init__(
            self,
            db_host: str = 'localhost',
            db_port: int = 3306,
            db_user: str = 'root',
            db_password: str = '',
            db_name: str = 'crawlo',
            table_name: str = 'item_fingerprints',
            log_level: str = "INFO"
    ):
        """
        初始化数据库去重管道
        
        :param db_host: 数据库主机地址
        :param db_port: 数据库端口
        :param db_user: 数据库用户名
        :param db_password: 数据库密码
        :param db_name: 数据库名称
        :param table_name: 存储指纹的表名
        :param log_level: 日志级别
        """
        self.logger = get_logger(self.__class__.__name__)
        
        # 数据库连接参数
        self.db_config = {
            'host': db_host,
            'port': db_port,
            'user': db_user,
            'password': db_password,
            'db': db_name,
            'autocommit': False
        }
        
        self.table_name = table_name
        self.dropped_count = 0
        self.connection = None
        self.pool = None

    @classmethod
    def from_crawler(cls, crawler):
        """从爬虫配置创建管道实例"""
        settings = crawler.settings
        
        return cls(
            db_host=settings.get('DB_HOST', 'localhost'),
            db_port=settings.getint('DB_PORT', 3306),
            db_user=settings.get('DB_USER', 'root'),
            db_password=settings.get('DB_PASSWORD', ''),
            db_name=settings.get('DB_NAME', 'crawlo'),
            table_name=settings.get('DB_DEDUP_TABLE', 'item_fingerprints'),
            log_level=settings.get('LOG_LEVEL', 'INFO')
        )

    async def open_spider(self, spider: Spider) -> None:
        """
        爬虫启动时初始化数据库连接
        
        :param spider: 爬虫实例
        """
        try:
            # 创建连接池
            self.pool = await aiomysql.create_pool(
                **self.db_config,
                minsize=2,
                maxsize=10
            )
            
            # 创建去重表（如果不存在）
            await self._create_dedup_table()
            
            self.logger.info(f"Database deduplication pipeline initialized: {self.db_config['host']}:{self.db_config['port']}/{self.db_config['db']}.{self.table_name}")
        except Exception as e:
            self.logger.error(f"Database deduplication pipeline initialization failed: {e}")
            raise RuntimeError(f"数据库去重管道初始化失败: {e}")

    async def _create_dedup_table(self) -> None:
        """创建去重表"""
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS `{self.table_name}` (
            `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
            `fingerprint` VARCHAR(64) NOT NULL UNIQUE,
            `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX `idx_fingerprint` (`fingerprint`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(create_table_sql)
                await conn.commit()

    async def process_item(self, item: Item, spider: Spider) -> Item:
        """
        处理数据项，进行去重检查
        
        :param item: 要处理的数据项
        :param spider: 爬虫实例
        :return: 处理后的数据项或抛出 ItemDiscard 异常
        """
        try:
            # 生成数据项指纹
            fingerprint = self._generate_item_fingerprint(item)
            
            # 检查指纹是否已存在
            exists = await self._check_fingerprint_exists(fingerprint)
            
            if exists:
                # 如果已存在，丢弃这个数据项
                self.dropped_count += 1
                self.logger.debug(f"Dropping duplicate item: {fingerprint[:20]}...")
                raise ItemDiscard(f"Duplicate item: {fingerprint}")
            else:
                # 记录新数据项的指纹
                await self._insert_fingerprint(fingerprint)
                self.logger.debug(f"Processing new item: {fingerprint[:20]}...")
                return item
                
        except ItemDiscard:
            # 重新抛出ItemDiscard异常，确保管道管理器能正确处理
            raise
        except Exception as e:
            self.logger.error(f"Error processing item: {e}")
            # 在错误时继续处理，避免丢失数据
            return item

    async def _check_fingerprint_exists(self, fingerprint: str) -> bool:
        """
        检查指纹是否已存在
        
        :param fingerprint: 数据项指纹
        :return: 是否存在
        """
        check_sql = f"SELECT 1 FROM `{self.table_name}` WHERE `fingerprint` = %s LIMIT 1"
        
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(check_sql, (fingerprint,))
                result = await cursor.fetchone()
                return result is not None

    async def _insert_fingerprint(self, fingerprint: str) -> None:
        """
        插入新指纹
        
        :param fingerprint: 数据项指纹
        """
        insert_sql = f"INSERT INTO `{self.table_name}` (`fingerprint`) VALUES (%s)"
        
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                try:
                    await cursor.execute(insert_sql, (fingerprint,))
                    await conn.commit()
                except aiomysql.IntegrityError:
                    # 指纹已存在（并发情况下可能发生）
                    await conn.rollback()
                    raise ItemDiscard(f"重复的数据项: {fingerprint}")
                except Exception:
                    await conn.rollback()
                    raise

    def _generate_item_fingerprint(self, item: Item) -> str:
        """
        生成数据项指纹
        
        基于数据项的所有字段生成唯一指纹，用于去重判断。
        
        :param item: 数据项
        :return: 指纹字符串
        """
        return FingerprintGenerator.item_fingerprint(item)

```

**code file end: crawlo/pipelines/database_dedup_pipeline.py**

---


### code file start: crawlo/pipelines/json_pipeline.py 

```python
# -*- coding: utf-8 -*-
import json
import asyncio
from pathlib import Path
from typing import Optional
from datetime import datetime
from crawlo.logging import get_logger
from crawlo.exceptions import ItemDiscard


class JsonPipeline:
    """JSON文件输出管道"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        # 配置文件路径
        self.file_path = self._get_file_path()
        self.file_handle = None
        self.lock = asyncio.Lock()  # 异步锁保证线程安全
        
        # 注册关闭事件
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    def _get_file_path(self) -> Path:
        """获取输出文件路径"""
        # 优先级：设置 > 爬虫属性 > 默认路径
        file_path = (
            self.settings.get('JSON_FILE') or
            getattr(self.crawler.spider, 'json_file', None) or
            f"output/{self.crawler.spider.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    async def _ensure_file_open(self):
        """确保文件已打开"""
        if self.file_handle is None:
            self.file_handle = open(self.file_path, 'w', encoding='utf-8')
            self.logger.info(f"JSON文件已创建: {self.file_path}")
    
    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item的核心方法"""
        try:
            async with self.lock:
                await self._ensure_file_open()
                
                # 转换为字典并序列化
                item_dict = dict(item)
                json_line = json.dumps(item_dict, ensure_ascii=False, indent=None)
                
                # 写入文件（每行一个JSON对象）
                self.file_handle.write(json_line + '\n')
                self.file_handle.flush()  # 立即刷新到磁盘
                
                # 统计
                self.crawler.stats.inc_value('json_pipeline/items_written')
                self.logger.debug(f"写入JSON项: {len(item_dict)} 字段")
                
            return item
            
        except Exception as e:
            self.crawler.stats.inc_value('json_pipeline/items_failed')
            self.logger.error(f"JSON写入失败: {e}")
            raise ItemDiscard(f"JSON Pipeline处理失败: {e}")
    
    async def spider_closed(self):
        """关闭爬虫时清理资源"""
        if self.file_handle:
            self.file_handle.close()
            self.logger.info(f"JSON文件已关闭: {self.file_path}")


class JsonLinesPipeline:
    """JSON Lines格式输出管道（每行一个JSON对象）"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        self.file_path = self._get_file_path()
        self.file_handle = None
        self.items_count = 0
        self.lock = asyncio.Lock()
        
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    def _get_file_path(self) -> Path:
        """获取输出文件路径"""
        file_path = (
            self.settings.get('JSONLINES_FILE') or
            getattr(self.crawler.spider, 'jsonlines_file', None) or
            f"output/{self.crawler.spider.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    async def _ensure_file_open(self):
        """确保文件已打开"""
        if self.file_handle is None:
            self.file_handle = open(self.file_path, 'w', encoding='utf-8')
            self.logger.info(f"JSONL文件已创建: {self.file_path}")
    
    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item方法"""
        try:
            async with self.lock:
                await self._ensure_file_open()
                
                item_dict = dict(item)
                
                # 添加元数据
                if self.settings.get_bool('JSON_ADD_METADATA', False):
                    item_dict['_crawl_time'] = datetime.now().isoformat()
                    item_dict['_spider_name'] = spider.name
                
                # 写入JSONL格式
                json_line = json.dumps(item_dict, ensure_ascii=False, separators=(',', ':'))
                self.file_handle.write(json_line + '\n')
                self.file_handle.flush()
                
                self.items_count += 1
                
                # 定期日志输出
                if self.items_count % 100 == 0:
                    self.logger.info(f"已写入 {self.items_count} 个JSON对象")
                
                self.crawler.stats.inc_value('jsonlines_pipeline/items_written')
                
            return item
            
        except Exception as e:
            self.crawler.stats.inc_value('jsonlines_pipeline/items_failed')
            self.logger.error(f"JSONL写入失败: {e}")
            raise ItemDiscard(f"JSON Lines Pipeline处理失败: {e}")
    
    async def spider_closed(self):
        """资源清理"""
        if self.file_handle:
            self.file_handle.close()
            self.logger.info(f"JSONL文件已关闭，共写入 {self.items_count} 个项目: {self.file_path}")


class JsonArrayPipeline:
    """JSON数组格式输出管道（所有item组成一个JSON数组）"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)
        
        self.file_path = self._get_file_path()
        self.items = []  # 内存中暂存所有items
        self.lock = asyncio.Lock()
        
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    
    def _get_file_path(self) -> Path:
        """获取输出文件路径"""
        file_path = (
            self.settings.get('JSON_ARRAY_FILE') or
            getattr(self.crawler.spider, 'json_array_file', None) or
            f"output/{self.crawler.spider.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_array.json"
        )
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    
    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item方法"""
        try:
            async with self.lock:
                item_dict = dict(item)
                self.items.append(item_dict)
                
                self.crawler.stats.inc_value('json_array_pipeline/items_collected')
                self.logger.debug(f"收集item，当前总数: {len(self.items)}")
                
            return item
            
        except Exception as e:
            self.crawler.stats.inc_value('json_array_pipeline/items_failed')
            self.logger.error(f"JSON Array收集失败: {e}")
            raise ItemDiscard(f"JSON Array Pipeline处理失败: {e}")
    
    async def spider_closed(self):
        """关闭时写入所有items到JSON数组文件"""
        try:
            if self.items:
                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.items, f, ensure_ascii=False, indent=2)
                
                self.logger.info(f"JSON数组文件已保存，包含 {len(self.items)} 个项目: {self.file_path}")
                self.crawler.stats.set_value('json_array_pipeline/total_items', len(self.items))
            else:
                self.logger.warning("没有items需要保存")
                
        except Exception as e:
            self.logger.error(f"保存JSON数组文件失败: {e}")
```

**code file end: crawlo/pipelines/json_pipeline.py**

---


### code file start: crawlo/pipelines/memory_dedup_pipeline.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
基于内存的数据项去重管道
======================
提供单节点环境下的数据项去重功能，防止保存重复的数据记录。

特点:
- 高性能: 使用内存集合进行快速查找
- 简单易用: 无需外部依赖
- 轻量级: 适用于小规模数据采集
- 低延迟: 内存操作无网络开销
"""

import hashlib
from typing import Set

from crawlo import Item
from crawlo.exceptions import ItemDiscard
from crawlo.spider import Spider
from crawlo.utils.fingerprint import FingerprintGenerator
from crawlo.logging import get_logger


class MemoryDedupPipeline:
    """基于内存的数据项去重管道"""

    def __init__(self, log_level: str = "INFO"):
        """
        初始化内存去重管道
        
        :param log_level: 日志级别
        """
        self.logger = get_logger(self.__class__.__name__)
        
        # 使用集合存储已见过的数据项指纹
        self.seen_items: Set[str] = set()
        self.dropped_count = 0
        
        self.logger.info("Memory deduplication pipeline initialized")

    @classmethod
    def from_crawler(cls, crawler):
        """从爬虫配置创建管道实例"""
        settings = crawler.settings
        
        return cls(
            log_level=settings.get('LOG_LEVEL', 'INFO')
        )

    def process_item(self, item: Item, spider: Spider) -> Item:
        """
        处理数据项，进行去重检查
        
        :param item: 要处理的数据项
        :param spider: 爬虫实例
        :return: 处理后的数据项或抛出 ItemDiscard 异常
        """
        try:
            # 生成数据项指纹
            fingerprint = self._generate_item_fingerprint(item)
            
            # 检查指纹是否已存在
            if fingerprint in self.seen_items:
                # 如果已存在，丢弃这个数据项
                self.dropped_count += 1
                self.logger.debug(f"Dropping duplicate item: {fingerprint[:20]}...")
                raise ItemDiscard(f"重复的数据项: {fingerprint}")
            else:
                # 记录新数据项的指纹
                self.seen_items.add(fingerprint)
                self.logger.debug(f"Processing new item: {fingerprint[:20]}...")
                return item
                
        except ItemDiscard:
            # 重新抛出ItemDiscard异常，确保管道管理器能正确处理
            raise
        except Exception as e:
            self.logger.error(f"Error processing item: {e}")
            # 在错误时继续处理，避免丢失数据
            return item

    def _generate_item_fingerprint(self, item: Item) -> str:
        """
        生成数据项指纹
        
        基于数据项的所有字段生成唯一指纹，用于去重判断。
        
        :param item: 数据项
        :return: 指纹字符串
        """
        return FingerprintGenerator.item_fingerprint(item)

    def close_spider(self, spider: Spider) -> None:
        """
        爬虫关闭时的清理工作
        
        :param spider: 爬虫实例
        """
        self.logger.info(f"Spider {spider.name} closed:")
        self.logger.info(f"  - Dropped duplicate items: {self.dropped_count}")
        self.logger.info(f"  - Fingerprints stored in memory: {len(self.seen_items)}")
        
        # 清理内存
        self.seen_items.clear()
        self.dropped_count = 0
```

**code file end: crawlo/pipelines/memory_dedup_pipeline.py**

---


### code file start: crawlo/pipelines/mongo_pipeline.py 

```python
# -*- coding: utf-8 -*-
from typing import Optional, List, Dict
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
from crawlo.logging import get_logger
from crawlo.utils.mongo_connection_pool import MongoConnectionPoolManager
from crawlo.exceptions import ItemDiscard


class MongoPipeline:
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)

        # 初始化连接参数
        self.client = None
        self.db = None
        self.collection = None

        # 配置默认值
        self.mongo_uri = self.settings.get('MONGO_URI', 'mongodb://localhost:27017')
        self.db_name = self.settings.get('MONGO_DATABASE', 'scrapy_db')
        self.collection_name = self.settings.get('MONGO_COLLECTION', crawler.spider.name)
        
        # 连接池配置
        self.max_pool_size = self.settings.getint('MONGO_MAX_POOL_SIZE', 100)
        self.min_pool_size = self.settings.getint('MONGO_MIN_POOL_SIZE', 10)
        self.connect_timeout_ms = self.settings.getint('MONGO_CONNECT_TIMEOUT_MS', 5000)
        self.socket_timeout_ms = self.settings.getint('MONGO_SOCKET_TIMEOUT_MS', 30000)

        # 批量插入配置
        self.batch_size = self.settings.getint('MONGO_BATCH_SIZE', 100)
        self.use_batch = self.settings.getbool('MONGO_USE_BATCH', False)
        self.batch_buffer: List[Dict] = []  # 批量缓冲区

        # 注册关闭事件
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    async def _ensure_connection(self):
        """确保连接已建立"""
        if self.client is None:
            # 使用单例连接池管理器
            self.client = await MongoConnectionPoolManager.get_client(
                mongo_uri=self.mongo_uri,
                db_name=self.db_name,
                max_pool_size=self.max_pool_size,
                min_pool_size=self.min_pool_size,
                connect_timeout_ms=self.connect_timeout_ms,
                socket_timeout_ms=self.socket_timeout_ms
            )
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            self.logger.info(
                f"MongoDB连接建立 (集合: {self.collection_name}, "
                f"使用全局共享连接池)"
            )

    async def process_item(self, item, spider) -> Optional[dict]:
        """处理item的核心方法（带重试机制）"""
        # 如果启用批量插入，将item添加到缓冲区
        if self.use_batch:
            self.batch_buffer.append(dict(item))
            
            # 如果缓冲区达到批量大小，执行批量插入
            if len(self.batch_buffer) >= self.batch_size:
                await self._flush_batch(spider)
                
            return item
        else:
            # 单条插入逻辑
            try:
                await self._ensure_connection()

                item_dict = dict(item)

                # 带重试的插入操作
                for attempt in range(3):
                    try:
                        result = await self.collection.insert_one(item_dict)
                        # 统一使用insert_success统计键名
                        self.crawler.stats.inc_value('mongodb/insert_success')
                        self.logger.debug(f"插入成功 [attempt {attempt + 1}]: {result.inserted_id}")
                        return item
                    except PyMongoError as e:
                        if attempt == 2:  # 最后一次尝试仍失败
                            raise
                        self.logger.warning(f"插入重试中 [attempt {attempt + 1}]: {e}")

            except Exception as e:
                # 统一使用insert_failed统计键名
                self.crawler.stats.inc_value('mongodb/insert_failed')
                self.logger.error(f"MongoDB操作最终失败: {e}")
                raise ItemDiscard(f"MongoDB操作失败: {e}")

    async def _flush_batch(self, spider):
        """刷新批量缓冲区并执行批量插入"""
        if not self.batch_buffer:
            return

        try:
            await self._ensure_connection()

            # 带重试的批量插入操作
            for attempt in range(3):
                try:
                    result = await self.collection.insert_many(self.batch_buffer, ordered=False)
                    # 统一使用insert_success统计键名
                    inserted_count = len(result.inserted_ids)
                    self.crawler.stats.inc_value('mongodb/insert_success', inserted_count)
                    self.logger.debug(f"批量插入成功 [attempt {attempt + 1}]: {inserted_count} 条记录")
                    self.batch_buffer.clear()
                    return
                except PyMongoError as e:
                    if attempt == 2:  # 最后一次尝试仍失败
                        raise
                    self.logger.warning(f"批量插入重试中 [attempt {attempt + 1}]: {e}")
        except Exception as e:
            # 统一使用insert_failed统计键名
            failed_count = len(self.batch_buffer)
            self.crawler.stats.inc_value('mongodb/insert_failed', failed_count)
            self.logger.error(f"MongoDB批量插入最终失败: {e}")
            raise ItemDiscard(f"MongoDB批量插入失败: {e}")

    async def spider_closed(self):
        """关闭爬虫时清理资源"""
        # 在关闭前刷新剩余的批量数据
        if self.use_batch and self.batch_buffer:
            await self._flush_batch(self.crawler.spider)
        
        # 注意：不再关闭客户端，因为客户端是全局共享的
        # 客户端的关闭由 MongoConnectionPoolManager.close_all_clients() 统一管理
        if self.client:
            self.logger.info(
                f"MongoDB Pipeline 关闭，但保留全局共享连接池以供其他爬虫使用"
            )
```

**code file end: crawlo/pipelines/mongo_pipeline.py**

---


### code file start: crawlo/pipelines/mysql_pipeline.py 

```python
# -*- coding: utf-8 -*-
import asyncio
from abc import ABC, abstractmethod
from typing import List, Dict, Any

import async_timeout

from crawlo.exceptions import ItemDiscard
from crawlo.items import Item
from crawlo.utils.db_helper import SQLBuilder
from crawlo.logging import get_logger
from crawlo.utils.mysql_connection_pool import MySQLConnectionPoolManager
from . import BasePipeline


class BaseMySQLPipeline(BasePipeline, ABC):
    """MySQL管道的基类，封装公共功能"""
    
    def __init__(self, crawler):
        self.crawler = crawler
        self.settings = crawler.settings
        self.logger = get_logger(self.__class__.__name__)

        # 记录管道初始化
        self.logger.info(f"MySQL pipeline initialized: {self.__class__.__name__}")

        # 使用异步锁和初始化标志确保线程安全
        self._pool_lock = asyncio.Lock()
        self._pool_initialized = False
        self.pool = None
        
        # 优先从爬虫的custom_settings中获取表名，如果没有则使用默认值
        spider_table_name = None
        if hasattr(crawler, 'spider') and crawler.spider and hasattr(crawler.spider, 'custom_settings'):
            spider_table_name = crawler.spider.custom_settings.get('MYSQL_TABLE')
            
        self.table_name = (
                spider_table_name or
                self.settings.get('MYSQL_TABLE') or
                getattr(crawler.spider, 'mysql_table', None) or
                f"{getattr(crawler.spider, 'name', 'default')}_items"
        )
        
        # 验证表名是否有效
        if not self.table_name or not isinstance(self.table_name, str):
            raise ValueError(f"Invalid table name: {self.table_name}. Table name must be a non-empty string.")
        
        # 清理表名，移除可能的非法字符
        self.table_name = self.table_name.strip().replace(' ', '_').replace('-', '_')
        
        # 批量插入配置
        self.batch_size = max(1, self.settings.get_int('MYSQL_BATCH_SIZE', 100))  # 确保至少为1
        self.use_batch = self.settings.get_bool('MYSQL_USE_BATCH', False)
        self.batch_buffer: List[Dict] = []  # 批量缓冲区

        # SQL生成配置
        self.auto_update = self.settings.get_bool('MYSQL_AUTO_UPDATE', False)
        self.insert_ignore = self.settings.get_bool('MYSQL_INSERT_IGNORE', False)
        self.update_columns = self.settings.get('MYSQL_UPDATE_COLUMNS', ())
        
        # 验证 update_columns 是否为元组或列表
        if self.update_columns and not isinstance(self.update_columns, (tuple, list)):
            self.logger.warning(f"update_columns should be a tuple or list, got {type(self.update_columns)}. Converting to tuple.")
            self.update_columns = (self.update_columns,)

        # 注册关闭事件
        crawler.subscriber.subscribe(self.spider_closed, event='spider_closed')

    async def process_item(self, item: Item, spider, kwargs: Dict[str, Any] = None) -> Item:
        """处理item的核心方法"""
        kwargs = kwargs or {}
        spider_name = getattr(spider, 'name', 'unknown')  # 获取爬虫名称
        
        # 如果启用批量插入，将item添加到缓冲区
        if self.use_batch:
            self.batch_buffer.append(dict(item))
            
            # 如果缓冲区达到批量大小，执行批量插入
            if len(self.batch_buffer) >= self.batch_size:
                await self._flush_batch(spider_name)
                
            return item
        else:
            # 单条插入逻辑
            try:
                await self._ensure_pool()
                
                # 检查连接池是否有效
                if not self._pool_initialized or not self.pool:
                    raise RuntimeError("Database connection pool is not initialized or invalid")
                
                item_dict = dict(item)
                sql = await self._make_insert_sql(item_dict, **kwargs)

                rowcount = await self._execute_sql(sql=sql)
                if rowcount > 1:
                    self.logger.info(
                        f"爬虫 {spider_name} 成功插入 {rowcount} 条记录到表 {self.table_name}"
                    )
                elif rowcount == 1:
                    self.logger.debug(
                        f"爬虫 {spider_name} 成功插入单条记录到表 {self.table_name}"
                    )
                else:
                    # 当使用 MYSQL_UPDATE_COLUMNS 时，如果更新的字段值与现有记录相同，
                    # MySQL 不会实际更新任何数据，rowcount 会是 0
                    if self.update_columns:
                        self.logger.info(
                            f"爬虫 {spider_name}: SQL执行完成，使用更新列配置 {self.update_columns}，"
                            f"可能未实际更新数据（字段值未变化）"
                        )
                    else:
                        self.logger.warning(
                            f"爬虫 {spider_name}: SQL执行成功但未插入新记录"
                        )

                # 统计计数移到这里，与AiomysqlMySQLPipeline保持一致
                self.crawler.stats.inc_value('mysql/insert_success')
                return item

            except Exception as e:
                # 添加更多调试信息
                error_msg = f"处理失败: {str(e)}"
                self.logger.error(f"处理item时发生错误: {error_msg}")
                self.crawler.stats.inc_value('mysql/insert_failed')
                raise ItemDiscard(error_msg)

    @abstractmethod
    async def _execute_sql(self, sql: str, values: list = None) -> int:
        """执行SQL语句并处理结果 - 子类需要重写此方法"""
        raise NotImplementedError("子类必须实现 _execute_sql 方法")

    @abstractmethod
    async def _execute_batch_sql(self, sql: str, values_list: list) -> int:
        """执行批量SQL语句 - 子类需要重写此方法"""
        raise NotImplementedError("子类必须实现 _execute_batch_sql 方法")

    async def _flush_batch(self, spider_name: str):
        """刷新批量缓冲区并执行批量插入"""
        if not self.batch_buffer:
            return

        try:
            await self._ensure_pool()
            
            # 检查连接池是否有效
            if not self._pool_initialized or not self.pool:
                raise RuntimeError("Database connection pool is not initialized or invalid")
            
            # 使用 SQLBuilder 生成批量插入 SQL
            batch_result = SQLBuilder.make_batch(
                table=self.table_name,
                datas=self.batch_buffer,
                auto_update=self.auto_update,
                update_columns=self.update_columns
            )

            if batch_result:
                sql, values_list = batch_result
                rowcount = await self._execute_batch_sql(sql=sql, values_list=values_list)
                
                if rowcount > 0:
                    self.logger.info(
                        f"爬虫 {spider_name} 批量插入 {len(self.batch_buffer)} 条记录到表 {self.table_name}，实际影响 {rowcount} 行"
                    )
                else:
                    # 当使用 MYSQL_UPDATE_COLUMNS 时，如果更新的字段值与现有记录相同，
                    # MySQL 不会实际更新任何数据，rowcount 会是 0
                    if self.update_columns:
                        self.logger.debug(
                            f"爬虫 {spider_name}: 批量SQL执行完成，使用更新列配置 {self.update_columns}，"
                            f"可能未实际更新数据（字段值未变化）"
                        )
                    else:
                        self.logger.warning(
                            f"爬虫 {spider_name}: 批量SQL执行完成但未插入新记录"
                        )

                # 清空缓冲区
                self.batch_buffer.clear()
                self.crawler.stats.inc_value('mysql/batch_insert_success')
            else:
                self.logger.warning(f"爬虫 {spider_name}: 批量数据为空，跳过插入")

        except Exception as e:
            # 添加更多调试信息
            error_msg = f"批量插入失败: {str(e)}"
            self.logger.error(f"批量处理时发生错误: {error_msg}")
            self.crawler.stats.inc_value('mysql/batch_insert_failed')
            # 不清空缓冲区，以便可能的重试
            # 但如果错误是由于数据问题导致的，可能需要清空缓冲区以避免无限重试
            if "Duplicate entry" in str(e) or "Data too long" in str(e):
                self.logger.warning("由于数据问题导致的错误，清空缓冲区以避免无限重试")
                self.batch_buffer.clear()
            raise ItemDiscard(error_msg)

    async def spider_closed(self):
        """关闭爬虫时清理资源"""
        # 在关闭前刷新剩余的批量数据
        if self.use_batch and self.batch_buffer:
            spider_name = getattr(self.crawler.spider, 'name', 'unknown')
            try:
                await self._flush_batch(spider_name)
            except Exception as e:
                self.logger.error(f"关闭爬虫时刷新批量数据失败: {e}")
        
        # 注意：不再关闭连接池，因为连接池是全局共享的
        # 连接池的关闭由 MySQLConnectionPoolManager.close_all_pools() 统一管理
        if self.pool:
            self.logger.info(
                f"MySQL Pipeline 关闭，但保留全局共享连接池以供其他爬虫使用"
            )
            
    async def _make_insert_sql(self, item_dict: Dict, **kwargs) -> str:
        """生成插入SQL语句，子类可以重写此方法"""
        # 合并管道配置和传入的kwargs参数
        sql_kwargs = {
            'auto_update': self.auto_update,
            'insert_ignore': self.insert_ignore,
            'update_columns': self.update_columns
        }
        sql_kwargs.update(kwargs)
        
        return SQLBuilder.make_insert(
            table=self.table_name, 
            data=item_dict, 
            **sql_kwargs
        )
        
    @abstractmethod
    async def _ensure_pool(self):
        """确保连接池已初始化（线程安全），子类必须实现此方法"""
        pass


class AsyncmyMySQLPipeline(BaseMySQLPipeline):
    """使用asyncmy库的MySQL管道实现"""
    
    def __init__(self, crawler):
        super().__init__(crawler)
        self.logger.info(f"AsyncmyMySQLPipeline instance created, config - host: {self.settings.get('MYSQL_HOST', 'localhost')}, database: {self.settings.get('MYSQL_DB', 'scrapy_db')}, table: {self.table_name}")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    async def _ensure_pool(self):
        """确保连接池已初始化（线程安全）"""
        if self._pool_initialized and self.pool:
            # 检查连接池是否仍然有效
            if hasattr(self.pool, 'closed') and not self.pool.closed:
                return
            else:
                self.logger.warning("连接池已初始化但无效，重新初始化")

        async with self._pool_lock:
            if not self._pool_initialized:  # 双重检查避免竞争条件
                try:
                    # 使用单例连接池管理器
                    self.pool = await MySQLConnectionPoolManager.get_pool(
                        pool_type='asyncmy',
                        host=self.settings.get('MYSQL_HOST', 'localhost'),
                        port=self.settings.get_int('MYSQL_PORT', 3306),
                        user=self.settings.get('MYSQL_USER', 'root'),
                        password=self.settings.get('MYSQL_PASSWORD', ''),
                        db=self.settings.get('MYSQL_DB', 'scrapy_db'),
                        minsize=self.settings.get_int('MYSQL_POOL_MIN', 3),
                        maxsize=self.settings.get_int('MYSQL_POOL_MAX', 10),
                        echo=self.settings.get_bool('MYSQL_ECHO', False)
                    )
                    self._pool_initialized = True
                    self.logger.info(
                        f"MySQL连接池初始化完成（表: {self.table_name}, "
                        f"使用全局共享连接池）"
                    )
                except Exception as e:
                    self.logger.error(f"MySQL连接池初始化失败: {e}")
                    # 重置状态以便重试
                    self._pool_initialized = False
                    self.pool = None
                    raise

    async def _execute_sql(self, sql: str, values: list = None) -> int:
        """执行SQL语句并处理结果，包含死锁重试机制"""
        max_retries = 3
        timeout = 30  # 30秒超时
        
        for attempt in range(max_retries):
            try:
                # 检查连接池状态
                if not self.pool:
                    raise RuntimeError("Database connection pool is not available")
                
                # 使用asyncmy的连接方式，带超时
                async with async_timeout.timeout(timeout):
                    async with self.pool.acquire() as conn:
                        async with conn.cursor() as cursor:
                            # 根据是否有参数值选择不同的执行方法
                            if values is not None:
                                rowcount = await cursor.execute(sql, values)
                            else:
                                rowcount = await cursor.execute(sql)

                            await conn.commit()
                            return rowcount
            except asyncio.TimeoutError:
                self.logger.error(f"执行SQL超时 ({timeout}秒): {sql[:100]}...")
                raise ItemDiscard(f"MySQL操作超时: {sql[:100]}...")
            except Exception as e:
                # 检查是否是死锁错误
                if "Deadlock found" in str(e) and attempt < max_retries - 1:
                    self.logger.warning(f"检测到死锁，正在进行第 {attempt + 1} 次重试: {str(e)}")
                    await asyncio.sleep(0.1 * (2 ** attempt))  # 指数退避
                    continue
                # 检查是否是连接错误，尝试重新初始化连接池
                elif ("Connection closed" in str(e) or "Lost connection" in str(e)) and attempt < max_retries - 1:
                    self.logger.warning(f"检测到连接错误，尝试重新初始化连接池并重试: {str(e)}")
                    self._pool_initialized = False
                    self.pool = None
                    await asyncio.sleep(0.5 * (attempt + 1))  # 简单退避
                    continue
                else:
                    # 添加更多调试信息
                    error_msg = f"MySQL插入失败: {str(e)}"
                    self.logger.error(f"执行SQL时发生错误: {error_msg}")
                    # 如果是批量操作，记录SQL和值以便调试
                    if values:
                        self.logger.debug(f"SQL: {sql[:200]}..., Values: {values[:5] if isinstance(values, list) else '...'}")
                    raise ItemDiscard(error_msg)

    async def _execute_batch_sql(self, sql: str, values_list: list) -> int:
        """执行批量SQL语句，包含死锁重试机制"""
        max_retries = 3
        timeout = 60  # 60秒超时，批量操作可能需要更长时间
        
        for attempt in range(max_retries):
            try:
                # 检查连接池状态
                if not self.pool:
                    raise RuntimeError("Database connection pool is not available")
                
                # 带超时的批量执行
                async with async_timeout.timeout(timeout):
                    async with self.pool.acquire() as conn:
                        async with conn.cursor() as cursor:
                            # 执行批量插入
                            rowcount = await cursor.executemany(sql, values_list)
                            await conn.commit()
                            return rowcount
            except asyncio.TimeoutError:
                self.logger.error(f"执行批量SQL超时 ({timeout}秒)")
                raise ItemDiscard(f"MySQL批量操作超时")
            except Exception as e:
                # 检查是否是死锁错误
                if "Deadlock found" in str(e) and attempt < max_retries - 1:
                    self.logger.warning(f"检测到批量插入死锁，正在进行第 {attempt + 1} 次重试: {str(e)}")
                    await asyncio.sleep(0.1 * (2 ** attempt))  # 指数退避
                    continue
                # 检查是否是连接错误，尝试重新初始化连接池
                elif ("Connection closed" in str(e) or "Lost connection" in str(e)) and attempt < max_retries - 1:
                    self.logger.warning(f"检测到连接错误，尝试重新初始化连接池并重试: {str(e)}")
                    self._pool_initialized = False
                    self.pool = None
                    await asyncio.sleep(0.5 * (attempt + 1))  # 简单退避
                    continue
                else:
                    # 添加更多调试信息
                    error_msg = f"MySQL批量插入失败: {str(e)}"
                    self.logger.error(f"执行批量SQL时发生错误: {error_msg}")
                    # 记录SQL和值的概要以便调试
                    self.logger.debug(f"SQL: {sql[:200]}..., Values count: {len(values_list) if isinstance(values_list, list) else 'unknown'}")
                    raise ItemDiscard(error_msg)


class AiomysqlMySQLPipeline(BaseMySQLPipeline):
    """使用aiomysql库的MySQL管道实现"""
    
    def __init__(self, crawler):
        super().__init__(crawler)
        self.logger.info(f"AiomysqlMySQLPipeline instance created, config - host: {self.settings.get('MYSQL_HOST', 'localhost')}, database: {self.settings.get('MYSQL_DB', 'scrapy_db')}, table: {self.table_name}")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    async def _ensure_pool(self):
        """延迟初始化连接池（线程安全）"""
        if self._pool_initialized and self.pool:
            # 检查连接池是否仍然有效
            if hasattr(self.pool, 'closed') and not self.pool.closed:
                return
            else:
                self.logger.warning("连接池已初始化但无效，重新初始化")

        async with self._pool_lock:
            if not self._pool_initialized:
                try:
                    # 使用单例连接池管理器
                    self.pool = await MySQLConnectionPoolManager.get_pool(
                        pool_type='aiomysql',
                        host=self.settings.get('MYSQL_HOST', 'localhost'),
                        port=self.settings.get_int('MYSQL_PORT', 3306),
                        user=self.settings.get('MYSQL_USER', 'root'),
                        password=self.settings.get('MYSQL_PASSWORD', ''),
                        db=self.settings.get('MYSQL_DB', 'scrapy_db'),
                        minsize=self.settings.get_int('MYSQL_POOL_MIN', 2),
                        maxsize=self.settings.get_int('MYSQL_POOL_MAX', 5)
                    )
                    self._pool_initialized = True
                    self.logger.info(
                        f"aiomysql连接池已初始化（表: {self.table_name}, "
                        f"使用全局共享连接池）"
                    )
                except Exception as e:
                    self.logger.error(f"aiomysql连接池初始化失败: {e}")
                    # 重置状态以便重试
                    self._pool_initialized = False
                    self.pool = None
                    raise

    async def _execute_sql(self, sql: str, values: list = None) -> int:
        """执行SQL语句并处理结果，包含死锁重试机制"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # 使用aiomysql的异步上下文管理器方式
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cursor:
                        # 根据是否有参数值选择不同的执行方法
                        if values is not None:
                            rowcount = await cursor.execute(sql, values)
                        else:
                            rowcount = await cursor.execute(sql)

                        await conn.commit()
                        return rowcount
            except Exception as e:
                # 检查是否是死锁错误
                if "Deadlock found" in str(e) and attempt < max_retries - 1:
                    self.logger.warning(f"检测到死锁，正在进行第 {attempt + 1} 次重试: {str(e)}")
                    await asyncio.sleep(0.1 * (2 ** attempt))  # 指数退避
                    continue
                else:
                    # 添加更多调试信息
                    error_msg = f"MySQL插入失败: {str(e)}"
                    self.logger.error(f"执行SQL时发生错误: {error_msg}")
                    raise ItemDiscard(error_msg)

    async def _execute_batch_sql(self, sql: str, values_list: list) -> int:
        """执行批量SQL语句，包含死锁重试机制"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cursor:
                        # 执行批量插入
                        rowcount = await cursor.executemany(sql, values_list)
                        await conn.commit()
                        return rowcount
            except Exception as e:
                # 检查是否是死锁错误
                if "Deadlock found" in str(e) and attempt < max_retries - 1:
                    self.logger.warning(f"检测到批量插入死锁，正在进行第 {attempt + 1} 次重试: {str(e)}")
                    await asyncio.sleep(0.1 * (2 ** attempt))  # 指数退避
                    continue
                else:
                    # 添加更多调试信息
                    error_msg = f"MySQL批量插入失败: {str(e)}"
                    self.logger.error(f"执行批量SQL时发生错误: {error_msg}")
                    raise ItemDiscard(error_msg)
```

**code file end: crawlo/pipelines/mysql_pipeline.py**

---


### code file start: crawlo/pipelines/pipeline_manager.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
from typing import List
from pprint import pformat
from asyncio import create_task

from crawlo.logging import get_logger
from crawlo.event import CrawlerEvent
from crawlo.utils.misc import load_object
from crawlo.project import common_call
from crawlo.exceptions import PipelineInitError, ItemDiscard, InvalidOutputError


def get_dedup_pipeline_classes():
    """获取所有已知的去重管道类名"""
    return [
        'crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline',
        'crawlo.pipelines.redis_dedup_pipeline.RedisDedupPipeline',
        'crawlo.pipelines.bloom_dedup_pipeline.BloomDedupPipeline',
        'crawlo.pipelines.database_dedup_pipeline.DatabaseDedupPipeline'
    ]


def remove_dedup_pipelines(pipelines: List[str]) -> List[str]:
    """从管道列表中移除所有去重管道"""
    dedup_classes = get_dedup_pipeline_classes()
    return [pipeline for pipeline in pipelines if pipeline not in dedup_classes]


class PipelineManager:

    def __init__(self, crawler):
        self.crawler = crawler
        self.pipelines: List = []
        self.methods: List = []

        self.logger = get_logger(self.__class__.__name__)
        pipelines = self.crawler.settings.get_list('PIPELINES')
        dedup_pipeline = self.crawler.settings.get('DEFAULT_DEDUP_PIPELINE')

        # 添加调试信息
        self.logger.debug(f"PIPELINES from settings: {pipelines}")
        self.logger.debug(f"DEFAULT_DEDUP_PIPELINE from settings: {dedup_pipeline}")

        # 确保DEFAULT_DEDUP_PIPELINE被添加到管道列表开头
        if dedup_pipeline:
            # 移除所有去重管道实例（如果存在）
            pipelines = remove_dedup_pipelines(pipelines)
            # 在开头插入去重管道
            self.logger.debug(f"{dedup_pipeline} insert successful")
            pipelines.insert(0, dedup_pipeline)

        self._add_pipelines(pipelines)
        self._add_methods()

    @classmethod
    def from_crawler(cls, *args, **kwargs):
        o = cls(*args, **kwargs)
        return o

    def _add_pipelines(self, pipelines):
        for pipeline in pipelines:
            try:
                pipeline_cls = load_object(pipeline)
                if not hasattr(pipeline_cls, 'from_crawler'):
                    raise PipelineInitError(
                        f"Pipeline init failed, must inherit from `BasePipeline` or have a `from_crawler` method"
                    )
                self.pipelines.append(pipeline_cls.from_crawler(self.crawler))
            except Exception as e:
                self.logger.error(f"Failed to load pipeline {pipeline}: {e}")
                # 可以选择继续加载其他管道或抛出异常
                raise
        if pipelines:
            # 恢复INFO级别日志，保留关键的启用信息
            self.logger.info(f"enabled pipelines: \n {pformat(pipelines)}")

    def _add_methods(self):
        for pipeline in self.pipelines:
            if hasattr(pipeline, 'process_item'):
                self.methods.append(pipeline.process_item)

    async def process_item(self, item):
        try:
            for i, method in enumerate(self.methods):
                self.logger.debug(f"Processing item with pipeline method {i}: {method.__qualname__}")
                try:
                    item = await common_call(method, item, self.crawler.spider)
                    if item is None:
                        raise InvalidOutputError(f"{method.__qualname__} return None is not supported.")
                except ItemDiscard as exc:
                    self.logger.debug(f"Item discarded by pipeline: {exc}")
                    create_task(self.crawler.subscriber.notify(CrawlerEvent.ITEM_DISCARD, item, exc, self.crawler.spider))
                    # 重新抛出异常，确保上层调用者也能捕获到，并停止执行后续管道
                    raise
        except ItemDiscard:
            # 异常已经被处理和通知，这里只需要重新抛出
            raise
        else:
            create_task(self.crawler.subscriber.notify(CrawlerEvent.ITEM_SUCCESSFUL, item, self.crawler.spider))

```

**code file end: crawlo/pipelines/pipeline_manager.py**

---


### code file start: crawlo/pipelines/redis_dedup_pipeline.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
基于 Redis 的数据项去重管道
========================
提供分布式环境下的数据项去重功能，防止保存重复的数据记录。

特点:
- 分布式支持: 多节点共享去重数据
- 高性能: 使用 Redis 集合进行快速查找
- 可配置: 支持自定义 Redis 连接参数
- 容错设计: 网络异常时不会丢失数据
"""
import redis
import hashlib
from typing import Optional

from crawlo import Item
from crawlo.spider import Spider
from crawlo.exceptions import ItemDiscard
from crawlo.utils.fingerprint import FingerprintGenerator
from crawlo.logging import get_logger


class RedisDedupPipeline:
    """基于 Redis 的数据项去重管道"""

    def __init__(
            self,
            redis_host: str = 'localhost',
            redis_port: int = 6379,
            redis_db: int = 0,
            redis_password: Optional[str] = None,
            redis_key: str = 'crawlo:item_fingerprints'
    ):
        """
        初始化 Redis 去重管道
        
        :param redis_host: Redis 主机地址
        :param redis_port: Redis 端口
        :param redis_db: Redis 数据库编号
        :param redis_password: Redis 密码
        :param redis_key: 存储指纹的 Redis 键名
        """
        self.logger = get_logger(self.__class__.__name__)
        
        # 初始化 Redis 连接
        try:
            self.redis_client = redis.Redis(
                host=redis_host,
                port=redis_port,
                db=redis_db,
                password=redis_password,
                decode_responses=True,
                socket_connect_timeout=5,
                socket_timeout=5
            )
            # 测试连接
            self.redis_client.ping()
        except Exception as e:
            self.logger.error(f"Redis connection failed: {e}")
            raise RuntimeError(f"Redis 连接失败: {e}")

        self.redis_key = redis_key
        self.dropped_count = 0

    @classmethod
    def from_crawler(cls, crawler):
        """从爬虫配置创建管道实例"""
        settings = crawler.settings
        
        # 使用统一的Redis key命名规范: crawlo:{project_name}:item:fingerprint
        project_name = settings.get('PROJECT_NAME', 'default')
        redis_key = f"crawlo:{project_name}:item:fingerprint"
        
        return cls(
            redis_host=settings.get('REDIS_HOST', 'localhost'),
            redis_port=settings.get_int('REDIS_PORT', 6379),
            redis_db=settings.get_int('REDIS_DB', 0),
            redis_password=settings.get('REDIS_PASSWORD') or None,
            redis_key=redis_key
        )

    def process_item(self, item: Item, spider: Spider) -> Item:
        """
        处理数据项，进行去重检查
        
        :param item: 要处理的数据项
        :param spider: 爬虫实例
        :return: 处理后的数据项或抛出 ItemDiscard 异常
        """
        try:
            # 生成数据项指纹
            fingerprint = self._generate_item_fingerprint(item)
            
            # 使用 Redis 的 SADD 命令检查并添加指纹
            # 如果指纹已存在，SADD 返回 0；如果指纹是新的，SADD 返回 1
            is_new = self.redis_client.sadd(self.redis_key, fingerprint)
            
            if not is_new:
                # 如果指纹已存在，丢弃这个数据项
                self.dropped_count += 1
                self.logger.info(f"Dropping duplicate item: {fingerprint}")
                raise ItemDiscard(f"Duplicate item: {fingerprint}")
            else:
                # 如果是新数据项，继续处理
                self.logger.debug(f"Processing new item: {fingerprint}")
                return item
                
        except redis.RedisError as e:
            self.logger.error(f"Redis error: {e}")
            # 在 Redis 错误时继续处理，避免丢失数据
            return item
        except ItemDiscard:
            # 重新抛出ItemDiscard异常，确保管道管理器能正确处理
            raise
        except Exception as e:
            self.logger.error(f"Error processing item: {e}")
            # 在其他错误时继续处理
            return item

    def _generate_item_fingerprint(self, item: Item) -> str:
        """
        生成数据项指纹
        
        基于数据项的所有字段生成唯一指纹，用于去重判断。
        
        :param item: 数据项
        :return: 指纹字符串
        """
        return FingerprintGenerator.item_fingerprint(item)

    def close_spider(self, spider: Spider) -> None:
        """
        爬虫关闭时的清理工作
        
        :param spider: 爬虫实例
        """
        try:
            # 获取去重统计信息
            total_items = self.redis_client.scard(self.redis_key)
            self.logger.info(f"Spider {spider.name} closed:")
            self.logger.info(f"  - Dropped duplicate items: {self.dropped_count}")
            self.logger.info(f"  - Fingerprints stored in Redis: {total_items}")
            
            # 注意：默认情况下不清理 Redis 中的指纹
            # 如果需要清理，可以在设置中配置
            # 安全访问crawler和settings
            crawler = getattr(spider, 'crawler', None)
            if crawler and hasattr(crawler, 'settings'):
                settings = crawler.settings
                if settings.getbool('REDIS_DEDUP_CLEANUP', False):
                    deleted = self.redis_client.delete(self.redis_key)
                    self.logger.info(f"  - Cleaned fingerprints: {deleted}")
        except Exception as e:
            self.logger.error(f"Error closing spider: {e}")
```

**code file end: crawlo/pipelines/redis_dedup_pipeline.py**

---


### code file start: crawlo/pipelines/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Pipeline 模块
=============

Pipeline体系：
- BasePipeline: 基础抽象类，定义Pipeline接口规范
- ResourceManagedPipeline: 提供资源管理功能（推荐使用）
- FileBasedPipeline/DatabasePipeline/CacheBasedPipeline: 特定场景的专用基类

内置去重Pipeline：
- MemoryDedupPipeline: 基于内存的去重
- RedisDedupPipeline: 基于Redis的分布式去重
- BloomDedupPipeline: 基于Bloom Filter的高效去重
- DatabaseDedupPipeline: 基于数据库的去重

使用示例：
    # 在settings.py中配置
    PIPELINES = [
        'crawlo.pipelines.RedisDedupPipeline',
        'your_project.pipelines.MongoPipeline',
    ]
"""

# 导入所有基类（从base_pipeline.py）
from .base_pipeline import (
    BasePipeline,
    ResourceManagedPipeline,
    FileBasedPipeline,
    DatabasePipeline,
    CacheBasedPipeline
)

# 导出去重管道
from .memory_dedup_pipeline import MemoryDedupPipeline
from .redis_dedup_pipeline import RedisDedupPipeline
from .bloom_dedup_pipeline import BloomDedupPipeline
from .database_dedup_pipeline import DatabaseDedupPipeline

__all__ = [
    # 基类
    'BasePipeline',
    'ResourceManagedPipeline',
    'FileBasedPipeline', 
    'DatabasePipeline',
    'CacheBasedPipeline',
    # 去重管道
    'MemoryDedupPipeline',
    'RedisDedupPipeline', 
    'BloomDedupPipeline',
    'DatabaseDedupPipeline'
]
```

**code file end: crawlo/pipelines/__init__.py**

---


### code file start: crawlo/queue/pqueue.py 

```python
# -*- coding:UTF-8 -*-
import asyncio
import sys
from asyncio import PriorityQueue
from typing import Optional, Any


class SpiderPriorityQueue(PriorityQueue):
    """带超时功能的异步优先级队列"""

    def __init__(self, maxsize: int = 0) -> None:
        """初始化队列，maxsize为0表示无大小限制"""
        super().__init__(maxsize)

    async def get(self, timeout: float = 0.01) -> Optional[Any]:
        """
        异步获取队列元素，带超时功能

        Args:
            timeout: 超时时间（秒），默认0.01秒

        Returns:
            队列元素(优先级, 值)或None(超时)
        """
        try:
            # 根据Python版本选择超时实现方式
            if sys.version_info >= (3, 11):
                async with asyncio.timeout(timeout):
                    item = await super().get()
                    return item
            else:
                item = await asyncio.wait_for(super().get(), timeout=timeout)
                return item
        except asyncio.TimeoutError:
            return None

    def qsize(self) -> int:
        """获取队列大小"""
        return super().qsize()
```

**code file end: crawlo/queue/pqueue.py**

---


### code file start: crawlo/queue/queue_manager.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
统一的队列管理器
提供简洁、一致的队列接口，自动处理不同队列类型的差异
"""
import asyncio
import time
import traceback
from enum import Enum
from typing import Optional, Dict, Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from crawlo import Request

from crawlo.queue.pqueue import SpiderPriorityQueue
from crawlo.utils.error_handler import ErrorHandler
from crawlo.logging import get_logger
from crawlo.utils.request_serializer import RequestSerializer

try:
    # 使用完整版Redis队列
    from crawlo.queue.redis_priority_queue import RedisPriorityQueue

    REDIS_AVAILABLE = True
except ImportError:
    RedisPriorityQueue = None
    REDIS_AVAILABLE = False


class QueueType(Enum):
    """Queue type enumeration"""
    MEMORY = "memory"
    REDIS = "redis"
    AUTO = "auto"  # 自动选择


class IntelligentScheduler:
    """智能调度器"""

    def __init__(self):
        self.domain_stats = {}  # 域名统计信息
        self.url_stats = {}  # URL统计信息
        self.last_request_time = {}  # 最后请求时间

    def calculate_priority(self, request: "Request") -> int:
        """计算请求的智能优先级"""
        priority = getattr(request, 'priority', 0)

        # 获取域名
        domain = self._extract_domain(request.url)

        # 基于域名访问频率调整优先级
        if domain in self.domain_stats:
            domain_access_count = self.domain_stats[domain]['count']
            last_access_time = self.domain_stats[domain]['last_time']

            # 如果最近访问过该域名，降低优先级（避免过度集中访问同一域名）
            time_since_last = time.time() - last_access_time
            if time_since_last < 5:  # 5秒内访问过
                priority -= 2
            elif time_since_last < 30:  # 30秒内访问过
                priority -= 1

            # 如果该域名访问次数过多，进一步降低优先级
            if domain_access_count > 10:
                priority -= 1

        # 基于URL访问历史调整优先级
        if request.url in self.url_stats:
            url_access_count = self.url_stats[request.url]
            if url_access_count > 1:
                # 重复URL降低优先级
                priority -= url_access_count

        # 基于深度调整优先级
        depth = getattr(request, 'meta', {}).get('depth', 0)
        priority -= depth  # 深度越大，优先级越低

        return priority

    def update_stats(self, request: "Request"):
        """更新统计信息"""
        domain = self._extract_domain(request.url)

        # 更新域名统计
        if domain not in self.domain_stats:
            self.domain_stats[domain] = {'count': 0, 'last_time': 0}

        self.domain_stats[domain]['count'] += 1
        self.domain_stats[domain]['last_time'] = time.time()

        # 更新URL统计
        if request.url not in self.url_stats:
            self.url_stats[request.url] = 0
        self.url_stats[request.url] += 1

        # 更新最后请求时间
        self.last_request_time[domain] = time.time()

    def _extract_domain(self, url: str) -> str:
        """提取域名"""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            return parsed.netloc
        except:
            return "unknown"


class QueueConfig:
    """Queue configuration class"""

    def __init__(
            self,
            queue_type: Union[QueueType, str] = QueueType.AUTO,
            redis_url: Optional[str] = None,
            redis_host: str = "127.0.0.1",
            redis_port: int = 6379,
            redis_password: Optional[str] = None,
            redis_db: int = 0,
            queue_name: str = "crawlo:requests",
            max_queue_size: int = 1000,
            max_retries: int = 3,
            timeout: int = 300,
            run_mode: Optional[str] = None,  # 新增：运行模式
            **kwargs
    ):
        self.queue_type = QueueType(queue_type) if isinstance(queue_type, str) else queue_type
        self.run_mode = run_mode  # 保存运行模式

        # Redis 配置
        if redis_url:
            self.redis_url = redis_url
        else:
            if redis_password:
                self.redis_url = f"redis://:{redis_password}@{redis_host}:{redis_port}/{redis_db}"
            else:
                self.redis_url = f"redis://{redis_host}:{redis_port}/{redis_db}"

        self.queue_name = queue_name
        self.max_queue_size = max_queue_size
        self.max_retries = max_retries
        self.timeout = timeout
        self.extra_config = kwargs

    @classmethod
    def from_settings(cls, settings) -> 'QueueConfig':
        """Create configuration from settings"""
        # 获取项目名称，用于生成默认队列名称
        project_name = settings.get('PROJECT_NAME', 'default')
        default_queue_name = f"crawlo:{project_name}:queue:requests"
        
        # 如果设置了SCHEDULER_QUEUE_NAME，则使用该值，否则使用基于项目名称的默认值
        scheduler_queue_name = settings.get('SCHEDULER_QUEUE_NAME')
        if scheduler_queue_name is not None:
            queue_name = scheduler_queue_name
        else:
            queue_name = default_queue_name
        
        return cls(
            queue_type=settings.get('QUEUE_TYPE', QueueType.AUTO),
            redis_url=settings.get('REDIS_URL'),
            redis_host=settings.get('REDIS_HOST', '127.0.0.1'),
            redis_port=settings.get_int('REDIS_PORT', 6379),
            redis_password=settings.get('REDIS_PASSWORD'),
            redis_db=settings.get_int('REDIS_DB', 0),
            queue_name=queue_name,
            max_queue_size=settings.get_int('SCHEDULER_MAX_QUEUE_SIZE', 1000),
            max_retries=settings.get_int('QUEUE_MAX_RETRIES', 3),
            timeout=settings.get_int('QUEUE_TIMEOUT', 300),
            run_mode=settings.get('RUN_MODE')  # 传递运行模式
        )


class QueueManager:
    """Unified queue manager"""

    def __init__(self, config: QueueConfig):
        self.config = config
        # 延迟初始化logger和error_handler避免循环依赖
        self._logger = None
        self._error_handler = None
        self.request_serializer = RequestSerializer()
        self._queue = None
        self._queue_semaphore = None
        self._queue_type = None
        self._health_status = "unknown"
        self._intelligent_scheduler = IntelligentScheduler()  # 智能调度器

    @property
    def logger(self):
        if self._logger is None:
            self._logger = get_logger(self.__class__.__name__)
        return self._logger

    @property
    def error_handler(self):
        if self._error_handler is None:
            self._error_handler = ErrorHandler(self.__class__.__name__)
        return self._error_handler

    async def initialize(self) -> bool:
        """初始化队列"""
        try:
            queue_type = await self._determine_queue_type()
            self._queue = await self._create_queue(queue_type)
            self._queue_type = queue_type

            # 测试队列健康状态
            health_check_result = await self._health_check()

            self.logger.info(f"Queue initialized successfully Type: {queue_type.value}")
            # 只在调试模式下输出详细配置信息
            self.logger.debug(f"Queue configuration: {self._get_queue_info()}")

            # 如果健康检查返回True，表示队列类型发生了切换，需要更新配置
            if health_check_result:
                return True

            # 如果队列类型是Redis，检查是否需要更新配置
            if queue_type == QueueType.REDIS:
                # 这个检查需要在调度器中进行，因为队列管理器无法访问crawler.settings
                # 但我们不需要总是返回True，只有在确实需要更新时才返回True
                # 调度器会进行更详细的检查
                pass

            return False  # 默认不需要更新配置

        except RuntimeError as e:
            # Distributed 模式下的 RuntimeError 必须重新抛出
            if self.config.run_mode == 'distributed':
                self.logger.error(f"Queue initialization failed: {e}")
                self._health_status = "error"
                raise  # 重新抛出异常
            # 其他模式记录错误但不抛出
            self.logger.error(f"Queue initialization failed: {e}")
            self.logger.debug(f"详细错误信息:\n{traceback.format_exc()}")
            self._health_status = "error"
            return False
        except Exception as e:
            # 记录详细的错误信息和堆栈跟踪
            self.logger.error(f"Queue initialization failed: {e}")
            self.logger.debug(f"详细错误信息:\n{traceback.format_exc()}")
            self._health_status = "error"
            return False

    async def put(self, request: "Request", priority: int = 0) -> bool:
        """Unified enqueue interface"""
        if not self._queue:
            raise RuntimeError("队列未初始化")

        try:
            # 应用智能调度算法计算优先级
            intelligent_priority = self._intelligent_scheduler.calculate_priority(request)
            # 结合原始优先级和智能优先级
            final_priority = priority + intelligent_priority

            # 更新统计信息
            self._intelligent_scheduler.update_stats(request)

            # 序列化处理（仅对 Redis 队列）
            if self._queue_type == QueueType.REDIS:
                request = self.request_serializer.prepare_for_serialization(request)

            # 背压控制（仅对内存队列）
            if self._queue_semaphore:
                # 对于大量请求，使用阻塞式等待而不是跳过
                # 这样可以确保不会丢失任何请求
                await self._queue_semaphore.acquire()

            # 统一的入队操作
            if hasattr(self._queue, 'put'):
                if self._queue_type == QueueType.REDIS:
                    success = await self._queue.put(request, final_priority)
                else:
                    # 对于内存队列，我们需要手动处理优先级
                    # 在SpiderPriorityQueue中，元素应该是(priority, item)的元组
                    await self._queue.put((final_priority, request))
                    success = True
            else:
                raise RuntimeError(f"队列类型 {self._queue_type} 不支持 put 操作")

            if success:
                self.logger.debug(f"Request enqueued successfully: {request.url} with priority {final_priority}")

            return success

        except Exception as e:
            self.logger.error(f"Failed to enqueue request: {e}")
            if self._queue_semaphore:
                self._queue_semaphore.release()
            return False

    async def get(self, timeout: float = 5.0) -> Optional["Request"]:
        """Unified dequeue interface"""
        if not self._queue:
            raise RuntimeError("队列未初始化")

        try:
            request = await self._queue.get(timeout=timeout)

            # 释放信号量（仅对内存队列）
            if self._queue_semaphore and request:
                self._queue_semaphore.release()

            # 反序列化处理（仅对 Redis 队列）
            if request and self._queue_type == QueueType.REDIS:
                # 这里需要 spider 实例，暂时返回原始请求
                # 实际的 callback 恢复在 scheduler 中处理
                pass

            # 如果是内存队列，需要解包(priority, request)元组
            if request and self._queue_type == QueueType.MEMORY:
                if isinstance(request, tuple) and len(request) == 2:
                    request = request[1]  # 取元组中的请求对象

            return request

        except Exception as e:
            self.logger.error(f"Failed to dequeue request: {e}")
            return None

    async def size(self) -> int:
        """Get queue size"""
        if not self._queue:
            return 0

        try:
            if hasattr(self._queue, 'qsize'):
                if asyncio.iscoroutinefunction(self._queue.qsize):
                    return await self._queue.qsize()
                else:
                    return self._queue.qsize()
            return 0
        except Exception as e:
            self.logger.warning(f"Failed to get queue size: {e}")
            return 0

    def empty(self) -> bool:
        """Check if queue is empty (synchronous version, for compatibility)"""
        try:
            # 对于内存队列，可以同步检查
            if self._queue_type == QueueType.MEMORY:
                # 确保正确检查队列大小
                if hasattr(self._queue, 'qsize'):
                    return self._queue.qsize() == 0
                else:
                    # 如果没有qsize方法，假设队列为空
                    return True
            # 对于 Redis 队列，由于需要异步操作，这里返回近似值
            # 为了确保程序能正常退出，我们返回True，让上层通过更精确的异步检查来判断
            return True
        except Exception:
            return True

    async def async_empty(self) -> bool:
        """Check if queue is empty (asynchronous version, more accurate)"""
        try:
            # 对于内存队列
            if self._queue_type == QueueType.MEMORY:
                # 确保正确检查队列大小
                if hasattr(self._queue, 'qsize'):
                    if asyncio.iscoroutinefunction(self._queue.qsize):
                        size = await self._queue.qsize()
                    else:
                        size = self._queue.qsize()
                    return size == 0
                else:
                    # 如果没有qsize方法，假设队列为空
                    return True
            # 对于 Redis 队列，使用异步检查
            elif self._queue_type == QueueType.REDIS:
                size = await self.size()
                return size == 0
            return True
        except Exception:
            return True

    async def close(self) -> None:
        """Close queue"""
        if self._queue and hasattr(self._queue, 'close'):
            try:
                await self._queue.close()
                # Change INFO level log to DEBUG level to avoid redundant output
                self.logger.debug("Queue closed")
            except Exception as e:
                self.logger.warning(f"Error closing queue: {e}")

    def get_status(self) -> Dict[str, Any]:
        """Get queue status information"""
        return {
            "type": self._queue_type.value if self._queue_type else "unknown",
            "health": self._health_status,
            "config": self._get_queue_info(),
            "initialized": self._queue is not None
        }

    async def _determine_queue_type(self) -> QueueType:
        """Determine queue type"""
        if self.config.queue_type == QueueType.AUTO:
            # 自动选择：优先使用 Redis（如果可用）
            if REDIS_AVAILABLE and self.config.redis_url:
                # 测试 Redis 连接
                try:
                    from crawlo.queue.redis_priority_queue import RedisPriorityQueue
                    test_queue = RedisPriorityQueue(self.config.redis_url)
                    await test_queue.connect()
                    await test_queue.close()
                    self.logger.debug("Auto-detection: Redis available, using distributed queue")
                    return QueueType.REDIS
                except Exception as e:
                    self.logger.debug(f"Auto-detection: Redis unavailable ({e}), using memory queue")
                    return QueueType.MEMORY
            else:
                self.logger.debug("Auto-detection: Redis not configured, using memory queue")
                return QueueType.MEMORY

        elif self.config.queue_type == QueueType.REDIS:
            # Distributed 模式：必须使用 Redis，不允许降级
            if self.config.run_mode == 'distributed':
                # 分布式模式必须确保 Redis 可用
                if not REDIS_AVAILABLE:
                    error_msg = (
                        "Distributed 模式要求 Redis 可用，但 Redis 客户端库未安装。\n"
                        "请安装 Redis 支持: pip install redis"
                    )
                    self.logger.error(error_msg)
                    raise RuntimeError(error_msg)
                
                if not self.config.redis_url:
                    error_msg = (
                        "Distributed 模式要求配置 Redis 连接信息。\n"
                        "请在 settings.py 中配置 REDIS_HOST、REDIS_PORT 等参数"
                    )
                    self.logger.error(error_msg)
                    raise RuntimeError(error_msg)
                
                # 测试 Redis 连接
                try:
                    from crawlo.queue.redis_priority_queue import RedisPriorityQueue
                    test_queue = RedisPriorityQueue(self.config.redis_url)
                    await test_queue.connect()
                    await test_queue.close()
                    self.logger.debug("Distributed mode: Redis connection verified")
                    return QueueType.REDIS
                except Exception as e:
                    error_msg = (
                        f"Distributed 模式要求 Redis 可用，但无法连接到 Redis 服务器。\n"
                        f"错误信息: {e}\n"
                        f"Redis URL: {self.config.redis_url}\n"
                        f"请检查：\n"
                        f"  1. Redis 服务是否正在运行\n"
                        f"  2. Redis 连接配置是否正确\n"
                        f"  3. 网络连接是否正常"
                    )
                    self.logger.error(error_msg)
                    raise RuntimeError(error_msg) from e
            else:
                # 非 distributed 模式：QUEUE_TYPE='redis' 时允许降级到 memory
                # 这提供了向后兼容性和更好的容错性
                if REDIS_AVAILABLE and self.config.redis_url:
                    # 测试 Redis 连接
                    try:
                        from crawlo.queue.redis_priority_queue import RedisPriorityQueue
                        test_queue = RedisPriorityQueue(self.config.redis_url)
                        await test_queue.connect()
                        await test_queue.close()
                        self.logger.debug("Redis mode: Redis available, using distributed queue")
                        return QueueType.REDIS
                    except Exception as e:
                        self.logger.warning(f"Redis mode: Redis unavailable ({e}), falling back to memory queue")
                        return QueueType.MEMORY
                else:
                    self.logger.warning("Redis mode: Redis not configured, falling back to memory queue")
                    return QueueType.MEMORY

        elif self.config.queue_type == QueueType.MEMORY:
            return QueueType.MEMORY

        else:
            raise ValueError(f"不支持的队列类型: {self.config.queue_type}")

    async def _create_queue(self, queue_type: QueueType):
        """Create queue instance"""
        if queue_type == QueueType.REDIS:
            # 延迟导入Redis队列
            try:
                from crawlo.queue.redis_priority_queue import RedisPriorityQueue
            except ImportError as e:
                raise RuntimeError(f"Redis队列不可用：未能导入RedisPriorityQueue ({e})")

            # 修复项目名称提取逻辑，严格按照测试文件中的逻辑实现
            project_name = "default"
            if ':' in self.config.queue_name:
                parts = self.config.queue_name.split(':')
                if len(parts) >= 2:
                    # 处理可能的双重 crawlo 前缀
                    if parts[0] == "crawlo" and parts[1] == "crawlo":
                        # 双重 crawlo 前缀，取"crawlo"作为项目名称
                        project_name = "crawlo"
                    elif parts[0] == "crawlo":
                        # 正常的 crawlo 前缀，取第二个部分作为项目名称
                        project_name = parts[1]
                    else:
                        # 没有 crawlo 前缀，使用第一个部分作为项目名称
                        project_name = parts[0]
                else:
                    project_name = self.config.queue_name or "default"
            else:
                project_name = self.config.queue_name or "default"

            queue = RedisPriorityQueue(
                redis_url=self.config.redis_url,
                queue_name=self.config.queue_name,
                max_retries=self.config.max_retries,
                timeout=self.config.timeout,
                module_name=project_name  # 传递项目名称作为module_name
            )
            # 不需要立即连接，使用 lazy connect
            return queue

        elif queue_type == QueueType.MEMORY:
            queue = SpiderPriorityQueue()
            # 为内存队列设置背压控制
            self._queue_semaphore = asyncio.Semaphore(self.config.max_queue_size)
            return queue

        else:
            raise ValueError(f"不支持的队列类型: {queue_type}")

    async def _health_check(self) -> bool:
        """Health check"""
        try:
            if self._queue_type == QueueType.REDIS:
                # 测试 Redis 连接
                await self._queue.connect()
                self._health_status = "healthy"
            else:
                # 内存队列总是健康的
                self._health_status = "healthy"
                return False  # 内存队列不需要更新配置
        except Exception as e:
            self.logger.warning(f"Queue health check failed: {e}")
            self._health_status = "unhealthy"
            
            # Distributed 模式下 Redis 健康检查失败应该报错
            if self.config.run_mode == 'distributed':
                error_msg = (
                    f"Distributed 模式下 Redis 健康检查失败。\n"
                    f"错误信息: {e}\n"
                    f"Redis URL: {self.config.redis_url}\n"
                    f"分布式模式不允许降级到内存队列，请修复 Redis 连接问题。"
                )
                self.logger.error(error_msg)
                raise RuntimeError(error_msg) from e
            
            # 非 Distributed 模式：如果是Redis队列且健康检查失败，尝试切换到内存队列
            # 对于 AUTO 模式允许回退
            if self._queue_type == QueueType.REDIS and self.config.queue_type == QueueType.AUTO:
                self.logger.info("Redis queue unavailable, attempting to switch to memory queue...")
                try:
                    await self._queue.close()
                except:
                    pass
                self._queue = None
                # 重新创建内存队列
                self._queue = await self._create_queue(QueueType.MEMORY)
                self._queue_type = QueueType.MEMORY
                self._queue_semaphore = asyncio.Semaphore(self.config.max_queue_size)
                self._health_status = "healthy"
                self.logger.info("Switched to memory queue")
                # 返回一个信号，表示需要更新过滤器和去重管道配置
                return True
        return False

    def _get_queue_info(self) -> Dict[str, Any]:
        """Get queue configuration information"""
        info = {
            "queue_name": self.config.queue_name,
            "max_queue_size": self.config.max_queue_size
        }

        if self._queue_type == QueueType.REDIS:
            info.update({
                "redis_url": self.config.redis_url,
                "max_retries": self.config.max_retries,
                "timeout": self.config.timeout
            })

        return info

```

**code file end: crawlo/queue/queue_manager.py**

---


### code file start: crawlo/queue/redis_priority_queue.py 

```python
import asyncio
import pickle
import time
import traceback
from typing import Optional, TYPE_CHECKING, List, Union, Any

import redis.asyncio as aioredis

# 尝试导入Redis集群支持
try:
    from redis.asyncio.cluster import RedisCluster
    REDIS_CLUSTER_AVAILABLE = True
except ImportError:
    RedisCluster = None
    REDIS_CLUSTER_AVAILABLE = False

# 使用 TYPE_CHECKING 避免运行时循环导入
if TYPE_CHECKING:
    from crawlo import Request

from crawlo.utils.error_handler import ErrorHandler, ErrorContext
from crawlo.logging import get_logger
from crawlo.utils.redis_connection_pool import get_redis_pool, RedisConnectionPool
from crawlo.utils.request_serializer import RequestSerializer

# 延迟初始化避免循环依赖
_logger = None
_error_handler = None


def get_module_logger():
    global _logger
    if _logger is None:
        _logger = get_logger(__name__)
    return _logger


def get_module_error_handler():
    global _error_handler
    if _error_handler is None:
        _error_handler = ErrorHandler(__name__)
    return _error_handler


class RedisPriorityQueue:
    """
    基于 Redis 的分布式异步优先级队列
    """

    def __init__(
            self,
            redis_url: Optional[str] = None,
            queue_name: Optional[str] = None,  # 修改默认值为 None
            processing_queue: Optional[str] = None,  # 修改默认值为 None
            failed_queue: Optional[str] = None,  # 修改默认值为 None
            max_retries: int = 3,
            timeout: int = 300,  # 任务处理超时时间（秒）
            max_connections: int = 10,  # 连接池大小
            module_name: str = "default",  # 添加 module_name 参数
            is_cluster: bool = False,  # 是否为集群模式
            cluster_nodes: Optional[List[str]] = None  # 集群节点列表
    ):
        # 移除直接使用 os.getenv()，要求通过参数传递 redis_url
        if redis_url is None:
            # 如果没有提供 redis_url，则抛出异常，要求在 settings 中配置
            raise ValueError("redis_url must be provided. Configure it in settings instead of using os.getenv()")

        self.redis_url = redis_url
        self.module_name = module_name  # 保存 module_name
        self.is_cluster = is_cluster
        self.cluster_nodes = cluster_nodes

        # 如果未提供 queue_name，则根据 module_name 自动生成
        if queue_name is None:
            self.queue_name = f"crawlo:{module_name}:queue:requests"
        else:
            # 处理多重 crawlo 前缀，规范化队列名称
            self.queue_name = self._normalize_queue_name(queue_name)

        # 如果未提供 processing_queue，则根据 queue_name 自动生成
        if processing_queue is None:
            if ":queue:requests" in self.queue_name:
                self.processing_queue = self.queue_name.replace(":queue:requests", ":queue:processing")
            else:
                self.processing_queue = f"{self.queue_name}:processing"
        else:
            self.processing_queue = processing_queue

        # 如果未提供 failed_queue，则根据 queue_name 自动生成
        if failed_queue is None:
            if ":queue:requests" in self.queue_name:
                self.failed_queue = self.queue_name.replace(":queue:requests", ":queue:failed")
            else:
                self.failed_queue = f"{self.queue_name}:failed"
        else:
            self.failed_queue = failed_queue

        self.max_retries = max_retries
        self.timeout = timeout
        self.max_connections = max_connections
        self._redis_pool: Optional[RedisConnectionPool] = None
        self._redis: Optional[Any] = None
        self._lock = asyncio.Lock()  # 用于连接初始化的锁
        self.request_serializer = RequestSerializer()  # 处理序列化

    def _normalize_queue_name(self, queue_name: str) -> str:
        """
        规范化队列名称，处理多重 crawlo 前缀
        
        :param queue_name: 原始队列名称
        :return: 规范化后的队列名称
        """
        # 如果队列名称已经符合规范（以 crawlo: 开头且不是 crawlo:crawlo:），则保持不变
        if queue_name.startswith("crawlo:") and not queue_name.startswith("crawlo:crawlo:"):
            return queue_name
            
        # 处理三重 crawlo 前缀，简化为标准格式
        if queue_name.startswith("crawlo:crawlo:crawlo:"):
            # 三重 crawlo 前缀，简化为标准 crawlo: 格式
            remaining = queue_name[21:]  # 去掉 "crawlo:crawlo:crawlo:" 前缀
            if remaining:
                return f"crawlo:{remaining}"
            else:
                return "crawlo:requests"  # 默认名称
                
        # 处理双重 crawlo 前缀
        elif queue_name.startswith("crawlo:crawlo:"):
            # 双重 crawlo 前缀，简化为标准 crawlo: 格式
            remaining = queue_name[14:]  # 去掉 "crawlo:crawlo:" 前缀
            if remaining:
                return f"crawlo:{remaining}"
            else:
                return "crawlo:requests"  # 默认名称
                
        # 处理无 crawlo 前缀的情况
        elif not queue_name.startswith("crawlo:"):
            # 无 crawlo 前缀，添加 crawlo: 前缀
            if queue_name:
                return f"crawlo:{queue_name}"
            else:
                return "crawlo:requests"  # 默认名称
                
        # 其他情况，保持不变
        else:
            return queue_name

    async def connect(self, max_retries=3, delay=1):
        """异步连接 Redis，支持重试"""
        async with self._lock:
            if self._redis is not None:
                # 如果已经连接，测试连接是否仍然有效
                try:
                    await self._redis.ping()
                    return self._redis
                except Exception:
                    # 连接失效，重新连接
                    self._redis = None

            for attempt in range(max_retries):
                try:
                    # 使用优化的连接池，确保 decode_responses=False 以避免编码问题
                    self._redis_pool = get_redis_pool(
                        self.redis_url,
                        is_cluster=self.is_cluster,
                        cluster_nodes=self.cluster_nodes,
                        max_connections=self.max_connections,
                        socket_connect_timeout=5,
                        socket_timeout=30,
                        health_check_interval=30,
                        retry_on_timeout=True,
                        decode_responses=False,  # 确保不自动解码响应
                        encoding='utf-8'
                    )

                    self._redis = await self._redis_pool.get_connection()

                    # 测试连接
                    if self._redis:
                        await self._redis.ping()
                    return self._redis
                except Exception as e:
                    error_msg = f"Redis 连接失败 (尝试 {attempt + 1}/{max_retries}, Module: {self.module_name}): {e}"
                    get_module_logger().warning(error_msg)
                    get_module_logger().debug(f"详细错误信息:\n{traceback.format_exc()}")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(delay)
                    else:
                        raise ConnectionError(f"无法连接 Redis (Module: {self.module_name}): {e}")

    async def _ensure_connection(self):
        """确保连接有效"""
        if self._redis is None:
            await self.connect()
        try:
            if self._redis:
                await self._redis.ping()
        except Exception as e:
            get_module_logger().warning(f"Redis 连接失效 (Module: {self.module_name})，尝试重连...: {e}")
            self._redis = None
            await self.connect()

    def _is_cluster_mode(self) -> bool:
        """检查是否为集群模式"""
        if REDIS_CLUSTER_AVAILABLE and RedisCluster is not None:
            # 检查 _redis 是否为 RedisCluster 实例
            if self._redis is not None and isinstance(self._redis, RedisCluster):
                return True
        return False

    async def put(self, request, priority: int = 0) -> bool:
        """放入请求到队列"""
        try:
            await self._ensure_connection()
            if not self._redis:
                return False
                
            # 修复优先级行为一致性问题
            # 原来: score = -priority （导致priority大的先出队）
            # 现在: score = priority （确保priority小的先出队，与内存队列一致）
            score = priority
            key = self._get_request_key(request)

            # 🔥 使用专用的序列化工具清理 Request
            clean_request = self.request_serializer.prepare_for_serialization(request)

            # 确保序列化后的数据可以被正确反序列化
            try:
                serialized = pickle.dumps(clean_request)
                # 验证序列化数据可以被反序列化
                pickle.loads(serialized)
            except Exception as serialize_error:
                get_module_logger().error(f"请求序列化验证失败 (Module: {self.module_name}): {serialize_error}")
                return False

            # 处理集群模式下的操作
            if self._is_cluster_mode():
                # 在集群模式下，确保所有键都在同一个slot中
                # 可以通过在键名中添加相同的哈希标签来实现
                hash_tag = "{queue}"  # 使用哈希标签确保键在同一个slot
                queue_name_with_tag = f"{self.queue_name}{hash_tag}"
                data_key_with_tag = f"{self.queue_name}:data{hash_tag}"
                
                pipe = self._redis.pipeline()
                pipe.zadd(queue_name_with_tag, {key: score})
                pipe.hset(data_key_with_tag, key, serialized)
                result = await pipe.execute()
            else:
                pipe = self._redis.pipeline()
                pipe.zadd(self.queue_name, {key: score})
                pipe.hset(f"{self.queue_name}:data", key, serialized)
                result = await pipe.execute()

            if result[0] > 0:
                get_module_logger().debug(f"成功入队 (Module: {self.module_name}): {request.url}")
            return result[0] > 0
        except Exception as e:
            error_context = ErrorContext(
                context=f"放入队列失败 (Module: {self.module_name})"
            )
            get_module_error_handler().handle_error(
                e,
                context=error_context,
                raise_error=False
            )
            return False

    async def get(self, timeout: float = 5.0):
        """
        获取请求（带超时）
        :param timeout: 最大等待时间（秒），避免无限轮询
        """
        try:
            await self._ensure_connection()
            if not self._redis:
                return None
                
            start_time = asyncio.get_event_loop().time()

            while True:
                # 尝试获取任务
                if self._is_cluster_mode():
                    # 集群模式处理
                    hash_tag = "{queue}"
                    queue_name_with_tag = f"{self.queue_name}{hash_tag}"
                    result = await self._redis.zpopmin(queue_name_with_tag, count=1)
                else:
                    result = await self._redis.zpopmin(self.queue_name, count=1)
                    
                if result:
                    key, score = result[0]
                    data_key = f"{self.queue_name}:data"
                    if self._is_cluster_mode():
                        hash_tag = "{queue}"
                        data_key = f"{self.queue_name}:data{hash_tag}"
                        
                    serialized = await self._redis.hget(data_key, key)
                    if not serialized:
                        continue

                    # 移动到 processing
                    processing_key = f"{key}:{int(time.time())}"
                    processing_queue = self.processing_queue
                    processing_data_key = f"{self.processing_queue}:data"
                    
                    if self._is_cluster_mode():
                        hash_tag = "{queue}"
                        processing_queue = f"{self.processing_queue}{hash_tag}"
                        processing_data_key = f"{self.processing_queue}:data{hash_tag}"

                    if self._is_cluster_mode():
                        pipe = self._redis.pipeline()
                        pipe.zadd(processing_queue, {processing_key: time.time() + self.timeout})
                        pipe.hset(processing_data_key, processing_key, serialized)
                        pipe.hdel(data_key, key)
                        await pipe.execute()
                    else:
                        pipe = self._redis.pipeline()
                        pipe.zadd(processing_queue, {processing_key: time.time() + self.timeout})
                        pipe.hset(processing_data_key, processing_key, serialized)
                        pipe.hdel(data_key, key)
                        await pipe.execute()

                    # 更安全的反序列化方式
                    try:
                        # 首先尝试标准的 pickle 反序列化
                        request = pickle.loads(serialized)
                        return request
                    except UnicodeDecodeError:
                        # 如果出现编码错误，尝试使用 latin1 解码
                        request = pickle.loads(serialized, encoding='latin1')
                        return request
                    except Exception as pickle_error:
                        # 如果pickle反序列化失败，记录错误并跳过这个任务
                        get_module_logger().error(f"无法反序列化请求数据 (Module: {self.module_name}): {pickle_error}")
                        # 从processing队列中移除这个无效的任务
                        if self._is_cluster_mode():
                            await self._redis.zrem(processing_queue, processing_key)
                            await self._redis.hdel(processing_data_key, processing_key)
                        else:
                            await self._redis.zrem(processing_queue, processing_key)
                            await self._redis.hdel(processing_data_key, processing_key)
                        # 继续尝试下一个任务
                        continue

                # 检查是否超时
                if asyncio.get_event_loop().time() - start_time > timeout:
                    return None

                # 短暂等待，避免空轮询，但减少等待时间以提高响应速度
                await asyncio.sleep(0.001)  # 从0.01减少到0.001

        except Exception as e:
            error_context = ErrorContext(
                context=f"获取队列任务失败 (Module: {self.module_name})"
            )
            get_module_error_handler().handle_error(
                e,
                context=error_context,
                raise_error=False
            )
            return None

    async def ack(self, request: "Request"):
        """确认任务完成"""
        try:
            await self._ensure_connection()
            if not self._redis:
                return
                
            key = self._get_request_key(request)
            processing_queue = self.processing_queue
            processing_data_key = f"{self.processing_queue}:data"
            
            if self._is_cluster_mode():
                hash_tag = "{queue}"
                processing_queue = f"{self.processing_queue}{hash_tag}"
                processing_data_key = f"{self.processing_queue}:data{hash_tag}"

            cursor = 0
            while True:
                if self._is_cluster_mode():
                    cursor, keys = await self._redis.zscan(processing_queue, cursor, match=f"{key}:*")
                else:
                    cursor, keys = await self._redis.zscan(processing_queue, cursor, match=f"{key}:*")
                if keys:
                    if self._is_cluster_mode():
                        pipe = self._redis.pipeline()
                        for k in keys:
                            pipe.zrem(processing_queue, k)
                            pipe.hdel(processing_data_key, k)
                        await pipe.execute()
                    else:
                        pipe = self._redis.pipeline()
                        for k in keys:
                            pipe.zrem(processing_queue, k)
                            pipe.hdel(processing_data_key, k)
                        await pipe.execute()
                if cursor == 0:
                    break
        except Exception as e:
            error_context = ErrorContext(
                context=f"确认任务完成失败 (Module: {self.module_name})"
            )
            get_module_error_handler().handle_error(
                e,
                context=error_context,
                raise_error=False
            )

    async def fail(self, request: "Request", reason: str = ""):
        """标记任务失败"""
        try:
            await self._ensure_connection()
            if not self._redis:
                return
                
            key = self._get_request_key(request)
            await self.ack(request)

            retry_key = f"{self.failed_queue}:retries:{key}"
            failed_queue = self.failed_queue
            
            if self._is_cluster_mode():
                hash_tag = "{queue}"
                retry_key = f"{self.failed_queue}:retries:{key}{hash_tag}"
                failed_queue = f"{self.failed_queue}{hash_tag}"

            retries = await self._redis.incr(retry_key)
            await self._redis.expire(retry_key, 86400)

            if retries <= self.max_retries:
                await self.put(request, priority=request.priority + 1)
                get_module_logger().info(
                    f"任务重试 [{retries}/{self.max_retries}] (Module: {self.module_name}): {request.url}")
            else:
                failed_data = {
                    "url": request.url,
                    "reason": reason,
                    "retries": retries,
                    "failed_at": time.time(),
                    "request_pickle": pickle.dumps(request).hex(),  # 可选：保存完整请求
                }
                await self._redis.lpush(failed_queue, pickle.dumps(failed_data))
                get_module_logger().error(f"任务彻底失败 [{retries}次] (Module: {self.module_name}): {request.url}")
        except Exception as e:
            error_context = ErrorContext(
                context=f"标记任务失败失败 (Module: {self.module_name})"
            )
            get_module_error_handler().handle_error(
                e,
                context=error_context,
                raise_error=False
            )

    def _get_request_key(self, request) -> str:
        """生成请求唯一键"""
        return f"{self.module_name}:url:{hash(request.url) & 0x7FFFFFFF}"  # 确保正数

    async def qsize(self) -> int:
        """Get queue size"""
        try:
            await self._ensure_connection()
            if not self._redis:
                return 0
                
            if self._is_cluster_mode():
                hash_tag = "{queue}"
                queue_name_with_tag = f"{self.queue_name}{hash_tag}"
                return await self._redis.zcard(queue_name_with_tag)
            else:
                return await self._redis.zcard(self.queue_name)
        except Exception as e:
            error_context = ErrorContext(
                context=f"Failed to get queue size (Module: {self.module_name})"
            )
            get_module_error_handler().handle_error(
                e,
                context=error_context,
                raise_error=False
            )
            return 0

    async def close(self):
        """关闭连接"""
        try:
            # 显式关闭Redis连接
            if self._redis is not None:
                try:
                    # 尝试关闭连接
                    if hasattr(self._redis, 'close'):
                        close_result = self._redis.close()
                        if asyncio.iscoroutine(close_result):
                            await close_result
                    
                    # 等待连接关闭完成
                    if hasattr(self._redis, 'wait_closed'):
                        wait_result = self._redis.wait_closed()
                        if asyncio.iscoroutine(wait_result):
                            await wait_result
                except Exception as close_error:
                    get_module_logger().warning(
                        f"Error closing Redis connection (Module: {self.module_name}): {close_error}"
                    )
                finally:
                    self._redis = None
            
            # 释放连接池引用（连接池由全局管理器管理）
            self._redis_pool = None
            
            get_module_logger().debug(f"Redis 连接已释放 (Module: {self.module_name})")
        except Exception as e:
            error_context = ErrorContext(
                context=f"释放 Redis 连接失败 (Module: {self.module_name})"
            )
            get_module_error_handler().handle_error(
                e,
                context=error_context,
                raise_error=False
            )
```

**code file end: crawlo/queue/redis_priority_queue.py**

---


### code file start: crawlo/queue/__init__.py 

```python
"""队列管理模块"""
from crawlo.queue.queue_manager import QueueManager, QueueConfig, QueueType
from crawlo.queue.pqueue import SpiderPriorityQueue

__all__ = [
    'QueueManager',
    'QueueConfig',
    'QueueType',
    'SpiderPriorityQueue',
]
```

**code file end: crawlo/queue/__init__.py**

---


### code file start: crawlo/settings/default_settings.py 

```python
# -*- coding:UTF-8 -*-
"""
默认配置文件
包含 Crawlo 框架的所有默认设置项
"""
# 添加环境变量配置工具导入
from crawlo.utils.config_manager import EnvConfigManager

# --------------------------------- 1. 框架基础配置 ------------------------------------

# 框架初始化控制
FRAMEWORK_INIT_ORDER = [
    'log_system',  # 日志系统
    'settings_system',  # 配置系统
    'core_components',  # 核心组件
    'extensions',  # 扩展组件
    'full_initialization'  # 完全初始化
]
FRAMEWORK_INIT_STATE = 'uninitialized'

# 项目基础配置
runtime_config = EnvConfigManager.get_runtime_config()
PROJECT_NAME = runtime_config['PROJECT_NAME']  # 项目名称（用于日志、Redis Key 等标识）
VERSION = EnvConfigManager.get_version()  # 项目版本号 - 从框架的__version__.py文件中读取，如果不存在则使用默认值
RUN_MODE = runtime_config['CRAWLO_MODE']  # 运行模式：standalone/distributed/auto
CONCURRENCY = runtime_config['CONCURRENCY']  # 并发数配置

# 爬虫模块配置
SPIDER_MODULES = []  # 爬虫模块列表
SPIDER_LOADER_WARN_ONLY = False  # 爬虫加载器是否只警告不报错

# --------------------------------- 2. 爬虫核心配置 ------------------------------------

# 下载器配置
DOWNLOADER = "crawlo.downloader.httpx_downloader.HttpXDownloader"  # 默认下载器
DOWNLOAD_DELAY = 0.5  # 请求延迟（秒）
RANDOMNESS = True  # 是否启用随机延迟
RANDOM_RANGE = [0.5, 1.5]  # 随机延迟范围因子，实际延迟 = DOWNLOAD_DELAY * RANDOM_RANGE[0] 到 DOWNLOAD_DELAY * RANDOM_RANGE[1]

# 调度器配置
DEPTH_PRIORITY = 1  # 深度优先级（负数表示深度优先，正数表示广度优先）
SCHEDULER_MAX_QUEUE_SIZE = 5000  # 调度器队列最大大小
BACKPRESSURE_RATIO = 0.9  # 背压触发阈值（队列大小达到最大容量的90%时触发背压控制）

# 请求生成控制
REQUEST_GENERATION_BATCH_SIZE = 10  # 请求生成批处理大小
REQUEST_GENERATION_INTERVAL = 0.01  # 请求生成间隔（秒）
ENABLE_CONTROLLED_REQUEST_GENERATION = False  # 是否启用受控请求生成

# 队列配置
QUEUE_TYPE = 'auto'  # 队列类型：memory/redis/auto
# SCHEDULER_QUEUE_NAME = f"crawlo:{PROJECT_NAME}:queue:requests"  # 调度器队列名称（遵循统一命名规范）
QUEUE_MAX_RETRIES = 3  # 队列操作最大重试次数
QUEUE_TIMEOUT = 300  # 队列操作超时时间（秒）

# --------------------------------- 3. 数据库和过滤器配置 ------------------------------------

# MySQL配置
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'crawl_pro'
MYSQL_TABLE = 'crawlo'
MYSQL_BATCH_SIZE = 100
MYSQL_USE_BATCH = False  # 是否启用批量插入
# MySQL SQL生成行为控制配置
MYSQL_AUTO_UPDATE = False  # 是否使用 REPLACE INTO（完全覆盖已存在记录）
MYSQL_INSERT_IGNORE = False  # 是否使用 INSERT IGNORE（忽略重复数据）
MYSQL_UPDATE_COLUMNS = ()  # 冲突时需更新的列名；指定后 MYSQL_AUTO_UPDATE 失效

# Redis配置
redis_config = EnvConfigManager.get_redis_config()
REDIS_HOST = redis_config['REDIS_HOST']
REDIS_PORT = redis_config['REDIS_PORT']
REDIS_PASSWORD = redis_config['REDIS_PASSWORD']
REDIS_DB = redis_config['REDIS_DB']

# Redis集群支持说明：
# Crawlo框架支持Redis单实例和集群模式的智能切换
# 集群模式配置方式：
# 1. 使用逗号分隔的节点列表：'192.168.1.100:7000,192.168.1.101:7000,192.168.1.102:7000'
# 2. 使用集群URL格式：'redis-cluster://192.168.1.100:7000,192.168.1.101:7000,192.168.1.102:7000'
# 框架会自动检测URL格式并选择合适的模式

# 根据是否有密码生成不同的 URL 格式
if REDIS_PASSWORD:
    REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
else:
    REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

# Redis key命名规范已封装到框架内部组件中，用户无需手动配置：
# - 请求去重: crawlo:{PROJECT_NAME}:filter:fingerprint
# - 数据项去重: crawlo:{PROJECT_NAME}:item:fingerprint
# - 请求队列: crawlo:{PROJECT_NAME}:queue:requests
# - 处理中队列: crawlo:{PROJECT_NAME}:queue:processing
# - 失败队列: crawlo:{PROJECT_NAME}:queue:failed

REDIS_TTL = 0  # 指纹过期时间（0 表示永不过期）
CLEANUP_FP = 0  # 程序结束时是否清理指纹（0=不清理）
FILTER_DEBUG = True  # 是否开启去重调试日志
DECODE_RESPONSES = True  # Redis 返回是否解码为字符串

# 过滤器配置
DEFAULT_DEDUP_PIPELINE = 'crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline'  # 默认使用内存过滤器和去重管道
FILTER_CLASS = 'crawlo.filters.memory_filter.MemoryFilter'

# Bloom过滤器配置
BLOOM_FILTER_CAPACITY = 1000000  # Bloom过滤器容量
BLOOM_FILTER_ERROR_RATE = 0.001  # Bloom过滤器错误率

# --------------------------------- 4. 中间件配置 ------------------------------------

# 框架中间件列表（框架默认中间件 + 用户自定义中间件）
MIDDLEWARES = [
    # === 请求预处理阶段 ===
    'crawlo.middleware.request_ignore.RequestIgnoreMiddleware',  # 1. 忽略无效请求
    'crawlo.middleware.download_delay.DownloadDelayMiddleware',  # 2. 控制请求频率
    'crawlo.middleware.default_header.DefaultHeaderMiddleware',  # 3. 添加默认请求头
    'crawlo.middleware.offsite.OffsiteMiddleware',  # 5. 站外请求过滤

    # === 响应处理阶段 ===
    'crawlo.middleware.retry.RetryMiddleware',  # 6. 失败请求重试
    'crawlo.middleware.response_code.ResponseCodeMiddleware',  # 7. 处理特殊状态码
    'crawlo.middleware.response_filter.ResponseFilterMiddleware',  # 8. 响应内容过滤
]

# --------------------------------- 5. 管道配置 ------------------------------------

# 框架数据处理管道列表（框架默认管道 + 用户自定义管道）
PIPELINES = [
    'crawlo.pipelines.console_pipeline.ConsolePipeline',
]

# --------------------------------- 6. 扩展配置 ------------------------------------

# 框架扩展组件列表（框架默认扩展 + 用户自定义扩展）
EXTENSIONS = [
    'crawlo.extension.log_interval.LogIntervalExtension',  # 定时日志
    'crawlo.extension.log_stats.LogStats',  # 统计信息
    'crawlo.extension.logging_extension.CustomLoggerExtension',  # 自定义日志
]

# --------------------------------- 7. 日志与监控配置 ------------------------------------

# 日志配置
LOG_LEVEL = None  # 日志级别: DEBUG/INFO/WARNING/ERROR，默认为None，由用户在项目settings中设置
STATS_DUMP = True  # 是否周期性输出统计信息
LOG_FILE = None  # 日志文件路径，将在项目配置中设置
LOG_FORMAT = '%(asctime)s - [%(name)s] - %(levelname)s: %(message)s'
LOG_ENCODING = 'utf-8'
LOG_MAX_BYTES = 10 * 1024 * 1024  # 日志轮转大小（字节）
LOG_BACKUP_COUNT = 5  # 日志备份数量

# 日志间隔配置
INTERVAL = 60  # 日志输出间隔（秒）

# 内存监控配置
MEMORY_MONITOR_ENABLED = False  # 是否启用内存监控
MEMORY_MONITOR_INTERVAL = 60  # 内存监控检查间隔（秒）
MEMORY_WARNING_THRESHOLD = 80.0  # 内存使用率警告阈值（百分比）
MEMORY_CRITICAL_THRESHOLD = 90.0  # 内存使用率严重阈值（百分比）

# 性能分析配置
PERFORMANCE_PROFILER_ENABLED = False  # 是否启用性能分析
PERFORMANCE_PROFILER_OUTPUT_DIR = 'profiling'  # 性能分析输出目录
PERFORMANCE_PROFILER_INTERVAL = 300  # 性能分析间隔（秒）

# 健康检查配置
HEALTH_CHECK_ENABLED = True  # 是否启用健康检查

# --------------------------------- 8. 网络请求配置 ------------------------------------

# 默认请求头配置
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
}  # 默认请求头

# 默认User-Agent（使用现代浏览器的User-Agent）
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"

# 是否启用随机User-Agent功能（默认禁用，用户可根据需要启用）
RANDOM_USER_AGENT_ENABLED = False  # 是否启用随机用户代理

# 站外过滤配置
ALLOWED_DOMAINS = []  # 允许的域名列表

# 代理配置（通用版，支持静态代理列表和动态代理API两种模式）
PROXY_LIST = []  # 静态代理列表配置
PROXY_API_URL = ""  # 动态代理API配置
# 代理提取配置，用于指定如何从API返回的数据中提取代理地址
# 可选值：
# - 字符串：直接作为字段名使用，如 "proxy"（默认值）
# - 字典：包含type和value字段，支持多种提取方式
#   - {"type": "field", "value": "data"}：从指定字段提取
#   - {"type": "jsonpath", "value": "$.data[0].proxy"}：使用JSONPath表达式提取
#   - {"type": "custom", "function": your_function}：使用自定义函数提取
PROXY_EXTRACTOR = "proxy"  # 代理提取配置
# 代理失败处理配置
PROXY_MAX_FAILED_ATTEMPTS = 3  # 代理最大失败尝试次数，超过此次数将标记为失效

# 代理使用示例：
# 1. 静态代理列表：
#    PROXY_LIST = ["http://proxy1:8080", "http://proxy2:8080"]
#    PROXY_API_URL = ""  # 不使用动态代理
#
# 2. 动态代理API（默认字段提取）：
#    PROXY_LIST = []  # 不使用静态代理
#    PROXY_API_URL = "http://api.example.com/get_proxy"
#    PROXY_EXTRACTOR = "proxy"  # 从"proxy"字段提取
#
# 3. 动态代理API（自定义字段提取）：
#    PROXY_LIST = []  # 不使用静态代理
#    PROXY_API_URL = "http://api.example.com/get_proxy"
#    PROXY_EXTRACTOR = "data"  # 从"data"字段提取
#
# 4. 动态代理API（嵌套字段提取）：
#    PROXY_LIST = []  # 不使用静态代理
#    PROXY_API_URL = "http://api.example.com/get_proxy"
#    PROXY_EXTRACTOR = {"type": "field", "value": "result"}  # 从"result"字段提取

# 下载器通用配置
DOWNLOAD_TIMEOUT = 30  # 下载超时时间（秒）
VERIFY_SSL = True  # 是否验证SSL证书
CONNECTION_POOL_LIMIT = 100  # 连接池大小限制
CONNECTION_POOL_LIMIT_PER_HOST = 20  # 每个主机的连接池大小限制
DOWNLOAD_MAXSIZE = 10 * 1024 * 1024  # 最大下载大小（字节）
DOWNLOAD_STATS = True  # 是否启用下载统计
DOWNLOAD_WARN_SIZE = 1024 * 1024  # 下载警告大小（字节）
DOWNLOAD_RETRY_TIMES = 3  # 下载重试次数
MAX_RETRY_TIMES = 3  # 最大重试次数

# 下载器健康检查
DOWNLOADER_HEALTH_CHECK = True  # 是否启用下载器健康检查
HEALTH_CHECK_INTERVAL = 60  # 健康检查间隔（秒）
REQUEST_STATS_ENABLED = True  # 是否启用请求统计
STATS_RESET_ON_START = False  # 启动时是否重置统计

# HttpX 下载器专用配置
HTTPX_HTTP2 = True  # 是否启用HTTP/2支持
HTTPX_FOLLOW_REDIRECTS = True  # 是否自动跟随重定向

# AioHttp 下载器专用配置
AIOHTTP_AUTO_DECOMPRESS = True  # 是否自动解压响应
AIOHTTP_FORCE_CLOSE = False  # 是否强制关闭连接

# Curl-Cffi 特有配置
CURL_BROWSER_TYPE = "chrome"  # 浏览器指纹模拟（仅 CurlCffi 下载器有效）
CURL_BROWSER_VERSION_MAP = {  # 自定义浏览器版本映射（可覆盖默认行为）
    "chrome": "chrome136",
    "edge": "edge101",
    "safari": "safari184",
    "firefox": "firefox135",
}

# Selenium 下载器配置
SELENIUM_BROWSER_TYPE = "chrome"  # 浏览器类型: chrome, firefox, edge
SELENIUM_HEADLESS = True  # 是否无头模式
SELENIUM_TIMEOUT = 30  # 超时时间（秒）
SELENIUM_LOAD_TIMEOUT = 10  # 页面加载超时时间（秒）
SELENIUM_WINDOW_WIDTH = 1920  # 窗口宽度
SELENIUM_WINDOW_HEIGHT = 1080  # 窗口高度
SELENIUM_WAIT_FOR_ELEMENT = None  # 等待特定元素选择器
SELENIUM_ENABLE_JS = True  # 是否启用JavaScript
SELENIUM_PROXY = None  # 代理设置
SELENIUM_SINGLE_BROWSER_MODE = True  # 单浏览器多标签页模式
SELENIUM_MAX_TABS_PER_BROWSER = 10  # 单浏览器最大标签页数量

# Playwright 下载器配置
PLAYWRIGHT_BROWSER_TYPE = "chromium"  # 浏览器类型: chromium, firefox, webkit
PLAYWRIGHT_HEADLESS = True  # 是否无头模式
PLAYWRIGHT_TIMEOUT = 30000  # 超时时间（毫秒）
PLAYWRIGHT_LOAD_TIMEOUT = 10000  # 页面加载超时时间（毫秒）
PLAYWRIGHT_VIEWPORT_WIDTH = 1920  # 视口宽度
PLAYWRIGHT_VIEWPORT_HEIGHT = 1080  # 视口高度
PLAYWRIGHT_WAIT_FOR_ELEMENT = None  # 等待特定元素选择器
PLAYWRIGHT_PROXY = None  # 代理设置
PLAYWRIGHT_SINGLE_BROWSER_MODE = True  # 单浏览器多标签页模式
PLAYWRIGHT_MAX_PAGES_PER_BROWSER = 10  # 单浏览器最大页面数量

# 通用优化配置
CONNECTION_TTL_DNS_CACHE = 300  # DNS缓存TTL（秒）
CONNECTION_KEEPALIVE = True  # 是否启用HTTP连接保持
```

**code file end: crawlo/settings/default_settings.py**

---


### code file start: crawlo/settings/setting_manager.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from copy import deepcopy
from importlib import import_module
from collections.abc import MutableMapping

from crawlo.settings import default_settings


class SettingManager(MutableMapping):

    def __init__(self, values=None):
        self.attributes = {}
        self.set_settings(default_settings)
        # 在初始化时合并配置
        self._merge_config(values)
        # 处理动态配置
        self._process_dynamic_config()

    def _merge_config(self, user_config):
        """合并默认配置和用户配置"""
        if not user_config:
            return

        # 合并中间件配置
        if 'MIDDLEWARES' in user_config:
            default_middlewares = self.attributes.get('MIDDLEWARES', [])
            user_middlewares = user_config['MIDDLEWARES']
            # 如果用户配置了空列表，则仍然使用默认配置
            if user_middlewares:
                # 过滤掉空值和注释
                user_middlewares = [middleware for middleware in user_middlewares if middleware and not middleware.strip().startswith('#')]
                # 合并默认中间件和用户中间件，去重但保持顺序
                merged_middlewares = default_middlewares[:]
                for middleware in user_middlewares:
                    if middleware not in merged_middlewares:
                        merged_middlewares.append(middleware)
                self.attributes['MIDDLEWARES'] = merged_middlewares

        # 合并管道配置
        if 'PIPELINES' in user_config:
            default_pipelines = self.attributes.get('PIPELINES', [])
            user_pipelines = user_config['PIPELINES']
            # 如果用户配置了空列表，则仍然使用默认配置
            if user_pipelines:
                # 过滤掉空值和注释
                user_pipelines = [pipeline for pipeline in user_pipelines if pipeline and not pipeline.strip().startswith('#')]
                # 合并默认管道和用户管道，去重但保持顺序
                merged_pipelines = default_pipelines[:]
                for pipeline in user_pipelines:
                    if pipeline not in merged_pipelines:
                        merged_pipelines.append(pipeline)
                self.attributes['PIPELINES'] = merged_pipelines



        # 合并扩展配置
        if 'EXTENSIONS' in user_config:
            default_extensions = self.attributes.get('EXTENSIONS', [])
            user_extensions = user_config['EXTENSIONS']
            # 如果用户配置了空列表，则仍然使用默认配置
            if user_extensions:
                # 过滤掉空值和注释
                user_extensions = [extension for extension in user_extensions if extension and not extension.strip().startswith('#')]
                # 合并默认扩展和用户扩展，去重但保持顺序
                merged_extensions = default_extensions[:]
                for extension in user_extensions:
                    if extension not in merged_extensions:
                        merged_extensions.append(extension)
                self.attributes['EXTENSIONS'] = merged_extensions

        # 更新其他用户配置
        for key, value in user_config.items():
            if key not in ['MIDDLEWARES', 'PIPELINES', 'EXTENSIONS']:
                self.attributes[key] = value
        
        # 特殊处理PIPELINES，确保去重管道在最前面（在所有配置更新后执行）
        dedup_pipeline = self.attributes.get('DEFAULT_DEDUP_PIPELINE')
        if dedup_pipeline:
            pipelines = self.attributes.get('PIPELINES', [])
            # 移除所有去重管道实例（如果存在）
            # 移除内存和Redis去重管道
            pipelines = [item for item in pipelines 
                       if item not in ('crawlo.pipelines.memory_dedup_pipeline.MemoryDedupPipeline', 
                                     'crawlo.pipelines.redis_dedup_pipeline.RedisDedupPipeline')]
            # 在开头插入去重管道
            pipelines.insert(0, dedup_pipeline)
            self.attributes['PIPELINES'] = pipelines

    def set_settings(self, module):
        if isinstance(module, str):
            module = import_module(module)
        
        # 收集模块中的所有配置项
        module_settings = {}
        for key in dir(module):
            if key.isupper():
                value = getattr(module, key)
                module_settings[key] = value
        
        # 使用合并逻辑而不是直接设置
        self._merge_config(module_settings)
        
        # 处理动态配置项（如LOG_FILE）
        self._process_dynamic_config()
        
    def _process_dynamic_config(self):
        """
        处理动态配置项
        某些配置项需要根据其他配置项的值进行动态计算
        """
        # 处理LOG_FILE配置
        if self.attributes.get('LOG_FILE') is None:
            project_name = self.attributes.get('PROJECT_NAME', 'crawlo')
            self.attributes['LOG_FILE'] = f'logs/{project_name}.log'

    def get(self, key, default=None):
        """安全获取值，不触发递归"""
        value = self.attributes.get(key, default)
        return value if value is not None else default

    def _get_merged_list(self, key, default=None):
        """这个方法已不再需要，因为配置合并已在配置加载时完成"""
        return self.attributes.get(key, default or [])

    def get_int(self, key, default=0):
        return int(self.get(key, default=default))

    def get_float(self, key, default=0.0):
        return float(self.get(key, default=default))

    def get_bool(self, key, default=False):
        got = self.get(key, default=default)
        if isinstance(got, bool):
            return got
        if isinstance(got, (int, float)):
            return bool(got)
        got_lower = str(got).strip().lower()
        if got_lower in ('1', 'true'):
            return True
        if got_lower in ('0', 'false'):
            return False
        raise ValueError(
            f"Unsupported value for boolean setting: {got}. "
            "Supported values are: 0/1, True/False, '0'/'1', 'True'/'False' (case-insensitive)."
        )

    def get_list(self, key, default=None):
        values = self.get(key, default or [])
        if isinstance(values, str):
            return [v.strip() for v in values.split(',') if v.strip()]
        try:
            return list(values)
        except TypeError:
            return [values]

    def get_dict(self, key, default=None):
        value = self.get(key, default or {})
        if isinstance(value, str):
            value = json.loads(value)
        try:
            return dict(value)
        except TypeError:
            return value

    def set(self, key, value):
        self.attributes[key] = value

    # 实现 MutableMapping 必须的方法
    def __getitem__(self, item):
        return self.attributes[item]

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        del self.attributes[key]

    def __iter__(self):
        return iter(self.attributes)

    def __len__(self):
        return len(self.attributes)

    def __str__(self):
        return f'<Settings: {self.attributes}>'

    __repr__ = __str__

    def update_attributes(self, attributes):
        if attributes is not None:
            for key, value in attributes.items():
                self.set(key, value)

    def copy(self):
        return deepcopy(self)

    def __deepcopy__(self, memo):
        """
        自定义深度复制方法，避免复制logger等不可pickle的对象
        """
        # 创建一个新的实例
        cls = self.__class__
        new_instance = cls.__new__(cls)

        # 复制attributes字典，但排除不可pickle的对象
        new_attributes = {}
        for key, value in self.attributes.items():
            try:
                # 尝试深度复制值
                new_attributes[key] = deepcopy(value, memo)
            except Exception:
                # 如果复制失败，保留原始引用（对于logger等对象）
                new_attributes[key] = value

        # 设置新实例的attributes
        new_instance.attributes = new_attributes

        return new_instance
```

**code file end: crawlo/settings/setting_manager.py**

---


### code file start: crawlo/settings/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
# @Time    :    2025-05-11 11:08
# @Author  :   oscar
# @Desc    :   None
"""

```

**code file end: crawlo/settings/__init__.py**

---


### code file start: crawlo/spider/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Crawlo Spider Module
==================
提供爬虫基类和相关功能。

核心功能:
- Spider基类：所有爬虫的基础类
- 自动注册机制：通过元类自动注册爬虫
- 配置管理：支持自定义设置和链式调用
- 生命周期管理：开启/关闭钩子函数
- 分布式支持：智能检测运行模式

使用示例:
    class MySpider(Spider):
        name = 'my_spider'
        start_urls = ['http://example.com']
        
        # 自定义配置
        custom_settings = {
            'DOWNLOADER_TYPE': 'httpx',
            'CONCURRENCY': 10
        }
        
        def parse(self, response):
            # 解析逻辑
            yield Item(data=response.json())
"""
from __future__ import annotations
from typing import Type, Any, Optional, List, Dict, Union, Iterator, AsyncIterator
from ..network.request import Request
from ..utils.log import get_logger


# 全局爬虫注册表
_DEFAULT_SPIDER_REGISTRY: dict[str, Type[Spider]] = {}


class SpiderMeta(type):
    """
    爬虫元类，提供自动注册功能
    
    功能:
    - 自动注册爬虫到全局注册表
    - 验证爬虫名称的唯一性
    - 提供完整的错误提示
    """
    
    def __new__(mcs, name: str, bases: tuple[type], namespace: dict[str, Any], **kwargs):
        cls = super().__new__(mcs, name, bases, namespace)

        # 检查是否为Spider子类
        is_spider_subclass = any(
            base is Spider or (isinstance(base, type) and issubclass(base, Spider))
            for base in bases
        )
        if not is_spider_subclass:
            return cls

        # 验证爬虫名称
        spider_name = namespace.get('name')
        if not isinstance(spider_name, str):
            raise AttributeError(
                f"爬虫类 '{cls.__name__}' 必须定义字符串类型的 'name' 属性。\n"
                f"示例: name = 'my_spider'"
            )

        # 检查名称唯一性
        if spider_name in _DEFAULT_SPIDER_REGISTRY:
            existing_class = _DEFAULT_SPIDER_REGISTRY[spider_name]
            raise ValueError(
                f"爬虫名称 '{spider_name}' 已被 {existing_class.__name__} 占用。\n"
                f"请确保每个爬虫的 name 属性全局唯一。\n"
                f"建议使用格式: 'project_module_function'"
            )

        # 注册爬虫
        _DEFAULT_SPIDER_REGISTRY[spider_name] = cls
        # 延迟初始化logger避免模块级别阻塞
        try:
            from crawlo.logging import get_logger
            get_logger(__name__).debug(f"自动注册爬虫: {spider_name} -> {cls.__name__}")
        except:
            # 如果日志系统未初始化，静默失败
            pass

        return cls


class Spider(metaclass=SpiderMeta):
    """
    爬虫基类 - 所有爬虫实现的基础
    
    必须定义的属性:
    - name: 爬虫名称，必须全局唯一
    
    可选配置:
    - start_urls: 起始 URL 列表
    - custom_settings: 自定义设置字典
    - allowed_domains: 允许的域名列表
    
    必须实现的方法:
    - parse(response): 解析响应的主方法
    
    可选实现的方法:
    - spider_opened(): 爬虫开启时调用
    - spider_closed(): 爬虫关闭时调用
    - start_requests(): 生成初始请求（默认使用start_urls）
    
    示例:
        class MySpider(Spider):
            name = 'example_spider'
            start_urls = ['https://example.com']
            
            custom_settings = {
                'DOWNLOADER_TYPE': 'httpx',
                'CONCURRENCY': 5,
                'DOWNLOAD_DELAY': 1.0
            }
            
            def parse(self, response):
                # 提取数据
                data = response.css('title::text').get()
                yield {'title': data}
                
                # 生成新请求
                for link in response.css('a::attr(href)').getall():
                    yield Request(url=link, callback=self.parse_detail)
    """
    
    # 必须定义的属性
    name: str = None
    
    # 可选属性
    start_urls: List[str] = None
    custom_settings: Dict[str, Any] = None
    allowed_domains: List[str] = None

    def __init__(self, name: str = None, **kwargs):
        """
        初始化爬虫实例
        
        :param name: 爬虫名称（可选，默认使用类属性）
        :param kwargs: 其他初始化参数
        """
        # 初始化基本属性
        if not hasattr(self, 'start_urls') or self.start_urls is None:
            self.start_urls = []
        if not hasattr(self, 'custom_settings') or self.custom_settings is None:
            self.custom_settings = {}
        if not hasattr(self, 'allowed_domains') or self.allowed_domains is None:
            self.allowed_domains = []
            
        # 设置爬虫名称
        self.name = name or self.name
        if not self.name:
            raise ValueError(f"爬虫 {self.__class__.__name__} 必须指定 name 属性")
        
        # 初始化其他属性
        self.crawler = None
        # 延迟初始化logger避免阻塞
        self._logger = None
        self.stats = None
        
        # 应用额外参数
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @property
    def logger(self):
        """延迟初始化logger"""
        if self._logger is None:
            from crawlo.logging import get_logger
            self._logger = get_logger(self.name)
        return self._logger

    @classmethod
    def create_instance(cls, crawler) -> 'Spider':
        """
        创建爬虫实例并绑定 crawler
        
        :param crawler: Crawler 实例
        :return: 爬虫实例
        """
        spider = cls()
        spider.crawler = crawler
        spider.stats = getattr(crawler, 'stats', None)
        
        # 合并自定义设置 - 使用延迟应用避免初始化时的循环依赖
        if hasattr(spider, 'custom_settings') and spider.custom_settings:
            # 延迟到真正需要时才应用设置
            spider._pending_settings = spider.custom_settings.copy()
            spider.logger.debug(f"准备应用 {len(spider.custom_settings)} 项自定义设置")
        
        return spider
    
    def apply_pending_settings(self):
        """应用待处理的设置（在初始化完成后调用）"""
        if hasattr(self, '_pending_settings') and self._pending_settings:
            for key, value in self._pending_settings.items():
                if self.crawler and hasattr(self.crawler, 'settings'):
                    self.crawler.settings.set(key, value)
                    self.logger.debug(f"应用自定义设置: {key} = {value}")
            # 清除待处理的设置
            delattr(self, '_pending_settings')

    def start_requests(self) -> Iterator[Request]:
        """
        生成初始请求
        
        默认行为:
        - 使用 start_urls 生成请求
        - 智能检测分布式模式决定是否去重
        - 支持单个 start_url 属性（兼容性）
        - 支持批量生成优化（大规模URL场景）
        
        :return: Request 迭代器
        """
        # 检测是否为分布式模式
        is_distributed = self._is_distributed_mode()
        
        # 获取批量处理配置
        batch_size = self._get_batch_size()
        
        # 从 start_urls 生成请求
        if self.start_urls:
            generated_count = 0
            for url in self.start_urls:
                if self._is_allowed_domain(url):
                    yield Request(
                        url=url, 
                        callback=self.parse,
                        dont_filter=not is_distributed,
                        meta={'spider_name': self.name}
                    )
                    generated_count += 1
                    
                    # 大规模URL时进行批量控制
                    if batch_size > 0 and generated_count % batch_size == 0:
                        self.logger.debug(f"已生成 {generated_count} 个请求（批量大小: {batch_size}）")
                else:
                    self.logger.warning(f"跳过不允许的域名: {url}")
        
        # 兼容单个 start_url 属性
        elif hasattr(self, 'start_url') and isinstance(getattr(self, 'start_url'), str):
            url = getattr(self, 'start_url')
            if self._is_allowed_domain(url):
                yield Request(
                    url=url, 
                    callback=self.parse,
                    dont_filter=not is_distributed,
                    meta={'spider_name': self.name}
                )
            else:
                self.logger.warning(f"跳过不允许的域名: {url}")
        
        else:
            self.logger.warning(
                f"爬虫 {self.name} 没有定义 start_urls 或 start_url。\n"
                f"请在爬虫类中定义或重写 start_requests() 方法。"
            )
    
    def _get_batch_size(self) -> int:
        """
        获取批量处理大小配置
        
        用于大规模URL场景的性能优化
        
        :return: 批量大小（0表示无限制）
        """
        if not self.crawler:
            return 0
            
        # 从设置中获取批量大小
        batch_size = self.crawler.settings.get_int('SPIDER_BATCH_SIZE', 0)
        
        # 如果start_urls超过一定数量，自动启用批量模式
        if batch_size == 0 and self.start_urls and len(self.start_urls) > 1000:
            batch_size = 500  # 默认批量大小
            self.logger.info(f"检测到大量start_urls ({len(self.start_urls)})，启用批量模式 (批量大小: {batch_size})")
            
        return batch_size
    
    def _is_distributed_mode(self) -> bool:
        """
        智能检测是否为分布式模式
        
        检测条件:
        - QUEUE_TYPE = 'redis'
        - FILTER_CLASS 包含 'aioredis_filter' 
        - RUN_MODE = 'distributed'
        
        :return: 是否为分布式模式
        """
        if not self.crawler:
            return False
            
        settings = self.crawler.settings
        
        # 检查多个条件来判断是否为分布式模式
        queue_type = settings.get('QUEUE_TYPE', 'memory')
        filter_class = settings.get('FILTER_CLASS', '')
        run_mode = settings.get('RUN_MODE', 'standalone')
        
        # 分布式模式的标志
        is_redis_queue = queue_type == 'redis'
        is_redis_filter = 'aioredis_filter' in filter_class.lower()
        is_distributed_run_mode = run_mode == 'distributed'
        
        distributed = is_redis_queue or is_redis_filter or is_distributed_run_mode
        
        if distributed:
            self.logger.debug("检测到分布式模式，启用请求去重")
        else:
            self.logger.debug("检测到单机模式，禁用请求去重")
            
        return distributed
    
    def _is_allowed_domain(self, url: str) -> bool:
        """
        检查URL是否在允许的域名列表中
        
        :param url: 要检查的URL
        :return: 是否允许
        """
        if not self.allowed_domains:
            return True
            
        from urllib.parse import urlparse
        try:
            domain = urlparse(url).netloc.lower()
            return any(
                domain == allowed.lower() or domain.endswith('.' + allowed.lower())
                for allowed in self.allowed_domains
            )
        except Exception as e:
            self.logger.warning(f"URL解析失败: {url} - {e}")
            return False

    def parse(self, response):
        """
        解析响应的主方法（必须实现）
        
        :param response: 响应对象
        :return: 生成的 Item 或 Request
        """
        raise NotImplementedError(
            f"爬虫 {self.__class__.__name__} 必须实现 parse() 方法\n"
            f"示例:\n"
            f"def parse(self, response):\n"
            f"    # 提取数据\n"
            f"    yield {{'title': response.css('title::text').get()}}\n"
            f"    # 生成新请求\n"
            f"    for link in response.css('a::attr(href)').getall():\n"
            f"        yield Request(url=link)"
        )
    
    async def spider_opened(self):
        """
        爬虫开启时调用的钩子函数
        
        可用于:
        - 初始化资源
        - 连接数据库
        - 设置初始状态
        """
        self.logger.info(f"Spider {self.name} opened")
    
    async def spider_closed(self):
        """
        爬虫关闭时调用的钩子函数
        
        可用于:
        - 清理资源
        - 关闭数据库连接
        """
        # 不再输出任何信息，避免与统计信息重复
        # 统计信息由StatsCollector负责输出
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def set_custom_setting(self, key: str, value: Any) -> 'Spider':
        """
        设置自定义配置（链式调用）
        
        :param key: 配置键名
        :param value: 配置值
        :return: self（支持链式调用）
        
        示例:
            spider.set_custom_setting('CONCURRENCY', 10)\
                  .set_custom_setting('DOWNLOAD_DELAY', 1.0)
        """
        if not hasattr(self, 'custom_settings') or self.custom_settings is None:
            self.custom_settings = {}
        
        self.custom_settings[key] = value
        self.logger.debug(f"设置自定义配置: {key} = {value}")
        
        # 如果已绑定crawler，立即应用设置
        if self.crawler:
            self.crawler.settings.set(key, value)
            
        return self
    
    def get_custom_setting(self, key: str, default: Any = None) -> Any:
        """
        获取自定义配置值
        
        :param key: 配置键名 
        :param default: 默认值
        :return: 配置值
        """
        if hasattr(self, 'custom_settings') and self.custom_settings:
            return self.custom_settings.get(key, default)
        return default
    
    def get_spider_info(self) -> Dict[str, Any]:
        """
        获取爬虫详细信息
        
        :return: 爬虫信息字典
        """
        info = {
            'name': self.name,
            'class_name': self.__class__.__name__,
            'module': self.__module__,
            'start_urls_count': len(self.start_urls) if self.start_urls else 0,
            'allowed_domains_count': len(self.allowed_domains) if self.allowed_domains else 0,
            'custom_settings_count': len(self.custom_settings) if self.custom_settings else 0,
            'is_distributed': self._is_distributed_mode() if self.crawler else None,
            'has_crawler': self.crawler is not None,
            'logger_name': self.logger.name if hasattr(self, 'logger') else None
        }
        
        # 添加方法检查
        info['methods'] = {
            'has_parse': callable(getattr(self, 'parse', None)),
            'has_spider_opened': callable(getattr(self, 'spider_opened', None)),
            'has_spider_closed': callable(getattr(self, 'spider_closed', None)),
            'has_start_requests': callable(getattr(self, 'start_requests', None))
        }
        
        return info
    
    def make_request(self, url: str, callback=None, **kwargs) -> Request:
        """
        便捷方法：创建 Request 对象
        
        :param url: 请求URL
        :param callback: 回调函数（默认为parse）
        :param kwargs: 其他Request参数
        :return: Request对象
        """
        return Request(
            url=url,
            callback=callback or self.parse,
            meta={'spider_name': self.name},
            **kwargs
        )


# === 高级爬虫功能扩展 ===

class SpiderStatsTracker:
    """
    爬虫统计跟踪器
    提供详细的性能监控功能
    """
    
    def __init__(self, spider_name: str):
        self.spider_name = spider_name
        self.start_time = None
        self.end_time = None
        self.request_count = 0
        self.response_count = 0
        self.item_count = 0
        self.error_count = 0
        self.domain_stats = {}
        
    def start_tracking(self):
        """开始统计"""
        import time
        self.start_time = time.time()
        
    def stop_tracking(self):
        """停止统计"""
        import time
        self.end_time = time.time()
        
    def record_request(self, url: str):
        """记录请求"""
        self.request_count += 1
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        self.domain_stats[domain] = self.domain_stats.get(domain, 0) + 1
        
    def record_response(self):
        """记录响应"""
        self.response_count += 1
        
    def record_item(self):
        """记录Item"""
        self.item_count += 1
        
    def record_error(self):
        """记录错误"""
        self.error_count += 1
        
    def get_summary(self) -> Dict[str, Any]:
        """获取统计摘要"""
        duration = (self.end_time - self.start_time) if (self.start_time and self.end_time) else 0
        
        return {
            'spider_name': self.spider_name,
            'duration_seconds': round(duration, 2),
            'requests': self.request_count,
            'responses': self.response_count,
            'items': self.item_count,
            'errors': self.error_count,
            'success_rate': round((self.response_count / max(1, self.request_count)) * 100, 2),
            'requests_per_second': round(self.request_count / max(1, duration), 2),
            'top_domains': sorted(
                self.domain_stats.items(), 
                key=lambda x: x[1], 
                reverse=True
            )[:5]
        }


def create_spider_from_template(name: str, start_urls: List[str], **options) -> Type[Spider]:
    """
    从模板快速创建爬虫类
    
    :param name: 爬虫名称
    :param start_urls: 起始URL列表
    :param options: 其他选项
    :return: 新创建的爬虫类
    
    示例:
        MySpider = create_spider_from_template(
            name='quick_spider',
            start_urls=['http://example.com'],
            allowed_domains=['example.com'],
            custom_settings={'CONCURRENCY': 5}
        )
    """
    
    # 动态创建爬虫类
    class_attrs = {
        'name': name,
        'start_urls': start_urls,
        'allowed_domains': options.get('allowed_domains', []),
        'custom_settings': options.get('custom_settings', {})
    }
    
    # 添加自定义parse方法
    if 'parse_function' in options:
        class_attrs['parse'] = options['parse_function']
    else:
        def default_parse(self, response):
            """默认解析方法"""
            yield {'url': response.url, 'title': getattr(response, 'title', 'N/A')}
        class_attrs['parse'] = default_parse
    
    # 创建类名
    class_name = options.get('class_name', f"Generated{name.replace('_', '').title()}Spider")
    
    # 动态创建类
    spider_class = type(class_name, (Spider,), class_attrs)
    
    get_logger(__name__).info(f"动态创建爬虫类: {class_name} (name='{name}')")
    
    return spider_class


# === 公共只读接口 ===
def get_global_spider_registry() -> dict[str, Type[Spider]]:
    """
    获取全局爬虫注册表的副本
    
    :return: 爬虫注册表的副本
    """
    return _DEFAULT_SPIDER_REGISTRY.copy()


def get_spider_by_name(name: str) -> Optional[Type[Spider]]:
    """
    根据名称获取爬虫类
    
    :param name: 爬虫名称
    :return: 爬虫类或None
    """
    return _DEFAULT_SPIDER_REGISTRY.get(name)


def get_all_spider_classes() -> List[Type[Spider]]:
    """
    获取所有注册的爬虫类
    
    :return: 爬虫类列表
    """
    return list(set(_DEFAULT_SPIDER_REGISTRY.values()))


def get_spider_names() -> List[str]:
    """
    获取所有爬虫名称
    
    :return: 爬虫名称列表
    """
    return list(_DEFAULT_SPIDER_REGISTRY.keys())


def is_spider_registered(name: str) -> bool:
    """
    检查爬虫是否已注册
    
    :param name: 爬虫名称
    :return: 是否已注册
    """
    return name in _DEFAULT_SPIDER_REGISTRY


def unregister_spider(name: str) -> bool:
    """
    取消注册爬虫（仅用于测试）
    
    :param name: 爬虫名称
    :return: 是否成功取消注册
    """
    if name in _DEFAULT_SPIDER_REGISTRY:
        del _DEFAULT_SPIDER_REGISTRY[name]
        return True
    return False


# 导出的公共接口
__all__ = [
    'Spider',
    'SpiderMeta', 
    'SpiderStatsTracker',
    'create_spider_from_template',
    'get_global_spider_registry',
    'get_spider_by_name',
    'get_all_spider_classes',
    'get_spider_names',
    'is_spider_registered',
    'unregister_spider'
]


```

**code file end: crawlo/spider/__init__.py**

---


### code file start: crawlo/tools/date_tools.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-05-17 10:20
# @Author  : crawl-coder
# @Desc    : 智能时间工具库（专为爬虫场景设计）
"""
import dateparser
from typing import Optional, Union, Literal
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
import pytz
from pytz import timezone as pytz_timezone

# 支持的单位类型
TimeUnit = Literal["seconds", "minutes", "hours", "days"]
# 时间输入类型
TimeType = Union[str, datetime]
# 时区类型
TimezoneType = Union[str, timezone, pytz_timezone]

# 常见时间格式列表（作为 dateparser 的后备方案）
COMMON_FORMATS = [
    "%Y-%m-%d %H:%M:%S",
    "%Y/%m/%d %H:%M:%S",
    "%d-%m-%Y %H:%M:%S",
    "%d/%m/%Y %H:%M:%S",
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%b %d, %Y",
    "%B %d, %Y",
    "%Y年%m月%d日",
    "%Y年%m月%d日 %H时%M分%S秒",
    "%a %b %d %H:%M:%S %Y",
    "%a, %d %b %Y %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%dT%H:%M:%S",
]


class TimeUtils:
    """
    时间处理工具类，提供日期解析、格式化、计算等一站式服务。
    特别适用于爬虫中处理多语言、多格式、相对时间的场景。
    """

    @staticmethod
    def _try_strptime(time_str: str) -> Optional[datetime]:
        """尝试使用预定义格式解析，作为 dateparser 的后备"""
        for fmt in COMMON_FORMATS:
            try:
                return datetime.strptime(time_str.strip(), fmt)
            except ValueError:
                continue
        return None

    @classmethod
    def parse(cls, time_input: TimeType, *, default: Optional[datetime] = None) -> Optional[datetime]:
        """
        智能解析时间输入（字符串或 datetime）。

        :param time_input: 时间字符串（支持各种语言、格式、相对时间）或 datetime 对象
        :param default: 解析失败时返回的默认值
        :return: 解析成功返回 datetime，失败返回 default
        """
        if isinstance(time_input, datetime):
            return time_input

        if not isinstance(time_input, str) or not time_input.strip():
            return default

        # 1. 优先使用 dateparser（支持多语言和相对时间）
        try:
            parsed = dateparser.parse(time_input.strip())
            if parsed:
                return parsed
        except Exception:
            pass  # 忽略异常，尝试后备方案

        # 2. 尝试使用常见格式解析
        try:
            parsed = cls._try_strptime(time_input)
            if parsed:
                return parsed
        except Exception:
            pass

        return default

    @classmethod
    def format(cls, dt: TimeType, fmt: str = "%Y-%m-%d %H:%M:%S") -> Optional[str]:
        """
        格式化时间。

        :param dt: datetime 对象或可解析的字符串
        :param fmt: 输出格式
        :return: 格式化后的字符串，失败返回 None
        """
        if isinstance(dt, str):
            dt = cls.parse(dt)
            if dt is None:
                return None
        try:
            return dt.strftime(fmt)
        except Exception:
            return None

    @classmethod
    def to_timestamp(cls, dt: TimeType) -> Optional[float]:
        """转换为时间戳（秒级）"""
        if isinstance(dt, str):
            dt = cls.parse(dt)
            if dt is None:
                return None
        try:
            return dt.timestamp()
        except Exception:
            return None

    @classmethod
    def from_timestamp(cls, ts: float) -> Optional[datetime]:
        """从时间戳创建 datetime"""
        try:
            return datetime.fromtimestamp(ts)
        except Exception:
            return None

    @classmethod
    def diff(cls, start: TimeType, end: TimeType, unit: TimeUnit = "seconds") -> Optional[int]:
        """
        计算两个时间的差值（自动解析字符串）。

        :param start: 起始时间
        :param end: 结束时间
        :param unit: 单位 ('seconds', 'minutes', 'hours', 'days')
        :return: 差值（绝对值），失败返回 None
        """
        start_dt = cls.parse(start)
        end_dt = cls.parse(end)
        if not start_dt or not end_dt:
            return None

        delta = abs((end_dt - start_dt).total_seconds())

        unit_map = {
            "seconds": 1,
            "minutes": 60,
            "hours": 3600,
            "days": 86400,
        }
        return int(delta // unit_map.get(unit, 1))

    @classmethod
    def add_days(cls, dt: TimeType, days: int) -> Optional[datetime]:
        """日期加减（天）"""
        dt = cls.parse(dt)
        if dt is None:
            return None
        return dt + timedelta(days=days)

    @classmethod
    def add_months(cls, dt: TimeType, months: int) -> Optional[datetime]:
        """日期加减（月）"""
        dt = cls.parse(dt)
        if dt is None:
            return None
        return dt + relativedelta(months=months)

    @classmethod
    def days_between(cls, dt1: TimeType, dt2: TimeType) -> Optional[int]:
        """计算两个日期之间的天数差"""
        return cls.diff(dt1, dt2, "days")

    @classmethod
    def is_leap_year(cls, year: int) -> bool:
        """判断是否是闰年"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def now(cls, fmt: Optional[str] = None) -> Union[datetime, str]:
        """
        获取当前时间。

        :param fmt: 如果提供，则返回格式化字符串；否则返回 datetime 对象。
        :return: datetime 或 str
        """
        dt = datetime.now()
        if fmt is not None:
            return dt.strftime(fmt)
        return dt

    @classmethod
    def iso_format(cls, dt: TimeType) -> Optional[str]:
        """返回 ISO 8601 格式字符串"""
        dt = cls.parse(dt)
        if dt is None:
            return None
        return dt.isoformat()

    @classmethod
    def to_timezone(cls, dt: TimeType, tz: TimezoneType) -> Optional[datetime]:
        """将时间转换为指定时区"""
        dt = cls.parse(dt)
        if dt is None:
            return None
        
        try:
            if isinstance(tz, str):
                tz = pytz_timezone(tz)
            return dt.astimezone(tz)
        except Exception:
            return None

    @classmethod
    def to_utc(cls, dt: TimeType) -> Optional[datetime]:
        """将时间转换为 UTC 时区"""
        return cls.to_timezone(dt, pytz.UTC)

    @classmethod
    def to_local(cls, dt: TimeType) -> Optional[datetime]:
        """将时间转换为本地时区"""
        return cls.to_timezone(dt, pytz.timezone("Asia/Shanghai"))

    @classmethod
    def from_timestamp_with_tz(cls, ts: float, tz: TimezoneType = None) -> Optional[datetime]:
        """从时间戳创建 datetime，并可选择指定时区"""
        try:
            dt = datetime.fromtimestamp(ts)
            if tz:
                if isinstance(tz, str):
                    tz = pytz_timezone(tz)
                dt = dt.replace(tzinfo=tz)
            return dt
        except Exception:
            return None


# =======================对外接口=======================

def parse_time(time_input: TimeType, default: Optional[datetime] = None) -> Optional[datetime]:
    """解析时间字符串或对象"""
    return TimeUtils.parse(time_input, default=default)


def format_time(dt: TimeType, fmt: str = "%Y-%m-%d %H:%M:%S") -> Optional[str]:
    """格式化时间"""
    return TimeUtils.format(dt, fmt)


def time_diff(start: TimeType, end: TimeType, unit: TimeUnit = "seconds") -> Optional[int]:
    """计算时间差"""
    return TimeUtils.diff(start, end, unit)


def to_timestamp(dt: TimeType) -> Optional[float]:
    """转时间戳"""
    return TimeUtils.to_timestamp(dt)


def to_datetime(ts: float) -> Optional[datetime]:
    """从时间戳转 datetime"""
    return TimeUtils.from_timestamp(ts)


def now(fmt: Optional[str] = None) -> Union[datetime, str]:
    """获取当前时间"""
    return TimeUtils.now(fmt)

def to_timezone(dt: TimeType, tz: TimezoneType) -> Optional[datetime]:
    """将时间转换为指定时区"""
    return TimeUtils.to_timezone(dt, tz)

def to_utc(dt: TimeType) -> Optional[datetime]:
    """将时间转换为 UTC 时区"""
    return TimeUtils.to_utc(dt)

def to_local(dt: TimeType) -> Optional[datetime]:
    """将时间转换为本地时区"""
    return TimeUtils.to_local(dt)

def from_timestamp_with_tz(ts: float, tz: TimezoneType = None) -> Optional[datetime]:
    """从时间戳创建 datetime，并可选择指定时区"""
    return TimeUtils.from_timestamp_with_tz(ts, tz)


if __name__ == '__main__':
    get_current_time = now(fmt="%Y-%m-%d %H:%M:%S")
    print(get_current_time)
```

**code file end: crawlo/tools/date_tools.py**

---


### code file start: crawlo/tools/distributed_coordinator.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-09-10 22:00
# @Author  : crawl-coder
# @Desc    : 分布式协调工具
"""

import hashlib
import time
import urllib.parse
from datetime import datetime
from typing import Dict, Any, Optional, Tuple, List, Set
from urllib.parse import urlparse

from crawlo.utils.fingerprint import FingerprintGenerator


class TaskDistributor:
    """任务分发工具类"""

    @staticmethod
    def generate_pagination_tasks(base_url: str, start_page: int = 1,
                                  end_page: int = 100, page_param: str = "page") -> List[str]:
        """
        生成分页任务URL列表
        
        Args:
            base_url (str): 基础URL
            start_page (int): 起始页码
            end_page (int): 结束页码
            page_param (str): 分页参数名
            
        Returns:
            List[str]: 分页URL列表
        """
        tasks = []
        parsed = urlparse(base_url)
        query_dict = dict([q.split('=') for q in parsed.query.split('&') if q]) if parsed.query else {}

        for page in range(start_page, end_page + 1):
            query_dict[page_param] = str(page)
            query_string = '&'.join([f"{k}={v}" for k, v in query_dict.items()])
            new_parsed = parsed._replace(query=query_string)
            tasks.append(urllib.parse.urlunparse(new_parsed))

        return tasks

    @staticmethod
    def distribute_tasks(tasks: List[Any], num_workers: int) -> List[List[Any]]:
        """
        将任务分发给多个工作节点
        
        Args:
            tasks (List[Any]): 任务列表
            num_workers (int): 工作节点数量
            
        Returns:
            List[List[Any]]: 分发后的任务列表
        """
        if num_workers <= 0:
            raise ValueError("工作节点数量必须大于0")

        if not tasks:
            return [[] for _ in range(num_workers)]

        # 计算每个工作节点应分配的任务数量
        tasks_per_worker = len(tasks) // num_workers
        remaining_tasks = len(tasks) % num_workers

        distributed_tasks = []
        task_index = 0

        for i in range(num_workers):
            # 分配基础任务数量
            worker_tasks_count = tasks_per_worker
            # 分配剩余任务
            if i < remaining_tasks:
                worker_tasks_count += 1

            worker_tasks = tasks[task_index:task_index + worker_tasks_count]
            distributed_tasks.append(worker_tasks)
            task_index += worker_tasks_count

        return distributed_tasks


class DeduplicationTool:
    """数据去重工具类"""

    def __init__(self):
        self.memory_set: Set[str] = set()
        self.bloom_filter = None  # 在实际应用中可以集成布隆过滤器

    @staticmethod
    def generate_fingerprint(data: Any) -> str:
        """
        生成数据指纹
        
        Args:
            data (Any): 数据
            
        Returns:
            str: 数据指纹（SHA256哈希）
        """
        return FingerprintGenerator.data_fingerprint(data)

    def is_duplicate(self, data: Any) -> bool:
        """
        检查数据是否重复（内存去重）
        
        Args:
            data (Any): 数据
            
        Returns:
            bool: 是否重复
        """
        fingerprint = self.generate_fingerprint(data)
        return fingerprint in self.memory_set

    def add_to_dedup(self, data: Any) -> bool:
        """
        将数据添加到去重集合
        
        Args:
            data (Any): 数据
            
        Returns:
            bool: 是否成功添加（True表示之前不存在，False表示已存在）
        """
        fingerprint = self.generate_fingerprint(data)
        if fingerprint in self.memory_set:
            return False
        else:
            self.memory_set.add(fingerprint)
            return True

    async def async_is_duplicate(self, data: Any) -> bool:
        """
        异步检查数据是否重复
        
        Args:
            data (Any): 数据
            
        Returns:
            bool: 是否重复
        """
        return self.is_duplicate(data)

    async def async_add_to_dedup(self, data: Any) -> bool:
        """
        异步将数据添加到去重集合
        
        Args:
            data (Any): 数据
            
        Returns:
            bool: 是否成功添加
        """
        return self.add_to_dedup(data)


class DistributedCoordinator:
    """分布式协调工具类"""

    def __init__(self, redis_client: Any = None):
        """
        初始化分布式协调工具
        
        Args:
            redis_client (Any): Redis客户端
        """
        self.redis_client = redis_client
        self.task_distributor = TaskDistributor()
        self.deduplication_tool = DeduplicationTool()

    @staticmethod
    def generate_task_id(url: str, spider_name: str) -> str:
        """
        生成任务ID
        
        Args:
            url (str): URL
            spider_name (str): 爬虫名称
            
        Returns:
            str: 任务ID
        """
        # 使用URL和爬虫名称生成唯一任务ID
        unique_string = f"{url}_{spider_name}_{int(time.time() * 1000)}"
        return hashlib.md5(unique_string.encode('utf-8')).hexdigest()

    async def claim_task(self, task_id: str, worker_id: str,
                         timeout: int = 300) -> Tuple[bool, Optional[str]]:
        """
        声明任务（分布式锁）
        
        Args:
            task_id (str): 任务ID
            worker_id (str): 工作节点ID
            timeout (int): 锁超时时间（秒）
            
        Returns:
            Tuple[bool, Optional[str]]: (是否成功声明, 错误信息)
        """
        # 如果没有Redis客户端，使用内存模拟
        if self.redis_client is None:
            # 模拟成功声明
            return True, None

        try:
            # 实际实现应该使用Redis的SET命令带有NX和EX选项
            # result = await self.redis_client.set(f"task_lock:{task_id}", worker_id, nx=True, ex=timeout)
            # return bool(result), None if result else "任务已被其他节点声明"
            return True, None
        except Exception as e:
            return False, str(e)

    async def report_task_status(self, task_id: str, status: str, worker_id: str) -> bool:
        """
        报告任务状态
        
        Args:
            task_id (str): 任务ID
            status (str): 任务状态 (pending, processing, completed, failed)
            worker_id (str): 工作节点ID
            
        Returns:
            bool: 是否成功报告
        """
        try:
            status_info = {
                "task_id": task_id,
                "status": status,
                "worker_id": worker_id,
                "timestamp": datetime.now().isoformat()
            }

            if self.redis_client is None:
                # 模拟成功报告
                print(f"报告任务状态: {status_info}")
                return True

            # 实际实现应该将状态信息存储到Redis中
            # await self.redis_client.hset(f"task_status:{task_id}", mapping=status_info)
            return True
        except Exception:
            return False

    async def get_cluster_info(self) -> Dict[str, Any]:
        """
        获取集群信息
        
        Returns:
            Dict[str, Any]: 集群信息
        """
        try:
            if self.redis_client is None:
                # 返回模拟的集群信息
                return {
                    "worker_count": 3,
                    "active_workers": ["worker_1", "worker_2", "worker_3"],
                    "task_queue_size": 100,
                    "processed_tasks": 500,
                    "failed_tasks": 5,
                    "timestamp": datetime.now().isoformat()
                }

            # 实际实现应该从Redis获取集群信息
            # 这里返回模拟数据
            return {
                "worker_count": 3,
                "active_workers": ["worker_1", "worker_2", "worker_3"],
                "task_queue_size": 100,
                "processed_tasks": 500,
                "failed_tasks": 5,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}

    def generate_pagination_tasks(self, base_url: str, start_page: int = 1,
                                  end_page: int = 100, page_param: str = "page") -> List[str]:
        """
        生成分页任务URL列表
        
        Args:
            base_url (str): 基础URL
            start_page (int): 起始页码
            end_page (int): 结束页码
            page_param (str): 分页参数名
            
        Returns:
            List[str]: 分页URL列表
        """
        return self.task_distributor.generate_pagination_tasks(base_url, start_page, end_page, page_param)

    def distribute_tasks(self, tasks: List[Any], num_workers: int) -> List[List[Any]]:
        """
        将任务分发给多个工作节点
        
        Args:
            tasks (List[Any]): 任务列表
            num_workers (int): 工作节点数量
            
        Returns:
            List[List[Any]]: 分发后的任务列表
        """
        return self.task_distributor.distribute_tasks(tasks, num_workers)

    async def is_duplicate(self, data: Any) -> bool:
        """
        检查数据是否重复
        
        Args:
            data (Any): 数据
            
        Returns:
            bool: 是否重复
        """
        # 如果有Redis客户端，可以使用布隆过滤器或Redis集合进行去重
        if self.redis_client is not None:
            # 这里可以实现基于Redis的去重逻辑
            pass

        # 使用内存去重作为后备方案
        return await self.deduplication_tool.async_is_duplicate(data)

    async def add_to_dedup(self, data: Any) -> bool:
        """
        将数据添加到去重集合
        
        Args:
            data (Any): 数据
            
        Returns:
            bool: 是否成功添加
        """
        # 如果有Redis客户端，可以使用布隆过滤器或Redis集合进行去重
        if self.redis_client is not None:
            # 这里可以实现基于Redis的去重逻辑
            pass

        # 使用内存去重作为后备方案
        return await self.deduplication_tool.async_add_to_dedup(data)


# 便捷函数
def generate_task_id(url: str, spider_name: str) -> str:
    """生成任务ID"""
    return DistributedCoordinator.generate_task_id(url, spider_name)


async def claim_task(task_id: str, worker_id: str,
                     redis_client: Any = None, timeout: int = 300) -> Tuple[bool, Optional[str]]:
    """声明任务"""
    coordinator = DistributedCoordinator(redis_client)
    return await coordinator.claim_task(task_id, worker_id, timeout)


async def report_task_status(task_id: str, status: str, worker_id: str,
                             redis_client: Any = None) -> bool:
    """报告任务状态"""
    coordinator = DistributedCoordinator(redis_client)
    return await coordinator.report_task_status(task_id, status, worker_id)


async def get_cluster_info(redis_client: Any = None) -> Dict[str, Any]:
    """获取集群信息"""
    coordinator = DistributedCoordinator(redis_client)
    return await coordinator.get_cluster_info()


def generate_pagination_tasks(base_url: str, start_page: int = 1,
                              end_page: int = 100, page_param: str = "page") -> List[str]:
    """生成分页任务URL列表"""
    coordinator = DistributedCoordinator()
    return coordinator.generate_pagination_tasks(base_url, start_page, end_page, page_param)


def distribute_tasks(tasks: List[Any], num_workers: int) -> List[List[Any]]:
    """将任务分发给多个工作节点"""
    coordinator = DistributedCoordinator()
    return coordinator.distribute_tasks(tasks, num_workers)

```

**code file end: crawlo/tools/distributed_coordinator.py**

---


### code file start: crawlo/tools/scenario_adapter.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
场景适配器
=========
根据不同的动态加载场景，自动配置和优化下载器选择策略。

支持的场景:
1. 列表页、详情页都要动态加载
2. 列表页使用协议请求、详情页使用动态加载
3. 列表页使用动态加载，详情页使用协议请求

使用示例:
    # 场景1: 全动态加载
    adapter = DynamicLoadingScenarioAdapter(scenario="all_dynamic")
    
    # 场景2: 列表页协议，详情页动态
    adapter = DynamicLoadingScenarioAdapter(scenario="list_protocol_detail_dynamic")
    
    # 场景3: 列表页动态，详情页协议
    adapter = DynamicLoadingScenarioAdapter(scenario="list_dynamic_detail_protocol")
"""
import re
from typing import Dict, Any
from urllib.parse import urlparse

from crawlo.logging import get_logger


class DynamicLoadingScenarioAdapter:
    """
    动态加载场景适配器
    根据不同的业务场景自动配置下载器选择策略
    """
    
    SCENARIOS = {
        "all_dynamic": "列表页、详情页都要动态加载",
        "list_protocol_detail_dynamic": "列表页使用协议请求、详情页使用动态加载",
        "list_dynamic_detail_protocol": "列表页使用动态加载，详情页使用协议请求"
    }
    
    def __init__(self, scenario: str = "list_protocol_detail_dynamic", **kwargs):
        """
        初始化场景适配器
        
        :param scenario: 场景类型
        :param kwargs: 其他配置参数
        """
        self.scenario = scenario
        self.logger = get_logger(self.__class__.__name__)
        
        # 验证场景类型
        if scenario not in self.SCENARIOS:
            raise ValueError(f"Unsupported scenario: {scenario}. Supported: {list(self.SCENARIOS.keys())}")
            
        self.logger.info(f"Initializing DynamicLoadingScenarioAdapter for scenario: {scenario}")
        
        # 配置参数
        self.list_page_patterns = kwargs.get("list_page_patterns", [
            r"/list", r"/search", r"/category", r"/page/\d+", r"\?page=", r"\?p=\d+"
        ])
        
        self.detail_page_patterns = kwargs.get("detail_page_patterns", [
            r"/detail", r"/item", r"/product", r"/article", r"/post", r"/view", r"/\d+"
        ])
        
        self.list_domains = set(kwargs.get("list_domains", []))
        self.detail_domains = set(kwargs.get("detail_domains", []))
        
        # 构建配置
        self.config = self._build_config()
        
    def _build_config(self) -> Dict[str, Any]:
        """根据场景构建配置"""
        config = {
            "HYBRID_DYNAMIC_URL_PATTERNS": [],
            "HYBRID_PROTOCOL_URL_PATTERNS": [],
            "HYBRID_DYNAMIC_DOMAINS": [],
            "HYBRID_PROTOCOL_DOMAINS": []
        }
        
        if self.scenario == "all_dynamic":
            # 所有页面都使用动态加载
            config["HYBRID_DYNAMIC_URL_PATTERNS"].extend(self.list_page_patterns)
            config["HYBRID_DYNAMIC_URL_PATTERNS"].extend(self.detail_page_patterns)
            
        elif self.scenario == "list_protocol_detail_dynamic":
            # 列表页使用协议请求，详情页使用动态加载
            config["HYBRID_PROTOCOL_URL_PATTERNS"].extend(self.list_page_patterns)
            config["HYBRID_DYNAMIC_URL_PATTERNS"].extend(self.detail_page_patterns)
            
            # 域名配置
            config["HYBRID_PROTOCOL_DOMAINS"].extend(self.list_domains)
            config["HYBRID_DYNAMIC_DOMAINS"].extend(self.detail_domains)
            
        elif self.scenario == "list_dynamic_detail_protocol":
            # 列表页使用动态加载，详情页使用协议请求
            config["HYBRID_DYNAMIC_URL_PATTERNS"].extend(self.list_page_patterns)
            config["HYBRID_PROTOCOL_URL_PATTERNS"].extend(self.detail_page_patterns)
            
            # 域名配置
            config["HYBRID_DYNAMIC_DOMAINS"].extend(self.list_domains)
            config["HYBRID_PROTOCOL_DOMAINS"].extend(self.detail_domains)
            
        return config
    
    def get_settings(self) -> Dict[str, Any]:
        """获取场景配置设置"""
        return self.config
    
    def should_use_dynamic_loader(self, url: str) -> bool:
        """
        判断给定URL是否应该使用动态加载器
        
        :param url: 要判断的URL
        :return: 是否使用动态加载器
        """
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        path = parsed_url.path.lower()
        query = parsed_url.query.lower()
        full_path = path + ("?" + query if query else "")
        
        # 检查域名
        if domain in self.config["HYBRID_DYNAMIC_DOMAINS"]:
            return True
        if domain in self.config["HYBRID_PROTOCOL_DOMAINS"]:
            return False
            
        # 检查URL模式
        # 检查动态模式
        for pattern in self.config["HYBRID_DYNAMIC_URL_PATTERNS"]:
            if re.search(pattern, full_path):
                return True
                
        # 检查协议模式
        for pattern in self.config["HYBRID_PROTOCOL_URL_PATTERNS"]:
            if re.search(pattern, full_path):
                return False
                
        # 默认策略
        if self.scenario == "all_dynamic":
            return True
        elif self.scenario == "list_protocol_detail_dynamic":
            # 默认详情页使用动态加载
            return True
        elif self.scenario == "list_dynamic_detail_protocol":
            # 默认详情页使用协议加载
            return False
            
        # 默认返回False（使用协议加载器）
        return False
    
    def get_loader_options(self, url: str) -> Dict[str, Any]:
        """
        获取特定URL的加载器选项
        
        :param url: URL
        :return: 加载器选项
        """
        options = {}
        
        # 可以根据URL添加特定的加载器选项
        # 例如，对于某些页面可能需要等待特定元素加载完成
        if "product" in url:
            options["wait_for_element"] = ".product-detail"
        elif "article" in url:
            options["wait_for_element"] = ".article-content"
            
        return options
    
    def adapt_request(self, request) -> None:
        """
        适配请求对象，根据场景自动设置加载器
        
        :param request: 请求对象
        """
        use_dynamic = self.should_use_dynamic_loader(request.url)
        
        if use_dynamic:
            request.set_dynamic_loader(True, self.get_loader_options(request.url))
            self.logger.debug(f"Adapted request {request.url} to use dynamic loader")
        else:
            request.set_protocol_loader()
            self.logger.debug(f"Adapted request {request.url} to use protocol loader")


# 便利函数
def create_scenario_adapter(scenario: str = "list_protocol_detail_dynamic", **kwargs):
    """
    创建场景适配器的便利函数
    
    :param scenario: 场景类型
    :param kwargs: 其他配置参数
    :return: 场景适配器实例
    """
    return DynamicLoadingScenarioAdapter(scenario, **kwargs)


def get_scenario_settings(scenario: str = "list_protocol_detail_dynamic", **kwargs) -> Dict[str, Any]:
    """
    获取场景配置设置的便利函数
    
    :param scenario: 场景类型
    :param kwargs: 其他配置参数
    :return: 配置设置字典
    """
    adapter = DynamicLoadingScenarioAdapter(scenario, **kwargs)
    return adapter.get_settings()


# 预定义场景配置
SCENARIO_CONFIGS = {
    "电商网站": {
        "scenario": "list_protocol_detail_dynamic",
        "list_page_patterns": [r"/list", r"/search", r"/category", r"/page/\d+"],
        "detail_page_patterns": [r"/product", r"/item", r"/detail/\d+"],
        "list_domains": [],
        "detail_domains": []
    },
    
    "新闻网站": {
        "scenario": "list_protocol_detail_dynamic",
        "list_page_patterns": [r"/list", r"/category", r"/page/\d+"],
        "detail_page_patterns": [r"/article", r"/post", r"/news/\d+"],
        "list_domains": [],
        "detail_domains": []
    },
    
    "社交平台": {
        "scenario": "all_dynamic",
        "list_page_patterns": [r"/feed", r"/timeline", r"/explore"],
        "detail_page_patterns": [r"/post", r"/status", r"/photo"],
        "list_domains": [],
        "detail_domains": []
    },
    
    "博客平台": {
        "scenario": "list_dynamic_detail_protocol",
        "list_page_patterns": [r"/blog", r"/posts", r"/archive"],
        "detail_page_patterns": [r"/\d{4}/\d{2}/\d{2}/"],
        "list_domains": [],
        "detail_domains": []
    }
}


def create_adapter_for_platform(platform: str, **custom_kwargs) -> DynamicLoadingScenarioAdapter:
    """
    为特定平台创建场景适配器
    
    :param platform: 平台名称
    :param custom_kwargs: 自定义配置参数
    :return: 场景适配器实例
    """
    if platform not in SCENARIO_CONFIGS:
        raise ValueError(f"Unsupported platform: {platform}. Supported: {list(SCENARIO_CONFIGS.keys())}")
    
    config = SCENARIO_CONFIGS[platform].copy()
    config.update(custom_kwargs)
    scenario = config.pop("scenario")
    
    return DynamicLoadingScenarioAdapter(scenario, **config)
```

**code file end: crawlo/tools/scenario_adapter.py**

---


### code file start: crawlo/tools/text_cleaner.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-09-10 22:00
# @Author  : crawl-coder
# @Desc    : 文本清洗工具
"""
import html
import re
import unicodedata
from typing import List


class TextCleaner:
    """
    文本清洗工具类，提供各种文本清洗功能。
    特别适用于爬虫中处理网页内容的清洗需求。
    """

    @staticmethod
    def remove_html_tags(text: str) -> str:
        """
        移除HTML标签
        
        :param text: 包含HTML标签的文本
        :return: 移除HTML标签后的文本
        """
        if not isinstance(text, str):
            return str(text)
        
        # 使用正则表达式移除HTML标签
        clean_text = re.sub(r'<[^>]+>', '', text)
        return clean_text.strip()

    @staticmethod
    def decode_html_entities(text: str) -> str:
        """
        解码HTML实体字符
        
        :param text: 包含HTML实体字符的文本
        :return: 解码后的文本
        """
        if not isinstance(text, str):
            return str(text)
        
        return html.unescape(text)

    @staticmethod
    def remove_extra_whitespace(text: str) -> str:
        """
        移除多余的空白字符（包括空格、制表符、换行符等）
        
        :param text: 文本
        :return: 清理后的文本
        """
        if not isinstance(text, str):
            return str(text)
        
        # 将多个连续的空白字符替换为单个空格
        clean_text = re.sub(r'\s+', ' ', text)
        return clean_text.strip()

    @staticmethod
    def remove_special_chars(text: str, chars: str = '') -> str:
        """
        移除特殊字符
        
        :param text: 文本
        :param chars: 要移除的特殊字符
        :return: 清理后的文本
        """
        if not isinstance(text, str):
            return str(text)
        
        # 移除常见的特殊字符
        special_chars = r'[^\w\s\u4e00-\u9fff' + chars + r']'
        clean_text = re.sub(special_chars, '', text)
        return clean_text

    @staticmethod
    def normalize_unicode(text: str) -> str:
        """
        标准化Unicode字符
        
        :param text: 文本
        :return: 标准化后的文本
        """
        if not isinstance(text, str):
            return str(text)
        
        return unicodedata.normalize('NFKC', text)

    @staticmethod
    def clean_text(text: str, 
                   remove_html: bool = True,
                   decode_entities: bool = True,
                   remove_whitespace: bool = True,
                   remove_special: bool = False,
                   normalize: bool = True) -> str:
        """
        综合文本清洗方法
        
        :param text: 原始文本
        :param remove_html: 是否移除HTML标签
        :param decode_entities: 是否解码HTML实体
        :param remove_whitespace: 是否移除多余空白字符
        :param remove_special: 是否移除特殊字符
        :param normalize: 是否标准化Unicode字符
        :return: 清洗后的文本
        """
        if not isinstance(text, str):
            text = str(text)
        
        if not text:
            return text
            
        # 按顺序进行清洗
        if remove_html:
            text = TextCleaner.remove_html_tags(text)
        
        if decode_entities:
            text = TextCleaner.decode_html_entities(text)
        
        if normalize:
            text = TextCleaner.normalize_unicode(text)
        
        if remove_whitespace:
            text = TextCleaner.remove_extra_whitespace(text)
        
        if remove_special:
            text = TextCleaner.remove_special_chars(text)
        
        return text

    @staticmethod
    def extract_numbers(text: str) -> List[str]:
        """
        从文本中提取数字
        
        :param text: 文本
        :return: 数字列表
        """
        if not isinstance(text, str):
            return []
        
        # 匹配整数和小数
        numbers = re.findall(r'-?\d+\.?\d*', text)
        return numbers

    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """
        从文本中提取邮箱地址
        
        :param text: 文本
        :return: 邮箱地址列表
        """
        if not isinstance(text, str):
            return []
        
        # 匹配邮箱地址
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return emails

    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """
        从文本中提取URL
        
        :param text: 文本
        :return: URL列表
        """
        if not isinstance(text, str):
            return []
        
        # 匹配URL
        urls = re.findall(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            text
        )
        return urls


# =======================对外接口=======================

def remove_html_tags(text: str) -> str:
    """移除HTML标签"""
    return TextCleaner.remove_html_tags(text)


def decode_html_entities(text: str) -> str:
    """解码HTML实体字符"""
    return TextCleaner.decode_html_entities(text)


def remove_extra_whitespace(text: str) -> str:
    """移除多余的空白字符"""
    return TextCleaner.remove_extra_whitespace(text)


def remove_special_chars(text: str, chars: str = '') -> str:
    """移除特殊字符"""
    return TextCleaner.remove_special_chars(text, chars)


def normalize_unicode(text: str) -> str:
    """标准化Unicode字符"""
    return TextCleaner.normalize_unicode(text)


def clean_text(text: str, 
               remove_html: bool = True,
               decode_entities: bool = True,
               remove_whitespace: bool = True,
               remove_special: bool = False,
               normalize: bool = True) -> str:
    """综合文本清洗"""
    return TextCleaner.clean_text(text, remove_html, decode_entities, remove_whitespace, remove_special, normalize)


def extract_numbers(text: str) -> List[str]:
    """提取数字"""
    return TextCleaner.extract_numbers(text)


def extract_emails(text: str) -> List[str]:
    """提取邮箱地址"""
    return TextCleaner.extract_emails(text)


def extract_urls(text: str) -> List[str]:
    """提取URL"""
    return TextCleaner.extract_urls(text)
```

**code file end: crawlo/tools/text_cleaner.py**

---


### code file start: crawlo/tools/__init__.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# @Time    : 2025-09-10 22:00
# @Author  : crawl-coder
# @Desc    : Crawlo框架工具包集合
"""

# 日期工具封装
from .date_tools import (
    TimeUtils,
    parse_time,
    format_time,
    time_diff,
    to_timestamp,
    to_datetime,
    now,
    to_timezone,
    to_utc,
    to_local,
    from_timestamp_with_tz
)

# 数据清洗工具封装
from .text_cleaner import (
    TextCleaner,
    remove_html_tags,
    decode_html_entities,
    remove_extra_whitespace,
    remove_special_chars,
    normalize_unicode,
    clean_text,
    extract_numbers,
    extract_emails,
    extract_urls
)

# 分布式协调工具
from .distributed_coordinator import (
    TaskDistributor,
    DeduplicationTool,
    DistributedCoordinator,
    generate_task_id,
    claim_task,
    report_task_status,
    get_cluster_info,
    generate_pagination_tasks,
    distribute_tasks
)

__all__ = [
    # 日期工具
    "TimeUtils",
    "parse_time",
    "format_time",
    "time_diff",
    "to_timestamp",
    "to_datetime",
    "now",
    "to_timezone",
    "to_utc",
    "to_local",
    "from_timestamp_with_tz",
    
    # 数据清洗工具
    "TextCleaner",
    "remove_html_tags",
    "decode_html_entities",
    "remove_extra_whitespace",
    "remove_special_chars",
    "normalize_unicode",
    "clean_text",
    "extract_numbers",
    "extract_emails",
    "extract_urls",
    
    # 分布式协调工具
    "TaskDistributor",
    "DeduplicationTool",
    "DistributedCoordinator",
    "generate_task_id",
    "claim_task",
    "report_task_status",
    "get_cluster_info",
    "generate_pagination_tasks",
    "distribute_tasks"
]
```

**code file end: crawlo/tools/__init__.py**

---


### code file start: crawlo/utils/batch_processor.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
批处理操作工具
提供批量操作的统一接口和优化实现
"""
import asyncio
from functools import wraps
from typing import List, Callable, Any, Optional, Dict

from crawlo.utils.error_handler import ErrorHandler
from crawlo.logging import get_logger


class BatchProcessor:
    """批处理处理器"""
    
    def __init__(self, batch_size: int = 100, max_concurrent_batches: int = 5):
        self.batch_size = batch_size
        self.max_concurrent_batches = max_concurrent_batches
        self.logger = get_logger(self.__class__.__name__)
        self.error_handler = ErrorHandler(self.__class__.__name__)
    
    async def process_batch(self, items: List[Any], processor_func: Callable, 
                           *args, **kwargs) -> List[Any]:
        """
        处理一批数据项
        
        Args:
            items: 要处理的数据项列表
            processor_func: 处理函数
            *args: 传递给处理函数的额外参数
            **kwargs: 传递给处理函数的关键字参数
            
        Returns:
            处理结果列表
        """
        results = []
        semaphore = asyncio.Semaphore(self.max_concurrent_batches)
        
        async def process_item(item):
            async with semaphore:
                try:
                    if asyncio.iscoroutinefunction(processor_func):
                        return await processor_func(item, *args, **kwargs)
                    else:
                        return processor_func(item, *args, **kwargs)
                except Exception as e:
                    self.logger.error(f"处理单项失败: {e}")
                    return None
        
        # 并发处理批次中的所有项
        tasks = [process_item(item) for item in items]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # 过滤掉异常结果
        return [result for result in results if not isinstance(result, Exception)]
    
    async def process_in_batches(self, items: List[Any], processor_func: Callable,
                                *args, **kwargs) -> List[Any]:
        """
        分批处理大量数据项
        
        Args:
            items: 要处理的数据项列表
            processor_func: 处理函数
            *args: 传递给处理函数的额外参数
            **kwargs: 传递给处理函数的关键字参数
            
        Returns:
            所有处理结果的列表
        """
        all_results = []
        
        # 将数据分批处理
        for i in range(0, len(items), self.batch_size):
            batch = items[i:i + self.batch_size]
            self.logger.debug(f"处理批次 {i//self.batch_size + 1}/{(len(items)-1)//self.batch_size + 1}")
            
            try:
                batch_results = await self.process_batch(batch, processor_func, *args, **kwargs)
                all_results.extend(batch_results)
            except Exception as e:
                self.logger.error(f"处理批次失败: {e}")
                # 继续处理下一个批次而不是中断
        
        return all_results
    
    def batch_process_decorator(self, batch_size: Optional[int] = None):
        """
        装饰器：将函数转换为批处理函数
        
        Args:
            batch_size: 批次大小（如果为None则使用实例的batch_size）
        """
        def decorator(func):
            @wraps(func)
            async def async_wrapper(items: List[Any], *args, **kwargs):
                actual_batch_size = batch_size or self.batch_size
                processor = BatchProcessor(actual_batch_size, self.max_concurrent_batches)
                return await processor.process_in_batches(items, func, *args, **kwargs)
            
            @wraps(func)
            def sync_wrapper(items: List[Any], *args, **kwargs):
                # 同步版本使用事件循环运行异步函数
                return asyncio.run(async_wrapper(items, *args, **kwargs))
            
            # 根据原函数是否为异步函数返回相应的包装器
            import inspect
            if inspect.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper
        
        return decorator


class RedisBatchProcessor:
    """Redis批处理处理器"""
    
    def __init__(self, redis_client, batch_size: int = 100):
        self.redis_client = redis_client
        self.batch_size = batch_size
        self.logger = get_logger(self.__class__.__name__)
        self.error_handler = ErrorHandler(self.__class__.__name__)
    
    async def batch_set(self, items: List[Dict[str, Any]]) -> int:
        """
        批量设置Redis键值对
        
        Args:
            items: 包含key和value的字典列表
            
        Returns:
            成功设置的键值对数量
        """
        try:
            pipe = self.redis_client.pipeline()
            count = 0
            
            for item in items:
                if 'key' in item and 'value' in item:
                    pipe.set(item['key'], item['value'])
                    count += 1
                    
                    # 每达到批次大小就执行一次
                    if count % self.batch_size == 0:
                        result = pipe.execute()
                        # 处理可能的异步情况
                        if asyncio.iscoroutine(result):
                            await result
                        pipe = self.redis_client.pipeline()
            
            # 执行剩余的操作
            if count % self.batch_size != 0:
                result = pipe.execute()
                # 处理可能的异步情况
                if asyncio.iscoroutine(result):
                    await result
            
            self.logger.debug(f"批量设置 {count} 个键值对")
            return count
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="Redis批量设置失败", 
                raise_error=False
            )
            return 0
    
    async def batch_get(self, keys: List[str]) -> Dict[str, Any]:
        """
        批量获取Redis键值
        
        Args:
            keys: 要获取的键列表
            
        Returns:
            键值对字典
        """
        try:
            # 使用管道批量获取
            pipe = self.redis_client.pipeline()
            for key in keys:
                pipe.get(key)
            
            result = pipe.execute()
            # 处理可能的异步情况
            if asyncio.iscoroutine(result):
                results = await result
            else:
                results = result
            
            # 构建结果字典
            result_dict = {}
            for i, key in enumerate(keys):
                if results[i] is not None:
                    result_dict[key] = results[i]
            
            self.logger.debug(f"批量获取 {len(result_dict)} 个键值对")
            return result_dict
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="Redis批量获取失败", 
                raise_error=False
            )
            return {}
    
    async def batch_delete(self, keys: List[str]) -> int:
        """
        批量删除Redis键
        
        Args:
            keys: 要删除的键列表
            
        Returns:
            成功删除的键数量
        """
        try:
            pipe = self.redis_client.pipeline()
            count = 0
            
            for key in keys:
                pipe.delete(key)
                count += 1
                
                # 每达到批次大小就执行一次
                if count % self.batch_size == 0:
                    result = pipe.execute()
                    # 处理可能的异步情况
                    if asyncio.iscoroutine(result):
                        await result
                    pipe = self.redis_client.pipeline()
            
            # 执行剩余的操作
            if count % self.batch_size != 0:
                result = pipe.execute()
                # 处理可能的异步情况
                if asyncio.iscoroutine(result):
                    await result
            
            self.logger.debug(f"批量删除 {count} 个键")
            return count
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="Redis批量删除失败", 
                raise_error=False
            )
            return 0


# 全局批处理器实例
default_batch_processor = BatchProcessor()


def batch_process(items: List[Any], processor_func: Callable, 
                 batch_size: int = 100, max_concurrent_batches: int = 5,
                 *args, **kwargs) -> List[Any]:
    """
    便捷函数：批处理数据项
    
    Args:
        items: 要处理的数据项列表
        processor_func: 处理函数
        batch_size: 批次大小
        max_concurrent_batches: 最大并发批次数量
        *args: 传递给处理函数的额外参数
        **kwargs: 传递给处理函数的关键字参数
        
    Returns:
        所有处理结果的列表
    """
    processor = BatchProcessor(batch_size, max_concurrent_batches)
    import asyncio
    return asyncio.run(processor.process_in_batches(items, processor_func, *args, **kwargs))
```

**code file end: crawlo/utils/batch_processor.py**

---


### code file start: crawlo/utils/config_manager.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
配置管理模块
===========
统一的配置管理接口，整合了通用配置工具、环境变量管理和大规模爬虫配置。

本模块包含：
1. ConfigUtils - 通用配置工具类
2. EnvConfigManager - 环境变量配置管理器
3. LargeScaleConfig - 大规模爬虫配置类
4. 便捷函数 - 快速访问常用配置功能
"""

import os
import re
from typing import Any, Dict, List, Optional, Union


# ============================================================================
# 第一部分：通用配置工具
# ============================================================================

class ConfigUtils:
    """通用配置工具类"""
    
    @staticmethod
    def get_config_value(
        config_sources: List[Union[Dict, Any]], 
        key: str, 
        default: Any = None,
        value_type: type = str
    ) -> Any:
        """
        从多个配置源中获取配置值
        
        Args:
            config_sources: 配置源列表，按优先级排序
            key: 配置键名
            default: 默认值
            value_type: 值类型
            
        Returns:
            配置值或默认值
        """
        for config_source in config_sources:
            if not config_source:
                continue
                
            # 获取配置值
            value = None
            if hasattr(config_source, 'get'):
                value = config_source.get(key)
            elif hasattr(config_source, key):
                value = getattr(config_source, key)
            else:
                continue
                
            if value is not None:
                # 类型转换
                try:
                    if value_type == bool:
                        if isinstance(value, str):
                            return value.lower() in ('1', 'true', 'yes', 'on')
                        return bool(value)
                    elif value_type == int:
                        return int(value)
                    elif value_type == float:
                        return float(value)
                    else:
                        return value_type(value)
                except (ValueError, TypeError):
                    continue
        
        return default
    
    @staticmethod
    def has_config_prefix(config_source: Union[Dict, Any], prefix: str) -> bool:
        """
        检查配置源是否包含指定前缀的配置项
        
        Args:
            config_source: 配置源
            prefix: 前缀
            
        Returns:
            是否包含指定前缀的配置项
        """
        if not config_source:
            return False
            
        if hasattr(config_source, 'keys'):
            return any(key.startswith(prefix) for key in config_source.keys())
        elif hasattr(config_source, '__dict__'):
            return any(key.startswith(prefix) for key in config_source.__dict__.keys())
        else:
            return any(key.startswith(prefix) for key in dir(config_source))
    
    @staticmethod
    def merge_config_sources(config_sources: List[Union[Dict, Any]]) -> Dict[str, Any]:
        """
        合并多个配置源，后面的配置源优先级更高
        
        Args:
            config_sources: 配置源列表
            
        Returns:
            合并后的配置字典
        """
        merged_config = {}
        
        for config_source in config_sources:
            if not config_source:
                continue
                
            if hasattr(config_source, 'keys'):
                # 字典类型配置源
                for key, value in config_source.items():
                    if key.isupper():  # 只合并大写的配置项
                        merged_config[key] = value
            elif hasattr(config_source, '__dict__'):
                # 对象类型配置源
                for key, value in config_source.__dict__.items():
                    if key.isupper():
                        merged_config[key] = value
            else:
                # 其他类型配置源
                for key in dir(config_source):
                    if key.isupper():
                        merged_config[key] = getattr(config_source, key)
        
        return merged_config


# ============================================================================
# 第二部分：环境变量配置管理
# ============================================================================

class EnvConfigManager:
    """环境变量配置管理器"""
    
    @staticmethod
    def get_env_var(var_name: str, default: Any = None, var_type: type = str) -> Any:
        """
        获取环境变量值
        
        Args:
            var_name: 环境变量名称
            default: 默认值
            var_type: 变量类型 (str, int, float, bool)
            
        Returns:
            环境变量值或默认值
        """
        value = os.getenv(var_name)
        if value is None:
            return default
        
        try:
            if var_type == bool:
                return value.lower() in ('1', 'true', 'yes', 'on')
            elif var_type == int:
                return int(value)
            elif var_type == float:
                return float(value)
            else:
                return value
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def get_redis_config() -> dict:
        """
        获取 Redis 配置
        
        Returns:
            Redis 配置字典
        """
        return {
            'REDIS_HOST': EnvConfigManager.get_env_var('CRAWLO_REDIS_HOST', '127.0.0.1', str),
            'REDIS_PORT': EnvConfigManager.get_env_var('CRAWLO_REDIS_PORT', 6379, int),
            'REDIS_PASSWORD': EnvConfigManager.get_env_var('CRAWLO_REDIS_PASSWORD', '', str),
            'REDIS_DB': EnvConfigManager.get_env_var('CRAWLO_REDIS_DB', 0, int),
        }
    
    @staticmethod
    def get_runtime_config() -> dict:
        """
        获取运行时配置
        
        Returns:
            运行时配置字典
        """
        return {
            'CRAWLO_MODE': EnvConfigManager.get_env_var('CRAWLO_MODE', 'standalone', str),
            'PROJECT_NAME': EnvConfigManager.get_env_var('CRAWLO_PROJECT_NAME', 'crawlo', str),
            'CONCURRENCY': EnvConfigManager.get_env_var('CRAWLO_CONCURRENCY', 8, int),
        }

    @staticmethod
    def get_version() -> str:
        """
        获取框架版本号
        
        Returns:
            框架版本号字符串
        """
        # 获取版本文件路径
        version_file = os.path.join(os.path.dirname(__file__), '..', '__version__.py')
        default_version = '1.0.0'
        
        if os.path.exists(version_file):
            try:
                with open(version_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # 使用正则表达式提取版本号
                    version_match = re.search(r"__version__\s*=\s*['\"]([^'\"]*)['\"]", content)
                    if version_match:
                        return version_match.group(1)
            except Exception:
                # 如果读取失败，使用默认版本号
                pass
        
        return default_version


# ============================================================================
# 第三部分：大规模爬虫配置
# ============================================================================

class LargeScaleConfig:
    """大规模爬虫配置类"""
    
    @staticmethod
    def conservative_config(concurrency: int = 8) -> Dict[str, Any]:
        """
        保守配置 - 适用于资源有限的环境
        
        特点：
        - 较小的队列容量
        - 较低的并发数
        - 较长的延迟
        """
        from crawlo.utils.queue_helper import QueueHelper
        
        config = QueueHelper.use_redis_queue(
            queue_name="crawlo:conservative",
            max_retries=3,
            timeout=300
        )
        
        config.update({
            # 并发控制
            'CONCURRENCY': concurrency,
            'SCHEDULER_MAX_QUEUE_SIZE': concurrency * 10,
            'MAX_RUNNING_SPIDERS': 1,
            
            # 请求控制
            'DOWNLOAD_DELAY': 0.2,
            'RANDOMNESS': True,
            'RANDOM_RANGE': (0.8, 1.5),
            
            # 内存控制
            'DOWNLOAD_MAXSIZE': 5 * 1024 * 1024,  # 5MB
            'CONNECTION_POOL_LIMIT': concurrency * 2,
            
            # 重试策略
            'MAX_RETRY_TIMES': 2,
            
            # 使用增强引擎
            'ENGINE_CLASS': 'crawlo.core.engine.Engine'
        })
        
        return config
    
    @staticmethod
    def balanced_config(concurrency: int = 16) -> Dict[str, Any]:
        """
        平衡配置 - 适用于一般生产环境
        
        特点：
        - 中等的队列容量
        - 平衡的并发数
        - 适中的延迟
        """
        from crawlo.utils.queue_helper import QueueHelper
        
        config = QueueHelper.use_redis_queue(
            queue_name="crawlo:balanced",
            max_retries=5,
            timeout=600
        )
        
        config.update({
            # 并发控制
            'CONCURRENCY': concurrency,
            'SCHEDULER_MAX_QUEUE_SIZE': concurrency * 15,
            'MAX_RUNNING_SPIDERS': 2,
            
            # 请求控制
            'DOWNLOAD_DELAY': 0.1,
            'RANDOMNESS': True,
            'RANDOM_RANGE': (0.5, 1.2),
            
            # 内存控制
            'DOWNLOAD_MAXSIZE': 10 * 1024 * 1024,  # 10MB
            'CONNECTION_POOL_LIMIT': concurrency * 3,
            
            # 重试策略
            'MAX_RETRY_TIMES': 3,
            
            # 使用增强引擎
            'ENGINE_CLASS': 'crawlo.core.engine.Engine'
        })
        
        return config
    
    @staticmethod
    def aggressive_config(concurrency: int = 32) -> Dict[str, Any]:
        """
        激进配置 - 适用于高性能环境
        
        特点：
        - 大的队列容量
        - 高并发数
        - 较短的延迟
        """
        from crawlo.utils.queue_helper import QueueHelper
        
        config = QueueHelper.use_redis_queue(
            queue_name="crawlo:aggressive",
            max_retries=10,
            timeout=900
        )
        
        config.update({
            # 并发控制
            'CONCURRENCY': concurrency,
            'SCHEDULER_MAX_QUEUE_SIZE': concurrency * 20,
            'MAX_RUNNING_SPIDERS': 3,
            
            # 请求控制
            'DOWNLOAD_DELAY': 0.05,
            'RANDOMNESS': True,
            'RANDOM_RANGE': (0.3, 1.0),
            
            # 内存控制
            'DOWNLOAD_MAXSIZE': 20 * 1024 * 1024,  # 20MB
            'CONNECTION_POOL_LIMIT': concurrency * 4,
            
            # 重试策略
            'MAX_RETRY_TIMES': 5,
            
            # 使用增强引擎
            'ENGINE_CLASS': 'crawlo.core.engine.Engine'
        })
        
        return config
    
    @staticmethod
    def memory_optimized_config(concurrency: int = 12) -> Dict[str, Any]:
        """
        内存优化配置 - 适用于大规模但内存受限的场景
        
        特点：
        - 小队列，快速流转
        - 严格的内存控制
        - 使用Redis减少内存压力
        """
        from crawlo.utils.queue_helper import QueueHelper
        
        config = QueueHelper.use_redis_queue(
            queue_name="crawlo:memory_optimized",
            max_retries=3,
            timeout=300
        )
        
        config.update({
            # 并发控制
            'CONCURRENCY': concurrency,
            'SCHEDULER_MAX_QUEUE_SIZE': concurrency * 5,
            'MAX_RUNNING_SPIDERS': 1,
            
            # 请求控制
            'DOWNLOAD_DELAY': 0.1,
            'RANDOMNESS': False,
            
            # 严格的内存控制
            'DOWNLOAD_MAXSIZE': 2 * 1024 * 1024,  # 2MB
            'DOWNLOAD_WARN_SIZE': 512 * 1024,     # 512KB
            'CONNECTION_POOL_LIMIT': concurrency,
            
            # 重试策略
            'MAX_RETRY_TIMES': 2,
            
            # 使用增强引擎
            'ENGINE_CLASS': 'crawlo.core.engine.Engine'
        })
        
        return config


def apply_large_scale_config(
    settings_dict: Dict[str, Any], 
    config_type: str = "balanced", 
    concurrency: Optional[int] = None
):
    """
    应用大规模配置
    
    Args:
        settings_dict: 设置字典
        config_type: 配置类型 ("conservative", "balanced", "aggressive", "memory_optimized")
        concurrency: 并发数（可选，不指定则使用默认值）
    """
    config_map = {
        "conservative": LargeScaleConfig.conservative_config,
        "balanced": LargeScaleConfig.balanced_config,
        "aggressive": LargeScaleConfig.aggressive_config,
        "memory_optimized": LargeScaleConfig.memory_optimized_config
    }
    
    if config_type not in config_map:
        raise ValueError(f"不支持的配置类型: {config_type}")
    
    if concurrency:
        config = config_map[config_type](concurrency)
    else:
        config = config_map[config_type]()
    
    settings_dict.update(config)
    
    return config


# 导出所有公共API
__all__ = [
    'ConfigUtils',
    'EnvConfigManager',
    'LargeScaleConfig',
    'apply_large_scale_config',
]

```

**code file end: crawlo/utils/config_manager.py**

---


### code file start: crawlo/utils/controlled_spider_mixin.py 

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
受控爬虫混入类
解决 start_requests() yield 上万个请求时的并发控制问题
"""
import asyncio
import time
from collections import deque
from typing import Generator, Optional

from crawlo import Request
from crawlo.logging import get_logger


class ControlledRequestMixin:
    """
    受控请求生成混入类
    
    解决问题：
    1. start_requests() 同时yield上万个请求导致内存爆炸
    2. 不遵守CONCURRENCY设置，无限制创建请求
    3. 队列积压过多请求影响性能
    
    解决方案：
    1. 按需生成请求，根据实际并发能力控制
    2. 动态监控队列状态，智能调节生成速度
    3. 支持背压控制，避免队列积压
    """
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        
        # 受控生成配置
        self.max_pending_requests = 100     # 最大待处理请求数
        self.batch_size = 50               # 每批生成请求数
        self.generation_interval = 0.1      # 生成间隔（秒）
        self.backpressure_threshold = 200   # 背压阈值
        
        # 内部状态
        self._original_start_requests = None
        self._pending_count = 0
        self._total_generated = 0
        self._generation_paused = False
        
        # 性能监控
        self._last_generation_time = 0
        self._generation_stats = {
            'generated': 0,
            'skipped': 0,
            'backpressure_events': 0
        }
    
    def start_requests(self) -> Generator[Request, None, None]:
        """
        受控的 start_requests 实现
        
        注意：这个方法会替换原始的 start_requests，
        原始请求将通过 _original_start_requests() 提供
        """
        # 保存原始的请求生成器
        if hasattr(self, '_original_start_requests') and self._original_start_requests:
            original_generator = self._original_start_requests()
        else:
            # 如果子类没有定义 _original_start_requests，尝试调用原始方法
            original_generator = self._get_original_requests()
        
        # 使用受控生成器包装原始生成器
        yield from self._controlled_request_generator(original_generator)
    
    def _original_start_requests(self) -> Generator[Request, None, None]:
        """
        子类应该实现这个方法，提供原始的请求生成逻辑
        
        示例：
        def _original_start_requests(self):
            for i in range(50000):  # 5万个请求
                yield Request(url=f"https://example.com/page/{i}")
        """
        raise NotImplementedError(
            "子类必须实现 _original_start_requests() 方法，"
            "或者确保原始的 start_requests() 方法存在"
        )
    
    def _get_original_requests(self) -> Generator[Request, None, None]:
        """尝试获取原始请求（向后兼容）"""
        # 这里可以尝试调用父类的 start_requests 或其他方式
        # 具体实现取决于你的需求
        return iter([])  # 默认返回空生成器
    
    def _controlled_request_generator(self, original_generator) -> Generator[Request, None, None]:
        """Controlled request generator"""
        self.logger.info(f"Starting controlled request generator (max pending: {self.max_pending_requests})")
        
        request_buffer = deque()
        batch_count = 0
        
        try:
            # 分批处理原始请求
            for request in original_generator:
                request_buffer.append(request)
                
                # 当缓冲区达到批次大小时，进行控制检查
                if len(request_buffer) >= self.batch_size:
                    yield from self._yield_controlled_batch(request_buffer)
                    batch_count += 1
                    
                    # 每批次后检查是否需要暂停
                    if self._should_pause_generation():
                        self._wait_for_capacity()
            
            # 处理剩余的请求
            if request_buffer:
                yield from self._yield_controlled_batch(request_buffer)
        
        except Exception as e:
            self.logger.error(f"Controlled request generation failed: {e}")
            raise
        
        self.logger.info(
            f"Controlled request generation completed!"
            f"总计: {self._generation_stats['generated']}, "
            f"跳过: {self._generation_stats['skipped']}, "
            f"背压事件: {self._generation_stats['backpressure_events']}"
        )
    
    def _yield_controlled_batch(self, request_buffer: deque) -> Generator[Request, None, None]:
        """分批受控 yield 请求"""
        while request_buffer:
            # 检查当前系统负载
            if self._should_pause_generation():
                self.logger.debug("检测到系统负载过高，暂停生成")
                self._generation_stats['backpressure_events'] += 1
                self._wait_for_capacity()
            
            # yield 一个请求
            request = request_buffer.popleft()
            
            # 可以在这里添加额外的请求处理逻辑
            processed_request = self._process_request_before_yield(request)
            if processed_request:
                self._total_generated += 1
                self._generation_stats['generated'] += 1
                self._last_generation_time = time.time()
                yield processed_request
            else:
                self._generation_stats['skipped'] += 1
            
            # 控制生成速度
            if self.generation_interval > 0:
                time.sleep(self.generation_interval)
    
    def _should_pause_generation(self) -> bool:
        """判断是否应该暂停请求生成"""
        # 检查队列大小（如果可以访问scheduler的话）
        if hasattr(self, 'crawler') and self.crawler:
            engine = getattr(self.crawler, 'engine', None)
            if engine and engine.scheduler:
                queue_size = len(engine.scheduler)
                if queue_size > self.backpressure_threshold:
                    return True
        
        # 检查任务管理器负载
        if hasattr(self, 'crawler') and self.crawler:
            engine = getattr(self.crawler, 'engine', None)
            if engine and engine.task_manager:
                current_tasks = len(engine.task_manager.current_task)
                concurrency = getattr(engine.task_manager, 'semaphore', None)
                if concurrency and hasattr(concurrency, '_initial_value'):
                    max_concurrency = concurrency._initial_value
                    # 如果当前任务数接近最大并发数，暂停生成
                    if current_tasks >= max_concurrency * 0.8:  # 80% 阈值
                        return True
        
        return False
    
    def _wait_for_capacity(self):
        """Wait for system to have sufficient capacity"""
        wait_time = 0.1
        max_wait = 5.0
        
        while self._should_pause_generation() and wait_time < max_wait:
            time.sleep(wait_time)
            wait_time = min(wait_time * 1.2, max_wait)  # 指数退避
    
    def _process_request_before_yield(self, request: Request) -> Optional[Request]:
        """
        在 yield 请求前进行处理
        子类可以重写这个方法来添加自定义逻辑
        
        返回 None 表示跳过这个请求
        """
        return request
    
    def get_generation_stats(self) -> dict:
        """获取生成统计信息"""
        return {
            **self._generation_stats,
            'total_generated': self._total_generated,
            'last_generation_time': self._last_generation_time
        }


class AsyncControlledRequestMixin:
    """
    异步版本的受控请求混入类
    
    使用asyncio来实现更精确的并发控制
    """
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        
        # 异步控制配置
        self.max_concurrent_generations = 10   # 最大同时生成数
        self.generation_semaphore = None
        self.queue_monitor_interval = 1.0       # 队列监控间隔
        
        # 异步状态
        self._generation_tasks = set()
        self._monitoring_task = None
        self._stop_generation = False
    
    def _original_start_requests(self) -> Generator[Request, None, None]:
        """
        子类应该实现这个方法，提供原始的请求生成逻辑
        
        示例：
        def _original_start_requests(self):
            for i in range(50000):  # 5万个请求
                yield Request(url=f"https://example.com/page/{i}")
        """
        raise NotImplementedError(
            "子类必须实现 _original_start_requests() 方法，"
            "或者确保原始的 start_requests() 方法存在"
        )
    
    def _get_original_requests(self) -> Generator[Request, None, None]:
        """尝试获取原始请求（向后兼容）"""
        # 这里可以尝试调用父类的 start_requests 或其他方式
        # 具体实现取决于你的需求
        return iter([])  # 默认返回空生成器
    
    def _should_pause_generation(self) -> bool:
        """判断是否应该暂停请求生成"""
        # 检查队列大小（如果可以访问scheduler的话）
        if hasattr(self, 'crawler') and self.crawler:
            engine = getattr(self.crawler, 'engine', None)
            if engine and engine.scheduler:
                queue_size = len(engine.scheduler)
                if queue_size > 200:  # 背压阈值
                    return True
        
        # 检查任务管理器负载
        if hasattr(self, 'crawler') and self.crawler:
            engine = getattr(self.crawler, 'engine', None)
            if engine and engine.task_manager:
                current_tasks = len(engine.task_manager.current_task)
                concurrency = getattr(engine.task_manager, 'semaphore', None)
                if concurrency and hasattr(concurrency, '_initial_value'):
                    max_concurrency = concurrency._initial_value
                    # 如果当前任务数接近最大并发数，暂停生成
                    if current_tasks >= max_concurrency * 0.8:  # 80% 阈值
                        return True
        
        return False
    
    def _process_request_before_yield(self, request: Request) -> Optional[Request]:
        """
        在 yield 请求前进行处理
        子类可以重写这个方法来添加自定义逻辑
        
        返回 None 表示跳过这个请求
        """
        return request
    
    async def start_requests_async(self) -> Generator[Request, None, None]:
        """异步版本的受控请求生成"""
        # 初始化信号量
        self.generation_semaphore = asyncio.Semaphore(self.max_concurrent_generations)
        
        # 启动队列监控
        self._monitoring_task = asyncio.create_task(self._monitor_queue_load())
        
        try:
            # 获取原始请求
            original_requests = self._original_start_requests()
            
            # 分批异步处理
            batch = []
            async for request in self._async_request_wrapper(original_requests):
                batch.append(request)
                
                if len(batch) >= 50:  # 批次大小
                    async for request in self._process_async_batch(batch):
                        yield request
                    batch = []
            
            # 处理剩余请求
            if batch:
                async for request in self._process_async_batch(batch):
                    yield request
        
        finally:
            # 清理
            self._stop_generation = True
            if self._monitoring_task:
                self._monitoring_task.cancel()
            
            # 等待所有生成任务完成
            if self._generation_tasks:
                await asyncio.gather(*self._generation_tasks, return_exceptions=True)
    
    async def _async_request_wrapper(self, sync_generator):
        """将同步生成器包装为异步"""
        for request in sync_generator:
            yield request
            await asyncio.sleep(0)  # 让出控制权
    
    async def _process_async_batch(self, batch):
        """异步处理批次请求"""
        async def process_single_request(request):
            async with self.generation_semaphore:
                # 等待合适的时机
                while self._should_pause_generation() and not self._stop_generation:
                    await asyncio.sleep(0.1)
                
                if not self._stop_generation:
                    return self._process_request_before_yield(request)
                return None
        
        # 并发处理批次中的请求
        tasks = [process_single_request(req) for req in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # yield 处理完的请求
        for result in results:
            if result and not isinstance(result, Exception):
                yield result
    
    async def _monitor_queue_load(self):
        """监控队列负载"""
        while not self._stop_generation:
            try:
                # 这里可以添加队列负载监控逻辑
                await asyncio.sleep(self.queue_monitor_interval)
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.warning(f"队列监控异常: {e}")
                await asyncio.sleep(1.0)


# 使用示例和文档
USAGE_EXAMPLE = '''
# 同步版本使用示例：

class MyControlledSpider(Spider, ControlledRequestMixin):
    name = 'controlled_spider'
    
    def __init__(self):
        Spider.__init__(self)
        ControlledRequestMixin.__init__(self)
        
        # 配置受控生成参数
        self.max_pending_requests = 200
        self.batch_size = 100
        self.generation_interval = 0.05
    
    def _original_start_requests(self):
        """提供原始的大量请求"""
        for i in range(50000):  # 5万个请求
            yield Request(url=f"https://example.com/page/{i}")
    
    def _process_request_before_yield(self, request):
        """可选：在yield前处理请求"""
        # 可以添加去重、优先级设置等逻辑
        return request
    
    async def parse(self, response):
        # 解析逻辑
        yield {"url": response.url}

# 异步版本使用示例：

class MyAsyncControlledSpider(Spider, AsyncControlledRequestMixin):
    name = 'async_controlled_spider'
    
    def __init__(self):
        Spider.__init__(self)
        AsyncControlledRequestMixin.__init__(self)
        
        # 配置异步控制参数
        self.max_concurrent_generations = 15
        self.queue_monitor_interval = 0.5
    
    def _original_start_requests(self):
        """提供原始的大量请求"""
        categories = ['tech', 'finance', 'sports']
        for category in categories:
            for page in range(1, 10000):  # 每个分类1万页
                yield Request(
                    url=f"https://news-site.com/{category}?page={page}",
                    meta={'category': category}
                )
    
    def _process_request_before_yield(self, request):
        """异步版本的请求预处理"""
        # 根据分类设置优先级
        category = request.meta.get('category', '')
        if category == 'tech':
            request.priority = 10
        return request
    
    async def parse(self, response):
        # 异步解析逻辑
        yield {
            "url": response.url,
            "category": response.meta['category']
        }

# 使用时：
from crawlo.crawler import CrawlerProcess
from crawlo.config import CrawloConfig

# 同步版本
config = CrawloConfig.standalone(concurrency=16)
process = CrawlerProcess(config)
process.crawl(MyControlledSpider)
process.start()

# 异步版本
async_config = CrawloConfig.standalone(
    concurrency=30,
    downloader='httpx'  # 推荐使用支持异步的下载器
)
async_process = CrawlerProcess(async_config)
async_process.crawl(MyAsyncControlledSpider)
async_process.start()
'''
```

**code file end: crawlo/utils/controlled_spider_mixin.py**

---


### code file start: crawlo/utils/db_helper.py 

```python
# -*- coding: utf-8 -*-
import json
import re
from typing import Any, Union, List, Dict, Tuple, Optional
from datetime import date, time, datetime
from enum import Enum

from crawlo.logging import get_logger

logger = get_logger(__name__)


class SQLStatementType(Enum):
    """SQL语句类型枚举"""
    INSERT = "INSERT"
    REPLACE = "REPLACE"
    UPDATE = "UPDATE"
    BATCH_INSERT = "BATCH_INSERT"
    BATCH_REPLACE = "BATCH_REPLACE"


class SQLBuilder:
    """SQL语句构建器"""
    
    @staticmethod
    def format_value(value: Any) -> Union[str, int, float, None]:
        """
        格式化 SQL 字段值，防止注入并兼容类型。

        Args:
            value (Any): 待处理的值

        Returns:
            str | int | float | None: 格式化后的值，None 表示 SQL 的 NULL
        """
        if value is None:
            return None

        if isinstance(value, str):
            return value.strip()

        elif isinstance(value, (list, tuple, dict)):
            try:
                return json.dumps(value, ensure_ascii=False, default=str)
            except Exception as e:
                raise ValueError(f"Failed to serialize container to JSON: {value}, error: {e}")

        elif isinstance(value, bool):
            return int(value)

        elif isinstance(value, (int, float)):
            return value

        elif isinstance(value, (date, time, datetime)):
            return str(value)

        else:
            raise TypeError(f"Unsupported value type: {type(value)}, value: {value}")

    @staticmethod
    def list_to_tuple_str(datas: List[Any]) -> str:
        """
        将列表转为 SQL 元组字符串格式。

        Args:
            datas (list): 输入列表

        Returns:
            str: 对应的元组字符串表示
        """
        if not datas:
            return "()"
        if len(datas) == 1:
            # 处理单元素元组，确保末尾有逗号
            return f"({datas[0]},)"
        return str(tuple(datas))

    @staticmethod
    def _build_key_value_pairs(data: Dict[str, Any]) -> Tuple[List[str], List[Any]]:
        """
        构建键值对列表

        Args:
            data (dict): 数据字典

        Returns:
            tuple: (键列表, 值列表)
        """
        keys = [f"`{key}`" for key in data.keys()]
        values = [SQLBuilder.format_value(value) for value in data.values()]
        return keys, values

    @staticmethod
    def _build_update_clause(update_columns: Union[Tuple, List]) -> str:
        """
        构建更新子句，使用新的 MySQL 语法避免 VALUES() 函数弃用警告

        Args:
            update_columns (tuple or list): 更新列名

        Returns:
            str: 更新子句
        """
        if not isinstance(update_columns, (tuple, list)):
            update_columns = (update_columns,)
        # 使用新的语法：INSERT ... VALUES (...) AS alias ... UPDATE ... alias.col
        # 确保使用 excluded 别名而不是 VALUES() 函数
        return ", ".join(f"`{key}`=`excluded`.`{key}`" for key in update_columns)

    @staticmethod
    def make_insert(
        table: str,
        data: Dict[str, Any],
        auto_update: bool = False,
        update_columns: Tuple = (),
        insert_ignore: bool = False,
    ) -> str:
        """
        生成 MySQL INSERT 或 REPLACE 语句。

        Args:
            table (str): 表名
            data (dict): 表数据，JSON 格式字典
            auto_update (bool): 是否使用 REPLACE INTO（完全覆盖已存在记录）
            update_columns (tuple or list): 冲突时需更新的列名；指定后 auto_update 失效
            insert_ignore (bool): 是否使用 INSERT IGNORE，忽略重复数据

        Returns:
            str: 生成的 SQL 语句
        """
        keys, values = SQLBuilder._build_key_value_pairs(data)
        keys_str = SQLBuilder.list_to_tuple_str(keys).replace("'", "")
        values_str = SQLBuilder.list_to_tuple_str(values)

        if update_columns:
            update_clause = SQLBuilder._build_update_clause(update_columns)
            ignore_flag = " IGNORE" if insert_ignore else ""
            # 使用新的语法避免 VALUES() 函数弃用警告
            sql = f"INSERT{ignore_flag} INTO `{table}` {keys_str} VALUES {values_str} AS `excluded` ON DUPLICATE KEY UPDATE {update_clause}"

        elif auto_update:
            sql = f"REPLACE INTO `{table}` {keys_str} VALUES {values_str}"

        else:
            ignore_flag = " IGNORE" if insert_ignore else ""
            sql = f"INSERT{ignore_flag} INTO `{table}` {keys_str} VALUES {values_str}"

        return sql.replace("None", "null")

    @staticmethod
    def make_update(
        table: str,
        data: Dict[str, Any],
        condition: str,
    ) -> str:
        """
        生成 MySQL UPDATE 语句。

        Args:
            table (str): 表名
            data (dict): 更新字段的键值对，键为列名，值为新值
            condition (str): WHERE 条件，如 "id = 1"

        Returns:
            str: 生成的 SQL 语句
        """
        key_values: List[str] = []
        for key, value in data.items():
            formatted_value = SQLBuilder.format_value(value)
            if isinstance(formatted_value, str):
                key_values.append(f"`{key}`={repr(formatted_value)}")
            elif formatted_value is None:
                key_values.append(f"`{key}`=null")
            else:
                key_values.append(f"`{key}`={formatted_value}")

        key_values_str = ", ".join(key_values)
        sql = f"UPDATE `{table}` SET {key_values_str} WHERE {condition}"
        return sql

    @staticmethod
    def make_batch(
        table: str,
        datas: List[Dict[str, Any]],
        auto_update: bool = False,
        update_columns: Tuple = (),
        update_columns_value: Tuple = (),
    ) -> Optional[Tuple[str, List[List[Any]]]]:
        """
        生成批量插入 SQL 及对应值列表。

        Args:
            table (str): 表名
            datas (list of dict): 数据列表
            auto_update (bool): 使用 REPLACE INTO 替代 INSERT
            update_columns (tuple or list): 主键冲突时要更新的列名
            update_columns_value (tuple): 更新列对应的固定值

        Returns:
            tuple[str, list[list]] | None: (SQL语句, 值列表)；若数据为空则返回 None
        """
        if not datas:
            return None

        # 提取所有唯一字段名
        keys = list({key for data in datas for key in data})
        values_list = []

        for data in datas:
            if not isinstance(data, dict):
                continue  # 跳过非字典数据

            row = []
            for key in keys:
                raw_value = data.get(key)
                try:
                    formatted_value = SQLBuilder.format_value(raw_value)
                    row.append(formatted_value)
                except Exception as e:
                    logger.error(f"{key}: {raw_value} (类型: {type(raw_value)}) -> {e}")
            values_list.append(row)

        keys_str = ", ".join(f"`{key}`" for key in keys)
        placeholders_str = ", ".join(["%s"] * len(keys))

        if update_columns:
            if not isinstance(update_columns, (tuple, list)):
                update_columns = (update_columns,)

            if update_columns_value:
                # 当提供了固定值时，使用这些值进行更新
                update_pairs = [
                    f"`{key}`={value}"
                    for key, value in zip(update_columns, update_columns_value)
                ]
            else:
                # 使用新的语法避免 VALUES() 函数弃用警告
                # INSERT ... VALUES (...) AS excluded ... ON DUPLICATE KEY UPDATE col=excluded.col
                update_pairs = [
                    f"`{key}`=`excluded`.`{key}`" for key in update_columns
                ]
            update_clause = ", ".join(update_pairs)
            sql = f"INSERT INTO `{table}` ({keys_str}) VALUES ({placeholders_str}) AS `excluded` ON DUPLICATE KEY UPDATE {update_clause}"

        elif auto_update:
            sql = f"REPLACE INTO `{table}` ({keys_str}) VALUES ({placeholders_str})"

        else:
            sql = f"INSERT IGNORE INTO `{table}` ({keys_str}) VALUES ({placeholders_str})"

        return sql, values_list
```

**code file end: crawlo/utils/db_helper.py**

---


### code file start: crawlo/utils/error_handler.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
错误处理工具
提供详细、一致的错误处理和日志记录机制
"""
import traceback
from functools import wraps
from datetime import datetime
from typing import Optional, Callable, Any, Dict, List

from crawlo.logging import get_logger


class ErrorContext:
    """错误上下文信息"""
    
    def __init__(self, context: str = "", module: str = "", function: str = ""):
        self.context = context
        self.module = module
        self.function = function
        self.timestamp = datetime.now()
        
    def __str__(self):
        parts = []
        if self.module:
            parts.append(f"Module: {self.module}")
        if self.function:
            parts.append(f"Function: {self.function}")
        if self.context:
            parts.append(f"Context: {self.context}")
        parts.append(f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        return " | ".join(parts)


class DetailedException(Exception):
    """带有详细信息的异常基类"""
    
    def __init__(self, message: str, context: Optional[ErrorContext] = None, 
                 error_code: Optional[str] = None, **kwargs):
        super().__init__(message)
        self.context = context
        self.error_code = error_code
        self.details = kwargs
        self.timestamp = datetime.now()
        
    def __str__(self):
        base_msg = super().__str__()
        if self.context:
            return f"{base_msg} ({self.context})"
        return base_msg
    
    def get_full_details(self) -> Dict:
        """获取完整的错误详情"""
        return {
            "message": str(self),
            "error_code": self.error_code,
            "context": str(self.context) if self.context else None,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
            "exception_type": self.__class__.__name__
        }


class EnhancedErrorHandler:
    """增强版错误处理器"""
    
    def __init__(self, logger_name: str = __name__, log_level: str = 'ERROR'):
        self.logger = get_logger(logger_name)
        self.error_history: List[Dict] = []  # 错误历史记录
        self.max_history_size = 100  # 最大历史记录数
    
    def handle_error(self, exception: Exception, context: Optional[ErrorContext] = None, 
                     raise_error: bool = True, log_error: bool = True,
                     extra_info: Optional[Dict] = None) -> Dict:
        """
        增强版错误处理
        
        Args:
            exception: 异常对象
            context: 错误上下文信息
            raise_error: 是否重新抛出异常
            log_error: 是否记录错误日志
            extra_info: 额外的错误信息
            
        Returns:
            包含错误详情的字典
        """
        # 构建错误详情
        error_details = {
            "exception": exception,
            "exception_type": type(exception).__name__,
            "message": str(exception),
            "context": str(context) if context else None,
            "timestamp": datetime.now().isoformat(),
            "traceback": traceback.format_exc() if log_error else None,
            "extra_info": extra_info or {}
        }
        
        # 记录到历史
        self._record_error(error_details)
        
        # 记录日志
        if log_error:
            self._log_error(error_details)
        
        # 重新抛出异常
        if raise_error:
            raise exception
        
        return error_details
    
    def _log_error(self, error_details: Dict):
        """记录错误日志"""
        # 基本错误信息
        context_info = error_details.get("context", "")
        message = error_details["message"]
        error_msg = f"{message} [{context_info}]" if context_info else message
        
        # 记录错误
        self.logger.error(error_msg)
        
        # 记录详细信息
        if error_details.get("traceback"):
            self.logger.debug(f"详细错误信息:\n{error_details['traceback']}")
        
        # 记录额外信息
        if error_details.get("extra_info"):
            self.logger.debug(f"额外信息: {error_details['extra_info']}")
    
    def _record_error(self, error_details: Dict):
        """记录错误到历史"""
        self.error_history.append(error_details)
        # 限制历史记录大小
        if len(self.error_history) > self.max_history_size:
            self.error_history.pop(0)
    
    def safe_call(self, func: Callable, *args, default_return=None, 
                  context: Optional[ErrorContext] = None, **kwargs) -> Any:
        """
        安全调用函数，捕获并处理异常
        
        Args:
            func: 要调用的函数
            *args: 函数参数
            default_return: 默认返回值
            context: 错误上下文
            **kwargs: 函数关键字参数
            
        Returns:
            函数返回值或默认值
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self.handle_error(e, context=context, raise_error=False)
            return default_return
    
    def retry_on_failure(self, max_retries: int = 3, delay: float = 1.0, 
                         exceptions: tuple = (Exception,), backoff_factor: float = 1.0,
                         context: Optional[ErrorContext] = None):
        """
        装饰器：失败时重试（增强版）
        
        Args:
            max_retries: 最大重试次数
            delay: 初始重试间隔（秒）
            exceptions: 需要重试的异常类型
            backoff_factor: 退避因子（每次重试间隔乘以此因子）
            context: 错误上下文
        """
        def decorator(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                last_exception = None
                current_delay = delay
                
                for attempt in range(max_retries + 1):
                    try:
                        return await func(*args, **kwargs)
                    except exceptions as e:
                        last_exception = e
                        if attempt < max_retries:
                            # 记录重试信息
                            retry_context = ErrorContext(
                                context=f"函数 {func.__name__} 执行失败 (尝试 {attempt + 1}/{max_retries + 1})",
                                module=context.module if context else "",
                                function=func.__name__
                            ) if context else None
                            
                            self.logger.warning(
                                f"函数 {func.__name__} 执行失败 (尝试 {attempt + 1}/{max_retries + 1}): {e}"
                            )
                            
                            import asyncio
                            await asyncio.sleep(current_delay)
                            current_delay *= backoff_factor  # 指数退避
                        else:
                            # 最后一次尝试失败
                            final_context = ErrorContext(
                                context=f"函数 {func.__name__} 执行失败，已达到最大重试次数",
                                module=context.module if context else "",
                                function=func.__name__
                            ) if context else None
                            
                            self.logger.error(
                                f"函数 {func.__name__} 执行失败，已达到最大重试次数: {e}"
                            )
                raise last_exception
            
            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                last_exception = None
                current_delay = delay
                
                for attempt in range(max_retries + 1):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as e:
                        last_exception = e
                        if attempt < max_retries:
                            # 记录重试信息
                            retry_context = ErrorContext(
                                context=f"函数 {func.__name__} 执行失败 (尝试 {attempt + 1}/{max_retries + 1})",
                                module=context.module if context else "",
                                function=func.__name__
                            ) if context else None
            
                            self.logger.warning(
                                f"函数 {func.__name__} 执行失败 (尝试 {attempt + 1}/{max_retries + 1}): {e}"
                            )
                            
                            import time
                            time.sleep(current_delay)
                            current_delay *= backoff_factor  # 指数退避
                        else:
                            # 最后一次尝试失败
                            final_context = ErrorContext(
                                context=f"函数 {func.__name__} 执行失败，已达到最大重试次数",
                                module=context.module if context else "",
                                function=func.__name__
                            ) if context else None
                            
                            self.logger.error(
                                f"函数 {func.__name__} 执行失败，已达到最大重试次数: {e}"
                            )
                raise last_exception
            
            # 根据函数是否为异步函数返回相应的包装器
            import inspect
            if inspect.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper
        
        return decorator
    
    def get_error_history(self) -> List[Dict]:
        """获取错误历史记录"""
        return self.error_history.copy()
    
    def clear_error_history(self):
        """清空错误历史记录"""
        self.error_history.clear()


# 为了向后兼容，提供与旧版error_handler.py相同的接口

# 别名，保持与旧版接口一致
ErrorHandler = EnhancedErrorHandler

# 全局增强错误处理器实例
enhanced_error_handler = EnhancedErrorHandler()

# 为了向后兼容，提供默认错误处理器实例
default_error_handler = enhanced_error_handler

def handle_exception(context: str = "", module: str = "", function: str = "",
                     raise_error: bool = True, log_error: bool = True,
                     error_code: Optional[str] = None):
    """
    装饰器：处理函数异常（增强版）
    
    Args:
        context: 错误上下文描述
        module: 模块名称
        function: 函数名称
        raise_error: 是否重新抛出异常
        log_error: 是否记录错误日志
        error_code: 错误代码
    """
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                error_context = ErrorContext(
                    context=f"{context} - {func.__name__}",
                    module=module,
                    function=func.__name__
                )
                
                # 如果是详细异常，保留原有信息
                if isinstance(e, DetailedException):
                    # 确保上下文信息完整
                    if not e.context:
                        e.context = error_context
                    enhanced_error_handler.handle_error(
                        e, context=e.context,
                        raise_error=raise_error, log_error=log_error
                    )
                else:
                    # 包装为详细异常
                    detailed_e = DetailedException(
                        str(e), context=error_context, error_code=error_code
                    )
                    enhanced_error_handler.handle_error(
                        detailed_e, context=error_context,
                        raise_error=raise_error, log_error=log_error
                    )
                if not raise_error:
                    return None
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_context = ErrorContext(
                    context=f"{context} - {func.__name__}",
                    module=module,
                    function=func.__name__
                )
                
                # 如果是详细异常，保留原有信息
                if isinstance(e, DetailedException):
                    # 确保上下文信息完整
                    if not e.context:
                        e.context = error_context
                    enhanced_error_handler.handle_error(
                        e, context=e.context,
                        raise_error=raise_error, log_error=log_error
                    )
                else:
                    # 包装为详细异常
                    detailed_e = DetailedException(
                        str(e), context=error_context, error_code=error_code
                    )
                    enhanced_error_handler.handle_error(
                        detailed_e, context=error_context,
                        raise_error=raise_error, log_error=log_error
                    )
                if not raise_error:
                    return None
        
        # 根据函数是否为异步函数返回相应的包装器
        import inspect
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator

# 为了完全向后兼容，也提供旧版的handle_exception接口
# 这个版本与error_handler.py中的接口完全一致
def handle_exception_simple(context: str = "", raise_error: bool = True, log_error: bool = True):
    """
    装饰器：处理函数异常（简化版，与旧版接口兼容）
    
    Args:
        context: 错误上下文描述
        raise_error: 是否重新抛出异常
        log_error: 是否记录错误日志
    """
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                error_context = ErrorContext(context=f"{context} - {func.__name__}")
                enhanced_error_handler.handle_error(
                    e, context=error_context,
                    raise_error=raise_error, log_error=log_error
                )
                if not raise_error:
                    return None

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_context = ErrorContext(context=f"{context} - {func.__name__}")
                enhanced_error_handler.handle_error(
                    e, context=error_context,
                    raise_error=raise_error, log_error=log_error
                )
                if not raise_error:
                    return None

        # 根据函数是否为异步函数返回相应的包装器
        import inspect
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator
```

**code file end: crawlo/utils/error_handler.py**

---


### code file start: crawlo/utils/fingerprint.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
统一指纹生成工具
================
提供一致的指纹生成方法，确保在框架各组件中生成的指纹保持一致。

特点:
- 算法统一: 所有指纹生成使用相同的算法(SHA256)
- 格式一致: 相同数据在不同场景下生成相同指纹
- 高性能: 优化的实现确保高效生成
- 易扩展: 支持不同类型数据的指纹生成
"""

import hashlib
from typing import Any, Dict
from w3lib.url import canonicalize_url


def generate_data_fingerprint(data: Any) -> str:
    """
    生成数据指纹
    
    基于数据内容生成唯一指纹，用于去重判断。
    使用 SHA256 算法确保安全性。
    
    :param data: 要生成指纹的数据（支持 dict, Item, namedtuple, str 等类型）
    :return: 数据指纹（hex string）
    """
    # 将数据转换为可序列化的字典
    if hasattr(data, 'to_dict'):
        # 支持 Item 等实现了 to_dict 方法的对象
        data_dict = data.to_dict()
    elif hasattr(data, '_asdict'):
        # 支持 namedtuple 对象
        data_dict = data._asdict()
    elif isinstance(data, dict):
        data_dict = data
    else:
        # 其他类型转换为字符串处理
        data_dict = {'__data__': str(data)}
    
    # 对字典进行排序以确保一致性
    sorted_items = sorted(data_dict.items())
    
    # 生成指纹字符串
    fingerprint_string = '|'.join([f"{k}={v}" for k, v in sorted_items if v is not None])
    
    # 使用 SHA256 生成固定长度的指纹
    return hashlib.sha256(fingerprint_string.encode('utf-8')).hexdigest()


def generate_request_fingerprint(
        method: str,
        url: str,
        body: bytes = b'',
        headers: Dict[str, str] = None
) -> str:
    """
    生成请求指纹
    
    基于请求的方法、URL、body 和可选的 headers 生成唯一指纹。
    使用 SHA256 算法确保安全性。
    
    :param method: HTTP方法
    :param url: 请求URL
    :param body: 请求体
    :param headers: 请求头
    :return: 请求指纹（hex string）
    """
    hash_func = hashlib.sha256()
    
    # 基本字段
    hash_func.update(method.encode('utf-8'))
    hash_func.update(canonicalize_url(url).encode('utf-8'))
    hash_func.update(body or b'')
    
    # 可选的 headers
    if headers:
        # 对 headers 进行排序以确保一致性
        sorted_headers = sorted(headers.items())
        for name, value in sorted_headers:
            hash_func.update(f"{name}:{value}".encode('utf-8'))
    
    return hash_func.hexdigest()


class FingerprintGenerator:
    """指纹生成器类"""
    
    @staticmethod
    def item_fingerprint(item) -> str:
        """
        生成数据项指纹
        
        :param item: 数据项
        :return: 指纹字符串
        """
        return generate_data_fingerprint(item)
    
    @staticmethod
    def request_fingerprint(method: str, url: str, body: bytes = b'', headers: Dict[str, str] = None) -> str:
        """
        生成请求指纹
        
        :param method: HTTP方法
        :param url: 请求URL
        :param body: 请求体
        :param headers: 请求头
        :return: 指纹字符串
        """
        return generate_request_fingerprint(method, url, body, headers)
    
    @staticmethod
    def data_fingerprint(data: Any) -> str:
        """
        生成通用数据指纹
        
        :param data: 任意数据
        :return: 指纹字符串
        """
        return generate_data_fingerprint(data)
```

**code file end: crawlo/utils/fingerprint.py**

---


### code file start: crawlo/utils/func_tools.py 

```python
# -*- coding: UTF-8 -*-
from typing import Union, AsyncGenerator, Generator
from inspect import isgenerator, isasyncgen
from crawlo import Response, Request, Item
from crawlo.exceptions import TransformTypeError

T = Union[Request, Item]


async def transform(
        func: Union[Generator[T, None, None], AsyncGenerator[T, None]],
        response: Response
) -> AsyncGenerator[Union[T, Exception], None]:
    """
    转换回调函数的输出为统一异步生成器

    Args:
        func: 同步或异步生成器函数
        response: 当前响应对象

    Yields:
        Union[T, Exception]: 生成请求/Item或异常对象

    Raises:
        TransformTypeError: 当输入类型不符合要求时
    """

    def _set_meta(obj: T) -> T:
        """统一设置请求的depth元数据"""
        if isinstance(obj, Request):
            obj.meta.setdefault('depth', response.meta.get('depth', 0))
        return obj

    # 类型检查前置
    if not (isgenerator(func) or isasyncgen(func)):
        raise TransformTypeError(
            f'Callback must return generator or async generator, got {type(func).__name__}'
        )

    try:
        if isgenerator(func):
            # 同步生成器处理
            for item in func:
                yield _set_meta(item)
        else:
            # 异步生成器处理
            async for item in func:
                yield _set_meta(item)

    except Exception as e:
        yield e

# #!/usr/bin/python
# # -*- coding:UTF-8 -*-
# from typing import Callable, Union
# from inspect import isgenerator, isasyncgen
# from crawlo import Response, Request, Item
# from crawlo.exceptions import TransformTypeError
#
#
# T = Union[Request, Item]
#
#
# async def transform(func: Callable, response: Response):
#     def set_request(t: T) -> T:
#         if isinstance(t, Request):
#             t.meta['depth'] = response.meta['depth']
#         return t
#     try:
#         if isgenerator(func):
#             for f in func:
#                 yield set_request(f)
#         elif isasyncgen(func):
#             async for f in func:
#                 yield set_request(f)
#         else:
#             raise TransformTypeError(
#                 f'callback return type error: {type(func)} must be `generator` or `async generator`'
#             )
#     except Exception as exp:
#         yield exp


```

**code file end: crawlo/utils/func_tools.py**

---


### code file start: crawlo/utils/large_scale_helper.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
大规模爬虫优化辅助工具
"""
import asyncio
import json
import time
from typing import Generator, List, Dict, Any

from crawlo.logging import get_logger


class LargeScaleHelper:
    """大规模爬虫辅助类"""
    
    def __init__(self, batch_size: int = 1000, checkpoint_interval: int = 5000):
        self.batch_size = batch_size
        self.checkpoint_interval = checkpoint_interval
        self.logger = get_logger(self.__class__.__name__)
        
    def batch_iterator(self, data_source, start_offset: int = 0) -> Generator[List[Any], None, None]:
        """
        批量迭代器，适用于大量数据的分批处理
        
        Args:
            data_source: 数据源（支持多种类型）
            start_offset: 起始偏移量
            
        Yields:
            每批数据的列表
        """
        if hasattr(data_source, '__iter__') and not isinstance(data_source, (str, bytes)):
            # 可迭代对象
            yield from self._iterate_batches(data_source, start_offset)
        elif hasattr(data_source, 'get_batch'):
            # 支持分批获取的数据源
            yield from self._get_batches_from_source(data_source, start_offset)
        elif callable(data_source):
            # 函数形式的数据源
            yield from self._get_batches_from_function(data_source, start_offset)
        else:
            raise ValueError(f"不支持的数据源类型: {type(data_source)}")
    
    def _iterate_batches(self, iterable, start_offset: int) -> Generator[List[Any], None, None]:
        """从可迭代对象分批获取数据"""
        iterator = iter(iterable)
        
        # 跳过已处理的数据
        for _ in range(start_offset):
            try:
                next(iterator)
            except StopIteration:
                return
        
        while True:
            batch = []
            for _ in range(self.batch_size):
                try:
                    batch.append(next(iterator))
                except StopIteration:
                    if batch:
                        yield batch
                    return
            
            if batch:
                yield batch
    
    def _get_batches_from_source(self, data_source, start_offset: int) -> Generator[List[Any], None, None]:
        """从支持分批获取的数据源获取数据"""
        offset = start_offset
        
        while True:
            try:
                batch = data_source.get_batch(offset, self.batch_size)
                if not batch:
                    break
                
                yield batch
                offset += len(batch)
                
                if len(batch) < self.batch_size:
                    break  # 已到达数据末尾
                    
            except Exception as e:
                self.logger.error(f"获取批次数据失败: {e}")
                break
    
    def _get_batches_from_function(self, func, start_offset: int) -> Generator[List[Any], None, None]:
        """从函数获取批次数据"""
        offset = start_offset
        
        while True:
            try:
                batch = func(offset, self.batch_size)
                if not batch:
                    break
                
                yield batch
                offset += len(batch)
                
                if len(batch) < self.batch_size:
                    break
                    
            except Exception as e:
                self.logger.error(f"函数获取数据失败: {e}")
                break


class ProgressManager:
    """进度管理器"""
    
    def __init__(self, progress_file: str = "spider_progress.json"):
        self.progress_file = progress_file
        self.logger = get_logger(self.__class__.__name__)
        
    def load_progress(self) -> Dict[str, Any]:
        """加载进度"""
        try:
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                progress = json.load(f)
                self.logger.info(f"加载进度: {progress}")
                return progress
        except FileNotFoundError:
            self.logger.info("📄 未找到进度文件，从头开始")
            return self._get_default_progress()
        except Exception as e:
            self.logger.error(f"加载进度失败: {e}")
            return self._get_default_progress()
    
    def save_progress(self, **kwargs):
        """保存进度"""
        try:
            progress = {
                **kwargs,
                'timestamp': time.time(),
                'formatted_time': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with open(self.progress_file, 'w', encoding='utf-8') as f:
                json.dump(progress, f, indent=2, ensure_ascii=False)
                
            self.logger.debug(f"💾 已保存进度: {progress}")
            
        except Exception as e:
            self.logger.error(f"保存进度失败: {e}")
    
    def _get_default_progress(self) -> Dict[str, Any]:
        """获取默认进度"""
        return {
            'batch_num': 0,
            'processed_count': 0,
            'skipped_count': 0,
            'timestamp': time.time()
        }


class MemoryOptimizer:
    """内存优化器"""
    
    def __init__(self, max_memory_mb: int = 500):
        self.max_memory_mb = max_memory_mb
        self.logger = get_logger(self.__class__.__name__)
        
    def check_memory_usage(self) -> Dict[str, float]:
        """检查内存使用情况"""
        try:
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            
            memory_mb = memory_info.rss / 1024 / 1024
            memory_percent = process.memory_percent()
            
            return {
                'memory_mb': memory_mb,
                'memory_percent': memory_percent,
                'threshold_mb': self.max_memory_mb
            }
        except ImportError:
            self.logger.warning("psutil 未安装，无法监控内存")
            return {}
        except Exception as e:
            self.logger.error(f"检查内存失败: {e}")
            return {}
    
    def should_pause_for_memory(self) -> bool:
        """检查是否应该因内存不足而暂停"""
        memory_info = self.check_memory_usage()
        
        if not memory_info:
            return False
            
        memory_mb = memory_info.get('memory_mb', 0)
        
        if memory_mb > self.max_memory_mb:
            self.logger.warning(f"内存使用过高: {memory_mb:.1f}MB > {self.max_memory_mb}MB")
            return True
            
        return False
    
    def force_garbage_collection(self):
        """强制垃圾回收"""
        try:
            import gc
            collected = gc.collect()
            self.logger.debug(f"垃圾回收: 清理了 {collected} 个对象")
        except Exception as e:
            self.logger.error(f"垃圾回收失败: {e}")


class DataSourceAdapter:
    """数据源适配器"""
    
    @staticmethod
    def from_redis_queue(queue, batch_size: int = 1000):
        """从Redis队列创建批量数据源"""
        def get_batch(offset: int, limit: int) -> List[Dict]:
            try:
                # 如果队列支持范围查询
                if hasattr(queue, 'get_range'):
                    return queue.get_range(offset, offset + limit - 1)
                
                # 如果队列支持批量获取
                if hasattr(queue, 'get_batch'):
                    return queue.get_batch(offset, limit)
                
                # 模拟批量获取
                results = []
                for _ in range(limit):
                    item = queue.get_nowait() if hasattr(queue, 'get_nowait') else None
                    if item:
                        results.append(item)
                    else:
                        break
                
                return results
                
            except Exception as e:
                print(f"获取批次失败: {e}")
                return []
        
        return get_batch
    
    @staticmethod
    def from_database(db_helper, query: str, batch_size: int = 1000):
        """从数据库创建批量数据源"""
        def get_batch(offset: int, limit: int) -> List[Dict]:
            try:
                # 添加分页查询
                paginated_query = f"{query} LIMIT {limit} OFFSET {offset}"
                return db_helper.execute_query(paginated_query)
            except Exception as e:
                print(f"数据库查询失败: {e}")
                return []
        
        return get_batch
    
    @staticmethod
    def from_file(file_path: str, batch_size: int = 1000):
        """从文件创建批量数据源"""
        def get_batch(offset: int, limit: int) -> List[str]:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 跳过已处理的行
                    for _ in range(offset):
                        f.readline()
                    
                    # 读取当前批次
                    batch = []
                    for _ in range(limit):
                        line = f.readline()
                        if not line:
                            break
                        batch.append(line.strip())
                    
                    return batch
            except Exception as e:
                print(f"读取文件失败: {e}")
                return []
        
        return get_batch


class LargeScaleSpiderMixin:
    """大规模爬虫混入类"""
    
    def __init__(self):
        super().__init__()
        self.large_scale_helper = LargeScaleHelper(
            batch_size=getattr(self, 'batch_size', 1000),
            checkpoint_interval=getattr(self, 'checkpoint_interval', 5000)
        )
        self.progress_manager = ProgressManager(
            progress_file=getattr(self, 'progress_file', f"{self.name}_progress.json")
        )
        self.memory_optimizer = MemoryOptimizer(
            max_memory_mb=getattr(self, 'max_memory_mb', 500)
        )
        
    def create_streaming_start_requests(self, data_source):
        """创建流式start_requests生成器"""
        progress = self.progress_manager.load_progress()
        start_offset = progress.get('processed_count', 0)
        
        processed_count = start_offset
        skipped_count = progress.get('skipped_count', 0)
        
        for batch in self.large_scale_helper.batch_iterator(data_source, start_offset):
            
            # 内存检查
            if self.memory_optimizer.should_pause_for_memory():
                self.memory_optimizer.force_garbage_collection()
                # 可以添加延迟或其他处理
                asyncio.sleep(1)
            
            for item in batch:
                processed_count += 1
                
                # 检查进度保存
                if processed_count % self.large_scale_helper.checkpoint_interval == 0:
                    self.progress_manager.save_progress(
                        processed_count=processed_count,
                        skipped_count=skipped_count
                    )
                
                # 生成请求
                request = self.create_request_from_item(item)
                if request:
                    yield request
                else:
                    skipped_count += 1
        
        # 最终保存进度
        self.progress_manager.save_progress(
            processed_count=processed_count,
            skipped_count=skipped_count,
            completed=True
        )
        
        self.logger.info(f"处理完成！总计: {processed_count}, 跳过: {skipped_count}")
    
    def create_request_from_item(self, item):
        """从数据项创建请求（需要子类实现）"""
        raise NotImplementedError("子类必须实现 create_request_from_item 方法")
```

**code file end: crawlo/utils/large_scale_helper.py**

---


### code file start: crawlo/utils/leak_detector.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
资源泄露检测器
==============

提供资源泄露检测和分析功能
"""
import gc
import time
import psutil
from typing import Dict, List, Any, Optional
from collections import defaultdict

from crawlo.logging import get_logger


class ResourceSnapshot:
    """资源快照"""
    
    def __init__(self, name: str = ""):
        self.name = name
        self.timestamp = time.time()
        
        # 进程信息
        process = psutil.Process()
        self.memory_mb = process.memory_info().rss / 1024 / 1024
        self.cpu_percent = process.cpu_percent()
        self.num_threads = process.num_threads()
        self.num_fds = process.num_fds() if hasattr(process, 'num_fds') else 0
        
        # GC信息
        gc.collect()  # 先触发一次GC
        self.gc_objects = len(gc.get_objects())
        self.gc_stats = gc.get_stats()
        
        # 对象类型统计
        self.object_types = self._count_object_types()
    
    def _count_object_types(self, top_n: int = 20) -> Dict[str, int]:
        """统计前N个对象类型"""
        type_counts = defaultdict(int)
        
        for obj in gc.get_objects():
            type_name = type(obj).__name__
            type_counts[type_name] += 1
        
        # 返回前N个
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_types[:top_n])
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'name': self.name,
            'timestamp': self.timestamp,
            'memory_mb': round(self.memory_mb, 2),
            'cpu_percent': self.cpu_percent,
            'num_threads': self.num_threads,
            'num_fds': self.num_fds,
            'gc_objects': self.gc_objects,
            'object_types': self.object_types,
        }


class LeakDetector:
    """
    资源泄露检测器
    
    功能：
    1. 定期记录资源快照
    2. 分析资源增长趋势
    3. 识别可能的泄露点
    4. 生成诊断报告
    """
    
    def __init__(self, name: str = "default"):
        self.name = name
        self._snapshots: List[ResourceSnapshot] = []
        self._logger = get_logger(f"LeakDetector.{name}")
        self._baseline: Optional[ResourceSnapshot] = None
    
    def set_baseline(self, name: str = "baseline"):
        """设置基线快照"""
        self._baseline = ResourceSnapshot(name)
        self._logger.info(f"Baseline set: {self._baseline.memory_mb:.2f}MB")
    
    def snapshot(self, name: str = ""):
        """记录当前资源快照"""
        snapshot = ResourceSnapshot(name or f"snapshot_{len(self._snapshots)}")
        self._snapshots.append(snapshot)
        
        self._logger.debug(
            f"Snapshot '{snapshot.name}': {snapshot.memory_mb:.2f}MB, "
            f"{snapshot.gc_objects} objects"
        )
        
        return snapshot
    
    def analyze(self, threshold_mb: float = 10.0) -> Dict[str, Any]:
        """
        分析资源使用情况
        
        Args:
            threshold_mb: 内存增长阈值（MB），超过视为可能泄露
        
        Returns:
            分析结果
        """
        if len(self._snapshots) < 2:
            return {
                'status': 'insufficient_data',
                'message': 'Need at least 2 snapshots for analysis',
                'snapshot_count': len(self._snapshots),
                'changes': {
                    'memory_mb': 0.0,
                    'memory_percent': 0.0,
                    'objects': 0,
                    'objects_percent': 0.0,
                    'file_descriptors': 0,
                    'threads': 0,
                },
                'potential_leaks': [],
                'type_changes': [],
            }
        
        first = self._baseline or self._snapshots[0]
        latest = self._snapshots[-1]
        
        # 内存增长
        memory_growth_mb = latest.memory_mb - first.memory_mb
        memory_growth_percent = (memory_growth_mb / first.memory_mb) * 100 if first.memory_mb > 0 else 0
        
        # 对象数量增长
        object_growth = latest.gc_objects - first.gc_objects
        object_growth_percent = (object_growth / first.gc_objects) * 100 if first.gc_objects > 0 else 0
        
        # 文件描述符增长
        fd_growth = latest.num_fds - first.num_fds
        
        # 线程数增长
        thread_growth = latest.num_threads - first.num_threads
        
        # 检测泄露
        potential_leaks = []
        
        if memory_growth_mb > threshold_mb:
            potential_leaks.append({
                'type': 'memory',
                'severity': 'high' if memory_growth_mb > threshold_mb * 2 else 'medium',
                'growth_mb': round(memory_growth_mb, 2),
                'growth_percent': round(memory_growth_percent, 2),
            })
        
        if object_growth > 1000:
            potential_leaks.append({
                'type': 'objects',
                'severity': 'medium',
                'growth': object_growth,
                'growth_percent': round(object_growth_percent, 2),
            })
        
        if fd_growth > 10:
            potential_leaks.append({
                'type': 'file_descriptors',
                'severity': 'high',
                'growth': fd_growth,
            })
        
        if thread_growth > 5:
            potential_leaks.append({
                'type': 'threads',
                'severity': 'medium',
                'growth': thread_growth,
            })
        
        # 对象类型变化分析
        type_changes = self._analyze_type_changes(first, latest)
        
        result = {
            'status': 'leak_detected' if potential_leaks else 'healthy',
            'duration_seconds': latest.timestamp - first.timestamp,
            'baseline': first.to_dict(),
            'latest': latest.to_dict(),
            'changes': {
                'memory_mb': round(memory_growth_mb, 2),
                'memory_percent': round(memory_growth_percent, 2),
                'objects': object_growth,
                'objects_percent': round(object_growth_percent, 2),
                'file_descriptors': fd_growth,
                'threads': thread_growth,
            },
            'potential_leaks': potential_leaks,
            'type_changes': type_changes,
            'snapshot_count': len(self._snapshots),
        }
        
        # 记录分析结果
        if potential_leaks:
            self._logger.warning(
                f"Potential leaks detected: {len(potential_leaks)} issue(s), "
                f"memory growth: {memory_growth_mb:.2f}MB ({memory_growth_percent:.1f}%)"
            )
        else:
            self._logger.info(
                f"No leaks detected, memory growth: {memory_growth_mb:.2f}MB "
                f"({memory_growth_percent:.1f}%)"
            )
        
        return result
    
    def _analyze_type_changes(self, first: ResourceSnapshot, latest: ResourceSnapshot, top_n: int = 10) -> List[Dict[str, Any]]:
        """分析对象类型变化"""
        changes = []
        
        # 找出增长最多的类型
        for type_name in set(list(first.object_types.keys()) + list(latest.object_types.keys())):
            old_count = first.object_types.get(type_name, 0)
            new_count = latest.object_types.get(type_name, 0)
            growth = new_count - old_count
            
            if growth > 0:
                changes.append({
                    'type': type_name,
                    'old_count': old_count,
                    'new_count': new_count,
                    'growth': growth,
                    'growth_percent': round((growth / old_count) * 100, 2) if old_count > 0 else float('inf')
                })
        
        # 按增长数量排序
        changes.sort(key=lambda x: x['growth'], reverse=True)
        
        return changes[:top_n]
    
    def get_trend(self, metric: str = 'memory_mb') -> List[float]:
        """获取指标趋势"""
        return [getattr(s, metric) for s in self._snapshots]
    
    def generate_report(self) -> str:
        """生成诊断报告"""
        if not self._snapshots:
            return "No snapshots available"
        
        analysis = self.analyze()
        
        # 如果数据不足，返回简单报告
        if analysis['status'] == 'insufficient_data':
            return (
                "=" * 60 + "\n" +
                "资源泄露检测报告\n" +
                "=" * 60 + "\n" +
                f"检测器: {self.name}\n" +
                f"快照数量: {analysis['snapshot_count']}\n" +
                "\n" +
                "⚠️  数据不足: " + analysis['message'] + "\n" +
                "=" * 60
            )
        
        report = []
        report.append("=" * 60)
        report.append("资源泄露检测报告")
        report.append("=" * 60)
        report.append(f"检测器: {self.name}")
        report.append(f"快照数量: {analysis['snapshot_count']}")
        report.append(f"持续时间: {analysis['duration_seconds']:.2f}秒")
        report.append("")
        
        report.append("资源变化:")
        report.append("-" * 60)
        changes = analysis['changes']
        report.append(f"  内存: {changes['memory_mb']:+.2f}MB ({changes['memory_percent']:+.2f}%)")
        report.append(f"  对象数: {changes['objects']:+d} ({changes['objects_percent']:+.2f}%)")
        report.append(f"  文件描述符: {changes['file_descriptors']:+d}")
        report.append(f"  线程数: {changes['threads']:+d}")
        report.append("")
        
        if analysis['potential_leaks']:
            report.append("⚠️ 潜在泄露:")
            report.append("-" * 60)
            for leak in analysis['potential_leaks']:
                report.append(f"  - {leak['type']}: {leak['severity']} severity")
                if 'growth_mb' in leak:
                    report.append(f"    增长: {leak['growth_mb']:.2f}MB ({leak['growth_percent']:.2f}%)")
                elif 'growth' in leak:
                    report.append(f"    增长: {leak['growth']}")
            report.append("")
        else:
            report.append("✅ 未检测到明显泄露")
            report.append("")
        
        if analysis['type_changes']:
            report.append("对象类型变化（Top 10）:")
            report.append("-" * 60)
            for change in analysis['type_changes'][:10]:
                report.append(
                    f"  {change['type']}: {change['old_count']} -> {change['new_count']} "
                    f"(+{change['growth']})"
                )
            report.append("")
        
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def clear(self):
        """清除所有快照"""
        self._snapshots.clear()
        self._baseline = None
        self._logger.debug("Snapshots cleared")


# 全局检测器注册表
_global_detectors: Dict[str, LeakDetector] = {}


def get_leak_detector(name: str = "default") -> LeakDetector:
    """
    获取泄露检测器实例（单例）
    
    Args:
        name: 检测器名称
    
    Returns:
        LeakDetector实例
    """
    if name not in _global_detectors:
        _global_detectors[name] = LeakDetector(name)
    return _global_detectors[name]


def cleanup_detectors():
    """清理所有检测器"""
    global _global_detectors
    _global_detectors.clear()

```

**code file end: crawlo/utils/leak_detector.py**

---


### code file start: crawlo/utils/log.py 

```python
# ==================== 向后兼容的日志接口 ====================
# 主要功能已迁移到 crawlo.logging 模块
# 本文件提供向后兼容接口，同时支持新的日志系统功能

import logging
from typing import Optional, Any

# 向后兼容：导入新的日志系统
try:
    from crawlo.logging import get_logger as new_get_logger, configure_logging

    _NEW_LOGGING_AVAILABLE = True
except ImportError:
    _NEW_LOGGING_AVAILABLE = False
    new_get_logger = None
    configure_logging = None

LOG_FORMAT = '%(asctime)s - [%(name)s] - %(levelname)s: %(message)s'


# 向后兼容的日志函数
def get_logger(name: str = 'default', level: Optional[int] = None):
    """获取Logger实例 - 向后兼容函数"""
    if _NEW_LOGGING_AVAILABLE and new_get_logger:
        # 使用新的日志系统
        return new_get_logger(name)
    else:
        # 降级到基本的Python logging
        logger = logging.getLogger(name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(LOG_FORMAT)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(level or logging.INFO)
        return logger


def get_component_logger(component_class: Any, settings: Optional[Any] = None, level: Optional[str] = None):
    """
    获取组件Logger - 推荐的组件日志创建方式
    
    Args:
        component_class: 组件类
        settings: 配置对象，用于读取日志级别配置
        level: 日志级别（优先级低于settings中的配置）
        
    Returns:
        logging.Logger: 配置好的Logger实例
    """
    # 获取组件名称
    if hasattr(component_class, '__name__'):
        component_name = component_class.__name__
    else:
        component_name = str(component_class)
    
    # 如果新日志系统可用，使用新系统
    if _NEW_LOGGING_AVAILABLE and new_get_logger:
        return new_get_logger(component_name)
    
    # 否则使用向后兼容方式
    # 从settings中获取日志级别（如果提供）
    if settings is not None:
        # 尝试从settings获取组件特定的日志级别
        if hasattr(settings, 'get'):
            # 检查是否有组件特定的日志级别配置
            component_level = settings.get(f'LOG_LEVEL_{component_name}')
            if component_level is not None:
                level = component_level
            else:
                # 检查通用日志级别
                general_level = settings.get('LOG_LEVEL')
                if general_level is not None:
                    level = general_level
    
    # 转换日志级别
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)
    
    return get_logger(component_name, level)
```

**code file end: crawlo/utils/log.py**

---


### code file start: crawlo/utils/misc.py 

```python
import importlib
import pkgutil
from typing import Iterator, Any, Type

from crawlo.spider import Spider


def walk_modules(module_path: str) -> Iterator[Any]:
    """
    加载模块并递归遍历其所有子模块
    
    Args:
        module_path: 模块路径
        
    Yields:
        导入的模块对象
        
    Raises:
        ImportError: 如果模块无法导入
    """
    # 导入模块
    module = importlib.import_module(module_path)
    yield module
    
    # 如果是包，则递归导入子模块
    if hasattr(module, '__path__'):
        for loader, submodule_name, is_pkg in pkgutil.walk_packages(module.__path__):
            try:
                submodule_path = f"{module_path}.{submodule_name}"
                submodule = importlib.import_module(submodule_path)
                yield submodule
                
                # 如果子模块也是包，递归遍历
                if is_pkg:
                    yield from walk_modules(submodule_path)
            except ImportError:
                # 跳过无法导入的子模块
                continue


def iter_spider_classes(module) -> Iterator[Type[Spider]]:
    """
    遍历模块中的所有Spider子类
    
    Args:
        module: 要遍历的模块
        
    Yields:
        Spider子类
    """
    for attr_name in dir(module):
        attr_value = getattr(module, attr_name)
        if (isinstance(attr_value, type) and
                issubclass(attr_value, Spider) and
                attr_value != Spider and
                hasattr(attr_value, 'name')):
            yield attr_value


def load_object(path: str):
    """
    从路径加载对象
    
    Args:
        path: 对象路径，格式为 module.submodule:object_name 或 module.submodule.object_name
        
    Returns:
        加载的对象
    """
    try:
        # 处理 module.submodule:object_name 格式
        if ':' in path:
            module_path, obj_name = path.split(':', 1)
            module = importlib.import_module(module_path)
            return getattr(module, obj_name)
        else:
            # 处理 module.submodule.object_name 格式
            module_path, obj_name = path.rsplit('.', 1)
            module = importlib.import_module(module_path)
            return getattr(module, obj_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not load object from path '{path}': {e}")
```

**code file end: crawlo/utils/misc.py**

---


### code file start: crawlo/utils/mongo_connection_pool.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
MongoDB 连接池管理器
==================

提供单例模式的MongoDB连接池，确保多个爬虫共享同一个连接池，
避免重复创建连接池导致的资源浪费。

特点：
1. 单例模式 - 全局唯一的连接池实例
2. 线程安全 - 使用异步锁保护初始化过程
3. 配置隔离 - 支持不同的数据库配置创建不同的连接池
4. 自动清理 - 支持资源清理和重置
"""

import asyncio
from typing import Dict, Optional, Any
from motor.motor_asyncio import AsyncIOMotorClient
from crawlo.logging import get_logger


class MongoConnectionPoolManager:
    """MongoDB 连接池管理器（单例模式）"""
    
    _instances: Dict[str, 'MongoConnectionPoolManager'] = {}
    _lock = asyncio.Lock()
    
    def __init__(self, pool_key: str):
        """
        初始化连接池管理器
        
        Args:
            pool_key: 连接池唯一标识
        """
        self.pool_key = pool_key
        self.client: Optional[AsyncIOMotorClient] = None
        self._client_lock = asyncio.Lock()
        self._client_initialized = False
        self._config: Dict[str, Any] = {}
        self.logger = get_logger(f'MongoPool.{pool_key}')
    
    @classmethod
    async def get_client(
        cls,
        mongo_uri: str = 'mongodb://localhost:27017',
        db_name: str = 'crawlo',
        max_pool_size: int = 100,
        min_pool_size: int = 10,
        connect_timeout_ms: int = 5000,
        socket_timeout_ms: int = 30000,
        **kwargs
    ) -> AsyncIOMotorClient:
        """
        获取 MongoDB 客户端实例（单例模式）
        
        Args:
            mongo_uri: MongoDB 连接 URI
            db_name: 数据库名
            max_pool_size: 最大连接池大小
            min_pool_size: 最小连接池大小
            connect_timeout_ms: 连接超时（毫秒）
            socket_timeout_ms: Socket 超时（毫秒）
            **kwargs: 其他连接参数
            
        Returns:
            MongoDB 客户端实例
        """
        # 生成连接池唯一标识
        pool_key = f"{mongo_uri}:{db_name}"
        
        async with cls._lock:
            if pool_key not in cls._instances:
                instance = cls(pool_key)
                instance._config = {
                    'mongo_uri': mongo_uri,
                    'db_name': db_name,
                    'max_pool_size': max_pool_size,
                    'min_pool_size': min_pool_size,
                    'connect_timeout_ms': connect_timeout_ms,
                    'socket_timeout_ms': socket_timeout_ms,
                    **kwargs
                }
                cls._instances[pool_key] = instance
                instance.logger.info(
                    f"创建新的 MongoDB 连接池管理器: {pool_key} "
                    f"(minPoolSize={min_pool_size}, maxPoolSize={max_pool_size})"
                )
            
            instance = cls._instances[pool_key]
            await instance._ensure_client()
            return instance.client
    
    async def _ensure_client(self):
        """确保客户端已初始化（线程安全）"""
        if self._client_initialized and self.client:
            return
        
        async with self._client_lock:
            if not self._client_initialized:
                try:
                    self.client = AsyncIOMotorClient(
                        self._config['mongo_uri'],
                        maxPoolSize=self._config['max_pool_size'],
                        minPoolSize=self._config['min_pool_size'],
                        connectTimeoutMS=self._config['connect_timeout_ms'],
                        socketTimeoutMS=self._config['socket_timeout_ms']
                    )
                    
                    self._client_initialized = True
                    self.logger.info(
                        f"MongoDB 客户端初始化成功: {self.pool_key} "
                        f"(minPoolSize={self._config['min_pool_size']}, "
                        f"maxPoolSize={self._config['max_pool_size']})"
                    )
                except Exception as e:
                    self.logger.error(f"MongoDB 客户端初始化失败: {e}")
                    self._client_initialized = False
                    self.client = None
                    raise
    
    @classmethod
    async def close_all_clients(cls):
        """关闭所有 MongoDB 客户端"""
        logger = get_logger('MongoPool')
        logger.info(f"开始关闭所有 MongoDB 客户端，共 {len(cls._instances)} 个")
        
        for pool_key, instance in cls._instances.items():
            try:
                if instance.client:
                    logger.info(f"关闭 MongoDB 客户端: {pool_key}")
                    instance.client.close()
                    logger.info(f"MongoDB 客户端已关闭: {pool_key}")
            except Exception as e:
                logger.error(f"关闭 MongoDB 客户端 {pool_key} 时发生错误: {e}")
        
        cls._instances.clear()
        logger.info("所有 MongoDB 客户端已关闭")
    
    @classmethod
    def get_pool_stats(cls) -> Dict[str, Any]:
        """获取所有连接池的统计信息"""
        stats = {
            'total_pools': len(cls._instances),
            'pools': {}
        }
        
        for pool_key, instance in cls._instances.items():
            if instance.client:
                stats['pools'][pool_key] = {
                    'uri': instance._config.get('mongo_uri', 'unknown'),
                    'db_name': instance._config.get('db_name', 'unknown'),
                    'min_pool_size': instance._config.get('min_pool_size', 'unknown'),
                    'max_pool_size': instance._config.get('max_pool_size', 'unknown')
                }
        
        return stats

```

**code file end: crawlo/utils/mongo_connection_pool.py**

---


### code file start: crawlo/utils/mysql_connection_pool.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
MySQL 连接池管理器
================

提供单例模式的MySQL连接池，确保多个爬虫共享同一个连接池，
避免重复创建连接池导致的资源浪费。

特点：
1. 单例模式 - 全局唯一的连接池实例
2. 线程安全 - 使用异步锁保护初始化过程
3. 配置隔离 - 支持不同的数据库配置创建不同的连接池
4. 自动清理 - 支持资源清理和重置
"""

import asyncio
import aiomysql
from asyncmy import create_pool as asyncmy_create_pool
from typing import Dict, Optional, Any
from crawlo.logging import get_logger


class MySQLConnectionPoolManager:
    """MySQL 连接池管理器（单例模式）"""
    
    _instances: Dict[str, 'MySQLConnectionPoolManager'] = {}
    _lock = asyncio.Lock()
    
    def __init__(self, pool_key: str):
        """
        初始化连接池管理器
        
        Args:
            pool_key: 连接池唯一标识
        """
        self.pool_key = pool_key
        self.pool = None
        self._pool_lock = asyncio.Lock()
        self._pool_initialized = False
        self._config: Dict[str, Any] = {}
        self._pool_type: str = 'asyncmy'  # 默认使用 asyncmy
        self.logger = get_logger(f'MySQLPool.{pool_key}')
    
    @classmethod
    async def get_pool(
        cls, 
        pool_type: str = 'asyncmy',
        host: str = 'localhost',
        port: int = 3306,
        user: str = 'root',
        password: str = '',
        db: str = 'crawlo',
        minsize: int = 3,
        maxsize: int = 10,
        **kwargs
    ):
        """
        获取连接池实例（单例模式）
        
        Args:
            pool_type: 连接池类型 ('asyncmy' 或 'aiomysql')
            host: 数据库主机
            port: 数据库端口
            user: 数据库用户名
            password: 数据库密码
            db: 数据库名
            minsize: 最小连接数
            maxsize: 最大连接数
            **kwargs: 其他连接参数
            
        Returns:
            连接池实例
        """
        # 生成连接池唯一标识
        pool_key = f"{pool_type}:{host}:{port}:{db}"
        
        async with cls._lock:
            if pool_key not in cls._instances:
                instance = cls(pool_key)
                instance._pool_type = pool_type
                instance._config = {
                    'host': host,
                    'port': port,
                    'user': user,
                    'password': password,
                    'db': db,
                    'minsize': minsize,
                    'maxsize': maxsize,
                    **kwargs
                }
                cls._instances[pool_key] = instance
                instance.logger.info(
                    f"创建新的连接池管理器: {pool_key} "
                    f"(type={pool_type}, minsize={minsize}, maxsize={maxsize})"
                )
            
            instance = cls._instances[pool_key]
            await instance._ensure_pool()
            return instance.pool
    
    async def _ensure_pool(self):
        """确保连接池已初始化（线程安全）"""
        if self._pool_initialized:
            # 检查连接池是否仍然有效
            if self.pool and hasattr(self.pool, 'closed') and not self.pool.closed:
                return
            else:
                self.logger.warning("连接池已初始化但无效，重新初始化")
        
        async with self._pool_lock:
            if not self._pool_initialized:
                try:
                    if self._pool_type == 'asyncmy':
                        self.pool = await self._create_asyncmy_pool()
                    elif self._pool_type == 'aiomysql':
                        self.pool = await self._create_aiomysql_pool()
                    else:
                        raise ValueError(f"不支持的连接池类型: {self._pool_type}")
                    
                    self._pool_initialized = True
                    self.logger.info(
                        f"连接池初始化成功: {self.pool_key} "
                        f"(minsize={self._config['minsize']}, maxsize={self._config['maxsize']})"
                    )
                except Exception as e:
                    self.logger.error(f"连接池初始化失败: {e}")
                    self._pool_initialized = False
                    self.pool = None
                    raise
    
    async def _create_asyncmy_pool(self):
        """创建 asyncmy 连接池"""
        return await asyncmy_create_pool(
            host=self._config['host'],
            port=self._config['port'],
            user=self._config['user'],
            password=self._config['password'],
            db=self._config['db'],
            minsize=self._config['minsize'],
            maxsize=self._config['maxsize'],
            echo=self._config.get('echo', False)
        )
    
    async def _create_aiomysql_pool(self):
        """创建 aiomysql 连接池"""
        return await aiomysql.create_pool(
            host=self._config['host'],
            port=self._config['port'],
            user=self._config['user'],
            password=self._config['password'],
            db=self._config['db'],
            minsize=self._config['minsize'],
            maxsize=self._config['maxsize'],
            cursorclass=aiomysql.DictCursor,
            autocommit=False
        )
    
    @classmethod
    async def close_all_pools(cls):
        """关闭所有连接池"""
        logger = get_logger('MySQLPool')
        logger.info(f"开始关闭所有连接池，共 {len(cls._instances)} 个")
        
        for pool_key, instance in cls._instances.items():
            try:
                if instance.pool:
                    logger.info(f"关闭连接池: {pool_key}")
                    instance.pool.close()
                    await instance.pool.wait_closed()
                    logger.info(f"连接池已关闭: {pool_key}")
            except Exception as e:
                logger.error(f"关闭连接池 {pool_key} 时发生错误: {e}")
        
        cls._instances.clear()
        logger.info("所有连接池已关闭")
    
    @classmethod
    def get_pool_stats(cls) -> Dict[str, Any]:
        """获取所有连接池的统计信息"""
        stats = {
            'total_pools': len(cls._instances),
            'pools': {}
        }
        
        for pool_key, instance in cls._instances.items():
            if instance.pool:
                stats['pools'][pool_key] = {
                    'type': instance._pool_type,
                    'size': getattr(instance.pool, 'size', 'unknown'),
                    'minsize': instance._config.get('minsize', 'unknown'),
                    'maxsize': instance._config.get('maxsize', 'unknown'),
                    'host': instance._config.get('host', 'unknown'),
                    'db': instance._config.get('db', 'unknown')
                }
        
        return stats

```

**code file end: crawlo/utils/mysql_connection_pool.py**

---


### code file start: crawlo/utils/performance_monitor.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
性能监控工具
提供系统性能监控和资源使用情况跟踪
"""
import asyncio
import time
from functools import wraps
from typing import Dict, Any

import psutil

from crawlo.utils.error_handler import ErrorHandler
from crawlo.logging import get_logger


class PerformanceMonitor:
    """性能监控器"""
    
    def __init__(self, logger_name: str = __name__):
        self.logger = get_logger(logger_name)
        self.error_handler = ErrorHandler(logger_name)
        self.process = psutil.Process()
        self.start_time = time.time()
        
        # 性能指标
        self.metrics = {
            'cpu_usage': [],
            'memory_usage': [],
            'network_io': [],
            'disk_io': []
        }
    
    def get_system_metrics(self) -> Dict[str, Any]:
        """
        获取系统性能指标
        
        Returns:
            包含各种性能指标的字典
        """
        try:
            # CPU使用率
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # 内存使用情况
            memory = psutil.virtual_memory()
            
            # 网络IO
            net_io = psutil.net_io_counters()
            
            # 磁盘IO
            disk_io = psutil.disk_io_counters()
            
            # 进程特定信息
            process_memory = self.process.memory_info()
            process_cpu = self.process.cpu_percent()
            
            return {
                'timestamp': time.time(),
                'uptime': time.time() - self.start_time,
                'cpu': {
                    'percent': cpu_percent,
                    'count': psutil.cpu_count(),
                    'freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else {}
                },
                'memory': {
                    'total': memory.total,
                    'available': memory.available,
                    'percent': memory.percent,
                    'used': memory.used,
                    'free': memory.free
                },
                'process': {
                    'memory_rss': process_memory.rss,
                    'memory_vms': process_memory.vms,
                    'cpu_percent': process_cpu,
                    'num_threads': self.process.num_threads(),
                    'num_fds': self.process.num_fds() if hasattr(self.process, 'num_fds') else 0
                },
                'network': {
                    'bytes_sent': net_io.bytes_sent,
                    'bytes_recv': net_io.bytes_recv,
                    'packets_sent': net_io.packets_sent,
                    'packets_recv': net_io.packets_recv
                },
                'disk': {
                    'read_bytes': disk_io.read_bytes,
                    'write_bytes': disk_io.write_bytes,
                    'read_count': disk_io.read_count,
                    'write_count': disk_io.write_count
                }
            }
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="获取系统性能指标失败", 
                raise_error=False
            )
            return {}
    
    def log_system_metrics(self, detailed: bool = False):
        """
        记录系统性能指标
        
        Args:
            detailed: 是否记录详细信息
        """
        try:
            metrics = self.get_system_metrics()
            if not metrics:
                return
            
            # 基本信息
            basic_info = (
                f"系统性能指标 | "
                f"CPU: {metrics['cpu']['percent']:.1f}% | "
                f"内存: {metrics['memory']['percent']:.1f}% | "
                f"进程CPU: {metrics['process']['cpu_percent']:.1f}% | "
                f"进程内存: {metrics['process']['memory_rss'] / 1024 / 1024:.1f}MB"
            )
            self.logger.info(basic_info)
            
            # 详细信息
            if detailed:
                detailed_info = (
                    f"   详细信息:\n"
                    f"   - CPU: {metrics['cpu']['count']} 核心\n"
                    f"   - 内存: 总计 {metrics['memory']['total'] / 1024 / 1024 / 1024:.1f}GB, "
                    f"可用 {metrics['memory']['available'] / 1024 / 1024 / 1024:.1f}GB\n"
                    f"   - 网络: 发送 {metrics['network']['bytes_sent'] / 1024 / 1024:.1f}MB, "
                    f"接收 {metrics['network']['bytes_recv'] / 1024 / 1024:.1f}MB\n"
                    f"   - 磁盘: 读取 {metrics['disk']['read_bytes'] / 1024 / 1024:.1f}MB, "
                    f"写入 {metrics['disk']['write_bytes'] / 1024 / 1024:.1f}MB"
                )
                self.logger.debug(detailed_info)
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context="记录系统性能指标失败", 
                raise_error=False
            )
    
    def start_monitoring(self, interval: int = 60, detailed: bool = False):
        """
        开始定期监控
        
        Args:
            interval: 监控间隔（秒）
            detailed: 是否记录详细信息
        """
        async def monitor_loop():
            while True:
                try:
                    self.log_system_metrics(detailed)
                    await asyncio.sleep(interval)
                except asyncio.CancelledError:
                    break
                except Exception as e:
                    self.logger.error(f"监控循环错误: {e}")
        
        # 启动监控任务
        self.monitor_task = asyncio.create_task(monitor_loop())
        self.logger.info(f"开始性能监控，间隔: {interval}秒")
    
    async def stop_monitoring(self):
        """停止监控"""
        if hasattr(self, 'monitor_task') and self.monitor_task:
            self.monitor_task.cancel()
            try:
                await self.monitor_task
            except asyncio.CancelledError:
                pass
            self.logger.info("性能监控已停止")


class PerformanceTimer:
    """性能计时器"""
    
    def __init__(self, name: str = "timer"):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.logger = get_logger(f"{__name__}.{self.__class__.__name__}")
        self.error_handler = ErrorHandler(f"{__name__}.{self.__class__.__name__}")
    
    def start(self):
        """开始计时"""
        self.start_time = time.time()
        self.logger.debug(f"开始计时: {self.name}")
    
    def stop(self) -> float:
        """
        停止计时并返回耗时
        
        Returns:
            耗时（秒）
        """
        self.end_time = time.time()
        if self.start_time is None:
            raise RuntimeError("计时器未启动")
        
        elapsed = self.end_time - self.start_time
        self.logger.debug(f"停止计时: {self.name}, 耗时: {elapsed:.3f}秒")
        return elapsed
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            elapsed = self.stop()
            if exc_type is None:
                self.logger.info(f"{self.name} 执行成功，耗时: {elapsed:.3f}秒")
            else:
                self.logger.error(f"{self.name} 执行失败，耗时: {elapsed:.3f}秒")
        except Exception as e:
            self.error_handler.handle_error(
                e, 
                context=f"计时器退出时发生错误: {self.name}", 
                raise_error=False
            )


def performance_monitor_decorator(name: str = None, log_level: str = "INFO"):
    """
    装饰器：监控函数性能
    
    Args:
        name: 函数名称（如果为None则使用函数名）
        log_level: 日志级别
    """
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            timer_name = name or f"{func.__module__}.{func.__name__}"
            logger = get_logger(timer_name)
            
            with PerformanceTimer(timer_name) as timer:
                if asyncio.iscoroutinefunction(func):
                    return await func(*args, **kwargs)
                else:
                    return func(*args, **kwargs)
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            timer_name = name or f"{func.__module__}.{func.__name__}"
            logger = get_logger(timer_name)
            
            with PerformanceTimer(timer_name) as timer:
                return func(*args, **kwargs)
        
        # 根据函数是否为异步函数返回相应的包装器
        import inspect
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator


# 全局性能监控器实例
default_performance_monitor = PerformanceMonitor()


def monitor_performance(interval: int = 60, detailed: bool = False):
    """
    便捷函数：开始性能监控
    
    Args:
        interval: 监控间隔（秒）
        detailed: 是否记录详细信息
    """
    default_performance_monitor.start_monitoring(interval, detailed)


def get_current_metrics() -> Dict[str, Any]:
    """
    便捷函数：获取当前性能指标
    
    Returns:
        性能指标字典
    """
    return default_performance_monitor.get_system_metrics()
```

**code file end: crawlo/utils/performance_monitor.py**

---


### code file start: crawlo/utils/queue_helper.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
队列配置辅助工具
为用户提供简洁的队列配置接口
"""
from typing import Dict, Any, Optional


class QueueHelper:
    """队列配置辅助类"""
    
    @staticmethod
    def use_memory_queue(max_size: int = 2000) -> Dict[str, Any]:
        """
        配置使用内存队列
        
        Args:
            max_size: 队列最大容量
            
        Returns:
            配置字典
        """
        return {
            'QUEUE_TYPE': 'memory',
            'SCHEDULER_MAX_QUEUE_SIZE': max_size,
        }
    
    @staticmethod
    def use_redis_queue(
        host: str = "127.0.0.1",
        port: int = 6379,
        password: Optional[str] = None,
        db: int = 0,
        queue_name: str = "crawlo:requests",
        max_retries: int = 3,
        timeout: int = 300
    ) -> Dict[str, Any]:
        """
        配置使用 Redis 分布式队列
        
        Args:
            host: Redis 主机地址
            port: Redis 端口
            password: Redis 密码（可选）
            db: Redis 数据库编号
            queue_name: 队列名称
            max_retries: 最大重试次数
            timeout: 操作超时时间（秒）
            
        Returns:
            配置字典
        """
        if password:
            redis_url = f"redis://:{password}@{host}:{port}/{db}"
        else:
            redis_url = f"redis://{host}:{port}/{db}"
        
        return {
            'QUEUE_TYPE': 'redis',
            'REDIS_URL': redis_url,
            'REDIS_HOST': host,
            'REDIS_PORT': port,
            'REDIS_PASSWORD': password or '',
            'REDIS_DB': db,
            'SCHEDULER_QUEUE_NAME': queue_name,
            'QUEUE_MAX_RETRIES': max_retries,
            'QUEUE_TIMEOUT': timeout,
        }
    
    @staticmethod
    def auto_queue(
        redis_fallback: bool = True,
        memory_max_size: int = 2000,
        **redis_kwargs
    ) -> Dict[str, Any]:
        """
        配置自动选择队列类型
        
        Args:
            redis_fallback: Redis 不可用时是否回退到内存队列
            memory_max_size: 内存队列最大容量
            **redis_kwargs: Redis 配置参数
            
        Returns:
            配置字典
        """
        config = {
            'QUEUE_TYPE': 'auto',
            'SCHEDULER_MAX_QUEUE_SIZE': memory_max_size,
        }
        
        # 添加 Redis 配置（用于自动检测）
        if redis_kwargs:
            redis_config = QueueHelper.use_redis_queue(**redis_kwargs)
            config.update(redis_config)
            config['QUEUE_TYPE'] = 'auto'  # 确保是自动模式
        
        return config


# 预定义的常用配置
class QueuePresets:
    """预定义的队列配置"""
    
    # 开发环境：使用内存队列
    DEVELOPMENT = QueueHelper.use_memory_queue(max_size=1000)
    
    # 生产环境：使用 Redis 分布式队列
    PRODUCTION = QueueHelper.use_redis_queue(
        host="127.0.0.1",
        port=6379,
        queue_name="crawlo:production",
        max_retries=5,
        timeout=600
    )
    
    # 测试环境：自动选择，Redis 不可用时使用内存队列
    TESTING = QueueHelper.auto_queue(
        redis_fallback=True,
        memory_max_size=500,
        host="127.0.0.1",
        port=6379,
        queue_name="crawlo:testing"
    )
    
    # 高性能环境：Redis 集群
    HIGH_PERFORMANCE = QueueHelper.use_redis_queue(
        host="redis-cluster.example.com",
        port=6379,
        queue_name="crawlo:cluster",
        max_retries=10,
        timeout=300
    )


def apply_queue_config(settings_dict: Dict[str, Any], config: Dict[str, Any]) -> None:
    """
    将队列配置应用到设置字典
    
    Args:
        settings_dict: 现有的设置字典
        config: 队列配置字典
    """
    settings_dict.update(config)


# 使用示例和文档
USAGE_EXAMPLES = """
# 使用示例：

# 1. 在 settings.py 中使用内存队列
from crawlo.utils.queue_helper import QueueHelper
apply_queue_config(locals(), QueueHelper.use_memory_queue())

# 2. 在 settings.py 中使用 Redis 队列
apply_queue_config(locals(), QueueHelper.use_redis_queue(
    host="redis.example.com",
    password="your_password"
))

# 3. 使用预定义配置
from crawlo.utils.queue_helper import QueuePresets
apply_queue_config(locals(), QueuePresets.PRODUCTION)

# 4. 自动选择队列类型
apply_queue_config(locals(), QueueHelper.auto_queue(
    host="127.0.0.1",
    port=6379
))

# 5. 直接在 settings 中配置
QUEUE_TYPE = 'auto'  # 'memory', 'redis', 'auto'
REDIS_URL = 'redis://127.0.0.1:6379/0'
SCHEDULER_MAX_QUEUE_SIZE = 2000
"""
```

**code file end: crawlo/utils/queue_helper.py**

---


### code file start: crawlo/utils/redis_checker.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Redis可用性检查工具
==================
提供Redis连接可用性检测功能，用于自动模式下的运行时决策。
"""

import asyncio
import logging
from typing import Optional
import redis.asyncio as aioredis


class RedisChecker:
    """Redis可用性检查器"""
    
    def __init__(self, redis_url: str, timeout: float = 5.0):
        """
        初始化Redis检查器
        
        Args:
            redis_url: Redis连接URL
            timeout: 连接超时时间（秒）
        """
        self.redis_url = redis_url
        self.timeout = timeout
        self.logger = logging.getLogger(self.__class__.__name__)
    
    async def is_redis_available(self) -> bool:
        """
        检查Redis是否可用
        
        Returns:
            Redis是否可用
        """
        try:
            # 创建Redis连接
            redis_client = aioredis.from_url(
                self.redis_url,
                socket_connect_timeout=self.timeout,
                socket_timeout=self.timeout,
                retry_on_timeout=False
            )
            
            # 尝试执行ping命令
            await asyncio.wait_for(redis_client.ping(), timeout=self.timeout)
            
            # 关闭连接
            await redis_client.close()
            
            self.logger.debug(f"Redis连接测试成功: {self.redis_url}")
            return True
            
        except asyncio.TimeoutError:
            self.logger.warning(f"Redis连接超时: {self.redis_url}")
            return False
            
        except Exception as e:
            self.logger.warning(f"Redis连接失败: {self.redis_url} - {e}")
            return False
    
    @staticmethod
    async def check_redis_availability(redis_url: str, timeout: float = 5.0) -> bool:
        """
        便捷函数：检查Redis是否可用
        
        Args:
            redis_url: Redis连接URL
            timeout: 连接超时时间（秒）
            
        Returns:
            Redis是否可用
        """
        checker = RedisChecker(redis_url, timeout)
        return await checker.is_redis_available()


# 便捷函数
async def is_redis_available(redis_url: str, timeout: float = 5.0) -> bool:
    """
    检查Redis是否可用
    
    Args:
        redis_url: Redis连接URL
        timeout: 连接超时时间（秒）
        
    Returns:
        Redis是否可用
    """
    return await RedisChecker.check_redis_availability(redis_url, timeout)
```

**code file end: crawlo/utils/redis_checker.py**

---


### code file start: crawlo/utils/redis_connection_pool.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Redis连接池工具
提供Redis连接池管理和配置
"""
from contextlib import asynccontextmanager
from typing import Dict, Any, Optional, List, Union, TYPE_CHECKING
import re

import redis.asyncio as aioredis

# 尝试导入Redis集群支持
try:
    from redis.asyncio.cluster import RedisCluster
    from redis.asyncio.cluster import ClusterNode
    REDIS_CLUSTER_AVAILABLE = True
except ImportError:
    RedisCluster = None
    ClusterNode = None
    REDIS_CLUSTER_AVAILABLE = False


if TYPE_CHECKING:
    from crawlo.utils.error_handler import ErrorHandler


class RedisConnectionPool:
    """Redis连接池管理器"""
    
    # 默认连接池配置
    DEFAULT_CONFIG = {
        'max_connections': 50,
        'socket_connect_timeout': 5,
        'socket_timeout': 30,
        'socket_keepalive': True,
        'health_check_interval': 30,
        'retry_on_timeout': True,
        'encoding': 'utf-8',
        'decode_responses': False,
    }
    
    # Redis集群不支持的配置参数
    CLUSTER_UNSUPPORTED_CONFIG = {
        'retry_on_timeout',
        'health_check_interval',
        'socket_keepalive'
    }
    
    def __init__(self, redis_url: str, is_cluster: bool = False, cluster_nodes: Optional[List[str]] = None, **kwargs):
        self.redis_url = redis_url
        self.is_cluster = is_cluster
        self.cluster_nodes = cluster_nodes
        self.config = {**self.DEFAULT_CONFIG, **kwargs}
        
        # 延迟初始化logger和error_handler
        self._logger = None
        self._error_handler: Optional["ErrorHandler"] = None
        
        # 连接池实例
        self._connection_pool: Optional[aioredis.ConnectionPool] = None
        self._redis_client = None
        self._connection_tested = False  # 标记是否已测试连接
        
        # 连接池统计信息
        self._stats = {
            'created_connections': 0,
            'active_connections': 0,
            'idle_connections': 0,
            'errors': 0
        }
        
        # 初始化连接池
        self._initialize_pool()
    
    @property
    def logger(self):
        """延迟初始化logger"""
        if self._logger is None:
            from crawlo.logging import get_logger
            self._logger = get_logger(self.__class__.__name__)
        return self._logger
    
    @property
    def error_handler(self):
        """延迟初始化error_handler"""
        if self._error_handler is None:
            from crawlo.utils.error_handler import ErrorHandler
            self._error_handler = ErrorHandler(self.__class__.__name__)
        return self._error_handler
    
    def _is_cluster_url(self) -> bool:
        """判断是否为集群URL格式"""
        if self.cluster_nodes:
            return True
        # 检查URL是否包含多个节点（逗号分隔）
        if ',' in self.redis_url:
            return True
        # 检查URL是否为集群格式
        if 'redis-cluster://' in self.redis_url or 'rediss-cluster://' in self.redis_url:
            return True
        return False
    
    def _parse_cluster_nodes(self) -> List[Dict[str, Union[str, int]]]:
        """解析集群节点"""
        nodes = []
        if self.cluster_nodes:
            node_list = self.cluster_nodes
        else:
            # 从URL中解析节点
            # 支持格式: redis://host1:port1,host2:port2,host3:port3
            # 或: host1:port1,host2:port2,host3:port3
            url_part = self.redis_url.replace('redis://', '').replace('rediss://', '')
            node_list = url_part.split(',')
        
        for node in node_list:
            # 解析host:port格式
            if ':' in node:
                host, port = node.rsplit(':', 1)
                try:
                    nodes.append({
                        'host': str(host.strip()),
                        'port': int(port.strip())
                    })
                except ValueError:
                    self.logger.warning(f"无效的节点格式: {node}")
            else:
                # 默认端口
                nodes.append({
                    'host': str(node.strip()),
                    'port': 6379
                })
        
        return nodes
    
    def _get_cluster_config(self) -> Dict[str, Any]:
        """获取适用于Redis集群的配置"""
        # 移除集群不支持的配置参数
        cluster_config = self.config.copy()
        for unsupported_key in self.CLUSTER_UNSUPPORTED_CONFIG:
            cluster_config.pop(unsupported_key, None)
        return cluster_config
    
    def _initialize_pool(self):
        """初始化连接池"""
        try:
            # 智能检测是否应该使用集群模式
            should_use_cluster = self.is_cluster or self._is_cluster_url()
            
            if should_use_cluster and REDIS_CLUSTER_AVAILABLE and RedisCluster is not None and ClusterNode is not None:
                # 使用Redis集群
                nodes = self._parse_cluster_nodes()
                cluster_config = self._get_cluster_config()
                
                if nodes:
                    if len(nodes) == 1:
                        # 单节点集群
                        self._redis_client = RedisCluster(
                            host=str(nodes[0]['host']),
                            port=int(nodes[0]['port']),
                            **cluster_config
                        )
                    else:
                        # 多节点集群
                        cluster_node_objects = [ClusterNode(str(node['host']), int(node['port'])) for node in nodes]
                        self._redis_client = RedisCluster(
                            startup_nodes=cluster_node_objects,
                            **cluster_config
                        )
                    self.logger.info(f"Redis集群连接池初始化成功: {len(nodes)} 个节点")
                else:
                    # 回退到单实例模式
                    self._connection_pool = aioredis.ConnectionPool.from_url(
                        self.redis_url,
                        **self.config
                    )
                    self._redis_client = aioredis.Redis(
                        connection_pool=self._connection_pool
                    )
                    self.logger.warning("无法解析集群节点，回退到单实例模式")
            else:
                # 使用单实例Redis
                self._connection_pool = aioredis.ConnectionPool.from_url(
                    self.redis_url,
                    **self.config
                )
                
                self._redis_client = aioredis.Redis(
                    connection_pool=self._connection_pool
                )
            
            # 只在调试模式下输出详细连接池信息
            if should_use_cluster and REDIS_CLUSTER_AVAILABLE:
                self.logger.debug(f"Redis集群连接池初始化成功: {self.redis_url}")
            else:
                self.logger.debug(f"Redis连接池初始化成功: {self.redis_url}")
                self.logger.debug(f"   连接池配置: {self.config}")
                
        except Exception as e:
            from crawlo.utils.error_handler import ErrorContext
            error_context = ErrorContext(context="Redis连接池初始化失败")
            self.error_handler.handle_error(
                e, 
                context=error_context, 
                raise_error=True
            )
    
    async def _test_connection(self):
        """测试Redis连接"""
        if self._redis_client and not self._connection_tested:
            try:
                await self._redis_client.ping()
                self._connection_tested = True
                # 只在调试模式下输出连接测试成功信息
                if REDIS_CLUSTER_AVAILABLE and RedisCluster is not None and isinstance(self._redis_client, RedisCluster):
                    self.logger.debug(f"Redis集群连接测试成功: {self.redis_url}")
                else:
                    self.logger.debug(f"Redis连接测试成功: {self.redis_url}")
            except Exception as e:
                self.logger.error(f"Redis连接测试失败: {self.redis_url} - {e}")
                raise
    
    async def get_connection(self):
        """
        获取Redis连接实例
        
        Returns:
            Redis连接实例
        """
        if not self._redis_client:
            self._initialize_pool()
        
        # 确保连接有效
        await self._test_connection()
        
        self._stats['active_connections'] += 1
        return self._redis_client
    
    async def ping(self) -> bool:
        """
        检查Redis连接是否正常
        
        Returns:
            连接是否正常
        """
        try:
            if self._redis_client:
                await self._redis_client.ping()
                return True
            return False
        except Exception as e:
            self.logger.warning(f"Redis连接检查失败: {e}")
            return False
    
    async def close(self):
        """关闭连接池"""
        try:
            if self._redis_client:
                await self._redis_client.close()
                self._redis_client = None
            
            if self._connection_pool:
                await self._connection_pool.disconnect()
                self._connection_pool = None
                
            self.logger.info("Redis连接池已关闭")
        except Exception as e:
            from crawlo.utils.error_handler import ErrorContext
            error_context = ErrorContext(context="关闭Redis连接池失败")
            self.error_handler.handle_error(
                e, 
                context=error_context, 
                raise_error=False
            )
    
    def get_stats(self) -> Dict[str, Any]:
        """
        获取连接池统计信息
        
        Returns:
            统计信息字典
        """
        if self._connection_pool and hasattr(self._connection_pool, 'max_connections'):
            pool_stats = {
                'max_connections': self._connection_pool.max_connections,
                'available_connections': len(self._connection_pool._available_connections) if hasattr(self._connection_pool, '_available_connections') else 0,
                'in_use_connections': len(self._connection_pool._in_use_connections) if hasattr(self._connection_pool, '_in_use_connections') else 0,
            }
            self._stats.update(pool_stats)
        
        return self._stats.copy()
    
    @asynccontextmanager
    async def connection_context(self):
        """
        连接上下文管理器
        
        Yields:
            Redis连接实例
        """
        connection = await self.get_connection()
        try:
            yield connection
        finally:
            self._stats['active_connections'] -= 1
            self._stats['idle_connections'] += 1


class RedisBatchOperationHelper:
    """Redis批量操作助手"""
    
    def __init__(self, redis_client, batch_size: int = 100):
        self.redis_client = redis_client
        self.batch_size = batch_size
        
        # 延迟初始化logger和error_handler
        self._logger = None
        self._error_handler = None
    
    @property
    def logger(self):
        """延迟初始化logger"""
        if self._logger is None:
            from crawlo.logging import get_logger
            self._logger = get_logger(self.__class__.__name__)
        return self._logger
    
    @property
    def error_handler(self):
        """延迟初始化error_handler"""
        if self._error_handler is None:
            from crawlo.utils.error_handler import ErrorHandler
            self._error_handler = ErrorHandler(self.__class__.__name__)
        return self._error_handler
    
    async def batch_execute(self, operations: list, batch_size: Optional[int] = None) -> list:
        """
        批量执行Redis操作
        
        Args:
            operations: 操作列表，每个操作是一个包含(command, *args)的元组
            batch_size: 批次大小（如果为None则使用实例的batch_size）
            
        Returns:
            执行结果列表
        """
        actual_batch_size = batch_size or self.batch_size
        results = []
        
        try:
            for i in range(0, len(operations), actual_batch_size):
                batch = operations[i:i + actual_batch_size]
                self.logger.debug(f"执行批次 {i//actual_batch_size + 1}/{(len(operations)-1)//actual_batch_size + 1}")
                
                try:
                    # 处理集群模式下的管道操作
                    if hasattr(self.redis_client, 'pipeline'):
                        pipe = self.redis_client.pipeline()
                        for operation in batch:
                            command, *args = operation
                            getattr(pipe, command)(*args)
                        
                        batch_results = await pipe.execute()
                        results.extend(batch_results)
                    else:
                        # 集群模式可能不支持跨slot的管道操作，逐个执行
                        batch_results = []
                        for operation in batch:
                            command, *args = operation
                            result = await getattr(self.redis_client, command)(*args)
                            batch_results.append(result)
                        results.extend(batch_results)
                    
                except Exception as e:
                    self.logger.error(f"执行批次失败: {e}")
                    # 继续执行下一个批次而不是中断
        
        except Exception as e:
            from crawlo.utils.error_handler import ErrorContext
            error_context = ErrorContext(context="Redis批量操作执行失败")
            self.error_handler.handle_error(
                e, 
                context=error_context, 
                raise_error=False
            )
        
        return results
    
    async def batch_set_hash(self, hash_key: str, items: Dict[str, Any]) -> int:
        """
        批量设置Hash字段
        
        Args:
            hash_key: Hash键名
            items: 要设置的字段字典
            
        Returns:
            成功设置的字段数量
        """
        try:
            if not items:
                return 0
            
            # 处理集群模式
            if hasattr(self.redis_client, 'pipeline'):
                pipe = self.redis_client.pipeline()
                count = 0
                
                for key, value in items.items():
                    pipe.hset(hash_key, key, value)
                    count += 1
                    
                    # 每达到批次大小就执行一次
                    if count % self.batch_size == 0:
                        await pipe.execute()
                        pipe = self.redis_client.pipeline()
                
                # 执行剩余的操作
                if count % self.batch_size != 0:
                    await pipe.execute()
            else:
                # 集群模式逐个执行
                count = 0
                batch_count = 0
                for key, value in items.items():
                    await self.redis_client.hset(hash_key, key, value)
                    count += 1
                    batch_count += 1
                    
                    # 每达到批次大小就暂停一下
                    if batch_count % self.batch_size == 0:
                        import asyncio
                        await asyncio.sleep(0.001)  # 避免过于频繁的请求
                        batch_count = 0
            
            self.logger.debug(f"批量设置Hash {count} 个字段")
            return count
            
        except Exception as e:
            from crawlo.utils.error_handler import ErrorContext
            error_context = ErrorContext(context="Redis批量设置Hash失败")
            self.error_handler.handle_error(
                e, 
                context=error_context, 
                raise_error=False
            )
            return 0
    
    async def batch_get_hash(self, hash_key: str, fields: list) -> Dict[str, Any]:
        """
        批量获取Hash字段值
        
        Args:
            hash_key: Hash键名
            fields: 要获取的字段列表
            
        Returns:
            字段值字典
        """
        try:
            if not fields:
                return {}
            
            # 处理集群模式
            if hasattr(self.redis_client, 'pipeline'):
                # 使用管道批量获取
                pipe = self.redis_client.pipeline()
                for field in fields:
                    pipe.hget(hash_key, field)
                
                results = await pipe.execute()
            else:
                # 集群模式逐个获取
                results = []
                for field in fields:
                    result = await self.redis_client.hget(hash_key, field)
                    results.append(result)
            
            # 构建结果字典
            result_dict = {}
            for i, field in enumerate(fields):
                if results[i] is not None:
                    result_dict[field] = results[i]
            
            self.logger.debug(f"批量获取Hash {len(result_dict)} 个字段")
            return result_dict
            
        except Exception as e:
            from crawlo.utils.error_handler import ErrorContext
            error_context = ErrorContext(context="Redis批量获取Hash失败")
            self.error_handler.handle_error(
                e, 
                context=error_context, 
                raise_error=False
            )
            return {}


# 全局连接池管理器
_connection_pools: Dict[str, RedisConnectionPool] = {}


def get_redis_pool(redis_url: str, is_cluster: bool = False, cluster_nodes: Optional[List[str]] = None, **kwargs) -> RedisConnectionPool:
    """
    获取Redis连接池实例（单例模式）
    
    Args:
        redis_url: Redis URL
        is_cluster: 是否为集群模式
        cluster_nodes: 集群节点列表
        **kwargs: 连接池配置参数
        
    Returns:
        Redis连接池实例
    """
    # 创建唯一标识符，包含集群相关信息
    pool_key = f"{redis_url}_{is_cluster}_{','.join(cluster_nodes) if cluster_nodes else ''}"
    
    if pool_key not in _connection_pools:
        _connection_pools[pool_key] = RedisConnectionPool(redis_url, is_cluster, cluster_nodes, **kwargs)
    
    return _connection_pools[pool_key]


async def close_all_pools():
    """关闭所有连接池"""
    import asyncio
    global _connection_pools
    
    from crawlo.logging import get_logger
    logger = get_logger('RedisConnectionPool')
    
    if not _connection_pools:
        logger.debug("No Redis connection pools to close")
        return
    
    logger.info(f"Closing {len(_connection_pools)} Redis connection pool(s)...")
    
    close_tasks = []
    for pool_key, pool in _connection_pools.items():
        try:
            close_tasks.append(pool.close())
        except Exception as e:
            logger.error(f"Error scheduling close for pool {pool_key}: {e}")
    
    # 并发关闭所有连接池
    if close_tasks:
        results = await asyncio.gather(*close_tasks, return_exceptions=True)
        
        # 检查结果
        error_count = sum(1 for r in results if isinstance(r, Exception))
        if error_count > 0:
            logger.warning(f"Failed to close {error_count} pool(s)")
        else:
            logger.info("All Redis connection pools closed successfully")
    
    _connection_pools.clear()
    logger.debug("Redis connection pools registry cleared")


# 便捷函数
async def execute_redis_batch(redis_url: str, operations: list, batch_size: int = 100, is_cluster: bool = False, cluster_nodes: Optional[List[str]] = None) -> list:
    """
    便捷函数：执行Redis批量操作
    
    Args:
        redis_url: Redis URL
        operations: 操作列表
        batch_size: 批次大小
        is_cluster: 是否为集群模式
        cluster_nodes: 集群节点列表
        
    Returns:
        执行结果列表
    """
    pool = get_redis_pool(redis_url, is_cluster, cluster_nodes)
    redis_client = await pool.get_connection()
    helper = RedisBatchOperationHelper(redis_client, batch_size)
    return await helper.batch_execute(operations)
```

**code file end: crawlo/utils/redis_connection_pool.py**

---


### code file start: crawlo/utils/redis_key_validator.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Redis Key 验证工具
=================
提供 Redis Key 命名规范的验证功能
"""
from typing import List, Tuple

from crawlo.logging import get_logger


class RedisKeyValidator:
    """Redis Key 验证器"""
    
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
    
    def validate_key_naming(self, key: str, project_name: str = None) -> bool:
        """
        验证Redis Key是否符合命名规范
        
        Args:
            key: Redis Key
            project_name: 项目名称（可选）
            
        Returns:
            bool: 是否符合命名规范
        """
        if not isinstance(key, str) or not key:
            return False
        
        # 检查是否以 crawlo: 开头
        if not key.startswith('crawlo:'):
            return False
        
        # 分割Key部分
        parts = key.split(':')
        if len(parts) < 3:
            return False
        
        # 检查基本结构
        if parts[0] != 'crawlo':
            return False
        
        # 如果提供了项目名称，检查是否匹配
        if project_name and parts[1] != project_name:
            return False
        
        # 检查组件类型
        valid_components = ['filter', 'queue', 'item']
        if parts[2] not in valid_components:
            return False
        
        # 检查子组件（根据组件类型）
        if parts[2] == 'queue':
            valid_subcomponents = ['requests', 'processing', 'failed']
            if len(parts) < 4 or parts[3] not in valid_subcomponents:
                return False
        elif parts[2] == 'filter':
            if len(parts) < 4 or parts[3] != 'fingerprint':
                return False
        elif parts[2] == 'item':
            if len(parts) < 4 or parts[3] != 'fingerprint':
                return False
        
        return True
    
    def validate_multiple_keys(self, keys: List[str], project_name: str = None) -> Tuple[bool, List[str]]:
        """
        验证多个Redis Key
        
        Args:
            keys: Redis Key列表
            project_name: 项目名称（可选）
            
        Returns:
            Tuple[bool, List[str]]: (是否全部有效, 无效的Key列表)
        """
        invalid_keys = []
        for key in keys:
            if not self.validate_key_naming(key, project_name):
                invalid_keys.append(key)
        
        return len(invalid_keys) == 0, invalid_keys
    
    def get_key_info(self, key: str) -> dict:
        """
        获取Redis Key的信息
        
        Args:
            key: Redis Key
            
        Returns:
            dict: Key信息
        """
        if not self.validate_key_naming(key):
            return {
                'valid': False,
                'error': 'Key不符合命名规范'
            }
        
        parts = key.split(':')
        info = {
            'valid': True,
            'framework': parts[0],
            'project': parts[1],
            'component': parts[2]
        }
        
        if parts[2] == 'queue' and len(parts) >= 4:
            info['sub_component'] = parts[3]
        elif len(parts) >= 4:
            info['sub_component'] = parts[3]
        
        return info


# 便利函数
def validate_redis_key_naming(key: str, project_name: str = None) -> bool:
    """
    验证Redis Key是否符合命名规范（便利函数）
    
    Args:
        key: Redis Key
        project_name: 项目名称（可选）
        
    Returns:
        bool: 是否符合命名规范
    """
    validator = RedisKeyValidator()
    return validator.validate_key_naming(key, project_name)


def validate_multiple_redis_keys(keys: List[str], project_name: str = None) -> Tuple[bool, List[str]]:
    """
    验证多个Redis Key（便利函数）
    
    Args:
        keys: Redis Key列表
        project_name: 项目名称（可选）
        
    Returns:
        Tuple[bool, List[str]]: (是否全部有效, 无效的Key列表)
    """
    validator = RedisKeyValidator()
    return validator.validate_multiple_keys(keys, project_name)


def get_redis_key_info(key: str) -> dict:
    """
    获取Redis Key的信息（便利函数）
    
    Args:
        key: Redis Key
        
    Returns:
        dict: Key信息
    """
    validator = RedisKeyValidator()
    return validator.get_key_info(key)


def print_validation_report(keys: List[str], project_name: str = None):
    """
    打印Redis Key验证报告
    
    Args:
        keys: Redis Key列表
        project_name: 项目名称（可选）
    """
    validator = RedisKeyValidator()
    is_valid, invalid_keys = validator.validate_multiple_keys(keys, project_name)
    
    print("=" * 50)
    print("Redis Key 命名规范验证报告")
    print("=" * 50)
    
    if is_valid:
        print("所有Redis Key命名规范验证通过")
    else:
        print("发现不符合命名规范的Redis Key:")
        for key in invalid_keys:
            print(f"  - {key}")
    
    print("\nKey 详细信息:")
    for key in keys:
        info = validator.get_key_info(key)
        if info['valid']:
            print(f"  {key}")
            print(f"     框架: {info['framework']}")
            print(f"     项目: {info['project']}")
            print(f"     组件: {info['component']}")
            if 'sub_component' in info:
                print(f"     子组件: {info['sub_component']}")
        else:
            print(f"  {key} - {info.get('error', '无效')}")
    
    print("=" * 50)
```

**code file end: crawlo/utils/redis_key_validator.py**

---


### code file start: crawlo/utils/request.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
# @Time    :    2025-07-08 08:55
# @Author  :   crawl-coder
# @Desc    :   None
"""
import importlib
import json
import hashlib
from typing import Any, Optional, Iterable, Union, Dict
from w3lib.url import canonicalize_url

from crawlo import Request


def to_bytes(data: Any, encoding: str = 'utf-8') -> bytes:
    """
    将各种类型统一转换为 bytes。

    Args:
        data: 要转换的数据，支持 str, bytes, dict, int, float, bool, None 等类型
        encoding: 字符串编码格式，默认为 'utf-8'

    Returns:
        bytes: 转换后的字节数据

    Raises:
        TypeError: 当数据类型无法转换时
        UnicodeEncodeError: 当编码失败时
        ValueError: 当 JSON 序列化失败时

    Examples:
        >>> to_bytes("hello")
        b'hello'
        >>> to_bytes({"key": "value"})
        b'{"key": "value"}'
        >>> to_bytes(123)
        b'123'
        >>> to_bytes(None)
        b'null'
    """
    # 预检查编码参数
    if not isinstance(encoding, str):
        raise TypeError(f"encoding must be str, not {type(encoding).__name__}")

    try:
        if isinstance(data, bytes):
            return data
        elif isinstance(data, str):
            return data.encode(encoding)
        elif isinstance(data, dict):
            return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode(encoding)
        elif isinstance(data, (int, float, bool)):
            return str(data).encode(encoding)
        elif data is None:
            return b'null'
        elif hasattr(data, '__str__'):
            # 处理其他可转换为字符串的对象
            return str(data).encode(encoding)
        else:
            raise TypeError(
                f"`data` must be str, dict, bytes, int, float, bool, or None, "
                f"not {type(data).__name__}"
            )
    except (UnicodeEncodeError, ValueError) as e:
        raise type(e)(f"Failed to convert {type(data).__name__} to bytes: {str(e)}") from e


def request_fingerprint(
        request: Request,
        include_headers: Optional[Iterable[Union[bytes, str]]] = None
) -> str:
    """
    生成请求指纹，基于方法、标准化 URL、body 和可选的 headers。
    
    .. deprecated:: 1.0.0
        此函数已废弃。请使用 :class:`crawlo.utils.fingerprint.FingerprintGenerator` 代替:
        
        .. code-block:: python
        
            from crawlo.utils.fingerprint import FingerprintGenerator
            
            fp = FingerprintGenerator.request_fingerprint(
                method=request.method,
                url=request.url,
                body=request.body or b'',
                headers=dict(request.headers) if hasattr(request, 'headers') else {}
            )
    
    此函数保留仅为向后兼容，将在 2.0.0 版本中移除。
    
    :param request: Request 对象（需包含 method, url, body, headers）
    :param include_headers: 指定要参与指纹计算的 header 名称列表（str 或 bytes）
    :return: 请求指纹（hex string）
    """
    import warnings
    warnings.warn(
        "request_fingerprint() is deprecated. "
        "Use FingerprintGenerator.request_fingerprint() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    from crawlo.utils.fingerprint import FingerprintGenerator
    
    # 准备请求数据
    method = request.method
    url = request.url
    body = request.body or b''
    headers = None
    
    # 处理 headers
    if include_headers and hasattr(request, 'headers'):
        headers = {}
        for header_name in include_headers:
            name_str = str(header_name).lower()  # 统一转为小写进行匹配
            value = ''

            # 兼容 headers 的访问方式（如 MultiDict 或 dict）
            if hasattr(request.headers, 'get_all'):
                # 如 scrapy.http.Headers 的 get_all 方法
                values = request.headers.get_all(name_str)
                value = ';'.join(str(v) for v in values) if values else ''
            elif hasattr(request.headers, '__getitem__'):
                # 如普通 dict
                try:
                    raw_value = request.headers[name_str]
                    if isinstance(raw_value, list):
                        value = ';'.join(str(v) for v in raw_value)
                    else:
                        value = str(raw_value)
                except (KeyError, TypeError):
                    value = ''
            else:
                value = ''
            
            headers[name_str] = value
    
    # 使用统一的指纹生成器
    return FingerprintGenerator.request_fingerprint(method, url, body, headers)


def set_request(request: Request, priority: int) -> None:
    """
    设置请求的深度和优先级
    
    :param request: Request 对象
    :param priority: 优先级值
    """
    # 增加请求深度
    request.meta['depth'] = request.meta.setdefault('depth', 0) + 1
    
    # 根据深度调整优先级，深度越深优先级越低
    if priority:
        request.priority -= request.meta['depth'] * priority


def request_to_dict(request: Request, spider=None) -> Dict[str, Any]:
    """
    将 Request 对象转换为可 JSON 序列化的字典，用于分布式爬虫中的请求序列化。

    Args:
        request: 要序列化的 Request 对象
        spider: 可选，用于辅助序列化（如回调函数的归属）

    Returns:
        包含 Request 所有关键信息的字典
    """
    # 基础属性
    d = {
        'url': request.url,
        'method': request.method,
        'headers': dict(request.headers),
        'body': request.body,
        'meta': request.meta.copy(),  # 复制一份
        'flags': request.flags.copy(),
        'cb_kwargs': request.cb_kwargs.copy(),
    }

    # 1. 处理 callback
    #    不能直接序列化函数，所以存储其路径
    if callable(getattr(request, 'callback', None)):
        d['_callback'] = _get_function_path(request.callback)

    # 2. 处理 errback
    if callable(getattr(request, 'err_back', None)):
        d['_errback'] = _get_function_path(request.err_back)

    # 3. 记录原始类名，以便反序列化时创建正确的实例
    d['_class'] = request.__class__.__module__ + '.' + request.__class__.__name__

    return d


def request_from_dict(d: Dict[str, Any], spider=None) -> Request:
    """
    从字典重建 Request 对象，用于分布式爬虫中的请求反序列化。

    Args:
        d: 由 request_to_dict 生成的字典
        spider: 可选，用于解析回调函数

    Returns:
        重建的 Request 对象
    """
    # 1. 获取类名并动态导入
    cls_path = d.pop('_class', None)
    if cls_path:
        module_path, cls_name = cls_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        cls = getattr(module, cls_name)
    else:
        cls = Request  # 默认为 Request

    # 2. 提取回调函数
    callback_path = d.pop('_callback', None)
    callback = _get_function_from_path(callback_path, spider) if callback_path else None

    # 3. 提取错误回调
    errback_path = d.pop('_errback', None)
    errback = _get_function_from_path(errback_path, spider) if errback_path else None

    # 5. 创建 Request 实例
    request = cls(
        url=d['url'],
        method=d.get('method', 'GET'),
        headers=d.get('headers', {}),
        body=d.get('body'),
        callback=callback,
        meta=d.get('meta', {}),
        flags=d.get('flags', []),
        cb_kwargs=d.get('cb_kwargs', {}),
    )
    
    # 手动设置 err_back 属性
    if errback is not None:
        request.err_back = errback

    return request


def _get_function_path(func: callable) -> str:
    """
    获取函数的模块路径，如 'myproject.spiders.my_spider.parse'
    """
    if hasattr(func, '__wrapped__'):
        # 处理被装饰的函数
        func = func.__wrapped__
    module = func.__module__
    if module is None or module == str.__class__.__module__:
        raise ValueError(f"无法序列化内置函数或lambda: {func}")
    return f"{module}.{func.__qualname__}"


def _get_function_from_path(path: str, spider=None) -> Optional[callable]:
    """
    从路径字符串获取函数对象。
    如果函数是 spider 的方法，会尝试绑定到 spider 实例。
    """
    try:
        module_path, func_name = path.rsplit('.', 1)
        module = importlib.import_module(module_path)

        # 逐级获取属性，支持 nested functions
        func = module
        for attr in func_name.split('.'):
            func = getattr(func, attr)

        # 如果 spider 存在，并且 func 是 spider 的方法
        if spider and hasattr(func, '__name__') and hasattr(spider, func.__name__):
            spider_method = getattr(spider, func.__name__)
            if spider_method is func:
                return spider_method  # 返回绑定的方法

        return func
    except Exception as e:
        raise ValueError(f"无法从路径 '{path}' 加载函数: {e}")


```

**code file end: crawlo/utils/request.py**

---


### code file start: crawlo/utils/request_serializer.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Request 序列化工具类
负责处理 Request 对象的序列化前清理工作，解决 logger 等不可序列化对象的问题
"""
import gc
import logging
import pickle

from crawlo.logging import get_logger


class RequestSerializer:
    """Request 序列化工具类"""
    
    def __init__(self):
        # 延迟初始化logger避免循环依赖
        self._logger = None
    
    @property
    def logger(self):
        if self._logger is None:
            self._logger = get_logger(self.__class__.__name__)
        return self._logger
    
    def prepare_for_serialization(self, request):
        """
        为序列化准备 Request 对象
        移除不可序列化的属性，保存必要信息用于恢复
        """
        try:
            # 处理 callback
            self._handle_callback(request)
            
            # 清理 meta 中的 logger
            if hasattr(request, 'meta') and request.meta:
                self._clean_dict_recursive(request.meta)
            
            # 清理 cb_kwargs 中的 logger
            if hasattr(request, 'cb_kwargs') and request.cb_kwargs:
                self._clean_dict_recursive(request.cb_kwargs)
            
            # 清理其他可能的 logger 引用
            for attr_name in ['headers', 'cookies']:
                if hasattr(request, attr_name):
                    attr_value = getattr(request, attr_name)
                    if isinstance(attr_value, dict):
                        self._clean_dict_recursive(attr_value)
            
            # 最终验证
            if not self._test_serialization(request):
                self.logger.warning("常规清理无效，使用深度清理")
                request = self._deep_clean_request(request)
                
            return request
            
        except Exception as e:
            self.logger.error(f"Request 序列化准备失败: {e}")
            # 最后的保险：重建 Request
            return self._rebuild_clean_request(request)
    
    def restore_after_deserialization(self, request, spider=None):
        """
        反序列化后恢复 Request 对象
        恢复 callback 等必要信息
        """
        if not request:
            return request
            
        # 恢复 callback
        if hasattr(request, 'meta') and '_callback_info' in request.meta:
            callback_info = request.meta.pop('_callback_info')
            
            if spider:
                spider_class_name = callback_info.get('spider_class')
                method_name = callback_info.get('method_name')
                
                if (spider.__class__.__name__ == spider_class_name and 
                    hasattr(spider, method_name)):
                    request.callback = getattr(spider, method_name)
                    
                    # 确保 spider 有有效的 logger
                    if not hasattr(spider, 'logger') or spider.logger is None:
                        spider.logger = get_logger(spider.name or spider.__class__.__name__)
        
        return request
    
    def _handle_callback(self, request):
        """处理 callback 相关的清理"""
        if hasattr(request, 'callback') and request.callback is not None:
            callback = request.callback
            
            # 如果是绑定方法，保存信息并移除引用
            if hasattr(callback, '__self__') and hasattr(callback, '__name__'):
                spider_instance = callback.__self__
                
                # 保存 callback 信息
                if not hasattr(request, 'meta') or request.meta is None:
                    request.meta = {}
                request.meta['_callback_info'] = {
                    'spider_class': spider_instance.__class__.__name__,
                    'method_name': callback.__name__
                }
                
                # 移除 callback 引用
                request.callback = None
    
    def _clean_dict_recursive(self, data, depth=0):
        """递归清理字典中的 logger"""
        if depth > 5 or not isinstance(data, dict):
            return
        
        keys_to_remove = []
        for key, value in list(data.items()):
            if isinstance(value, logging.Logger):
                keys_to_remove.append(key)
            elif isinstance(key, str) and 'logger' in key.lower():
                keys_to_remove.append(key)
            elif isinstance(value, dict):
                self._clean_dict_recursive(value, depth + 1)
            elif isinstance(value, (list, tuple)):
                for item in value:
                    if isinstance(item, dict):
                        self._clean_dict_recursive(item, depth + 1)
        
        for key in keys_to_remove:
            data.pop(key, None)
    
    def _test_serialization(self, request):
        """测试是否可以序列化"""
        try:
            pickle.dumps(request)
            return True
        except Exception:
            return False
    
    def _deep_clean_request(self, request):
        """深度清理 Request 对象"""
        import logging
        
        def recursive_clean(target, visited=None, depth=0):
            if depth > 5 or not target:
                return
            if visited is None:
                visited = set()
                
            obj_id = id(target)
            if obj_id in visited:
                return
            visited.add(obj_id)
            
            # 处理对象属性
            if hasattr(target, '__dict__'):
                attrs_to_clean = []
                for attr_name, attr_value in list(target.__dict__.items()):
                    if isinstance(attr_value, logging.Logger):
                        attrs_to_clean.append(attr_name)
                    elif isinstance(attr_name, str) and 'logger' in attr_name.lower():
                        attrs_to_clean.append(attr_name)
                    elif hasattr(attr_value, '__dict__'):
                        recursive_clean(attr_value, visited, depth + 1)
                
                for attr_name in attrs_to_clean:
                    try:
                        setattr(target, attr_name, None)
                    except (AttributeError, TypeError):
                        pass
            
            # 处理字典
            elif isinstance(target, dict):
                self._clean_dict_recursive(target, depth)
        
        recursive_clean(request)
        gc.collect()
        return request
    
    def _rebuild_clean_request(self, original_request):
        """重建一个干净的 Request 对象"""
        from crawlo.network.request import Request
        
        try:
            # 提取安全的属性
            safe_meta = {}
            if hasattr(original_request, 'meta') and original_request.meta:
                for key, value in original_request.meta.items():
                    if not isinstance(value, logging.Logger):
                        try:
                            pickle.dumps(value)
                            safe_meta[key] = value
                        except Exception:
                            try:
                                safe_meta[key] = str(value)
                            except Exception:
                                continue
            
            # 安全地获取其他属性
            safe_headers = {}
            if hasattr(original_request, 'headers') and original_request.headers:
                for k, v in original_request.headers.items():
                    try:
                        safe_headers[str(k)] = str(v)
                    except Exception:
                        continue
            
            # 创建干净的 Request
            clean_request = Request(
                url=str(original_request.url),
                method=getattr(original_request, 'method', 'GET'),
                headers=safe_headers,
                meta=safe_meta,
                priority=-getattr(original_request, 'priority', 0),
                dont_filter=getattr(original_request, 'dont_filter', False),
                timeout=getattr(original_request, 'timeout', None),
                encoding=getattr(original_request, 'encoding', 'utf-8')
            )
            
            # 验证新 Request 可以序列化
            pickle.dumps(clean_request)
            return clean_request
            
        except Exception as e:
            self.logger.error(f"重建 Request 失败: {e}")
            # 最简单的 fallback
            from crawlo.network.request import Request
            return Request(url=str(original_request.url))
```

**code file end: crawlo/utils/request_serializer.py**

---


### code file start: crawlo/utils/resource_manager.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
资源管理器 - 统一管理所有可清理资源
========================================

功能特性：
- 统一注册和清理资源
- 支持异步资源清理
- 资源泄露检测
- 清理顺序保证（LIFO）
"""
import asyncio
import time
import traceback
from typing import Any, Callable, List, Tuple, Optional, Dict
from enum import Enum

from crawlo.logging import get_logger


class ResourceType(Enum):
    """资源类型枚举"""
    DOWNLOADER = "downloader"
    REDIS_POOL = "redis_pool"
    QUEUE = "queue"
    FILTER = "filter"
    PIPELINE = "pipeline"
    MIDDLEWARE = "middleware"
    EXTENSION = "extension"
    SESSION = "session"
    BROWSER = "browser"
    OTHER = "other"


class ResourceStatus(Enum):
    """资源状态"""
    ACTIVE = "active"
    CLOSING = "closing"
    CLOSED = "closed"
    ERROR = "error"


class ManagedResource:
    """托管资源"""
    
    def __init__(self, 
                 resource: Any,
                 cleanup_func: Callable,
                 resource_type: ResourceType = ResourceType.OTHER,
                 name: Optional[str] = None):
        self.resource = resource
        self.cleanup_func = cleanup_func
        self.resource_type = resource_type
        self.name = name or f"{resource_type.value}_{id(resource)}"
        self.status = ResourceStatus.ACTIVE
        self.created_at = time.time()
        self.closed_at: Optional[float] = None
    
    async def cleanup(self) -> bool:
        """清理资源"""
        if self.status == ResourceStatus.CLOSED:
            return True
        
        self.status = ResourceStatus.CLOSING
        try:
            # 检查cleanup_func是否为异步函数
            if asyncio.iscoroutinefunction(self.cleanup_func):
                await self.cleanup_func(self.resource)
            else:
                # 同步函数，直接调用
                result = self.cleanup_func(self.resource)
                # 如果返回的是协程，则await
                if asyncio.iscoroutine(result):
                    await result
            
            self.status = ResourceStatus.CLOSED
            self.closed_at = time.time()
            return True
        except Exception as e:
            self.status = ResourceStatus.ERROR
            raise e
    
    def get_lifetime(self) -> float:
        """获取资源生命周期（秒）"""
        end_time = self.closed_at or time.time()
        return end_time - self.created_at


class ResourceManager:
    """
    资源管理器 - 统一管理所有可清理资源
    
    特性：
    1. 自动跟踪注册的资源
    2. 保证清理顺序（LIFO - 后进先出）
    3. 容错清理（一个失败不影响其他）
    4. 资源泄露检测
    5. 统计和监控
    """
    
    def __init__(self, name: str = "default"):
        self.name = name
        self._resources: List[ManagedResource] = []
        self._lock = asyncio.Lock()
        self._cleanup_errors: List[Tuple[str, Exception]] = []
        self._logger = get_logger(f"ResourceManager.{name}")
        
        # 统计信息
        self._stats = {
            'total_registered': 0,
            'total_cleaned': 0,
            'total_errors': 0,
            'active_resources': 0,
        }
    
    def register(self,
                 resource: Any,
                 cleanup_func: Callable,
                 resource_type: ResourceType = ResourceType.OTHER,
                 name: Optional[str] = None) -> ManagedResource:
        """
        注册需要清理的资源
        
        Args:
            resource: 资源对象
            cleanup_func: 清理函数（同步或异步）
            resource_type: 资源类型
            name: 资源名称（用于日志）
        
        Returns:
            托管资源对象
        """
        managed = ManagedResource(resource, cleanup_func, resource_type, name)
        self._resources.append(managed)
        self._stats['total_registered'] += 1
        self._stats['active_resources'] += 1
        
        self._logger.debug(f"Resource registered: {managed.name} ({resource_type.value})")
        return managed
    
    async def cleanup_all(self, reverse: bool = True) -> Dict[str, Any]:
        """
        清理所有注册的资源
        
        Args:
            reverse: 是否反向清理（LIFO，推荐）
        
        Returns:
            清理结果统计
        """
        async with self._lock:
            if not self._resources:
                self._logger.debug("No resources to cleanup")
                return self._get_cleanup_stats()
            
            self._logger.info(f"Starting cleanup of {len(self._resources)} resources...")
            
            # 反向清理（后创建的先清理）
            resources = reversed(self._resources) if reverse else self._resources
            
            cleanup_start = time.time()
            success_count = 0
            error_count = 0
            
            for managed in resources:
                try:
                    self._logger.debug(f"Cleaning up: {managed.name}")
                    await managed.cleanup()
                    success_count += 1
                    self._stats['total_cleaned'] += 1
                    self._stats['active_resources'] -= 1
                except Exception as e:
                    error_count += 1
                    self._stats['total_errors'] += 1
                    self._cleanup_errors.append((managed.name, e))
                    self._logger.error(
                        f"Failed to cleanup {managed.name}: {e}",
                        exc_info=True
                    )
                    # 继续清理其他资源，不中断
            
            cleanup_duration = time.time() - cleanup_start
            
            # 清空资源列表
            self._resources.clear()
            
            result = {
                'success': success_count,
                'errors': error_count,
                'duration': cleanup_duration,
                'total_resources': success_count + error_count,
            }
            
            if error_count > 0:
                self._logger.warning(
                    f"Cleanup completed with errors: {success_count} success, "
                    f"{error_count} errors in {cleanup_duration:.2f}s"
                )
            else:
                self._logger.info(
                    f"Cleanup completed successfully: {success_count} resources "
                    f"in {cleanup_duration:.2f}s"
                )
            
            return result
    
    async def cleanup_by_type(self, resource_type: ResourceType) -> int:
        """
        按类型清理资源
        
        Args:
            resource_type: 资源类型
        
        Returns:
            清理的资源数量
        """
        async with self._lock:
            to_cleanup = [r for r in self._resources if r.resource_type == resource_type]
            
            if not to_cleanup:
                return 0
            
            cleaned = 0
            for managed in reversed(to_cleanup):
                try:
                    await managed.cleanup()
                    self._resources.remove(managed)
                    cleaned += 1
                    self._stats['total_cleaned'] += 1
                    self._stats['active_resources'] -= 1
                except Exception as e:
                    self._logger.error(f"Failed to cleanup {managed.name}: {e}")
                    self._stats['total_errors'] += 1
            
            return cleaned
    
    def get_active_resources(self) -> List[ManagedResource]:
        """获取所有活跃资源"""
        return [r for r in self._resources if r.status == ResourceStatus.ACTIVE]
    
    def get_resources_by_type(self, resource_type: ResourceType) -> List[ManagedResource]:
        """按类型获取资源"""
        return [r for r in self._resources if r.resource_type == resource_type]
    
    def detect_leaks(self, max_lifetime: float = 3600) -> List[ManagedResource]:
        """
        检测可能的资源泄露
        
        Args:
            max_lifetime: 最大生命周期（秒），超过此时间未清理视为泄露
        
        Returns:
            可能泄露的资源列表
        """
        current_time = time.time()
        leaks = []
        
        for managed in self._resources:
            if managed.status == ResourceStatus.ACTIVE:
                lifetime = current_time - managed.created_at
                if lifetime > max_lifetime:
                    leaks.append(managed)
                    self._logger.warning(
                        f"Potential leak detected: {managed.name} "
                        f"(lifetime: {lifetime:.2f}s)"
                    )
        
        return leaks
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        return {
            **self._stats,
            'cleanup_errors': len(self._cleanup_errors),
            'active_by_type': self._get_active_by_type(),
        }
    
    def _get_active_by_type(self) -> Dict[str, int]:
        """按类型统计活跃资源"""
        result = {}
        for managed in self._resources:
            if managed.status == ResourceStatus.ACTIVE:
                type_name = managed.resource_type.value
                result[type_name] = result.get(type_name, 0) + 1
        return result
    
    def _get_cleanup_stats(self) -> Dict[str, Any]:
        """获取清理统计"""
        return {
            'success': 0,
            'errors': 0,
            'duration': 0.0,
            'total_resources': 0,
        }
    
    async def __aenter__(self):
        """上下文管理器入口"""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出，自动清理"""
        await self.cleanup_all()
        return False


# 全局资源管理器注册表
_global_managers: Dict[str, ResourceManager] = {}


def get_resource_manager(name: str = "default") -> ResourceManager:
    """
    获取资源管理器实例（单例）
    
    Args:
        name: 管理器名称
    
    Returns:
        资源管理器实例
    """
    if name not in _global_managers:
        _global_managers[name] = ResourceManager(name)
    return _global_managers[name]


async def cleanup_all_managers():
    """清理所有资源管理器"""
    logger = get_logger("ResourceManager")
    
    for name, manager in _global_managers.items():
        try:
            logger.info(f"Cleaning up resource manager: {name}")
            await manager.cleanup_all()
        except Exception as e:
            logger.error(f"Failed to cleanup manager {name}: {e}")
    
    _global_managers.clear()

```

**code file end: crawlo/utils/resource_manager.py**

---


### code file start: crawlo/utils/selector_helper.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
选择器辅助工具模块
==================
提供用于处理parsel选择器的辅助函数，用于提取文本和属性等操作。

该模块包含以下主要函数：
- extract_text: 从元素列表中提取文本并拼接
- extract_texts: 从元素列表中提取多个文本列表
- extract_attr: 从元素列表中提取单个元素的属性值
- extract_attrs: 从元素列表中提取多个元素的属性值列表
- is_xpath: 判断查询语句是否为XPath

所有方法都采用了简洁直观的命名风格，便于记忆和使用。
"""

from typing import List, Any, Optional
from parsel import Selector, SelectorList


def extract_text(elements: SelectorList, join_str: str = " ") -> str:
    """
    从元素列表中提取文本并拼接
    
    :param elements: SelectorList元素列表
    :param join_str: 文本拼接分隔符
    :return: 拼接后的文本
    
    示例:
        title_elements = selector.css('title')
        title_text = extract_text(title_elements)
    """
    texts = []
    for element in elements:
        # 获取元素的所有文本节点
        if hasattr(element, 'xpath'):
            element_texts = element.xpath('.//text()').getall()
        else:
            element_texts = [str(element)]
        # 清理并添加非空文本
        for text in element_texts:
            cleaned = text.strip()
            if cleaned:
                texts.append(cleaned)
    return join_str.join(texts)


def extract_texts(elements: SelectorList, join_str: str = " ") -> List[str]:
    """
    从元素列表中提取多个文本列表
    
    :param elements: SelectorList元素列表
    :param join_str: 单个节点内文本拼接分隔符
    :return: 纯文本列表(每个元素对应一个节点的文本)
    
    示例:
        li_elements = selector.css('.list li')
        li_texts = extract_texts(li_elements)
    """
    result = []
    for element in elements:
        # 对每个元素提取文本
        if hasattr(element, 'xpath'):
            texts = element.xpath('.//text()').getall()
        else:
            texts = [str(element)]
            
        # 清理文本并拼接
        clean_texts = [text.strip() for text in texts if text.strip()]
        if clean_texts:
            result.append(join_str.join(clean_texts))
            
    return result


def extract_attr(elements: SelectorList, attr_name: str, default: Any = None) -> Any:
    """
    从元素列表中提取单个元素的属性值
    
    :param elements: SelectorList元素列表
    :param attr_name: 属性名称
    :param default: 默认返回值
    :return: 属性值或默认值
    
    示例:
        link_elements = selector.css('.link')
        link_href = extract_attr(link_elements, 'href')
    """
    # 使用parsel的attrib属性获取第一个匹配元素的属性值
    if hasattr(elements, 'attrib'):
        return elements.attrib.get(attr_name, default)
    # 如果elements是SelectorList，获取第一个元素的属性
    elif len(elements) > 0 and hasattr(elements[0], 'attrib'):
        return elements[0].attrib.get(attr_name, default)
    return default


def extract_attrs(elements: SelectorList, attr_name: str) -> List[Any]:
    """
    从元素列表中提取多个元素的属性值列表
    
    :param elements: SelectorList元素列表
    :param attr_name: 属性名称
    :return: 属性值列表
    
    示例:
        all_links = selector.css('a')
        all_hrefs = extract_attrs(all_links, 'href')
    """
    result = []
    for element in elements:
        # 使用parsel的attrib属性获取元素的属性值
        if hasattr(element, 'attrib'):
            attr_value = element.attrib.get(attr_name)
            if attr_value is not None:
                result.append(attr_value)
                
    return result


def is_xpath(query: str) -> bool:
    """
    判断查询语句是否为XPath
    
    :param query: 查询语句
    :return: 是否为XPath
    """
    return query.startswith(('/', '//', './'))


__all__ = [
    "extract_text",
    "extract_texts",
    "extract_attr",
    "extract_attrs",
    "is_xpath"
]
```

**code file end: crawlo/utils/selector_helper.py**

---


### code file start: crawlo/utils/singleton.py 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
单例模式工具模块
================

提供同步和异步两种单例实现方式，适用于不同的使用场景。

使用场景：
1. 同步单例：用于框架初始化、配置管理等同步代码
2. 异步单例：用于数据库连接池、网络资源等异步代码

示例：
    # 同步单例
    @singleton
    class CoreInitializer:
        pass
    
    # 异步单例（在连接池管理器中使用）
    class MySQLConnectionPoolManager:
        _instances: Dict[str, 'MySQLConnectionPoolManager'] = {}
        _lock = asyncio.Lock()
        
        @classmethod
        async def get_pool(cls, ...):
            async with cls._lock:
                if pool_key not in cls._instances:
                    cls._instances[pool_key] = cls(pool_key)
            return cls._instances[pool_key].pool
"""

import threading
from typing import Any, Dict, Type


class SingletonMeta(type):
    """单例元类"""
    _instances: Dict[Type, Any] = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


def singleton(cls):
    """
    单例装饰器
    
    Args:
        cls: 要装饰的类
        
    Returns:
        装饰后的类，确保只有一个实例
    """
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
```

**code file end: crawlo/utils/singleton.py**

---


### code file start: crawlo/utils/spider_loader.py 

```python
import importlib
import traceback
import warnings
from collections import defaultdict
from pathlib import Path
from typing import List, Type, Dict, Any

from crawlo.interfaces import ISpiderLoader
from crawlo.settings.setting_manager import SettingManager
from crawlo.spider import Spider
from crawlo.network.request import Request
from crawlo.logging import get_logger

logger = get_logger(__name__)


class SpiderLoaderProtocol:
    """Protocol for spider loader"""
    
    @classmethod
    def from_settings(cls, settings: SettingManager) -> 'SpiderLoaderProtocol':
        """Create spider loader from settings"""
        return cls(settings)
    
    def load(self, spider_name: str) -> Type[Spider]:
        """Load a spider by name"""
        raise NotImplementedError
    
    def list(self) -> List[str]:
        """List all available spider names"""
        raise NotImplementedError
    
    def find_by_request(self, request: 'Request') -> List[str]:
        """Find spider names that can handle the given request"""
        raise NotImplementedError


class SpiderLoader(ISpiderLoader):
    """爬虫加载器，负责发现和加载爬虫"""
    
    def __init__(self, settings: SettingManager = None):
        # 如果提供了settings，则从settings中获取配置
        if settings is not None:
            self.spider_modules = settings.get('SPIDER_MODULES', [])
            self.warn_only = settings.get('SPIDER_LOADER_WARN_ONLY', False)
        else:
            # 默认配置
            self.spider_modules = []
            self.warn_only = False
            
        self._spiders: Dict[str, Type[Spider]] = {}
        self._found: Dict[str, List[tuple]] = defaultdict(list)
        self._load_all_spiders()
    
    @classmethod
    def from_settings(cls, settings: SettingManager) -> 'SpiderLoader':
        """从设置创建SpiderLoader实例"""
        return cls(settings)
    
    def _check_name_duplicates(self) -> None:
        """检查重复的spider名称"""
        dupes = []
        for name, locations in self._found.items():
            if len(locations) > 1:
                dupes.extend([
                    f"  {cls} named {name!r} (in {mod})"
                    for mod, cls in locations
                ])
        
        if dupes:
            dupes_string = "\n\n".join(dupes)
            warnings.warn(
                "There are several spiders with the same name:\n\n"
                f"{dupes_string}\n\n  This can cause unexpected behavior.",
                category=UserWarning,
            )
    
    def _load_spiders(self, module) -> None:
        """加载模块中的所有spider"""
        for attr_name in dir(module):
            attr_value = getattr(module, attr_name)
            if (isinstance(attr_value, type) and
                    issubclass(attr_value, Spider) and
                    attr_value != Spider and
                    hasattr(attr_value, 'name')):
                
                spider_name = getattr(attr_value, 'name')
                self._found[spider_name].append((module.__name__, attr_value.__name__))
                self._spiders[spider_name] = attr_value
    
    def _load_spiders_from_package(self, package_name: str) -> None:
        """从包中加载spiders"""
        try:
            # 尝试导入包
            package = importlib.import_module(package_name)
            
            # 遍历包中的所有模块
            package_path = Path(package.__file__).parent
            for py_file in package_path.glob("*.py"):
                if py_file.name.startswith('_'):
                    continue
                
                module_name = py_file.stem
                spider_module_path = f"{package_name}.{module_name}"
                
                try:
                    module = importlib.import_module(spider_module_path)
                    self._load_spiders(module)
                except ImportError as e:
                    if self.warn_only:
                        logger.warning(f"Could not load spiders from module '{spider_module_path}': {e}")
                        logger.debug(traceback.format_exc())
                    else:
                        raise
        except (ImportError, SyntaxError) as e:
            if self.warn_only:
                logger.warning(f"Could not load spiders from package '{package_name}': {e}")
                logger.debug(traceback.format_exc())
            else:
                raise
    
    def _load_all_spiders(self) -> None:
        """加载所有spiders"""
        # 如果配置了SPIDER_MODULES，则从这些模块加载
        if self.spider_modules:
            for module_name in self.spider_modules:
                self._load_spiders_from_package(module_name)
        else:
            # 向后兼容：如果没有配置SPIDER_MODULES，则使用旧的方式
            # 这里假设默认的spiders目录结构
            spiders_dir = Path.cwd() / 'spiders'
            if not spiders_dir.exists():
                spiders_dir = Path.cwd() / 'spider'
                if not spiders_dir.exists():
                    logger.warning("Spiders directory not found")
                    return
            
            for py_file in spiders_dir.glob("*.py"):
                if py_file.name.startswith('_'):
                    continue
                
                module_name = py_file.stem
                module = None
                try:
                    # 尝试不同的导入路径
                    spider_module_path = None
                    for possible_package in ['spiders', 'spider']:
                        try:
                            spider_module_path = f"{possible_package}.{module_name}"
                            module = importlib.import_module(spider_module_path)
                            break
                        except ImportError:
                            continue
                    
                    if module is None:
                        raise ImportError(f"Could not import {module_name}")
                    
                    self._load_spiders(module)
                except ImportError as e:
                    logger.debug(f"Skip module {module_name}: {e}")
                    continue
        
        self._check_name_duplicates()
    
    def load(self, spider_name: str) -> Type[Spider]:
        """
        通过name加载爬虫
        
        Args:
            spider_name: 爬虫名称
            
        Returns:
            Spider类
            
        Raises:
            KeyError: 如果找不到指定名称的爬虫
        """
        if spider_name not in self._spiders:
            raise KeyError(f"Spider not found: {spider_name}")
        return self._spiders[spider_name]
    
    def list(self) -> List[str]:
        """列出所有可用的爬虫名称"""
        return list(self._spiders.keys())
    
    def find_by_request(self, request: 'Request') -> List[str]:
        """
        根据请求找到可以处理该请求的爬虫名称
        
        Args:
            request: 请求对象
            
        Returns:
            可以处理该请求的爬虫名称列表
        """
        # 这里可以实现更复杂的匹配逻辑
        # 目前只是返回所有爬虫名称
        return list(self._spiders.keys())
    
    def get_all(self) -> Dict[str, Type[Spider]]:
        """获取所有爬虫"""
        return self._spiders.copy()
```

**code file end: crawlo/utils/spider_loader.py**

---


### code file start: crawlo/utils/text_helper.py 

```python
# -*- coding: utf-8 -*-
import json
import re
from typing import Any, Union, List, Dict, Tuple, Optional

from crawlo.logging import get_logger

logger = get_logger(__name__)

# 正则表达式缓存
_REGEXPS: Dict[str, "re.Pattern"] = {}


def extract_text_by_regex(
    text: Union[str, Any],
    patterns: Union[str, List[str]],
    allow_repeat: bool = True,
    fetch_one: bool = False,
    join_with: Optional[str] = None,
) -> Union[str, List[str], Tuple]:
    """
    从文本中提取信息，支持正则匹配和多模式 fallback。

    Args:
        text (str): 文本内容或可转为字符串的类型
        patterns (str or list of str): 正则表达式模式，按顺序尝试匹配
        allow_repeat (bool): 是否允许重复结果
        fetch_one (bool): 是否只提取第一个匹配项（返回元组）
        join_with (str, optional): 若提供，则将结果用该字符连接成字符串

    Returns:
        str | list | tuple: 匹配结果，根据参数返回字符串、列表或元组
    """
    if isinstance(patterns, str):
        patterns = [patterns]

    results = []
    for pattern in patterns:
        if not pattern:
            continue

        if pattern not in _REGEXPS:
            _REGEXPS[pattern] = re.compile(pattern, re.S)

        if fetch_one:
            match = _REGEXPS[pattern].search(str(text))
            results = match.groups() if match else ("",)
            break
        else:
            found = _REGEXPS[pattern].findall(str(text))
            if found:
                results = found
                break

    if fetch_one:
        return results[0] if len(results) == 1 else results

    if not allow_repeat:
        results = sorted(set(results), key=results.index)

    return join_with.join(results) if join_with else results


def parse_json_safely(json_str: Union[str, Any]) -> Dict:
    """
    安全解析 JSON 字符串，兼容非标准格式（如单引号、缺少引号键）。

    Args:
        json_str (str): JSON 字符串

    Returns:
        dict: 解析后的字典，失败返回空字典
    """
    if not json_str:
        return {}

    try:
        return json.loads(json_str)
    except Exception as e1:
        try:
            cleaned = json_str.strip().replace("'", '"')
            # 使用新的函数名
            keys = extract_text_by_regex(cleaned, r'(\w+):')
            for key in keys:
                cleaned = cleaned.replace(f"{key}:", f'"{key}":')
            return json.loads(cleaned) if cleaned else {}
        except Exception as e2:
            logger.error(
                f"JSON 解析失败\n"
                f"原始内容: {json_str}\n"
                f"错误1: {e1}\n"
                f"修复后: {cleaned}\n"
                f"错误2: {e2}"
            )
        return {}
```

**code file end: crawlo/utils/text_helper.py**

---


### code file start: crawlo/utils/url_utils.py 

```python
from urllib.parse import urldefrag
from w3lib.url import add_or_replace_parameter


def escape_ajax(url: str) -> str:
    """
    根据Google AJAX爬取规范转换URL（处理哈希片段#!）：
    https://developers.google.com/webmasters/ajax-crawling/docs/getting-started

    规则说明：
    1. 仅当URL包含 `#!` 时才转换（表示这是AJAX可爬取页面）
    2. 将 `#!key=value` 转换为 `?_escaped_fragment_=key%3Dvalue`
    3. 保留原始查询参数（如果有）

    示例：
    >>> escape_ajax("www.example.com/ajax.html#!key=value")
    'www.example.com/ajax.html?_escaped_fragment_=key%3Dvalue'
    >>> escape_ajax("www.example.com/ajax.html?k1=v1#!key=value")
    'www.example.com/ajax.html?k1=v1&_escaped_fragment_=key%3Dvalue'
    >>> escape_ajax("www.example.com/ajax.html#!")
    'www.example.com/ajax.html?_escaped_fragment_='

    非AJAX可爬取的URL（无#!）原样返回：
    >>> escape_ajax("www.example.com/ajax.html#normal")
    'www.example.com/ajax.html#normal'
    """
    # 分离URL的基础部分和哈希片段
    de_frag, frag = urldefrag(url)

    # 仅处理以"!"开头的哈希片段（Google规范）
    if not frag.startswith("!"):
        return url  # 不符合规则则原样返回

    # 调用辅助函数添加 `_escaped_fragment_` 参数
    return add_or_replace_parameter(de_frag, "_escaped_fragment_", frag[1:])


if __name__ == '__main__':
    f = escape_ajax('http://example.com/page#!')
    print(f)
```

**code file end: crawlo/utils/url_utils.py**

---


### code file start: crawlo/utils/__init__.py 

```python
#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
# @Time    :    2025-02-05 13:57
# @Author  :   oscar
# @Desc    :   工具模块集合

提供用于处理parsel选择器的辅助函数，用于提取文本和属性等操作。
所有方法都采用了简洁直观的命名风格，便于记忆和使用。
"""

from ..tools.date_tools import (
    TimeUtils,
    parse_time,
    format_time,
    time_diff,
    to_timestamp,
    to_datetime,
    now,
    to_timezone,
    to_utc,
    to_local,
    from_timestamp_with_tz
)

from .selector_helper import (
    extract_text,
    extract_texts,
    extract_attr,
    extract_attrs,
    is_xpath
)

__all__ = [
    "TimeUtils",
    "parse_time",
    "format_time",
    "time_diff",
    "to_timestamp",
    "to_datetime",
    "now",
    "to_timezone",
    "to_utc",
    "to_local",
    "from_timestamp_with_tz",
    "extract_text",
    "extract_texts",
    "extract_attr",
    "extract_attrs",
    "is_xpath"
]
```

**code file end: crawlo/utils/__init__.py**

---

