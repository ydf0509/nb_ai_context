
from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator, NbPath


project_name = "celery"
project_root = fr"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is a powerful task queue library for Python. 
"""

ai_md_codes = AiMdGenerator(
    fr"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples\{project_name}_all_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)

ai_md_docs = AiMdGenerator(
    fr"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples\{project_name}_all_docs.md"
).set_project_propery(project_name=project_name, project_root=project_root)

(
    ai_md_codes
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            f"{project_name}/__init__.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)

(
    ai_md_docs
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            f"{project_name}/__init__.py",
        ],
    )
    .merge_from_dir(
        relative_dir_name='docs',
        use_gitignore=True,
        as_title=f"{project_name} docs",
        should_include_suffixes=[".py", ".md", '.rst', '.html'],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)

ai_md_docs_and_codes = NbPath(
    r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples',
    f'{project_name}_all_docs_and_codes.md'
).clear_text().merge_text_from_files([ai_md_docs, ai_md_codes])

# copy_md_to_txt(ai_md_codes)
# copy_md_to_txt(ai_md_docs)
# copy_md_to_txt(ai_md_docs_and_codes)

# ai_md_docs_and_codes.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')