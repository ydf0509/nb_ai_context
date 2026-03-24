
from requests import get
from nb_path import AiMdGenerator,NbPath
from nb_log import get_logger

get_logger('nb_path')

project_name="nb_api"
project_root=fr"D:\codes\{project_name}"

project_summary = """
- `nb_api` 自动给fastapi的orm模型生成增删改查接口，减少重复工作
- `AioSQLModelCRUDRouter(...)` 是主要类之一，用于 sqlmodel orm 自动生成fastapi的 异步接口
"""

ai_md = AiMdGenerator(r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\nb_api_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)
    

(
        ai_md
        .clear_text()
        .add_project_summary(
            project_summary=project_summary,
            most_core_source_code_file_list=[
                "nb_api/core/aio_sqlmodel.py",
                "nb_api/core/base.py",
            ],
        )
        .auto_merge_from_python_project_some_files(
        )
        .merge_from_dir(
          
            relative_dir_name=project_name,
            use_gitignore=True,
            as_title=f"{project_name} codes",
            # 只包含 .py 和 .md 文件
            should_include_suffixes=[".py", ".md"],
            # 排除 __pycache__ 目录和特定的测试文件
            excluded_dir_name_list=[],
            excluded_file_name_list=[],
            include_ast_metadata=True,
        )
        .show_textfile_info()
        .copy_to(project_root)
    )