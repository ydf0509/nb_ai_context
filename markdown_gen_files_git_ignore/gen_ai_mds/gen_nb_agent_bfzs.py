from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name = "nb_agent_bfzs"
project_root = rf"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` 是基于 nb_agent 框架的演示项目——智能笔记助手，展示如何用极少代码构建功能完整的 AI Agent + 终端 TUI。
- 核心入口 `main.py` 不到 10 行，演示了 nb_agent 的所有扩展能力：
  - Tools：7 个自定义工具（笔记 CRUD 5 个 + 项目统计 2 个）
  - MCP Server：书签管理（FastMCP）、Redis 7 工具（万能执行 + 智能读写 + 监控）、web-search（SSE）、filesystem（npx）
  - Skills：6 个（日报、会议纪要、Git changelog、代码审查、重构、代码解释）
  - 审批引擎：配置层 + 代码层双重审批（Redis 写命令细粒度控制）
- 关键文件：
  - `main.py`: 入口，加载配置 → 注册审批规则 → 启动 TUI
  - `config.jsonc`: 模型 / MCP / 审批 / UI 配置
  - `approval_rules.py`: 自定义审批规则（Redis 写命令拦截、危险工具黑名单）
  - `tools/note_tools.py`: 笔记 CRUD 工具（group="note"）
  - `tools/project_tools.py`: 项目文件统计工具（group="project"）
  - `mcp_servers/bookmark_server.py`: FastMCP 书签管理 Server
  - `mcp_servers/redis_tools_server.py`: FastMCP Redis 工具 Server
  - `.nb_agent/skills/*/SKILL.md`: Agent Skills（agentskills.io 规范）
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
            "main.py",
            "approval_rules.py",
            "tools/note_tools.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name="tools",
        use_gitignore=True,
        as_title=f"{project_name} tools",
        should_include_suffixes=[".py"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_dir(
        relative_dir_name="mcp_servers",
        use_gitignore=True,
        as_title=f"{project_name} mcp_servers",
        should_include_suffixes=[".py"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_dir(
        relative_dir_name=".nb_agent/skills",
        use_gitignore=True,
        as_title=f"{project_name} skills",
        should_include_suffixes=[".md", ".py"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_files(
        relative_file_name_list=[
            "main.py",
            "approval_rules.py",
            "config.jsonc",
            "nb_log_config.py",
        ],
        as_title=f"{project_name} root files",
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)

ai_md.copy_to(f"{project_root}/{project_name}_all_docs_and_codes.md")
