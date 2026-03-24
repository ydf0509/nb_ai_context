



from nb_path.ai_md_generator import AiMdGenerator
from nb_path.contrib.gen_github_proj_ai_md import extract_repo_name, gen_github_proj_all_dirs_ai_md
from nb_path import NbPath


# 使用示例
if __name__ == "__main__":
    # 示例：生成 sqlmodel 项目的文档
    gen_github_proj_all_dirs_ai_md(
        github_zip_url="https://codeload.github.com/langchain-ai/langchain/zip/refs/heads/master",
        output_md_path=NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples',
        "langchain_codes.md"),
        should_include_suffixes=[".py", ".md",],
        excluded_dir_name_list=['tests',]
    )

   