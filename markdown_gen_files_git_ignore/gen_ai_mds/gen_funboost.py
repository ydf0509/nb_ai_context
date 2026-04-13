
import time
from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator,NbPath
from helpers.extract_funboost_docs_md_titel import get_funboost_docs_md_titles


project_name="funboost"
project_root=fr"D:\codes\{project_name}"

project_summary = """
- `funboost` 是python 全功能分布式函数调度框架
- `funboost.faas` 是funboost的战略级核武器。使函数调度框架产生架构质变：从 Worker 到 Service

- 以下一定要记住，最最重要的 类和函数如下：
   - @boost(BoosterParams(...))  任意普通函数加上装饰器，变成分布式函数
   - BoosterParams 装饰器入参控制大全，一定要学习这个类的所有入参配置；ai绝对不允许胡编乱造源码api和教程中不存在的BoosterParams字段入参。
   - BrokerEnum：支持 40+ 种消息队列中间件。
   - BoostersManager 管理分布式函数，高阶用法可能需要用到，例如启动一组消费函数，启动所有消费函数等。
   - ApsJobAdder 类， 是定时任务的最重要使用方式的类
   - ConcurrentModeEnum：funboost支持的并发模式。
   - funboost/core/broker_kind__exclusive_config_default_define.py 决定了每种中间件类型能传递哪些
   

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
            
            r"funboost\funboost_web_manager\static",
            r"funboost/concurrent_pool/backup",
            r'funboost/funweb/flask_bps',
        
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
    .append_text( # 添加 funboost 教程 标题大全
        f'''

## funboost 教程 标题大全：             
`````text

{get_funboost_docs_md_titles()}

`````
                 
                 '''
                 )
    .merge_from_files(
        relative_file_name_list=[r'funboost/md_for_ai/funboost_ai_coding_编程指南_rules_and_skills.md'],
        as_title=f"funboost 框架 ai coding 的 rules 和skills ,ai谨记",
        project_root=r'D:/codes/funboost/',
    )
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