from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name = "learn_agent"
project_root = r"D:\codes\ai_proj"

project_summary = f"""
- `{project_name}` 是一个学习型 AI Agent 项目，模仿 OpenCode 的架构设计。
- 支持 TUI（Terminal User Interface）交互、MCP 工具调用、RAG 知识库检索、多轮对话等功能。
- 核心模块：
  - `agent/`: Agent 核心逻辑（对话循环、MCP 客户端、会话管理、审批规则）
  - `ui/`: 基于 Textual 的 TUI 界面（彩虹跑马灯、计时器等炫酷效果）
  - `mcp_servers/`: MCP 服务端（Redis 工具、系统工具、开发者工具包）
  - `rag/`: RAG 检索增强生成（ChromaDB + SiliconFlow 向量化 + Rerank）
  - `tools/`: 内置工具集（文件操作、Shell 执行等）
- 入口：`main.py` 启动 Textual TUI 应用
- 配置：`config.jsonc` 集中管理模型、MCP、RAG 等配置
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
            f"{project_name}/main.py",
            f"{project_name}/config.jsonc",
            f"{project_name}/config_loader.py",
            f"{project_name}/agent/core.py",
            f"{project_name}/agent/mcp_client.py",
            f"{project_name}/agent/approval_rules.py",
            f"{project_name}/ui/app.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        should_include_suffixes=[".py", ".md", ".tcss", ".jsonc", ".txt"],
        excluded_dir_name_list=[
            r"learn_agent\data",
            r"learn_agent\NVIDIA Corporation",
        ],
        include_ast_metadata=False,
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)

ai_md.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')
