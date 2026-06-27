from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name = "nbrag"
project_root = rf"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is an Agentic RAG MCP Server with 12 complementary tools for AI-driven multi-round code retrieval.
- Dual storage: ChromaDB for vectorized chunks (with overlap) + raw_files/ for original file snapshots (no overlap).
- Core modules:
  - `{project_name}/server.py`: 12 MCP tools + CLI entry point (`main()`)
  - `{project_name}/core.py`: Embedding/Rerank API calls, ChromaDB CRUD, file ingestion
  - `{project_name}/chunker.py`: Text splitting, line number calculation, Python AST scope parsing, header injection
  - `{project_name}/config.py`: Configuration loading: CLI > env vars > YAML > defaults
- AST scope injection: Python file chunks get `[File:] [Scope:] [Sig:] [Lines:]` headers before embedding, significantly improving search accuracy.
- Each chunk stores 8 metadata fields: source, filename, doc_id, chunk_index, total_chunks, line_start, line_end, scope.
- Usage: `uvx nbrag` (stdio) or `uvx nbrag --transport streamable-http --port 9101` (HTTP)
"""

ai_md = (
    AiMdGenerator(
        rf"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\{project_name}_all_docs_and_codes.md"
    )
    .set_project_propery(project_name=project_name, project_root=project_root)
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            f"{project_name}/server.py",
            f"{project_name}/core.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        should_include_suffixes=[".py"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_dir(
        relative_dir_name="nbrag/skills",
        use_gitignore=True,
        as_title=f"{project_name} skills",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        relative_dir_name="scripts",
        use_gitignore=True,
        as_title=f"{project_name} scripts",
        should_include_suffixes=[".py"],
        excluded_dir_name_list=[],
        include_ast_metadata=False,
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)

ai_md.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')
