from nb_ai_context import AiMdGenerator

project_name="nb_aiohttp"
project_root=fr"D:\codes\{project_name}"

project_summary = """
- `nb_aiohttp` is a powerful and easy-to-use aiohttp library for Python. 
- `NbAioHttpClient(...)` is the main class to create a aiohttp object.
"""

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\nb_aiohttp_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


(
    ai_md.clear_text()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
           "nb_aiohttp/__init__.py",
           "nb_aiohttp/nb_aiohttp_m.py",
           "nb_aiohttp/nb_synchttp.py",
           "nb_aiohttp/nbhttp_instance.py",
        ],
    )
    .merge_from_dir(
    
        relative_dir_name=".",
        use_gitignore=True,
        as_title=f"{project_name} codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        excluded_file_name_list=['nb_log_config.py'],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)
