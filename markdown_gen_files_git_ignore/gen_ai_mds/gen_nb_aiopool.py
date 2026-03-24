
from nb_path import AiMdGenerator





project_name="nb_aiopool"
project_root=fr"D:\codes\{project_name}"

project_summary = """
- `nb_aiopool` is a powerful aiopool library for Python.

- `NbAioPool(...)` is the main class to create a aiopool object.

- `@aio_task(...)` is the main decorator to create a aio task.
"""

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\nb_aiopool_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


(
    ai_md.clear_text()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_aiopool/contrib/nb_aio_task.py",
           "nb_aiopool/nb_aiopool.py",
           "nb_aiopool/__init__.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .show_textfile_info()
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
    .show_textfile_info()
)
