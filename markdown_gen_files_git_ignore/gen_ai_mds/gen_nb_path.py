
from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name="nb_path"

project_summary = """
- `nb_path` is a super-enhanced version of Python's standard `pathlib.Path`. 

- `NbPath(...)` is the main class to create a path object.

"""

nb_path_ai_md = AiMdGenerator(r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\nb_path_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=fr"D:\codes\{project_name}")
    
(
        nb_path_ai_md
        .clear_text()
        .add_project_summary(project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_path/__init__.py",
            "nb_path/nb_path_class.py",
            "nb_path/nb_path_py_impoter.py",
        ])
        .auto_merge_from_python_project_some_files()
        .show_textfile_info()
        .merge_from_dir(
            relative_dir_name=project_name,
            use_gitignore=True,
            as_title=f"{project_name} codes",
            # 只包含 .py 和 .md 文件
            should_include_suffixes=[".py", ".md"],
            # 排除 __pycache__ 目录和特定的测试文件
            excluded_dir_name_list=["tests/markdown_gen_files"],
            include_ast_metadata=True,
        )
        .show_textfile_info()
        .copy_to('d:/codes/nb_path/tests/markdown_gen_files/nb_path_all_docs_and_codes.md')
    )

copy_md_to_txt(nb_path_ai_md)