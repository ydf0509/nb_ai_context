
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
# markdown content namespace: boost_spider project summary 



- **`boost_spider` = `funboost` 的超跑引擎 + 一套为爬虫量身打造的瑞士军刀。所有仿scrapy api爬虫框架都还是处在变花样造一辆马车**

- `boost_spider` 是增加了3个爬虫常用类，RequestClient  和  SpiderResponse  和 DatasetSink, 由funboost 驱动调度和并发。


## 📋 boost_spider most core source files metadata (Entry Points)


以下是项目 boost_spider 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project boost_spider most core source code files as follows: 
- `boost_spider/sink/json_sink.py`
- `boost_spider/http/request_client.py`
- `boost_spider/__init__.py`
- `boost_spider/sink/dataset_sink.py`


### 📄 Python File Metadata: `boost_spider/sink/json_sink.py`

#### 📦 Imports

- `import datetime`
- `import json`
- `import threading`
- `import time`
- `from pathlib import Path`
- `from boost_spider.sink.sink_helper import log_save_item`

#### 🏛️ Classes (1)

##### 📌 `class JsonFileSink`
*Line: 10*

**🔧 Constructor (`__init__`):**
- `def __init__(self, path, file)`
  - **Parameters:**
    - `self`
    - `path`
    - `file`

**Public Methods (2):**
- `def save(self, item: dict)`
- `def read_json(self)`

**Class Variables (2):**
- `_lock = threading.Lock()`
- `full_path__f_map = {}`


---




### 📄 Python File Metadata: `boost_spider/http/request_client.py`

#### 📝 Module Docstring

`````
改版包装requests的Session类，主要使用的是代理模式
1、支持一键设多种代理ip
2、支持3种类型的cookie添加
3、支持长会话，保持cookie状态, ss = RequestClient() , 一直用这个ss对象就可以自动保持cookie了
4、支持一键设置requests请求重试次数，确保请求成功，默认重试一次。
5、记录下当天的请求到文件，方便统计，同时开放了日志级别设置参数，用于禁止日志。
6、从使用requests修改为使用RequstClient门槛很低，三方包的request方法和此类的方法入参和返回完全100%保持了一致。
7、支持多个代理厂商自动切换。需要将proxy_name设置为一个列表，指定多个代理厂商的名字。
8、支持继承 RequestClient 来增加使用各种代理的请求方法，新增加代理商后，将请求方法名字加到 PROXYNAME__REQUEST_METHED_MAP 中。
`````

#### 📦 Imports

- `import json`
- `import logging`
- `import typing`
- `from enum import Enum`
- `from functools import lru_cache`
- `from pathlib import Path`
- `import nb_log`
- `import copy`
- `import time`
- `from typing import Union`
- `import requests`
- `from requests.cookies import RequestsCookieJar`
- `import urllib3.exceptions`
- `from boost_spider.http.user_agent import rand_get_useragent`
- `from parsel import Selector`
- `import re`

#### 🏛️ Classes (3)

##### 📌 `class HttpStatusError(Exception)`
*Line: 35*

**🔧 Constructor (`__init__`):**
- `def __init__(self, http_status_code)`
  - **Parameters:**
    - `self`
    - `http_status_code`

##### 📌 `class SpiderResponse(requests.Response)`
*Line: 43*

**🔧 Constructor (`__init__`):**
- `def __init__(self, resp: requests.Response)`
  - **Parameters:**
    - `self`
    - `resp: requests.Response`

**Public Methods (4):**
- `def re_search(self, pattern, flags = 0)`
- `def re_findall(self, pattern, flags = 0)`
- `def xpath(self, query)`
- `def css(self, query)`

**Properties (3):**
- `@property selector -> Selector`
- `@property resp_dict -> typing.Dict`
- `@property text -> str`

**Class Variables (1):**
- `re_pattern_map = {}`

##### 📌 `class RequestClient`
*Line: 89*

**🔧 Constructor (`__init__`):**
- `def __init__(self, proxy_name_list = None, ua = None, default_use_pc_ua = True, is_change_ua_every_request = False, timeout: Union[tuple, float] = (30, 40), verify = False, allow_redirects = True, is_close_session = True, request_retry_times = 2, using_platfrom = '')`
  - **Docstring:**
  `````
  :param proxy_name_list: 轮流使用代理服务商名字，可设置为 None,'noproxy', 'kuai', 'abuyun', 'crawlera',为None不使用代理
  :param ua:  useragent，如果不设置就随机分配一个欺骗的
  :param is_change_ua_every_request: 为每次请求设置新的useragent
  :param timeout: 超时设置
  :param verify:  是否校验服务器证书
  :param allow_redirects
  :param is_close_session: 是否在请求后关闭会话，连续型的请求需要cookie保持的，请设置为False，并且一直使用RequestClient实例化后的对象
  :param logger_level:日志级别，10 20 30 40 50
  `````
  - **Parameters:**
    - `self`
    - `proxy_name_list = None`
    - `ua = None`
    - `default_use_pc_ua = True`
    - `is_change_ua_every_request = False`
    - `timeout: Union[tuple, float] = (30, 40)`
    - `verify = False`
    - `allow_redirects = True`
    - `is_close_session = True`
    - `request_retry_times = 2`
    - `using_platfrom = ''`

**Public Methods (9):**
- `def get_cookie_jar(self)`
  - *返回cookiejar*
- `def get_cookie_dict(self)`
  - *返回cookie字典*
- `def get_cookie_str(self)`
  - *返回cookie字典*
- `def add_cookies(self, cookies: Union[str, dict, RequestsCookieJar])`
  - **Docstring:**
  `````
  :param cookies: 浏览器复制的cookie字符串或字典类型或者CookieJar类型
  :return:
  `````
- `def request(self, method: str, url: str, verify: bool = None, timeout: Union[int, float, tuple] = None, headers: dict = None, cookies: dict = None, **kwargs) -> typing.Optional[SpiderResponse]`
  - **Docstring:**
  `````
  使用指定名字的代理请求,从_proxy_name读取,当请求出错时候轮流使用各种代理ip。
  :param method:
  :param url:
  :param verify:
  :param timeout:
  :param headers:
  :param cookies:
  :param kwargs:
  :param kwargs :可接受一切requests.request方法中的参数
  :return:
  `````
- `def get(self, url: str, verify: bool = None, timeout: Union[int, float, tuple] = None, headers: dict = None, cookies: dict = None, **kwargs)`
- `def post(self, url: str, verify: bool = None, timeout: Union[int, float, tuple] = None, headers: dict = None, cookies: dict = None, **kwargs)`
- `def close_session(self)`
- `def save_picture(self, url, pic_path, pic_file = None)`

**Class Variables (5):**
- `logger = request_logger`
- `PROXY_NOPROXY = 'noproxy'`
- `PROXY_ABUYUN = 'abuyun'`
- `PROXY_KUAI = 'kuai'`
- `PROXYNAME__REQUEST_METHED_MAP = {'noproxy': _request_with_no_proxy, 'abuyun': _request_with_abuyun_proxy, 'kuai': _request_with_kuai_proxy}`


---




### 📄 Python File Metadata: `boost_spider/__init__.py`

#### 📝 Module Docstring

`````
boost_spider
是一款自由奔放写法的爬虫框架，无任何束缚，和用户手写平铺直叙的爬虫函数一样，
是横冲直撞的思维写的, 不需要callback回调解析方法, 不需要继承BaseSpider类, 没有BaseSpider类, 大开大合自由奔放.
只需要加上boost装饰器就可以自动加速并发，控制手段比传统爬虫框架多太多
`````

#### 📦 Imports

- `from boost_spider.http.request_client import RequestClient`
- `from boost_spider.http.request_client import SpiderResponse`
- `from boost_spider.sink.momgo_sink import MongoSink`
- `from boost_spider.sink.mysql_sink import MysqlSink`
- `from funboost import *`
- `import json`
- `import re`


---




### 📄 Python File Metadata: `boost_spider/sink/dataset_sink.py`

#### 📝 Module Docstring

`````
dataset 很适合保存一个字典到各种数据库 mysql postgre sqlite
`````

#### 📦 Imports

- `import dataset`

#### 🏛️ Classes (1)

##### 📌 `class DatasetSink`
*Line: 7*

**🔧 Constructor (`__init__`):**
- `def __init__(self, db_url)`
  - **Parameters:**
    - `self`
    - `db_url`

**Public Methods (2):**
- `def save(self, table_name: str, data: dict)`
- `def get_instance(cls, db_url)` `classmethod`

**Class Variables (2):**
- `_instances = {}`
- `_has__init_set = set()`


---



## 🔗 boost_spider Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ boost_spider/sink/dataset_sink.py
  ★ boost_spider/sink/json_sink.py

Core Files (imported by other files, sorted by import count):
  ◆ boost_spider/__init__.py (imported by 2 files)
  ◆ boost_spider/http/request_client.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `boost_spider/__init__.py`

**Imports from project:**
- `boost_spider/http/request_client.py`

**Imported by:**
- `boost_spider/http/request_client.py`
- `boost_spider/sink/json_sink.py`

#### `boost_spider/http/request_client.py`

**Imports from project:**
- `boost_spider/__init__.py`

**Imported by:**
- `boost_spider/__init__.py`

#### `boost_spider/sink/json_sink.py`

**Imports from project:**
- `boost_spider/__init__.py`

### 📦 Third-party Dependencies

项目使用的第三方库：

- `dataset`
- `funboost`
- `nb_log`
- `parsel`
- `requests`
- `urllib3`
- ......以及更多的第三方库......


---
# markdown content namespace: boost_spider codes 


## boost_spider File Tree (relative dir: `boost_spider`)


`````

└── boost_spider
    ├── __init__.py
    ├── http
    │   ├── __init__.py
    │   ├── request_client.py
    │   └── user_agent.py
    ├── sink
    │   ├── __init__.py
    │   ├── dataset_sink.py
    │   ├── excel_sink.py
    │   ├── json_sink.py
    │   ├── momgo_sink.py
    │   ├── mysql_sink.py
    │   ├── sink_helper.py
    │   └── sqlite_sink.py
    └── utils
        ├── __init__.py
        └── thread_local_obj.py

`````

---


## boost_spider (relative dir: `boost_spider`)  Included Files (total: 14 files)


- `boost_spider/__init__.py`

- `boost_spider/http/request_client.py`

- `boost_spider/http/user_agent.py`

- `boost_spider/http/__init__.py`

- `boost_spider/sink/dataset_sink.py`

- `boost_spider/sink/excel_sink.py`

- `boost_spider/sink/json_sink.py`

- `boost_spider/sink/momgo_sink.py`

- `boost_spider/sink/mysql_sink.py`

- `boost_spider/sink/sink_helper.py`

- `boost_spider/sink/sqlite_sink.py`

- `boost_spider/sink/__init__.py`

- `boost_spider/utils/thread_local_obj.py`

- `boost_spider/utils/__init__.py`


---


--- **start of file: boost_spider/__init__.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/__init__.py`

#### 📝 Module Docstring

`````
boost_spider
是一款自由奔放写法的爬虫框架，无任何束缚，和用户手写平铺直叙的爬虫函数一样，
是横冲直撞的思维写的, 不需要callback回调解析方法, 不需要继承BaseSpider类, 没有BaseSpider类, 大开大合自由奔放.
只需要加上boost装饰器就可以自动加速并发，控制手段比传统爬虫框架多太多
`````

#### 📦 Imports

- `from boost_spider.http.request_client import RequestClient`
- `from boost_spider.http.request_client import SpiderResponse`
- `from boost_spider.sink.momgo_sink import MongoSink`
- `from boost_spider.sink.mysql_sink import MysqlSink`
- `from funboost import *`
- `import json`
- `import re`


---

`````python
"""
boost_spider
是一款自由奔放写法的爬虫框架，无任何束缚，和用户手写平铺直叙的爬虫函数一样，
是横冲直撞的思维写的, 不需要callback回调解析方法, 不需要继承BaseSpider类, 没有BaseSpider类, 大开大合自由奔放.
只需要加上boost装饰器就可以自动加速并发，控制手段比传统爬虫框架多太多
"""

from boost_spider.http.request_client import RequestClient,SpiderResponse
from boost_spider.sink.momgo_sink import MongoSink
from boost_spider.sink.mysql_sink import MysqlSink
from funboost import *

import json
import re
`````

--- **end of file: boost_spider/__init__.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/http/request_client.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/http/request_client.py`

#### 📝 Module Docstring

`````
改版包装requests的Session类，主要使用的是代理模式
1、支持一键设多种代理ip
2、支持3种类型的cookie添加
3、支持长会话，保持cookie状态, ss = RequestClient() , 一直用这个ss对象就可以自动保持cookie了
4、支持一键设置requests请求重试次数，确保请求成功，默认重试一次。
5、记录下当天的请求到文件，方便统计，同时开放了日志级别设置参数，用于禁止日志。
6、从使用requests修改为使用RequstClient门槛很低，三方包的request方法和此类的方法入参和返回完全100%保持了一致。
7、支持多个代理厂商自动切换。需要将proxy_name设置为一个列表，指定多个代理厂商的名字。
8、支持继承 RequestClient 来增加使用各种代理的请求方法，新增加代理商后，将请求方法名字加到 PROXYNAME__REQUEST_METHED_MAP 中。
`````

#### 📦 Imports

- `import json`
- `import logging`
- `import typing`
- `from enum import Enum`
- `from functools import lru_cache`
- `from pathlib import Path`
- `import nb_log`
- `import copy`
- `import time`
- `from typing import Union`
- `import requests`
- `from requests.cookies import RequestsCookieJar`
- `import urllib3.exceptions`
- `from boost_spider.http.user_agent import rand_get_useragent`
- `from parsel import Selector`
- `import re`

#### 🏛️ Classes (3)

##### 📌 `class HttpStatusError(Exception)`
*Line: 35*

**🔧 Constructor (`__init__`):**
- `def __init__(self, http_status_code)`
  - **Parameters:**
    - `self`
    - `http_status_code`

##### 📌 `class SpiderResponse(requests.Response)`
*Line: 43*

**🔧 Constructor (`__init__`):**
- `def __init__(self, resp: requests.Response)`
  - **Parameters:**
    - `self`
    - `resp: requests.Response`

**Public Methods (4):**
- `def re_search(self, pattern, flags = 0)`
- `def re_findall(self, pattern, flags = 0)`
- `def xpath(self, query)`
- `def css(self, query)`

**Properties (3):**
- `@property selector -> Selector`
- `@property resp_dict -> typing.Dict`
- `@property text -> str`

**Class Variables (1):**
- `re_pattern_map = {}`

##### 📌 `class RequestClient`
*Line: 89*

**🔧 Constructor (`__init__`):**
- `def __init__(self, proxy_name_list = None, ua = None, default_use_pc_ua = True, is_change_ua_every_request = False, timeout: Union[tuple, float] = (30, 40), verify = False, allow_redirects = True, is_close_session = True, request_retry_times = 2, using_platfrom = '')`
  - **Docstring:**
  `````
  :param proxy_name_list: 轮流使用代理服务商名字，可设置为 None,'noproxy', 'kuai', 'abuyun', 'crawlera',为None不使用代理
  :param ua:  useragent，如果不设置就随机分配一个欺骗的
  :param is_change_ua_every_request: 为每次请求设置新的useragent
  :param timeout: 超时设置
  :param verify:  是否校验服务器证书
  :param allow_redirects
  :param is_close_session: 是否在请求后关闭会话，连续型的请求需要cookie保持的，请设置为False，并且一直使用RequestClient实例化后的对象
  :param logger_level:日志级别，10 20 30 40 50
  `````
  - **Parameters:**
    - `self`
    - `proxy_name_list = None`
    - `ua = None`
    - `default_use_pc_ua = True`
    - `is_change_ua_every_request = False`
    - `timeout: Union[tuple, float] = (30, 40)`
    - `verify = False`
    - `allow_redirects = True`
    - `is_close_session = True`
    - `request_retry_times = 2`
    - `using_platfrom = ''`

**Public Methods (9):**
- `def get_cookie_jar(self)`
  - *返回cookiejar*
- `def get_cookie_dict(self)`
  - *返回cookie字典*
- `def get_cookie_str(self)`
  - *返回cookie字典*
- `def add_cookies(self, cookies: Union[str, dict, RequestsCookieJar])`
  - **Docstring:**
  `````
  :param cookies: 浏览器复制的cookie字符串或字典类型或者CookieJar类型
  :return:
  `````
- `def request(self, method: str, url: str, verify: bool = None, timeout: Union[int, float, tuple] = None, headers: dict = None, cookies: dict = None, **kwargs) -> typing.Optional[SpiderResponse]`
  - **Docstring:**
  `````
  使用指定名字的代理请求,从_proxy_name读取,当请求出错时候轮流使用各种代理ip。
  :param method:
  :param url:
  :param verify:
  :param timeout:
  :param headers:
  :param cookies:
  :param kwargs:
  :param kwargs :可接受一切requests.request方法中的参数
  :return:
  `````
- `def get(self, url: str, verify: bool = None, timeout: Union[int, float, tuple] = None, headers: dict = None, cookies: dict = None, **kwargs)`
- `def post(self, url: str, verify: bool = None, timeout: Union[int, float, tuple] = None, headers: dict = None, cookies: dict = None, **kwargs)`
- `def close_session(self)`
- `def save_picture(self, url, pic_path, pic_file = None)`

**Class Variables (5):**
- `logger = request_logger`
- `PROXY_NOPROXY = 'noproxy'`
- `PROXY_ABUYUN = 'abuyun'`
- `PROXY_KUAI = 'kuai'`
- `PROXYNAME__REQUEST_METHED_MAP = {'noproxy': _request_with_no_proxy, 'abuyun': _request_with_abuyun_proxy, 'kuai': _request_with_kuai_proxy}`


---

`````python
# coding=utf-8
"""
改版包装requests的Session类，主要使用的是代理模式
1、支持一键设多种代理ip
2、支持3种类型的cookie添加
3、支持长会话，保持cookie状态, ss = RequestClient() , 一直用这个ss对象就可以自动保持cookie了
4、支持一键设置requests请求重试次数，确保请求成功，默认重试一次。
5、记录下当天的请求到文件，方便统计，同时开放了日志级别设置参数，用于禁止日志。
6、从使用requests修改为使用RequstClient门槛很低，三方包的request方法和此类的方法入参和返回完全100%保持了一致。
7、支持多个代理厂商自动切换。需要将proxy_name设置为一个列表，指定多个代理厂商的名字。
8、支持继承 RequestClient 来增加使用各种代理的请求方法，新增加代理商后，将请求方法名字加到 PROXYNAME__REQUEST_METHED_MAP 中。
"""
import json
import logging
import typing
from enum import Enum
from functools import lru_cache
from pathlib import Path

import nb_log
import copy
import time
from typing import Union
import requests
from requests.cookies import RequestsCookieJar
import urllib3.exceptions

from boost_spider.http.user_agent import rand_get_useragent

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from parsel import Selector
import re


class HttpStatusError(Exception):
    def __init__(self, http_status_code):
        super().__init__(f'请求返回的状态码不是200，是{http_status_code}')


request_logger = nb_log.get_logger('RequestClient', log_level_int=logging.DEBUG)


class SpiderResponse(requests.Response):  # 继承主要是方便代码补全提示，
    # noinspection PyMissingConstructor

    re_pattern_map = {}  # type: typing.Dict[str,re.Pattern]

    def __init__(self, resp: requests.Response):
        self.__dict__.update(resp.__dict__)  # 使 SpiderResponse 类具备requests.Response的所有属性

    @property
    @lru_cache()
    def selector(self) -> Selector:
        return Selector(self.text)

    @property
    @lru_cache()
    def resp_dict(self) -> typing.Dict:
        return json.loads(self.text)

    @property
    @lru_cache()
    def text(self) -> str:
        return super().text

    def re_search(self, pattern, flags=0):
        key = f'{pattern} {flags}'
        if key not in self.re_pattern_map:
            pa_obj = re.compile(pattern=pattern, flags=flags)
            self.re_pattern_map[key] = pa_obj
        return self.re_pattern_map[key].search(self.text)

    def re_findall(self, pattern, flags=0):
        # return re.findall(pattern, self.text, flags)
        key = f'{pattern} {flags}'
        if key not in self.re_pattern_map:
            pa_obj = re.compile(pattern=pattern, flags=flags)
            self.re_pattern_map[key] = pa_obj
        return self.re_pattern_map[key].findall(self.text)

    def xpath(self, query):
        return self.selector.xpath(query)

    def css(self, query):
        return self.selector.css(query)


# noinspection PyBroadException
class RequestClient:
    logger = request_logger

    def __init__(self, proxy_name_list=None,
                 ua=None, default_use_pc_ua=True, is_change_ua_every_request=False,
                 timeout: Union[tuple, float] = (30, 40),
                 verify=False, allow_redirects=True, is_close_session=True,
                 request_retry_times=2,
                 using_platfrom=''):
        """
        :param proxy_name_list: 轮流使用代理服务商名字，可设置为 None,'noproxy', 'kuai', 'abuyun', 'crawlera',为None不使用代理
        :param ua:  useragent，如果不设置就随机分配一个欺骗的
        :param is_change_ua_every_request: 为每次请求设置新的useragent
        :param timeout: 超时设置
        :param verify:  是否校验服务器证书
        :param allow_redirects
        :param is_close_session: 是否在请求后关闭会话，连续型的请求需要cookie保持的，请设置为False，并且一直使用RequestClient实例化后的对象
        :param logger_level:日志级别，10 20 30 40 50
        """
        if proxy_name_list is None:
            proxy_name_list = ['noproxy']
        if not isinstance(proxy_name_list, list):
            proxy_name_list = [proxy_name_list]
        if not set(proxy_name_list).issubset(set(self.PROXYNAME__REQUEST_METHED_MAP.keys())):
            raise Exception('设置的代理名称错误')
        self._proxy_name_list = proxy_name_list
        default_ua = (
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' if default_use_pc_ua else
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36')
        self._ua = ua if ua else default_ua
        self._default_use_pc_ua = default_use_pc_ua
        self._is_change_ua_every_request = is_change_ua_every_request
        self._timeout = timeout
        self._verify = verify
        self._allow_redirects = allow_redirects
        self._is_close_session = is_close_session
        self.ss = requests.Session()
        self._max_request_retry_times = request_retry_times
        self._using_platfrom = using_platfrom

    def __add_ua_to_headers(self, headers):
        # noinspection PyDictCreation
        if not headers:
            headers = dict()
            headers['user-agent'] = self._ua
        else:
            if 'user-agent' not in headers and 'User-Agent' not in headers:
                headers['user-agent'] = self._ua
        if self._is_change_ua_every_request:
            if self._default_use_pc_ua:
                headers['user-agent'] = rand_get_useragent('chrome')
            else:
                headers['user-agent'] = rand_get_useragent('mobile')
        headers.update({'Accept-Language': 'zh-CN,zh;q=0.8'})
        return headers

    def get_cookie_jar(self):
        """返回cookiejar"""
        return self.ss.cookies

    def get_cookie_dict(self):
        """返回cookie字典"""
        return self.ss.cookies.get_dict()

    def get_cookie_str(self):
        """返回cookie字典"""
        cookie_str = ''
        for cookie_item in self.get_cookie_dict().items():
            cookie_str += cookie_item[0] + '=' + cookie_item[1] + ';'
        return cookie_str[:-1]

    def add_cookies(self, cookies: Union[str, dict, RequestsCookieJar]):
        """
        :param cookies: 浏览器复制的cookie字符串或字典类型或者CookieJar类型
        :return:
        """
        cookies_dict = dict()
        if not isinstance(cookies, (str, dict, RequestsCookieJar)):
            raise TypeError('传入的cookie类型错误')
        if isinstance(cookies, str):
            cookie_pairs = cookies.split('; ')
            for cookie_pair in cookie_pairs:
                k, v = cookie_pair.split('=', maxsplit=1)
                cookies_dict[k] = v
        if isinstance(cookies, (dict, RequestsCookieJar)):
            cookies_dict = cookies
        self.ss.cookies = requests.sessions.merge_cookies(self.ss.cookies, cookies_dict)

    def request(self, method: str, url: str, verify: bool = None,
                timeout: Union[int, float, tuple] = None, headers: dict = None,
                cookies: dict = None, **kwargs) -> typing.Optional[SpiderResponse]:
        """
        使用指定名字的代理请求,从_proxy_name读取,当请求出错时候轮流使用各种代理ip。
        :param method:
        :param url:
        :param verify:
        :param timeout:
        :param headers:
        :param cookies:
        :param kwargs:
        :param kwargs :可接受一切requests.request方法中的参数
        :return:
        """
        # self.logger.debug(locals())
        key_word_args = copy.copy(locals())
        key_word_args['headers'] = self.__add_ua_to_headers(headers)
        # key_word_args.pop('self')
        key_word_args.pop('kwargs')
        key_word_args.update(kwargs)
        if 'allow_redirects' not in key_word_args:
            key_word_args['allow_redirects'] = self._allow_redirects

        resp = None
        # self.logger.debug('starting {} this url -->  '.format(method) + url)
        # print(key_word_args)
        exception_request = None
        proxy_list = self._proxy_name_list * (self._max_request_retry_times + 1)
        for i in range(self._max_request_retry_times + 1):
            current_proxy_name = proxy_list[i]
            t_start = time.time()
            try:
                request_proxy_method = self.PROXYNAME__REQUEST_METHED_MAP[current_proxy_name]
                resp = request_proxy_method(**key_word_args)
                time_spend = round(time.time() - t_start, 2)
                resp.time_spend = time_spend
                resp.ts = time_spend  # 简写
                resp_log_dict = {
                    'time_spend': round(time_spend, 2),
                    'status_code': resp.status_code,
                    'method': method,
                    'current_retry_time': i,
                    'current_proxy_name': current_proxy_name,
                    'is_redirect': resp.is_redirect,
                    'resp_len': len(resp.text),
                    'resp_url': resp.url,
                }
                msg = f''' {self._using_platfrom}  request响应状态: {json.dumps(resp_log_dict, ensure_ascii=False)}'''
                self.logger.debug(msg, extra=resp_log_dict)
                if resp.status_code != 200 and i < self._max_request_retry_times + 1:
                    self.logger.warning(msg, extra=resp_log_dict)
                    raise HttpStatusError(resp.status_code)
                if i != 0:
                    pass
                    # self.logger.info(f'第 {i} 次重试请求成功')
                break
            except Exception as e:
                exception_request = e
                if i != self._max_request_retry_times:
                    self.logger.warning(
                        f'{self._using_platfrom} RequestClient内部第{i}次请求出错，此次使用的代理是{current_proxy_name}, url: {url}'
                        f'浪费时间[{round(time.time() - t_start, 2)}],再重试一次，原因是：{type(e)}    {e}')
        self.close_session()
        if resp is not None:  # 如<Response [404]>也是false,但不是none
            return SpiderResponse(resp)
        else:
            raise exception_request

    def get(self, url: str, verify: bool = None,
            timeout: Union[int, float, tuple] = None, headers: dict = None,
            cookies: dict = None, **kwargs):
        params = copy.copy(locals())
        params.pop('self')
        params.pop('kwargs')
        params.update(kwargs)
        params['method'] = 'get'
        return self.request(**params)

    def post(self, url: str, verify: bool = None,
             timeout: Union[int, float, tuple] = None, headers: dict = None,
             cookies: dict = None, **kwargs):
        params = copy.copy(locals())
        params.pop('self')
        params.pop('kwargs')
        params.update(kwargs)
        params['method'] = 'post'
        return self.request(**params)

    def close_session(self):
        if self._is_close_session:
            try:
                self.ss.close()
            except Exception:
                pass

    def save_picture(self, url, pic_path, pic_file=None, ):
        resp = self.get(url)
        if pic_file is None:
            pic_file = url.split('/')[-1]
        Path(pic_path).mkdir(exist_ok=True)
        full_path = Path(pic_path) / Path(pic_file)
        full_path.write_bytes(resp.content)

    def _request_with_no_proxy(self, method, url, verify=None, timeout=None, headers=None, cookies=None, **kwargs):
        """普通不使用代理"""

        return self.ss.request(method, url, verify=verify or self._verify, timeout=timeout or self._timeout,
                               headers=headers, cookies=cookies, **kwargs)

    def _request_with_abuyun_proxy(self, method, url, verify=None, timeout=None, headers=None, cookies=None, **kwargs):
        # 代理服务器
        proxy_host = "http-dyn.abuyun.com"
        proxy_port = "9020"

        # 代理隧道验证信息
        proxy_user = "HH65YN4C381XXXXX"
        proxy_pass = "7176BE32A00YYYYY"

        proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxy_host,
            "port": proxy_port,
            "user": proxy_user,
            "pass": proxy_pass,
        }

        proxies = {
            "http": proxy_meta,
            "https": proxy_meta,
        }
        resp = self.ss.request(method, url, verify=verify or self._verify, timeout=timeout or self._timeout,
                               headers=headers, cookies=cookies,
                               proxies=proxies, **kwargs)
        if resp.status_code == 429 or "429 Too Many Requests'" in resp.text or "429 To Many Requests'" in resp.text:
            raise IOError(f'阿布云返回的状态是 {resp.status_code}')
        return resp

    def _request_with_kuai_proxy(self, method, url, verify=None, timeout=None, headers=None, cookies=None, **kwargs):
        """使用redis中的快代理池子,怎么从redis拿代理ip和requests怎么使用代理，用户自己写"""

        raise NotImplemented


    PROXY_NOPROXY = 'noproxy'  # 方便代理名称补全.
    PROXY_ABUYUN = 'abuyun'
    PROXY_KUAI = 'kuai'

    PROXYNAME__REQUEST_METHED_MAP = {'noproxy': _request_with_no_proxy,
                                     'abuyun': _request_with_abuyun_proxy,
                                     'kuai': _request_with_kuai_proxy
                                     }  # 用户新增了方法后，在这里添加代理名字和请求方法的映射映射

    """
    用户可以继承 RequestClient ,增加代理商的ip使用方法,然后在 PROXYNAME__REQUEST_METHED_MAP 新增代理商名字 对应的 方法名 映射 ,
    根据入参 proxy_name_list 的 代理商名字, 自动轮流使用用户自己的各个ip代理商 发请求.
    """

    """
# 扩展方式例如:
    
class MyRequestClient(RequestClient):

    def _request_with_my_redis_ip_proxy(self, method, url, **kwargs):
        # 实现你自己的代理逻辑
      
        proxies = {
            "http": $从你的redis ip代理池随机取一个ip,
            "https": $从你的redis ip代理池随机取一个ip,
        }
        return self.ss.request(method, url, proxies=proxies, **kwargs)
    
    # 扩展代理映射
    RequestClient.PROXYNAME__REQUEST_METHED_MAP['my_proxy'] = _request_with_my_redis_ip_proxy
  
    """


if __name__ == '__main__':
    rc = RequestClient(using_platfrom='爬百度的')
    resp = rc.get('https://www.baidu.com')
    print(resp.request.headers)
    print(resp.status_code)
    print(resp.selector)
    print(resp.selector)

    rc.save_picture('https://scarb-images.oss-cn-hangzhou.aliyuncs.com/img/202207142159934.png', '/pics')

`````

--- **end of file: boost_spider/http/request_client.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/http/user_agent.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/http/user_agent.py`

#### 📝 Module Docstring

`````
Created on 2016-12-28 17:55
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
`````

#### 📦 Imports

- `import random`
- `import typing`

#### 🔧 Public Functions (1)

- `def rand_get_useragent(ua_type: str = None)`
  - *Line: 382*
  - **Docstring:**
  `````
  :param ua_type:  chrome  firefox opera internetexplorer safari  mobile
  :return:
  `````


---

`````python
# -*- coding: utf-8 -*-
"""
Created on 2016-12-28 17:55
---------
@summary:
---------
@author: Boris
@email: boris_liu@foxmail.com
"""

import random
import typing

USER_AGENTS = {
    "chrome": [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
        "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14",
    ],
    "opera": [
        "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
        "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
        "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
        "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
        "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
        "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
        "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
        "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
        "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
        "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
        "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
        "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
        "Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50",
        "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
        "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11",
        "Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10",
        "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
        "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
        "Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1",
        "Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
        "Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
        "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01",
        "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00",
        "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00",
    ],
    "firefox": [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
        "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0",
        "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0",
        "Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0",
        "Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0)  Gecko/20100101 Firefox/18.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6",
    ],
    "internetexplorer": [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
        "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",
        "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)",
    ],
    "safari": [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    ],
    "mobile": [
        "Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/14.2 Safari/536.2+",
        "Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/14.2 Safari/536.2+",
        "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/14.2 Mobile Safari/537.10+",
        "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/14.2 Mobile Safari/537.10+",
        "Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/14.2 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/14.2 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/14.2 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/14.2 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/14.2 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/14.2 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/14.2 Mobile/14E304 Safari/602.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/14.2 Mobile/14E304 Safari/602.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/14.2 Mobile/15A372 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:89.0 Gecko/48.0 Firefox/90.0 KAIOS/2.5",
        "Mozilla/5.0 (Mobile; LYF/F300B/LYF-F300B-001-01-15-130718-i;Android; rv:89.0 Gecko/48.0 Firefox/90.0 KAIOS/2.5",
        "Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true",
        "Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true",
        "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36 Edge/14.14263",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36 Edge/14.14263",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36 Edge/14.14263",
        "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36 Edge/14.14263",
        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)",
        "Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
        "Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",
        "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36 Edg/93.0.4576.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0 Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.2 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4576.0 Safari/537.36 Edg/93.0.4576.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0 Gecko/20100101 Firefox/90.0",
    ],
}


def rand_get_useragent(ua_type: str = None):
    """

    :param ua_type:  chrome  firefox opera internetexplorer safari  mobile
    :return:
    """
    if not ua_type:
        ua_type = random.choice(list(USER_AGENTS.keys()))
    elif ua_type not in USER_AGENTS:
        raise ValueError(
            "ua_type error, expect one of {}".format(list(USER_AGENTS.keys()))
        )

    return random.choice(USER_AGENTS[ua_type])

`````

--- **end of file: boost_spider/http/user_agent.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/http/__init__.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/http/__init__.py`


---

`````python

`````

--- **end of file: boost_spider/http/__init__.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/dataset_sink.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/dataset_sink.py`

#### 📝 Module Docstring

`````
dataset 很适合保存一个字典到各种数据库 mysql postgre sqlite
`````

#### 📦 Imports

- `import dataset`

#### 🏛️ Classes (1)

##### 📌 `class DatasetSink`
*Line: 7*

**🔧 Constructor (`__init__`):**
- `def __init__(self, db_url)`
  - **Parameters:**
    - `self`
    - `db_url`

**Public Methods (2):**
- `def save(self, table_name: str, data: dict)`
- `def get_instance(cls, db_url)` `classmethod`

**Class Variables (2):**
- `_instances = {}`
- `_has__init_set = set()`


---

`````python
"""
dataset 很适合保存一个字典到各种数据库 mysql postgre sqlite
"""
import dataset


class DatasetSink:
    # 类级别的实例缓存，按 db_url 存储
    _instances = {}
    _has__init_set = set()

    def __new__(cls, db_url):
        # 如果 db_url 已存在，直接返回已有实例
        if db_url not in cls._instances:
            # 创建新实例并存入缓存
            self = super(DatasetSink, cls).__new__(cls)
            cls._instances[db_url] = self
        return cls._instances[db_url]

    def __init__(self, db_url):
        if id(self) not in self.__class__._has__init_set:
            print(f'创建连接 {db_url}')
            self.db = dataset.connect(db_url, ensure_schema=True)
            self.__class__._has__init_set.add(id(self))

    def save(self, table_name: str, data: dict, ):
        # 使用已有的连接插入数据
        table = self.db[table_name]
        table.insert(data)

    @classmethod
    def get_instance(cls, db_url):
        # 提供一个显式的获取实例方法（可选）
        return cls(db_url)


if __name__ == '__main__':
    dataset_sink1 = DatasetSink("mysql+pymysql://root:123456@localhost/testdb2")
    DatasetSink("mysql+pymysql://root:123456@localhost/testdb2")
    data = {'user': 'user2', 'oderid': 222}
    dataset_sink1.save('your_table', data)  # 使用第一个数据库

`````

--- **end of file: boost_spider/sink/dataset_sink.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/excel_sink.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/excel_sink.py`


---

`````python

`````

--- **end of file: boost_spider/sink/excel_sink.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/json_sink.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/json_sink.py`

#### 📦 Imports

- `import datetime`
- `import json`
- `import threading`
- `import time`
- `from pathlib import Path`
- `from boost_spider.sink.sink_helper import log_save_item`

#### 🏛️ Classes (1)

##### 📌 `class JsonFileSink`
*Line: 10*

**🔧 Constructor (`__init__`):**
- `def __init__(self, path, file)`
  - **Parameters:**
    - `self`
    - `path`
    - `file`

**Public Methods (2):**
- `def save(self, item: dict)`
- `def read_json(self)`

**Class Variables (2):**
- `_lock = threading.Lock()`
- `full_path__f_map = {}`


---

`````python
import datetime
import json
import threading
import time
from pathlib import Path

from boost_spider.sink.sink_helper import log_save_item


class JsonFileSink:
    _lock = threading.Lock()
    # path__has_create_map = {}
    full_path__f_map = {}

    def __init__(self, path, file):
        self.full_path = Path(path) / Path(file)
        self._key = f'{path}{file}'
        if self._key not in self.full_path__f_map:
            Path(path).mkdir(exist_ok=True)
            self.full_path__f_map[self._key] = Path(self.full_path).open('a+', encoding='utf8')
        self.f = self.full_path__f_map[self._key]

    def save(self, item: dict):
        item['item_insert_time'] = str(datetime.datetime.now())
        with self._lock:
            self.f.write(json.dumps(item) + ',\n')
        # log_save_item(item,'jsonfile',self.full_path,'')

    def read_json(self):
        text = Path(self.full_path).read_text(encoding='utf8')
        json_text = f'[{text[:-2]}]'
        return json.loads(json_text)


if __name__ == '__main__':
    t1 = time.time()
    for i in range(1000):
        # JsonFileSink('/codedir', 'testjsonfile2.json').save({'a': i, 'b': f'{i*2}'})
        JsonFileSink('/codedir', 'testjsonfile.json').save({'a': 63, 'b': 4})
        pass
    print(time.time() - t1)
    # print(JsonFileSink('/codedir', 'testjsonfile2.json').read_json())

`````

--- **end of file: boost_spider/sink/json_sink.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/momgo_sink.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/momgo_sink.py`

#### 📦 Imports

- `import os`
- `from pymongo.collection import Collection`
- `from pymongo import MongoClient`
- `from boost_spider.sink.sink_helper import log_save_item`

#### 🏛️ Classes (1)

##### 📌 `class MongoSink`
*Line: 12*

**🔧 Constructor (`__init__`):**
- `def __init__(self, db: str, col: str, uniqu_key: str, mongo_connect_url = 'mongodb://127.0.0.1')`
  - **Parameters:**
    - `self`
    - `db: str`
    - `col: str`
    - `uniqu_key: str`
    - `mongo_connect_url = 'mongodb://127.0.0.1'`

**Public Methods (2):**
- `def get_col(self) -> Collection`
  - *封装一个函数，判断pid*
- `def save(self, item)`

**Class Variables (1):**
- `pid__col_map = {}`


---

`````python
import os
from pymongo.collection import Collection
from pymongo import MongoClient
from boost_spider.sink.sink_helper import log_save_item

"""
此模块封装的pymongo是在linux上子进程安全的。
在win上无所谓都正常。
"""


class MongoSink:
    pid__col_map = {}

    def __init__(self, db: str, col: str, uniqu_key: str, mongo_connect_url='mongodb://127.0.0.1', ):
        self.db = db
        self.col = col
        self.uniqu_key = uniqu_key
        self.mongo_connect_url = mongo_connect_url

    def get_col(self, ) -> Collection:
        """封装一个函数，判断pid"""
        pid = os.getpid()
        key = (pid, self.mongo_connect_url, self.db, self.col)
        if key not in self.pid__col_map:
            self.pid__col_map[key] = MongoClient(self.mongo_connect_url).get_database(self.db).get_collection(self.col)
        return self.pid__col_map[key]

    def save(self, item):
        item['_id'] = item[self.uniqu_key]
        self.get_col().replace_one({'_id': item['_id']}, item, upsert=True)
        log_save_item(item, 'mongo', self.db, self.col)

`````

--- **end of file: boost_spider/sink/momgo_sink.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/mysql_sink.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/mysql_sink.py`

#### 📦 Imports

- `import typing`
- `import pymysql.cursors`
- `from universal_object_pool import ObjectPool`
- `from universal_object_pool.contrib.pymysql_pool import PyMysqlOperator`
- `from boost_spider.sink.sink_helper import log_save_item`

#### 🏛️ Classes (1)

##### 📌 `class MysqlSink`
*Line: 15*

**Docstring:**
`````
不推荐,使用dataset_sink 就好了.
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, host = '127.0.0.1', port = 3306, user = 'root', password = '123456', db = None, table = None)`
  - **Parameters:**
    - `self`
    - `host = '127.0.0.1'`
    - `port = 3306`
    - `user = 'root'`
    - `password = '123456'`
    - `db = None`
    - `table = None`

**Public Methods (1):**
- `def save(self, item: dict)`

**Class Variables (1):**
- `_key__pool_map = {}`


---

`````python

import typing

import pymysql.cursors
from universal_object_pool import ObjectPool
from universal_object_pool.contrib.pymysql_pool import PyMysqlOperator

from boost_spider.sink.sink_helper import log_save_item


"""
保存到 mysql,不推荐,直接 使用dataset_sink 就好了.
"""

class MysqlSink:
    """不推荐,使用dataset_sink 就好了."""
    _key__pool_map = {}

    def _get_pool(self):
        if self._pool_key not in self._key__pool_map:
            self._key__pool_map[self._pool_key] = ObjectPool(object_type=PyMysqlOperator,
                                                             object_pool_size=100,
                                                             object_init_kwargs=self._mysql_conn_kwargs)
        return self._key__pool_map[self._pool_key]

    def __init__(self, host='127.0.0.1', port=3306, user='root', password='123456', db=None, table=None):
        self._mysql_conn_kwargs = {'host': host, 'user': user, 'password': password, 'port': port,'database':db}
        self._pool_key = f'{host} {port} {user} {password} {db}'
        self.db = db
        self.table = table

    def save(self, item: dict):
        mysql_pool = self._get_pool()
        sql = self._build_sql(item)
        with mysql_pool.get() as operator:  # type: typing.Union[PyMysqlOperator,pymysql.cursors.DictCursor] #利于补全
            operator.execute(sql,args=None)
        log_save_item(item, 'mysql', self.db, self.table)

    def _build_sql(self, item: dict):
        """
        这段字典转sql代码是复制网上的，可以使用dataset_sink来直接保存字典。
        :param item:
        :return:
        """
        key_list = []
        value_list = []
        for k, v in item.items():
            key_list.append(k)
            value_list.append(v)
        keys_str = ''
        for k in key_list:
            keys_str += f'`{k}`,'
        keys_str = f'( {keys_str[:-1]} )'

        values_str = ''
        for v in value_list:
            if isinstance(v, str):
                v = f"'{v}'"
            values_str += f'{v},'
        values_str = f'( {values_str[:-1]} )'
        sql = f"replace into {self.table} {keys_str} values {values_str}"
        return sql


if __name__ == '__main__':
    print(MysqlSink(db='testdb', table='test_table')._build_sql({'a': 1, 'b': 2}))
    MysqlSink(db='testdb', table='t2').save({'uname': 'uname1', 'age': 1})

`````

--- **end of file: boost_spider/sink/mysql_sink.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/sink_helper.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/sink_helper.py`

#### 📦 Imports

- `import nb_log`

#### 🔧 Public Functions (1)

- `def log_save_item(item, dbtype, db, table)`
  - *Line: 6*


---

`````python
import nb_log

logger = nb_log.get_logger(__name__, log_filename='boost_spider_sink.log')


def log_save_item(item, dbtype, db, table):
    logger.info(f'保存结果到 {dbtype} {db}.{table} 中成功,  {item} ')

`````

--- **end of file: boost_spider/sink/sink_helper.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/sqlite_sink.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/sqlite_sink.py`

#### 📦 Imports

- `import os`
- `import sqlite3`
- `import threading`
- `from pathlib import Path`
- `import nb_log`
- `from pymongo.collection import Collection`
- `from pymongo import MongoClient`
- `from boost_spider.sink.sink_helper import log_save_item`

#### 🏛️ Classes (1)

##### 📌 `class SqliteSink`
*Line: 15*

**🔧 Constructor (`__init__`):**
- `def __init__(self, path, db, table)`
  - **Parameters:**
    - `self`
    - `path`
    - `db`
    - `table`

**Public Methods (1):**
- `def save(self, item: dict)`

**Class Variables (4):**
- `db__cusor_map = {}`
- `db__conn_map = {}`
- `_op_lock = threading.Lock()`
- `logger = nb_log.get_logger('SqliteSink')`


---

`````python
import os
import sqlite3
import threading
from pathlib import Path
import nb_log
from pymongo.collection import Collection
from pymongo import MongoClient
from boost_spider.sink.sink_helper import log_save_item

"""
保存到sqlite,不推荐,直接 使用dataset_sink 就好了.
"""


class SqliteSink:
    db__cusor_map = {}
    db__conn_map = {}
    _op_lock = threading.Lock()

    logger = nb_log.get_logger('SqliteSink')

    def __init__(self, path, db, table):
        self.db = db
        self.table = table
        self._key = f'{path} {db}'
        if self._key not in self.db__cusor_map:
            Path(path).mkdir(exist_ok=True)
            full_path = Path(path) / Path(f'{db}.db')
            conn = sqlite3.connect(full_path)
            cursor = conn.cursor()
            self.logger.debug(f'创建 {full_path} sqlite连接成功')
            self.db__cusor_map[self._key] = cursor
            self.db__conn_map[self._key] = conn
        self.cusror = self.db__cusor_map[self._key]
        self.conn = self.db__conn_map[self._key]

    def save(self, item: dict):
        sql = self._build_sql(item)
        with self._op_lock:
            self.cusror.execute(sql)
            self.conn.commit()
            log_save_item(item, 'sqlite', self.db, self.table)

    def _build_sql(self, item: dict):
        key_list = []
        value_list = []
        for k, v in item.items():
            key_list.append(k)
            value_list.append(v)
        # keys_str = str(tuple(key_list)).replace("'", "`")
        keys_str = ''
        for k in key_list:
            keys_str += f'`{k}`,'
        keys_str = f'( {keys_str[:-1]} )'

        values_str = ''
        for v in value_list:
            if isinstance(v, str):
                v = f"'{v}'"
            values_str += f'{v},'
        values_str = f'( {values_str[:-1]} )'
        sql = f"replace into {self.table} {keys_str} values {values_str}"
        return sql


if __name__ == '__main__':
    SqliteSink('/codedir/sqlite/', 'testdb', 'testtable').save({'a': '1', 'b': 2})
    SqliteSink('/codedir/sqlite/', 'testdb', 'testtable').save({'a': '7', 'b': 8})

`````

--- **end of file: boost_spider/sink/sqlite_sink.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/sink/__init__.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/sink/__init__.py`


---

`````python

`````

--- **end of file: boost_spider/sink/__init__.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/utils/thread_local_obj.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/utils/thread_local_obj.py`

#### 📦 Imports

- `import abc`
- `import threading`
- `import time`
- `from typing import Type`
- `from typing import TypeVar`
- `import httpx`
- `from concurrent.futures import ThreadPoolExecutor`

#### 🏛️ Classes (2)

##### 📌 `class BaseThreadLocalObjGetter`
*Line: 9*

**Public Methods (1):**
- `def get_obj(self, obj_type: T) -> T`

**Class Variables (1):**
- `thread_local = threading.local()`

##### 📌 `class AsyncClientGetter(BaseThreadLocalObjGetter)`
*Line: 30*

#### 🔧 Public Functions (1)

- `def t()`
  - *Line: 35*


---

`````python
import abc
import threading
import time
from typing import Type, TypeVar

T = TypeVar('T')


class BaseThreadLocalObjGetter(metaclass=abc.ABCMeta):
    thread_local = threading.local()

    def get_obj(self, obj_type: T,) -> T:
        obj_name = str(type(self))
        if not getattr(self.thread_local, obj_name, None):
            obj = self._get_obj()
            print(f'生成线程变量 {obj}')
            setattr(self.thread_local, obj_name, obj)
        return getattr(self.thread_local, obj_name)

    @abc.abstractmethod
    def _get_obj(self):
        raise NotImplemented


if __name__ == '__main__':
    import httpx
    from concurrent.futures import ThreadPoolExecutor


    class AsyncClientGetter(BaseThreadLocalObjGetter):
        def _get_obj(self):
            return httpx.AsyncClient()


    def t():
        for i in range(5):
            print(AsyncClientGetter().get_obj(httpx.AsyncClient))


    pool = ThreadPoolExecutor(20)
    for i in range(10):
        pool.submit(t)

`````

--- **end of file: boost_spider/utils/thread_local_obj.py** (project: boost_spider) --- 

---


--- **start of file: boost_spider/utils/__init__.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_spider/utils/__init__.py`


---

`````python

`````

--- **end of file: boost_spider/utils/__init__.py** (project: boost_spider) --- 

---

# markdown content namespace: demo_crawler codes 


## boost_spider File Tree (relative dir: `demo_crawler`)


`````

└── demo_crawler
    ├── boost_scrapy_imp
    │   ├── boost_scrapy_demo.py
    │   ├── items.py
    │   ├── middlewares.py
    │   └── pipelines.py
    ├── boost_spider_imp
    │   └── boost_spider_crawler.py
    ├── celery_imp
    │   └── celery_crawler.py
    ├── feapder_imp
    │   └── feapder_news_crawler.py
    ├── news_server.py
    ├── scrapy_imp
    │   └── scrapy_spider_crawler.py
    ├── threadpool_crawler_imp
    │   └── threadpool_crawler.py
    └── threadpool_redis_crawler_imp
        └── redis_threadpool_crawler.py

`````

---


## boost_spider (relative dir: `demo_crawler`)  Included Files (total: 11 files)


- `demo_crawler/news_server.py`

- `demo_crawler/boost_scrapy_imp/boost_scrapy_demo.py`

- `demo_crawler/boost_scrapy_imp/items.py`

- `demo_crawler/boost_scrapy_imp/middlewares.py`

- `demo_crawler/boost_scrapy_imp/pipelines.py`

- `demo_crawler/boost_spider_imp/boost_spider_crawler.py`

- `demo_crawler/celery_imp/celery_crawler.py`

- `demo_crawler/feapder_imp/feapder_news_crawler.py`

- `demo_crawler/scrapy_imp/scrapy_spider_crawler.py`

- `demo_crawler/threadpool_crawler_imp/threadpool_crawler.py`

- `demo_crawler/threadpool_redis_crawler_imp/redis_threadpool_crawler.py`


---


--- **start of file: demo_crawler/news_server.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/news_server.py`

#### 📝 Module Docstring

`````
新闻服务端 - FastAPI实现
提供列表页、详情页和评论页API，用于爬虫测试
`````

#### 📦 Imports

- `import random`
- `import string`
- `from datetime import datetime`
- `from datetime import timedelta`
- `from fastapi import FastAPI`
- `from fastapi.responses import HTMLResponse`
- `from pydantic import BaseModel`
- `from typing import List`
- `import uvicorn`

#### 🏛️ Classes (2)

##### 📌 `class NewsListItem(BaseModel)`
*Line: 17*

**Docstring:**
`````
列表页新闻项
`````

**Class Variables (2):**
- `id: int`
- `title: str`

##### 📌 `class NewsDetail(BaseModel)`
*Line: 23*

**Docstring:**
`````
详情页新闻
`````

**Class Variables (5):**
- `id: int`
- `title: str`
- `content: str`
- `author: str`
- `publish_time: str`

#### 🔧 Public Functions (9)

- `def random_chinese_title() -> str`
  - *Line: 33*
  - *生成随机新闻标题*

- `def random_content(paragraphs: int = 5) -> str`
  - *Line: 41*
  - *生成随机新闻正文*

- `def random_author() -> str`
  - *Line: 62*
  - *生成随机作者名*

- `def random_time() -> str`
  - *Line: 69*
  - *生成随机发布时间（最近7天内）*

- `def get_news_list(page: int = 1, size: int = 10)` `app.get('/news/list', response_model=List[NewsListItem], summary='获取新闻列表')`
  - *Line: 78*
  - **Docstring:**
  `````
  获取新闻列表页
  - **page**: 页码，默认1
  - **size**: 每页数量，默认10
  `````

- `def get_news_detail(news_id: int)` `app.get('/news/{news_id}', response_model=NewsDetail, summary='获取新闻详情')`
  - *Line: 95*
  - **Docstring:**
  `````
  获取新闻详情页
  - **news_id**: 新闻ID
  `````

- `def random_comment_content() -> str`
  - *Line: 110*
  - *生成随机评论内容*

- `def get_news_comments_html(news_id: int, page: int = 1, size: int = 10)` `app.get('/news/{news_id}/comments', response_class=HTMLResponse, summary='获取新闻评论页(HTML)')`
  - *Line: 128*
  - **Docstring:**
  `````
  获取新闻评论页 - 返回HTML格式，可使用xpath解析
  - **news_id**: 新闻ID
  - **page**: 页码，默认1
  - **size**: 每页数量，默认10
  `````

- `def root()` `app.get('/', summary='首页')`
  - *Line: 204*
  - *API根路径，返回欢迎信息*


---

`````python
"""
新闻服务端 - FastAPI实现
提供列表页、详情页和评论页API，用于爬虫测试
"""
import random
import string
from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="新闻服务API", description="模拟新闻网站，支持列表页、详情页和评论页")

# ================= 数据模型 =================
class NewsListItem(BaseModel):
    """列表页新闻项"""
    id: int
    title: str


class NewsDetail(BaseModel):
    """详情页新闻"""
    id: int
    title: str
    content: str
    author: str
    publish_time: str


# ================= 随机内容生成器 =================
def random_chinese_title() -> str:
    """生成随机新闻标题"""
    prefixes = ["突发", "重磅", "独家", "最新", "今日", "热点", "特别报道", "深度分析"]
    topics = ["科技发展", "经济形势", "社会新闻", "国际动态", "文化教育", "体育赛事", "娱乐八卦", "健康养生"]
    actions = ["引发关注", "成为焦点", "获得突破", "再创新高", "迎来变革", "取得进展", "备受瞩目", "值得期待"]
    return f"{random.choice(prefixes)}：{random.choice(topics)}{random.choice(actions)}"


def random_content(paragraphs: int = 5) -> str:
    """生成随机新闻正文"""
    sentences = [
        "这是一个令人振奋的消息。",
        "相关专家表示，这一发展具有重要意义。",
        "据了解，该事件引起了广泛关注。",
        "业内人士指出，未来发展前景十分乐观。",
        "根据最新数据显示，相关指标持续向好。",
        "有关部门正在积极推进相关工作。",
        "社会各界对此表示高度关注。",
        "这标志着我们在该领域取得了重要突破。",
        "预计未来还将有更多利好消息发布。",
        "相关政策的出台将进一步推动行业发展。",
    ]
    content_parts = []
    for _ in range(paragraphs):
        paragraph = "".join(random.sample(sentences, k=random.randint(2, 4)))
        content_parts.append(paragraph)
    return "\n\n".join(content_parts)


def random_author() -> str:
    """生成随机作者名"""
    surnames = ["张", "王", "李", "赵", "刘", "陈", "杨", "黄"]
    names = ["明", "华", "强", "伟", "芳", "敏", "静", "军"]
    return f"{random.choice(surnames)}{random.choice(names)}"


def random_time() -> str:
    """生成随机发布时间（最近7天内）"""
    delta = timedelta(days=random.randint(0, 7), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    dt = datetime.now() - delta
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# ================= API接口 =================
@app.get("/news/list", response_model=List[NewsListItem], summary="获取新闻列表")
def get_news_list(page: int = 1, size: int = 10):
    """
    获取新闻列表页
    - **page**: 页码，默认1
    - **size**: 每页数量，默认10
    """
    news_list = []
    start_id = (page - 1) * size + 1
    for i in range(size):
        news_list.append(NewsListItem(
            id=start_id + i,
            title=random_chinese_title()
        ))
    return news_list


@app.get("/news/{news_id}", response_model=NewsDetail, summary="获取新闻详情")
def get_news_detail(news_id: int):
    """
    获取新闻详情页
    - **news_id**: 新闻ID
    """
    return NewsDetail(
        id=news_id,
        title=random_chinese_title(),
        content=random_content(paragraphs=random.randint(3, 6)),
        author=random_author(),
        publish_time=random_time()
    )


# ================= 评论相关 =================
def random_comment_content() -> str:
    """生成随机评论内容"""
    comments = [
        "这篇文章写得真好，非常有深度！",
        "感谢分享，学到了很多新知识。",
        "作者的观点很有见地，支持！",
        "希望能看到更多这样的好文章。",
        "非常赞同作者的分析，逻辑清晰。",
        "这是我今天看到最好的一篇文章。",
        "太棒了！期待后续更新。",
        "收藏了，回头慢慢品读。",
        "虽然有些观点不太认同，但总体不错。",
        "专业的分析，受益匪浅。",
    ]
    return random.choice(comments)


@app.get("/news/{news_id}/comments", response_class=HTMLResponse, summary="获取新闻评论页(HTML)")
def get_news_comments_html(news_id: int, page: int = 1, size: int = 10):
    """
    获取新闻评论页 - 返回HTML格式，可使用xpath解析
    - **news_id**: 新闻ID
    - **page**: 页码，默认1
    - **size**: 每页数量，默认10
    """
    comments_html = ""
    start_id = (page - 1) * size + 1
    
    for i in range(size):
        comment_id = (news_id * 1000) + start_id + i
        author = random_author()
        content = random_comment_content()
        time_str = random_time()
        likes = random.randint(0, 100)
        
        comments_html += f"""
        <div class="comment-item" data-id="{comment_id}">
            <div class="comment-header">
                <span class="author">{author}</span>
                <span class="time">{time_str}</span>
            </div>
            <div class="comment-content">
                <p class="text">{content}</p>
            </div>
            <div class="comment-footer">
                <span class="likes">👍 {likes}</span>
                <a class="reply-link" href="/news/{news_id}/comments/{comment_id}/reply">回复</a>
            </div>
        </div>
        """
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>新闻{news_id}的评论 - 第{page}页</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f5f5f5; padding: 20px; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
            h1 {{ color: #333; }}
            .comment-list {{ background: white; padding: 20px; border-radius: 8px; }}
            .comment-item {{ border-bottom: 1px solid #eee; padding: 15px 0; }}
            .comment-header {{ margin-bottom: 8px; }}
            .author {{ font-weight: bold; color: #333; margin-right: 10px; }}
            .time {{ color: #999; font-size: 12px; }}
            .comment-content {{ color: #666; margin-bottom: 8px; }}
            .comment-footer {{ font-size: 12px; color: #999; }}
            .likes {{ margin-right: 15px; }}
            .reply-link {{ color: #1890ff; text-decoration: none; }}
            .pagination {{ margin-top: 20px; text-align: center; }}
            .pagination a {{ margin: 0 5px; padding: 5px 10px; background: #1890ff; color: white; 
                           text-decoration: none; border-radius: 4px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>新闻 #{news_id} 的评论</h1>
            <div class="comment-list" id="commentList">
                {comments_html}
            </div>
            <div class="pagination">
                <a href="/news/{news_id}/comments?page={max(1, page-1)}&size={size}">上一页</a>
                <span>第 {page} 页</span>
                <a href="/news/{news_id}/comments?page={page+1}&size={size}">下一页</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/", summary="首页")
def root():
    """API根路径，返回欢迎信息"""
    return {
        "message": "欢迎访问新闻服务API",
        "endpoints": {
            "列表页": "/news/list?page=1&size=10",
            "详情页": "/news/{news_id}",
            "评论页(HTML)": "/news/{news_id}/comments?page=1&size=10",
            "API文档": "/docs"
        }
    }


if __name__ == "__main__":
    print("=" * 50)
    print("新闻服务端启动中...")
    print("API文档: http://127.0.0.1:7000/docs")
    print("=" * 50)
    uvicorn.run(app, host="127.0.0.1", port=7000)

`````

--- **end of file: demo_crawler/news_server.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/boost_scrapy_imp/boost_scrapy_demo.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/boost_scrapy_imp/boost_scrapy_demo.py`

#### 📝 Module Docstring

`````
================================================================================
         新闻爬虫 Demo - 使用 boost_scrapy 框架 (Scrapy 风格)
================================================================================

🎯 本文件目的：
   演示如何使用 boost_scrapy 框架实现 Scrapy 风格的爬虫。
   爬取流程: 列表页 -> 详情页 -> 评论页

📊 使用方式：
   1. 先启动 news_server.py:
      cd demo_crawler
      python news_server.py
   
   2. 运行本爬虫:
      cd demo_crawler/boost_scrapy_imp
      python boost_scrapy_demo.py

================================================================================
`````

#### 📦 Imports

- `import sys`
- `import os`
- `from boost_scrapy import Spider`
- `from boost_scrapy import Request`
- `from boost_scrapy import Engine`
- `from items import NewsItem`
- `from items import CommentItem`
- `from middlewares import MyProxyMiddleware`
- `from middlewares import MyUserAgentMiddleware`
- `from boost_scrapy import SQLModelPipeline`
- `from boost_scrapy import ConsolePipeline`

#### 🏛️ Classes (1)

##### 📌 `class NewsSpider(Spider)`
*Line: 40*

**Docstring:**
`````
新闻爬虫 - 使用 boost_scrapy 实现 (Scrapy 风格)

爬取流程: 列表页(JSON) -> 详情页(JSON) -> 评论页(HTML/xpath)

⭐ 核心用法:
1. yield Request(url, callback=self.xxx) - 发起请求并指定回调
2. response.meta['key'] - 获取传递的上下文数据
3. response.resp_dict - 解析 JSON 响应
4. response.xpath() / response.css() - XPath/CSS 选择器
5. yield Item(...) - 数据自动流经 Pipeline
`````

**Public Methods (5):**
- `def start_requests(self)`
  - **Docstring:**
  `````
  初始请求入口 - 类似 Scrapy
  
  yield Request(url, callback=self.xxx) 指定回调函数
  `````
- `def parse_list(self, response)`
  - **Docstring:**
  `````
  解析列表页 - JSON 响应
  
  - response.resp_dict: 自动解析 JSON
  - response.meta: 获取传递的上下文数据
  - yield Request(...): 发起新请求
  `````
- `def parse_detail(self, response)`
  - **Docstring:**
  `````
  解析详情页 - 获取新闻内容并 yield Item 入库
  
  - yield Item: 数据自动流经 Pipeline
  `````
- `def parse_comments(self, response)`
  - **Docstring:**
  `````
  解析评论页 - 使用 XPath 解析 HTML
  
  - response.xpath(): XPath 选择器（和 Scrapy 一样）
  - response.css(): CSS 选择器
  `````
- `def closed(self, reason)`
  - *爬虫关闭时回调*

**Class Variables (3):**
- `name = 'news_spider'`
- `custom_settings = {'concurrent_num': 5, 'qps': 10, 'max_retry_times': 3}`
- `BASE_URL = 'http://127.0.0.1:7000'`


---

`````python
# coding=utf-8
"""
================================================================================
         新闻爬虫 Demo - 使用 boost_scrapy 框架 (Scrapy 风格)
================================================================================

🎯 本文件目的：
   演示如何使用 boost_scrapy 框架实现 Scrapy 风格的爬虫。
   爬取流程: 列表页 -> 详情页 -> 评论页

📊 使用方式：
   1. 先启动 news_server.py:
      cd demo_crawler
      python news_server.py
   
   2. 运行本爬虫:
      cd demo_crawler/boost_scrapy_imp
      python boost_scrapy_demo.py

================================================================================
"""

import sys
import os

# # 确保能够导入项目模块
# project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)



from boost_scrapy import Spider, Request, Engine
from items import NewsItem, CommentItem
from middlewares import MyProxyMiddleware, MyUserAgentMiddleware
from boost_scrapy import SQLModelPipeline, ConsolePipeline

# ================= 定义 Spider =================

class NewsSpider(Spider):
    """
    新闻爬虫 - 使用 boost_scrapy 实现 (Scrapy 风格)
    
    爬取流程: 列表页(JSON) -> 详情页(JSON) -> 评论页(HTML/xpath)
    
    ⭐ 核心用法:
    1. yield Request(url, callback=self.xxx) - 发起请求并指定回调
    2. response.meta['key'] - 获取传递的上下文数据
    3. response.resp_dict - 解析 JSON 响应
    4. response.xpath() / response.css() - XPath/CSS 选择器
    5. yield Item(...) - 数据自动流经 Pipeline
    """
    
    name = "news_spider"
    
    # 自定义配置（可选）
    custom_settings = {
        'concurrent_num': 5,
        'qps': 10,
        'max_retry_times': 3,
    }
    
    BASE_URL = "http://127.0.0.1:7000"
    
    def start_requests(self):
        """
        初始请求入口 - 类似 Scrapy
        
        yield Request(url, callback=self.xxx) 指定回调函数
        """
        print()
        print("=" * 60)
        print("  boost_scrapy 新闻爬虫 Demo")
        print("  Scrapy 风格: yield Request + callback")
        print("=" * 60)
        print()
        
        # 爬取前3页列表，每页5条
        for page in range(1, 4):
            url = f"{self.BASE_URL}/news/list?page={page}&size=5"
            print(f"[发布任务] 列表页 第{page}页")
            yield Request(url, callback=self.parse_list, meta={'page': page},
                        #    dont_filter=True
                          )
    
    def parse_list(self, response):
        """
        解析列表页 - JSON 响应
        
        - response.resp_dict: 自动解析 JSON
        - response.meta: 获取传递的上下文数据
        - yield Request(...): 发起新请求
        """
        page = response.meta.get('page', 1)
        news_list = response.resp_dict
        
        print(f"[列表页] 第{page}页 获取到 {len(news_list)} 条新闻")
        
        for news in news_list:
            news_id = news["id"]
            title = news["title"]
            print(f"  -> 发现新闻 [ID: {news_id}] {title}")
            
            # yield Request 发起详情页请求
            yield Request(
                f"{self.BASE_URL}/news/{news_id}",
                callback=self.parse_detail,
                meta={'news_id': news_id, 'title': title}
            )
    
    def parse_detail(self, response):
        """
        解析详情页 - 获取新闻内容并 yield Item 入库
        
        - yield Item: 数据自动流经 Pipeline
        """
        news_id = response.meta['news_id']
        title = response.meta['title']
        news = response.resp_dict
        
        print(f"[详情页] 新闻ID: {news_id} - {title}")
        
        # yield Item - 自动流经 Pipeline
        yield NewsItem(
            news_id=news_id,
            title=title,
            author=news.get("author", "未知"),
            publish_time=news.get("publish_time", ""),
            content=news.get("content", ""),
        )
        
        # 继续爬取评论页（前2页）
        for page in range(1, 3):
            yield Request(
                f"{self.BASE_URL}/news/{news_id}/comments?page={page}&size=10",
                callback=self.parse_comments,
                meta={'news_id': news_id, 'title': title, 'page': page}
            )
            print(f"  -> 已发布: 爬取新闻{news_id}的第{page}页评论")
    
    def parse_comments(self, response):
        """
        解析评论页 - 使用 XPath 解析 HTML
        
        - response.xpath(): XPath 选择器（和 Scrapy 一样）
        - response.css(): CSS 选择器
        """
        news_id = response.meta['news_id']
        page = response.meta['page']
        
        print(f"[评论页] 新闻{news_id} 第{page}页")
        
        # 使用 xpath 解析评论 (和 Scrapy 用法一致!)
        comments = response.xpath('//div[@class="comment-item"]')
        print(f"  找到 {len(comments)} 条评论")
        
        for item in comments:
            yield CommentItem(
                news_id=news_id,
                comment_id=item.xpath('./@data-id').get(),
                author=item.xpath('.//span[@class="author"]/text()').get(),
                content=item.xpath('.//p[@class="text"]/text()').get(),
                likes=item.xpath('.//span[@class="likes"]/text()').get(),
            )
    
    def closed(self, reason):
        """爬虫关闭时回调"""
        print(f"\n[Spider] 爬虫关闭: {reason}")


# ================= 启动爬虫 =================

if __name__ == "__main__":
    print()
    print("⚠️ 请先确保 news_server.py 正在运行:")
    print("   cd demo_crawler")
    print("   python news_server.py")
    print()
    
    # 创建引擎并运行爬虫
    # - pipelines: 数据入库管道
    # - middlewares: 中间件（用户自定义，演示 UA/代理 切换）
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'boost_scrapy_data.db')
    
    engine = Engine(
        # Engine 里面的入参可以放在全局字典，多个spider共享，也可以放在你的Spider的custom_settings的字典中。
        pipelines=[ConsolePipeline(),SQLModelPipeline(db_url=f'sqlite:///{db_path}'), ],  
        middlewares=[
            MyUserAgentMiddleware(),   # 🔄 自定义 UA 中间件：每次请求随机切换 UA
            # MyProxyMiddleware(),     # 🌐 自定义代理中间件：从内存/Redis 获取代理（取消注释启用）
        ],
        use_funboost=True, # use_funboost为False就使用单线程顺序爬虫，可以用于调试。
        enable_filter=False, # 默认是否启动过滤，也可以在 yield Request 的 dont_filter=True 来禁用
    )
    engine.run(NewsSpider)



`````

--- **end of file: demo_crawler/boost_scrapy_imp/boost_scrapy_demo.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/boost_scrapy_imp/items.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/boost_scrapy_imp/items.py`

#### 📦 Imports

- `from sqlmodel import SQLModel`
- `from sqlmodel import Field`
- `from typing import Optional`
- `from sqlalchemy import Text`
- `from boost_scrapy import Item`

#### 🏛️ Classes (2)

##### 📌 `class NewsItem(Item)`
*Line: 8*

**Docstring:**
`````
新闻详情数据项 (映射数据库表 news_detail)
`````

**Class Variables (7):**
- `__tablename__ = 'news_detail'`
- `id: Optional[int] = Field(default=None, primary_key=True)`
- `news_id: int`
- `title: str = Field(max_length=200)`
- `author: Optional[str] = Field(default=None, max_length=50)`
- `publish_time: Optional[str] = Field(default=None, max_length=50)`
- `content: Optional[str] = Field(default=None, sa_type=Text)`

##### 📌 `class CommentItem(Item)`
*Line: 20*

**Docstring:**
`````
评论数据项 (映射数据库表 comments)
`````

**Class Variables (7):**
- `__tablename__ = 'comments'`
- `id: Optional[int] = Field(default=None, primary_key=True)`
- `news_id: int`
- `comment_id: str = Field(max_length=50)`
- `author: Optional[str] = Field(default=None, max_length=50)`
- `content: Optional[str] = Field(default=None, sa_type=Text)`
- `likes: Optional[str] = Field(default=None, max_length=20)`


---

`````python
from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Text
from boost_scrapy import Item

# ================= 定义 Item (继承 SQLModel) =================

class NewsItem(Item, table=True):
    """新闻详情数据项 (映射数据库表 news_detail)"""
    __tablename__ = "news_detail"

    id: Optional[int] = Field(default=None, primary_key=True)
    news_id: int
    title: str = Field(max_length=200) # 指定 VARCHAR(200)
    author: Optional[str] = Field(default=None, max_length=50)
    publish_time: Optional[str] = Field(default=None, max_length=50)
    content: Optional[str] = Field(default=None, sa_type=Text) # 指定使用 TEXT 类型（不限长度）


class CommentItem(Item, table=True):
    """评论数据项 (映射数据库表 comments)"""
    __tablename__ = "comments"

    id: Optional[int] = Field(default=None, primary_key=True)
    news_id: int
    comment_id: str = Field(max_length=50)
    author: Optional[str] = Field(default=None, max_length=50)
    content: Optional[str] = Field(default=None, sa_type=Text)
    likes: Optional[str] = Field(default=None, max_length=20)
`````

--- **end of file: demo_crawler/boost_scrapy_imp/items.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/boost_scrapy_imp/middlewares.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/boost_scrapy_imp/middlewares.py`

#### 📦 Imports

- `from boost_scrapy import Middleware`
- `import random`

#### 🏛️ Classes (2)

##### 📌 `class MyProxyMiddleware(Middleware)`
*Line: 8*

**Docstring:**
`````
自定义代理中间件 - 演示用户如何从 Redis/内存 获取代理 IP

用户可以根据实际情况修改 get_proxy() 方法：
- 从 Redis 代理池获取
- 从内存代理列表获取
- 从第三方代理 API 获取
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self)`
  - **Parameters:**
    - `self`

**Public Methods (2):**
- `def get_proxy(self) -> str`
  - **Docstring:**
  `````
  获取代理 IP（用户可自定义实现）
  
  示例：
  - 从内存列表随机获取
  - 从 Redis 的 set/list 获取
  - 从代理服务商 API 获取
  `````
- `def process_request(self, request, spider)`
  - *每次请求时自动设置代理*

##### 📌 `class MyUserAgentMiddleware(Middleware)`
*Line: 58*

**Docstring:**
`````
自定义 UA 中间件 - 演示用户如何切换 UserAgent
`````

**Public Methods (1):**
- `def process_request(self, request, spider)`
  - *每次请求时随机切换 UA*

**Class Variables (1):**
- `USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0']`


---

`````python

from boost_scrapy import Middleware
import random


# ================= 自定义 Middleware（演示代理切换） =================

class MyProxyMiddleware(Middleware):
    """
    自定义代理中间件 - 演示用户如何从 Redis/内存 获取代理 IP
    
    用户可以根据实际情况修改 get_proxy() 方法：
    - 从 Redis 代理池获取
    - 从内存代理列表获取
    - 从第三方代理 API 获取
    """
    
    def __init__(self):
        # 模拟内存代理池（实际项目中可以从 Redis 获取）
        self.proxy_pool = [
            'http://proxy1.example.com:8080',
            'http://proxy2.example.com:8080',
            'http://proxy3.example.com:8080',
        ]
        # 如果使用 Redis:
        # import redis
        # self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def get_proxy(self) -> str:
        """
        获取代理 IP（用户可自定义实现）
        
        示例：
        - 从内存列表随机获取
        - 从 Redis 的 set/list 获取
        - 从代理服务商 API 获取
        """
        # 方式1：从内存列表随机选一个
        proxy = random.choice(self.proxy_pool)
        
        # 方式2：从 Redis 获取（示例）
        # proxy = self.redis_client.srandmember('proxy_pool').decode()
        
        # 方式3：从代理服务商 API 获取（示例）
        # resp = requests.get('http://proxy-api.com/get')
        # proxy = resp.json()['proxy']
        
        return proxy
    
    def process_request(self, request, spider):
        """每次请求时自动设置代理"""
        proxy = self.get_proxy()
        request.kwargs['proxies'] = {'http': proxy, 'https': proxy}
        print(f"  🌐 [MyProxyMiddleware] 使用代理: {proxy}")
        return None


class MyUserAgentMiddleware(Middleware):
    """
    自定义 UA 中间件 - 演示用户如何切换 UserAgent
    """
    
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    ]
    
    def process_request(self, request, spider):
        """每次请求时随机切换 UA"""
        ua = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = ua
        print(f"  🔄 [MyUserAgentMiddleware] UA: {ua[:50]}...")
        return None
`````

--- **end of file: demo_crawler/boost_scrapy_imp/middlewares.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/boost_scrapy_imp/pipelines.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/boost_scrapy_imp/pipelines.py`

#### 📦 Imports

- `from boost_scrapy.pipeline import SQLModelPipeline`
- `from boost_scrapy.pipeline import ConsolePipeline`
- `from boost_scrapy import Pipeline`


---

`````python

from boost_scrapy.pipeline import SQLModelPipeline, ConsolePipeline
from boost_scrapy import Pipeline

# ================= 定义 Pipeline =================

# 这里可以留空，或者重新导出，或者如果需要自定义扩展，再继承
# 目前直接从框架导入即可

# 为了兼容 demo 中的引用，我们重新导出
__all__ = ['SQLModelPipeline', 'ConsolePipeline', ]

# 如果你想扩展功能：
# class MyCustomPipeline(SQLModelPipeline):
#     def process_item(self, item, spider):
#         print("Before save...")
#         super().process_item(item, spider)
#         print("After save...")
#         return item
`````

--- **end of file: demo_crawler/boost_scrapy_imp/pipelines.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/boost_spider_imp/boost_spider_crawler.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/boost_spider_imp/boost_spider_crawler.py`

#### 📝 Module Docstring

`````
================================================================================
            新闻爬虫 - 使用 Funboost + boost_spider 实现分布式爬取
================================================================================

🎯 本文件目的：
   演示如何使用 Funboost 框架实现列表页、详情页、评论页的三层爬取流程。
   使用 boost_spider 的 SpiderResponse 进行 xpath 解析（你羡慕的 Scrapy selector 功能）

================================================================================
                  ⭐ Funboost + boost_spider 核心优势对比表
================================================================================

📊 与 Scrapy 对比（详见 ../scrapy_imp/scrapy_spider_crawler.py）：
┌──────────────────────────┬────────────────────────────────────────────────────────┐
│       ⭐ 优势项           │              Funboost + boost_spider 实现              │
├──────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. 单文件开箱即用        │ 无需创建项目结构，单个 .py 文件即可运行                │
│ 2. 40+ 中间件选择        │ Redis/RabbitMQ/Kafka/MongoDB/SQLite/NSQ/...           │
│ 3. 原生分布式            │ 改一个参数 broker_kind 立刻分布式，无需额外插件        │
│ 4. 精确 QPS 流控         │ qps=5 精确每秒5次，支持分布式统一流控                 │
│ 5. 一键任务去重          │ do_task_filtering=True 即可去重                       │
│ 6. 自动重试              │ max_retry_times=3 自动重试                            │
│ 7. 消息确认 ACK          │ REDIS_ACK_ABLE 确保任务不丢失，支持断点续爬           │
│ 8. 外部动态任务注入      │ ⭐ HTTP/API 随时注入二级任务（Scrapy 无法实现！）      │
│ 9. 分组启动消费          │ BoostersManager.consume_group("xxx") 一键启动一组     │
│ 10. RPC 获取结果         │ is_using_rpc_mode=True 支持获取消费结果               │
│ 11. XPath/CSS 解析       │ SpiderResponse.xpath()/css() 和 Scrapy 一样强大       │
│ 12. 代理/UA/Cookie管理   │ RequestClient 内置代理轮换、UA随机、Session管理       │
│ 13. 内置监控面板         │ funboost_web_manager 可视化监控                       │
│ 14. 定时任务             │ ApsJobAdder 内置 APScheduler                         │
│ 15. 平铺直叙的代码风格   │ 无 callback 地狱，函数之间直接 .push() 调用           │
└──────────────────────────┴────────────────────────────────────────────────────────┘

⭐ 核心优势：外部系统实时动态注入"二级任务"
───────────────────────────────────────────
场景：运营人员在后台发现某条新闻需要重新爬取
Funboost：直接调用 crawl_detail_page.push(news_id=12345)
Scrapy：❌ 无法实现，只能从 start_urls 开始爬取

这是 Funboost 对 Scrapy 的【降维打击】！
================================================================================
`````

#### 📦 Imports

- `import httpx`
- `from boost_spider import boost`
- `from boost_spider import BoosterParams`
- `from boost_spider import BrokerEnum`
- `from boost_spider import ctrl_c_recv`
- `from boost_spider import BoostersManager`
- `from boost_spider import RequestClient`
- `from boost_spider import ConcurrentModeEnum`
- `from boost_spider import TaskOptions`
- `from boost_spider.sink.dataset_sink import DatasetSink`

#### 🏛️ Classes (1)

##### 📌 `class BaseCrawlerParams(BoosterParams)`
*Line: 78*

**Docstring:**
`````
爬虫通用配置基类

⭐【Funboost 优势 2】配置集中：所有配置在装饰器一个地方
⭐【Funboost 优势 3】类型安全：BoosterParams 是 Pydantic 模型，IDE 可以自动补全和类型检查
💔  Scrapy 对比：settings 是 Python 字典，没有类型检查，容易拼错键名

- 统一使用 Redis ACK Able 中间件（增强数据安全性）
- 统一归属到 news_crawler_group 分组
`````

**Class Variables (3):**
- `broker_kind: str = BrokerEnum.REDIS_ACK_ABLE`
- `booster_group: str = 'news_crawler_group'`
- `max_retry_times: int = 3`

#### 🔧 Public Functions (3)

- `def crawl_list_page(page: int = 1, size: int = 10)` `boost(BaseCrawlerParams(queue_name='news_crawler_list_page', qps=2, concurrent_num=5))`
  - *Line: 115*
  - **Docstring:**
  `````
  爬取新闻列表页
  
  ⭐【Funboost 优势 9】平铺直叙的代码风格
  - 无需 callback 回调，直接 crawl_detail_page.push() 发起下一层任务
  - 代码逻辑清晰，如同编写普通脚本
  💔  Scrapy 对比：callback 回调地狱，parse_list -> parse_detail -> parse_comments
  
  ⭐【Funboost 优势 10】外部动态任务注入（核心降维打击优势！）
  - 运营人员可以随时调用 crawl_list_page.push(page=5) 注入新任务
  - 支持 HTTP API 注入（funboost.faas）
  💔  Scrapy 对比：❌ 无法从外部实时注入二级任务，只能从 start_urls 开始
  
  - 请求列表页API
  - 解析返回的新闻列表
  - 推送详情页爬取任务
  `````

- `async def crawl_detail_page(news_id: int, title: str)` `boost(BaseCrawlerParams(queue_name='news_crawler_detail_page', qps=5, concurrent_num=50, concurrent_mode=ConcurrentModeEnum.ASYNC, do_task_filtering=True, task_filtering_expire_seconds=600))`
  - *Line: 176*
  - **Docstring:**
  `````
  爬取新闻详情页（使用 httpx 异步客户端）
  
  ⭐【Funboost 优势 12】函数参数类型安全
  - news_id: int, title: str 有类型标注
  - IDE 可以检查类型，push 时参数错误会提示
  💔  Scrapy 对比：通过 response.meta 传参，容易出错
  
  - 请求详情页API
  - 解析并保存新闻内容
  - 推送评论页爬取任务
  `````

- `def crawl_comments_page(news_id: int, title: str, page: int = 1, size: int = 10)` `boost(BaseCrawlerParams(queue_name='news_crawler_comments_page', qps=10, concurrent_num=15, retry_interval=1, do_task_filtering=True))`
  - *Line: 254*
  - **Docstring:**
  `````
  爬取新闻评论页 - 使用 boost_spider 的 SpiderResponse 进行 xpath 解析
  
  ⭐【boost_spider 优势】SpiderResponse 拥有你羡慕的 Scrapy selector 功能！
  - resp.xpath('//div[@class="xxx"]')  -> XPath 选择器
  - resp.css('div.xxx')                -> CSS 选择器  
  - resp.re_search(pattern)            -> 正则匹配
  - resp.resp_dict                     -> 自动解析 JSON
  - resp.selector                      -> parsel.Selector 对象
  
  同时 RequestClient 还内置了：
  - 代理管理（多代理商轮换）：proxy_name_list=['kuai', 'abuyun']
  - 请求自动重试：request_retry_times=3
  - UA 随机化：is_change_ua_every_request=True
  - Session/Cookie 管理：自动保持会话
  💔  Scrapy 对比：代理/重试/UA 都需要自己写中间件配置
  
  - 请求评论页HTML
  - 使用xpath解析评论列表
  - 提取评论信息
  `````


---

`````python
"""
================================================================================
            新闻爬虫 - 使用 Funboost + boost_spider 实现分布式爬取
================================================================================

🎯 本文件目的：
   演示如何使用 Funboost 框架实现列表页、详情页、评论页的三层爬取流程。
   使用 boost_spider 的 SpiderResponse 进行 xpath 解析（你羡慕的 Scrapy selector 功能）

================================================================================
                  ⭐ Funboost + boost_spider 核心优势对比表
================================================================================

📊 与 Scrapy 对比（详见 ../scrapy_imp/scrapy_spider_crawler.py）：
┌──────────────────────────┬────────────────────────────────────────────────────────┐
│       ⭐ 优势项           │              Funboost + boost_spider 实现              │
├──────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. 单文件开箱即用        │ 无需创建项目结构，单个 .py 文件即可运行                │
│ 2. 40+ 中间件选择        │ Redis/RabbitMQ/Kafka/MongoDB/SQLite/NSQ/...           │
│ 3. 原生分布式            │ 改一个参数 broker_kind 立刻分布式，无需额外插件        │
│ 4. 精确 QPS 流控         │ qps=5 精确每秒5次，支持分布式统一流控                 │
│ 5. 一键任务去重          │ do_task_filtering=True 即可去重                       │
│ 6. 自动重试              │ max_retry_times=3 自动重试                            │
│ 7. 消息确认 ACK          │ REDIS_ACK_ABLE 确保任务不丢失，支持断点续爬           │
│ 8. 外部动态任务注入      │ ⭐ HTTP/API 随时注入二级任务（Scrapy 无法实现！）      │
│ 9. 分组启动消费          │ BoostersManager.consume_group("xxx") 一键启动一组     │
│ 10. RPC 获取结果         │ is_using_rpc_mode=True 支持获取消费结果               │
│ 11. XPath/CSS 解析       │ SpiderResponse.xpath()/css() 和 Scrapy 一样强大       │
│ 12. 代理/UA/Cookie管理   │ RequestClient 内置代理轮换、UA随机、Session管理       │
│ 13. 内置监控面板         │ funboost_web_manager 可视化监控                       │
│ 14. 定时任务             │ ApsJobAdder 内置 APScheduler                         │
│ 15. 平铺直叙的代码风格   │ 无 callback 地狱，函数之间直接 .push() 调用           │
└──────────────────────────┴────────────────────────────────────────────────────────┘

⭐ 核心优势：外部系统实时动态注入"二级任务"
───────────────────────────────────────────
场景：运营人员在后台发现某条新闻需要重新爬取
Funboost：直接调用 crawl_detail_page.push(news_id=12345)
Scrapy：❌ 无法实现，只能从 start_urls 开始爬取

这是 Funboost 对 Scrapy 的【降维打击】！
================================================================================
"""

import httpx  # ⭐ httpx 异步请求库
from boost_spider import boost, BoosterParams, BrokerEnum, ctrl_c_recv, BoostersManager, RequestClient, ConcurrentModeEnum,TaskOptions
# RequestClient.get()/request() 返回 SpiderResponse 对象，支持 xpath/css 解析

# ⭐【boost_spider 优势 13】DatasetSink：一行代码保存到 SQLite/MySQL/PostgreSQL
# 💔  Scrapy 对比：需要定义 Item、配置 Pipeline、在 settings 中启用 Pipeline
from boost_spider.sink.dataset_sink import DatasetSink



# ================= 配置 =================
BASE_URL = "http://127.0.0.1:7000"

# ⭐ DatasetSink 初始化：一行代码，连接 SQLite 数据库
# 💔 Scrapy 对比：需要在 settings.py 配置 ITEM_PIPELINES，再定义 Pipeline 类
DB_URL = "sqlite:///demo_crawler/boost_spider_imp/boost_spider_crawled_data.db"  # SQLite 数据库文件
data_sink = DatasetSink(DB_URL)

# ⭐【httpx 全局异步客户端】 演示 funboost 能使用 asyncio 生态爬虫，独一档，feapder和scrapy无法比拟。
httpx_async_client = httpx.AsyncClient(
    timeout=httpx.Timeout(10.0),
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://news.example.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
)



# ================= 爬虫公共配置 =================
# ⭐【Funboost 优势 1】配置继承：子类继承 BoosterParams，避免重复配置
# 💔  Scrapy 对比：settings.py + custom_settings + 中间件，配置分散在多处
class BaseCrawlerParams(BoosterParams):
    """
    爬虫通用配置基类
    
    ⭐【Funboost 优势 2】配置集中：所有配置在装饰器一个地方
    ⭐【Funboost 优势 3】类型安全：BoosterParams 是 Pydantic 模型，IDE 可以自动补全和类型检查
    💔  Scrapy 对比：settings 是 Python 字典，没有类型检查，容易拼错键名
    
    - 统一使用 Redis ACK Able 中间件（增强数据安全性）
    - 统一归属到 news_crawler_group 分组
    """
    # ⭐【Funboost 优势 4】40+ 种中间件选择
    # 💔  Scrapy 对比：仅支持内存队列，分布式需要 scrapy-redis 插件
    broker_kind:str = BrokerEnum.REDIS_ACK_ABLE  # 使用Redis ACK模式，确保消息不丢失，支持断点续爬
    
    # ⭐【Funboost 优势 5】分组管理：一个参数即可分组
    # 💔  Scrapy 对比：无分组概念，需要手动管理多个 Spider
    booster_group:str = "news_crawler_group"     # 统一分组，BoostersManager.consume_group("xxx")一键启动
    
    # ⭐【Funboost 优势 6】自动重试：一个参数搞定
    # 💔  Scrapy 对比：需要配置 RETRY_ENABLED 和 RETRY_TIMES 等多个 settings
    max_retry_times :int= 3                      # 默认重试3次
  
  


# ================= 爬虫函数定义 =================
# ⭐【Funboost 优势 7】装饰器即分布式：普通函数 + @boost = 分布式消费函数
# 💔  Scrapy 对比：必须继承 Spider 类，遵循框架约定

@boost(BaseCrawlerParams(
    queue_name="news_crawler_list_page",
    # ⭐【Funboost 优势 8】精确 QPS 流控：qps=2 表示精确每秒2次
    # 💔  Scrapy 对比：DOWNLOAD_DELAY 是近似控制，不精确
    qps=2,  # 每秒最多请求2次列表页，支持分布式统一流控
    concurrent_num=5,  # 并发数5
))
def crawl_list_page(page: int = 1, size: int = 10):
    """
    爬取新闻列表页
    
    ⭐【Funboost 优势 9】平铺直叙的代码风格
    - 无需 callback 回调，直接 crawl_detail_page.push() 发起下一层任务
    - 代码逻辑清晰，如同编写普通脚本
    💔  Scrapy 对比：callback 回调地狱，parse_list -> parse_detail -> parse_comments
    
    ⭐【Funboost 优势 10】外部动态任务注入（核心降维打击优势！）
    - 运营人员可以随时调用 crawl_list_page.push(page=5) 注入新任务
    - 支持 HTTP API 注入（funboost.faas）
    💔  Scrapy 对比：❌ 无法从外部实时注入二级任务，只能从 start_urls 开始
    
    - 请求列表页API
    - 解析返回的新闻列表
    - 推送详情页爬取任务
    """
    url = f"{BASE_URL}/news/list?page={page}&size={size}"
    print(f"[列表页] 正在爬取: {url}")
    
    
    # ⭐【boost_spider 优势 14】动态请求头：RequestClient 内置 UA 随机化
    # 💔  Scrapy 对比：需要定义 Downloader Middleware 类，配置 settings
    client = RequestClient(
        proxy_name_list=None,        # 可设置代理列表，如 ['kuai', 'abuyun']
        request_retry_times=3,       # 请求重试次数
        is_change_ua_every_request=True,  # ⭐ 只需一行代码每次请求随机切换 UA！
    )
    # 可以设置自定义请求头
    custom_headers = {
        'Referer': 'https://news.example.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = client.get(url, timeout=10, headers=custom_headers)
    news_list = response.resp_dict  # ⭐ SpiderResponse 自动解析 JSON
    
    print(f"[列表页] 获取到 {len(news_list)} 条新闻")
    
    # 遍历新闻列表，推送详情页爬取任务
    for news_item in news_list:
        news_id = news_item["id"]
        title = news_item["title"]
        print(f"  -> 发现新闻 [ID: {news_id}] {title}")
        # 推送详情页爬取任务
        crawl_detail_page.push(news_id=news_id, title=title)
    
    return {"status": "success", "page": page, "count": len(news_list)}
    

@boost(BaseCrawlerParams(
    queue_name="news_crawler_detail_page",
    qps=5,  # 每秒最多请求5次详情页
    concurrent_num=50,  # ⭐ 协程并发数可以开很大
    concurrent_mode=ConcurrentModeEnum.ASYNC,  # 使用 asyncio 协程并发模式
    # ⭐【Funboost 优势 11】一键任务去重
    # 💔  Scrapy 对比：需要配置 DUPEFILTER_CLASS，可能还需要 BloomFilter 插件
    do_task_filtering=True, # 通过函数入参自动去重，无需任何配置
    task_filtering_expire_seconds = 600, # 仅在600秒之内去重，支持过期时间控制
    
))
async def crawl_detail_page(news_id: int, title: str):
    """
    爬取新闻详情页（使用 httpx 异步客户端）
    
    ⭐【Funboost 优势 12】函数参数类型安全
    - news_id: int, title: str 有类型标注
    - IDE 可以检查类型，push 时参数错误会提示
    💔  Scrapy 对比：通过 response.meta 传参，容易出错
    
    - 请求详情页API
    - 解析并保存新闻内容
    - 推送评论页爬取任务
    """
    url = f"{BASE_URL}/news/{news_id}"
    print(f"[详情页-httpx异步] 正在爬取: {url}")
    
    # ⭐ 使用 httpx 全局异步客户端
    response = await httpx_async_client.get(url)
    response.raise_for_status()
    news_detail = response.json()
    
    # 提取新闻内容
    content = news_detail.get("content", "")
    author = news_detail.get("author", "未知")
    publish_time = news_detail.get("publish_time", "未知")
    
    # 输出爬取结果（实际项目中可以保存到数据库）
    print("=" * 60)
    print(f"[爬取成功] 新闻ID: {news_id}")
    print(f"标题: {title}")
    print(f"作者: {author}")
    print(f"发布时间: {publish_time}")
    print(f"正文预览: {content[:100]}...")
    print("=" * 60)
    
    # 推送评论页爬取任务（爬取前2页评论）
    for page in range(1, 3):
        crawl_comments_page.publish(
            dict(news_id=news_id, title=title, page=page),
                task_options=TaskOptions(do_task_filtering=True,
                # filter_str是funboost核心去重过滤大招，可以只根据部分入参去重，吊打scrapy那种整个url加post请求的data或者json来生成hash md5去重指纹。
                # 如果body很大，还有一些很长的不重要的文字，会干扰去重，导致无法命中去重。
                # 例如假设body里面必须包含当前时间或者一个uuid随机数，那么就没法命中去重了，
                # funboost中 你可以在 Body 里塞入任何垃圾数据、随机数，只要 filter_str 没变，系统就认定它是重复的。完全无需写复杂的指纹计算代码。
                filter_str=f"news_id={news_id}&page={page}")
        )
        print(f"  -> 已发布: 爬取新闻{news_id}的第{page}页评论")
    
    # ⭐【boost_spider 优势】DatasetSink 一行代码保存到 SQLite！
    # 💔  Scrapy 对比：需要 yield item -> Pipeline -> 数据库
    news_data = {
        "news_id": news_id,
        "title": title,
        "author": author,
        "publish_time": publish_time,
        "content": content,
    }
    data_sink.save("news_detail", news_data)  # ⭐ 一行代码保存！
    print(f"  💾 [已保存到SQLite] news_detail 表")
    
    return {
        "status": "success",
        "news_id": news_id,
        "title": title,
        "content_length": len(content)
    }
    
 


@boost(BaseCrawlerParams(
    queue_name="news_crawler_comments_page",
    qps=10,  # 每秒最多请求10次评论页
    concurrent_num=15,  # 并发数15
    retry_interval=1,   # 这里可以覆盖基类的配置,
    do_task_filtering=True, # 通过函数入参自动去重
    # task_filtering_expire_seconds = 600, # 不配置有效期就是永久过滤。
))
def crawl_comments_page(news_id: int, title: str, page: int = 1, size: int = 10):
    """
    爬取新闻评论页 - 使用 boost_spider 的 SpiderResponse 进行 xpath 解析
    
    ⭐【boost_spider 优势】SpiderResponse 拥有你羡慕的 Scrapy selector 功能！
    - resp.xpath('//div[@class="xxx"]')  -> XPath 选择器
    - resp.css('div.xxx')                -> CSS 选择器  
    - resp.re_search(pattern)            -> 正则匹配
    - resp.resp_dict                     -> 自动解析 JSON
    - resp.selector                      -> parsel.Selector 对象
    
    同时 RequestClient 还内置了：
    - 代理管理（多代理商轮换）：proxy_name_list=['kuai', 'abuyun']
    - 请求自动重试：request_retry_times=3
    - UA 随机化：is_change_ua_every_request=True
    - Session/Cookie 管理：自动保持会话
    💔  Scrapy 对比：代理/重试/UA 都需要自己写中间件配置
    
    - 请求评论页HTML
    - 使用xpath解析评论列表
    - 提取评论信息
    """
    url = f"{BASE_URL}/news/{news_id}/comments?page={page}&size={size}"
    print(f"[评论页] 正在爬取: {url}")
    
    
    # 使用 boost_spider 的 RequestClient 发送请求
    # RequestClient.request() 返回 SpiderResponse 对象，支持 xpath/css 解析
    client = RequestClient(proxy_name_list=None,request_retry_times=3,is_change_ua_every_request=True)
    resp = client.get(url, timeout=10)
    
    # 使用 xpath 解析 HTML 页面
    # 通过 resp.selector 属性获取 parsel.Selector 对象
    print("[评论页] 使用 xpath 解析评论...")


    # 提取所有评论项
    # boost_spider的 resp是 SpiderResponse类型，自带你羡慕的scrapy那样的xpath css方法
    comment_items = resp.xpath('//div[@class="comment-item"]') 
    print(f"[评论页] 找到 {len(comment_items)} 条评论")
    
    comments = []
    for item in comment_items:
        # 提取评论ID
        comment_id = item.xpath('./@data-id').get()
        # 提取作者
        author = item.xpath('.//span[@class="author"]/text()').get()
        # 提取评论时间
        time_str = item.xpath('.//span[@class="time"]/text()').get()
        # 提取评论内容
        content = item.xpath('.//p[@class="text"]/text()').get()
        # 提取点赞数
        likes = item.xpath('.//span[@class="likes"]/text()').get()
        
        comment = {
            "comment_id": comment_id,
            "author": author,
            "time": time_str,
            "content": content,
            "likes": likes,
        }
        comments.append(comment)
        
        # 输出每条评论
        print(f"  📝 评论#{comment_id} | {author} | {time_str}")
        print(f"     内容: {content}")
        print(f"     点赞: {likes}")
    
    # 输出汇总
    print("=" * 60)
    print(f"[评论爬取成功] 新闻ID: {news_id}, 第{page}页")
    print(f"标题: {title}")
    print(f"共解析 {len(comments)} 条评论")
    print("=" * 60)
    
    # ⭐【boost_spider 优势】DatasetSink 批量保存评论到 SQLite！
    # 💔  Scrapy 对比：需要在 Pipeline 中处理 item
    for comment in comments:
        comment["news_id"] = news_id
        comment["news_title"] = title
        comment["page"] = page
        data_sink.save("comments", comment)  # ⭐ 一行代码保存！
    print(f"  💾 [已保存到SQLite] comments 表, {len(comments)} 条记录")
    
    return {
        "status": "success",
        "news_id": news_id,
        "page": page,
        "comments_count": len(comments),
        "comments": comments
    }
    



# ================= 入口 =================
if __name__ == "__main__":
    print("=" * 60)
    print("新闻爬虫 - Funboost 分布式爬取")
    print("支持：列表页 -> 详情页 -> 评论页(xpath解析)")
    print("=" * 60)
    print()
    
    # 1. 使用 BoostersManager.consume_group 分组启动所有消费者（非阻塞）
    # 只要装饰器中指定了 booster_group 参数，就可以通过该分组名称一次性启动所有相关消费者
    print("[启动] 分组启动所有爬虫消费者...")
    BoostersManager.consume_group("news_crawler_group")
    # BoostersManager.mp_consume_group("news_crawler_group",process_num=6) # 可以多进程叠加多线程/协程，性能炸裂
    print("  -> 列表页/详情页/评论页爬虫消费者已启动 ✓")
    
    # 2. 发布初始任务：爬取前3页新闻列表
    print()
    print("[发布任务] 开始爬取前3页新闻列表...")
    for page in range(1, 4):
        crawl_list_page.push(page=page, size=5)
        print(f"  -> 已发布: 爬取第 {page} 页")
    
    print()
    print("爬虫已启动，按 Ctrl+C 停止...")
    print()
    
    # 3. 保持程序主线程在运行
    ctrl_c_recv()

`````

--- **end of file: demo_crawler/boost_spider_imp/boost_spider_crawler.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/celery_imp/celery_crawler.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/celery_imp/celery_crawler.py`

#### 📝 Module Docstring

`````
================================================================================
                新闻爬虫 - 使用 Celery 分布式任务队列实现
================================================================================

🎯 本文件目的：
   使用 Celery 框架实现新闻爬虫，与 Funboost + boost_spider 形成对比。
   展示 Celery 作为分布式任务队列在爬虫场景下与 Funboost 的差异。

================================================================================
                    ⚠️ Celery 实现的痛点对比
================================================================================

📊 与 Funboost 对比：
┌─────────────────────────┬────────────────────────────────┬────────────────────────────────┐
│       对比项            │           Celery               │     Funboost + boost_spider    │
├─────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ 项目结构                │ 需要多个文件(app/tasks/config) │ ⭐ 单文件即可运行              │
│ 启动方式                │ 需要单独启动 worker 进程       │ ⭐ .consume() 一行代码         │
│ 中间件选择              │ 主要 Redis/RabbitMQ            │ ⭐ 40+ 种中间件               │
│ 精确流控(QPS)           │ rate_limit 近似控制            │ ⭐ qps=5 精确到毫秒            │
│ 分布式流控              │ 需要自己实现                   │ ⭐ 内置分布式 QPS 控制         │
│ 任务去重                │ 需要自己实现                   │ ⭐ do_task_filtering=True     │
│ 分组启动                │ 需要配置 queue 路由            │ ⭐ booster_group 一个参数     │
│ 外部动态注入            │ ⚠️ 可以但需 apply_async       │ ⭐ .push() 更简洁             │
│ 监控面板                │ 需要单独部署 Flower            │ ⭐ 内置 Web 管理面板           │
│ RPC 获取结果            │ AsyncResult 异步获取           │ ⭐ 原生 RPC 模式更简洁         │
│ 定时任务                │ celery-beat 单独进程           │ ⭐ 内置 APScheduler           │
│ 消息确认机制            │ ack_late 配置                  │ ⭐ ACK_ABLE 中间件原生支持    │
│ 代理/UA管理             │ 需要自己实现                   │ ⭐ RequestClient 一行代码     │
│ 数据保存                │ 需要自己实现                   │ ⭐ DatasetSink 一行代码       │
│ 配置复杂度              │ 需要单独配置文件               │ ⭐ 装饰器参数集中配置          │
└─────────────────────────┴────────────────────────────────┴────────────────────────────────┘

💔 Celery 的主要问题：
   1. 需要单独的 worker 进程（celery -A tasks worker）
   2. 需要单独的配置文件
   3. 没有内置的精确 QPS 控制
   4. 没有内置的任务去重
   5. 监控需要额外部署 Flower

================================================================================
`````

#### 📦 Imports

- `from celery import Celery`
- `import requests`
- `import sqlite3`
- `import os`
- `import random`
- `from threading import Lock`
- `import json`
- `from lxml import etree`

#### 🔧 Public Functions (7)

- `def init_database()`
  - *Line: 126*
  - *初始化数据库*

- `def save_news_to_db(news_data)`
  - *Line: 157*

- `def save_comment_to_db(comment_data)`
  - *Line: 169*

- `def get_random_headers()`
  - *Line: 192*

- `def crawl_list_page(self, page: int = 1, size: int = 10)` `app.task(bind=True, max_retries=3, default_retry_delay=1, rate_limit='2/s')`
  - *Line: 212*
  - **Docstring:**
  `````
  爬取新闻列表页
  
  💔 Celery 痛点 10：任务定义需要 @app.task 装饰器 + 各种参数
  🌟 Funboost 对比：
     @boost(BoosterParams(
         queue_name="list_page",
         qps=2,
         concurrent_num=5,
     ))
     def crawl_list_page(page, size): ...
     
     配置更简洁，参数更直观！
  
  💔 Celery 痛点 11：bind=True + self 才能访问任务上下文
  🌟 Funboost 对比：fct (Funboost Current Task) 上下文直接可用
  `````

- `def crawl_detail_page(self, news_id: int, title: str)` `app.task(bind=True, max_retries=3, default_retry_delay=1, rate_limit='5/s')`
  - *Line: 265*
  - **Docstring:**
  `````
  爬取新闻详情页
  
  💔 Celery 痛点 14：没有内置的任务去重功能
  🌟 Funboost 对比：
     do_task_filtering=True,              # 开启去重
     task_filtering_expire_seconds=600,   # 过期时间
  `````

- `def crawl_comments_page(self, news_id: int, title: str, page: int = 1, size: int = 10)` `app.task(bind=True, max_retries=3, default_retry_delay=1, rate_limit='10/s')`
  - *Line: 327*
  - **Docstring:**
  `````
  爬取新闻评论页
  
  💔 Celery 痛点 15：没有内置的 XPath/CSS 解析
  🌟 Funboost 对比：SpiderResponse.xpath() 开箱即用
  `````


---

`````python
# -*- coding: utf-8 -*-
"""
================================================================================
                新闻爬虫 - 使用 Celery 分布式任务队列实现
================================================================================

🎯 本文件目的：
   使用 Celery 框架实现新闻爬虫，与 Funboost + boost_spider 形成对比。
   展示 Celery 作为分布式任务队列在爬虫场景下与 Funboost 的差异。

================================================================================
                    ⚠️ Celery 实现的痛点对比
================================================================================

📊 与 Funboost 对比：
┌─────────────────────────┬────────────────────────────────┬────────────────────────────────┐
│       对比项            │           Celery               │     Funboost + boost_spider    │
├─────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ 项目结构                │ 需要多个文件(app/tasks/config) │ ⭐ 单文件即可运行              │
│ 启动方式                │ 需要单独启动 worker 进程       │ ⭐ .consume() 一行代码         │
│ 中间件选择              │ 主要 Redis/RabbitMQ            │ ⭐ 40+ 种中间件               │
│ 精确流控(QPS)           │ rate_limit 近似控制            │ ⭐ qps=5 精确到毫秒            │
│ 分布式流控              │ 需要自己实现                   │ ⭐ 内置分布式 QPS 控制         │
│ 任务去重                │ 需要自己实现                   │ ⭐ do_task_filtering=True     │
│ 分组启动                │ 需要配置 queue 路由            │ ⭐ booster_group 一个参数     │
│ 外部动态注入            │ ⚠️ 可以但需 apply_async       │ ⭐ .push() 更简洁             │
│ 监控面板                │ 需要单独部署 Flower            │ ⭐ 内置 Web 管理面板           │
│ RPC 获取结果            │ AsyncResult 异步获取           │ ⭐ 原生 RPC 模式更简洁         │
│ 定时任务                │ celery-beat 单独进程           │ ⭐ 内置 APScheduler           │
│ 消息确认机制            │ ack_late 配置                  │ ⭐ ACK_ABLE 中间件原生支持    │
│ 代理/UA管理             │ 需要自己实现                   │ ⭐ RequestClient 一行代码     │
│ 数据保存                │ 需要自己实现                   │ ⭐ DatasetSink 一行代码       │
│ 配置复杂度              │ 需要单独配置文件               │ ⭐ 装饰器参数集中配置          │
└─────────────────────────┴────────────────────────────────┴────────────────────────────────┘

💔 Celery 的主要问题：
   1. 需要单独的 worker 进程（celery -A tasks worker）
   2. 需要单独的配置文件
   3. 没有内置的精确 QPS 控制
   4. 没有内置的任务去重
   5. 监控需要额外部署 Flower

================================================================================
"""

# ==========================================
# 💔 Celery 痛点 1：需要创建 Celery 应用实例
# ==========================================
# 🌟 Funboost 对比：直接使用 @boost 装饰器，无需创建应用实例
from celery import Celery
import requests
import sqlite3
import os
import random
from threading import Lock
import json

# ==========================================
# 💔 Celery 痛点 2：需要配置 broker 和 backend
# ==========================================
# 🌟 Funboost 对比：broker_kind=BrokerEnum.REDIS_ACK_ABLE 一个参数
app = Celery(
    'news_crawler',
    broker='redis://localhost:6379/1',      # 消息代理
    backend='redis://localhost:6379/2',     # 结果存储
)

# ==========================================
# 💔 Celery 痛点 3：需要单独的配置
# ==========================================
# 🌟 Funboost 对比：所有配置在 @boost(BoosterParams(...)) 一个地方
app.conf.update(
    # 任务序列化格式
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    
    # 时区
    timezone='Asia/Shanghai',
    enable_utc=True,
    
    # 重试配置
    # 💔 Celery：需要在任务中手动处理重试
    # 🌟 Funboost：max_retry_times=3 一个参数
    task_acks_late=True,  # 任务完成后才确认
    task_reject_on_worker_lost=True,
    
    # 并发配置
    # 💔 Celery：启动 worker 时用 -c 参数指定
    # 🌟 Funboost：concurrent_num=10 一个参数
    worker_concurrency=10,
    
    # 💔 Celery 痛点 4：rate_limit 是近似控制，不精确
    # 🌟 Funboost：qps=5 精确到毫秒级
    # task_default_rate_limit='5/s',  # 近似每秒5个
    
    # 队列路由
    # 💔 Celery 痛点 5：需要配置复杂的队列路由
    # 🌟 Funboost：queue_name 直接指定
    task_routes={
        'celery_crawler.crawl_list_page': {'queue': 'list_page'},
        'celery_crawler.crawl_detail_page': {'queue': 'detail_page'},
        'celery_crawler.crawl_comments_page': {'queue': 'comments_page'},
    },
)

# ================= 配置 =================
BASE_URL = "http://127.0.0.1:7000"

# ==========================================
# 💔 Celery 痛点 6：需要自己实现任务去重
# ==========================================
# 🌟 Funboost 对比：do_task_filtering=True 一个参数
crawled_detail_ids = set()
crawled_detail_lock = Lock()
crawled_comment_keys = set()
crawled_comment_lock = Lock()

# ==========================================
# 💔 Celery 痛点 7：需要自己实现数据保存
# ==========================================
# 🌟 Funboost 对比：DatasetSink.save() 一行代码
db_lock = Lock()
db_path = os.path.join(os.path.dirname(__file__), 'celery_crawled_data.db')

def init_database():
    """初始化数据库"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news_detail (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_id INTEGER,
            title TEXT,
            author TEXT,
            publish_time TEXT,
            content TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_id INTEGER,
            news_title TEXT,
            page INTEGER,
            comment_id TEXT,
            author TEXT,
            time TEXT,
            content TEXT,
            likes TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("💔 [Celery] 数据库初始化完成")

def save_news_to_db(news_data):
    with db_lock:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO news_detail (news_id, title, author, publish_time, content)
            VALUES (?, ?, ?, ?, ?)
        ''', (news_data['news_id'], news_data['title'], news_data['author'],
              news_data['publish_time'], news_data['content']))
        conn.commit()
        conn.close()

def save_comment_to_db(comment_data):
    with db_lock:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO comments (news_id, news_title, page, comment_id, author, time, content, likes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (comment_data['news_id'], comment_data['news_title'], comment_data['page'],
              comment_data['comment_id'], comment_data['author'], comment_data['time'],
              comment_data['content'], comment_data['likes']))
        conn.commit()
        conn.close()

# ==========================================
# 💔 Celery 痛点 8：需要自己实现动态 UA
# ==========================================
# 🌟 Funboost 对比：RequestClient(is_change_ua_every_request=True)
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
]

def get_random_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }


# ==========================================
# Celery 任务定义
# ==========================================

@app.task(
    bind=True,              # 绑定任务实例
    max_retries=3,          # 最大重试次数
    default_retry_delay=1,  # 重试延迟
    # 💔 Celery 痛点 9：rate_limit 是近似控制
    # 🌟 Funboost：qps=2 精确每秒2次
    rate_limit='2/s',
)
def crawl_list_page(self, page: int = 1, size: int = 10):
    """
    爬取新闻列表页
    
    💔 Celery 痛点 10：任务定义需要 @app.task 装饰器 + 各种参数
    🌟 Funboost 对比：
       @boost(BoosterParams(
           queue_name="list_page",
           qps=2,
           concurrent_num=5,
       ))
       def crawl_list_page(page, size): ...
       
       配置更简洁，参数更直观！
    
    💔 Celery 痛点 11：bind=True + self 才能访问任务上下文
    🌟 Funboost 对比：fct (Funboost Current Task) 上下文直接可用
    """
    url = f"{BASE_URL}/news/list?page={page}&size={size}"
    print(f"[列表页] 正在爬取: {url}")
    
    try:
        response = requests.get(url, headers=get_random_headers(), timeout=10)
        response.raise_for_status()
        news_list = response.json()
        
        print(f"[列表页] 获取到 {len(news_list)} 条新闻")
        
        # 💔 Celery 痛点 12：推送子任务需要 .delay() 或 .apply_async()
        # 🌟 Funboost 对比：crawl_detail_page.push(news_id=xxx) 更直观
        for news_item in news_list:
            news_id = news_item["id"]
            title = news_item["title"]
            print(f"  -> 发现新闻 [ID: {news_id}] {title}")
            
            # 使用 delay 推送任务
            crawl_detail_page.delay(news_id=news_id, title=title)
        
        return {"status": "success", "page": page, "count": len(news_list)}
    
    except Exception as e:
        print(f"[列表页] 爬取失败: {e}")
        # 💔 Celery 痛点 13：需要手动调用 retry
        # 🌟 Funboost 对比：抛出异常自动重试
        raise self.retry(exc=e)


@app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=1,
    rate_limit='5/s',
)
def crawl_detail_page(self, news_id: int, title: str):
    """
    爬取新闻详情页
    
    💔 Celery 痛点 14：没有内置的任务去重功能
    🌟 Funboost 对比：
       do_task_filtering=True,              # 开启去重
       task_filtering_expire_seconds=600,   # 过期时间
    """
    # 手动去重逻辑
    with crawled_detail_lock:
        if news_id in crawled_detail_ids:
            print(f"  💔 [Celery] 跳过已爬取: news_id={news_id}")
            return None
        crawled_detail_ids.add(news_id)
    
    url = f"{BASE_URL}/news/{news_id}"
    print(f"[详情页] 正在爬取: {url}")
    
    try:
        response = requests.get(url, headers=get_random_headers(), timeout=10)
        response.raise_for_status()
        news_detail = response.json()
        
        content = news_detail.get("content", "")
        author = news_detail.get("author", "未知")
        publish_time = news_detail.get("publish_time", "未知")
        
        print("=" * 60)
        print(f"[爬取成功] 新闻ID: {news_id}")
        print(f"标题: {title}")
        print(f"作者: {author}")
        print("=" * 60)
        
        # 保存到数据库
        save_news_to_db({
            "news_id": news_id,
            "title": title,
            "author": author,
            "publish_time": publish_time,
            "content": content,
        })
        print("  💔 [Celery] 保存新闻到 SQLite（需自己写保存函数）")
        
        # 推送评论页任务
        for page in range(1, 3):
            crawl_comments_page.delay(news_id=news_id, title=title, page=page)
            print(f"  -> 已推送: 爬取新闻{news_id}的第{page}页评论")
        
        return {"status": "success", "news_id": news_id}
    
    except Exception as e:
        print(f"[详情页] 爬取失败 (ID: {news_id}): {e}")
        raise self.retry(exc=e)


@app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=1,
    rate_limit='10/s',
)
def crawl_comments_page(self, news_id: int, title: str, page: int = 1, size: int = 10):
    """
    爬取新闻评论页
    
    💔 Celery 痛点 15：没有内置的 XPath/CSS 解析
    🌟 Funboost 对比：SpiderResponse.xpath() 开箱即用
    """
    # 手动去重
    cache_key = f"{news_id}_{page}"
    with crawled_comment_lock:
        if cache_key in crawled_comment_keys:
            print(f"  💔 [Celery] 跳过已爬取: {cache_key}")
            return None
        crawled_comment_keys.add(cache_key)
    
    url = f"{BASE_URL}/news/{news_id}/comments?page={page}&size={size}"
    print(f"[评论页] 正在爬取: {url}")
    
    try:
        response = requests.get(url, headers=get_random_headers(), timeout=10)
        response.raise_for_status()
        
        # 需要手动安装和使用 lxml 解析
        from lxml import etree
        html = etree.HTML(response.text)
        comment_items = html.xpath('//div[@class="comment-item"]')
        
        print(f"[评论页] 找到 {len(comment_items)} 条评论")
        
        for item in comment_items:
            comment_id = item.get('data-id')
            author = item.xpath('.//span[@class="author"]/text()')
            author = author[0] if author else None
            time_str = item.xpath('.//span[@class="time"]/text()')
            time_str = time_str[0] if time_str else None
            content = item.xpath('.//p[@class="text"]/text()')
            content = content[0] if content else None
            likes = item.xpath('.//span[@class="likes"]/text()')
            likes = likes[0] if likes else None
            
            save_comment_to_db({
                "news_id": news_id,
                "news_title": title,
                "page": page,
                "comment_id": comment_id,
                "author": author,
                "time": time_str,
                "content": content,
                "likes": likes,
            })
            
            print(f"  📝 评论#{comment_id} | {author}")
        
        print(f"[评论爬取成功] 新闻ID: {news_id}, 第{page}页, 共 {len(comment_items)} 条")
        return {"status": "success", "news_id": news_id, "page": page}
    
    except Exception as e:
        print(f"[评论页] 爬取失败: {e}")
        raise self.retry(exc=e)


# ================= 入口 =================
if __name__ == "__main__":
    print()
    print("=" * 70)
    print("            新闻爬虫 - Celery 分布式任务队列实现")
    print("=" * 70)
    print()
    print("⚠️ Celery 的使用步骤（比 Funboost 复杂得多）：")
    print()
    print("💔 步骤 1：启动 Redis")
    print("   redis-server")
    print()
    print("💔 步骤 2：启动 news_server.py")
    print("   python news_server.py")
    print()
    print("💔 步骤 3：启动 Celery Worker（需要单独的终端）")
    print("   celery -A celery_crawler worker -l info -Q list_page,detail_page,comments_page")
    print()
    print("💔 步骤 4：发布初始任务（又一个终端）")
    print("   python -c \"from celery_crawler import *; [crawl_list_page.delay(page=i) for i in range(1,4)]\"")
    print()
    print("💔 步骤 5：（可选）启动 Flower 监控")
    print("   celery -A celery_crawler flower")
    print()
    print("=" * 70)
    print()
    print("🌟 Funboost 对比（简洁得多）：")
    print()
    print("   # 只需要一个文件，运行一次即可：")
    print("   python boost_spider_crawler.py")
    print()
    print("   # 内部代码也更简洁：")
    print("   from funboost import boost, BoosterParams, BrokerEnum")
    print()
    print("   @boost(BoosterParams(")
    print("       queue_name='list_page',")
    print("       broker_kind=BrokerEnum.REDIS_ACK_ABLE,")
    print("       qps=2,")
    print("       concurrent_num=5,")
    print("       do_task_filtering=True,")
    print("   ))")
    print("   def crawl_list_page(page, size): ...")
    print()
    print("   crawl_list_page.consume()  # 启动消费")
    print("   crawl_list_page.push(page=1)  # 发布任务")
    print()
    print("=" * 70)
    print()
    print("💔 Celery 的 15 个痛点总结：")
    print("   1. 需要创建 Celery 应用实例")
    print("   2. 需要配置 broker 和 backend")
    print("   3. 需要单独的配置文件/配置项")
    print("   4. rate_limit 是近似控制，不精确")
    print("   5. 需要配置复杂的队列路由")
    print("   6. 需要自己实现任务去重")
    print("   7. 需要自己实现数据保存")
    print("   8. 需要自己实现动态 UA")
    print("   9. rate_limit 近似 QPS 控制")
    print("   10. 任务装饰器参数繁多")
    print("   11. bind=True + self 才能访问上下文")
    print("   12. 推送子任务需要 .delay()/.apply_async()")
    print("   13. 需要手动调用 retry")
    print("   14. 没有内置任务去重")
    print("   15. 没有内置 XPath/CSS 解析")
    print()
    print("🌟 Funboost 只需要：")
    print("   @boost(BoosterParams(...)) + .consume() + .push()")
    print("   一切自动处理！")
    print("=" * 70)
    
    # 初始化数据库
    init_database()
    
    print()
    print("请按照上述步骤在多个终端中启动 Celery Worker...")

`````

--- **end of file: demo_crawler/celery_imp/celery_crawler.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/feapder_imp/feapder_news_crawler.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/feapder_imp/feapder_news_crawler.py`

#### 📝 Module Docstring

`````
================================================================================
            新闻爬虫 - 使用 Feapder Spider 实现分布式爬取
================================================================================

🎯 本文件目的：
   演示如何使用 Feapder 框架的 Spider（分布式爬虫）实现列表页、详情页、评论页的三层爬取。
   符合 Feapder 最佳实践。

================================================================================
                        ⭐ Feapder 核心特性
================================================================================

📊 Feapder Spider 特点：
┌──────────────────────────┬────────────────────────────────────────────────────────┐
│       ⭐ 特性             │              说明                                      │
├──────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. 基于Redis分布式        │ 任务存储在Redis，支持多进程/多机器分布式采集            │
│ 2. 断点续爬              │ 爬虫中断后重启，自动从上次中断处继续                    │
│ 3. 任务防丢              │ 任务做完才删除，异常退出10分钟后任务自动重新可用        │
│ 4. RANDOM_HEADERS        │ 内置1000+ User-Agent，自动随机切换                      │
│ 5. Item自动入库          │ yield Item() 自动批量入库，无需手动处理                 │
│ 6. 自定义Pipeline        │ 支持MySQL/MongoDB/自定义Pipeline                       │
│ 7. callback回调链        │ parse_list -> parse_detail -> parse_comments           │
│ 8. Request携带参数       │ Request(url, news_id=xxx) 直接携带，无需meta           │
│ 9. 内置去重              │ REQUEST_FILTER_ENABLE / ITEM_FILTER_ENABLE             │
│ 10. xpath/css/re解析     │ response.xpath/css/re 类似Scrapy                       │
└──────────────────────────┴────────────────────────────────────────────────────────┘

================================================================================
`````

#### 📦 Imports

- `import os`
- `import sqlite3`
- `from typing import Dict`
- `from typing import List`
- `from typing import Tuple`
- `import feapder`
- `from feapder import Item`
- `from feapder.pipelines import BasePipeline`

#### 🏛️ Classes (4)

##### 📌 `class SQLitePipeline(BasePipeline)`
*Line: 45*

**Docstring:**
`````
SQLite Pipeline - 自动创建表并批量入库

feapder的Item会自动流经此Pipeline:
- Item类名去掉Item后缀作为表名（如NewsDetailItem -> news_detail）
- 自动根据Item字段创建表
- 批量插入数据
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self)`
  - **Parameters:**
    - `self`

**Public Methods (3):**
- `def save_items(self, table: str, items: List[Dict]) -> bool`
  - *批量保存数据*
- `def update_items(self, table: str, items: List[Dict], update_keys: Tuple = ()) -> bool`
  - *更新数据（暂不实现）*
- `def close(self)`
  - *关闭数据库连接*

##### 📌 `class NewsDetailItem(Item)`
*Line: 116*

**Docstring:**
`````
新闻详情 Item - 自动入库到 news_detail 表

Feapder 最佳实践：
- 定义Item类，yield item 自动批量入库
- __pipelines__ 指定Pipeline实例
- __unique_key__ 可指定去重字段
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, *args, **kwargs)`
  - **Parameters:**
    - `self`
    - `*args`
    - `**kwargs`

**Class Variables (2):**
- `__pipelines__ = [_sqlite_pipeline]`
- `__unique_key__ = ['news_id']`

##### 📌 `class CommentsItem(Item)`
*Line: 137*

**Docstring:**
`````
评论 Item - 自动入库到 comments 表
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, *args, **kwargs)`
  - **Parameters:**
    - `self`
    - `*args`
    - `**kwargs`

**Class Variables (2):**
- `__pipelines__ = [_sqlite_pipeline]`
- `__unique_key__ = ['comment_id']`

##### 📌 `class NewsCrawler(feapder.Spider)`
*Line: 158*

**Docstring:**
`````
Feapder 分布式新闻爬虫

爬取流程: 列表页(JSON) -> 详情页(JSON) -> 评论页(HTML/xpath)

⭐ Feapder 最佳实践：
1. 使用 Spider 类（基于Redis的分布式爬虫）
2. 使用 __custom_setting__ 配置爬虫参数
3. 使用 callback 指定解析函数
4. 使用 Request(url, param=value) 携带参数
5. 使用 yield Item() 自动入库
`````

**Public Methods (4):**
- `def start_requests(self)`
  - **Docstring:**
  `````
  初始任务入口 - 下发列表页任务
  
  ⭐ Feapder 最佳实践：
  - yield feapder.Request(url, callback=self.xxx) 指定回调函数
  - 可以携带自定义参数：feapder.Request(url, page=1)
  `````
- `def parse_list(self, request, response)`
  - **Docstring:**
  `````
  解析列表页 - JSON响应
  
  ⭐ Feapder 特性：
  - response.json 直接获取JSON数据（类似 response.json()）
  - 通过 request.page 取出携带的参数
  
  💔 Scrapy 对比：需要 response.meta['page'] 传递参数
  ✅ Funboost 对比：response.resp_dict 获取JSON
  `````
- `def parse_detail(self, request, response)`
  - **Docstring:**
  `````
  解析详情页 - JSON响应，yield Item 自动入库
  
  ⭐ Feapder 最佳实践：
  - request.news_id 取出携带的参数
  - yield Item() 自动批量入库
  
  💔 Scrapy 对比：需要定义 Item 类 + Pipeline + settings 配置
  ✅ Funboost 对比：DatasetSink.save() 一行代码入库
  `````
- `def parse_comments(self, request, response)`
  - **Docstring:**
  `````
  解析评论页 - HTML响应，使用 xpath 解析
  
  ⭐ Feapder 特性：
  - response.xpath() 返回 SelectorList，与 Scrapy 用法一致
  - .extract_first() 获取第一个匹配的文本
  - .extract() 获取所有匹配的文本列表
  
  💔 Scrapy 对比：用法相同
  ✅ Funboost 对比：SpiderResponse.xpath() 用法相同
  `````

**Class Variables (2):**
- `__custom_setting__ = dict(REDISDB_IP_PORTS='localhost:6379', REDISDB_USER_PASS='', REDISDB_DB=0, SPIDER_THREAD_COUNT=5, SPIDER_MAX_RETRY_TIMES=3, SPIDER_SLEEP_TIME=0, RANDOM_HEADERS=True, USER_AGENT_TYPE='chrome', LOG_LEVEL='INFO')`
- `BASE_URL = 'http://127.0.0.1:7000'`


---

`````python
# -*- coding: utf-8 -*-
"""
================================================================================
            新闻爬虫 - 使用 Feapder Spider 实现分布式爬取
================================================================================

🎯 本文件目的：
   演示如何使用 Feapder 框架的 Spider（分布式爬虫）实现列表页、详情页、评论页的三层爬取。
   符合 Feapder 最佳实践。

================================================================================
                        ⭐ Feapder 核心特性
================================================================================

📊 Feapder Spider 特点：
┌──────────────────────────┬────────────────────────────────────────────────────────┐
│       ⭐ 特性             │              说明                                      │
├──────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. 基于Redis分布式        │ 任务存储在Redis，支持多进程/多机器分布式采集            │
│ 2. 断点续爬              │ 爬虫中断后重启，自动从上次中断处继续                    │
│ 3. 任务防丢              │ 任务做完才删除，异常退出10分钟后任务自动重新可用        │
│ 4. RANDOM_HEADERS        │ 内置1000+ User-Agent，自动随机切换                      │
│ 5. Item自动入库          │ yield Item() 自动批量入库，无需手动处理                 │
│ 6. 自定义Pipeline        │ 支持MySQL/MongoDB/自定义Pipeline                       │
│ 7. callback回调链        │ parse_list -> parse_detail -> parse_comments           │
│ 8. Request携带参数       │ Request(url, news_id=xxx) 直接携带，无需meta           │
│ 9. 内置去重              │ REQUEST_FILTER_ENABLE / ITEM_FILTER_ENABLE             │
│ 10. xpath/css/re解析     │ response.xpath/css/re 类似Scrapy                       │
└──────────────────────────┴────────────────────────────────────────────────────────┘

================================================================================
"""

import os
import sqlite3
from typing import Dict, List, Tuple

import feapder
from feapder import Item
from feapder.pipelines import BasePipeline


# ================= SQLite Pipeline =================

class SQLitePipeline(BasePipeline):
    """
    SQLite Pipeline - 自动创建表并批量入库
    
    feapder的Item会自动流经此Pipeline:
    - Item类名去掉Item后缀作为表名（如NewsDetailItem -> news_detail）
    - 自动根据Item字段创建表
    - 批量插入数据
    """
    
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), 'feapder_crawled_data.db')
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._created_tables = set()
        print(f"[SQLitePipeline] 数据库已连接: {db_path}")
    
    def _ensure_table(self, table: str, item: Dict):
        """确保表存在，不存在则创建"""
        if table in self._created_tables:
            return
        
        # 根据item的字段动态创建表
        columns = ', '.join([f"{k} TEXT" for k in item.keys()])
        sql = f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})"
        
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        self._created_tables.add(table)
        print(f"[SQLitePipeline] 表 {table} 已就绪")
    
    def save_items(self, table: str, items: List[Dict]) -> bool:
        """批量保存数据"""
        if not items:
            return True
        
        self._ensure_table(table, items[0])
        
        cursor = self.conn.cursor()
        for item in items:
            columns = ', '.join(item.keys())
            placeholders = ', '.join(['?' for _ in item])
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            try:
                cursor.execute(sql, list(item.values()))
            except Exception as e:
                print(f"[SQLitePipeline] 插入失败: {e}")
        
        self.conn.commit()
        print(f"[SQLitePipeline] ✓ 保存 {len(items)} 条到 {table} 表")
        return True
    
    def update_items(self, table: str, items: List[Dict], update_keys: Tuple = ()) -> bool:
        """更新数据（暂不实现）"""
        return True
    
    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()
            print("[SQLitePipeline] 数据库连接已关闭")


# 创建全局Pipeline实例，供Item使用
_sqlite_pipeline = SQLitePipeline()


# ================= Item 定义 =================
# Item类名去掉Item后缀 = 表名 (news_detail, comments)
# 使用 __pipelines__ 指定Pipeline实例（feapder语法）

class NewsDetailItem(Item):
    """
    新闻详情 Item - 自动入库到 news_detail 表
    
    Feapder 最佳实践：
    - 定义Item类，yield item 自动批量入库
    - __pipelines__ 指定Pipeline实例
    - __unique_key__ 可指定去重字段
    """
    __pipelines__ = [_sqlite_pipeline]  # ⭐ 使用Item的__pipelines__指定Pipeline
    __unique_key__ = ["news_id"]  # 根据 news_id 去重
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news_id = None
        self.title = None
        self.author = None
        self.publish_time = None
        self.content = None


class CommentsItem(Item):
    """
    评论 Item - 自动入库到 comments 表
    """
    __pipelines__ = [_sqlite_pipeline]  # ⭐ 使用Item的__pipelines__指定Pipeline
    __unique_key__ = ["comment_id"]  # 根据 comment_id 去重
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news_id = None
        self.news_title = None
        self.page = None
        self.comment_id = None
        self.author = None
        self.time = None
        self.content = None
        self.likes = None


# ================= Spider 爬虫 =================

class NewsCrawler(feapder.Spider):
    """
    Feapder 分布式新闻爬虫
    
    爬取流程: 列表页(JSON) -> 详情页(JSON) -> 评论页(HTML/xpath)
    
    ⭐ Feapder 最佳实践：
    1. 使用 Spider 类（基于Redis的分布式爬虫）
    2. 使用 __custom_setting__ 配置爬虫参数
    3. 使用 callback 指定解析函数
    4. 使用 Request(url, param=value) 携带参数
    5. 使用 yield Item() 自动入库
    """
    
    # ⭐ 爬虫配置 - 使用 __custom_setting__ 覆盖默认配置
    __custom_setting__ = dict(
        # Redis 配置（Spider必须）
        REDISDB_IP_PORTS="localhost:6379",
        REDISDB_USER_PASS="",
        REDISDB_DB=0,
        
        # 并发配置
        SPIDER_THREAD_COUNT=5,          # 并发线程数
        SPIDER_MAX_RETRY_TIMES=3,       # 最大重试次数
        SPIDER_SLEEP_TIME=0,            # 下载间隔（秒）
        
        # ⭐ 随机 User-Agent（feapder内置功能，无需自己实现！）
        RANDOM_HEADERS=True,            # 开启随机UA
        USER_AGENT_TYPE="chrome",       # UA类型：chrome/firefox/safari/mobile
        
        # 注意：Pipeline已在Item类中通过 __pipelines__ 指定，无需在这里配置
        
        # 日志
        LOG_LEVEL="INFO",
    )
    
    BASE_URL = "http://127.0.0.1:7000"
    
    def start_requests(self):
        """
        初始任务入口 - 下发列表页任务
        
        ⭐ Feapder 最佳实践：
        - yield feapder.Request(url, callback=self.xxx) 指定回调函数
        - 可以携带自定义参数：feapder.Request(url, page=1)
        """
        print("=" * 60)
        print("新闻爬虫 - Feapder Spider 分布式爬取")
        print("爬取流程: 列表页 -> 详情页 -> 评论页(xpath解析)")
        print("=" * 60)
        
        # 爬取前3页列表，每页5条
        for page in range(1, 4):
            url = f"{self.BASE_URL}/news/list?page={page}&size=5"
            print(f"[下发任务] 列表页 第{page}页: {url}")
            yield feapder.Request(url, callback=self.parse_list, page=page)
    
    def parse_list(self, request, response):
        """
        解析列表页 - JSON响应
        
        ⭐ Feapder 特性：
        - response.json 直接获取JSON数据（类似 response.json()）
        - 通过 request.page 取出携带的参数
        
        💔 Scrapy 对比：需要 response.meta['page'] 传递参数
        ✅ Funboost 对比：response.resp_dict 获取JSON
        """
        page = request.page
        
        # ⭐【Feapder 特性 1】response.json 属性直接获取JSON
        # 💔 Scrapy 对比：json.loads(response.text)
        news_list = response.json
        
        print(f"[列表页] 第{page}页 获取到 {len(news_list)} 条新闻")
        
        for news in news_list:
            news_id = news["id"]
            title = news["title"]
            print(f"  -> 发现新闻 [ID: {news_id}] {title}")
            
            # ⭐【Feapder 特性 2】Request直接携带参数，无需meta
            # 💔 Scrapy 对比：需要 meta={'news_id': news_id, 'title': title}
            # ✅ Funboost 对比：函数参数直接传递
            yield feapder.Request(
                f"{self.BASE_URL}/news/{news_id}",
                callback=self.parse_detail,
                news_id=news_id,
                title=title,
            )
    
    def parse_detail(self, request, response):
        """
        解析详情页 - JSON响应，yield Item 自动入库
        
        ⭐ Feapder 最佳实践：
        - request.news_id 取出携带的参数
        - yield Item() 自动批量入库
        
        💔 Scrapy 对比：需要定义 Item 类 + Pipeline + settings 配置
        ✅ Funboost 对比：DatasetSink.save() 一行代码入库
        """
        news_id = request.news_id
        title = request.title
        news = response.json
        
        # ⭐【Feapder 特性 3】创建 Item 并赋值
        # 💔 Scrapy 对比：同样需要定义 Item 类
        # ✅ Funboost 对比：直接使用 dict 即可
        item = NewsDetailItem()
        item.news_id = news_id
        item.title = title
        item.author = news.get("author", "未知")
        item.publish_time = news.get("publish_time", "")
        item.content = news.get("content", "")
        
        print("=" * 60)
        print(f"[详情页] 新闻ID: {news_id}")
        print(f"标题: {title}")
        print(f"作者: {item.author}")
        print(f"发布时间: {item.publish_time}")
        print(f"正文预览: {item.content[:80]}...")
        print("=" * 60)
        
        # ⭐【Feapder 特性 4】yield Item，自动批量入库到 news_detail 表
        # 💔 Scrapy 对比：需要配置 ITEM_PIPELINES，在 Pipeline 中手写 SQL
        # ✅ Funboost 对比：DatasetSink("sqlite:///data.db").save("news", data)
        yield item
        print(f"  💾 [yield Item] 将自动入库到 news_detail 表")
        
        # ⭐【Feapder 特性 5】下发评论页任务（前2页）
        # 💔 Scrapy 对比：同样使用 yield Request
        # ✅ Funboost 对比：crawl_comments_page.push()
        for page in range(1, 3):
            yield feapder.Request(
                f"{self.BASE_URL}/news/{news_id}/comments?page={page}&size=10",
                callback=self.parse_comments,
                news_id=news_id,
                title=title,
                comment_page=page,
            )
            print(f"  -> 已发布: 爬取新闻{news_id}的第{page}页评论")
    
    def parse_comments(self, request, response):
        """
        解析评论页 - HTML响应，使用 xpath 解析
        
        ⭐ Feapder 特性：
        - response.xpath() 返回 SelectorList，与 Scrapy 用法一致
        - .extract_first() 获取第一个匹配的文本
        - .extract() 获取所有匹配的文本列表
        
        💔 Scrapy 对比：用法相同
        ✅ Funboost 对比：SpiderResponse.xpath() 用法相同
        """
        news_id = request.news_id
        title = request.title
        page = request.comment_page
        
        print(f"[评论页] 正在解析: 新闻{news_id} 第{page}页")
        
        # ⭐【Feapder 特性 6】使用 xpath 解析 HTML
        # 💔 Scrapy 对比：用法完全相同
        # ✅ Funboost 对比：SpiderResponse.xpath() 同样支持
        comment_items = response.xpath('//div[@class="comment-item"]')
        print(f"[评论页] 找到 {len(comment_items)} 条评论")
        
        for elem in comment_items:
            # ⭐【Feapder 特性 7】创建 Item 并使用 xpath 提取数据
            item = CommentsItem()
            item.news_id = news_id
            item.news_title = title
            item.page = page
            
            # 提取评论ID
            item.comment_id = elem.xpath('./@data-id').extract_first()
            # 提取作者
            item.author = elem.xpath('.//span[@class="author"]/text()').extract_first()
            # 提取评论时间
            item.time = elem.xpath('.//span[@class="time"]/text()').extract_first()
            # 提取评论内容
            item.content = elem.xpath('.//p[@class="text"]/text()').extract_first()
            # 提取点赞数
            item.likes = elem.xpath('.//span[@class="likes"]/text()').extract_first()
            
            print(f"  📝 评论#{item.comment_id} | {item.author} | {item.time}")
            print(f"     内容: {item.content}")
            print(f"     点赞: {item.likes}")
            
            # ⭐【Feapder 特性 8】yield Item，自动批量入库到 comments 表
            yield item
        
        # 输出汇总
        print("=" * 60)
        print(f"[评论爬取成功] 新闻ID: {news_id}, 第{page}页")
        print(f"标题: {title}")
        print(f"共解析 {len(comment_items)} 条评论")
        print(f"  💾 [yield Item] 将自动入库到 comments 表")
        print("=" * 60)


# ================= 入口 =================
if __name__ == "__main__":
    """
    运行说明：
    
    1. 先启动 Redis:
       redis-server
    
    2. 启动 news_server.py:
       cd demo_crawler
       python news_server.py
    
    3. 运行爬虫:
       cd demo_crawler/feapder_imp
       python feapder_news_crawler.py
    
    4. 验证数据:
       sqlite3 feapder_crawled_data.db
       .tables
       SELECT COUNT(*) FROM news_detail;
       SELECT COUNT(*) FROM comments;
    """
    print("=" * 60)
    print("新闻爬虫 - Feapder Spider 分布式爬取")
    print("支持：列表页 -> 详情页 -> 评论页(xpath解析)")
    print("=" * 60)
    print()
    
    # ⭐【Feapder 特性】Spider 基于 Redis 分布式
    # 💔 Scrapy 对比：需要 scrapy-redis 插件才能分布式
    # ✅ Funboost 对比：支持 40+ 种中间件
    print("[启动] 创建 Feapder Spider 实例...")
    print("[配置] Redis: localhost:6379")
    print("[配置] 并发线程: 5")
    print("[配置] 随机UA: 开启")
    print()
    
    # delete_keys="*" 清空任务队列，重新爬取（开发调试时使用）
    # 正式环境去掉 delete_keys 参数，支持断点续爬
    spider = NewsCrawler(
        redis_key="news:feapder",  # Redis中的key前缀
        delete_keys="*",           # 开发模式：每次清空重新爬取
    )
    
    print("[启动] 开始爬取...")
    print()
    spider.start()


`````

--- **end of file: demo_crawler/feapder_imp/feapder_news_crawler.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/scrapy_imp/scrapy_spider_crawler.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/scrapy_imp/scrapy_spider_crawler.py`

#### 📝 Module Docstring

`````
================================================================================
                 Scrapy 新闻爬虫实现 —— 与 Funboost 爬虫的对比学习
================================================================================

🎯 本文件目的：
   使用 Scrapy 框架实现同样的新闻爬虫功能，与 boost_spider_imp/boost_spider_crawler.py 形成对比。
   通过大量注释说明两个框架在各方面的差异，帮助理解 Funboost + boost_spider 的优势。

📊 功能对比表（同样的爬取需求，不同的实现方式）：
   ┌──────────────────────┬──────────────────────────────┬──────────────────────────────┐
   │       对比项         │          Scrapy              │     Funboost + boost_spider  │
   ├──────────────────────┼──────────────────────────────┼──────────────────────────────┤
   │ 项目结构             │ 需要标准项目结构，多个文件   │ ⭐ 单文件即可运行            │
   │ 分布式能力           │ 需安装 scrapy-redis 插件     │ ⭐ 原生40+中间件分布式       │
   │ 中间件选择           │ 仅 Redis/Kafka(需插件)       │ ⭐ 40+种消息队列中间件       │
   │ 任务队列             │ 内存队列，进程结束任务丢失   │ ⭐ 持久化队列，断点续爬      │
   │ 动态任务注入         │ ❌ 不支持外部实时注入二级任务 │ ⭐ 天然支持HTTP/RPC动态注入  │
   │ 精确流控(QPS)        │ 近似控制(DOWNLOAD_DELAY)     │ ⭐ 精确到毫秒级QPS控制       │
   │ 分布式流控           │ 需自己实现                   │ ⭐ 内置分布式QPS控制         │
   │ 任务去重             │ 需配置+BloomFilter           │ ⭐ 一个参数do_task_filtering │
   │ 自动重试             │ 中间件配置                   │ ⭐ 装饰器参数max_retry_times │
   │ 消息确认(ACK)        │ 需scrapy-redis支持           │ ⭐ 原生ACK，消息不丢失       │
   │ 并发模型             │ Twisted异步                  │ ⭐ 多种:线程/协程/gevent/... │
   │ 监控面板             │ 需部署Scrapyd+第三方UI       │ ⭐ 内置Web管理面板           │
   │ RPC获取结果          │ 不支持                       │ ⭐ 原生RPC模式获取结果       │
   │ 定时任务             │ 需配合cron/celery-beat       │ ⭐ 内置APScheduler集成       │
   │ 学习曲线             │ 需学Twisted/中间件/settings  │ ⭐ 装饰器一行搞定            │
   │ 爬取路径追踪         │ 复杂 callback 链             │ ⭐ 直观的函数调用链          │
   │ XPath/CSS解析        │ 内置selector                 │ ⭐ SpiderResponse同样支持    │
   │ 代理管理             │ 需自己实现中间件             │ ⭐ RequestClient内置代理管理 │
   │ Session/Cookie管理   │ 需CookiesMiddleware配置      │ ⭐ RequestClient自动管理     │
   └──────────────────────┴──────────────────────────────┴──────────────────────────────┘

================================================================================
                          ⚠️ Scrapy 实现的局限性说明
================================================================================

1. 【外部动态任务注入】（Scrapy 无法实现）
   Scrapy的任务只能从start_urls或Spider内部yield产生，不能从外部系统实时注入任务。
   
   🌟 Funboost对比：
   - 天然支持 HTTP/API/RPC 任意时刻从外部注入"二级任务"
   - 例如：用户在后台点击"立即爬取此新闻"，马上可以 crawl_detail_page.push(news_id=xxx)
   - 这是 Scrapy 架构根本无法实现的功能，是 Funboost 降维打击 Scrapy 的核心优势！

2. 【分布式部署】（Scrapy 需要额外插件）
   需要安装配置 scrapy-redis，修改settings，配置Redis连接等。
   
   🌟 Funboost对比：
   - 只需把 broker_kind 改为 BrokerEnum.REDIS_ACK_ABLE
   - 无需任何额外配置，开箱即用分布式
   - 支持40+种消息队列作为分布式后端

3. 【任务去重】（Scrapy 需要配置）
   需要在 settings 中配置 DUPEFILTER_CLASS，可能还需要 BloomFilter
   
   🌟 Funboost对比：
   - 装饰器加一个参数：do_task_filtering=True
   - 可选配置过期时间：task_filtering_expire_seconds=600

4. 【精确流控】（Scrapy 近似控制）
   Scrapy 的 DOWNLOAD_DELAY 是近似控制，不是精确 QPS
   
   🌟 Funboost对比：
   - qps=5 表示精确每秒5次
   - 支持分布式场景下的统一流控

================================================================================
`````

#### 📦 Imports

- `import scrapy`
- `from scrapy.crawler import CrawlerProcess`
- `from scrapy.http import Request`
- `from scrapy import signals`
- `import json`
- `import sqlite3`
- `import os`
- `import random`

#### 🏛️ Classes (3)

##### 📌 `class SQLitePipeline`
*Line: 94*

**Docstring:**
`````
💔 Scrapy 需要定义这个 Pipeline 类来保存数据

需要：
1. 定义 Pipeline 类
2. 实现 open_spider / close_spider / process_item 方法
3. 在 settings 中配置 ITEM_PIPELINES 启用

🌟 Funboost 对比：sink.save("table", data) 一行代码搞定！
`````

**Public Methods (3):**
- `def open_spider(self, spider)`
  - *爬虫启动时创建数据库连接*
- `def close_spider(self, spider)`
  - *爬虫结束时关闭数据库连接*
- `def process_item(self, item, spider)`
  - *处理每个 item*

##### 📌 `class RandomUserAgentMiddleware`
*Line: 186*

**Docstring:**
`````
💔 Scrapy 需要定义这个 Middleware 类来实现动态 User-Agent

需要：
1. 定义 Middleware 类
2. 实现 process_request 方法
3. 在 settings 中配置 DOWNLOADER_MIDDLEWARES 启用
4. 需要禁用默认的 UserAgentMiddleware

🌟 Funboost + boost_spider 对比：
   client = RequestClient(is_change_ua_every_request=True)
   只需要这一个参数！RequestClient 内置了 100+ 种 UA 随机切换
`````

**Public Methods (1):**
- `def process_request(self, request, spider)`
  - *为每个请求随机设置 User-Agent*

##### 📌 `class NewsSpider(scrapy.Spider)`
*Line: 213*

**Docstring:**
`````
Scrapy 新闻爬虫

┌─────────────────────────────────────────────────────────────────┐
│  💔 Scrapy 的痛点 1：必须继承 Spider 类                          │
│                                                                 │
│  🌟 Funboost 对比：                                              │
│  - 任何普通函数加 @boost 装饰器即可变为分布式消费函数             │
│  - 无需继承任何类，无需遵循任何框架约定                          │
│  - 思维方式：横冲直撞，大开大合，自由奔放                        │
└─────────────────────────────────────────────────────────────────┘
`````

**Public Methods (7):**
- `def start_requests(self)`
  - **Docstring:**
  `````
  ==========================================
  【Scrapy 痛点 4】任务起点固定
  ==========================================
  Scrapy 的任务只能从 start_requests 或 start_urls 开始
  无法从外部动态注入任务
  
  🌟 Funboost 对比：
  - 任务可以从任何地方发起：crawl_list_page.push(page=1)
  - 支持 HTTP API 动态注入任务（funboost.faas）
  - 支持 RPC 远程调用发布任务
  - 支持定时任务自动发布（ApsJobAdder）
  
  ⭐ 外部系统实时动态注入"二级任务"的需求：
  假设运营人员在后台看到一条新闻需要重新爬取，他可以直接调用：
     crawl_detail_page.push(news_id=12345)
  这个任务会立即进入消息队列，等待消费者处理。
  
  💔 Scrapy 完全无法实现这种外部动态注入！
  `````
- `def parse_list_page(self, response)`
  - **Docstring:**
  `````
  解析新闻列表页
  
  ==========================================
  【Scrapy 痛点 6】callback 回调地狱
  ==========================================
  Scrapy 的解析流程必须通过 callback 链接：
    start_requests -> parse_list_page -> parse_detail_page -> ...
  
  这种写法的问题：
    - 代码逻辑被切割成多个回调函数
    - 难以追踪完整的爬取路径
    - 传递上下文数据需要通过 meta 字典
  
  🌟 Funboost 对比：
    - 直观的函数调用链：
      crawl_list_page 中直接 crawl_detail_page.push(news_id=xxx)
    - 每个函数独立，逻辑清晰
    - 上下文通过函数参数传递，类型安全
    - 思维方式：平铺直叙，如写普通脚本
  `````
- `def parse_detail_page(self, response)`
  - **Docstring:**
  `````
  解析新闻详情页
  
  ==========================================
  【boost_spider 的 SpiderResponse 优势】
  ==========================================
  在 Funboost 爬虫中，使用 boost_spider 的 RequestClient 发请求：
  
  from boost_spider import RequestClient
  client = RequestClient(proxy_name_list=None, request_retry_times=3)
  resp = client.get(url)  # 返回 SpiderResponse 对象
  
  SpiderResponse 兼具 requests.Response 的所有功能，同时增加：
  - resp.xpath('//div[@class="xxx"]')  -> 类似 Scrapy selector
  - resp.css('div.xxx')                -> CSS 选择器
  - resp.resp_dict                     -> 自动解析 JSON
  - resp.re_search / re_findall        -> 正则匹配
  - resp.selector                      -> parsel.Selector 对象
  
  🌟 你羡慕的 Scrapy selector 功能，boost_spider 全都有！
  🌟 而且 boost_spider 的 RequestClient 还内置了：
     - 代理管理（多代理商轮换）
     - Session 管理
     - 请求重试    
     - UA 随机化
  `````
- `def parse_comments_page(self, response)`
  - **Docstring:**
  `````
  解析评论页（使用 XPath）
  
  ==========================================
  【XPath/CSS 解析对比】
  ==========================================
  
  Scrapy 内置强大的 Selector：
    response.xpath('//div[@class="comment-item"]')
    response.css('div.comment-item')
  
  🌟 boost_spider 的 SpiderResponse 同样支持：
    resp.xpath('//div[@class="comment-item"]')
    resp.css('div.comment-item')
  
  两者在解析能力上几乎一样强大！
  但 boost_spider 的优势在于：
    - 与 Funboost 分布式调度无缝集成
    - RequestClient 内置代理/重试/UA管理
    - 无需学习 Twisted 异步编程
  `````
- `def handle_error(self, failure)`
  - **Docstring:**
  `````
  错误处理
  
  ==========================================
  【Scrapy 痛点 9】错误处理复杂
  ==========================================
  💔 Scrapy：需要配置 errback，处理 Twisted Failure 对象
  🌟 Funboost：异常自动重试，max_retry_times=3
             抛出 ExceptionForRetry 触发重试
             抛出 ExceptionForRequeue 重新入队
             抛出 ExceptionForPushToDlxqueue 推送到死信队列
  `````
- `def from_crawler(cls, crawler, *args, **kwargs)` `classmethod`
- `def spider_closed(self, spider)`
  - *爬虫关闭时输出统计*

**Class Variables (3):**
- `name = 'news_spider'`
- `custom_settings = {'CONCURRENT_REQUESTS': 10, 'CONCURRENT_REQUESTS_PER_DOMAIN': 10, 'DOWNLOAD_DELAY': 0.2, 'RETRY_ENABLED': True, 'RETRY_TIMES': 3, 'LOG_LEVEL': 'INFO', 'ITEM_PIPELINES': {'__main__.SQLitePipeline': 300}, 'DOWNLOADER_MIDDLEWARES': {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, '__main__.RandomUserAgentMiddleware': 400}}`
- `crawled_count = {'list': 0, 'detail': 0, 'comment': 0}`


---

`````python
# -*- coding: utf-8 -*-
"""
================================================================================
                 Scrapy 新闻爬虫实现 —— 与 Funboost 爬虫的对比学习
================================================================================

🎯 本文件目的：
   使用 Scrapy 框架实现同样的新闻爬虫功能，与 boost_spider_imp/boost_spider_crawler.py 形成对比。
   通过大量注释说明两个框架在各方面的差异，帮助理解 Funboost + boost_spider 的优势。

📊 功能对比表（同样的爬取需求，不同的实现方式）：
   ┌──────────────────────┬──────────────────────────────┬──────────────────────────────┐
   │       对比项         │          Scrapy              │     Funboost + boost_spider  │
   ├──────────────────────┼──────────────────────────────┼──────────────────────────────┤
   │ 项目结构             │ 需要标准项目结构，多个文件   │ ⭐ 单文件即可运行            │
   │ 分布式能力           │ 需安装 scrapy-redis 插件     │ ⭐ 原生40+中间件分布式       │
   │ 中间件选择           │ 仅 Redis/Kafka(需插件)       │ ⭐ 40+种消息队列中间件       │
   │ 任务队列             │ 内存队列，进程结束任务丢失   │ ⭐ 持久化队列，断点续爬      │
   │ 动态任务注入         │ ❌ 不支持外部实时注入二级任务 │ ⭐ 天然支持HTTP/RPC动态注入  │
   │ 精确流控(QPS)        │ 近似控制(DOWNLOAD_DELAY)     │ ⭐ 精确到毫秒级QPS控制       │
   │ 分布式流控           │ 需自己实现                   │ ⭐ 内置分布式QPS控制         │
   │ 任务去重             │ 需配置+BloomFilter           │ ⭐ 一个参数do_task_filtering │
   │ 自动重试             │ 中间件配置                   │ ⭐ 装饰器参数max_retry_times │
   │ 消息确认(ACK)        │ 需scrapy-redis支持           │ ⭐ 原生ACK，消息不丢失       │
   │ 并发模型             │ Twisted异步                  │ ⭐ 多种:线程/协程/gevent/... │
   │ 监控面板             │ 需部署Scrapyd+第三方UI       │ ⭐ 内置Web管理面板           │
   │ RPC获取结果          │ 不支持                       │ ⭐ 原生RPC模式获取结果       │
   │ 定时任务             │ 需配合cron/celery-beat       │ ⭐ 内置APScheduler集成       │
   │ 学习曲线             │ 需学Twisted/中间件/settings  │ ⭐ 装饰器一行搞定            │
   │ 爬取路径追踪         │ 复杂 callback 链             │ ⭐ 直观的函数调用链          │
   │ XPath/CSS解析        │ 内置selector                 │ ⭐ SpiderResponse同样支持    │
   │ 代理管理             │ 需自己实现中间件             │ ⭐ RequestClient内置代理管理 │
   │ Session/Cookie管理   │ 需CookiesMiddleware配置      │ ⭐ RequestClient自动管理     │
   └──────────────────────┴──────────────────────────────┴──────────────────────────────┘

================================================================================
                          ⚠️ Scrapy 实现的局限性说明
================================================================================

1. 【外部动态任务注入】（Scrapy 无法实现）
   Scrapy的任务只能从start_urls或Spider内部yield产生，不能从外部系统实时注入任务。
   
   🌟 Funboost对比：
   - 天然支持 HTTP/API/RPC 任意时刻从外部注入"二级任务"
   - 例如：用户在后台点击"立即爬取此新闻"，马上可以 crawl_detail_page.push(news_id=xxx)
   - 这是 Scrapy 架构根本无法实现的功能，是 Funboost 降维打击 Scrapy 的核心优势！

2. 【分布式部署】（Scrapy 需要额外插件）
   需要安装配置 scrapy-redis，修改settings，配置Redis连接等。
   
   🌟 Funboost对比：
   - 只需把 broker_kind 改为 BrokerEnum.REDIS_ACK_ABLE
   - 无需任何额外配置，开箱即用分布式
   - 支持40+种消息队列作为分布式后端

3. 【任务去重】（Scrapy 需要配置）
   需要在 settings 中配置 DUPEFILTER_CLASS，可能还需要 BloomFilter
   
   🌟 Funboost对比：
   - 装饰器加一个参数：do_task_filtering=True
   - 可选配置过期时间：task_filtering_expire_seconds=600

4. 【精确流控】（Scrapy 近似控制）
   Scrapy 的 DOWNLOAD_DELAY 是近似控制，不是精确 QPS
   
   🌟 Funboost对比：
   - qps=5 表示精确每秒5次
   - 支持分布式场景下的统一流控

================================================================================
"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy import signals
import json
import sqlite3  # 用于 SQLite Pipeline
import os       # 用于路径处理
import random   # 用于动态 User-Agent

# ================= 配置 =================
BASE_URL = "http://127.0.0.1:7000"

# ==========================================
# 【Scrapy 痛点 11】数据持久化需要定义 Pipeline 类
# ==========================================
# 💔 Scrapy：需要下面这么多代码来保存数据到 SQLite
# 🌟 Funboost + boost_spider 对比：
#    from boost_spider.sink.dataset_sink import DatasetSink
#    sink = DatasetSink("sqlite:///data.db")
#    sink.save("table_name", data_dict)  # 就这一行！

class SQLitePipeline:
    """
    💔 Scrapy 需要定义这个 Pipeline 类来保存数据
    
    需要：
    1. 定义 Pipeline 类
    2. 实现 open_spider / close_spider / process_item 方法
    3. 在 settings 中配置 ITEM_PIPELINES 启用
    
    🌟 Funboost 对比：sink.save("table", data) 一行代码搞定！
    """
    
    def open_spider(self, spider):
        """爬虫启动时创建数据库连接"""
        db_path = os.path.join(os.path.dirname(__file__), 'scrapy_crawled_data.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        # 创建表
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS news_detail (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                news_id INTEGER,
                title TEXT,
                author TEXT,
                publish_time TEXT,
                content TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                news_id INTEGER,
                news_title TEXT,
                page INTEGER,
                comment_id TEXT,
                author TEXT,
                time TEXT,
                content TEXT,
                likes TEXT
            )
        ''')
        self.conn.commit()
        print("💔 [Scrapy Pipeline] 数据库已连接")
    
    def close_spider(self, spider):
        """爬虫结束时关闭数据库连接"""
        self.conn.close()
        print("💔 [Scrapy Pipeline] 数据库已关闭")
    
    def process_item(self, item, spider):
        """处理每个 item"""
        if item.get('type') == 'news_detail':
            self.cursor.execute('''
                INSERT INTO news_detail (news_id, title, author, publish_time, content)
                VALUES (?, ?, ?, ?, ?)
            ''', (item['news_id'], item['title'], item['author'], 
                  item['publish_time'], item['content']))
            self.conn.commit()
            print(f"  💔 [Scrapy Pipeline] 保存新闻到 SQLite: {item['news_id']}")
        
        elif item.get('type') == 'comments':
            for comment in item.get('comments', []):
                self.cursor.execute('''
                    INSERT INTO comments (news_id, news_title, page, comment_id, author, time, content, likes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (item['news_id'], item.get('title', ''), item['page'],
                      comment.get('comment_id'), comment.get('author'),
                      comment.get('time'), comment.get('content'), comment.get('likes')))
            self.conn.commit()
            print(f"  💔 [Scrapy Pipeline] 保存 {len(item.get('comments', []))} 条评论到 SQLite")
        
        return item


# ==========================================
# 【Scrapy 痛点 13】动态请求头需要定义 Middleware 类
# ==========================================
# 💔 Scrapy：需要下面这么多代码来实现动态 User-Agent
# 🌟 Funboost + boost_spider 对比：
#    client = RequestClient(is_change_ua_every_request=True)  # 就这一个参数！

# 预定义的 User-Agent 列表
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]

class RandomUserAgentMiddleware:
    """
    💔 Scrapy 需要定义这个 Middleware 类来实现动态 User-Agent
    
    需要：
    1. 定义 Middleware 类
    2. 实现 process_request 方法
    3. 在 settings 中配置 DOWNLOADER_MIDDLEWARES 启用
    4. 需要禁用默认的 UserAgentMiddleware
    
    🌟 Funboost + boost_spider 对比：
       client = RequestClient(is_change_ua_every_request=True)
       只需要这一个参数！RequestClient 内置了 100+ 种 UA 随机切换
    """
    
    def process_request(self, request, spider):
        """为每个请求随机设置 User-Agent"""
        ua = random.choice(USER_AGENTS)
        request.headers['User-Agent'] = ua
        # 添加其他常见请求头
        request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
        request.headers['Accept-Encoding'] = 'gzip, deflate'
        request.headers['Referer'] = 'https://news.example.com/'
        print(f"  💔 [Scrapy Middleware] 设置 UA: {ua[:50]}...")
        return None  # 继续处理请求

class NewsSpider(scrapy.Spider):
    """
    Scrapy 新闻爬虫
    
    ┌─────────────────────────────────────────────────────────────────┐
    │  💔 Scrapy 的痛点 1：必须继承 Spider 类                          │
    │                                                                 │
    │  🌟 Funboost 对比：                                              │
    │  - 任何普通函数加 @boost 装饰器即可变为分布式消费函数             │
    │  - 无需继承任何类，无需遵循任何框架约定                          │
    │  - 思维方式：横冲直撞，大开大合，自由奔放                        │
    └─────────────────────────────────────────────────────────────────┘
    """
    name = 'news_spider'
    
    # ==========================================
    # 【Scrapy 痛点 2】settings 配置分散在多个地方
    # ==========================================
    # 在 Scrapy 中，配置分散在：
    #   - settings.py（全局配置）
    #   - custom_settings（Spider级别配置）
    #   - 各种中间件配置
    #
    # 🌟 Funboost 对比：
    #   - 所有配置集中在 @boost(BoosterParams(...)) 一个地方
    #   - qps、concurrent_num、max_retry_times 等一目了然
    #   - 继承 BoosterParams 还可以复用配置
    custom_settings = {
        # 并发数设置
        # 💔 Scrapy：需要在 settings 中配置
        # 🌟 Funboost：concurrent_num=10 一个参数搞定
        'CONCURRENT_REQUESTS': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
        
        # 下载延迟（近似流控）
        # 💔 Scrapy：DOWNLOAD_DELAY 是近似控制，不精确
        # 🌟 Funboost：qps=5 表示精确每秒5次，支持分布式统一控频
        'DOWNLOAD_DELAY': 0.2,  # 每个请求间隔0.2秒，约 5 QPS
        
        # 重试配置
        # 💔 Scrapy：需要配置中间件
        # 🌟 Funboost：max_retry_times=3 一个参数搞定
        'RETRY_ENABLED': True,
        'RETRY_TIMES': 3,
        
        # 日志级别
        'LOG_LEVEL': 'INFO',
        
        # ==========================================
        # 【Scrapy 痛点 3】去重需要额外配置
        # ==========================================
        # 💔 Scrapy：需要配置 DUPEFILTER_CLASS
        # 🌟 Funboost：do_task_filtering=True 一个参数
        #            task_filtering_expire_seconds=600 控制过期时间
        # 'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',
        
        # ==========================================
        # 【Scrapy 痛点 12】数据持久化需要配置 ITEM_PIPELINES
        # ==========================================
        # 💔 Scrapy：需要在 settings 中配置 Pipeline
        # 🌟 Funboost：sink.save("table", data) 一行代码！
        'ITEM_PIPELINES': {
            '__main__.SQLitePipeline': 300,  # 启用 SQLite Pipeline
        },
        
        # ==========================================
        # 【Scrapy 痛点 14】动态请求头需要配置 DOWNLOADER_MIDDLEWARES
        # ==========================================
        # 💔 Scrapy：需要定义 Middleware 类 + 下面的 settings 配置
        # 🌟 Funboost：RequestClient(is_change_ua_every_request=True) 一个参数！
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 禁用默认 UA
            '__main__.RandomUserAgentMiddleware': 400,  # 启用自定义动态 UA
        },
    }
    
    # 统计数据
    crawled_count = {'list': 0, 'detail': 0, 'comment': 0}
    
    def start_requests(self):
        """
        ==========================================
        【Scrapy 痛点 4】任务起点固定
        ==========================================
        Scrapy 的任务只能从 start_requests 或 start_urls 开始
        无法从外部动态注入任务
        
        🌟 Funboost 对比：
        - 任务可以从任何地方发起：crawl_list_page.push(page=1)
        - 支持 HTTP API 动态注入任务（funboost.faas）
        - 支持 RPC 远程调用发布任务
        - 支持定时任务自动发布（ApsJobAdder）
        
        ⭐ 外部系统实时动态注入"二级任务"的需求：
        假设运营人员在后台看到一条新闻需要重新爬取，他可以直接调用：
           crawl_detail_page.push(news_id=12345)
        这个任务会立即进入消息队列，等待消费者处理。
        
        💔 Scrapy 完全无法实现这种外部动态注入！
        """
        print("=" * 60)
        print("新闻爬虫 - Scrapy 实现")
        print("☠️ 对比 Funboost，Scrapy 有诸多局限性，详见代码注释")
        print("=" * 60)
        print()
        
        # 爬取前3页新闻列表
        for page in range(1, 4):
            url = f"{BASE_URL}/news/list?page={page}&size=5"
            print(f"[列表页] 发起请求: {url}")
            yield Request(
                url=url,
                callback=self.parse_list_page,
                meta={'page': page},
                # ==========================================
                # 【Scrapy 痛点 5】错误处理需要配置 errback
                # ==========================================
                # 💔 Scrapy：需要分别配置 callback 和 errback
                # 🌟 Funboost：异常自动重试，max_retry_times=3
                errback=self.handle_error,
            )
    
    def parse_list_page(self, response):
        """
        解析新闻列表页
        
        ==========================================
        【Scrapy 痛点 6】callback 回调地狱
        ==========================================
        Scrapy 的解析流程必须通过 callback 链接：
          start_requests -> parse_list_page -> parse_detail_page -> ...
        
        这种写法的问题：
          - 代码逻辑被切割成多个回调函数
          - 难以追踪完整的爬取路径
          - 传递上下文数据需要通过 meta 字典
        
        🌟 Funboost 对比：
          - 直观的函数调用链：
            crawl_list_page 中直接 crawl_detail_page.push(news_id=xxx)
          - 每个函数独立，逻辑清晰
          - 上下文通过函数参数传递，类型安全
          - 思维方式：平铺直叙，如写普通脚本
        """
        page = response.meta.get('page', 1)
        
        try:
            news_list = json.loads(response.text)
            self.crawled_count['list'] += 1
            print(f"[列表页] 获取到 {len(news_list)} 条新闻 (第{page}页)")
            
            # 遍历新闻列表，发起详情页请求
            for news_item in news_list:
                news_id = news_item['id']
                title = news_item['title']
                print(f"  -> 发现新闻 [ID: {news_id}] {title}")
                
                # 请求详情页
                detail_url = f"{BASE_URL}/news/{news_id}"
                yield Request(
                    url=detail_url,
                    callback=self.parse_detail_page,
                    # ==========================================
                    # 【Scrapy 痛点 7】meta 传参容易出错
                    # ==========================================
                    # 💔 Scrapy：通过 meta 字典传递数据，没有类型检查
                    # 🌟 Funboost：函数参数直接传递，IDE 可以检查类型
                    #            crawl_detail_page.push(news_id=news_id, title=title)
                    meta={'news_id': news_id, 'title': title},
                    errback=self.handle_error,
                )
        except Exception as e:
            print(f"[列表页] 解析失败: {e}")
    
    def parse_detail_page(self, response):
        """
        解析新闻详情页
        
        ==========================================
        【boost_spider 的 SpiderResponse 优势】
        ==========================================
        在 Funboost 爬虫中，使用 boost_spider 的 RequestClient 发请求：
        
        from boost_spider import RequestClient
        client = RequestClient(proxy_name_list=None, request_retry_times=3)
        resp = client.get(url)  # 返回 SpiderResponse 对象
        
        SpiderResponse 兼具 requests.Response 的所有功能，同时增加：
        - resp.xpath('//div[@class="xxx"]')  -> 类似 Scrapy selector
        - resp.css('div.xxx')                -> CSS 选择器
        - resp.resp_dict                     -> 自动解析 JSON
        - resp.re_search / re_findall        -> 正则匹配
        - resp.selector                      -> parsel.Selector 对象
        
        🌟 你羡慕的 Scrapy selector 功能，boost_spider 全都有！
        🌟 而且 boost_spider 的 RequestClient 还内置了：
           - 代理管理（多代理商轮换）
           - Session 管理
           - 请求重试    
           - UA 随机化
        """
        news_id = response.meta.get('news_id')
        title = response.meta.get('title')
        
        try:
            news_detail = json.loads(response.text)
            self.crawled_count['detail'] += 1
            
            content = news_detail.get('content', '')
            author = news_detail.get('author', '未知')
            publish_time = news_detail.get('publish_time', '未知')
            
            print("=" * 60)
            print(f"[爬取成功] 新闻ID: {news_id}")
            print(f"标题: {title}")
            print(f"作者: {author}")
            print(f"发布时间: {publish_time}")
            print(f"正文预览: {content[:100]}...")
            print("=" * 60)
            
            # 💔 Scrapy 需要 yield item 给 Pipeline 处理
            # 🌟 Funboost 对比：sink.save("news_detail", data) 一行代码
            yield {
                'type': 'news_detail',
                'news_id': news_id,
                'title': title,
                'author': author,
                'publish_time': publish_time,
                'content': content,
            }
            
            # 请求评论页（前2页）
            for page in range(1, 3):
                comments_url = f"{BASE_URL}/news/{news_id}/comments?page={page}&size=10"
                yield Request(
                    url=comments_url,
                    callback=self.parse_comments_page,
                    meta={'news_id': news_id, 'title': title, 'page': page},
                    errback=self.handle_error,
                )
                print(f"  -> 已发起: 爬取新闻{news_id}的第{page}页评论")
                
        except Exception as e:
            print(f"[详情页] 解析失败 (ID: {news_id}): {e}")
    
    def parse_comments_page(self, response):
        """
        解析评论页（使用 XPath）
        
        ==========================================
        【XPath/CSS 解析对比】
        ==========================================
        
        Scrapy 内置强大的 Selector：
          response.xpath('//div[@class="comment-item"]')
          response.css('div.comment-item')
        
        🌟 boost_spider 的 SpiderResponse 同样支持：
          resp.xpath('//div[@class="comment-item"]')
          resp.css('div.comment-item')
        
        两者在解析能力上几乎一样强大！
        但 boost_spider 的优势在于：
          - 与 Funboost 分布式调度无缝集成
          - RequestClient 内置代理/重试/UA管理
          - 无需学习 Twisted 异步编程
        """
        news_id = response.meta.get('news_id')
        title = response.meta.get('title')
        page = response.meta.get('page')
        
        print(f"[评论页] 正在解析: 新闻{news_id} 第{page}页")
        
        # 使用 XPath 解析评论
        comment_items = response.xpath('//div[@class="comment-item"]')
        print(f"[评论页] 找到 {len(comment_items)} 条评论")
        
        comments = []
        for item in comment_items:
            comment_id = item.xpath('./@data-id').get()
            author = item.xpath('.//span[@class="author"]/text()').get()
            time_str = item.xpath('.//span[@class="time"]/text()').get()
            content = item.xpath('.//p[@class="text"]/text()').get()
            likes = item.xpath('.//span[@class="likes"]/text()').get()
            
            comment = {
                'comment_id': comment_id,
                'author': author,
                'time': time_str,
                'content': content,
                'likes': likes,
            }
            comments.append(comment)
            
            print(f"  📝 评论#{comment_id} | {author} | {time_str}")
            print(f"     内容: {content}")
            print(f"     点赞: {likes}")
        
        self.crawled_count['comment'] += 1
        
        print("=" * 60)
        print(f"[评论爬取成功] 新闻ID: {news_id}, 第{page}页")
        print(f"标题: {title}")
        print(f"共解析 {len(comments)} 条评论")
        print("=" * 60)
        
        # ==========================================
        # 【Scrapy 痛点 8】数据持久化需要 Pipeline
        # ==========================================
        # 💔 Scrapy：需要配置 ItemPipeline 处理数据
        # 🌟 boost_spider 对比：
        #    - DatasetSink：一行代码保存到 MySQL/PostgreSQL/SQLite
        #    - MongoSink：一行代码保存到 MongoDB
        #    - MysqlSink：直接保存到 MySQL
        #
        # 示例：
        #   from boost_spider import DatasetSink
        #   sink = DatasetSink('mysql://user:pass@host/db')
        #   sink.save('comments', comment_data)
        
        yield {
            'type': 'comments',
            'news_id': news_id,
            'page': page,
            'comments': comments,
        }
    
    def handle_error(self, failure):
        """
        错误处理
        
        ==========================================
        【Scrapy 痛点 9】错误处理复杂
        ==========================================
        💔 Scrapy：需要配置 errback，处理 Twisted Failure 对象
        🌟 Funboost：异常自动重试，max_retry_times=3
                   抛出 ExceptionForRetry 触发重试
                   抛出 ExceptionForRequeue 重新入队
                   抛出 ExceptionForPushToDlxqueue 推送到死信队列
        """
        print(f"[错误] 请求失败: {failure.request.url}")
        print(f"[错误] 原因: {failure.value}")
    
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider
    
    def spider_closed(self, spider):
        """爬虫关闭时输出统计"""
        print()
        print("=" * 60)
        print("爬虫运行结束 - 统计数据")
        print("=" * 60)
        print(f"列表页爬取: {self.crawled_count['list']} 页")
        print(f"详情页爬取: {self.crawled_count['detail']} 篇")
        print(f"评论页爬取: {self.crawled_count['comment']} 页")
        print()
        print("=" * 60)
        print("⚠️ Scrapy 的局限性总结：")
        print("=" * 60)
        print("1. ❌ 无法外部动态注入任务（Funboost ✅ 可以）")
        print("2. ❌ 分布式需要额外插件（Funboost ✅ 原生支持40+中间件）")
        print("3. ❌ 精确流控困难（Funboost ✅ qps=5 精确控制）")
        print("4. ❌ 任务不持久化（Funboost ✅ 支持断点续爬）")
        print("5. ❌ 配置分散（Funboost ✅ 装饰器一处配置）")
        print("6. ❌ callback 回调链复杂（Funboost ✅ 平铺直叙）")
        print("=" * 60)


# ========================================
# 【Scrapy 痛点 10】启动方式固定
# ========================================
# 💔 Scrapy：需要使用 scrapy crawl spider_name 命令
#           或者使用 CrawlerProcess 包装
#
# 🌟 Funboost 对比：
#   crawl_list_page.consume()  # 启动消费
#   BoostersManager.consume_group("news_crawler_group")  # 分组启动
#   ctrl_c_recv()  # 阻塞主线程
#
# Funboost 可以更灵活地：
#   - 单独启动某个消费函数
#   - 按分组启动一组消费函数
#   - 多进程启动提升性能

if __name__ == "__main__":
    print()
    print("=" * 60)
    print("         Scrapy 新闻爬虫 vs Funboost 爬虫")
    print("=" * 60)
    print()
    print("⚠️ 请先启动 news_server.py：")
    print("   cd demo_crawler")
    print("   python news_server.py")
    print()
    print("📖 对比 Funboost 实现请查看：")
    print("   funboost_imp/boost_spider_crawler.py")
    print()
    print("=" * 60)
    print()
    
    # 使用 CrawlerProcess 运行爬虫
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    })
    
    process.crawl(NewsSpider)
    process.start()

`````

--- **end of file: demo_crawler/scrapy_imp/scrapy_spider_crawler.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/threadpool_crawler_imp/threadpool_crawler.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/threadpool_crawler_imp/threadpool_crawler.py`

#### 📝 Module Docstring

`````
================================================================================
        新闻爬虫 - 使用 ThreadPoolExecutor 原生线程池实现
================================================================================

🎯 本文件目的：
   使用 Python 原生的 ThreadPoolExecutor 实现新闻爬虫，
   与 Funboost + boost_spider 和 Scrapy 形成三方对比。

================================================================================
                    ⚠️ ThreadPoolExecutor 的局限性
================================================================================

📊 与 Funboost 对比：
┌─────────────────────────┬────────────────────────────────┬────────────────────────────────┐
│       对比项            │     ThreadPoolExecutor          │     Funboost + boost_spider    │
├─────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ 分布式能力              │ ❌ 仅单机，无法跨机器          │ ⭐ 40+ 中间件原生分布式         │
│ 任务持久化              │ ❌ 进程死亡任务全部丢失        │ ⭐ 消息队列持久化，断点续爬     │
│ 消息确认(ACK)           │ ❌ 不支持                      │ ⭐ 消息处理失败自动重新入队     │
│ 精确流控(QPS)           │ ❌ 需要自己手动实现            │ ⭐ qps=5 一个参数搞定          │
│ 分布式流控              │ ❌ 无法实现                    │ ⭐ 多机统一 QPS 限制           │
│ 任务去重                │ ❌ 需要自己维护 set/bloom      │ ⭐ do_task_filtering=True      │
│ 自动重试                │ ❌ 需要自己 try-except 封装    │ ⭐ max_retry_times=3           │
│ 外部动态任务注入        │ ❌ 无法从外部注入任务          │ ⭐ HTTP API / RPC 随时注入     │
│ 监控面板                │ ❌ 无                          │ ⭐ 内置 Web 管理面板           │
│ RPC 获取结果            │ ❌ 需要自己实现                │ ⭐ is_using_rpc_mode=True      │
│ 定时任务                │ ❌ 需要配合其他库              │ ⭐ 内置 APScheduler            │
│ 代理/UA管理             │ ❌ 完全手动实现                │ ⭐ RequestClient 一行代码      │
│ 数据保存                │ ❌ 完全手动实现                │ ⭐ DatasetSink 一行代码        │
└─────────────────────────┴────────────────────────────────┴────────────────────────────────┘

💔 ThreadPoolExecutor 的本质问题：
   - 它只是一个"线程池"，不是任务调度框架
   - 所有任务和状态都在内存中，进程一死全没了
   - 适合简单的并发场景，不适合生产级爬虫

================================================================================
`````

#### 📦 Imports

- `import requests`
- `from concurrent.futures import ThreadPoolExecutor`
- `from concurrent.futures import as_completed`
- `import time`
- `import sqlite3`
- `import os`
- `import random`
- `from threading import Lock`
- `from lxml import etree`

#### 🔧 Public Functions (8)

- `def init_database()`
  - *Line: 79*
  - *初始化数据库*

- `def save_news_to_db(news_data)`
  - *Line: 110*
  - *保存新闻到数据库*

- `def save_comment_to_db(comment_data)`
  - *Line: 123*
  - *保存评论到数据库*

- `def get_random_headers()`
  - *Line: 148*
  - *获取随机请求头*

- `def request_with_retry(url, max_retries = 3)`
  - *Line: 161*
  - *带重试的请求函数*

- `def crawl_list_page(page: int = 1, size: int = 10)`
  - *Line: 179*
  - **Docstring:**
  `````
  爬取新闻列表页
  
  💔 ThreadPoolExecutor 痛点 6：无法从外部动态注入任务
  - 所有任务必须在代码中预先定义
  - 无法通过 HTTP API 实时添加任务
  
  🌟 Funboost 对比：
  - crawl_list_page.push(page=5) 随时注入
  - funboost.faas HTTP API 动态注入
  `````

- `def crawl_detail_page(news_id: int, title: str)`
  - *Line: 217*
  - **Docstring:**
  `````
  爬取新闻详情页
  
  💔 ThreadPoolExecutor 痛点 8：需要手动实现任务去重
  🌟 Funboost 对比：do_task_filtering=True 自动去重
  `````

- `def crawl_comments_page(news_id: int, title: str, page: int = 1, size: int = 10)`
  - *Line: 274*
  - **Docstring:**
  `````
  爬取新闻评论页
  
  💔 ThreadPoolExecutor 痛点 9：无法使用 xpath/css 解析
  - 需要自己安装 lxml/parsel 并手动处理
  
  🌟 Funboost 对比：SpiderResponse.xpath() 开箱即用
  `````


---

`````python
# -*- coding: utf-8 -*-
"""
================================================================================
        新闻爬虫 - 使用 ThreadPoolExecutor 原生线程池实现
================================================================================

🎯 本文件目的：
   使用 Python 原生的 ThreadPoolExecutor 实现新闻爬虫，
   与 Funboost + boost_spider 和 Scrapy 形成三方对比。

================================================================================
                    ⚠️ ThreadPoolExecutor 的局限性
================================================================================

📊 与 Funboost 对比：
┌─────────────────────────┬────────────────────────────────┬────────────────────────────────┐
│       对比项            │     ThreadPoolExecutor          │     Funboost + boost_spider    │
├─────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ 分布式能力              │ ❌ 仅单机，无法跨机器          │ ⭐ 40+ 中间件原生分布式         │
│ 任务持久化              │ ❌ 进程死亡任务全部丢失        │ ⭐ 消息队列持久化，断点续爬     │
│ 消息确认(ACK)           │ ❌ 不支持                      │ ⭐ 消息处理失败自动重新入队     │
│ 精确流控(QPS)           │ ❌ 需要自己手动实现            │ ⭐ qps=5 一个参数搞定          │
│ 分布式流控              │ ❌ 无法实现                    │ ⭐ 多机统一 QPS 限制           │
│ 任务去重                │ ❌ 需要自己维护 set/bloom      │ ⭐ do_task_filtering=True      │
│ 自动重试                │ ❌ 需要自己 try-except 封装    │ ⭐ max_retry_times=3           │
│ 外部动态任务注入        │ ❌ 无法从外部注入任务          │ ⭐ HTTP API / RPC 随时注入     │
│ 监控面板                │ ❌ 无                          │ ⭐ 内置 Web 管理面板           │
│ RPC 获取结果            │ ❌ 需要自己实现                │ ⭐ is_using_rpc_mode=True      │
│ 定时任务                │ ❌ 需要配合其他库              │ ⭐ 内置 APScheduler            │
│ 代理/UA管理             │ ❌ 完全手动实现                │ ⭐ RequestClient 一行代码      │
│ 数据保存                │ ❌ 完全手动实现                │ ⭐ DatasetSink 一行代码        │
└─────────────────────────┴────────────────────────────────┴────────────────────────────────┘

💔 ThreadPoolExecutor 的本质问题：
   - 它只是一个"线程池"，不是任务调度框架
   - 所有任务和状态都在内存中，进程一死全没了
   - 适合简单的并发场景，不适合生产级爬虫

================================================================================
"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import sqlite3
import os
import random
from threading import Lock

# ================= 配置 =================
BASE_URL = "http://127.0.0.1:7000"

# ==========================================
# 💔 ThreadPoolExecutor 痛点 1：需要自己创建和管理多个线程池
# ==========================================
# 每个爬取层级使用独立的线程池
# 🌟 Funboost 对比：@boost 装饰器自动管理，无需手动创建线程池
list_page_pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix="list_page")
detail_page_pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="detail_page")
comments_page_pool = ThreadPoolExecutor(max_workers=15, thread_name_prefix="comments_page")

# ==========================================
# 💔 ThreadPoolExecutor 痛点 2：需要自己维护任务去重
# ==========================================
# 🌟 Funboost 对比：do_task_filtering=True 一个参数搞定
crawled_detail_ids = set()
crawled_detail_lock = Lock()

crawled_comment_keys = set()
crawled_comment_lock = Lock()

# ==========================================
# 💔 ThreadPoolExecutor 痛点 3：需要自己实现数据保存
# ==========================================
# 🌟 Funboost 对比：DatasetSink("sqlite:///data.db").save("table", data) 一行代码
db_lock = Lock()
db_path = os.path.join(os.path.dirname(__file__), 'threadpool_crawled_data.db')

def init_database():
    """初始化数据库"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news_detail (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_id INTEGER,
            title TEXT,
            author TEXT,
            publish_time TEXT,
            content TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_id INTEGER,
            news_title TEXT,
            page INTEGER,
            comment_id TEXT,
            author TEXT,
            time TEXT,
            content TEXT,
            likes TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("💔 [ThreadPool] 数据库初始化完成（需要自己写 ~30 行建表代码）")

def save_news_to_db(news_data):
    """保存新闻到数据库"""
    with db_lock:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO news_detail (news_id, title, author, publish_time, content)
            VALUES (?, ?, ?, ?, ?)
        ''', (news_data['news_id'], news_data['title'], news_data['author'],
              news_data['publish_time'], news_data['content']))
        conn.commit()
        conn.close()

def save_comment_to_db(comment_data):
    """保存评论到数据库"""
    with db_lock:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO comments (news_id, news_title, page, comment_id, author, time, content, likes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (comment_data['news_id'], comment_data['news_title'], comment_data['page'],
              comment_data['comment_id'], comment_data['author'], comment_data['time'],
              comment_data['content'], comment_data['likes']))
        conn.commit()
        conn.close()

# ==========================================
# 💔 ThreadPoolExecutor 痛点 4：需要自己实现动态 UA
# ==========================================
# 🌟 Funboost 对比：RequestClient(is_change_ua_every_request=True) 一个参数
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
]

def get_random_headers():
    """获取随机请求头"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Referer': 'https://news.example.com/',
    }

# ==========================================
# 💔 ThreadPoolExecutor 痛点 5：需要自己实现重试逻辑
# ==========================================
# 🌟 Funboost 对比：max_retry_times=3 一个参数搞定
def request_with_retry(url, max_retries=3):
    """带重试的请求函数"""
    for i in range(max_retries):
        try:
            response = requests.get(url, headers=get_random_headers(), timeout=10)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"  💔 [ThreadPool] 请求失败 (第{i+1}次): {e}")
            if i < max_retries - 1:
                time.sleep(1)
    return None


# ==========================================
# 爬虫函数定义
# ==========================================

def crawl_list_page(page: int = 1, size: int = 10):
    """
    爬取新闻列表页
    
    💔 ThreadPoolExecutor 痛点 6：无法从外部动态注入任务
    - 所有任务必须在代码中预先定义
    - 无法通过 HTTP API 实时添加任务
    
    🌟 Funboost 对比：
    - crawl_list_page.push(page=5) 随时注入
    - funboost.faas HTTP API 动态注入
    """
    url = f"{BASE_URL}/news/list?page={page}&size={size}"
    print(f"[列表页] 正在爬取: {url}")
    
    response = request_with_retry(url)
    if not response:
        print(f"[列表页] 爬取失败: {url}")
        return None
    
    news_list = response.json()
    print(f"[列表页] 获取到 {len(news_list)} 条新闻")
    
    # 💔 痛点 7：需要手动收集 Future 并等待
    # 🌟 Funboost 对比：crawl_detail_page.push(...) 自动进入队列
    futures = []
    for news_item in news_list:
        news_id = news_item["id"]
        title = news_item["title"]
        print(f"  -> 发现新闻 [ID: {news_id}] {title}")
        
        # 使用详情页线程池提交任务
        future = detail_page_pool.submit(crawl_detail_page, news_id, title)
        futures.append(future)
    
    return {"page": page, "count": len(news_list), "futures": futures}


def crawl_detail_page(news_id: int, title: str):
    """
    爬取新闻详情页
    
    💔 ThreadPoolExecutor 痛点 8：需要手动实现任务去重
    🌟 Funboost 对比：do_task_filtering=True 自动去重
    """
    # 手动去重逻辑
    with crawled_detail_lock:
        if news_id in crawled_detail_ids:
            print(f"  💔 [ThreadPool] 跳过已爬取: news_id={news_id}")
            return None
        crawled_detail_ids.add(news_id)
    
    url = f"{BASE_URL}/news/{news_id}"
    print(f"[详情页] 正在爬取: {url}")
    
    response = request_with_retry(url)
    if not response:
        print(f"[详情页] 爬取失败 (ID: {news_id})")
        return None
    
    news_detail = response.json()
    
    content = news_detail.get("content", "")
    author = news_detail.get("author", "未知")
    publish_time = news_detail.get("publish_time", "未知")
    
    print("=" * 60)
    print(f"[爬取成功] 新闻ID: {news_id}")
    print(f"标题: {title}")
    print(f"作者: {author}")
    print(f"发布时间: {publish_time}")
    print(f"正文预览: {content[:100]}...")
    print("=" * 60)
    
    # 保存到数据库
    news_data = {
        "news_id": news_id,
        "title": title,
        "author": author,
        "publish_time": publish_time,
        "content": content,
    }
    save_news_to_db(news_data)
    print(f"  💔 [ThreadPool] 保存新闻到 SQLite（需要自己写保存函数）")
    
    # 提交评论页爬取任务
    futures = []
    for page in range(1, 3):
        future = comments_page_pool.submit(crawl_comments_page, news_id, title, page)
        futures.append(future)
        print(f"  -> 已提交: 爬取新闻{news_id}的第{page}页评论")
    
    return {"news_id": news_id, "futures": futures}


def crawl_comments_page(news_id: int, title: str, page: int = 1, size: int = 10):
    """
    爬取新闻评论页
    
    💔 ThreadPoolExecutor 痛点 9：无法使用 xpath/css 解析
    - 需要自己安装 lxml/parsel 并手动处理
    
    🌟 Funboost 对比：SpiderResponse.xpath() 开箱即用
    """
    # 手动去重逻辑
    cache_key = f"{news_id}_{page}"
    with crawled_comment_lock:
        if cache_key in crawled_comment_keys:
            print(f"  💔 [ThreadPool] 跳过已爬取: {cache_key}")
            return None
        crawled_comment_keys.add(cache_key)
    
    url = f"{BASE_URL}/news/{news_id}/comments?page={page}&size={size}"
    print(f"[评论页] 正在爬取: {url}")
    
    response = request_with_retry(url)
    if not response:
        print(f"[评论页] 爬取失败 (新闻ID: {news_id}, 第{page}页)")
        return None
    
    # 💔 痛点 10：需要手动安装和使用 lxml/parsel 解析 HTML
    # 🌟 Funboost 对比：resp.xpath('//div[@class="xxx"]') 开箱即用
    from lxml import etree
    html = etree.HTML(response.text)
    comment_items = html.xpath('//div[@class="comment-item"]')
    
    print(f"[评论页] 找到 {len(comment_items)} 条评论")
    
    comments = []
    for item in comment_items:
        comment_id = item.get('data-id')
        author = item.xpath('.//span[@class="author"]/text()')
        author = author[0] if author else None
        time_str = item.xpath('.//span[@class="time"]/text()')
        time_str = time_str[0] if time_str else None
        content = item.xpath('.//p[@class="text"]/text()')
        content = content[0] if content else None
        likes = item.xpath('.//span[@class="likes"]/text()')
        likes = likes[0] if likes else None
        
        comment = {
            "news_id": news_id,
            "news_title": title,
            "page": page,
            "comment_id": comment_id,
            "author": author,
            "time": time_str,
            "content": content,
            "likes": likes,
        }
        comments.append(comment)
        save_comment_to_db(comment)
        
        print(f"  📝 评论#{comment_id} | {author} | {time_str}")
        print(f"     内容: {content}")
        print(f"     点赞: {likes}")
    
    print("=" * 60)
    print(f"[评论爬取成功] 新闻ID: {news_id}, 第{page}页")
    print(f"标题: {title}")
    print(f"共解析 {len(comments)} 条评论")
    print(f"  💔 [ThreadPool] 保存 {len(comments)} 条评论到 SQLite")
    print("=" * 60)
    
    return {"news_id": news_id, "page": page, "comments_count": len(comments)}


# ================= 入口 =================
if __name__ == "__main__":
    print()
    print("=" * 60)
    print("  新闻爬虫 - ThreadPoolExecutor 原生线程池实现")
    print("=" * 60)
    print()
    print("⚠️ 请先启动 news_server.py：")
    print("   cd demo_crawler")
    print("   python news_server.py")
    print()
    print("💔 ThreadPoolExecutor 的局限性：")
    print("   - 仅单机，无法分布式")
    print("   - 进程死亡任务全部丢失")
    print("   - 需要手动实现：去重、重试、流控、数据保存...")
    print()
    print("=" * 60)
    print()
    
    # 初始化数据库
    init_database()
    
    start_time = time.time()
    
    # 💔 痛点 11：需要手动管理所有 Future
    # 🌟 Funboost 对比：ctrl_c_recv() 阻塞即可
    all_futures = []
    
    # 爬取前3页列表
    for page in range(1, 4):
        future = list_page_pool.submit(crawl_list_page, page, 5)
        all_futures.append(future)
    
    # 等待所有任务完成
    print("\n💔 [ThreadPool] 等待所有任务完成...")
    for future in as_completed(all_futures):
        try:
            result = future.result()
            if result and 'futures' in result:
                all_futures.extend(result.get('futures', []))
        except Exception as e:
            print(f"💔 [ThreadPool] 任务异常: {e}")
    
    # 💔 痛点 12：需要手动关闭线程池
    # 🌟 Funboost 对比：无需手动管理
    list_page_pool.shutdown(wait=True)
    detail_page_pool.shutdown(wait=True)
    comments_page_pool.shutdown(wait=True)
    
    elapsed = time.time() - start_time
    
    print()
    print("=" * 60)
    print("爬虫运行结束 - ThreadPoolExecutor")
    print("=" * 60)
    print(f"耗时: {elapsed:.2f} 秒")
    print()
    print("💔 ThreadPoolExecutor 需要手动实现的功能：")
    print("   1. 多个线程池的创建和管理")
    print("   2. 任务去重（set + Lock）")
    print("   3. 请求重试逻辑")
    print("   4. 动态 UA 随机")
    print("   5. 数据库保存（建表 + 写入）")
    print("   6. HTML 解析（安装 lxml）")
    print("   7. 等待所有 Future 完成")
    print("   8. 关闭线程池")
    print()
    print("🌟 Funboost 只需要：")
    print("   @boost(BoosterParams(...)) 装饰器 + .push() 调用")
    print("=" * 60)

`````

--- **end of file: demo_crawler/threadpool_crawler_imp/threadpool_crawler.py** (project: boost_spider) --- 

---


--- **start of file: demo_crawler/threadpool_redis_crawler_imp/redis_threadpool_crawler.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `demo_crawler/threadpool_redis_crawler_imp/redis_threadpool_crawler.py`

#### 📝 Module Docstring

`````
================================================================================
     新闻爬虫 - 使用 Redis + ThreadPoolExecutor 手动实现分布式
================================================================================

🎯 本文件目的：
   使用 Redis blpop + ThreadPoolExecutor 手动实现一个"分布式"爬虫，
   展示如果不使用 Funboost，自己实现分布式调度有多麻烦。

================================================================================
                    ⚠️ 手动实现分布式的痛点
================================================================================

这个实现需要自己手动处理：
1. Redis 连接管理
2. 3 个 while True 循环监听队列
3. 3 个独立的线程池
4. JSON 序列化/反序列化
5. 异常处理和重试逻辑
6. 任务去重
7. 数据保存
8. 优雅退出

💔 代码量：~400 行
🌟 Funboost 相同功能：~100 行（3 个 @boost 装饰的函数）

================================================================================
`````

#### 📦 Imports

- `import json`
- `import time`
- `import threading`
- `import sys`
- `import requests`
- `import sqlite3`
- `import os`
- `import random`
- `from concurrent.futures import ThreadPoolExecutor`
- `from threading import Lock`
- `import redis`
- `from lxml import etree`

#### 🔧 Public Functions (13)

- `def get_redis_client()`
  - *Line: 75*

- `def init_database()`
  - *Line: 104*
  - *初始化数据库*

- `def save_news_to_db(news_data)`
  - *Line: 135*

- `def save_comment_to_db(comment_data)`
  - *Line: 147*

- `def get_random_headers()`
  - *Line: 169*

- `def request_with_retry(url, max_retries = 3)`
  - *Line: 179*

- `def process_list_page(msg_data)`
  - *Line: 196*
  - *处理列表页任务*

- `def process_detail_page(msg_data)`
  - *Line: 225*
  - *处理详情页任务*

- `def process_comments_page(msg_data)`
  - *Line: 274*
  - *处理评论页任务*

- `def consume_list_page()`
  - *Line: 339*
  - *消费列表页队列*

- `def consume_detail_page()`
  - *Line: 358*
  - *消费详情页队列*

- `def consume_comments_page()`
  - *Line: 375*
  - *消费评论页队列*

- `def publish_initial_tasks()`
  - *Line: 397*
  - *发布初始的列表页任务*


---

`````python
# -*- coding: utf-8 -*-
"""
================================================================================
     新闻爬虫 - 使用 Redis + ThreadPoolExecutor 手动实现分布式
================================================================================

🎯 本文件目的：
   使用 Redis blpop + ThreadPoolExecutor 手动实现一个"分布式"爬虫，
   展示如果不使用 Funboost，自己实现分布式调度有多麻烦。

================================================================================
                    ⚠️ 手动实现分布式的痛点
================================================================================

这个实现需要自己手动处理：
1. Redis 连接管理
2. 3 个 while True 循环监听队列
3. 3 个独立的线程池
4. JSON 序列化/反序列化
5. 异常处理和重试逻辑
6. 任务去重
7. 数据保存
8. 优雅退出

💔 代码量：~400 行
🌟 Funboost 相同功能：~100 行（3 个 @boost 装饰的函数）

================================================================================
"""

import json
import time
import threading

import sys
import requests
import sqlite3
import os
import random
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# ==========================================
# 💔 痛点 1：需要自己安装和管理 Redis 连接
# ==========================================
# 🌟 Funboost 对比：broker_kind=BrokerEnum.REDIS_ACK_ABLE 一个参数搞定
try:
    import redis
except ImportError:
    print("请安装 redis: pip install redis")
    sys.exit(1)

# ================= 配置 =================
BASE_URL = "http://127.0.0.1:7000"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0

# Redis 队列名称
QUEUE_LIST_PAGE = "crawler:list_page"
QUEUE_DETAIL_PAGE = "crawler:detail_page"
QUEUE_COMMENTS_PAGE = "crawler:comments_page"

# ==========================================
# 💔 痛点 2：需要自己创建 Redis 连接池
# ==========================================
# 🌟 Funboost 对比：自动管理连接池
redis_pool = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True
)

def get_redis_client():
    return redis.Redis(connection_pool=redis_pool)

# ==========================================
# 💔 痛点 3：需要自己创建和管理多个线程池
# ==========================================
# 🌟 Funboost 对比：@boost 装饰器自动管理
list_page_pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix="list_page")
detail_page_pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="detail_page")
comments_page_pool = ThreadPoolExecutor(max_workers=15, thread_name_prefix="comments_page")



# ==========================================
# 💔 痛点 5：需要自己维护任务去重
# ==========================================
# 🌟 Funboost 对比：do_task_filtering=True 一个参数
crawled_detail_ids = set()
crawled_detail_lock = Lock()
crawled_comment_keys = set()
crawled_comment_lock = Lock()

# ==========================================
# 💔 痛点 6：需要自己实现数据保存
# ==========================================
# 🌟 Funboost 对比：DatasetSink.save() 一行代码
db_lock = Lock()
db_path = os.path.join(os.path.dirname(__file__), 'redis_threadpool_data.db')

def init_database():
    """初始化数据库"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news_detail (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_id INTEGER,
            title TEXT,
            author TEXT,
            publish_time TEXT,
            content TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_id INTEGER,
            news_title TEXT,
            page INTEGER,
            comment_id TEXT,
            author TEXT,
            time TEXT,
            content TEXT,
            likes TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("💔 [Redis+Pool] 数据库初始化完成")

def save_news_to_db(news_data):
    with db_lock:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO news_detail (news_id, title, author, publish_time, content)
            VALUES (?, ?, ?, ?, ?)
        ''', (news_data['news_id'], news_data['title'], news_data['author'],
              news_data['publish_time'], news_data['content']))
        conn.commit()
        conn.close()

def save_comment_to_db(comment_data):
    with db_lock:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO comments (news_id, news_title, page, comment_id, author, time, content, likes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (comment_data['news_id'], comment_data['news_title'], comment_data['page'],
              comment_data['comment_id'], comment_data['author'], comment_data['time'],
              comment_data['content'], comment_data['likes']))
        conn.commit()
        conn.close()

# ==========================================
# 💔 痛点 7：需要自己实现动态 UA
# ==========================================
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
]

def get_random_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

# ==========================================
# 💔 痛点 8：需要自己实现请求重试
# ==========================================
def request_with_retry(url, max_retries=3):
    for i in range(max_retries):
        try:
            response = requests.get(url, headers=get_random_headers(), timeout=10)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"  💔 请求失败 (第{i+1}次): {e}")
            if i < max_retries - 1:
                time.sleep(1)
    return None


# ==========================================
# 爬虫处理函数
# ==========================================

def process_list_page(msg_data):
    """处理列表页任务"""
    page = msg_data.get('page', 1)
    size = msg_data.get('size', 10)
    
    url = f"{BASE_URL}/news/list?page={page}&size={size}"
    print(f"[列表页] 正在爬取: {url}")
    
    response = request_with_retry(url)
    if not response:
        print(f"[列表页] 爬取失败: {url}")
        return
    
    news_list = response.json()
    print(f"[列表页] 获取到 {len(news_list)} 条新闻")
    
    # 💔 痛点 9：需要手动序列化并推送到 Redis
    # 🌟 Funboost 对比：crawl_detail_page.push(news_id=xxx)
    r = get_redis_client()
    for news_item in news_list:
        news_id = news_item["id"]
        title = news_item["title"]
        print(f"  -> 发现新闻 [ID: {news_id}] {title}")
        
        # 手动 JSON 序列化并推送
        task_data = json.dumps({"news_id": news_id, "title": title})
        r.rpush(QUEUE_DETAIL_PAGE, task_data)


def process_detail_page(msg_data):
    """处理详情页任务"""
    news_id = msg_data.get('news_id')
    title = msg_data.get('title', '')
    
    # 手动去重
    with crawled_detail_lock:
        if news_id in crawled_detail_ids:
            print(f"  💔 跳过已爬取: news_id={news_id}")
            return
        crawled_detail_ids.add(news_id)
    
    url = f"{BASE_URL}/news/{news_id}"
    print(f"[详情页] 正在爬取: {url}")
    
    response = request_with_retry(url)
    if not response:
        print(f"[详情页] 爬取失败 (ID: {news_id})")
        return
    
    news_detail = response.json()
    
    content = news_detail.get("content", "")
    author = news_detail.get("author", "未知")
    publish_time = news_detail.get("publish_time", "未知")
    
    print("=" * 60)
    print(f"[爬取成功] 新闻ID: {news_id}")
    print(f"标题: {title}")
    print(f"作者: {author}")
    print("=" * 60)
    
    # 保存到数据库
    save_news_to_db({
        "news_id": news_id,
        "title": title,
        "author": author,
        "publish_time": publish_time,
        "content": content,
    })
    
    # 推送评论页任务到 Redis
    r = get_redis_client()
    for page in range(1, 3):
        task_data = json.dumps({"news_id": news_id, "title": title, "page": page})
        r.rpush(QUEUE_COMMENTS_PAGE, task_data)
        print(f"  -> 已推送: 爬取新闻{news_id}的第{page}页评论")


def process_comments_page(msg_data):
    """处理评论页任务"""
    news_id = msg_data.get('news_id')
    title = msg_data.get('title', '')
    page = msg_data.get('page', 1)
    
    # 手动去重
    cache_key = f"{news_id}_{page}"
    with crawled_comment_lock:
        if cache_key in crawled_comment_keys:
            print(f"  💔 跳过已爬取: {cache_key}")
            return
        crawled_comment_keys.add(cache_key)
    
    url = f"{BASE_URL}/news/{news_id}/comments?page={page}&size=10"
    print(f"[评论页] 正在爬取: {url}")
    
    response = request_with_retry(url)
    if not response:
        print(f"[评论页] 爬取失败")
        return
    
    # 解析 HTML
    from lxml import etree
    html = etree.HTML(response.text)
    comment_items = html.xpath('//div[@class="comment-item"]')
    
    print(f"[评论页] 找到 {len(comment_items)} 条评论")
    
    for item in comment_items:
        comment_id = item.get('data-id')
        author = item.xpath('.//span[@class="author"]/text()')
        author = author[0] if author else None
        time_str = item.xpath('.//span[@class="time"]/text()')
        time_str = time_str[0] if time_str else None
        content = item.xpath('.//p[@class="text"]/text()')
        content = content[0] if content else None
        likes = item.xpath('.//span[@class="likes"]/text()')
        likes = likes[0] if likes else None
        
        save_comment_to_db({
            "news_id": news_id,
            "news_title": title,
            "page": page,
            "comment_id": comment_id,
            "author": author,
            "time": time_str,
            "content": content,
            "likes": likes,
        })
        
        print(f"  📝 评论#{comment_id} | {author}")
    
    print(f"[评论爬取成功] 新闻ID: {news_id}, 第{page}页, 共 {len(comment_items)} 条")


# ==========================================
# 💔 痛点 10：需要自己实现 3 个消费者循环
# ==========================================
# 🌟 Funboost 对比：
#    crawl_list_page.consume()
#    crawl_detail_page.consume()
#    crawl_comments_page.consume()
#    只需要 3 行！

def consume_list_page():
    """消费列表页队列"""
    r = get_redis_client()
    print(f"💔 [消费者] 开始监听队列: {QUEUE_LIST_PAGE}")
    
    while True:
        try:
            # blpop 阻塞等待，超时 1 秒
            result = r.blpop(QUEUE_LIST_PAGE, timeout=1)
            if result:
                _, msg = result
                msg_data = json.loads(msg)
                # 提交到线程池
                list_page_pool.submit(process_list_page, msg_data)
        except Exception as e:
            print(f"💔 [消费者] 列表页队列异常: {e}")
            time.sleep(1)


def consume_detail_page():
    """消费详情页队列"""
    r = get_redis_client()
    print(f"💔 [消费者] 开始监听队列: {QUEUE_DETAIL_PAGE}")
    
    while True:
        try:
            result = r.blpop(QUEUE_DETAIL_PAGE, timeout=1)
            if result:
                _, msg = result
                msg_data = json.loads(msg)
                detail_page_pool.submit(process_detail_page, msg_data)
        except Exception as e:
            print(f"💔 [消费者] 详情页队列异常: {e}")
            time.sleep(1)


def consume_comments_page():
    """消费评论页队列"""
    r = get_redis_client()
    print(f"💔 [消费者] 开始监听队列: {QUEUE_COMMENTS_PAGE}")
    
    while True:
        try:
            result = r.blpop(QUEUE_COMMENTS_PAGE, timeout=1)
            if result:
                _, msg = result
                msg_data = json.loads(msg)
                comments_page_pool.submit(process_comments_page, msg_data)
        except Exception as e:
            print(f"💔 [消费者] 评论页队列异常: {e}")
            time.sleep(1)


# ==========================================
# 💔 痛点 11：需要自己发布初始任务
# ==========================================
# 🌟 Funboost 对比：crawl_list_page.push(page=1) 一行代码

def publish_initial_tasks():
    """发布初始的列表页任务"""
    r = get_redis_client()
    print("💔 [发布] 发布初始任务...")
    
    for page in range(1, 4):
        task_data = json.dumps({"page": page, "size": 5})
        r.rpush(QUEUE_LIST_PAGE, task_data)
        print(f"  -> 已发布: 爬取第 {page} 页列表")


# ================= 入口 =================
if __name__ == "__main__":
    print()
    print("=" * 70)
    print("  新闻爬虫 - Redis blpop + ThreadPoolExecutor 手动分布式实现")
    print("=" * 70)
    print()
    print("⚠️ 请先启动：")
    print("   1. Redis 服务器")
    print("   2. news_server.py")
    print()
    print("💔 这个实现需要自己手动处理：")
    print("   - Redis 连接管理")
    print("   - 3 个 while True 消费者循环（永远等待消息）")
    print("   - 3 个独立的线程池")
    print("   - JSON 序列化/反序列化")
    print("   - 异常处理、重试、去重、数据保存...")
    print()
    print("🌟 Funboost 对比：")
    print("   @boost(BoosterParams(queue_name='xxx', broker_kind=BrokerEnum.REDIS_ACK_ABLE))")
    print("   def crawl_page(...): ...")
    print("   crawl_page.consume()  # 自动处理一切！永远等待消息！")
    print()
    print("=" * 70)
    print()
    
    # 初始化数据库
    init_database()
    
    # 💔 痛点 12：需要手动启动多个消费者线程
    # 🌟 Funboost 对比：BoostersManager.consume_group("xxx") 一行代码
    # 
    # 注意：这里使用 daemon=False，让消费者线程永远运行
    # 直到收到 Ctrl+C 信号才退出
    consumer_threads = [
        threading.Thread(target=consume_list_page, name="consumer_list", daemon=True),
        threading.Thread(target=consume_detail_page, name="consumer_detail", daemon=True),
        threading.Thread(target=consume_comments_page, name="consumer_comments", daemon=True),
    ]
    
    for t in consumer_threads:
        t.start()
        print(f"💔 [启动] 消费者线程: {t.name}")
    
    time.sleep(1)
    
    # 发布初始任务（仅作为示例，实际生产环境可以通过其他方式发布任务）
    publish_initial_tasks()
    
    print()
    print("=" * 70)
    print("� [永久运行模式] 消费者正在等待消息...")
    print("   - 3 个 while True 循环持续监听 Redis 队列")
    print("   - 随时可以从外部推送新任务到 Redis 队列")
    print("   - 按 Ctrl+C 退出")
    print("=" * 70)
    print()
    
    # 永久等待
    while True:
        time.sleep(3600)

    # ==========================================
    # 以下为说明
    # ==========================================
    """
    💔 手动实现分布式需要处理的痛点：
       1. Redis 连接池管理
       2. 多个线程池创建和管理
       3. 多个 while True 消费者循环（永远等待）
       4. JSON 序列化/反序列化
       5. 任务去重（set + Lock）
       6. 请求重试
       7. 动态 UA
       8. 数据库保存
       9. HTML 解析
       10. 初始任务发布
       11. 消费者线程启动
       12. 永久等待实现
    """
    print()
    print("🌟 Funboost 只需要：")
    print("   @boost(BoosterParams(...)) + .consume() + .push()")
    print("   所有痛点自动处理！永远等待消息！")
    print("=" * 70)

`````

--- **end of file: demo_crawler/threadpool_redis_crawler_imp/redis_threadpool_crawler.py** (project: boost_spider) --- 

---

# markdown content namespace: boost_scrapy codes 


## boost_spider File Tree (relative dir: `boost_scrapy`)


`````

└── boost_scrapy
    ├── __init__.py
    ├── engine.py
    ├── item.py
    ├── log.py
    ├── middleware.py
    ├── pipeline.py
    ├── request.py
    ├── response.py
    └── spider.py

`````

---


## boost_spider (relative dir: `boost_scrapy`)  Included Files (total: 9 files)


- `boost_scrapy/engine.py`

- `boost_scrapy/item.py`

- `boost_scrapy/log.py`

- `boost_scrapy/middleware.py`

- `boost_scrapy/pipeline.py`

- `boost_scrapy/request.py`

- `boost_scrapy/response.py`

- `boost_scrapy/spider.py`

- `boost_scrapy/__init__.py`


---


--- **start of file: boost_scrapy/engine.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/engine.py`

#### 📝 Module Docstring

`````
boost_scrapy.engine - 核心引擎

解析 Spider 的 yield 生成器，调度 funboost 任务。
这是 boost_scrapy 框架的核心，负责协调请求、响应、回调和入库。
`````

#### 📦 Imports

- `import traceback`
- `import time`
- `import types`
- `import requests`
- `import logging`
- `import hashlib`
- `from typing import Type`
- `from typing import List`
- `from typing import Generator`
- `from typing import Optional`
- `from typing import Callable`
- `from typing import Any`
- `from urllib.parse import urlparse`
- `from urllib.parse import parse_qsl`
- `from urllib.parse import urlencode`
- `from urllib.parse import urlunparse`
- `import json`
- `from funboost import boost`
- `from funboost import BoosterParams`
- `from funboost import BrokerEnum`
- `from funboost import ctrl_c_recv`
- `from funboost import TaskOptions`
- `from boost_scrapy.request import Request`
- `from boost_scrapy.response import Response`
- `from boost_scrapy.item import Item`
- `from boost_scrapy.spider import Spider`
- `from boost_scrapy.pipeline import Pipeline`
- `from boost_scrapy.pipeline import ConsolePipeline`
- `from boost_scrapy.middleware import Middleware`
- `from boost_scrapy.log import logger`

#### 🏛️ Classes (1)

##### 📌 `class Engine`
*Line: 31*

**Docstring:**
`````
核心引擎 - 解析 Spider 的 yield 生成器，调度 funboost 任务

工作流程:
1. 实例化 Spider
2. 初始化 Pipeline 列表
3. 执行 spider.start_requests() 获取初始 Request
4. 使用 boost_spider.RequestClient 发送请求
5. 调用 Request.callback 处理响应
6. 解析 callback 返回的生成器:
   - yield Request -> 递归处理新请求
   - yield Item -> 流经 Pipeline 入库
7. 通过 funboost 队列实现分布式调度（可选）

使用示例:
    engine = Engine()
    engine.run(MySpider)
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, pipelines: Optional[List[Pipeline]] = None, middlewares: Optional[List[Middleware]] = None, use_funboost: bool = False, broker_kind: str = BrokerEnum.PERSISTQUEUE, concurrent_num: int = 5, qps: float = 0, max_retry_times: int = 3, request_timeout: float = 30, queue_name_prefix: str = 'boost_scrapy', enable_filter: bool = True, log_level: int = logging.DEBUG)`
  - **Docstring:**
  `````
  初始化引擎
  
  Args:
      pipelines: Pipeline 实例列表（如果为 None，默认使用 ConsolePipeline）
      middlewares: Middleware 中间件列表（如 UserAgentMiddleware）
      use_funboost: 是否使用 funboost 分布式调度
      broker_kind: 消息队列类型（use_funboost=True 时有效）
      concurrent_num: 并发数
      qps: QPS 限制（0 表示不限制）
      max_retry_times: 最大重试次数
      request_timeout: 请求超时秒数
      queue_name_prefix: funboost 队列名称前缀
      enable_filter: 是否启用请求去重
      log_level: 日志级别
  `````
  - **Parameters:**
    - `self`
    - `pipelines: Optional[List[Pipeline]] = None`
    - `middlewares: Optional[List[Middleware]] = None`
    - `use_funboost: bool = False`
    - `broker_kind: str = BrokerEnum.PERSISTQUEUE`
    - `concurrent_num: int = 5`
    - `qps: float = 0`
    - `max_retry_times: int = 3`
    - `request_timeout: float = 30`
    - `queue_name_prefix: str = 'boost_scrapy'`
    - `enable_filter: bool = True`
    - `log_level: int = logging.DEBUG`

**Public Methods (1):**
- `def run(self, spider_cls: Type[Spider], **kwargs)`
  - **Docstring:**
  `````
  运行爬虫
  
  Args:
      spider_cls: Spider 类（非实例）
      **kwargs: 传递给 Spider 构造函数的参数
  `````


---

`````python
# coding=utf-8
"""
boost_scrapy.engine - 核心引擎

解析 Spider 的 yield 生成器，调度 funboost 任务。
这是 boost_scrapy 框架的核心，负责协调请求、响应、回调和入库。
"""
import traceback
import time
import types
import requests
import logging
import hashlib
from typing import Type, List, Generator, Optional, Callable, Any
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
import json

from funboost import boost, BoosterParams, BrokerEnum, ctrl_c_recv, TaskOptions

from boost_scrapy.request import Request
from boost_scrapy.response import Response
from boost_scrapy.item import Item
from boost_scrapy.spider import Spider
from boost_scrapy.pipeline import Pipeline, ConsolePipeline
from boost_scrapy.middleware import Middleware
from boost_scrapy.log import logger




class Engine:
    """
    核心引擎 - 解析 Spider 的 yield 生成器，调度 funboost 任务
    
    工作流程:
    1. 实例化 Spider
    2. 初始化 Pipeline 列表
    3. 执行 spider.start_requests() 获取初始 Request
    4. 使用 boost_spider.RequestClient 发送请求
    5. 调用 Request.callback 处理响应
    6. 解析 callback 返回的生成器:
       - yield Request -> 递归处理新请求
       - yield Item -> 流经 Pipeline 入库
    7. 通过 funboost 队列实现分布式调度（可选）
    
    使用示例:
        engine = Engine()
        engine.run(MySpider)
    """
    
    def __init__(
        self,
        pipelines: Optional[List[Pipeline]] = None,
        middlewares: Optional[List[Middleware]] = None,
        use_funboost: bool = False,
        broker_kind: str = BrokerEnum.PERSISTQUEUE,
        concurrent_num: int = 5,
        qps: float = 0,
        max_retry_times: int = 3,
        request_timeout: float = 30,
        queue_name_prefix: str = "boost_scrapy",
        enable_filter: bool = True,
        log_level: int = logging.DEBUG,
    ):
        """
        初始化引擎
        
        Args:
            pipelines: Pipeline 实例列表（如果为 None，默认使用 ConsolePipeline）
            middlewares: Middleware 中间件列表（如 UserAgentMiddleware）
            use_funboost: 是否使用 funboost 分布式调度
            broker_kind: 消息队列类型（use_funboost=True 时有效）
            concurrent_num: 并发数
            qps: QPS 限制（0 表示不限制）
            max_retry_times: 最大重试次数
            request_timeout: 请求超时秒数
            queue_name_prefix: funboost 队列名称前缀
            enable_filter: 是否启用请求去重
            log_level: 日志级别
        """
        self.pipelines = pipelines if pipelines is not None else [ConsolePipeline()]
        self.middlewares = middlewares or []
        self.use_funboost = use_funboost
        self.broker_kind = broker_kind
        self.concurrent_num = concurrent_num
        self.qps = qps
        self.max_retry_times = max_retry_times
        self.request_timeout = request_timeout
        self.queue_name_prefix = queue_name_prefix
        self.enable_filter = enable_filter
        logger.setLevel(log_level)


        
        # HTTP 客户端 (requests.Session)
        self._session: Optional[requests.Session] = None
        
        # 当前爬虫实例
        self._spider: Optional[Spider] = None
        
        # funboost 消费函数（use_funboost=True 时使用）
        self._request_handler = None
    
    def run(self, spider_cls: Type[Spider], **kwargs):
        """
        运行爬虫
        
        Args:
            spider_cls: Spider 类（非实例）
            **kwargs: 传递给 Spider 构造函数的参数
        """
        # 1. 实例化 Spider
        self._spider = spider_cls.from_crawler(**kwargs)
        logger.info(f"启动爬虫: {self._spider}")
        
        # 2. 合并配置
        settings = {
            'concurrent_num': self.concurrent_num,
            'qps': self.qps,
            'max_retry_times': self.max_retry_times,
        }
        settings.update(self._spider.custom_settings)
        self.concurrent_num = settings.get('concurrent_num', self.concurrent_num)
        self.qps = settings.get('qps', self.qps)
        self.max_retry_times = settings.get('max_retry_times', self.max_retry_times)
        
        # 3. 初始化 Pipeline
        spider_pipelines = []
        for pipeline_cls in self._spider.pipelines:
            if isinstance(pipeline_cls, type):
                spider_pipelines.append(pipeline_cls())
            else:
                spider_pipelines.append(pipeline_cls)
        all_pipelines = self.pipelines + spider_pipelines
        
        for pipeline in all_pipelines:
            pipeline.open_spider(self._spider)
        
        # 4. 初始化 HTTP 客户端 (requests.Session)
        self._session = requests.Session()
        
        try:
            if self.use_funboost:
                # 使用 funboost 分布式调度
                self._run_with_funboost(all_pipelines)
            else:
                # 简单模式：同步执行
                self._run_simple(all_pipelines)
        finally:
            # 5. 关闭 HTTP Session
            if self._session:
                self._session.close()
                self._session = None
            
            # 6. 关闭 Pipeline
            for pipeline in all_pipelines:
                pipeline.close_spider(self._spider)
            
            # 7. 回调 spider.closed()
            self._spider.closed("finished")
            
            # 8. 打印结束日志
            logger.info(f"爬虫结束: {self._spider}")
    
    def _run_simple(self, pipelines: List[Pipeline]):
        """
        简单模式运行（同步执行，适合小规模爬取和调试）
        """
        logger.info("运行模式: 简单模式（同步执行）")
        
        # 执行 start_requests
        start_gen = self._spider.start_requests()
        # 简单模式下 push_func=None
        self._process_generator(start_gen, pipelines, push_func=None)
    
    def _run_with_funboost(self, pipelines: List[Pipeline]):
        """
        funboost 模式运行（分布式调度）
        """

        logger.info("运行模式: funboost 分布式调度")
        logger.info(f"broker_kind={self.broker_kind}, concurrent_num={self.concurrent_num}, qps={self.qps}")
        
        queue_name = f"{self.queue_name_prefix}_{self._spider.name}"
        
        # 创建 funboost 消费函数
        @boost(BoosterParams(
            queue_name=queue_name,
            broker_kind=self.broker_kind,
            concurrent_num=self.concurrent_num,
            qps=self.qps,
            max_retry_times=self.max_retry_times,
        ))
        def process_request(request_data: dict):
            """处理单个请求"""
            request = self._deserialize_request(request_data)
            self._process_single_request(request, pipelines, process_request)
        
        self._request_handler = process_request
        
        # 启动消费者
        process_request.consume()
        
        # 发布初始任务
        for request in self._spider.start_requests():
            request_data = self._serialize_request(request)
            
            task_options = None
            if self.enable_filter and not request.dont_filter:
                fingerprint = self._get_request_fingerprint(request)
                # logger.info(f"请求指纹: {fingerprint},request={request}")
                # print(f"请求指纹: {fingerprint},request={request}")
                task_options = TaskOptions(filter_str=fingerprint, do_task_filtering=True)
            
            process_request.publish({'request_data': request_data}, task_options=task_options)
        
        # 阻塞主线程

        logger.info("爬虫已启动，按 Ctrl+C 停止...")
        ctrl_c_recv()
    
    def _get_request_fingerprint(self, request: Request) -> str:
        """
        计算请求指纹（用于去重）
        
        逻辑升级：
        1. 规范化 URL 参数（排序）
        2. 包含 Request Body (data/json)
        3. 包含 Method
        
        Args:
            request: 请求对象
            
        Returns:
            请求指纹（MD5 哈希）
        """
        # 1. 规范化 URL (参数排序，合并 query 和 params)
        parsed = urlparse(request.url)
        query_items = []
        
        # 1.1 从原始 URL 中提取 query
        if parsed.query:
            query_items.extend(parse_qsl(parsed.query))
            
        # 1.2 从 kwargs['params'] 中提取
        req_params = request.kwargs.get('params')
        if req_params:
            if isinstance(req_params, dict):
                query_items.extend(req_params.items())
            elif isinstance(req_params, (list, tuple)):
                query_items.extend(req_params)
        
        # 1.3 排序并重组
        if query_items:
            # 排序确保顺序一致
            # 注意：将所有元素转为字符串再排序，防止类型不一致报错 (如 int 和 str)
            query_items.sort(key=lambda x: (str(x[0]), str(x[1])))
            normalized_query = urlencode(query_items)
        else:
            normalized_query = ""
            
        # 重组 URL
        normalized_url = urlunparse((
            parsed.scheme, parsed.netloc, parsed.path,
            parsed.params, normalized_query, parsed.fragment
        ))

        # 2. 收集 Body 数据 (json/data)
        body_str = ""
        
        # 处理 json 参数 (kwargs['json'])
        req_json = request.kwargs.get('json')
        if req_json:
            # JSON 键排序，确保 {a:1, b:2} 和 {b:2, a:1} 指纹一致
            body_str += json.dumps(req_json, sort_keys=True, separators=(',', ':'))
            
        # 处理 data 参数 (kwargs['data'])
        req_data = request.kwargs.get('data')
        if req_data:
            if isinstance(req_data, dict):
                # 字典类型 data，排序键
                # 注意：request data 为字典时通常是 form-data，顺序可能不敏感，排序更稳健
                sorted_data = dict(sorted(req_data.items()))
                body_str += str(sorted_data)
            else:
                # 字符串或 bytes，直接拼接
                body_str += str(req_data)

        # 3. 拼接指纹字符串
        # 格式: METHOD:URL:BODY
        fp_string = f"{request.method}:{normalized_url}:{body_str}"
        
        # print(f"原始指纹串: {fp_string}") # debug用
        return hashlib.md5(fp_string.encode('utf-8')).hexdigest()
    
    def _process_generator(self, gen: Generator, pipelines: List[Pipeline], push_func: Callable = None):
        """
        处理生成器：递归处理 yield 的 Request 和 Item
        """
        if gen is None:
            return
        
        # 兼容 list/tuple 返回值 (Scrapy 允许 return [Request(...), Item(...)])
        if isinstance(gen, (list, tuple)):
            for item in gen:
                self._process_yield_item(item, pipelines, push_func)
            return
        
        if not isinstance(gen, types.GeneratorType):
            # 如果不是生成器也不是列表，可能是单个 Request 或 Item
            self._process_yield_item(gen, pipelines, push_func)
            return
        
        for item in gen:
            self._process_yield_item(item, pipelines, push_func)
    
    def _process_yield_item(self, item: Any, pipelines: List[Pipeline], push_func: Callable = None):
        """
        处理单个 yield 产出的对象
        
        Args:
            item: yield 产出的对象
            pipelines: Pipeline 列表
            push_func: funboost 模式下用于推送新任务的函数
        """
        if isinstance(item, Request):
            # yield Request -> 发送请求并处理响应
            if push_func:
                # funboost 模式：推送到队列
                request_data = self._serialize_request(item)
                
                task_options = None
                if self.enable_filter and not item.dont_filter:
                    fingerprint = self._get_request_fingerprint(item)
                    task_options = TaskOptions(filter_str=fingerprint, do_task_filtering=True)
                
                push_func.publish(msg={'request_data': request_data}, task_options=task_options)
            else:
                # 简单模式：直接处理 (无去重)
                self._process_single_request(item, pipelines)
                
        elif isinstance(item, Item):
            # yield Item -> 流经 Pipeline
            self._process_item(item, pipelines)
            
        else:
             logger.warning(f"  ⚠️ [Engine] 忽略非 Item 对象: {type(item)} (请继承 boost_scrapy.Item)")
    
    def _process_single_request(
        self, 
        request: Request, 
        pipelines: List[Pipeline],
        push_func: Callable = None
    ):
        """
        处理单个请求：发送 HTTP 请求，调用 callback，处理返回的生成器
        
        Args:
            request: 请求对象
            pipelines: Pipeline 列表
            push_func: funboost 模式下用于推送新任务的函数
        """
        response = None
        
        try:
            # 1. 执行中间件的 process_request（请求发送前）
            for middleware in self.middlewares:
                result = middleware.process_request(request, self._spider)
                if result is not None:
                    if isinstance(result, Request):
                        request = result
                    elif isinstance(result, Response):
                        response = result
                        break
            
            if response is None:
                # 2. 发送 HTTP 请求
                logger.debug(f"发送请求: {request.method} {request.url}")
                
                # 优先使用 request.kwargs 中的 timeout，否则使用 engine 默认配置
                request_timeout = request.kwargs.pop('timeout', self.request_timeout)
                
                
                start_time = time.time()
                raw_resp = self._session.request(
                    method=request.method,
                    url=request.url,
                    headers=request.headers or None,
                    cookies=request.cookies or None,
                    timeout=request_timeout,
                    **request.kwargs
                )
                time_cost = time.time() - start_time
                
                # 3. 封装 Response
                response = Response(raw_resp, meta=request.meta, request=request)
                logger.debug(f"收到响应: {request.method} {request.url} 状态码:{response.status_code} "
                                  f"耗时:{time_cost:.3f}s 长度:{len(response.content)} 内容预览:{response.text[:200].replace(chr(10), '')}")
            
            # 4. 执行中间件的 process_response（响应返回后）
            for middleware in reversed(self.middlewares):
                response = middleware.process_response(request, response, self._spider)
            
            # 5. 调用 callback
            callback = request.callback or self._spider.parse
            result = callback(response)
            
            # 6. 处理回调返回值
            if isinstance(result, types.GeneratorType):
                for item in result:
                    self._process_yield_item(item, pipelines, push_func)
            elif result is not None:
                self._process_yield_item(result, pipelines, push_func)
                
        except Exception as e:
            # 7. 执行中间件的 process_exception
            for middleware in self.middlewares:
                result = middleware.process_exception(request, e, self._spider)
                if result is not None:
                    if isinstance(result, Request):
                        self._process_single_request(result, pipelines, push_func)
                        return
                    elif isinstance(result, Response):
                        callback = request.callback or self._spider.parse
                        gen_result = callback(result)
                        # 修复: 异常重试产生的任务必须走 push_func 入队
                        self._process_generator(gen_result, pipelines, push_func)
                        return
            
            logger.error(f"请求失败: {request.url}, 错误: {e}")
            
            logger.debug(traceback.format_exc())
    
    def _process_item(self, item: Item, pipelines: List[Pipeline]):
        """
        处理 Item：流经所有 Pipeline
        """
        for pipeline in pipelines:
            try:
                item = pipeline.process_item(item, self._spider)
                if item is None:
                    break
            except Exception as e:
                logger.error(f"Pipeline 处理失败: {e}")
                logger.debug(traceback.format_exc())
    
    def _serialize_request(self, request: Request) -> dict:
        """
        序列化 Request 对象（用于 funboost 消息传递）
        """
        callback_name = None
        if request.callback:
            callback_name = request.callback.__name__
        
        return {
            'url': request.url,
            'method': request.method,
            'headers': request.headers,
            'cookies': request.cookies,
            'meta': request.meta,
            'dont_filter': request.dont_filter,
            'priority': request.priority,
            'callback_name': callback_name,
            'kwargs': request.kwargs,
        }
    
    def _deserialize_request(self, data: dict) -> Request:
        """
        反序列化 Request 对象
        """
        callback = None
        callback_name = data.get('callback_name')
        if callback_name and self._spider:
            callback = getattr(self._spider, callback_name, None)
        
        return Request(
            url=data['url'],
            callback=callback,
            method=data.get('method', 'GET'),
            headers=data.get('headers'),
            cookies=data.get('cookies'),
            meta=data.get('meta'),
            dont_filter=data.get('dont_filter', False),
            priority=data.get('priority', 0),
            **data.get('kwargs', {})
        )

`````

--- **end of file: boost_scrapy/engine.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/item.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/item.py`

#### 📝 Module Docstring

`````
boost_scrapy.item - Item 数据项

类似 Scrapy 的 Item，用于定义爬取的数据结构。
`````

#### 📦 Imports

- `from sqlmodel import SQLModel`
- `import json`
- `import json`

#### 🏛️ Classes (1)

##### 📌 `class Item(SQLModel)`
*Line: 11*

**Docstring:**
`````
数据项基类 - 继承自 SQLModel

终端用户定义的 Item 应继承此类，例如:
    class NewsItem(Item, table=True):
        ...

提供了方便的序列化方法:
- to_dict()
- to_json()
- to_pretty_json()
`````

**Public Methods (4):**
- `def to_dict(self) -> dict`
  - *转换为字典 (兼容 Pydantic v1/v2)*
- `def to_json(self) -> str`
  - *转换为 JSON 字符串*
- `def to_pretty_json(self) -> str`
  - *转换为格式化的 JSON 字符串*
- `def get(self, key, default = None)`
  - *兼容 dict.get()*


---

`````python
# coding=utf-8
"""
boost_scrapy.item - Item 数据项

类似 Scrapy 的 Item，用于定义爬取的数据结构。
"""

from sqlmodel import SQLModel


class Item(SQLModel):
    """
    数据项基类 - 继承自 SQLModel
    
    终端用户定义的 Item 应继承此类，例如:
        class NewsItem(Item, table=True):
            ...
    
    提供了方便的序列化方法:
    - to_dict()
    - to_json()
    - to_pretty_json()
    """
    
    def to_dict(self) -> dict:
        """转换为字典 (兼容 Pydantic v1/v2)"""
        # Pydantic v2 / SQLModel forward compatible
        if hasattr(self, 'model_dump'):
            return self.model_dump()
        # Pydantic v1 / Old SQLModel
        return self.dict()
    
    def to_json(self) -> str:
        """转换为 JSON 字符串"""
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False)
    
    def to_pretty_json(self) -> str:
        """转换为格式化的 JSON 字符串"""
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)
    
    def __getitem__(self, key):
        """兼容字典式访问 item['key']"""
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        """兼容字典式赋值 item['key'] = value"""
        setattr(self, key, value)
    
    def get(self, key, default=None):
        """兼容 dict.get()"""
        return getattr(self, key, default)

`````

--- **end of file: boost_scrapy/item.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/log.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/log.py`

#### 📦 Imports

- `import nb_log`


---

`````python


import nb_log

logger_name = 'boost_scrapy'
logger = nb_log.get_logger(logger_name)
`````

--- **end of file: boost_scrapy/log.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/middleware.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/middleware.py`

#### 📝 Module Docstring

`````
boost_scrapy.middleware - 中间件

类似 Scrapy 的 Downloader Middleware，可以在请求发送前/响应返回后进行处理。
`````

#### 📦 Imports

- `import random`
- `from typing import Optional`
- `from typing import TYPE_CHECKING`
- `import random`
- `from typing import Optional`
- `from typing import TYPE_CHECKING`
- `from boost_scrapy.log import logger`
- `from boost_scrapy.request import Request`
- `from boost_scrapy.response import Response`
- `from boost_scrapy.spider import Spider`

#### 🏛️ Classes (5)

##### 📌 `class Middleware`
*Line: 36*

**Docstring:**
`````
中间件基类 - 类似 Scrapy Downloader Middleware

使用示例:
    class MyMiddleware(Middleware):
        def process_request(self, request, spider):
            request.headers['X-Custom'] = 'value'
            return None  # 继续处理
        
        def process_response(self, request, response, spider):
            return response  # 返回响应
`````

**Public Methods (3):**
- `def process_request(self, request: 'Request', spider: 'Spider') -> Optional['Request']`
  - **Docstring:**
  `````
  处理请求（请求发送前调用）
  
  Args:
      request: 请求对象
      spider: 爬虫实例
  
  Returns:
      - None: 继续处理，将请求传递给下一个中间件
      - Request: 返回新的 Request 对象
      - Response: 直接返回响应，不发送请求（用于缓存等场景）
  `````
- `def process_response(self, request: 'Request', response: 'Response', spider: 'Spider') -> 'Response'`
  - **Docstring:**
  `````
  处理响应（响应返回后调用）
  
  Args:
      request: 请求对象
      response: 响应对象
      spider: 爬虫实例
  
  Returns:
      Response 对象
  `````
- `def process_exception(self, request: 'Request', exception: Exception, spider: 'Spider')`
  - **Docstring:**
  `````
  处理异常
  
  Args:
      request: 请求对象
      exception: 异常对象
      spider: 爬虫实例
  
  Returns:
      - None: 继续抛出异常
      - Response: 返回响应
      - Request: 重新发送请求
  `````

##### 📌 `class UserAgentMiddleware(Middleware)`
*Line: 96*

**Docstring:**
`````
随机 User-Agent 中间件

每次请求自动随机切换 User-Agent。

使用示例:
    engine = Engine(middlewares=[UserAgentMiddleware()])
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, user_agents: list = None)`
  - **Docstring:**
  `````
  Args:
      user_agents: 自定义 UA 列表，默认使用内置列表
  `````
  - **Parameters:**
    - `self`
    - `user_agents: list = None`

**Public Methods (1):**
- `def process_request(self, request: 'Request', spider: 'Spider')`
  - *为每个请求设置随机 User-Agent*

##### 📌 `class HeadersMiddleware(Middleware)`
*Line: 121*

**Docstring:**
`````
自定义请求头中间件

使用示例:
    engine = Engine(middlewares=[
        HeadersMiddleware({
            'Referer': 'https://www.google.com',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        })
    ])
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, headers: dict)`
  - **Docstring:**
  `````
  Args:
      headers: 要添加的请求头字典
  `````
  - **Parameters:**
    - `self`
    - `headers: dict`

**Public Methods (1):**
- `def process_request(self, request: 'Request', spider: 'Spider')`
  - *为每个请求添加自定义请求头*

##### 📌 `class RetryMiddleware(Middleware)`
*Line: 149*

**Docstring:**
`````
重试中间件

请求失败时自动重试。
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, max_retries: int = 3)`
  - **Parameters:**
    - `self`
    - `max_retries: int = 3`

**Public Methods (1):**
- `def process_exception(self, request: 'Request', exception: Exception, spider: 'Spider')`
  - *请求异常时重试*

##### 📌 `class ProxyMiddleware(Middleware)`
*Line: 170*

**Docstring:**
`````
代理中间件 - 自动切换代理 IP

使用示例:
    # 单个代理
    engine = Engine(middlewares=[
        ProxyMiddleware('http://127.0.0.1:8080')
    ])
    
    # 代理池（自动轮换）
    engine = Engine(middlewares=[
        ProxyMiddleware([
            'http://proxy1:8080',
            'http://proxy2:8080',
            'http://user:pass@proxy3:8080',  # 支持认证
        ])
    ])
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, proxies)`
  - **Docstring:**
  `````
  Args:
      proxies: 代理配置，支持以下格式：
          - str: 单个代理，如 'http://127.0.0.1:8080'
          - list: 代理池列表，自动轮换
          - dict: requests 格式，如 {'http': 'http://proxy:8080', 'https': 'http://proxy:8080'}
  `````
  - **Parameters:**
    - `self`
    - `proxies`

**Public Methods (1):**
- `def process_request(self, request: 'Request', spider: 'Spider')`
  - *为每个请求设置代理*


---

`````python
# coding=utf-8
"""
boost_scrapy.middleware - 中间件

类似 Scrapy 的 Downloader Middleware，可以在请求发送前/响应返回后进行处理。
"""

import random
from typing import Optional, TYPE_CHECKING
import random
from typing import Optional, TYPE_CHECKING
from boost_scrapy.log import logger

if TYPE_CHECKING:
    from boost_scrapy.request import Request
    from boost_scrapy.response import Response
    from boost_scrapy.spider import Spider


# 预定义的 User-Agent 列表
USER_AGENTS = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # Firefox
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
    # Safari
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    # Edge
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
]


class Middleware:
    """
    中间件基类 - 类似 Scrapy Downloader Middleware
    
    使用示例:
        class MyMiddleware(Middleware):
            def process_request(self, request, spider):
                request.headers['X-Custom'] = 'value'
                return None  # 继续处理
            
            def process_response(self, request, response, spider):
                return response  # 返回响应
    """
    
    def process_request(self, request: 'Request', spider: 'Spider') -> Optional['Request']:
        """
        处理请求（请求发送前调用）
        
        Args:
            request: 请求对象
            spider: 爬虫实例
        
        Returns:
            - None: 继续处理，将请求传递给下一个中间件
            - Request: 返回新的 Request 对象
            - Response: 直接返回响应，不发送请求（用于缓存等场景）
        """
        return None
    
    def process_response(self, request: 'Request', response: 'Response', spider: 'Spider') -> 'Response':
        """
        处理响应（响应返回后调用）
        
        Args:
            request: 请求对象
            response: 响应对象
            spider: 爬虫实例
        
        Returns:
            Response 对象
        """
        return response
    
    def process_exception(self, request: 'Request', exception: Exception, spider: 'Spider'):
        """
        处理异常
        
        Args:
            request: 请求对象
            exception: 异常对象
            spider: 爬虫实例
        
        Returns:
            - None: 继续抛出异常
            - Response: 返回响应
            - Request: 重新发送请求
        """
        return None


class UserAgentMiddleware(Middleware):
    """
    随机 User-Agent 中间件
    
    每次请求自动随机切换 User-Agent。
    
    使用示例:
        engine = Engine(middlewares=[UserAgentMiddleware()])
    """
    
    def __init__(self, user_agents: list = None):
        """
        Args:
            user_agents: 自定义 UA 列表，默认使用内置列表
        """
        self.user_agents = user_agents or USER_AGENTS
    
    def process_request(self, request: 'Request', spider: 'Spider'):
        """为每个请求设置随机 User-Agent"""
        ua = random.choice(self.user_agents)
        request.headers['User-Agent'] = ua
        logger.debug(f"  🔄 [UserAgentMiddleware] UA: {ua[:50]}...")
        return None


class HeadersMiddleware(Middleware):
    """
    自定义请求头中间件
    
    使用示例:
        engine = Engine(middlewares=[
            HeadersMiddleware({
                'Referer': 'https://www.google.com',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            })
        ])
    """
    
    def __init__(self, headers: dict):
        """
        Args:
            headers: 要添加的请求头字典
        """
        self.headers = headers
    
    def process_request(self, request: 'Request', spider: 'Spider'):
        """为每个请求添加自定义请求头"""
        for key, value in self.headers.items():
            if key not in request.headers:
                request.headers[key] = value
        return None


class RetryMiddleware(Middleware):
    """
    重试中间件
    
    请求失败时自动重试。
    """
    
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
    
    def process_exception(self, request: 'Request', exception: Exception, spider: 'Spider'):
        """请求异常时重试"""
        retry_count = request.meta.get('_retry_count', 0)
        if retry_count < self.max_retries:
            logger.warning(f"  🔁 [RetryMiddleware] 重试 {retry_count + 1}/{self.max_retries}: {request.url}")
            new_request = request.copy()
            new_request.meta['_retry_count'] = retry_count + 1
            return new_request
        return None


class ProxyMiddleware(Middleware):
    """
    代理中间件 - 自动切换代理 IP
    
    使用示例:
        # 单个代理
        engine = Engine(middlewares=[
            ProxyMiddleware('http://127.0.0.1:8080')
        ])
        
        # 代理池（自动轮换）
        engine = Engine(middlewares=[
            ProxyMiddleware([
                'http://proxy1:8080',
                'http://proxy2:8080',
                'http://user:pass@proxy3:8080',  # 支持认证
            ])
        ])
    """
    
    def __init__(self, proxies):
        """
        Args:
            proxies: 代理配置，支持以下格式：
                - str: 单个代理，如 'http://127.0.0.1:8080'
                - list: 代理池列表，自动轮换
                - dict: requests 格式，如 {'http': 'http://proxy:8080', 'https': 'http://proxy:8080'}
        """
        if isinstance(proxies, str):
            self.proxy_list = [proxies]
        elif isinstance(proxies, list):
            self.proxy_list = proxies
        elif isinstance(proxies, dict):
            self.proxy_list = None
            self.proxy_dict = proxies
        else:
            raise ValueError("proxies must be str, list, or dict")
        
        self.index = 0
    
    def _get_proxy(self) -> dict:
        """获取代理配置（轮换）"""
        if hasattr(self, 'proxy_dict'):
            return self.proxy_dict
        
        if not self.proxy_list:
            return {}
        
        proxy = self.proxy_list[self.index % len(self.proxy_list)]
        self.index += 1
        return {'http': proxy, 'https': proxy}
    
    def process_request(self, request: 'Request', spider: 'Spider'):
        """为每个请求设置代理"""
        proxy = self._get_proxy()
        if proxy:
            request.kwargs['proxies'] = proxy
            proxy_str = list(proxy.values())[0] if proxy else 'None'
            logger.debug(f"  🌐 [ProxyMiddleware] Proxy: {proxy_str}")
        return None


`````

--- **end of file: boost_scrapy/middleware.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/pipeline.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/pipeline.py`

#### 📝 Module Docstring

`````
boost_scrapy.pipeline - Pipeline 数据入库管道

类似 Scrapy 的 Pipeline，用于处理 Item 数据入库。
`````

#### 📦 Imports

- `from typing import TYPE_CHECKING`
- `from boost_scrapy.log import logger`
- `from boost_scrapy.item import Item`
- `from boost_scrapy.item import Item`
- `from boost_scrapy.spider import Spider`
- `from boost_scrapy.item import Item`
- `from sqlmodel import create_engine`
- `from sqlmodel import Session`
- `from sqlmodel import create_engine`

#### 🏛️ Classes (3)

##### 📌 `class Pipeline`
*Line: 18*

**Docstring:**
`````
数据入库管道基类 - 类似 Scrapy Pipeline

使用示例:
    class SQLitePipeline(Pipeline):
        def open_spider(self, spider):
            self.conn = sqlite3.connect('data.db')
        
        def process_item(self, item, spider):
            # 入库逻辑
            return item
        
        def close_spider(self, spider):
            self.conn.close()
`````

**Public Methods (3):**
- `def open_spider(self, spider: 'Spider')`
  - **Docstring:**
  `````
  爬虫启动时调用
  
  可在此处初始化数据库连接等资源。
  
  Args:
      spider: 爬虫实例
  `````
- `def process_item(self, item: 'Item', spider: 'Spider') -> 'Item'`
  - **Docstring:**
  `````
  处理每个 Item
  
  可在此处进行数据清洗、入库等操作。
  
  Args:
      item: 数据项
      spider: 爬虫实例
  
  Returns:
      处理后的 Item（可返回 None 表示丢弃该 Item）
  `````
- `def close_spider(self, spider: 'Spider')`
  - **Docstring:**
  `````
  爬虫关闭时调用
  
  可在此处释放资源。
  
  Args:
      spider: 爬虫实例
  `````

##### 📌 `class ConsolePipeline(Pipeline)`
*Line: 77*

**Docstring:**
`````
打印 Pipeline - 仅打印 Item 用于调试
`````

**Public Methods (1):**
- `def process_item(self, item: 'Item', spider: 'Spider') -> 'Item'`

##### 📌 `class SQLModelPipeline(Pipeline)`
*Line: 89*

**Docstring:**
`````
SQLModel Pipeline - 自动保存 SQLModel Item 到数据库

1. 自动根据 Item 定义创建表
2. 自动保存数据 (Session.add / commit) ，不需要学scrapy那样，在pipeline手写insert语句。
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, db_url: str)`
  - **Docstring:**
  `````
  Args:
      db_url: 数据库连接字符串 (必填)
  `````
  - **Parameters:**
    - `self`
    - `db_url: str`

**Public Methods (3):**
- `def open_spider(self, spider)`
  - *爬虫启动时创建数据库连接和表*
- `def process_item(self, item, spider)`
  - *处理 Item，保存到数据库*
- `def close_spider(self, spider)`
  - *爬虫关闭时操作*


---

`````python
# coding=utf-8
"""
boost_scrapy.pipeline - Pipeline 数据入库管道

类似 Scrapy 的 Pipeline，用于处理 Item 数据入库。
"""

from typing import TYPE_CHECKING
from boost_scrapy.log import logger
from boost_scrapy.item import Item


if TYPE_CHECKING:
    from boost_scrapy.item import Item
    from boost_scrapy.spider import Spider


class Pipeline:
    """
    数据入库管道基类 - 类似 Scrapy Pipeline
    
    使用示例:
        class SQLitePipeline(Pipeline):
            def open_spider(self, spider):
                self.conn = sqlite3.connect('data.db')
            
            def process_item(self, item, spider):
                # 入库逻辑
                return item
            
            def close_spider(self, spider):
                self.conn.close()
    """
    
    def open_spider(self, spider: 'Spider'):
        """
        爬虫启动时调用
        
        可在此处初始化数据库连接等资源。
        
        Args:
            spider: 爬虫实例
        """
        pass
    
    def process_item(self, item: 'Item', spider: 'Spider') -> 'Item':
        """
        处理每个 Item
        
        可在此处进行数据清洗、入库等操作。
        
        Args:
            item: 数据项
            spider: 爬虫实例
        
        Returns:
            处理后的 Item（可返回 None 表示丢弃该 Item）
        """
        return item
    

        
        return item
    
    def close_spider(self, spider: 'Spider'):
        """
        爬虫关闭时调用
        
        可在此处释放资源。
        
        Args:
            spider: 爬虫实例
        """
        pass


class ConsolePipeline(Pipeline):
    """
    打印 Pipeline - 仅打印 Item 用于调试
    """
    
    def process_item(self, item: 'Item', spider: 'Spider') -> 'Item':
        # 此时 item 已经是 boost_scrapy.Item (Engine 已处理)
        # 直接使用 Item 的方法获取漂亮打印的 JSON
        logger.info(f"  👀 [Console] {type(item).__name__}:\n{item.to_pretty_json()}")
        return item


class SQLModelPipeline(Pipeline):
    """
    SQLModel Pipeline - 自动保存 SQLModel Item 到数据库
    
    1. 自动根据 Item 定义创建表
    2. 自动保存数据 (Session.add / commit) ，不需要学scrapy那样，在pipeline手写insert语句。
    """
    
    def __init__(self, db_url: str):
        """
        Args:
            db_url: 数据库连接字符串 (必填)
        """
        try:
            from sqlmodel import create_engine
        except ImportError:
            raise ImportError("SQLModelPipeline requires 'sqlmodel' to be installed.")
        
        self.db_url = db_url
        self.engine = None
        self.item_count = {} # 统计每种 Item 的数量
    
    def open_spider(self, spider):
        """爬虫启动时创建数据库连接和表"""
        from boost_scrapy.item import Item
        from sqlmodel import create_engine
        
        logger.info(f"[SQLModelPipeline] 连接数据库: {self.db_url}")
        connect_args = {"check_same_thread": False} if "sqlite" in self.db_url else {}
        self.engine = create_engine(self.db_url, connect_args=connect_args)
        
        # 自动创建表
        logger.info("[SQLModelPipeline] 正在检查并创建数据库表...")
        Item.metadata.create_all(self.engine)
        logger.info("[SQLModelPipeline] 数据库表已就绪")
    
    def process_item(self, item, spider):
        """处理 Item，保存到数据库"""
        from sqlmodel import Session
        
        # 强制 Item 为 boost_scrapy.Item
        
        if not isinstance(item, Item):
             logger.warning(f"  ⚠️ [SQLModelPipeline] 忽略非 Item 对象: {type(item)}")
             return item

        with Session(self.engine) as session:
            item_json = item.to_json()
            session.add(item)
            session.commit()
            
            # 统计数量
            name = type(item).__name__
            self.item_count[name] = self.item_count.get(name, 0) + 1
            
            logger.info(f"  💾 [SQLModel] 保存 {name} {item_json}")
        
        return item
    
    def close_spider(self, spider):
        """爬虫关闭时操作"""
        logger.info("-" * 60)
        logger.info(f"[SQLModelPipeline] 数据保存统计")
        for name, count in self.item_count.items():
            logger.info(f"  {name}: {count} 条")
        logger.info(f"  数据库: {self.db_url}")
        logger.info("-" * 60)

`````

--- **end of file: boost_scrapy/pipeline.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/request.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/request.py`

#### 📝 Module Docstring

`````
boost_scrapy.request - Request 请求封装

类似 Scrapy 的 Request 对象，封装 URL、callback、method、headers、meta 等属性。
`````

#### 📦 Imports

- `from typing import Callable`
- `from typing import Dict`
- `from typing import Any`
- `from typing import Optional`

#### 🏛️ Classes (1)

##### 📌 `class Request`
*Line: 11*

**Docstring:**
`````
请求对象 - 类似 Scrapy 的 Request

使用示例:
    yield Request(
        url="http://example.com",
        callback=self.parse,
        method='GET',
        headers={'User-Agent': 'xxx'},
        meta={'page': 1},
    )
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, url: str, callback: Callable = None, method: str = 'GET', headers: Optional[Dict[str, str]] = None, cookies: Optional[Dict[str, str]] = None, meta: Optional[Dict[str, Any]] = None, dont_filter: bool = False, priority: int = 0, **kwargs)`
  - **Docstring:**
  `````
  初始化 Request 对象
  
  Args:
      url: 请求 URL
      callback: 响应回调函数
      method: 请求方法 (GET, POST, PUT, DELETE 等)
      headers: 请求头
      cookies: Cookie
      meta: 传递给回调函数的上下文数据
      dont_filter: 是否跳过去重过滤
      priority: 优先级（数值越大优先级越高）
      **kwargs: 额外请求参数（如 data, json, params, timeout）
  `````
  - **Parameters:**
    - `self`
    - `url: str`
    - `callback: Callable = None`
    - `method: str = 'GET'`
    - `headers: Optional[Dict[str, str]] = None`
    - `cookies: Optional[Dict[str, str]] = None`
    - `meta: Optional[Dict[str, Any]] = None`
    - `dont_filter: bool = False`
    - `priority: int = 0`
    - `**kwargs`

**Public Methods (2):**
- `def copy(self) -> 'Request'`
  - *创建请求的副本*
- `def replace(self, **kwargs) -> 'Request'`
  - *创建请求的副本并替换指定属性*


---

`````python
# coding=utf-8
"""
boost_scrapy.request - Request 请求封装

类似 Scrapy 的 Request 对象，封装 URL、callback、method、headers、meta 等属性。
"""

from typing import Callable, Dict, Any, Optional


class Request:
    """
    请求对象 - 类似 Scrapy 的 Request
    
    使用示例:
        yield Request(
            url="http://example.com",
            callback=self.parse,
            method='GET',
            headers={'User-Agent': 'xxx'},
            meta={'page': 1},
        )
    """
    
    def __init__(
        self,
        url: str,
        callback: Callable = None,
        method: str = 'GET',
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        meta: Optional[Dict[str, Any]] = None,
        dont_filter: bool = False,
        priority: int = 0,
        **kwargs  # 额外参数: data, json, params, timeout 等
    ):
        """
        初始化 Request 对象
        
        Args:
            url: 请求 URL
            callback: 响应回调函数
            method: 请求方法 (GET, POST, PUT, DELETE 等)
            headers: 请求头
            cookies: Cookie
            meta: 传递给回调函数的上下文数据
            dont_filter: 是否跳过去重过滤
            priority: 优先级（数值越大优先级越高）
            **kwargs: 额外请求参数（如 data, json, params, timeout）
        """
        self.url = url
        self.callback = callback
        self.method = method.upper()
        self.headers = headers or {}
        self.cookies = cookies or {}
        self.meta = meta or {}
        self.dont_filter = dont_filter
        self.priority = priority
        self.kwargs = kwargs  # data, json, params, timeout 等
        
        # 内部属性：关联的 Spider 实例（由 Engine 设置）
        self._spider = None
    
    def __repr__(self):
        return f"<Request [{self.method}] {self.url}>"
    
    def copy(self) -> 'Request':
        """创建请求的副本"""
        return Request(
            url=self.url,
            callback=self.callback,
            method=self.method,
            headers=self.headers.copy(),
            cookies=self.cookies.copy(),
            meta=self.meta.copy(),
            dont_filter=self.dont_filter,
            priority=self.priority,
            **self.kwargs
        )
    
    def replace(self, **kwargs) -> 'Request':
        """创建请求的副本并替换指定属性"""
        new_request = self.copy()
        for key, value in kwargs.items():
            if hasattr(new_request, key):
                setattr(new_request, key, value)
            else:
                new_request.kwargs[key] = value
        return new_request

`````

--- **end of file: boost_scrapy/request.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/response.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/response.py`

#### 📝 Module Docstring

`````
boost_scrapy.response - Response 响应封装

独立实现，不依赖 boost_spider，提供 xpath/css/json 解析功能。
`````

#### 📦 Imports

- `import re`
- `from typing import Dict`
- `from typing import Any`
- `from typing import Optional`
- `from typing import TYPE_CHECKING`
- `import requests`
- `from parsel import Selector`
- `from boost_scrapy.request import Request`

#### 🏛️ Classes (1)

##### 📌 `class Response`
*Line: 18*

**Docstring:**
`````
响应对象 - 独立实现，不依赖 boost_spider

提供以下功能：
- xpath(query): XPath 选择器
- css(query): CSS 选择器
- resp_dict: 自动解析 JSON
- re_search(pattern): 正则搜索
- re_findall(pattern): 正则查找全部
- selector: parsel.Selector 对象
- meta: 从 Request 传递的上下文数据
- request: 关联的 Request 对象
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self, resp: requests.Response, meta: Optional[Dict[str, Any]] = None, request: Optional['Request'] = None)`
  - **Docstring:**
  `````
  初始化 Response 对象
  
  Args:
      resp: requests.Response 原始响应对象
      meta: 从 Request 传递的上下文数据
      request: 关联的 Request 对象
  `````
  - **Parameters:**
    - `self`
    - `resp: requests.Response`
    - `meta: Optional[Dict[str, Any]] = None`
    - `request: Optional['Request'] = None`

**Public Methods (5):**
- `def xpath(self, query: str)`
  - **Docstring:**
  `````
  XPath 选择器
  
  Args:
      query: XPath 表达式
  
  Returns:
      SelectorList 对象
  `````
- `def css(self, query: str)`
  - **Docstring:**
  `````
  CSS 选择器
  
  Args:
      query: CSS 选择器表达式
  
  Returns:
      SelectorList 对象
  `````
- `def re_search(self, pattern: str, flags: int = 0)`
  - **Docstring:**
  `````
  正则搜索（返回第一个匹配）
  
  Args:
      pattern: 正则表达式
      flags: 正则标志
  
  Returns:
      Match 对象或 None
  `````
- `def re_findall(self, pattern: str, flags: int = 0)`
  - **Docstring:**
  `````
  正则查找全部
  
  Args:
      pattern: 正则表达式
      flags: 正则标志
  
  Returns:
      匹配列表
  `````
- `def json(self) -> Any`
  - *解析 JSON 响应（兼容 requests.Response.json()）*

**Properties (5):**
- `@property text -> str`
- `@property selector -> Selector`
- `@property resp_dict -> Any`
- `@property meta -> Dict[str, Any]`
- `@property request -> Optional['Request']`

**Class Variables (1):**
- `_re_pattern_cache = {}`


---

`````python
# coding=utf-8
"""
boost_scrapy.response - Response 响应封装

独立实现，不依赖 boost_spider，提供 xpath/css/json 解析功能。
"""

import re
from typing import Dict, Any, Optional, TYPE_CHECKING

import requests
from parsel import Selector

if TYPE_CHECKING:
    from boost_scrapy.request import Request


class Response:
    """
    响应对象 - 独立实现，不依赖 boost_spider
    
    提供以下功能：
    - xpath(query): XPath 选择器
    - css(query): CSS 选择器
    - resp_dict: 自动解析 JSON
    - re_search(pattern): 正则搜索
    - re_findall(pattern): 正则查找全部
    - selector: parsel.Selector 对象
    - meta: 从 Request 传递的上下文数据
    - request: 关联的 Request 对象
    """
    
    # 类级别的正则缓存，所有 Response 实例共享
    _re_pattern_cache = {}
    
    def __init__(
        self, 
        resp: requests.Response, 
        meta: Optional[Dict[str, Any]] = None,
        request: Optional['Request'] = None
    ):
        """
        初始化 Response 对象
        
        Args:
            resp: requests.Response 原始响应对象
            meta: 从 Request 传递的上下文数据
            request: 关联的 Request 对象
        """
        # 复制 requests.Response 的核心属性
        self._response = resp
        self.status_code = resp.status_code
        self.url = resp.url
        self.headers = resp.headers
        self.cookies = resp.cookies
        self.encoding = resp.encoding
        self.content = resp.content
        
        # boost_scrapy 扩展属性
        self._meta = meta or {}
        self._request = request
        
        self._selector = None
        self._text = None
        self._resp_dict = None
    
    @property
    def text(self) -> str:
        """获取响应文本"""
        if self._text is None:
            self._text = self._response.text
        return self._text
    
    @property
    def selector(self) -> Selector:
        """获取 parsel.Selector 对象"""
        if self._selector is None:
            self._selector = Selector(text=self.text)
        return self._selector
    
    @property
    def resp_dict(self) -> Any:
        """自动解析 JSON 响应"""
        if self._resp_dict is None:
            try:
                self._resp_dict = self._response.json()
            except Exception:
                self._resp_dict = {}
        return self._resp_dict
    
    @property
    def meta(self) -> Dict[str, Any]:
        """获取传递的上下文数据"""
        return self._meta
    
    @property
    def request(self) -> Optional['Request']:
        """获取关联的 Request 对象"""
        return self._request
    
    def xpath(self, query: str):
        """
        XPath 选择器
        
        Args:
            query: XPath 表达式
        
        Returns:
            SelectorList 对象
        """
        return self.selector.xpath(query)
    
    def css(self, query: str):
        """
        CSS 选择器
        
        Args:
            query: CSS 选择器表达式
        
        Returns:
            SelectorList 对象
        """
        return self.selector.css(query)
    
    def re_search(self, pattern: str, flags: int = 0):
        """
        正则搜索（返回第一个匹配）
        
        Args:
            pattern: 正则表达式
            flags: 正则标志
        
        Returns:
            Match 对象或 None
        """

        cache_key = (pattern, flags)
        if cache_key not in self._re_pattern_cache:
            self._re_pattern_cache[cache_key] = re.compile(pattern, flags)
        return self._re_pattern_cache[cache_key].search(self.text)
    
    def re_findall(self, pattern: str, flags: int = 0):
        """
        正则查找全部
        
        Args:
            pattern: 正则表达式
            flags: 正则标志
        
        Returns:
            匹配列表
        """

        cache_key = (pattern, flags)
        if cache_key not in self._re_pattern_cache:
            self._re_pattern_cache[cache_key] = re.compile(pattern, flags)
        return self._re_pattern_cache[cache_key].findall(self.text)
    
    def json(self) -> Any:
        """解析 JSON 响应（兼容 requests.Response.json()）"""
        return self._response.json()
    
    def __repr__(self):
        return f"<Response [{self.status_code}] {self.url}>"

`````

--- **end of file: boost_scrapy/response.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/spider.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/spider.py`

#### 📝 Module Docstring

`````
boost_scrapy.spider - Spider 爬虫基类

类似 Scrapy 的 Spider，用户继承此类定义爬虫逻辑。
`````

#### 📦 Imports

- `from typing import Dict`
- `from typing import Any`
- `from typing import Generator`
- `from typing import List`
- `from typing import TYPE_CHECKING`
- `from typing import Type`
- `from boost_scrapy.request import Request`
- `from boost_scrapy.response import Response`
- `from boost_scrapy.pipeline import Pipeline`

#### 🏛️ Classes (1)

##### 📌 `class Spider`
*Line: 16*

**Docstring:**
`````
爬虫基类 - 类似 Scrapy Spider

使用示例:
    class NewsSpider(Spider):
        name = "news_spider"
        custom_settings = {'concurrent_num': 5}
        
        def start_requests(self):
            yield Request("http://example.com", callback=self.parse)
        
        def parse(self, response):
            for item in response.xpath('//div'):
                yield Request(item.xpath('./@href').get(), callback=self.parse_detail)
        
        def parse_detail(self, response):
            yield Item(title=response.xpath('//h1/text()').get())
`````

**🔧 Constructor (`__init__`):**
- `def __init__(self)`
  - **Docstring:**
  `````
  初始化爬虫
  `````
  - **Parameters:**
    - `self`

**Public Methods (4):**
- `def start_requests(self) -> Generator['Request', None, None]`
  - **Docstring:**
  `````
  初始请求生成器 - 子类必须实现
  
  yield Request 对象发起初始请求。
  
  Returns:
      Request 生成器
  
  示例:
      def start_requests(self):
          for page in range(1, 10):
              yield Request(f"http://example.com?page={page}", callback=self.parse)
  `````
- `def parse(self, response: 'Response')`
  - **Docstring:**
  `````
  默认解析方法
  
  如果 Request 没有指定 callback，则使用此方法。
  
  Args:
      response: 响应对象
  
  Returns:
      可 yield Request 或 Item
  `````
- `def closed(self, reason: str)`
  - **Docstring:**
  `````
  爬虫关闭时回调
  
  Args:
      reason: 关闭原因
  `````
- `def from_crawler(cls, **kwargs) -> 'Spider'` `classmethod`
  - **Docstring:**
  `````
  工厂方法 - 创建爬虫实例
  
  Args:
      **kwargs: 初始化参数
  
  Returns:
      爬虫实例
  `````

**Class Variables (3):**
- `name: str = 'base_spider'`
- `custom_settings: Dict[str, Any] = {}`
- `pipelines: List[Type['Pipeline']] = []`


---

`````python
# coding=utf-8
"""
boost_scrapy.spider - Spider 爬虫基类

类似 Scrapy 的 Spider，用户继承此类定义爬虫逻辑。
"""

from typing import Dict, Any, Generator, List, TYPE_CHECKING, Type

if TYPE_CHECKING:
    from boost_scrapy.request import Request
    from boost_scrapy.response import Response
    from boost_scrapy.pipeline import Pipeline


class Spider:
    """
    爬虫基类 - 类似 Scrapy Spider
    
    使用示例:
        class NewsSpider(Spider):
            name = "news_spider"
            custom_settings = {'concurrent_num': 5}
            
            def start_requests(self):
                yield Request("http://example.com", callback=self.parse)
            
            def parse(self, response):
                for item in response.xpath('//div'):
                    yield Request(item.xpath('./@href').get(), callback=self.parse_detail)
            
            def parse_detail(self, response):
                yield Item(title=response.xpath('//h1/text()').get())
    """
    
    # 爬虫名称（子类必须定义）
    name: str = "base_spider"
    
    # 自定义配置（可选）
    # 可配置项: concurrent_num, qps, max_retry_times, broker_kind 等
    custom_settings: Dict[str, Any] = {}
    
    # Pipeline 列表（可选）
    pipelines: List[Type['Pipeline']] = []
    
    def __init__(self):
        """初始化爬虫"""
        self._closed = False
    
    def start_requests(self) -> Generator['Request', None, None]:
        """
        初始请求生成器 - 子类必须实现
        
        yield Request 对象发起初始请求。
        
        Returns:
            Request 生成器
        
        示例:
            def start_requests(self):
                for page in range(1, 10):
                    yield Request(f"http://example.com?page={page}", callback=self.parse)
        """
        raise NotImplementedError(f"{type(self).__name__}.start_requests() must be implemented")
    
    def parse(self, response: 'Response'):
        """
        默认解析方法
        
        如果 Request 没有指定 callback，则使用此方法。
        
        Args:
            response: 响应对象
        
        Returns:
            可 yield Request 或 Item
        """
        pass
    
    def closed(self, reason: str):
        """
        爬虫关闭时回调
        
        Args:
            reason: 关闭原因
        """
        pass
    
    @classmethod
    def from_crawler(cls, **kwargs) -> 'Spider':
        """
        工厂方法 - 创建爬虫实例
        
        Args:
            **kwargs: 初始化参数
        
        Returns:
            爬虫实例
        """
        return cls(**kwargs)
    
    def __repr__(self):
        return f"<{type(self).__name__} '{self.name}'>"

`````

--- **end of file: boost_scrapy/spider.py** (project: boost_spider) --- 

---


--- **start of file: boost_scrapy/__init__.py** (project: boost_spider) --- 


### 📄 Python File Metadata: `boost_scrapy/__init__.py`

#### 📝 Module Docstring

`````
boost_scrapy - 基于 funboost 的 Scrapy 风格爬虫框架

将 funboost 封装成类似 Scrapy 的 yield Request 框架，
让习惯 Scrapy 写法的用户能够快速上手。

核心组件:
- Request: 请求对象，封装 URL、callback、meta 等
- Response: 响应对象，继承 SpiderResponse，支持 xpath/css
- Item: 数据项，用于定义爬取的数据结构
- Spider: 爬虫基类，提供 start_requests 和 parse 方法
- Pipeline: 数据入库管道
- Engine: 核心引擎，解析 yield 生成器并调度任务

使用示例:
    from boost_scrapy import Spider, Request, Item, Engine
    
    class NewsItem(Item):
        pass
    
    class NewsSpider(Spider):
        name = "news_spider"
        
        def start_requests(self):
            yield Request("http://example.com/list", callback=self.parse_list)
        
        def parse_list(self, response):
            for news in response.resp_dict:
                yield Request(
                    f"/detail/{news['id']}", 
                    callback=self.parse_detail,
                    meta={'id': news['id']}
                )
        
        def parse_detail(self, response):
            yield NewsItem(
                id=response.meta['id'],
                title=response.xpath('//h1/text()').get()
            )
    
    if __name__ == "__main__":
        engine = Engine()
        engine.run(NewsSpider)
`````

#### 📦 Imports

- `from boost_scrapy.request import Request`
- `from boost_scrapy.response import Response`
- `from boost_scrapy.item import Item`
- `from boost_scrapy.spider import Spider`
- `from boost_scrapy.pipeline import Pipeline`
- `from boost_scrapy.pipeline import ConsolePipeline`
- `from boost_scrapy.pipeline import SQLModelPipeline`
- `from boost_scrapy.middleware import Middleware`
- `from boost_scrapy.middleware import UserAgentMiddleware`
- `from boost_scrapy.middleware import HeadersMiddleware`
- `from boost_scrapy.middleware import RetryMiddleware`
- `from boost_scrapy.middleware import ProxyMiddleware`
- `from boost_scrapy.engine import Engine`
- `from boost_scrapy.log import logger`


---

`````python
# coding=utf-8
"""
boost_scrapy - 基于 funboost 的 Scrapy 风格爬虫框架

将 funboost 封装成类似 Scrapy 的 yield Request 框架，
让习惯 Scrapy 写法的用户能够快速上手。

核心组件:
- Request: 请求对象，封装 URL、callback、meta 等
- Response: 响应对象，继承 SpiderResponse，支持 xpath/css
- Item: 数据项，用于定义爬取的数据结构
- Spider: 爬虫基类，提供 start_requests 和 parse 方法
- Pipeline: 数据入库管道
- Engine: 核心引擎，解析 yield 生成器并调度任务

使用示例:
    from boost_scrapy import Spider, Request, Item, Engine
    
    class NewsItem(Item):
        pass
    
    class NewsSpider(Spider):
        name = "news_spider"
        
        def start_requests(self):
            yield Request("http://example.com/list", callback=self.parse_list)
        
        def parse_list(self, response):
            for news in response.resp_dict:
                yield Request(
                    f"/detail/{news['id']}", 
                    callback=self.parse_detail,
                    meta={'id': news['id']}
                )
        
        def parse_detail(self, response):
            yield NewsItem(
                id=response.meta['id'],
                title=response.xpath('//h1/text()').get()
            )
    
    if __name__ == "__main__":
        engine = Engine()
        engine.run(NewsSpider)
"""

from boost_scrapy.request import Request
from boost_scrapy.response import Response
from boost_scrapy.item import Item
from boost_scrapy.spider import Spider
from boost_scrapy.pipeline import Pipeline, ConsolePipeline, SQLModelPipeline
from boost_scrapy.middleware import Middleware, UserAgentMiddleware, HeadersMiddleware, RetryMiddleware, ProxyMiddleware
from boost_scrapy.engine import Engine
from boost_scrapy.log import logger

__all__ = [
    'Request',
    'Response', 
    'Item',
    'Spider',
    'Pipeline',
    'SQLModelPipeline',
    'ConsolePipeline',
    'Middleware',
    'UserAgentMiddleware',
    'HeadersMiddleware',
    'RetryMiddleware',
    'ProxyMiddleware',
    'Engine',
    'logger',
]

__version__ = '0.1.0'

`````

--- **end of file: boost_scrapy/__init__.py** (project: boost_spider) --- 

---

