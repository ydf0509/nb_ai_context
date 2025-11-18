"""
Generate tutorials and code from any GitHub project into a markdown file for AI context

Download GitHub project zip file
https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main
https://codeload.github.com/fastapi/sqlmodel/zip/refs/tags/0.0.25

Unzip the file
Generate markdown file
"""

import typing
from nb_path import NbPath
from nb_ai_context import AiMdGenerator
import re


def extract_repo_name(github_url):
    # Match GitHub codeload URL pattern
    pattern = r"https://codeload\.github\.com/[^/]+/([^/]+)"
    match = re.search(pattern, github_url)
    if match:
        return match.group(1)
    return None


def gen_github_proj_docs_and_codes_ai_md(
    github_zip_url: str,
    output_md_path: str,
    docs_dir_name: str,
    codes_dir_name: str,
    readme_file: str,
    should_include_suffixes: list = None,
    excluded_dir_name_list: typing.List[str] = [],
    excluded_file_name_list: typing.List[str] = [],
):
    """
    Generate a Markdown document containing README, tutorials, and source code from a GitHub repository URL

    Args:
        github_zip_url: GitHub repository zip download link
                       Example: https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main
        output_md_path: Output Markdown file path
        readme_file: README file name, default is "README.md"
        docs_dir_name: Documentation directory name, e.g. "docs"
        codes_dir_name: Source code directory name, e.g. "sqlmodel"
        should_include_suffixes: List of file extensions to include,
                                By default includes ['.py', '.java', '.go', '.md', '.html']
    """
    project_name = extract_repo_name(github_zip_url)
    if should_include_suffixes is None:
        should_include_suffixes = [".py", ".java", ".go", ".md", ".html"]

    with NbPath.tempdir() as temp_dir:
        # Download zip file
        zip_file = temp_dir / "repo.zip"
        zip_file.download_from_url(github_zip_url)

        # Unzip the file
        unzip_dir = zip_file.unzip_to(temp_dir / "unzip")
        project_root = list(unzip_dir.iterdir())[
            0
        ]  # Get the project root directory after extraction

        print(f"tempdir github project_root: {project_root}")

        # Create AiMdGenerator instance and chain calls

        md_generator = (
            AiMdGenerator(output_md_path)
            .set_project_propery(project_name=project_name, project_root=project_root)
            .clear_text()
            .merge_from_files(
                relative_file_name_list=[readme_file],
                as_title=f"{project_name}  README",
            )
            .merge_from_dir(
                relative_dir_name=docs_dir_name,
                as_title=f"{project_name}  Documentation",
                should_include_suffixes=should_include_suffixes,
                use_gitignore=False,
                excluded_dir_name_list=excluded_dir_name_list,
                excluded_file_name_list=excluded_file_name_list,
            )
            .merge_from_dir(
                relative_dir_name=codes_dir_name,
                as_title=f"{project_name}  Source Code",
                should_include_suffixes=should_include_suffixes,
                use_gitignore=False,
                excluded_dir_name_list=excluded_dir_name_list,
                excluded_file_name_list=excluded_file_name_list,
            )
            .show_textfile_info()
        )

        return md_generator


def gen_github_proj_all_dirs_ai_md(
    github_zip_url: str,
    output_md_path: str,
    should_include_suffixes: list = None,
    excluded_dir_name_list: typing.List[str] = [],
    excluded_file_name_list: typing.List[str] = [],
):
    """
    生成github的项目根目录下所有文件到markdown，
    """
    project_name = extract_repo_name(github_zip_url)
    if should_include_suffixes is None:
        should_include_suffixes = [".py", ".java", ".go", ".md", ".html"]

    with NbPath.tempdir() as temp_dir:
        # Download zip file
        zip_file = temp_dir / "repo.zip"
        zip_file.download_from_url(github_zip_url)

        # Unzip the file
        unzip_dir = zip_file.unzip_to(temp_dir / "unzip")
        project_root = list(unzip_dir.iterdir())[
            0
        ]  # Get the project root directory after extraction

        print(f"tempdir github project_root: {project_root}")

        # Create AiMdGenerator instance and chain calls

        md_generator = (
            AiMdGenerator(output_md_path)
            .set_project_propery(project_name=project_name, project_root=project_root)
            .clear_text()
            .merge_from_dir(
                relative_dir_name=".",
                as_title=f"{project_name}  all files",
                should_include_suffixes=should_include_suffixes,
                use_gitignore=False,
                excluded_dir_name_list=excluded_dir_name_list,
                excluded_file_name_list=excluded_file_name_list,
            )
            .show_textfile_info()
        )

        return md_generator


if __name__ == "__main__":
    # Example: Generate documentation for sqlmodel project
    gen_github_proj_docs_and_codes_ai_md(
        github_zip_url="https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main",
        output_md_path=NbPath(
            r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples"
        )
        .joinpath("sqlmodel_all_docs_and_codes.md")
        .ensure_parent(),
        readme_file="README.md",
        docs_dir_name="docs",
        codes_dir_name="sqlmodel",
        should_include_suffixes=[
            ".py",
            ".md",
        ],
    )

    gen_github_proj_all_dirs_ai_md(
        github_zip_url="https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main",
        output_md_path=NbPath(
            r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\other_peoples"
        )
        .joinpath("sqlmodel_all_dirs.md")
        .ensure_parent(),
    )
