from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name = "nb_agent"
project_root = rf"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` 是一个可 import 使用的 TUI Agent 框架，让用户快速开发自己的 AI Agent 项目。
- 三种扩展机制：Tools（@tool 装饰器）、MCP（外部 MCP Server）、Skills（SKILL.md 文档注入）
- 核心模块：
  - `{project_name}/core/agent.py`: AgentCore — 对话循环、工具调用、模型切换、分组管理
  - `{project_name}/tools/base.py`: @tool 装饰器 — 自动生成 OpenAI Function Calling schema，支持 group 参数
  - `{project_name}/mcp/manager.py`: MCP 管理器 — 动态连接 MCP Server、工具发现
  - `{project_name}/skills/manager.py`: SkillManager — SKILL.md 发现、加载、匹配
  - `{project_name}/tui/app.py`: TUI 界面 — 基于 Textual 的终端交互（F2 Skills / F3 工具组 / @ 补全）
  - `{project_name}/session/store.py`: 会话持久化 — SQLModel + SQLite
  - `{project_name}/approval/`: 危险操作审批机制
  - `{project_name}/config/`: 配置管理（JSONC 格式）
- 用户用法：`from nb_agent.core import AgentCore` + `from nb_agent.tools import tool`
- 支持工具分组（tool_group）：`@tool(group="file")` → `file__read_file`，TUI 中可禁用整组
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
            f"{project_name}/core/agent.py",
            f"{project_name}/tools/base.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        should_include_suffixes=[".py", ".md", ".tcss", ".jsonc"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_files(
        relative_file_name_list=[
            "nb_agent_config_jsonc_abount.md",
        ],
        as_title="项目文档",
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)

ai_md.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')
