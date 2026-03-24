# D:\codes\fastapi-crudrouter



from requests import get
from nb_path import AiMdGenerator,NbPath
from nb_log import get_logger

get_logger('nb_path')

ai_md = AiMdGenerator(r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples\fastapi_crudrouter_all_docs_and_codes.md")
    

(
        ai_md
        .clear_text()
        .merge_from_dir(
            project_root=r"D:\codes\fastapi-crudrouter",
            relative_dir_name=".",
            use_gitignore=True,
            as_title="fastapi_crudrouter all docs and codes",
            # 只包含 .py 和 .md 文件
            should_include_suffixes=[".py", ".md", ],
            # 排除 __pycache__ 目录和特定的测试文件
            excluded_dir_name_list=[],
        )
        .get_textfile_info(is_show_info=True)
    )