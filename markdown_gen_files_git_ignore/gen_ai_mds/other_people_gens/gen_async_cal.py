from nb_ai_context import AiMdGenerator

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples\feature_async_cal.md"
)


(
    ai_md.clear_text()
    .merge_from_files(
        relative_file_name_list=["README.md"],
        project_root=r"D:\codes_aku\feature_async_cal",
        as_title="feature_async_cal readme",
    )
    .show_textfile_info()
    .merge_from_dir(
        project_root=r"D:\codes_aku\feature_async_cal",
        relative_dir_name=".",
        use_gitignore=True,
        as_title="feature_async_cal codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md", ".java",".yaml"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[
            r'src\main\java\com\akulaku\define\Afi',
            r'src\main\java\com\akulaku\define\Asi',
            r'src\main\java\com\akulaku\define\Bnc',
            r'src\main\java\com\akulaku\define\Coln',
            r'src\main\java\com\akulaku\define\Eu',
            r'src\main\java\com\akulaku\define\Ext',
            r'src\main\java\com\akulaku\define\My',
            r'src\main\java\com\akulaku\define\Pid',
        
        
        
        ],
    )
    .show_textfile_info()
)
