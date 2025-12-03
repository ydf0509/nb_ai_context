# nb_ai_context

**[English](README.md) | [中文](README_CN.md)**

[![PyPI version](https://img.shields.io/pypi/v/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![Python versions](https://img.shields.io/pypi/pyversions/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚀 **极其强大的 AI 上下文生成器** - 将任意 IT 项目合并生成为1个结构化 Markdown 文档，方便一次上传给 AI 大模型或 RAG 知识库。 

**神级别骚操作的用途场景：随时随地和ai聊项目** - 快要下班和放假前，你执行一下 `AiMdGenerator` 得到单个合并markdown，你在乘坐地铁时和睡觉前都能和ai非常精准的聊项目代码，因为你不可能随时随地抱着你的编程电脑到处跑吧,但是手机却可以24小时不离身，尤其是把文档传给 `google ai studio` 的代码理解和生成能力吊打我们一般码农。在手机上用自然语言，轻松对着你几万行的项目指点江山。这简直就是降维打击，因为它让一个拿着手机的人，拥有了比抱着电脑但只会死磕 IDE 的人更广阔的视野和更灵活的思考空间。这才是 AI 赋能程序员的终极形态。

**`nb_ai_context` 生成的 markdown 文件传给 `Google AI Studio`，生成代码质量和准确率，远远吊打在 `Cursor` `Trae` `Qoder` `Gemini Code Assist` 等 AI IDE 中写代码。**

<pre style="color: red;font-weight: bold;background-color:yellow;padding: 10px;border-radius: 5px;font-size: 16px;">
本人实测：
将 nb_ai_context 对项目教程+源码生成的单个 markdown 文件传给 Google AI Studio 网页版
的 1000k 上下文 + Gemini 2.5 Pro 大模型，再提问让 Gemini 写代码，代码生成的准确率和质量
远远吊打在 Cursor Trae Qoder 等 AI IDE 或 Gemini Code Assist 等编程插件里面提问写代码。

Google AI Studio 优点是 1000k 上下文以及免费。唯一缺点是它在网页生成代码，而不是直接
操作修改你的本地代码文件。

nb_ai_context 生成的 markdown 丢给 Google AI Studio 完爆 Cursor Trae 等 IDE 中写代码
的主要原因是：Google AI Studio 网页版是全量阅读推理你上传的文件，而 AI 编程 IDE 对长
教程或者源码，AI Agent 试图采取关键字搜索匹配再投喂上下文给 AI 大模型，这种方式简直是
管中窥豹、一叶障目不见泰山。

最根本原因还是：AI IDE 为了减少成本，防止 token 消耗大，不会全量把源码教程喂给 AI 大模型。
nb_ai_context 对大型编程项目的效果尤为突出！
</pre>

## nb_ai_context 作用

Nb_ai_context is not simply merging project file code, it is a context optimization tool specifically designed for AI code interaction, with the core goal of reducing AI illusions.

- nb_ai_context 就是要把 任何it项目打包生成一个markdown，上传给ai掌握。

- 你可以先搜索下repomix的作用，nb_ai_context 生成的文档对ai学习而言，远超 repomix ，尤其是对python项目来说。  repomix 只是简单的合并多个文件内容，nb_ai_context 远不是合并这么简单而已。

- 为什么需要nb_ai_context？因为例如 google-genai 和 langchain 和pydantic这些三方包的api变化太快了，你不给最新文档，直接让ai写，
  ai就给你写出过气过时的三方包版本用法，旧版本用法连有些api的import都报错，无法可用，所以需要上传更新的教程文档给ai，ai才能写出正确的代码。
  用户不能为了使用ai而妥协，而使用很老过时的python三方包版本。



## ✨ 核心特性

- ✅ **AI 阅读指南** - 为 AI 模型添加阅读说明，帮助理解文档结构，减少幻觉
- ✅ **文件依赖分析** - 分析 import 依赖关系，识别入口文件和核心模块
- ✅ **AST 元数据提取** - 从 Python 文件提取类/函数签名，无需完整源码
- ✅ **智能文件合并** - 支持 .gitignore、文件过滤、目录排除
- ✅ **清晰的文件边界** - 每个文件标记项目名和路径，方便 AI 识别
- ✅ **GitHub 项目支持** - 直接从 GitHub zip URL 生成文档
- ✅ **链式 API** - 优雅的流式接口构建上下文

## 📦 安装

```bash
pip install nb_ai_context
```

**依赖项：**
- Python >= 3.7
- nb_path
- nb_log

## 🚀 快速开始

### 基本用法

```python
from nb_ai_context import AiMdGenerator

project_name = "my_project"
project_root = r"D:\codes\my_project"

project_summary = f"""
- `{project_name}` 是一个强大的 Python 库
- 主入口是 `src/main.py` 中的 `MyClass`
"""

(
    AiMdGenerator(rf"D:\ai_docs\{project_name}_for_ai.md")
    .set_project_propery(project_name=project_name, project_root=project_root)
    .clear_text()
    .add_ai_reading_guide()  # 添加 AI 阅读指南
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "src/__init__.py",
            "src/main.py",
            "src/utils.py",
        ],
    )
    .auto_merge_from_python_project_some_files()  # 自动合并 README、setup.py、pyproject.toml
    .merge_from_dir(
        relative_dir_name="src",
        as_title=f"{project_name} 源代码",
        use_gitignore=True,
        should_include_suffixes=[".py", ".md"],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)
```

### 多项目不同根目录

```python
from nb_ai_context import AiMdGenerator

project_name = "nb_log"
project_root = r"D:\codes\nb_log"

ai_md = AiMdGenerator(
    r"D:\ai_docs\nb_log_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)

(
    ai_md.clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary="nb_log 是一个强大的日志库...",
        most_core_source_code_file_list=[
            "nb_log/__init__.py",
            "nb_log/log_manager.py",
        ],
    )
    # 从不同的项目根目录合并文档
    .merge_from_dir(
        project_root=r"D:\codes\nb_log_docs",  # 不同的根目录！
        relative_dir_name=r"source\articles",
        as_title=f"{project_name} 文档",
        should_include_suffixes=[".md"],
    )
    # 从原始根目录合并源码
    .merge_from_dir(
        relative_dir_name=project_name,
        as_title=f"{project_name} 源代码",
        should_include_suffixes=[".py", ".md"],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)
```

### 从 GitHub 项目生成

```python
from nb_ai_context import gen_github_proj_docs_and_codes_ai_md

gen_github_proj_docs_and_codes_ai_md(
    github_zip_url="https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main",
    output_md_path=r"D:\ai_docs\sqlmodel_all_docs_and_codes.md",
    readme_file="README.md",
    docs_dir_name="docs",
    codes_dir_name="sqlmodel",
    should_include_suffixes=[".py", ".md"],
    excluded_dir_name_list=["tests", "__pycache__"],
)
```

## 📖 API 参考

### AiMdGenerator 类

生成 AI 上下文的核心类。继承自 `NbPath`，支持链式调用。

#### 方法

| 方法 | 描述 |
|------|------|
| `set_project_propery(project_name, project_root)` | **必须首先调用**。设置项目名称和根目录 |
| `add_ai_reading_guide()` | 添加 AI 阅读指南以减少幻觉 |
| `add_project_summary(project_summary, most_core_source_code_file_list)` | 添加项目概述和核心文件 AST 元数据 |
| `add_file_dependencies(file_list)` | 分析并添加文件依赖图 |
| `auto_merge_from_python_project_some_files()` | 自动合并 README.md、setup.py、pyproject.toml |
| `merge_from_files(file_list, as_title)` | 合并指定文件 |
| `merge_from_dir(relative_dir_name, as_title, ...)` | 合并整个目录（支持过滤） |
| `merge_from_files_with_metadata(...)` | 高级合并，可控制元数据 |
| `show_textfile_info()` | 显示生成文件的统计信息 |

#### merge_from_dir 参数

```python
.merge_from_dir(
    relative_dir_name="src",           # 相对于 project_root 的目录
    as_title="源代码",                  # Markdown 中的章节标题
    project_root=None,                 # 覆盖项目根目录（可选）
    should_include_suffixes=[".py"],   # 要包含的文件扩展名
    excluded_dir_name_list=[],         # 要排除的目录
    excluded_file_name_list=[],        # 要排除的文件
    use_gitignore=True,                # 遵循 .gitignore 规则
    dry_run=False,                     # 预览模式（不实际生成）
    include_ast_metadata=True,         # 包含 Python AST 元数据
)
```

### GitHub 辅助函数

| 函数 | 描述 |
|------|------|
| `gen_github_proj_docs_and_codes_ai_md(...)` | 从 GitHub 仓库生成文档（分离文档/代码目录） |
| `gen_github_proj_all_dirs_ai_md(...)` | 从整个 GitHub 仓库生成文档 |

## 🎨 生成的 Markdown 结构

````markdown
# 🤖 AI Reading Guide for Project: my_project
（AI 模型阅读说明）

# markdown content namespace: my_project project summary
（项目描述）

## 📋 my_project most core source files metadata
（核心文件的 AST 元数据 - 无源码）

## 🔗 my_project File Dependencies Analysis
（import 依赖关系和依赖图）

# markdown content namespace: my_project 源代码

## my_project File Tree (relative dir: `src`)
（目录树）

## my_project Included Files (total: X files)
（文件列表）

--- **start of file: src/main.py** (project: my_project) ---
### 📄 Python File Metadata: `src/main.py`
（AST 元数据）

```python
（完整源码）
```

--- **end of file: src/main.py** (project: my_project) ---
````

## 🐍 Python AST 元数据提取

对于 Python 文件，自动提取：
- 模块文档字符串
- import 语句
- 类定义（名称、基类、装饰器、文档字符串、方法、属性、类变量）
- 函数定义（名称、参数及类型/默认值、返回类型、装饰器、文档字符串）
- 构造函数（`__init__`）详情

## 🔒 安全性

- 当 `use_gitignore=True` 时自动遵循 `.gitignore` 规则
- 排除隐藏目录（以 `.` 开头）
- 支持手动排除敏感目录/文件

## 🎯 使用场景

1. **AI 代码审查** - 让 AI 分析整个项目的质量、安全、性能
2. **RAG 知识库** - 将结构化项目文档导入向量数据库
3. **项目文档** - 为新团队成员生成全面的项目概览
4. **学习开源项目** - 借助 AI 快速理解 GitHub 项目架构

### 神级别骚操作的用途场景：

**神级别骚操作的用途场景：随时随地和ai聊项目** - 快要下班和放假前，你执行一下 `AiMdGenerator` 得到单个合并markdown，你在乘坐地铁时和睡觉前都能和ai非常精准的聊项目代码，因为你不可能随时随地抱着你的编程电脑到处跑吧,但是手机却可以24小时不离身，尤其是把文档传给 `google ai studio` 的代码理解和生成能力吊打我们一般码农。在手机上用自然语言，轻松对着你几万行的项目指点江山。这简直就是降维打击，因为它让一个拿着手机的人，拥有了比抱着电脑但只会死磕 IDE 的人更广阔的视野和更灵活的思考空间。这才是 AI 赋能程序员的终极形态。

#### 这种工作流的“爽点”在哪里？

**场景一：地铁上的“代码审查”**
> *你在地铁上，突然想到：“哎，下午写的那个 `User` 模块是不是和 `Order` 模块耦合太紧了？”*
>
> **操作**：打开手机，问 Gemini：“基于我上传的代码，分析一下 `User` 类和 `Order` 类的耦合度，并给出重构建议。”
> **结果**：AI 会引用你具体的代码行数，给出极其专业的重构方案。你只需要点头：“嗯，这思路对，明天早上去公司就这么改。” —— **通勤时间变成了高价值的架构思考时间。**

**场景二：睡前的“无痛阅读”**
> *接手了一个屎山代码，白天看了一天头昏脑涨，还有一个核心逻辑没看懂。*
>
> **操作**：躺在床上，问 Gemini：“用最通俗的语言，给我讲讲 `CoreEngine` 这个类是怎么调度任务的，画一个文字版的流程图给我。”
> **结果**：AI 像一个耐心的导师，把逻辑拆解给你看。你不用费眼看代码，看着中文解释就懂了，安心睡觉。

**场景三：灵感捕捉**
> *周末在逛街，突然想到一个新功能。*
>
> **操作**：掏出手机：“如果在现在的项目里加一个 `WebSocket` 推送功能，需要改动哪些文件？写一个 MVP 方案给我。”
> **结果**：AI 基于你现有的全量代码，列出了具体要改 `api.py`, `models.py`，甚至把代码大概样子都写好了。你截图保存，周一直接由 AI 辅助落地。

#### **总结：**   

这个用法，**把“写代码”这种重体力劳动，变成了“聊架构、聊逻辑”的轻脑力劳动。**

## 💡 为什么需要 nb_ai_context？

### 对比优势

| 方案 | 上下文完整性 | Token 消耗 | 安全性 | 成本 |
|------|--------------|------------|--------|------|
| **Cursor/Trae/Qoder** | ❌ 分段阅读 | ⚠️ 高 | ⚠️ 需手动过滤 | 💰 付费次数限制 |
| **手动复制粘贴** | ❌ 易遗漏 | ❌ 极高 | ❌ 易泄露敏感信息 | ⏰ 耗时 |
| **repomix** | ⚠️ 简单合并 | ⚠️ 一般 | ⚠️ 基本过滤 | 🆓 免费工具 |
| **nb_ai_context** | ✅ 完整结构化 | ✅ AST 元数据优化 | ✅ 自动 .gitignore | 🆓 免费工具 |

### 推荐工作流

1. 使用 `nb_ai_context` 生成项目的 Markdown 文档
2. 上传到 [Google AI Studio](https://aistudio.google.com/)（免费，1000k 上下文）
3. 与 Gemini 2.5 Pro 对话，获得高质量的代码建议

### 其他推荐平台

- **Google AI Studio**: https://aistudio.google.com/ （1000k 上下文，免费）
- **智谱清言 AI 智能体**: https://chatglm.cn/ （支持免费 RAG）
- **腾讯 IMA 知识库**: https://ima.qq.com/

## 🔗 相关链接

- **GitHub**: https://github.com/ydf0509/nb_ai_context
- **PyPI**: https://pypi.org/project/nb_ai_context/
- **Issues**: https://github.com/ydf0509/nb_ai_context/issues



## 📄 许可证

MIT License

## 🌟 Star History

如果这个项目对你有帮助，请给个 Star ⭐️！

---

**nb_ai_context** - 让 AI 真正理解你的代码 🚀




# nb_ai_context 与 repomix 比较：减少 AI 幻觉的专业分析

- `nb_ai_context` 是 `nb_path`的副产物，`AiMdGenerator`继承自 `NbPath`，所以也支持无限链式操作，方便用户无限链式合并多个文件夹来源到一个markdown中。    
但是现在 `nb_ai_context` 独立出来了，因为生成ai上下文比文件路径操作更难，更复杂，更需要技巧。

- `repomix` 是it项目代码打包到一个单独文件的 顶流三方库 ， 但`nb_ai_context` 几乎在各方面远超 `repomix`  

- `nb_ai_context` 是python代码无限链式操作方式，支持各种方法，比`repomix`的命令行灵活太多了,例如支持自定义重要ai提示词工程，`nb_ai_context` 支持用户通过 `most_core_source_code_file_list` 指定最最重要的核心文件列表，以便让ai更清晰知道三方包或者本项目的核心api ;支持新增通过 project_summary入参 自定义 ai提示词。

- 用户可以验证 `nb_ai_context` 到底强不强，还是作者吹牛逼的，  本项目下的`ai_md_files_demo/nb_ai_context_all_docs_and_codes.md` 文件就是 `nb_ai_context` 生成的,
   用户可以把 `nb_ai_context_all_docs_and_codes.md` 上传给 `google ai stduio`，让ai帮你掌握 `nb_ai_context` 的使用方式，看ai在没有训练过的前提下，能不能学会冷门三方包的使用方式。



## 核心设计哲学对比

### nb_ai_context
**专为减少 AI 幻觉而设计**，文档中明确提到了多项针对性功能：
- 详细的 AI 阅读指南（明确告诉 AI 如何理解文档结构）
- 严格的文件边界标记（清晰标识每个文件的开始/结束）
- AST 元数据提取（让 AI 先理解代码结构，再看源码）
- 项目依赖关系分析（帮助 AI 理解模块间关系）
- 强制路径验证（要求 AI 在建议代码变更时必须验证文件路径存在）

### repomix
**主要聚焦于代码库聚合**，其设计目标是将代码库转化为单一文本文件：
- 简单的文件分隔标记
- 基本的文件过滤能力
- 保留原始代码结构
- 缺乏专门针对 AI 理解和减少幻觉的深度设计

## 减少 AI 幻觉的关键特性对比

| 特性 | nb_ai_context | repomix |
|------|--------------|---------|
| **AI 阅读指南** | ✅ 详细指南，明确告诉 AI 如何理解文档结构 | ❌ 基本没有 |
| **文件边界标识** | ✅ 严格的项目名称+路径标识，防止文件混淆 | ⚠️ 简单的文件分隔符 |
| **代码结构预览** | ✅ AST 元数据提取（类/函数签名、文档字符串） | ❌ 无，直接显示源码 |
| **依赖关系分析** | ✅ 可视化模块间依赖，帮助 AI 理解架构 | ❌ 无 |
| **核心入口标识** | ✅ 明确标识核心文件和入口点 | ❌ 无 |
| **路径验证要求** | ✅ 明确指令要求 AI 验证文件路径 | ❌ 无明确指导 |
| **项目摘要** | ✅ 结构化项目概述，帮助 AI 快速把握重点 | ⚠️ 有限的描述能力 |
| **隐藏/敏感文件处理** | ✅ 支持 .gitignore 和手动排除敏感内容 | ⚠️ 基本过滤功能 |

## 实际效果对比

当将这些工具生成的上下文提供给 AI 模型时：

### nb_ai_context 优势
1. **减少文件路径幻觉**：通过强制要求 AI "检查文件路径" 和 "验证文件路径存在于文件树中"，几乎消除了 AI 虚构不存在文件的问题
2. **减少架构误解**：通过依赖关系图和 AST 元数据，AI 更容易理解项目的整体架构，不会错误假设模块间关系
3. **精准代码引用**：严格标记的文件边界使 AI 在回答时能准确引用特定文件和行号
4. **上下文理解更全面**：项目摘要和核心文件分析帮助 AI 快速把握项目重点，而不是迷失在细节中

### repomix 局限
1. **边界模糊**：简单的文件分隔符可能导致 AI 混淆不同文件的内容
2. **缺乏指导**：没有明确告诉 AI 如何解读文档结构，增加了幻觉风险
3. **深度理解不足**：直接暴露完整源码，没有提供代码结构的预览，AI 难以快速把握项目架构

## 结论：nb_ai_context 在减少 AI 幻觉方面显著更强

nb_ai_context 不仅仅是一个代码聚合工具，而是一个**专门为 AI 与代码交互设计的上下文优化系统**。它明确以"减少幻觉"为核心目标，在文档中反复强调：

> ⚠️ Important Notes
> 1. **Do NOT hallucinate**: Only reference code, classes, functions, and APIs that actually exist in this document
> 2. **Check file paths**: When suggesting code changes, always verify the file path exists in the File Tree
> 3. **Respect the project structure**: The File Tree shows the actual directory layout

而 repomix 更多是一个通用的代码聚合工具，没有专门针对 AI 幻觉问题的深度设计。对于需要高质量 AI 代码理解、审查或生成的场景，nb_ai_context 提供了更专业的解决方案。

如果您正在为 AI 系统准备代码上下文，特别是在企业级应用或安全敏感场景中，nb_ai_context 的专业设计将显著降低 AI 产生危险幻觉的风险。