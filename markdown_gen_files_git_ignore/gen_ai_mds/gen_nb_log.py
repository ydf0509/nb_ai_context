from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator,NbPath
from nb_log import get_logger

get_logger("nb_path")

project_name = "nb_log"
project_root = rf"D:\codes\{project_name}"

project_summary = """
- `nb_log` is a powerful logging library for Python. 

- `nb_log.get_logger(...)` is the main function to get a logger object.
   get_logger 入参非常重要，不可以胡乱编造入参。

- nb_log_config.py 是nb_log的配置文件，非常重要，不可以胡乱编造配置名称。

"""

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\nb_log_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


(
    ai_md.clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_log/__init__.py",
            "nb_log/log_manager.py",
            "nb_log/nb_log_config_default.py",
        ],
    )
    .merge_from_dir(
        project_root=r"D:\codes\nb_log_readdocs",
        relative_dir_name=r"source\articles",
        use_gitignore=True,
        as_title=f"{project_name} docs",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
    )
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .get_textfile_info(is_show_info=True)
)

copy_md_to_txt(ai_md)



NbPath(r'D:\codes\nb_log','nb_log_合并教程_and_源码.md').clear_text().merge_text_from_files([ai_md])