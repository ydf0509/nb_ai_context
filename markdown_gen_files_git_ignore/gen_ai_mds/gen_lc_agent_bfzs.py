import sys
sys.path.insert(0, r'D:\codes\nb_ai_context')

from markdown_gen_files_git_ignore.copy_md_to_txt import copy_md_to_txt
from nb_ai_context import AiMdGenerator


project_name = "lc_agent_bfzs"
project_root = r"D:\codes\lc-agent-bfzs"

project_summary = """
- `lc-agent-bfzs` 是基于 lc-agent 框架的自定义 Agent 应用实例。
- 展示如何用极少代码基于 lc-agent 框架构建功能完整的 AI Agent Web 应用。
- 核心入口 `bfzs/main.py` 演示了 lc-agent 的扩展能力：
  - Tools：自定义文件工具 + 数据工具（导入即注册到全局 ToolRegistry）
  - Agent：自定义 LangGraph CompiledGraph（research_agent，多步骤研究助手）
  - MCP：配置多个 MCP Server（filesystem、nbrag、context7 等）
  - Skills：配置 skills 目录
- 关键文件：
  - `bfzs/main.py`: 入口，加载配置 → 注册工具 → 构建 Agent → 启动
  - `bfzs/agents/research_agent.py`: 研究助手 Agent（plan → research → summarize）
  - `bfzs/tools/file_tools.py`: 文件操作工具
  - `bfzs/tools/data_tools.py`: 数据分析工具
  - `config.jsonc`: 模型/MCP/Skills 配置
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
            "bfzs/main.py",
            "bfzs/agents/research_agent.py",
            "bfzs/tools/file_tools.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .merge_from_dir(
        relative_dir_name="bfzs",
        use_gitignore=True,
        as_title=f"{project_name} 应用代码",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=["__pycache__"],
        include_ast_metadata=True,
    )
    .merge_from_files(
        relative_file_name_list=[
            "config.jsonc",
        ],
        as_title=f"{project_name} 配置文件",
    )
    .show_textfile_info()
)

copy_md_to_txt(ai_md)
ai_md.copy_to(f'{project_root}/{project_name}_all_docs_and_codes.md')
