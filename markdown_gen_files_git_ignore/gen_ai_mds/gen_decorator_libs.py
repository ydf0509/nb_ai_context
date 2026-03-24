
from requests import get
from nb_path import AiMdGenerator,NbPath
from nb_log import get_logger

get_logger('nb_path')

ai_md = AiMdGenerator(r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\decorator_libs_all_docs_and_codes.md")
    

(
        ai_md
        .clear_text()
        .merge_from_files(
            relative_file_name_list=["README.md"],
            project_root=r"D:\codes\decorator_libs",
            as_title="decorator_libs readme",
        )
        .merge_from_dir(
            project_root=r"D:\codes\decorator_libs",
            relative_dir_name="decorator_libs",
            use_gitignore=True,
            as_title="decorator_libs codes",
            # 只包含 .py 和 .md 文件
            should_include_suffixes=[".py", ".md"],
            # 排除 __pycache__ 目录和特定的测试文件
            excluded_dir_name_list=[],
        )
        .get_textfile_info(is_show_info=True)
    )