



from nb_path.ai_md_generator import AiMdGenerator
from nb_path.contrib.gen_github_proj_ai_md import extract_repo_name, gen_github_proj_all_dirs_ai_md
from nb_path import NbPath


# 使用示例
if __name__ == "__main__":
    # 示例：生成 sqlmodel 项目的文档
    gen_github_proj_all_dirs_ai_md(
        github_zip_url="https://codeload.github.com/crawl-coder/Crawlo/zip/refs/heads/master",
        output_md_path=NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples',
        "crawlo_docs_and_codes.md"),
        should_include_suffixes=[".py", ".md",],
        excluded_dir_name_list=['tests',]
    )

    gen_github_proj_all_dirs_ai_md(
        github_zip_url="https://codeload.github.com/crawl-coder/Crawlo/zip/refs/heads/master",
        output_md_path=NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples',
        "crawlo_codes.md"),
        should_include_suffixes=[".py", ".md",],
        excluded_dir_name_list=['tests','docs','examples']
    )

    gen_github_proj_all_dirs_ai_md(
        github_zip_url="https://codeload.github.com/crawl-coder/Crawlo/zip/refs/heads/master",
        output_md_path=NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples',
        "crawlo_docs.md"),
        should_include_suffixes=[".py", ".md",],
        excluded_dir_name_list=['tests','crawlo','examples']
    )

    # github_zip_url="https://codeload.github.com/crawl-coder/Crawlo/zip/refs/heads/master"
    # project_name = extract_repo_name(github_zip_url)


    # with NbPath.tempdir() as temp_dir:
    #     # Download zip file
    #     zip_file = temp_dir / "repo.zip"
    #     zip_file.download_from_url(github_zip_url)
        
    #     # Unzip the file
    #     unzip_dir = zip_file.unzip_to(temp_dir / "unzip")
    #     project_root = list(unzip_dir.iterdir())[0]  # Get the project root directory after extraction

    #     print(f'tempdir github project_root: {project_root}')
        
    #     # Create AiMdGenerator instance and chain calls
    #     output_md_path=NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples',
    #      "crawlo_docs_and_codes.md")
    #     md_generator = (
    #         AiMdGenerator(output_md_path)
    #         .clear_text()
    #         .merge_from_dir(project_root,'.',as_title=f"{project_name}  all files",
    #         should_include_suffixes=[".py", ".md",],use_gitignore=False,
    #         excluded_dir_name_list=['tests'],
    #         excluded_file_name_list=[])
    #         .show_textfile_info()
    #     )

 
