import sys
sys.path.insert(0, r'D:\codes\nb_ai_context')

from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator, NbPath


project_name = "lc-agent"
project_root = r"D:\codes\lc-agent"
bfzs_root = r"D:\codes\lc-agent-bfzs"

project_summary = """
- `lc-agent` 是基于 LangChain / LangGraph 的 AI Agent 应用框架。
- 提供 WebSocket 流式对话、工具调用、MCP 集成、Skill 系统、多 Agent 管理等能力。
- 前端使用 Vue 3 + Element Plus + Vite 构建，后端使用 FastAPI + LangGraph。
- `lc-agent-bfzs` 是基于 lc-agent 框架的自定义 Agent 应用实例。

核心模块:
  - `lc_agent/app.py` — 应用入口 LcAgentApp
  - `lc_agent/core/engine.py` — AgentEngine 核心引擎
  - `lc_agent/server/websocket.py` — WebSocket 流式对话
  - `lc_agent/mcp/` — MCP 服务管理
  - `lc_agent/skills/` — Skill 扫描与执行
  - `lc_agent/tools/` — 工具注册与调用
  - `frontend/src/` — Vue 3 前端
"""

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\lc_agent_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)

(
    ai_md
    .clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "lc_agent/__init__.py",
            "lc_agent/app.py",
            "lc_agent/core/engine.py",
            "lc_agent/server/websocket.py",
            "lc_agent/mcp/manager.py",
            "lc_agent/tools/registry.py",
        ],
    )
    .merge_from_files(
        relative_file_name_list=[
            "README.md",
            "pyproject.toml",
            "docs/my_docs/task.md",
        ],
        as_title="lc-agent 项目文档",
    )
    .merge_from_dir(
        relative_dir_name="lc_agent",
        use_gitignore=True,
        as_title="lc-agent Python 后端源码",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=["__pycache__", "web"],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        relative_dir_name="frontend/src",
        use_gitignore=True,
        as_title="lc-agent 前端源码",
        should_include_suffixes=[".vue", ".ts", ".tsx"],
        excluded_dir_name_list=["node_modules"],
        include_ast_metadata=False,
    )
    .merge_from_dir(
        project_root=bfzs_root,
        relative_dir_name="bfzs",
        use_gitignore=True,
        as_title="lc-agent-bfzs 自定义 Agent 应用",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=["__pycache__"],
        include_ast_metadata=False,
    )
    .merge_from_files(
        relative_file_name_list=["config.jsonc"],
        project_root=bfzs_root,
        as_title="lc-agent-bfzs 配置文件",
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)
ai_md.copy_to(f'{project_root}/lc_agent_all_docs_and_codes.md')
