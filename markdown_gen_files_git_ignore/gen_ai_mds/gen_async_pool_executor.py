from nb_ai_context import AiMdGenerator

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\async_pool_executor_all_docs_and_codes.md"
)


(
    ai_md.clear_text()
    .merge_from_files(
        relative_file_name_list=["README.md"],
        project_root=r"D:\codes\async_pool_executor",
        as_title="async_pool_executor readme",
    )
    .show_textfile_info()
    .merge_from_dir(
        project_root=r"D:\codes\async_pool_executor",
        relative_dir_name="async_pool_executor",
        use_gitignore=True,
        as_title="async_pool_executor codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
    )
    .show_textfile_info()
)
