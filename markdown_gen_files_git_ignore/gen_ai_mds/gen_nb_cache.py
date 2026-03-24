from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name="nb_cache"
project_root=fr"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is a powerful cache library for Python. 
- `cache(...)` is the main method for  user.
"""

ai_md = AiMdGenerator(
    fr"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\{project_name}_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


(
    ai_md
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            f"{project_name}/__init__.py",
            'nb_cache/wrapper.py',
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
        include_ast_metadata=False,
    )
    .merge_from_dir(
        relative_dir_name='examples',
        use_gitignore=True,
        as_title=f"{project_name} examples",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    .merge_from_files(
        relative_file_name_list = ['tests/ai_codes/test_core.py'],
        as_title = 'nb_cache 测试用例',
        
    )
    # .merge_from_dir(
    #     relative_dir_name='cashews',
    #     use_gitignore=True,
    #     as_title=f"知名三方包cashews 的 codes",
    #     # 只包含 .py 和 .md 文件
    #     should_include_suffixes=[".py", ".md"],
    #     # 排除 __pycache__ 目录和特定的测试文件
    #     excluded_dir_name_list=[],
    #     include_ast_metadata=False,
    # )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)


ai_md.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')