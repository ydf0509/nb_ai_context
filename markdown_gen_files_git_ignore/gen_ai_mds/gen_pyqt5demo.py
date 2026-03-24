from nb_ai_context import AiMdGenerator

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\pyqt5demo_all_docs_and_codes.md"
)


(
    ai_md.clear_text()
    .merge_from_files(
        relative_file_name_list=["README.md",'qt_app.py',],
        project_root=r"D:\codes\pyqt5demo",
        as_title="pyqt5demo codes",
    )
    .show_textfile_info()
    
    .show_textfile_info()
)
