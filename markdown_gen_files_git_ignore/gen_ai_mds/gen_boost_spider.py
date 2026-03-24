from nb_ai_context import AiMdGenerator

project_name="boost_spider"
project_root=fr"D:\codes\{project_name}"

project_summary = """
- **`boost_spider` = `funboost` 的超跑引擎 + 一套为爬虫量身打造的瑞士军刀。所有仿scrapy api爬虫框架都还是处在变花样造一辆马车**

- `boost_spider` 是增加了3个爬虫常用类，RequestClient  和  SpiderResponse  和 DatasetSink, 由funboost 驱动调度和并发。
"""

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\boost_spider_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


SHOULD_INCLUDE_SUFFIXES = [".py", 
                           ".md"
                           ]

(
    ai_md.clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
           "boost_spider/sink/json_sink.py",
           "boost_spider/http/request_client.py",
           "boost_spider/__init__.py",
           "boost_spider/sink/dataset_sink.py",
        ],
    )
    
    .auto_merge_from_python_project_some_files(
    )
    
    .show_textfile_info()
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=SHOULD_INCLUDE_SUFFIXES,
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        relative_dir_name='demo_crawler',
        use_gitignore=True,
        as_title=f"demo_crawler codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=SHOULD_INCLUDE_SUFFIXES,
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    .merge_from_files(
        relative_file_name_list=[
            '七种爬虫方式公正评分(50项详细维度)-claude.md',
                                 '七种爬虫方式公正评分(50项详细维度)-gemini.md',
                                 ],
        as_title='ai评价的7中爬虫方式打分',
      
        
    )
    .merge_from_dir(
        relative_dir_name='boost_scrapy',
        use_gitignore=True,
        as_title=f"boost_scrapy codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=SHOULD_INCLUDE_SUFFIXES,
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=False,
        
    )
    .show_textfile_info()
)
