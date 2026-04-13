
import time
from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator,NbPath
from helpers.extract_funboost_docs_md_titel import get_funboost_docs_md_titles


project_name="funboost"
project_root=fr"D:\codes\{project_name}"

project_summary = """

- `funboost` 是 Python 全功能分布式函数调度框架。
- `funboost.faas` 是 funboost 的战略级核武器，使函数调度框架产生架构质变：从 Worker 到 Service（一行代码即可为 FastAPI/Flask/Django 生成标准 Web 接口）。
- `boost_spider` 是基于 funboost 的爬虫增强包，包含 `RequestClient`, `SpiderResponse`, `DatasetSink`，用于实现无拘无束的超高光速并发爬虫。

- 🚨 **AI 必读：本文档中包含一个专门为你准备的目录 `funboost/md_for_ai/`**  
  该目录下的文件对你理解和使用 funboost 至关重要，请优先阅读并按其中规则执行。

- 📌 `funboost/md_for_ai/` 中的核心文件说明：
   - **`funboost_ai_coding_编程指南_rules_and_skills.md`**：  
     这是你生成 funboost 代码时的 **最高行为准则**。  
     包含禁止臆造参数、必须使用 `BoosterParams`、如何正确使用 `fct` 上下文、如何启动消费等铁律。  
     **生成任何代码前必须先深度学习此文件。**

   - **`funboost源码速查for_ai.md`**：  
     这是 **源码位置索引**。当用户询问某个类、函数、参数的定义或实现位置时，**优先查阅此文件**，它会给出精确的文件路径和行号。

   - **`如何扩展增加新的中间件.md`**：  
     这是 **自定义扩展指南**。当用户需要增加新的消息队列中间件或定制现有 broker 行为时，必须遵循此文档。  
     文档详细说明了 **两种扩展方式**：
        1. **`register_custom_broker`**（方式一）：适合完全新增一个不存在的 broker 类型。
        2. **`consumer_override_cls` / `publisher_override_cls`**（方式二）：适合通过 Mixin 方式修改或增强现有 broker 的逻辑（推荐）。

- 🎯 **以下是最重要的核心类和函数（务必牢记）**：
   - `@boost(BoosterParams(...))`：核心装饰器，将任意普通函数变成分布式函数。
   - `BoosterParams`：装饰器入参控制大全。**AI 绝对不允许胡编乱造不存在的字段**。
   - `fct` (funboost_current_task)：**神级任务上下文**。禁止像 Celery 那样在参数里传 `self`，必须通过 `from funboost import fct` 获取 `fct.task_id`, `fct.full_msg` 等。
   - `BrokerEnum`：支持 40+ 种消息队列中间件。
   - `BoostersManager`：管理分布式函数（启动消费组、启动所有等）。
   - `ApsJobAdder`：添加定时任务的唯一正确方式。
   - `ConcurrentModeEnum`：支持的并发模式（THREADING/GEVENT/EVENTLET/ASYNC/SINGLE_THREAD）。
   - ⬇️ **`broker_exclusive_config`**：`BoosterParams` 中的字典参数，用于设置特定消息队列中间件的**专属配置**（如 Kafka 的 `group_id`、RabbitMQ 的 `x-max-priority`、Redis 的 `pull_msg_batch_size` 等）。**严禁臆造键名**，支持的键取决于所选 `broker_kind`，可在 `funboost/core/broker_kind__exclusive_config_default_define.py` 中查看。示例：`broker_exclusive_config={'x-max-priority': 5, 'no_ack': False}`。

- **`MEMORY_QUEUE` 的重要性**：  
     这是 funboost 中最最核心的 broker（SSS 级）。它支持传递任何不可序列化的对象，并且可以把 `@boost` 当作**超级装饰器**使用——即使不需要分布式，也能获得 QPS 控频、重试、超时、去重等 30+ 种控制能力。  
     当用户想“只用一个装饰器控制函数并发/重试/超时，不想要消息队列”时，应推荐 `broker_kind=BrokerEnum.MEMORY_QUEUE`。

- 🛑 **高频 AI 幻觉与避坑指南（Anti-Hallucination Shield）**：
   **AI 在生成代码时极易犯以下错误，请严格规避！**
   1. **参数命名的幻觉**：严禁臆造 `BoosterParams` 字段！重试次数是 `max_retry_times`（不是 max_retries）；超时是 `function_timeout`（不是 timeout）；消息过期是 `msg_expire_seconds`（不是 expires），ai需要高度重视BoosterParams的字段不能乱造。
   2. **发布消息的幻觉**：传业务参数用 `func.push(x=1)`；传控制参数（如延迟 countdown、自定义 task_id）**必须**包裹在字典和 `TaskOptions` 中，写成 `func.publish({"x":1}, task_options=TaskOptions(countdown=10))`。**严禁** `func.push(x=1, countdown=10)`。
   3. **获取 RPC 结果的幻觉**：在 `async def` 环境下，**绝对禁止**直接 `async_result.result`（会引发阻塞灾难），**必须**使用 `await AioAsyncResult(task_id).result`！
   4. **实例方法发布的幻觉**：对于类中的实例方法，**严禁**写成 `obj.method.push(x)`。必须将对象实例作为第一个参数传入，写成 `ClassName.method.push(obj, x)`。
   5. **消费启动的幻觉**：`func.consume()` 默认就是在后台非阻塞运行的。**严禁**画蛇添足写成 `threading.Thread(target=func.consume).start()`。
   6. **消费外部 JSON 的幻觉**：若要消费 Java/Go 发布的带有多余字段的 JSON，**严禁**定义 `def task_fun(msg):` 企图接收整个字典。**必须**定义为 `def task_fun(**kwargs):` 并设置 `should_check_publish_func_params=False`。
   7. **重复造轮子/改源码的幻觉**：若用户要提供 HTTP 发版/查结果接口，**严禁手搓 FastAPI 路由**，必须直接 `app.include_router(fastapi_router)`；若要修改消费逻辑，**严禁提议改 funboost 源码**，必须让用户通过 `consumer_override_cls` 传参！
   8. **老式语法的幻觉**：绝对禁止生成 `@boost('queue_name')` 这种过时语法。**永远**使用 Pydantic 模型传参：`@boost(BoosterParams(queue_name='xxx'))`。
   9. 9. **`ctrl_c_recv()` 的幻觉**：  
      严禁认为 `ctrl_c_recv()` 的作用是“优雅退出”或“防止程序结束”。实际上，不加它程序也会一直运行。  
      真实作用：在 Windows 下如果不加这行代码，按 `Ctrl+C` **无法停止程序**。加上后即可正常退出。详细原理和用法见教程 **6.25b 章节**。  
      **AI 生成启动脚本时，应在 `func.consume()` 后默认加上 `ctrl_c_recv()`**。

- 🧠 **AI 回答问题的思考与检索优先级**：
   1. 用户问“怎么使用某个功能” → 优先查 **教程示例 (`source/articles/`)** 以及 **`Rules & Skills`**。
   2. 用户问“某个类/函数/参数的定义或实现位置” → 优先查 **`funboost源码速查for_ai.md`**。
   3. 用户要求“写一段代码” → 必须严格遵循 **`funboost_ai_coding_编程指南_rules_and_skills.md`** 的约束，绝不使用已被取代的旧语法。
   4. 用户问“如何扩展中间件/自定义 broker” → 必须查阅 **`如何扩展增加新的中间件.md`**。
   5. 用户问底层实现细节 → 再通过速查表定位，深入具体的 `funboost codes` 源码文件进行推理。

- 📁 **文件名拼写注意事项**（避免搜索源码时因作者历史拼写错误而找不到文件）：
   - `funboost_config_deafult.py`（是 deafult 不是 default）
   - `publisher_factotry.py`（是 factotry 不是 factory）
   - `peewee_conusmer.py`（是 conusmer 不是 consumer）
   - `active_cousumer_info_getter.py`（是 cousumer 不是 consumer）
   - `muliti_process_enhance.py`（是 muliti 不是 multi）
   - `consuming_func_iniput_params_check.py`（是 iniput 不是 input）
   - `meomory_deque_publisher.py`（是 meomory 不是 memory）
"""


boost_spider_summary = """
- **`boost_spider` = `funboost` 的超跑引擎 + 一套为爬虫量身打造的瑞士军刀。所有仿scrapy api爬虫框架都还是处在变花样造一辆马车**

- `boost_spider` 是增加了3个爬虫常用类，RequestClient  和  SpiderResponse  和 DatasetSink, 由funboost 驱动调度和并发。
"""


ai_md_codes = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\funboost_all_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)

ai_md_docs = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\funboost_all_docs.md"
      ).set_project_propery(project_name="funboost_docs", project_root=r'D:\codes\funboost_docs')


funboost_most_core_source_code_file_list=[
        "funboost/__init__.py",
        "funboost/core/booster.py",
        "funboost/core/func_params_model.py",
        "funboost/constant.py",
        "funboost/timing_job/timing_push.py",
        "funboost/funboost_config_deafult.py",
        "funboost/core/current_task.py",
        "funboost/core/cli/discovery_boosters.py",
        "funboost/core/broker_kind__exclusive_config_default_define.py",
        
        "funboost/core/msg_result_getter.py",
        "funboost/publishers/base_publisher.py",
        "funboost/consumers/base_consumer.py",
        "funboost/core/active_cousumer_info_getter.py",
        
    ]

(
    ai_md_codes
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary, 
        most_core_source_code_file_list=funboost_most_core_source_code_file_list)
    .add_project_summary(
        project_summary=boost_spider_summary, 
        project_root=r"D:\codes\boost_spider",
        most_core_source_code_file_list=[
           "boost_spider/__init__.py",
           "boost_spider/http/request_client.py",
           "boost_spider/sink/dataset_sink.py",
         
        
    ])
    # .merge_from_dir(
    #     relative_dir_name='examples',
    #     use_gitignore=True,
    #     as_title=f"{project_name} examples",
    #     # 只包含 .py 和 .md 文件
    #     should_include_suffixes=[".py", ".md", ".html"],
    #     # 排除 __pycache__ 目录和特定的测试文件
    #     excluded_dir_name_list=[],
    #     include_ast_metadata=False,
    # )
    .merge_from_dir(
        relative_dir_name='funboost/md_for_ai',
        use_gitignore=True,
        as_title=f"专门为ai理解funboost源码的markdown",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md", 
        # ".html"    # html文件太大了，不要被合并,会突破100万上下文
        ],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[
        ],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md", 
        # ".html"    # html文件太大了，不要被合并,会突破100万上下文
        ],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[
            r"funboost\utils\dependency_packages",
            r"funboost\utils\dependency_packages_in_pythonpath",
            r"funboost/utils/func_timeout",
            
            r"funboost\funweb\static",
            r'funboost\funweb\flask_bps',
            r"funboost/concurrent_pool/backup",
            
            
            
        ],
        excluded_file_name_list=[],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        project_root=r"D:\codes\boost_spider",
        relative_dir_name="boost_spider",
        use_gitignore=True,
        as_title="boost_spider codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md", ".html"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    #  .merge_from_dir(
    #     project_root=r"D:\codes\boost_spider",
    #     relative_dir_name="demo_crawler",
    #     use_gitignore=True,
    #     as_title="demo_crawler  4 kind codes",
    #     # 只包含 .py 和 .md 文件
    #     should_include_suffixes=[".py", ".md", ".html"],
    #     # 排除 __pycache__ 目录和特定的测试文件
    #     excluded_dir_name_list=[],
    # )
    .get_textfile_info(is_show_info=True)
)


(
    ai_md_docs
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary, 
        project_root=r"D:\codes\funboost",
        most_core_source_code_file_list=funboost_most_core_source_code_file_list
    )
    .add_project_summary(
        project_summary=boost_spider_summary, 
        project_root=r"D:\codes\boost_spider",
        most_core_source_code_file_list=[
           "boost_spider/__init__.py",
           "boost_spider/http/request_client.py",
           "boost_spider/sink/dataset_sink.py",
        
    ])
    .append_text( # 添加 funboost 教程 标题大全
        f'''

## funboost 教程 标题大全：             
`````text

{get_funboost_docs_md_titles()}

`````
                 
                 '''
                 )
    .merge_from_dir(
        project_root=r"D:\codes\funboost",
        relative_dir_name='examples',
        use_gitignore=True,
        as_title=f"{project_name} examples",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md", ".html"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        project_root=r"D:\codes\funboost_docs",
        relative_dir_name=r"source\articles",
        use_gitignore=True,
        as_title="funboost docs",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        excluded_file_name_list=[
            # 'source/articles/c16.md'
        ],
    )
    .merge_from_files(
        relative_file_name_list=["README.md"],
        project_root=r"D:\codes\boost_spider",
        as_title="boost_spider readme",
    )
    .get_textfile_info(is_show_info=True)
)

ai_md_docs_and_codes = NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files','funboost_all_docs_and_codes.md').clear_text().merge_text_from_files([ai_md_docs,ai_md_codes])

NbPath(r'D:\codes\funboost','funboost_all_docs.md').clear_text().merge_text_from_files([ai_md_docs])
NbPath(r'D:\codes\funboost','funboost_all_docs_and_codes.md').clear_text().merge_text_from_files([ai_md_docs,ai_md_codes])
NbPath(r'D:\codes\funboost','README.md').clear_text().merge_text_from_files([r'D:\codes\funboost_docs\source\articles\c1.md'])

NbPath(r'D:\codes\funboost_docs','funboost_all_docs.md').clear_text().merge_text_from_files([ai_md_docs])
NbPath(r'D:\codes\funboost_docs','funboost_all_docs_and_codes.md').clear_text().merge_text_from_files([ai_md_docs,ai_md_codes])

NbPath(r'D:\codes\boost_spider','funboost_all_docs_and_codes.md').clear_text().merge_text_from_files([ai_md_docs,ai_md_codes])


copy_md_to_txt(ai_md_codes)
copy_md_to_txt(ai_md_docs)
copy_md_to_txt(ai_md_docs_and_codes)


while 1:
    time.sleep(10)