# nb_ai_context

**[English](README.md) | [中文](README_CN.md)**

[![PyPI version](https://img.shields.io/pypi/v/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![Python versions](https://img.shields.io/pypi/pyversions/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚀 **An extremely powerful AI context generator** - Merge any IT project into a single structured Markdown document for AI LLMs or RAG knowledge bases.

**🔥 God-tier Use Case: Chat with AI about your project anytime, anywhere** - Before leaving work or going on vacation, run `AiMdGenerator` to get a single merged markdown. You can then have precise conversations with AI about your project code while on the subway or before bed. You can't carry your programming computer everywhere, but your phone is with you 24/7. Upload the document to `Google AI Studio` - its code understanding and generation capabilities far surpass average programmers. Use natural language on your phone to effortlessly command your tens of thousands of lines of code.This is like a total game-changer: it gives someone with just a smartphone a wider perspective and far more flexible thinking than someone glued to their computer, obsessing over their IDE. This is what AI empowerment for programmers looks like at its ultimate level.

## What is nb_ai_context?

nb_ai_context is not simply merging project file code, it is a context optimization tool specifically designed for AI code interaction, with the core goal of reducing AI illusions.

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

### 🔥 God-tier Use Case Scenarios:

**Chat with AI about your project anytime, anywhere** - Before leaving work or going on vacation, run `AiMdGenerator` to get a single merged markdown. You can then have precise conversations with AI about your project code while on the subway or before bed. You can't carry your programming computer everywhere, but your phone is with you 24/7. Upload the document to `Google AI Studio` - its code understanding and generation capabilities far surpass average programmers. Use natural language on your phone to effortlessly command your tens of thousands of lines of code.This is like a total game-changer: it gives someone with just a smartphone a wider perspective and far more flexible thinking than someone glued to their computer, obsessing over their IDE. This is what AI empowerment for programmers looks like at its ultimate level.

#### What makes this workflow so satisfying?

**Scenario 1: "Code Review" on the Subway**
> *You're on the subway and suddenly think: "Hmm, is that `User` module I wrote this afternoon too tightly coupled with the `Order` module?"*
>
> **Action**: Open your phone and ask Gemini: "Based on the code I uploaded, analyze the coupling between the `User` class and `Order` class, and give me refactoring suggestions."
> **Result**: AI will reference your specific code line numbers and provide extremely professional refactoring solutions. You just nod: "Yeah, this approach is right, I'll make these changes first thing tomorrow morning." — **Commute time becomes high-value architecture thinking time.**

**Scenario 2: "Painless Reading" Before Bed**
> *You inherited a legacy codebase, spent all day looking at it with a headache, and still don't understand one core logic.*
>
> **Action**: Lying in bed, ask Gemini: "In the simplest language possible, explain how the `CoreEngine` class schedules tasks, and draw me a text-based flowchart."
> **Result**: AI acts like a patient mentor, breaking down the logic for you. You don't need to strain your eyes reading code - you understand it through the plain language explanation and can sleep peacefully.

**Scenario 3: Capturing Inspiration**
> *You're out shopping on the weekend and suddenly think of a new feature.*
>
> **Action**: Pull out your phone: "If I want to add a `WebSocket` push feature to the current project, which files need to be changed? Write me an MVP plan."
> **Result**: Based on your complete codebase, AI lists exactly which files to modify - `api.py`, `models.py` - and even drafts the approximate code. You screenshot it, and on Monday you can implement it directly with AI assistance.

#### **Summary:**

This workflow **transforms "writing code" (heavy physical labor) into "discussing architecture and logic" (light mental work).**

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

## Comparison with Similar Tools

In addition to the detailed comparison with repomix provided above, here is a concise table comparing key features:

| Tool | Context Completeness | Token Consumption | Security | Cost |
|------|---------------------|------------------|----------|------|
| **repomix** | ⚠️ Simple concatenation | ⚠️ Moderate | ⚠️ Basic filtering | 🆓 Free tool |
| **nb_ai_context** | ✅ Full structured context | ✅ AST metadata optimized | ✅ Automatic .gitignore support | 🆓 Free tool |

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
