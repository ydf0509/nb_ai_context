# 🤖 AI Reading Guide for Project: nb_ai_context

> **Important Notice for AI Models**: This document contains the complete source code and documentation for the `nb_ai_context` project. Please read this guide carefully before analyzing the content.

## 📖 Document Structure

This markdown document is structured as follows:

1. **Project Summary** (`# markdown content namespace: xxx project summary`)
   - Brief project description
   - Core source files metadata (AST-parsed class/function signatures without full source code)
   - File dependencies analysis

2. **Project Root Files** (`# markdown content namespace: xxx Project Root Dir Some Files`)
   - README.md, pyproject.toml, setup.py, etc.

3. **Source Code Sections** (`# markdown content namespace: xxx codes/examples/...`)
   - File Tree: Shows directory structure
   - Included Files: Lists all files in this section
   - Full source code with AST metadata for Python files

## 🔍 How to Identify File Boundaries

- Each file starts with: `--- **start of file: <path>** (project: nb_ai_context) ---`
- Each file ends with: `--- **end of file: <path>** (project: nb_ai_context) ---`
- All file paths are relative to the project root

## ⚠️ Important Notes

1. **Do NOT hallucinate**: Only reference code, classes, functions, and APIs that actually exist in this document
2. **Check file paths**: When suggesting code changes, always verify the file path exists in the File Tree
3. **Respect the project structure**: The File Tree shows the actual directory layout
4. **AST Metadata**: Python files include parsed metadata (imports, classes, methods) before the full source code

---

# markdown content namespace: nb_ai_context project summary 



- `nb_ai_context` is a powerful ai llm context gennerator library ,it is uesd for ai llm and rag
- `AiMdGenerator(...)` is the main class to create ai context for llm.


## 📋 nb_ai_context most core source files metadata (Entry Points)


以下是项目 nb_ai_context 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nb_ai_context most core source code files as follows: 
- `nb_ai_context/__init__.py`
- `nb_ai_context/ai_md_generator.py`
- `nb_ai_context/contrib/gen_github_proj_ai_md.py`


### 📄 Python File Metadata: `nb_ai_context/__init__.py`

#### 📦 Imports

- `from nb_path import NbPath`
- `from ai_md_generator import AiMdGenerator`
- `from contrib.gen_github_proj_ai_md import gen_github_proj_docs_and_codes_ai_md`
- `from contrib.gen_github_proj_ai_md import gen_github_proj_all_dirs_ai_md`


---




### 📄 Python File Metadata: `nb_ai_context/ai_md_generator.py`

#### 📦 Imports

- `import typing`
- `import os`
- `import fnmatch`
- `import ast`
- `from nb_path import NbPath`
- `import astor`

#### 🏛️ Classes (1)

##### 📌 `class AiMdGenerator(NbPath)`
*Line: 10*

**Docstring:**
`````
An extremely powerful context generator born for AI collaboration.

This class is designed to revolutionize how developers interact with Large Language
Models (LLMs). It intelligently merges multiple project source files into a single,
well-structured, and context-rich Markdown file, providing the AI with a perfect
and comprehensive project snapshot.

Key Features:
1.  **AI Reading Guide**: `add_ai_reading_guide()` adds instructions for AI models
    to better understand the document structure and avoid hallucinations.
2.  **Project Summary with Core Files Metadata**: `add_project_summary()` extracts
    AST metadata from core files without full source code, helping AI quickly
    grasp the project architecture.
3.  **File Dependencies Analysis**: `add_file_dependencies()` analyzes import
    relationships between files, showing entry points and core modules.
4.  **Smart File Merging**: `merge_from_dir()` and `merge_from_files()` with
    .gitignore support, file filtering, and AST metadata extraction.
5.  **Clear File Boundaries**: Each file is marked with project name and path
    for easy identification by AI models.

Main Public Methods:
- `set_project_propery(project_name, project_root)`: Set project info (required first)
- `add_ai_reading_guide()`: Add AI reading instructions to reduce hallucinations
- `add_project_summary(project_summary, most_core_source_code_file_list)`: Add summary with core file metadata
- `add_file_dependencies(file_list)`: Analyze and add file dependency graph
- `auto_merge_from_python_project_some_files()`: Auto-merge README, setup.py, pyproject.toml
- `merge_from_files(file_list, as_title)`: Merge specific files
- `merge_from_dir(dir_name, as_title, ...)`: Merge entire directory with filters
- `merge_from_files_with_metadata(file_list, as_title, include_ast_metadata, include_file_text)`: Advanced merge with metadata control

Example:
    >>> from nb_ai_context import AiMdGenerator
    >>> 
    >>> project_name = "my_project"
    >>> project_root = r"D:\codes\my_project"
    >>> 
    >>> (
    ...     AiMdGenerator(rf"D:\ai_docs\{project_name}_for_ai.md")
    ...     .set_project_propery(project_name=project_name, project_root=project_root)
    ...     .clear_text()
    ...     .add_ai_reading_guide()  # Add AI reading instructions
    ...     .add_project_summary(
    ...         project_summary="This is my awesome project...",
    ...         most_core_source_code_file_list=[
    ...             "src/main.py",
    ...             "src/api.py",
    ...         ]
    ...     )
    ...     .auto_merge_from_python_project_some_files()
    ...     .merge_from_dir(
    ...         relative_dir_name="src",
    ...         as_title=f"{project_name} Source Code",
    ...         use_gitignore=True,
    ...         should_include_suffixes=[".py", ".md"],
    ...         include_ast_metadata=True,
    ...     )
    ...     .show_textfile_info()
    ... )
`````

**Public Methods (9):**
- `def set_project_propery(self, project_name: str, project_root: typing.Union[os.PathLike, str]) -> 'AiMdGenerator'`
  - *Sets the project name for the current markdown file.*
- `def add_ai_reading_guide(self) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  添加 AI 阅读指南，帮助 AI 大模型更好地理解文档结构
  
  建议在 clear_text() 之后、add_project_summary() 之前调用
  `````
- `def add_project_summary(self, project_summary: str, most_core_source_code_file_list: typing.List[str] = None, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  Adds a project summary to the current markdown file.
  
  Args:
      project_summary: 项目概述文本
      project_root: 项目根目录（如果提供了 most_core_source_code_file_list）
      most_core_source_code_file_list: 最核心的源码文件列表（相对路径）
                                       只提取这些文件的 AST 元数据，不包含完整源码
  
  Example:
      >>> (
      ...     AiMdGenerator("output.md")
      ...     .set_project_name("my_project")
      ...     .clear_text()
      ...     .add_project_summary(
      ...         project_summary="这是一个优秀的项目...",
      ...         project_root="/path/to/project",
      ...         most_core_source_code_file_list=["src/main.py", "src/api.py"],
      ...     )
      ... )
  `````
- `def auto_merge_from_python_project_some_files(self, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - *自动合并项目根目录下的 readme.md 或者ReADME.md 以及setup.py 和 pyproject.toml ，如果有就添加*
- `def merge_from_files(self, relative_file_name_list: typing.List[str], as_title: str, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  Merges the content of the given files into the current markdown file.
  the current markdown file will be used to upload to ai model for code review and learning.
  `````
- `def merge_from_dir(self, relative_dir_name: str, as_title: str, project_root: typing.Union[os.PathLike, str] = None, should_include_suffixes: typing.List[str] = [], excluded_dir_name_list: typing.List[str] = [], excluded_file_name_list: typing.List[str] = [], use_gitignore: bool = True, dry_run: bool = False, include_ast_metadata: bool = True) -> 'AiMdGenerator'`
  - *Merges the content of the given directory into the current file.*
- `def merge_dir_of_package_examples(self)`
  - *合并包的examples目录到当前markdown文件*
- `def merge_from_files_with_metadata(self, relative_file_name_list: typing.List[str], as_title: str, project_root: typing.Union[os.PathLike, str] = None, include_ast_metadata: bool = True, include_file_text: bool = True) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  合并文件内容到 Markdown，对于 Python 文件会额外生成 AST 元数据
  
  Args:
      project_root: 项目根目录
      relative_file_name_list: 相对文件路径列表
      as_title: 标题
      include_ast_metadata: 是否包含 AST 元数据（仅对 .py 文件）
      include_file_text: 是否包含完整文件源码（False 时只显示元数据）
  `````
- `def add_file_dependencies(self, file_list: typing.List[str] = None, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  分析并添加项目文件之间的依赖关系到 markdown
  
  Args:
      file_list: 要分析的文件列表（相对路径），如果为 None 则分析整个项目
      project_root: 项目根目录
      
  Example:
      >>> (
      ...     AiMdGenerator("output.md")
      ...     .set_project_propery("my_project", "/path/to/project")
      ...     .clear_text()
      ...     .add_project_summary(project_summary="...")
      ... )
  `````

**Class Variables (1):**
- `suffix__lang_map = {'.py': 'python', '.md': 'markdown', '.txt': 'text...`


---




### 📄 Python File Metadata: `nb_ai_context/contrib/gen_github_proj_ai_md.py`

#### 📝 Module Docstring

`````
Generate tutorials and code from any GitHub project into a markdown file for AI context

Download GitHub project zip file
https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main
https://codeload.github.com/fastapi/sqlmodel/zip/refs/tags/0.0.25

Unzip the file
Generate markdown file
`````

#### 📦 Imports

- `import typing`
- `from nb_path import NbPath`
- `from nb_ai_context.ai_md_generator import AiMdGenerator`
- `import re`

#### 🔧 Public Functions (3)

- `def extract_repo_name(github_url)`
  - *Line: 18*

- `def gen_github_proj_docs_and_codes_ai_md(github_zip_url: str, output_md_path: str, docs_dir_name: str, codes_dir_name: str, readme_file: str, should_include_suffixes: list = None, excluded_dir_name_list: typing.List[str] = [], excluded_file_name_list: typing.List[str] = [])`
  - *Line: 27*
  - **Docstring:**
  `````
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
  `````

- `def gen_github_proj_all_dirs_ai_md(github_zip_url: str, output_md_path: str, should_include_suffixes: list = None, excluded_dir_name_list: typing.List[str] = [], excluded_file_name_list: typing.List[str] = [])`
  - *Line: 99*
  - *生成github的项目根目录下所有文件到markdown，*


---



## 🔗 nb_ai_context Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ nb_ai_context/__init__.py

Core Files (imported by other files, sorted by import count):
  ◆ nb_ai_context/ai_md_generator.py (imported by 2 files)
  ◆ nb_ai_context/contrib/gen_github_proj_ai_md.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `nb_ai_context/__init__.py`

**Imports from project:**
- `nb_ai_context/ai_md_generator.py`
- `nb_ai_context/contrib/gen_github_proj_ai_md.py`

#### `nb_ai_context/ai_md_generator.py`

**Imported by:**
- `nb_ai_context/__init__.py`
- `nb_ai_context/contrib/gen_github_proj_ai_md.py`

#### `nb_ai_context/contrib/gen_github_proj_ai_md.py`

**Imports from project:**
- `nb_ai_context/ai_md_generator.py`

**Imported by:**
- `nb_ai_context/__init__.py`

### 📦 Third-party Dependencies

项目使用的第三方库：

- `astor`
- `nb_path`
- ......以及更多的第三方库......


---
# markdown content namespace: nb_ai_context Project Root Dir Some Files 


## nb_ai_context File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## nb_ai_context (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: nb_ai_context) --- 

`````markdown
# nb_ai_context

**[English](README.md) | [中文](README_CN.md)**

[![PyPI version](https://img.shields.io/pypi/v/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![Python versions](https://img.shields.io/pypi/pyversions/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚀 **An extremely powerful AI context generator** - Merge any IT project into a single structured Markdown document for AI LLMs or RAG knowledge bases.

## What is nb_ai_context?

- **nb_ai_context packages any IT project into a single markdown file for AI to learn and understand.**
- You can search for "repomix" to understand its purpose - nb_ai_context generates documents that are far superior for AI learning, especially for Python projects.  
  repomix simply merges multiple file contents, but nb_ai_context does much more than just merging.
- **Why do you need nb_ai_context?** Because third-party packages like google-genai, langchain, and pydantic have APIs that change too quickly. If you don't provide the latest documentation, AI will write outdated code using old package versions - sometimes even the imports won't work!  
  You need to upload updated tutorial documents to AI so it can write correct code. Users shouldn't have to compromise by using old, outdated Python package versions just to use AI.

## ✨ Core Features

- ✅ **AI Reading Guide** - Adds instructions to help AI models understand document structure and reduce hallucinations
- ✅ **File Dependencies Analysis** - Analyzes import relationships, identifies entry points and core modules
- ✅ **AST Metadata Extraction** - Extracts class/function signatures from Python files without full source code
- ✅ **Smart File Merging** - Supports .gitignore, file filtering, directory exclusion
- ✅ **Clear File Boundaries** - Each file marked with project name and path for easy AI identification
- ✅ **GitHub Project Support** - Generate docs directly from GitHub zip URLs
- ✅ **Chainable API** - Elegant fluent interface for building context

## 📦 Installation

```bash
pip install nb_ai_context
```

**Requirements:**
- Python >= 3.7
- nb_path
- nb_log

## 🚀 Quick Start

### Basic Usage (from examples/AiMdGenerator_example.py)

```python
from nb_ai_context import AiMdGenerator

project_name = "nb_ai_context"
project_root = rf"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is a powerful ai llm context generator library, it is used for ai llm and rag
- `AiMdGenerator(...)` is the main class to create ai context for llm.
"""

(
    AiMdGenerator(
        rf"D:\codes\nb_ai_context\ai_md_files_demo\{project_name}_all_docs_and_codes.md"
    )
    .set_project_propery(project_name=project_name, project_root=project_root)
    .ensure_parent()
    .clear_text()
    .add_ai_reading_guide()  # Add AI reading guide to help AI understand document structure
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_ai_context/__init__.py",
            "nb_ai_context/ai_md_generator.py",
            "nb_ai_context/contrib/gen_github_proj_ai_md.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .show_textfile_info()
    .merge_from_dir(
        relative_dir_name='examples',
        use_gitignore=True,
        as_title=f"{project_name} examples",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        should_include_suffixes=[".py", ".md"],
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)
```

### From GitHub Projects

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

## 📖 API Reference

### AiMdGenerator Class

The core class for generating AI context. Inherits from `NbPath` and supports chainable calls.

#### Methods

| Method | Description |
|--------|-------------|
| `set_project_propery(project_name, project_root)` | **Required first**. Set project name and root directory |
| `add_ai_reading_guide()` | Add AI reading instructions to reduce hallucinations |
| `add_project_summary(project_summary, most_core_source_code_file_list)` | Add project summary with core file AST metadata |
| `add_file_dependencies(file_list)` | Analyze and add file dependency graph |
| `auto_merge_from_python_project_some_files()` | Auto-merge README.md, setup.py, pyproject.toml |
| `merge_from_files(file_list, as_title)` | Merge specific files |
| `merge_from_dir(relative_dir_name, as_title, ...)` | Merge entire directory with filters |
| `merge_from_files_with_metadata(...)` | Advanced merge with metadata control |
| `show_textfile_info()` | Display generated file statistics |

#### merge_from_dir Parameters

```python
.merge_from_dir(
    relative_dir_name="src",           # Directory relative to project_root
    as_title="Source Code",            # Section title in markdown
    project_root=None,                 # Override project root (optional)
    should_include_suffixes=[".py"],   # File extensions to include
    excluded_dir_name_list=[],         # Directories to exclude
    excluded_file_name_list=[],        # Files to exclude
    use_gitignore=True,                # Respect .gitignore rules
    dry_run=False,                     # Preview mode (no actual generation)
    include_ast_metadata=True,         # Include Python AST metadata
)
```

### GitHub Helper Functions

| Function | Description |
|----------|-------------|
| `gen_github_proj_docs_and_codes_ai_md(...)` | Generate docs from GitHub repo with separate docs/codes directories |
| `gen_github_proj_all_dirs_ai_md(...)` | Generate docs from entire GitHub repo |

## 🎨 Generated Markdown Structure

````markdown
# 🤖 AI Reading Guide for Project: my_project
(Instructions for AI models)

# markdown content namespace: my_project project summary
(Project description)

## 📋 my_project most core source files metadata
(AST metadata for core files - no source code)

## 🔗 my_project File Dependencies Analysis
(Import relationships and dependency graph)

# markdown content namespace: my_project Source Code

## my_project File Tree (relative dir: `src`)
(Directory tree)

## my_project Included Files (total: X files)
(File list)

--- **start of file: src/main.py** (project: my_project) ---
### 📄 Python File Metadata: `src/main.py`
(AST metadata)

```python
(Full source code)
```

--- **end of file: src/main.py** (project: my_project) ---
````

## 🐍 Python AST Metadata Extraction

For Python files, automatically extracts:
- Module docstrings
- Import statements
- Class definitions (name, bases, decorators, docstring, methods, properties, class variables)
- Function definitions (name, parameters with types/defaults, return type, decorators, docstring)
- Constructor (`__init__`) details

## 🔒 Security

- Automatically respects `.gitignore` rules when `use_gitignore=True`
- Excludes hidden directories (starting with `.`)
- Supports manual exclusion of sensitive directories/files

## 🎯 Use Cases

1. **AI Code Review** - Let AI analyze entire project for quality, security, performance
2. **RAG Knowledge Base** - Import structured project docs into vector databases
3. **Project Documentation** - Generate comprehensive project overview for new team members
4. **Learning Open Source** - Quickly understand GitHub project architecture with AI assistance

## 🔗 Links

- **GitHub**: https://github.com/ydf0509/nb_ai_context
- **PyPI**: https://pypi.org/project/nb_ai_context/
- **Issues**: https://github.com/ydf0509/nb_ai_context/issues

## 📄 License

MIT License

---

# nb_ai_context vs repomix: Professional Analysis on Reducing AI Hallucinations

- `nb_ai_context` is a byproduct of `nb_path`. `AiMdGenerator` inherits from `NbPath`, so it also supports infinite chainable operations, making it easy for users to chain-merge multiple folder sources into one markdown.  
  However, `nb_ai_context` has now been separated out because generating AI context is harder, more complex, and requires more skill than file path operations.

- `repomix` is the top-tier third-party library for packaging IT project code into a single file, but **`nb_ai_context` surpasses `repomix` in almost every aspect**.
- `nb_ai_context` uses Python code with infinite chainable operations, supporting various methods - much more flexible than repomix's command-line approach. For example, it supports custom important AI prompt engineering.  
  `nb_ai_context` allows users to specify the most important core file list via `most_core_source_code_file_list`, helping AI clearly understand the core APIs of third-party packages or your project. `nb_ai_context` Support adding custom AI prompt words through project_stummary input parameter.
- Users can verify whether `nb_ai_context` is really powerful or if the author is just bragging. The file `ai_md_files_demo/nb_ai_context_all_docs_and_codes.md` in this project was generated by `nb_ai_context`.  
  You can upload `nb_ai_context_all_docs_and_codes.md` to `Google AI Studio` and let AI help you master how to use `nb_ai_context` - see if AI can learn how to use an obscure third-party package without prior training.

## Core Design Philosophy Comparison

### nb_ai_context
**Designed specifically to reduce AI hallucinations**, with multiple targeted features explicitly mentioned in the documentation:
- Detailed AI reading guide (explicitly tells AI how to understand document structure)
- Strict file boundary markers (clearly identifies start/end of each file)
- AST metadata extraction (lets AI understand code structure before seeing source code)
- Project dependency analysis (helps AI understand inter-module relationships)
- Forced path verification (requires AI to verify file paths exist when suggesting code changes)

### repomix
**Mainly focused on codebase aggregation**, with the design goal of converting codebases into a single text file:
- Simple file separation markers
- Basic file filtering capability
- Preserves original code structure
- Lacks deep design specifically for AI understanding and reducing hallucinations

## Key Feature Comparison for Reducing AI Hallucinations

| Feature | nb_ai_context | repomix |
|---------|---------------|---------|
| **AI Reading Guide** | ✅ Detailed guide explicitly telling AI how to understand document structure | ❌ Basically none |
| **File Boundary Identification** | ✅ Strict project name + path identification to prevent file confusion | ⚠️ Simple file separators |
| **Code Structure Preview** | ✅ AST metadata extraction (class/function signatures, docstrings) | ❌ None, shows source code directly |
| **Dependency Analysis** | ✅ Visualizes inter-module dependencies, helps AI understand architecture | ❌ None |
| **Core Entry Point Identification** | ✅ Clearly identifies core files and entry points | ❌ None |
| **Path Verification Requirements** | ✅ Explicit instructions requiring AI to verify file paths | ❌ No explicit guidance |
| **Project Summary** | ✅ Structured project overview helps AI quickly grasp key points | ⚠️ Limited description capability |
| **Hidden/Sensitive File Handling** | ✅ Supports .gitignore and manual exclusion of sensitive content | ⚠️ Basic filtering |

## Practical Effect Comparison

When providing context generated by these tools to AI models:

### nb_ai_context Advantages
1. **Reduces file path hallucinations**: By forcing AI to "check file paths" and "verify file paths exist in the File Tree", it nearly eliminates the problem of AI fabricating non-existent files
2. **Reduces architectural misunderstanding**: Through dependency graphs and AST metadata, AI more easily understands overall project architecture and won't incorrectly assume inter-module relationships
3. **Precise code references**: Strictly marked file boundaries enable AI to accurately reference specific files and line numbers when answering
4. **More comprehensive context understanding**: Project summaries and core file analysis help AI quickly grasp project focus instead of getting lost in details

### repomix Limitations
1. **Blurred boundaries**: Simple file separators may cause AI to confuse content from different files
2. **Lack of guidance**: No explicit instructions on how AI should interpret document structure, increasing hallucination risk
3. **Insufficient deep understanding**: Directly exposes complete source code without providing code structure preview, making it difficult for AI to quickly grasp project architecture

## Conclusion: nb_ai_context is Significantly Stronger at Reducing AI Hallucinations

nb_ai_context is not just a code aggregation tool, but **a context optimization system specifically designed for AI-code interaction**. It explicitly targets "reducing hallucinations" as a core goal, repeatedly emphasizing in the documentation:

> ⚠️ Important Notes
> 1. **Do NOT hallucinate**: Only reference code, classes, functions, and APIs that actually exist in this document
> 2. **Check file paths**: When suggesting code changes, always verify the file path exists in the File Tree
> 3. **Respect the project structure**: The File Tree shows the actual directory layout

While repomix is more of a general code aggregation tool without deep design specifically targeting AI hallucination issues. For scenarios requiring high-quality AI code understanding, review, or generation, nb_ai_context provides a more professional solution.

If you're preparing code context for AI systems, especially in enterprise applications or security-sensitive scenarios, nb_ai_context's professional design will significantly reduce the risk of AI producing dangerous hallucinations.

---

**nb_ai_context** - Let AI truly understand your code 🚀

`````

--- **end of file: README.md** (project: nb_ai_context) --- 

---


--- **start of file: pyproject.toml** (project: nb_ai_context) --- 

`````text
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "nb_ai_context"
version = "1.5"
description = "非常强力的对任意it项目生成ai上下文单个markdown文档，丢给大模型或者知识库，非常强力，大模型幻觉大幅度减少。尤其是对python项目还有专门的ast语法树解析"
keywords = ["ai", "ai context", "llm", "rag", "python","ast","ast metadata","ai context generator","markdown"]
authors = [
    {name = "ydf0509", email = "ydf0509@xxx.com"},
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]
dependencies = [
    "typing_extensions>=3.7; python_version < '3.8'",
    "nb_path",
    "nb_log",
]

[project.optional-dependencies]
test = [
    "pytest>=6.0",
    "pytest-asyncio>=0.14",
]
dev = [
    "black>=21.0",
    "flake8>=3.8",
    "mypy>=0.812",
]

[project.urls]
Homepage = "https://github.com/ydf0509/nb_ai_context"
Repository = "https://github.com/ydf0509/nb_ai_context"
Issues = "https://github.com/ydf0509/nb_ai_context/issues"

[tool.setuptools.packages.find]
where = ["."]
include = ["nb_ai_context*"]

[tool.setuptools.package-data]
nb_ai_context = ["py.typed", "contrib/README.md"]

`````

--- **end of file: pyproject.toml** (project: nb_ai_context) --- 

---

# markdown content namespace: nb_ai_context examples 


## nb_ai_context File Tree (relative dir: `examples`)


`````

└── examples
    ├── AiMdGenerator_example.py
    └── generate_nb_log_ai_context.py

`````

---


## nb_ai_context (relative dir: `examples`)  Included Files (total: 2 files)


- `examples/AiMdGenerator_example.py`

- `examples/generate_nb_log_ai_context.py`


---


--- **start of file: examples/AiMdGenerator_example.py** (project: nb_ai_context) --- 


### 📄 Python File Metadata: `examples/AiMdGenerator_example.py`

#### 📦 Imports

- `from nb_ai_context import AiMdGenerator`


---

`````python
from nb_ai_context import AiMdGenerator


project_name = "nb_ai_context"
project_root = rf"D:\codes\{project_name}"

project_summary = f"""
- `{project_name}` is a powerful ai llm context gennerator library ,it is uesd for ai llm and rag
- `AiMdGenerator(...)` is the main class to create ai context for llm.
"""


(
    AiMdGenerator(
        rf"D:\codes\nb_ai_context\ai_md_files_demo\{project_name}_all_docs_and_codes.md"
    )
    .set_project_propery(project_name=project_name, project_root=project_root)
    .ensure_parent()
    .clear_text()
    .add_ai_reading_guide()  # 添加 AI 阅读指南，帮助 AI 更好地理解文档结构
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_ai_context/__init__.py",
            "nb_ai_context/ai_md_generator.py",
            "nb_ai_context/contrib/gen_github_proj_ai_md.py",
        ],
    )
    .auto_merge_from_python_project_some_files()
    .show_textfile_info()
    .merge_from_dir(
        relative_dir_name='examples',
        use_gitignore=True,
        as_title=f"{project_name} examples",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .show_textfile_info()
)

`````

--- **end of file: examples/AiMdGenerator_example.py** (project: nb_ai_context) --- 

---


--- **start of file: examples/generate_nb_log_ai_context.py** (project: nb_ai_context) --- 


### 📄 Python File Metadata: `examples/generate_nb_log_ai_context.py`

#### 📦 Imports

- `from nb_ai_context import AiMdGenerator`
- `from nb_log import get_logger`


---

`````python

from nb_ai_context import AiMdGenerator
from nb_log import get_logger

get_logger("nb_path")

project_name = "nb_log"
project_root = rf"D:\codes\{project_name}"

project_summary = """
- `nb_log` is a powerful logging library for Python. 

- `nb_log.get_logger(...)` is the main function to get a logger object.

"""

ai_md = AiMdGenerator(
    r"D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files\nb_log_all_docs_and_codes.md"
).set_project_propery(project_name=project_name, project_root=project_root)


(
    ai_md.clear_text()
    .add_ai_reading_guide()
    .add_project_summary(
        project_summary=project_summary,
        most_core_source_code_file_list=[
            "nb_log/__init__.py",
            "nb_log/log_manager.py",
            "nb_log/nb_log_config_default.py",
        ],
    )
    .merge_from_dir(
        project_root=r"D:\codes\nb_log_readdocs",
        relative_dir_name=r"source\articles",
        use_gitignore=True,
        as_title=f"{project_name} docs",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
    )
    .merge_from_dir(
        relative_dir_name=project_name,
        use_gitignore=True,
        as_title=f"{project_name} codes",
        # 只包含 .py 和 .md 文件
        should_include_suffixes=[".py", ".md"],
        # 排除 __pycache__ 目录和特定的测试文件
        excluded_dir_name_list=[],
        include_ast_metadata=True,
    )
    .get_textfile_info(is_show_info=True)
)

`````

--- **end of file: examples/generate_nb_log_ai_context.py** (project: nb_ai_context) --- 

---

# markdown content namespace: nb_ai_context codes 


## nb_ai_context File Tree (relative dir: `nb_ai_context`)


`````

└── nb_ai_context
    ├── __init__.py
    ├── ai_md_generator.py
    └── contrib
        ├── about.md
        └── gen_github_proj_ai_md.py

`````

---


## nb_ai_context (relative dir: `nb_ai_context`)  Included Files (total: 4 files)


- `nb_ai_context/ai_md_generator.py`

- `nb_ai_context/__init__.py`

- `nb_ai_context/contrib/about.md`

- `nb_ai_context/contrib/gen_github_proj_ai_md.py`


---


--- **start of file: nb_ai_context/ai_md_generator.py** (project: nb_ai_context) --- 


### 📄 Python File Metadata: `nb_ai_context/ai_md_generator.py`

#### 📦 Imports

- `import typing`
- `import os`
- `import fnmatch`
- `import ast`
- `from nb_path import NbPath`
- `import astor`

#### 🏛️ Classes (1)

##### 📌 `class AiMdGenerator(NbPath)`
*Line: 10*

**Docstring:**
`````
An extremely powerful context generator born for AI collaboration.

This class is designed to revolutionize how developers interact with Large Language
Models (LLMs). It intelligently merges multiple project source files into a single,
well-structured, and context-rich Markdown file, providing the AI with a perfect
and comprehensive project snapshot.

Key Features:
1.  **AI Reading Guide**: `add_ai_reading_guide()` adds instructions for AI models
    to better understand the document structure and avoid hallucinations.
2.  **Project Summary with Core Files Metadata**: `add_project_summary()` extracts
    AST metadata from core files without full source code, helping AI quickly
    grasp the project architecture.
3.  **File Dependencies Analysis**: `add_file_dependencies()` analyzes import
    relationships between files, showing entry points and core modules.
4.  **Smart File Merging**: `merge_from_dir()` and `merge_from_files()` with
    .gitignore support, file filtering, and AST metadata extraction.
5.  **Clear File Boundaries**: Each file is marked with project name and path
    for easy identification by AI models.

Main Public Methods:
- `set_project_propery(project_name, project_root)`: Set project info (required first)
- `add_ai_reading_guide()`: Add AI reading instructions to reduce hallucinations
- `add_project_summary(project_summary, most_core_source_code_file_list)`: Add summary with core file metadata
- `add_file_dependencies(file_list)`: Analyze and add file dependency graph
- `auto_merge_from_python_project_some_files()`: Auto-merge README, setup.py, pyproject.toml
- `merge_from_files(file_list, as_title)`: Merge specific files
- `merge_from_dir(dir_name, as_title, ...)`: Merge entire directory with filters
- `merge_from_files_with_metadata(file_list, as_title, include_ast_metadata, include_file_text)`: Advanced merge with metadata control

Example:
    >>> from nb_ai_context import AiMdGenerator
    >>> 
    >>> project_name = "my_project"
    >>> project_root = r"D:\codes\my_project"
    >>> 
    >>> (
    ...     AiMdGenerator(rf"D:\ai_docs\{project_name}_for_ai.md")
    ...     .set_project_propery(project_name=project_name, project_root=project_root)
    ...     .clear_text()
    ...     .add_ai_reading_guide()  # Add AI reading instructions
    ...     .add_project_summary(
    ...         project_summary="This is my awesome project...",
    ...         most_core_source_code_file_list=[
    ...             "src/main.py",
    ...             "src/api.py",
    ...         ]
    ...     )
    ...     .auto_merge_from_python_project_some_files()
    ...     .merge_from_dir(
    ...         relative_dir_name="src",
    ...         as_title=f"{project_name} Source Code",
    ...         use_gitignore=True,
    ...         should_include_suffixes=[".py", ".md"],
    ...         include_ast_metadata=True,
    ...     )
    ...     .show_textfile_info()
    ... )
`````

**Public Methods (9):**
- `def set_project_propery(self, project_name: str, project_root: typing.Union[os.PathLike, str]) -> 'AiMdGenerator'`
  - *Sets the project name for the current markdown file.*
- `def add_ai_reading_guide(self) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  添加 AI 阅读指南，帮助 AI 大模型更好地理解文档结构
  
  建议在 clear_text() 之后、add_project_summary() 之前调用
  `````
- `def add_project_summary(self, project_summary: str, most_core_source_code_file_list: typing.List[str] = None, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  Adds a project summary to the current markdown file.
  
  Args:
      project_summary: 项目概述文本
      project_root: 项目根目录（如果提供了 most_core_source_code_file_list）
      most_core_source_code_file_list: 最核心的源码文件列表（相对路径）
                                       只提取这些文件的 AST 元数据，不包含完整源码
  
  Example:
      >>> (
      ...     AiMdGenerator("output.md")
      ...     .set_project_name("my_project")
      ...     .clear_text()
      ...     .add_project_summary(
      ...         project_summary="这是一个优秀的项目...",
      ...         project_root="/path/to/project",
      ...         most_core_source_code_file_list=["src/main.py", "src/api.py"],
      ...     )
      ... )
  `````
- `def auto_merge_from_python_project_some_files(self, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - *自动合并项目根目录下的 readme.md 或者ReADME.md 以及setup.py 和 pyproject.toml ，如果有就添加*
- `def merge_from_files(self, relative_file_name_list: typing.List[str], as_title: str, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  Merges the content of the given files into the current markdown file.
  the current markdown file will be used to upload to ai model for code review and learning.
  `````
- `def merge_from_dir(self, relative_dir_name: str, as_title: str, project_root: typing.Union[os.PathLike, str] = None, should_include_suffixes: typing.List[str] = [], excluded_dir_name_list: typing.List[str] = [], excluded_file_name_list: typing.List[str] = [], use_gitignore: bool = True, dry_run: bool = False, include_ast_metadata: bool = True) -> 'AiMdGenerator'`
  - *Merges the content of the given directory into the current file.*
- `def merge_dir_of_package_examples(self)`
  - *合并包的examples目录到当前markdown文件*
- `def merge_from_files_with_metadata(self, relative_file_name_list: typing.List[str], as_title: str, project_root: typing.Union[os.PathLike, str] = None, include_ast_metadata: bool = True, include_file_text: bool = True) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  合并文件内容到 Markdown，对于 Python 文件会额外生成 AST 元数据
  
  Args:
      project_root: 项目根目录
      relative_file_name_list: 相对文件路径列表
      as_title: 标题
      include_ast_metadata: 是否包含 AST 元数据（仅对 .py 文件）
      include_file_text: 是否包含完整文件源码（False 时只显示元数据）
  `````
- `def add_file_dependencies(self, file_list: typing.List[str] = None, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator'`
  - **Docstring:**
  `````
  分析并添加项目文件之间的依赖关系到 markdown
  
  Args:
      file_list: 要分析的文件列表（相对路径），如果为 None 则分析整个项目
      project_root: 项目根目录
      
  Example:
      >>> (
      ...     AiMdGenerator("output.md")
      ...     .set_project_propery("my_project", "/path/to/project")
      ...     .clear_text()
      ...     .add_project_summary(project_summary="...")
      ... )
  `````

**Class Variables (1):**
- `suffix__lang_map = {'.py': 'python', '.md': 'markdown', '.txt': 'text...`


---

`````python
import typing
import os
import fnmatch
import ast

from nb_path import NbPath

FILE_CONTENT_BACKQUOTES = "`````"  # 不用反三引号是为了避免与被合并的如果本身就是.md文件的里面的反三引号冲突，导致文件块提前判断结束

class AiMdGenerator(NbPath):
    """
    An extremely powerful context generator born for AI collaboration.

    This class is designed to revolutionize how developers interact with Large Language
    Models (LLMs). It intelligently merges multiple project source files into a single,
    well-structured, and context-rich Markdown file, providing the AI with a perfect
    and comprehensive project snapshot.

    Key Features:
    1.  **AI Reading Guide**: `add_ai_reading_guide()` adds instructions for AI models
        to better understand the document structure and avoid hallucinations.
    2.  **Project Summary with Core Files Metadata**: `add_project_summary()` extracts
        AST metadata from core files without full source code, helping AI quickly
        grasp the project architecture.
    3.  **File Dependencies Analysis**: `add_file_dependencies()` analyzes import
        relationships between files, showing entry points and core modules.
    4.  **Smart File Merging**: `merge_from_dir()` and `merge_from_files()` with
        .gitignore support, file filtering, and AST metadata extraction.
    5.  **Clear File Boundaries**: Each file is marked with project name and path
        for easy identification by AI models.

    Main Public Methods:
    - `set_project_propery(project_name, project_root)`: Set project info (required first)
    - `add_ai_reading_guide()`: Add AI reading instructions to reduce hallucinations
    - `add_project_summary(project_summary, most_core_source_code_file_list)`: Add summary with core file metadata
    - `add_file_dependencies(file_list)`: Analyze and add file dependency graph
    - `auto_merge_from_python_project_some_files()`: Auto-merge README, setup.py, pyproject.toml
    - `merge_from_files(file_list, as_title)`: Merge specific files
    - `merge_from_dir(dir_name, as_title, ...)`: Merge entire directory with filters
    - `merge_from_files_with_metadata(file_list, as_title, include_ast_metadata, include_file_text)`: Advanced merge with metadata control

    Example:
        >>> from nb_ai_context import AiMdGenerator
        >>> 
        >>> project_name = "my_project"
        >>> project_root = r"D:\\codes\\my_project"
        >>> 
        >>> (
        ...     AiMdGenerator(rf"D:\\ai_docs\\{project_name}_for_ai.md")
        ...     .set_project_propery(project_name=project_name, project_root=project_root)
        ...     .clear_text()
        ...     .add_ai_reading_guide()  # Add AI reading instructions
        ...     .add_project_summary(
        ...         project_summary="This is my awesome project...",
        ...         most_core_source_code_file_list=[
        ...             "src/main.py",
        ...             "src/api.py",
        ...         ]
        ...     )
        ...     .auto_merge_from_python_project_some_files()
        ...     .merge_from_dir(
        ...         relative_dir_name="src",
        ...         as_title=f"{project_name} Source Code",
        ...         use_gitignore=True,
        ...         should_include_suffixes=[".py", ".md"],
        ...         include_ast_metadata=True,
        ...     )
        ...     .show_textfile_info()
        ... )
    """

    """cn description
    一个极其强大的、为 AI 协作而生的上下文生成器。

    此类旨在彻底改变开发者与大语言模型（LLM）的交互方式。它能够智能地将多个项目源文件
    合并成一个结构清晰、上下文丰富的单一 Markdown 文件，从而为 AI 提供一个完美、全面的项目快照。

    核心功能：
    1.  **AI 阅读指南**：`add_ai_reading_guide()` 为 AI 模型添加阅读说明，帮助其更好地
        理解文档结构，减少幻觉。
    2.  **项目概述与核心文件元数据**：`add_project_summary()` 从核心文件中提取 AST 元数据
        （不含完整源码），帮助 AI 快速掌握项目架构。
    3.  **文件依赖分析**：`add_file_dependencies()` 分析文件间的 import 依赖关系，
        展示入口文件和核心模块。
    4.  **智能文件合并**：`merge_from_dir()` 和 `merge_from_files()` 支持 .gitignore、
        文件过滤和 AST 元数据提取。
    5.  **清晰的文件边界**：每个文件都标记了项目名和路径，方便 AI 模型识别。

    主要公开方法：
    - `set_project_propery(project_name, project_root)`: 设置项目信息（必须首先调用）
    - `add_ai_reading_guide()`: 添加 AI 阅读指南以减少幻觉
    - `add_project_summary(project_summary, most_core_source_code_file_list)`: 添加项目概述和核心文件元数据
    - `add_file_dependencies(file_list)`: 分析并添加文件依赖图
    - `auto_merge_from_python_project_some_files()`: 自动合并 README、setup.py、pyproject.toml
    - `merge_from_files(file_list, as_title)`: 合并指定文件
    - `merge_from_dir(dir_name, as_title, ...)`: 合并整个目录（支持过滤）
    - `merge_from_files_with_metadata(...)`: 高级合并，可控制元数据和源码

    """

    suffix__lang_map = {
        ".py": "python",
        ".md": "markdown",
        ".txt": "text",
        ".json": "json",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".xml": "xml",
        ".html": "html",
        ".css": "css",
        ".js": "javascript",
        ".ts": "typescript",
        ".jsx": "javascript",
        ".tsx": "typescript",
        ".vue": "vue",
        ".php": "php",
        ".java": "java",
        ".c": "c",
        ".cpp": "cpp",
        ".h": "h",
        ".hpp": "hpp",
        ".cs": "csharp",
        ".vb": "vb",
        ".sql": "sql",
        ".bat": "batch",
        ".sh": "shell",
        ".ps1": "powershell",
        ".psm1": "powershell",
        ".psd1": "powershell",
        ".pssc": "powershell",
        ".psscx": "powershell",
    }

    def set_project_propery(self, project_name: str, project_root: typing.Union[os.PathLike, str] ) -> "AiMdGenerator":
        """Sets the project name for the current markdown file."""
        self.project_name = project_name
        self.project_root = project_root
        return self
    
    def _check_project_name(self) -> "AiMdGenerator":
        """Checks if the project name is set."""
        if not hasattr(self, 'project_name'):
            raise ValueError("Project name is not set. Please call set_project_name() first.")
        return self

    def add_ai_reading_guide(self) -> "AiMdGenerator":
        """
        添加 AI 阅读指南，帮助 AI 大模型更好地理解文档结构
        
        建议在 clear_text() 之后、add_project_summary() 之前调用
        """
        self._check_project_name()
        guide = f"""# 🤖 AI Reading Guide for Project: {self.project_name}

> **Important Notice for AI Models**: This document contains the complete source code and documentation for the `{self.project_name}` project. Please read this guide carefully before analyzing the content.

## 📖 Document Structure

This markdown document is structured as follows:

1. **Project Summary** (`# markdown content namespace: xxx project summary`)
   - Brief project description
   - Core source files metadata (AST-parsed class/function signatures without full source code)
   - File dependencies analysis

2. **Project Root Files** (`# markdown content namespace: xxx Project Root Dir Some Files`)
   - README.md, pyproject.toml, setup.py, etc.

3. **Source Code Sections** (`# markdown content namespace: xxx codes/examples/...`)
   - File Tree: Shows directory structure
   - Included Files: Lists all files in this section
   - Full source code with AST metadata for Python files

## 🔍 How to Identify File Boundaries

- Each file starts with: `--- **start of file: <path>** (project: {self.project_name}) ---`
- Each file ends with: `--- **end of file: <path>** (project: {self.project_name}) ---`
- All file paths are relative to the project root

## ⚠️ Important Notes

1. **Do NOT hallucinate**: Only reference code, classes, functions, and APIs that actually exist in this document
2. **Check file paths**: When suggesting code changes, always verify the file path exists in the File Tree
3. **Respect the project structure**: The File Tree shows the actual directory layout
4. **AST Metadata**: Python files include parsed metadata (imports, classes, methods) before the full source code

---

"""
        self.append_text(guide)
        return self

    def add_project_summary(
        self, 
        project_summary: str, 
        most_core_source_code_file_list: typing.List[str] = None,
        project_root: typing.Union[os.PathLike, str] = None,
    ) -> "AiMdGenerator":
        """
        Adds a project summary to the current markdown file.
        
        Args:
            project_summary: 项目概述文本
            project_root: 项目根目录（如果提供了 most_core_source_code_file_list）
            most_core_source_code_file_list: 最核心的源码文件列表（相对路径）
                                             只提取这些文件的 AST 元数据，不包含完整源码
        
        Example:
            >>> (
            ...     AiMdGenerator("output.md")
            ...     .set_project_name("my_project")
            ...     .clear_text()
            ...     .add_project_summary(
            ...         project_summary="这是一个优秀的项目...",
            ...         project_root="/path/to/project",
            ...         most_core_source_code_file_list=["src/main.py", "src/api.py"],
            ...     )
            ... )
        """
        self._check_project_name()
        project_root =  project_root or self.project_root 
        str_list = [f"# markdown content namespace: {self.project_name} project summary \n\n"]
        str_list.append(project_summary)
        # str_list.append("\n---\n\n")
        
        # 如果提供了核心文件列表，提取它们的元数据（不包含源码）
        if most_core_source_code_file_list and project_root:
            # str_list.append("\n---\n\n")
            str_list.append(f"\n## 📋 {self.project_name} most core source files metadata (Entry Points)\n\n")
            str_list.append(f"以下是项目 {self.project_name} 最核心的入口文件的结构化元数据，帮助快速理解项目架构：\n\n")
            most_core_source_code_file_list_str = ''
            for relative_file_name in most_core_source_code_file_list:
                most_core_source_code_file_list_str += f"- `{relative_file_name}`\n"
            str_list.append(f'\n### the project {self.project_name} most core source code files as follows: \n{most_core_source_code_file_list_str}')
            
            
            project_root_path = NbPath(project_root).resolve()
            
            for relative_file_name in most_core_source_code_file_list:
                file = (project_root_path / relative_file_name).resolve()
                if not file.exists():
                    raise FileNotFoundError(f"File {file} not found.")

                if file.is_file() and file.is_text() and file.suffix == ".py":
                    relative_file_name_posix = file.relative_to(project_root_path).as_posix()
                    
                    self.logger.info(f"提取核心文件元数据（无源码）: {relative_file_name_posix}")
                    
                    # 只提取元数据，不包含源码
                    metadata = self._parse_python_file_ast(file)
                    metadata_md = self._format_py_metadata_as_markdown(metadata, relative_file_name_posix)
                    str_list.append(metadata_md)
                    str_list.append("\n")
        
        self.append_text('\n'.join(str_list))
        self.add_file_dependencies(most_core_source_code_file_list)
        return self

    def _generate_markdown_header(self, as_title: str, file_text_list: list) -> list:
        """生成包含文件树和文件列表的 Markdown 头部"""
        str_list = [f"# markdown content namespace: {as_title} \n\n"]
        
        # 从文件列表中提取公共目录前缀，用于显示相对目录信息
        if file_text_list:
            all_paths = [item[1] for item in file_text_list]
            # 找出公共目录前缀
            if all_paths:
                first_parts = all_paths[0].split('/')
                common_prefix_parts = []
                for i, part in enumerate(first_parts[:-1]):  # 不包括文件名
                    if all(p.split('/')[i] == part if i < len(p.split('/')) else False for p in all_paths):
                        common_prefix_parts.append(part)
                    else:
                        break
                relative_dir = '/'.join(common_prefix_parts) if common_prefix_parts else '.'
            else:
                relative_dir = '.'
        else:
            relative_dir = '.'

        # 1. 生成文件树
        str_list.append(f"## {self.project_name} File Tree (relative dir: `{relative_dir}`)\n\n")
        str_list.append(f"{FILE_CONTENT_BACKQUOTES}\n")
        tree = {}
        sorted_paths = sorted([item[1] for item in file_text_list])
        for path in sorted_paths:
            parts = path.split('/')
            current_level = tree
            for part in parts:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

        def format_tree(node, prefix=""):
            lines = []
            entries = sorted(node.keys())
            for i, entry in enumerate(entries):
                connector = "├── " if i < len(entries) - 1 else "└── "
                lines.append(f"{prefix}{connector}{entry}")
                if node[entry]:
                    extension = "│   " if i < len(entries) - 1 else "    "
                    lines.extend(format_tree(node[entry], prefix + extension))
            return lines

        str_list.extend(format_tree(tree))
        str_list.append(f"\n{FILE_CONTENT_BACKQUOTES}\n\n---\n\n")

        # 2. 生成文件列表
        str_list.append(f"## {self.project_name} (relative dir: `{relative_dir}`)  Included Files (total: {len(file_text_list)} files)\n\n")
        for _, relative_file_name_posix, _, _ in file_text_list:
            str_list.append(f"- `{relative_file_name_posix}`\n")
        str_list.append("\n---\n\n")

        return str_list

    def auto_merge_from_python_project_some_files(self, project_root: typing.Union[os.PathLike, str] = None) -> 'AiMdGenerator':
        """自动合并项目根目录下的 readme.md 或者ReADME.md 以及setup.py 和 pyproject.toml ，如果有就添加"""
        self._check_project_name()
        project_root =  project_root or self.project_root
        file_merge_list = []
        
        # 定义要查找的根目录文件
        root_files_to_check = [
            "README.md",
            # "readme.md",
            "setup.py",
            "pyproject.toml"
        ]
        
        # 检查每个文件是否存在，如果存在则添加到合并列表中
        project_root_path = NbPath(project_root).resolve()
        for filename in root_files_to_check:
            file_path = project_root_path / filename
            if file_path.is_file() and file_path.is_text():
                file_merge_list.append(filename)
                
        self.merge_from_files(file_merge_list, f"{self.project_name} Project Root Dir Some Files",project_root, )
        return self

    def merge_from_files(
        self,
        relative_file_name_list: typing.List[str],
        as_title: str,
        project_root: typing.Union[os.PathLike, str] = None,
    ) -> "AiMdGenerator":
        """Merges the content of the given files into the current markdown file.
        the current markdown file will be used to upload to ai model for code review and learning.
        """
        self._check_project_name()
        project_root =  project_root or self.project_root
        file_text_list = []
        project_root_path = NbPath(project_root).resolve()
        for relative_file_name in relative_file_name_list:
            file = (project_root_path / relative_file_name).resolve()
            if not file.exists():
                raise FileNotFoundError(f"File {file} not found.")
            if file.is_file() and file.is_text():
                relative_file_name_posix = file.relative_to(
                    project_root_path
                ).as_posix()
                try:
                    text = file.read_text()
                except Exception as e:
                    self.logger.error(f"Error reading file {file}: {e}")
                    text = ""
                file_text_list.append(
                    [file, relative_file_name_posix, file.suffix, text]
                )
                self.logger.debug(f"need merged file: {file}")
            else:
                raise ValueError(f"File {file} is not a text file.")
        str_list = []
        if file_text_list:
            # 调用新函数生成头部
            str_list.extend(self._generate_markdown_header(as_title, file_text_list))


        for file, relative_file_name_posix, suffix, text in file_text_list:
            # 2. Remove the debug print statement.
            # print(f'file: {file}, relative_file_name_posix: {relative_file_name_posix}, suffix: {suffix}, text: {text}')
            str_list.append(f"--- **start of file: {relative_file_name_posix}** (project: {self.project_name}) --- \n")
            # 3. Handle .md files separately to ensure their content is rendered correctly.
            #    Other file types are wrapped in code blocks.
            # if suffix == ".md":
            #     str_list.append(text + "\n")
            # else:
            #     lang = self.suffix__lang_map.get(suffix, "text")
            #     str_list.append(f"{FILE_CONTENT_BACKQUOTES}{lang}\n{text}\n{FILE_CONTENT_BACKQUOTES}\n")
            lang = self.suffix__lang_map.get(suffix, "text")
            str_list.append(f"{FILE_CONTENT_BACKQUOTES}{lang}\n{text}\n{FILE_CONTENT_BACKQUOTES}\n")

            str_list.append(f"--- **end of file: {relative_file_name_posix}** (project: {self.project_name}) --- \n")
            str_list.append("---\n\n")

        # with self.open(mode="a", encoding="utf-8") as f:
        #     f.write("\n".join(str_list))
        self.append_text('\n'.join(str_list))
        self.ensure_utf8_bom()
        return self
        
        
    def merge_from_dir(
        self,
        relative_dir_name: str,
        as_title: str,
        project_root: typing.Union[os.PathLike, str] = None,
        should_include_suffixes: typing.List[str] = [],
        excluded_dir_name_list: typing.List[str] = [],
        excluded_file_name_list: typing.List[str] = [],
        use_gitignore: bool = True,
        dry_run: bool = False,
        include_ast_metadata: bool = True,
    ) -> "AiMdGenerator":
        """Merges the content of the given directory into the current file."""
        project_root =  project_root or self.project_root
        project_root_path = NbPath(project_root).resolve()
        target_dir_path = (project_root_path / relative_dir_name).resolve()
        if not target_dir_path.exists():
            raise FileNotFoundError(f"Directory {target_dir_path} not found.")

        # Use sets for efficient lookups
        excluded_dir_paths = {
            (project_root_path / d).resolve() for d in excluded_dir_name_list
        }
        excluded_file_paths = {
            (project_root_path / f).resolve() for f in excluded_file_name_list
        }

        ignore_patterns = []
        if use_gitignore:
            try:
                gitignore_path = project_root_path.find_git_root() / ".gitignore"
                if gitignore_path.is_file():
                    self.logger.debug(f"Using .gitignore rules from: {gitignore_path}")
                    with open(gitignore_path, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith("#"):
                                # Gitignore patterns always use forward slashes.
                                # We will compare against the posix version of the relative path
                                # for cross-platform reliability.
                                ignore_patterns.append(line)
            except FileNotFoundError:
                self.logger.warning("use_gitignore is True, but no .git/ or .gitignore file found.")

        relative_paths_to_include = []
        for path_obj in target_dir_path.rglob("*"):
            # Automatically exclude directories starting with a dot at the project root
            try:
                first_part = path_obj.relative_to(project_root_path).parts[0]
                if first_part.startswith('.'):
                    continue
            except (ValueError, IndexError):
                continue
            # Check if the path is within any of the excluded directories
            is_in_excluded_dir = any(
                path_obj == excluded_dir or excluded_dir in path_obj.parents
                for excluded_dir in excluded_dir_paths
            )
            if is_in_excluded_dir:
                continue

            # Check if the path matches any gitignore patterns.
            # Convert the relative path to a posix-style string for reliable matching.
            relative_to_root = path_obj.relative_to(project_root_path)
            relative_posix_path = relative_to_root.as_posix()
            # Use fnmatch for robust gitignore-style pattern matching.
            is_ignored = False
            for p in ignore_patterns:
                # If a pattern does not contain a slash, it matches in any directory.
                # e.g., 'test_git_ignore1.py' should match 'nb_path/example_dir/test_git_ignore1.py'
                if '/' not in p.strip('/'):
                    p_glob = f"**/{p.strip('/')}"
                else:
                    p_glob = p
                if fnmatch.fnmatch(relative_posix_path, p_glob) or fnmatch.fnmatch(relative_posix_path, p):
                    is_ignored = True
                    break
            if is_ignored:
                self.logger.debug(f"Ignoring {relative_to_root} due to .gitignore rule.")
                continue

            if path_obj.is_file():
                # Check if the file itself is excluded
                if path_obj.resolve() in excluded_file_paths:
                    continue
                # Check if the file is a text file
                if not path_obj.is_text():
                    continue
                # Check if the suffix is in the inclusion list (if the list is not empty)
                if (
                    should_include_suffixes
                    and path_obj.suffix not in should_include_suffixes
                ):
                    continue
                relative_paths_to_include.append(
                    path_obj.relative_to(project_root_path).as_posix()
                )

        if dry_run:
            print("\n--- [DRY RUN] AiMdGenerator Execution Plan ---")
            print(f"\n✅ {len(relative_paths_to_include)} files would be INCLUDED in '{self.name}':")
            for p in sorted(relative_paths_to_include):
                print(f"  - {p}")
            print("\n--- End of DRY RUN ---")
            return self
        else:
            # 使用带元数据的方法
            return self.merge_from_files_with_metadata(
                 
                relative_paths_to_include, 
                as_title,
                project_root=project_root,
                include_ast_metadata=include_ast_metadata
            )

    def merge_dir_of_package_examples(self):
        """合并包的examples目录到当前markdown文件"""
        self._check_project_name()
        self.merge_from_dir(
            relative_dir_name=self.project_name,
            use_gitignore=True,
            as_title=f"{self.project_name} codes",
            # 只包含 .py 和 .md 文件
            should_include_suffixes=[".py", ".md"],
            # 排除 __pycache__ 目录和特定的测试文件
            excluded_dir_name_list=[],
        ).merge_from_dir(
            relative_dir_name="examples",
            use_gitignore=True,
            as_title=f"{self.project_name} examples",
            # 只包含 .py 和 .md 文件
            should_include_suffixes=[".py", ".md"],
            # 排除 __pycache__ 目录和特定的测试文件
            excluded_dir_name_list=[],
            include_ast_metadata=False,
        )
        return self

    def _ast_to_source(self, node) -> str:
        """将 AST 节点转换为源代码字符串，兼容 Python 3.7+"""
        if node is None:
            return ""
        try:
            # Python 3.9+ 支持 ast.unparse
            if hasattr(ast, 'unparse'):
                return ast.unparse(node)
            else:
                # Python 3.7/3.8 的回退方案
                # 尝试使用 astor
                try:
                    import astor
                    return astor.to_source(node).strip()
                except ImportError:
                    pass
                
                # 简单的手工处理常见情况
                if isinstance(node, ast.Name):
                    return node.id
                elif isinstance(node, ast.Constant):
                    return repr(node.value)
                elif isinstance(node, ast.Attribute):
                    value = self._ast_to_source(node.value)
                    return f"{value}.{node.attr}"
                elif isinstance(node, ast.Subscript):
                    value = self._ast_to_source(node.value)
                    slice_val = self._ast_to_source(node.slice)
                    return f"{value}[{slice_val}]"
                elif isinstance(node, (ast.List, ast.Tuple)):
                    elts = [self._ast_to_source(e) for e in node.elts]
                    if isinstance(node, ast.List):
                        return f"[{', '.join(elts)}]"
                    else:
                        return f"({', '.join(elts)})"
                else:
                    # 对于复杂类型，返回类型名称
                    return node.__class__.__name__
        except Exception:
            return ""

    def _parse_type_annotation(self, annotation) -> str:
        """解析类型注解，返回字符串表示"""
        return self._ast_to_source(annotation)

    def _extract_function_metadata(self, node: typing.Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> dict:
        """提取函数/方法的元数据"""
        metadata = {
            "name": node.name,
            "type": "async_function" if isinstance(node, ast.AsyncFunctionDef) else "function",
            "lineno": node.lineno,
            "docstring": ast.get_docstring(node) or "",
            "parameters": [],
            "return_type": self._parse_type_annotation(node.returns),
            "decorators": [self._ast_to_source(dec) for dec in node.decorator_list],
            "is_public": not node.name.startswith("_"),
        }

        # 提取参数信息
        for arg in node.args.args:
            param_info = {
                "name": arg.arg,
                "type": self._parse_type_annotation(arg.annotation),
                "default": None,
            }
            metadata["parameters"].append(param_info)

        # 处理默认参数
        defaults = node.args.defaults
        if defaults:
            # 默认值从后往前对应参数
            num_defaults = len(defaults)
            for i, default in enumerate(defaults):
                param_idx = len(metadata["parameters"]) - num_defaults + i
                if param_idx >= 0:
                    try:
                        metadata["parameters"][param_idx]["default"] = self._ast_to_source(default)
                    except Exception:
                        metadata["parameters"][param_idx]["default"] = "<complex_default>"

        # 处理 *args 和 **kwargs
        if node.args.vararg:
            metadata["parameters"].append({
                "name": f"*{node.args.vararg.arg}",
                "type": self._parse_type_annotation(node.args.vararg.annotation),
                "default": None,
            })
        if node.args.kwarg:
            metadata["parameters"].append({
                "name": f"**{node.args.kwarg.arg}",
                "type": self._parse_type_annotation(node.args.kwarg.annotation),
                "default": None,
            })

        return metadata

    def _extract_class_metadata(self, node: ast.ClassDef) -> dict:
        """提取类的元数据"""
        metadata = {
            "name": node.name,
            "type": "class",
            "lineno": node.lineno,
            "docstring": ast.get_docstring(node) or "",
            "bases": [self._ast_to_source(base) for base in node.bases],
            "decorators": [self._ast_to_source(dec) for dec in node.decorator_list],
            "methods": [],
            "properties": [],
            "class_variables": [],
            "is_public": not node.name.startswith("_"),
        }

        # 遍历类的成员
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                method_info = self._extract_function_metadata(item)
                
                # 检查是否是 property
                is_property = any("property" in dec for dec in method_info["decorators"])
                if is_property:
                    metadata["properties"].append(method_info)
                else:
                    metadata["methods"].append(method_info)
            
            elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                # 类变量（带类型注解）
                value_str = ""
                if item.value:
                    try:
                        value_str = self._ast_to_source(item.value)
                        # 限制值的长度
                        if len(value_str) > 50:
                            value_str = value_str[:50] + "..."
                    except Exception:
                        value_str = "<value>"
                
                metadata["class_variables"].append({
                    "name": item.target.id,
                    "type": self._parse_type_annotation(item.annotation),
                    "value": value_str,
                    "lineno": item.lineno,
                })
            elif isinstance(item, ast.Assign):
                # 类变量（无类型注解）
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        # 提取值
                        value_str = ""
                        if item.value:
                            try:
                                value_str = self._ast_to_source(item.value)
                                # 限制值的长度
                                if len(value_str) > 50:
                                    value_str = value_str[:50] + "..."
                            except Exception:
                                value_str = "<value>"
                        
                        metadata["class_variables"].append({
                            "name": target.id,
                            "type": "",
                            "value": value_str,
                            "lineno": item.lineno,
                        })

        return metadata

    def _parse_python_file_ast(self, file_path: NbPath) -> dict:
        """解析 Python 文件的 AST，提取所有元数据"""
        try:
            source_code = file_path.read_text(encoding="utf-8")
            # 移除 BOM (Byte Order Mark) 字符，如果存在的话
            # BOM 是 U+FEFF，在 UTF-8 编码中是 \ufeff
            if source_code.startswith('\ufeff'):
                source_code = source_code[1:]
                self.logger.debug(f"Removed BOM from file: {file_path}")
            tree = ast.parse(source_code, filename=str(file_path))
        except Exception as e:
            self.logger.error(f"Failed to parse Python file {file_path}: {e}")
            return {
                "error": str(e),
                "classes": [],
                "functions": [],
                "imports": [],
                "module_docstring": "",
            }

        metadata = {
            "file": str(file_path),
            "module_docstring": ast.get_docstring(tree) or "",
            "classes": [],
            "functions": [],
            "imports": [],
            "constants": [],
        }

        # 遍历模块级别的节点
        for node in ast.walk(tree):
            # 只处理模块级别的定义（通过检查父节点）
            if isinstance(node, ast.ClassDef):
                # 检查是否是顶级类（不在其他类内部）
                parent = None
                for potential_parent in ast.walk(tree):
                    if isinstance(potential_parent, ast.ClassDef) and node in ast.walk(potential_parent) and node != potential_parent:
                        parent = potential_parent
                        break
                if parent is None:  # 顶级类
                    metadata["classes"].append(self._extract_class_metadata(node))

            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # 检查是否是顶级函数（不在类内部）
                parent_class = None
                for potential_parent in ast.walk(tree):
                    if isinstance(potential_parent, ast.ClassDef) and node in ast.walk(potential_parent):
                        parent_class = potential_parent
                        break
                if parent_class is None:  # 顶级函数
                    metadata["functions"].append(self._extract_function_metadata(node))

            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        metadata["imports"].append({
                            "type": "import",
                            "module": alias.name,
                            "alias": alias.asname,
                            "lineno": node.lineno,
                        })
                else:  # ImportFrom
                    module = node.module or ""
                    for alias in node.names:
                        metadata["imports"].append({
                            "type": "from_import",
                            "module": module,
                            "name": alias.name,
                            "alias": alias.asname,
                            "lineno": node.lineno,
                        })

        return metadata

    def _format_py_metadata_as_markdown(self, metadata: dict, relative_file_name: str) -> str:
        """将 Python 文件元数据格式化为 Markdown"""
        lines = []
        lines.append(f"\n### 📄 Python File Metadata: `{relative_file_name}`\n")

        # 模块文档字符串
        if metadata.get("module_docstring"):
            lines.append("#### 📝 Module Docstring\n")
            lines.append(FILE_CONTENT_BACKQUOTES)
            lines.append(metadata["module_docstring"])
            lines.append(f"{FILE_CONTENT_BACKQUOTES}\n")

        # 导入信息
        if metadata.get("imports"):
            lines.append("#### 📦 Imports\n")
            for imp in metadata["imports"]:  # 显示所有 imports，不再限制数量
                if imp["type"] == "import":
                    alias_str = f" as {imp['alias']}" if imp['alias'] else ""
                    lines.append(f"- `import {imp['module']}{alias_str}`")
                else:
                    alias_str = f" as {imp['alias']}" if imp['alias'] else ""
                    lines.append(f"- `from {imp['module']} import {imp['name']}{alias_str}`")
            lines.append("")

        # 类信息
        if metadata.get("classes"):
            lines.append(f"#### 🏛️ Classes ({len(metadata['classes'])})\n")
            for cls in metadata["classes"]:
                # 只显示公有类或所有类（根据需要）
                class_header = f"##### 📌 `class {cls['name']}"
                if cls["bases"]:
                    class_header += f"({', '.join(cls['bases'])})"
                class_header += "`"
                lines.append(class_header)
                lines.append(f"*Line: {cls['lineno']}*\n")
                
                if cls["docstring"]:
                    # 显示完整的类文档字符串
                    docstring_lines = cls["docstring"].split("\n")
                    lines.append("**Docstring:**")
                    lines.append(FILE_CONTENT_BACKQUOTES)
                    lines.extend(docstring_lines)
                    lines.append(f"{FILE_CONTENT_BACKQUOTES}\n")

                # 首先单独显示 __init__ 方法（非常重要）
                init_method = None
                for method in cls["methods"]:
                    if method["name"] == "__init__":
                        init_method = method
                        break
                
                if init_method:
                    lines.append("**🔧 Constructor (`__init__`):**")
                    params_str = self._format_parameters(init_method["parameters"])
                    lines.append(f"- `def __init__({params_str})`")
                    
                    # 显示 __init__ 的完整文档字符串
                    if init_method["docstring"]:
                        lines.append("  - **Docstring:**")
                        lines.append(f"  {FILE_CONTENT_BACKQUOTES}")
                        for doc_line in init_method["docstring"].split("\n"):
                            lines.append(f"  {doc_line}")
                        lines.append(f"  {FILE_CONTENT_BACKQUOTES}")
                    
                    # 显示每个参数的详细信息
                    if init_method["parameters"]:
                        lines.append("  - **Parameters:**")
                        for param in init_method["parameters"]:
                            param_name = param["name"]
                            param_type = f": {param['type']}" if param["type"] else ""
                            param_default = f" = {param['default']}" if param["default"] else ""
                            lines.append(f"    - `{param_name}{param_type}{param_default}`")
                    lines.append("")

                # 公有方法（排除 __init__）
                public_methods = [m for m in cls["methods"] if m["is_public"] and m["name"] != "__init__"]
                if public_methods:
                    lines.append(f"**Public Methods ({len(public_methods)}):**")
                    for method in public_methods:
                        params_str = self._format_parameters(method["parameters"])
                        return_str = f" -> {method['return_type']}" if method["return_type"] else ""
                        async_str = "async " if method["type"] == "async_function" else ""
                        
                        decorators_str = ""
                        if method["decorators"]:
                            decorators_str = " " + " ".join([f"`{d}`" for d in method["decorators"]])
                        
                        lines.append(f"- `{async_str}def {method['name']}({params_str}){return_str}`{decorators_str}")
                        
                        # 显示完整的文档字符串
                        if method["docstring"]:
                            # 如果文档字符串只有一行，用简短格式显示
                            docstring_lines = method["docstring"].split("\n")
                            if len(docstring_lines) == 1:
                                lines.append(f"  - *{method['docstring'].strip()}*")
                            else:
                                # 多行文档字符串,用代码块格式显示
                                lines.append("  - **Docstring:**")
                                lines.append(f"  {FILE_CONTENT_BACKQUOTES}")
                                for doc_line in docstring_lines:
                                    lines.append(f"  {doc_line}")
                                lines.append(f"  {FILE_CONTENT_BACKQUOTES}")
                    lines.append("")

                # Properties
                if cls["properties"]:
                    lines.append(f"**Properties ({len(cls['properties'])}):**")
                    for prop in cls["properties"]:
                        return_str = f" -> {prop['return_type']}" if prop["return_type"] else ""
                        lines.append(f"- `@property {prop['name']}{return_str}`")
                    lines.append("")

                # 类变量
                if cls["class_variables"]:
                    lines.append(f"**Class Variables ({len(cls['class_variables'])}):**")
                    for var in cls["class_variables"]:
                        type_str = f": {var['type']}" if var["type"] else ""
                        value_str = f" = {var['value']}" if var.get("value") else ""
                        lines.append(f"- `{var['name']}{type_str}{value_str}`")
                    lines.append("")

        # 顶级函数
        if metadata.get("functions"):
            public_functions = [f for f in metadata["functions"] if f["is_public"]]
            if public_functions:
                lines.append(f"#### 🔧 Public Functions ({len(public_functions)})\n")
                for func in public_functions:
                    params_str = self._format_parameters(func["parameters"])
                    return_str = f" -> {func['return_type']}" if func["return_type"] else ""
                    async_str = "async " if func["type"] == "async_function" else ""
                    
                    decorators_str = ""
                    if func["decorators"]:
                        decorators_str = " " + " ".join([f"`{d}`" for d in func["decorators"]])
                    
                    lines.append(f"- `{async_str}def {func['name']}({params_str}){return_str}`{decorators_str}")
                    lines.append(f"  - *Line: {func['lineno']}*")
                    
                    if func["docstring"]:
                        # 如果文档字符串只有一行，用简短格式显示
                        docstring_lines = func["docstring"].split("\n")
                        if len(docstring_lines) == 1:
                            lines.append(f"  - *{func['docstring'].strip()}*")
                        else:
                            # 多行文档字符串,用代码块格式显示
                            lines.append("  - **Docstring:**")
                            lines.append(f"  {FILE_CONTENT_BACKQUOTES}")
                            for doc_line in docstring_lines:
                                lines.append(f"  {doc_line}")
                            lines.append(f"  {FILE_CONTENT_BACKQUOTES}")
                    lines.append("")

        lines.append("\n---\n")
        return "\n".join(lines)

    def _format_parameters(self, parameters: list) -> str:
        """格式化函数参数列表"""
        param_strs = []
        for param in parameters:
            param_str = param["name"]
            if param["type"]:
                param_str += f": {param['type']}"
            if param["default"]:
                param_str += f" = {param['default']}"
            param_strs.append(param_str)
        return ", ".join(param_strs)

    def merge_from_files_with_metadata(
        self,
        relative_file_name_list: typing.List[str],
        as_title: str,
        project_root: typing.Union[os.PathLike, str] = None,
        include_ast_metadata: bool = True,
        include_file_text: bool = True,
    ) -> "AiMdGenerator":
        """
        合并文件内容到 Markdown，对于 Python 文件会额外生成 AST 元数据
        
        Args:
            project_root: 项目根目录
            relative_file_name_list: 相对文件路径列表
            as_title: 标题
            include_ast_metadata: 是否包含 AST 元数据（仅对 .py 文件）
            include_file_text: 是否包含完整文件源码（False 时只显示元数据）
        """
        self._check_project_name()
        project_root =  project_root or self.project_root
        file_text_list = []
        project_root_path = NbPath(project_root).resolve()
        
        for relative_file_name in relative_file_name_list:
            file = (project_root_path / relative_file_name).resolve()
            if not file.exists():
                raise FileNotFoundError(f"File {file} not found.")
            if file.is_file() and file.is_text():
                relative_file_name_posix = file.relative_to(project_root_path).as_posix()
                try:
                    text = file.read_text()
                except Exception as e:
                    self.logger.error(f"Error reading file {file}: {e}")
                    text = ""
                
                file_text_list.append([file, relative_file_name_posix, file.suffix, text])
                self.logger.debug(f"need merged file: {file}")
            else:
                raise ValueError(f"File {file} is not a text file.")
        
        str_list = []
        if file_text_list:
            str_list.extend(self._generate_markdown_header(as_title, file_text_list))

        for file, relative_file_name_posix, suffix, text in file_text_list:
            # 如果不包含文件内容，只输出元数据（仅对 Python 文件）
            if not include_file_text:
                if suffix == ".py" and include_ast_metadata:
                    # 只显示元数据，不显示源码
                    metadata = self._parse_python_file_ast(file)
                    metadata_md = self._format_py_metadata_as_markdown(metadata, relative_file_name_posix)
                    str_list.append(metadata_md)
                    str_list.append("\n")
                # 非 Python 文件跳过
                continue
            
            # 正常流程：包含文件内容
            str_list.append(f"--- **start of file: {relative_file_name_posix}** (project: {self.project_name}) --- \n")
            
            # 对于 Python 文件，添加 AST 元数据
            if suffix == ".py" and include_ast_metadata:
                metadata = self._parse_python_file_ast(file)
                metadata_md = self._format_py_metadata_as_markdown(metadata, relative_file_name_posix)
                str_list.append(metadata_md)
            
            # 添加完整的文件内容
            lang = self.suffix__lang_map.get(suffix, "text")
            str_list.append(f"{FILE_CONTENT_BACKQUOTES}{lang}\n{text}\n{FILE_CONTENT_BACKQUOTES}\n")

            str_list.append(f"--- **end of file: {relative_file_name_posix}** (project: {self.project_name}) --- \n")
            str_list.append("---\n\n")

        self.append_text('\n'.join(str_list))
        self.ensure_utf8_bom()
        return self

    def _analyze_file_dependencies(
        self, 
        file_list: typing.List[str], 
        project_root: typing.Union[os.PathLike, str] = None
    ) -> dict:
        """
        分析项目文件之间的 import 依赖关系
        
        Args:
            file_list: 相对文件路径列表
            project_root: 项目根目录
            
        Returns:
            dict: {
                "internal_deps": {file: [依赖的项目内文件列表]},
                "external_deps": {file: [外部依赖模块列表]},
                "reverse_deps": {file: [被哪些文件依赖]}
            }
        """
        project_root = project_root or self.project_root
        project_root_path = NbPath(project_root).resolve()
        
        # 构建项目内模块名到文件路径的映射
        # 例如: "nb_ai_context.ai_md_generator" -> "nb_ai_context/ai_md_generator.py"
        module_to_file = {}
        file_to_module = {}
        
        for relative_file in file_list:
            if relative_file.endswith('.py'):
                # 将文件路径转换为模块名
                module_name = relative_file.replace('/', '.').replace('\\', '.')
                if module_name.endswith('.py'):
                    module_name = module_name[:-3]
                if module_name.endswith('.__init__'):
                    module_name = module_name[:-9]
                
                module_to_file[module_name] = relative_file
                file_to_module[relative_file] = module_name
                
                # 也添加各级父模块的映射
                parts = module_name.split('.')
                for i in range(1, len(parts)):
                    parent_module = '.'.join(parts[:i])
                    parent_file = '/'.join(parts[:i]) + '/__init__.py'
                    if parent_file in file_list:
                        module_to_file[parent_module] = parent_file
        
        internal_deps = {}  # 项目内部依赖
        external_deps = {}  # 外部依赖
        reverse_deps = {}   # 反向依赖（被谁依赖）
        
        # 初始化
        for f in file_list:
            internal_deps[f] = []
            external_deps[f] = set()
            reverse_deps[f] = []
        
        # 分析每个 Python 文件的 imports
        for relative_file in file_list:
            if not relative_file.endswith('.py'):
                continue
                
            file_path = project_root_path / relative_file
            if not file_path.exists():
                continue
                
            try:
                source_code = file_path.read_text(encoding='utf-8')
                if source_code.startswith('\ufeff'):
                    source_code = source_code[1:]
                tree = ast.parse(source_code)
            except Exception as e:
                self.logger.warning(f"无法解析文件 {relative_file}: {e}")
                continue
            
            current_module = file_to_module.get(relative_file, '')
            # 对于 __init__.py 文件，它本身就是包，current_package 应该等于 current_module
            # 对于普通 .py 文件，current_package 是其父目录对应的模块
            if relative_file.endswith('__init__.py'):
                current_package = current_module
            else:
                current_package = '.'.join(current_module.split('.')[:-1]) if '.' in current_module else ''
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        module_name = alias.name
                        self._categorize_import(
                            module_name, relative_file, module_to_file,
                            internal_deps, external_deps, reverse_deps
                        )
                        
                elif isinstance(node, ast.ImportFrom):
                    module_name = node.module or ''
                    
                    # 处理相对导入
                    if node.level > 0:  # 相对导入
                        if current_package:
                            # 计算绝对模块名
                            # level=1 表示当前包，level=2 表示父包，以此类推
                            package_parts = current_package.split('.')
                            # 回退 level-1 级（level=1 时不回退，就是当前包）
                            levels_to_go_up = node.level - 1
                            if levels_to_go_up < len(package_parts):
                                base = '.'.join(package_parts[:len(package_parts) - levels_to_go_up])
                                if module_name:
                                    module_name = f"{base}.{module_name}"
                                else:
                                    module_name = base
                            else:
                                # 相对导入超出了包的层级，保持原样
                                if module_name:
                                    pass  # 保持 module_name 不变
                    
                    if module_name:
                        self._categorize_import(
                            module_name, relative_file, module_to_file,
                            internal_deps, external_deps, reverse_deps
                        )
        
        # 转换 set 为 list 并排序
        for f in external_deps:
            external_deps[f] = sorted(list(external_deps[f]))
        
        return {
            "internal_deps": internal_deps,
            "external_deps": external_deps,
            "reverse_deps": reverse_deps,
            "module_to_file": module_to_file
        }
    
    def _categorize_import(
        self, 
        module_name: str, 
        current_file: str,
        module_to_file: dict,
        internal_deps: dict,
        external_deps: dict,
        reverse_deps: dict
    ):
        """将 import 分类为内部依赖或外部依赖"""
        # 检查是否是项目内部模块
        found_internal = False
        
        # 尝试匹配完整模块名或其前缀
        parts = module_name.split('.')
        for i in range(len(parts), 0, -1):
            check_module = '.'.join(parts[:i])
            if check_module in module_to_file:
                dep_file = module_to_file[check_module]
                if dep_file != current_file and dep_file not in internal_deps[current_file]:
                    internal_deps[current_file].append(dep_file)
                    if dep_file in reverse_deps:
                        reverse_deps[dep_file].append(current_file)
                found_internal = True
                break
        
        if not found_internal:
            # 外部依赖，只记录顶级模块名
            top_module = parts[0]
            external_deps[current_file].add(top_module)
    
    def _format_dependencies_as_markdown(self, deps_info: dict, file_list: typing.List[str]) -> str:
        """将依赖关系格式化为 Markdown"""
        lines = []
        lines.append(f"\n## 🔗 {self.project_name} Some File Dependencies Analysis\n")
        lines.append("以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：\n")
        
        internal_deps = deps_info["internal_deps"]
        external_deps = deps_info["external_deps"]
        reverse_deps = deps_info["reverse_deps"]
        
        # 1. 依赖关系图（文本形式）
        lines.append("### 📊 Internal Dependencies Graph\n")
        lines.append(f"{FILE_CONTENT_BACKQUOTES}")
        
        # 找出入口文件（没有被其他文件依赖的文件）
        entry_files = [f for f in file_list if f.endswith('.py') and not reverse_deps.get(f, [])]
        if entry_files:
            lines.append("Entry Points (not imported by other project files):")
            for f in sorted(entry_files):
                lines.append(f"  ★ {f}")
            lines.append("")
        
        # 找出核心文件（被多个文件依赖的文件）
        core_files = [(f, len(reverse_deps.get(f, []))) for f in file_list if f.endswith('.py')]
        core_files = sorted(core_files, key=lambda x: x[1], reverse=True)
        core_files = [(f, count) for f, count in core_files if count > 0]
        
        if core_files:
            lines.append("Core Files (imported by other files, sorted by import count):")
            for f, count in core_files[:10]:  # 只显示前10个
                lines.append(f"  ◆ {f} (imported by {count} files)")
            lines.append("")
        
        lines.append(f"{FILE_CONTENT_BACKQUOTES}\n")
        
        # 2. 详细依赖列表
        lines.append("### 📋 Detailed Dependencies\n")
        
        py_files = sorted([f for f in file_list if f.endswith('.py')])
        
        for f in py_files:
            int_deps = internal_deps.get(f, [])
            rev_deps = reverse_deps.get(f, [])
            
            # 只显示有依赖关系的文件
            if int_deps or rev_deps:
                lines.append(f"#### `{f}`\n")
                
                if int_deps:
                    lines.append("**Imports from project:**")
                    for dep in sorted(int_deps):
                        lines.append(f"- `{dep}`")
                    lines.append("")
                
                if rev_deps:
                    lines.append("**Imported by:**")
                    for dep in sorted(rev_deps):
                        lines.append(f"- `{dep}`")
                    lines.append("")
        
        # 3. 外部依赖汇总
        all_external = set()
        for ext_list in external_deps.values():
            all_external.update(ext_list)
        
        if all_external:
            # 过滤掉标准库模块（Python 3.7+ 完整标准库列表）
            stdlib_modules = {
                # 文本处理
                'string', 'stringprep', 're', 'difflib', 'textwrap', 'unicodedata',
                # 二进制数据
                'struct', 'codecs',
                # 数据类型
                'datetime', 'zoneinfo', 'calendar', 'collections', 'heapq', 'bisect',
                'array', 'weakref', 'types', 'copy', 'pprint', 'reprlib', 'enum',
                'graphlib',
                # 数学和数字
                'numbers', 'math', 'cmath', 'decimal', 'fractions', 'random', 'statistics',
                # 函数式编程
                'itertools', 'functools', 'operator',
                # 文件和目录
                'pathlib', 'os', 'io', 'time', 'argparse', 'getopt', 'logging',
                'getpass', 'curses', 'platform', 'errno', 'ctypes',
                # 文件格式
                'csv', 'configparser', 'tomllib', 'netrc', 'plistlib',
                # 加密
                'hashlib', 'hmac', 'secrets',
                # 操作系统服务
                'os', 'io', 'time', 'argparse', 'getopt', 'logging', 'getpass',
                'curses', 'platform', 'errno', 'ctypes',
                # 并发
                'threading', 'multiprocessing', 'concurrent', 'subprocess', 'sched',
                'queue', '_thread',
                # 网络和进程间通信
                'asyncio', 'socket', 'ssl', 'select', 'selectors', 'signal',
                'mmap', 'asyncore', 'asynchat',
                # 互联网数据处理
                'email', 'json', 'mailbox', 'mimetypes', 'base64', 'binascii',
                'quopri', 'uu',
                # HTML 和 XML
                'html', 'xml',
                # 互联网协议
                'webbrowser', 'wsgiref', 'urllib', 'http', 'ftplib', 'poplib',
                'imaplib', 'smtplib', 'uuid', 'socketserver', 'xmlrpc', 'ipaddress',
                # 多媒体
                'wave', 'colorsys',
                # 国际化
                'locale', 'gettext',
                # 程序框架
                'turtle', 'cmd', 'shlex',
                # 图形界面
                'tkinter', 'idlelib',
                # 开发工具
                'typing', 'pydoc', 'doctest', 'unittest', 'test', '2to3', 'lib2to3',
                # 调试和性能
                'bdb', 'faulthandler', 'pdb', 'profile', 'timeit', 'trace',
                'tracemalloc', 'cProfile',
                # 软件打包和分发
                'distutils', 'ensurepip', 'venv', 'zipapp',
                # Python 运行时
                'sys', 'sysconfig', 'builtins', 'warnings', 'dataclasses',
                'contextlib', 'abc', 'atexit', 'traceback', 'gc', 'inspect',
                'site',
                # 自定义解释器
                'code', 'codeop',
                # 导入系统
                'importlib', 'pkgutil', 'modulefinder', 'runpy', 'zipimport',
                # Python 语言服务
                'ast', 'symtable', 'token', 'keyword', 'tokenize', 'tabnanny',
                'pyclbr', 'py_compile', 'compileall', 'dis', 'pickletools',
                # 文件归档
                'zipfile', 'tarfile', 'gzip', 'bz2', 'lzma', 'shutil',
                # 持久化
                'pickle', 'copyreg', 'shelve', 'marshal', 'dbm', 'sqlite3',
                # 文件通配
                'glob', 'fnmatch', 'linecache', 'filecmp', 'fileinput', 'tempfile',
                # 其他
                '__future__', 'rlcompleter', 'readline', 'posix', 'posixpath',
                'ntpath', 'genericpath', 'stat', 'grp', 'pwd', 'spwd', 'crypt',
                'termios', 'tty', 'pty', 'fcntl', 'resource', 'syslog',
                'aifc', 'sunau', 'chunk', 'imghdr', 'sndhdr', 'ossaudiodev',
                'typing_extensions',  # 虽然是第三方但通常被视为标准扩展
            }
            third_party = sorted([m for m in all_external if m not in stdlib_modules])
            
            if third_party:
                lines.append("### 📦 Third-party Dependencies\n")
                lines.append("项目使用的第三方库：\n")
                for m in third_party:
                    lines.append(f"- `{m}`")
                lines.append('- ......以及更多的第三方库......')
                lines.append("")
        
        lines.append("\n---\n")
        return "\n".join(lines)
    
    def add_file_dependencies(
        self,
        file_list: typing.List[str] = None,
        project_root: typing.Union[os.PathLike, str] = None,
    ) -> "AiMdGenerator":
        """
        分析并添加项目文件之间的依赖关系到 markdown
        
        Args:
            file_list: 要分析的文件列表（相对路径），如果为 None 则分析整个项目
            project_root: 项目根目录
            
        Example:
            >>> (
            ...     AiMdGenerator("output.md")
            ...     .set_project_propery("my_project", "/path/to/project")
            ...     .clear_text()
            ...     .add_project_summary(project_summary="...")
            ... )
        """
        self._check_project_name()
        project_root = project_root or self.project_root
        
        if file_list is None:
            # 如果没有指定文件列表，扫描整个项目的 .py 文件
            project_root_path = NbPath(project_root).resolve()
            file_list = []
            for py_file in project_root_path.rglob("*.py"):
                # 排除隐藏目录
                relative = py_file.relative_to(project_root_path)
                if not any(part.startswith('.') for part in relative.parts):
                    file_list.append(relative.as_posix())
        
        # 分析依赖
        deps_info = self._analyze_file_dependencies(file_list, project_root)
        
        # 格式化并添加到 markdown
        deps_md = self._format_dependencies_as_markdown(deps_info, file_list)
        self.append_text(deps_md)
        
        return self

`````

--- **end of file: nb_ai_context/ai_md_generator.py** (project: nb_ai_context) --- 

---


--- **start of file: nb_ai_context/__init__.py** (project: nb_ai_context) --- 


### 📄 Python File Metadata: `nb_ai_context/__init__.py`

#### 📦 Imports

- `from nb_path import NbPath`
- `from ai_md_generator import AiMdGenerator`
- `from contrib.gen_github_proj_ai_md import gen_github_proj_docs_and_codes_ai_md`
- `from contrib.gen_github_proj_ai_md import gen_github_proj_all_dirs_ai_md`


---

`````python

from nb_path import NbPath
from .ai_md_generator import AiMdGenerator

from .contrib.gen_github_proj_ai_md import gen_github_proj_docs_and_codes_ai_md,gen_github_proj_all_dirs_ai_md
`````

--- **end of file: nb_ai_context/__init__.py** (project: nb_ai_context) --- 

---


--- **start of file: nb_ai_context/contrib/about.md** (project: nb_ai_context) --- 

`````markdown


some contribution about nb_path
`````

--- **end of file: nb_ai_context/contrib/about.md** (project: nb_ai_context) --- 

---


--- **start of file: nb_ai_context/contrib/gen_github_proj_ai_md.py** (project: nb_ai_context) --- 


### 📄 Python File Metadata: `nb_ai_context/contrib/gen_github_proj_ai_md.py`

#### 📝 Module Docstring

`````
Generate tutorials and code from any GitHub project into a markdown file for AI context

Download GitHub project zip file
https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main
https://codeload.github.com/fastapi/sqlmodel/zip/refs/tags/0.0.25

Unzip the file
Generate markdown file
`````

#### 📦 Imports

- `import typing`
- `from nb_path import NbPath`
- `from nb_ai_context.ai_md_generator import AiMdGenerator`
- `import re`

#### 🔧 Public Functions (3)

- `def extract_repo_name(github_url)`
  - *Line: 18*

- `def gen_github_proj_docs_and_codes_ai_md(github_zip_url: str, output_md_path: str, docs_dir_name: str, codes_dir_name: str, readme_file: str, should_include_suffixes: list = None, excluded_dir_name_list: typing.List[str] = [], excluded_file_name_list: typing.List[str] = [])`
  - *Line: 27*
  - **Docstring:**
  `````
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
  `````

- `def gen_github_proj_all_dirs_ai_md(github_zip_url: str, output_md_path: str, should_include_suffixes: list = None, excluded_dir_name_list: typing.List[str] = [], excluded_file_name_list: typing.List[str] = [])`
  - *Line: 99*
  - *生成github的项目根目录下所有文件到markdown，*


---

`````python
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
from nb_ai_context.ai_md_generator import AiMdGenerator
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

`````

--- **end of file: nb_ai_context/contrib/gen_github_proj_ai_md.py** (project: nb_ai_context) --- 

---

