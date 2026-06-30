import sys
sys.path.insert(0, r'D:\codes\nb_ai_context')

from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name = "lc_agent"
project_root = r"D:\codes\lc-agent"

project_summary = """
- `lc-agent` 是基于 LangChain / LangGraph 的 AI Agent Web 应用框架。
- 提供 WebSocket 流式对话、工具调用、MCP 集成、Skill 系统、多 Agent Preset 管理等能力。
- 前端使用 Vue 3 + Element Plus + Vite，后端使用 FastAPI + LangGraph。
- 核心模块：
  - `lc_agent/app.py`: LcAgentApp — 应用编排入口，创建引擎、注册路由、启动服务
  - `lc_agent/core/engine.py`: AgentEngine — 核心引擎，管理 Agent 实例、Preset、工具组
  - `lc_agent/server/websocket.py`: ChatWebSocketHandler — WebSocket 流式事件转发
  - `lc_agent/mcp/manager.py`: McpManager — MCP 服务连接管理
  - `lc_agent/tools/registry.py`: ToolRegistry — 工具注册表
  - `lc_agent/skills/scanner.py`: SkillScanner — Skill 扫描与匹配
  - `lc_agent/db/`: SQLAlchemy 异步数据持久化
  - `frontend/src/`: Vue 3 前端界面
- 用户用法：`from lc_agent import LcAgentApp, load_config`
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
            "lc_agent/__init__.py",
            "lc_agent/app.py",
            "lc_agent/core/engine.py",
            "lc_agent/server/websocket.py",
            "lc_agent/mcp/manager.py",
            "lc_agent/tools/registry.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name="lc_agent",
        use_gitignore=True,
        as_title="lc_agent Python 后端源码",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=["__pycache__", "web"],
        include_ast_metadata=True,
    )
    .merge_from_dir(
        relative_dir_name="frontend/src",
        use_gitignore=True,
        as_title="lc_agent 前端源码 (Vue 3)",
        should_include_suffixes=[".vue", ".ts", ".tsx"],
        excluded_dir_name_list=["node_modules"],
        include_ast_metadata=False,
    )
    .merge_from_files(
        relative_file_name_list=[
            "docs/my_docs/task.md",
        ],
        as_title="项目规划文档",
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)
ai_md.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')
