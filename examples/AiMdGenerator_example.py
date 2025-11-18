from nb_ai_context import AiMdGenerator


project_name = "nb_ai_context"
project_root = rf"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is a powerful ai llm context gennerator library ,it is uesd for ai llm and rag
- `AiMdGenerator(...)` is the main class to create ai context for llm.
"""


(
    AiMdGenerator(
        rf"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\{project_name}_all_docs_and_codes.md"
    )
    .set_project_propery(project_name=project_name, project_root=project_root)
    .clear_text()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_ai_context/__init__.py",
            "nb_ai_context/ai_md_generator.py",
            "nb_ai_context/contrib/gen_github_proj_ai_md.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .show_textfile_info()
    .merge_from_dir(
        relative_dir_name='examples',
        use_gitignore=True,
        as_title=f"{project_name} examples",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=True,
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
    .show_textfile_info()
)
