from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name="nb_config_center"
project_root=fr"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is a redis config center library for Python. 
- `NbConfigCenter(...)` is the main class to create a redis config center object.
"""

ai_md = AiMdGenerator(
    fr"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\{project_name}_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


(
    ai_md
    .clear_text()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            f"{project_name}/__init__.py",
            'nb_config_center/nb_config_center_class.py'
        ],
    )
    .auto_merge_from_python_project_some_files()
    .show_textfile_info()
    .merge_dir_of_package_examples()
    .show_textfile_info()
)

copy_md_to_txt(ai_md)