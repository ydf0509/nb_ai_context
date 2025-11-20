# nb_ai_context

[![PyPI version](https://img.shields.io/pypi/v/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![Python versions](https://img.shields.io/pypi/pyversions/nb_ai_context.svg)](https://pypi.org/project/nb_ai_context/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🚀 **极其强大的 AI 上下文生成器** - 将任意 IT 项目合并生成为1个结构化 Markdown 文档，方便一次上传给ai大模型或者rag知识库。  

**`nb_ai_context` 生成的markdown文件 传给  `google ai studio` ，生成代码质量和准确率，远远吊打在 `cursor` `trae` `qoder` `gemini-code-assit` 等ai ide中写代码。**

<pre style="color: red;font-weight: bold;background-color:yellow;padding: 10px;border-radius: 5px;font-size: 16px;">
本人实测：
将 nb_ai_context 对项目教程+源码生成的单个markdown文件 传给 `google ai studio` 网页版
的1000k上下文+gemini 3.0pro 大模型，再提问让gemini写代码，代码生成的准确率和质量远远吊打在 
cursor trae qoder等ai ide或gemini-code-assit等 编程插件 里面提问写代码。

 `google ai studio` 优点是1000k上下文以及免费。唯一缺点是他在网页生成代码，而不是直接操作
 修改你的本地代码文件。

 `nb_ai_context` 生成的markdown丢给`google ai studio`完爆cursor trae等ide中写代码 
 主要原因是：  
`google ai studio` 网页版是全量阅读推理你上传的文件，而 ai编程ide 对长教程或者源码，
ai agent试图采取关键字搜索匹配再投喂上下文给ai大模型，（有时候模糊搜索的关键字压根搜不到内容，
因为ai造出来的关键字不是完完全全的匹配你的函数名字或者教程内容，所以就搜不到，
例如近义词，你代码用别的单词表示，ai却用自己的单词来表示，靠关键字压根就搜不到内容，agent咋投喂ai大模型？）
ai ide 这种方式简直是管中窥豹 一叶障目不见泰山。

最根本原因还是：  
ai ide 为了减少成本，防止token消耗大，不会全量把源码教程喂给ai大模型，不然的靠用户交的那20美元的月会员，
cursor要亏得裤衩没得穿。100万 tokens上下文输入，calude gemini gpt 价格大约是3美元，相当于20元人民币，
如果问一次就20元人民币，cursor每个月给你用8次就要开始亏血本了，(另外tokens输出价格远高于输入价格），
现在cursor还给你每月用500次，那他只能从节约tokens下手了，具体表现就是cursor不全量把所有教程和源码
发给ai大模型推理。

`nb_ai_context` 对大型编程项目的效果尤为突出，远远吊打 cursor trae qoder gemini-code-assit 等ai ide中写代码。
</pre>

## ✨ 核心特性

### 🎯 为什么需要 nb_ai_context？

当你想让 AI 大模型（如 ChatGPT、Claude）理解你的整个项目时，手动复制粘贴代码既繁琐又容易出错。`nb_ai_context` 彻底解决了这个痛点：

- ✅ **自动化合并** - 一键将整个项目合并为单个 Markdown 文件
- ✅ **结构化输出** - 包含文件树、文件边界、相对路径，AI 能完美理解项目架构
- ✅ **智能元数据提取** - 对 Python 项目提供 AST 语法树解析，自动生成类、函数、方法签名
- ✅ **安全可靠** - 内置 `.gitignore` 支持，自动排除敏感信息（API 密钥、.env 文件等）
- ✅ **灵活可控** - 支持文件过滤、目录排除、自定义文件类型
- ✅ **GitHub 项目支持** - 直接从 GitHub zip 下载地址生成文档

### 💡 **关键优势对比**
| 方案 | 上下文完整性 | Token 消耗 | 安全性 | 成本 |
|------|--------------|------------|--------|------|
| **Cursor/trae/qoder** | ❌ 分段阅读 | ⚠️ 高 | ⚠️ 需手动过滤 | 💰 付费次数限制 |
| **手动复制粘贴** | ❌ 易遗漏 | ❌ 极高 | ❌ 易泄露敏感信息 | ⏰ 耗时 |
| **nb_ai_context** | ✅ 完整结构化 | ✅ AST 元数据优化 | ✅ 自动 `.gitignore` | 🆓 免费工具 |



### 🎁 对 AI 大模型的巨大价值

1. **提供上帝视角** 📐
   - 清晰的文件树和文件边界
   - 完整的相对路径信息
   - AI 能轻松构建项目的整体架构图

2. **确保信息完整性** 📚
   - 未经删减的完整源码
   - 避免手动复制导致的格式混乱
   - 零上下文缺失，AI 分析更精准

3. **增强安全性** 🔒
   - 自动遵循 `.gitignore` 规则
   - 防止敏感信息泄露
   - 放心分享代码给 AI

4. **Python 项目专属优化** 🐍
   - AST 语法树解析
   - 自动提取类、函数、方法签名
   - 参数类型、返回值、装饰器一目了然

## 📦 安装

```bash
pip install nb_ai_context
```

**依赖项：**
- Python >= 3.7
- nb_path
- nb_log

## 🚀 快速开始

### 示例 1：为本地 Python 项目生成 AI 上下文

```python
from nb_ai_context import AiMdGenerator

project_name = "my_awesome_project"
project_root = r"D:\codes\my_awesome_project"

project_summary = f"""
- `{project_name}` 是一个优秀的 Python Web 应用
- 使用 FastAPI 框架
- 包含完整的用户认证和权限管理
"""

(
    AiMdGenerator(rf"D:\ai_docs\{project_name}_for_ai.md")
    .set_project_propery(project_name=project_name, project_root=project_root)
    .clear_text()  # 清空旧内容
    .add_project_summary(
        project_summary=project_summary,
        # 核心文件列表（只提取元数据，不包含完整源码）
        most_core_source_code_file_list=[
            "src/main.py",
            "src/api.py",
            "src/models.py",
        ],
    )
    .auto_merge_from_python_project_some_files()  # 自动包含 README.md、setup.py、pyproject.toml
    .merge_from_dir(
        relative_dir_name="src",
        as_title=f"{project_name} 源代码",
        use_gitignore=True,  # 使用 .gitignore 规则
        should_include_suffixes=[".py", ".md"],  # 只包含指定文件类型
        include_ast_metadata=True,  # 包含 AST 元数据
    )
    .merge_from_dir(
        relative_dir_name="tests",
        as_title=f"{project_name} 测试代码",
        use_gitignore=True,
        should_include_suffixes=[".py"],
        excluded_dir_name_list=["tests/temp"],  # 排除特定目录
        include_ast_metadata=True,
    )
    .show_textfile_info()  # 显示生成的文件信息
)
```

### 示例 2：从 GitHub 项目生成 AI 文档

```python
from nb_ai_context import gen_github_proj_docs_and_codes_ai_md
from nb_path import NbPath

# 生成 SQLModel 项目的文档和代码
gen_github_proj_docs_and_codes_ai_md(
    github_zip_url="https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main",
    output_md_path=r"D:\ai_docs\sqlmodel_all_docs_and_codes.md",
    readme_file="README.md",
    docs_dir_name="docs",  # 文档目录
    codes_dir_name="sqlmodel",  # 源码目录
    should_include_suffixes=[".py", ".md"],
    excluded_dir_name_list=["tests", "__pycache__"],
    excluded_file_name_list=["test_*.py"],
)
```

### 示例 3：生成 GitHub 项目的所有文件

```python
from nb_ai_context import gen_github_proj_all_dirs_ai_md

# 生成整个项目的所有文件
gen_github_proj_all_dirs_ai_md(
    github_zip_url="https://codeload.github.com/fastapi/sqlmodel/zip/refs/heads/main",
    output_md_path=r"D:\ai_docs\sqlmodel_all_files.md",
    should_include_suffixes=[".py", ".md", ".html"],
    excluded_dir_name_list=["node_modules", ".git", "__pycache__"],
)
```


## 为什么要这个 nb_ai_context ？脱了裤子放屁？让cusror trae 去阅读项目的源码和教程，还能在ide里面生成代码，这不更香吗？(预判质疑)

- 1. 有时候是非ide环境问项目的用法

- 2. cursor 太贵了，经常提问cursor浪费宝贵次数，要把宝贵次数留给真正的代码生成，而不是提问。
     cursor trae 存在上下文太短，调教成不积极阅读全量源码和教程等问题。

- 3. 可以作为 rag 在线知识库使用，让ai大模型阅读生成的markdown，然后回答问题。

- 4. 可以把生成的markdown丢给免费且上下文无敌高达1000k 的 `google ai studio` 去阅读，claude gpt才256k token，国内大模型才128k token，压根不够用，  
     只有  google ai studio + gemini 3.0pro 才能完整阅读项目源码加教程，并且免费使用。 

- 5. `google ai studio` 对于4M 以内的文件，可以一次性全量阅读全文+推理，并且免费使用。
     一般三方包项目的源码加教程远没有达到4M。
     如果是用户自己的真实项目而非框架或者三方包项目，项目中可能包含大量写法模式非常重复的需求代码，代码加教程加起来可能会超过4M，但是 用户项目核心公共入口函数和类的用法的源码 + 教程 绝对不超过1M。

- 6. `nb_ai_context` 支持按文件夹合并和过滤需要合并的文件，并且`nb_ai_context` 支持 `ast` 解析 任何python文件的 类 函数 入参 注释 等 元信息，大幅减少token消耗，让ai抓住重点。  
     `AiMdGenerator.add_project_summary(most_core_source_code_file_list=[...])` 支持添加项目概述和核心文件元数据，让ai快速抓住重点。  
     不管项目多复杂有几百个class类和模块，但真正能作为公共使用入口的模块一般不会超过10个。  
     例如 `funboost` 项目 `python`文件高达几百个，但真正能作为框架使用用户级别的公共使用入口的python文件也就三四个，其他的python文件压根没机会被终端用户直接import并使用。


- 10. 最最主要的原因！！！ cursor trae 内置的大模型都不乖乖阅读所有源码和教程，即使你明确发出指令强迫他阅读所有教程和源码，他也会偷懒不读，只读部分代码，导致幻觉率极高。
      为什么 cursor trae 里面的大模型不全量阅读呢，因为他早就预判了有流氓玩家恶意滥用大模型算力， 如果你让cursor + claude 阅读c盘下的所有文件，cursor和claude 会这么乖吗？
      c盘下的文本文件高达几百亿行，如果读完一次就会消耗价值几十万美元的tokens，大模型厂商亏得裤衩没得穿，你才20美元的包月会员，cursor和claude厂家不被你薅秃噜皮？
      所以不管用户怎么强迫cursor  trae去阅读所有源码和教程，cursor 和 claude 和trae都不会听你的话。

- 11. trae 和 cursor 被调教限制了， trae一次最多阅读200行，qoder一次最多阅读1000行，对超长教程，需要分多次阅读，导致幻觉率极高，你让这种 ai ide + 大模型去总结 项目的中心思想非常不靠谱。 
      并且分段阅读交互次数高达几十次，太费等待时间了。
      并且 ai ide里面阅读长文件会分批阅读直到20次就会自动停止，例如文件有10000行，trae一次阅读200行，需要50次交互，但ai ide设置了最多交互20次就会自动停止；这是因为担心流氓恶意用户让他阅读1亿行的文件导致自己血亏，所以最多分段阅读20次就会停止。

- 12. 解决 10和11的痛点问题， 只有 `google ai studio` 才能做到 ， 或者使用rag也勉强可以。
      把文档上传给 `google ai studio` 网页版的1000k上下文的gemini pro 这种方式最强， 其次是 `rag`方式。
      对 4M以内的文档（大约就是1000k tokens）， 推荐使用  `google ai studio`，不要使用 `rag` 方式。
      超过4M文档的上下文，突破了gemini 1000k token 上限，无法使用，此时需要使用 `rag`方式。

- 13. 一些网址：
       google ai studio 网址  [https://aistudio.google.com/](https://aistudio.google.com/)    
       智谱清言 ai智能体网址，可以支持免费rag  [chatglm.cn/main/gdetail/69168f75e8e6a00da25f55cc?lang=zh](chatglm.cn/main/gdetail/69168f75e8e6a00da25f55cc?lang=zh)    
       腾讯ima知识库 [ima.qq.com](https://ima.qq.com/)    



## 📖 核心 API 详解

### AiMdGenerator 类

`AiMdGenerator` 是核心类，继承自 `NbPath`，支持优雅的链式调用。

#### 主要方法

##### 1. `set_project_propery(project_name, project_root)`
设置项目名称和根目录（必须首先调用）

```python
.set_project_propery(
    project_name="my_project",
    project_root=r"D:\codes\my_project"
)
```

##### 2. `add_project_summary(project_summary, most_core_source_code_file_list)`
添加项目概述和核心文件元数据

```python
.add_project_summary(
    project_summary="项目描述...",
    most_core_source_code_file_list=[
        "src/main.py",  # 只提取这些文件的 AST 元数据，不包含完整源码
        "src/api.py",
    ]
)
```

##### 3. `auto_merge_from_python_project_some_files()`
自动合并项目根目录的关键文件（README.md、setup.py、pyproject.toml）

```python
.auto_merge_from_python_project_some_files()
```

##### 4. `merge_from_files(relative_file_name_list, as_title)`
合并指定文件列表

```python
.merge_from_files(
    relative_file_name_list=["docs/intro.md", "docs/api.md"],
    as_title="项目文档"
)
```

##### 5. `merge_from_dir()` ⭐ 最强大的方法
合并整个目录的文件

```python
.merge_from_dir(
    relative_dir_name="src",           # 相对目录名
    as_title="源代码",                  # 章节标题
    should_include_suffixes=[".py"],   # 包含的文件类型
    excluded_dir_name_list=[],         # 排除的目录列表
    excluded_file_name_list=[],        # 排除的文件列表
    use_gitignore=True,                # 使用 .gitignore 规则
    include_ast_metadata=True,         # 包含 Python AST 元数据
)
```

**参数说明：**
- `relative_dir_name`: 相对于项目根目录的路径
- `as_title`: 在生成的 Markdown 中的章节标题
- `should_include_suffixes`: 只包含这些后缀的文件（留空则包含所有文本文件）
- `excluded_dir_name_list`: 要排除的目录列表
- `excluded_file_name_list`: 要排除的文件列表
- `use_gitignore`: 是否遵循 `.gitignore` 规则（强烈推荐开启）
- `include_ast_metadata`: 对 Python 文件是否生成 AST 元数据
- `dry_run`: 预览模式，只显示将要包含的文件，不实际生成

##### 6. `merge_from_files_with_metadata()`
带元数据的文件合并（更高级的控制）

```python
.merge_from_files_with_metadata(
    relative_file_name_list=["src/main.py"],
    as_title="核心代码",
    include_ast_metadata=True,   # 是否包含 AST 元数据
    include_file_text=True,      # 是否包含完整源码
)
```

##### 7. `show_textfile_info()`
显示生成文件的统计信息

```python
.show_textfile_info()  # 打印文件大小、行数等信息
```

### GitHub 项目处理函数

#### `gen_github_proj_docs_and_codes_ai_md()`
生成 GitHub 项目的 README、文档和源码

```python
from nb_ai_context import gen_github_proj_docs_and_codes_ai_md

gen_github_proj_docs_and_codes_ai_md(
    github_zip_url="https://codeload.github.com/owner/repo/zip/refs/heads/main",
    output_md_path="output.md",
    readme_file="README.md",
    docs_dir_name="docs",
    codes_dir_name="src",
    should_include_suffixes=[".py", ".md"],
    excluded_dir_name_list=["tests"],
    excluded_file_name_list=["test_*.py"],
)
```

#### `gen_github_proj_all_dirs_ai_md()`
生成 GitHub 项目根目录下的所有文件

```python
from nb_ai_context import gen_github_proj_all_dirs_ai_md

gen_github_proj_all_dirs_ai_md(
    github_zip_url="https://codeload.github.com/owner/repo/zip/refs/heads/main",
    output_md_path="output_all.md",
    should_include_suffixes=[".py", ".java", ".go", ".md"],
    excluded_dir_name_list=["node_modules", ".git"],
)
```

## 🐍 Python AST 元数据提取

对于 Python 文件，`nb_ai_context` 会自动提取以下元数据：

### 提取内容
- ✅ **模块文档字符串**
- ✅ **导入语句** (import / from import)
- ✅ **类定义**
  - 类名、继承关系、装饰器
  - 类文档字符串
  - 公有方法（含参数类型、返回值、装饰器）
  - 属性 (@property)
  - 类变量
- ✅ **顶级函数**
  - 函数签名（参数类型、默认值、返回值）
  - 装饰器
  - 文档字符串
  - 异步函数标识

### 元数据示例输出

```markdown
### 📄 Python File Metadata: `src/main.py`

#### 📝 Module Docstring
```
这是主模块，包含应用的入口点
```

#### 📦 Imports
- `import os`
- `from typing import List, Optional`
- `from fastapi import FastAPI`

#### 🏛️ Classes (2)

##### 📌 `class UserService(BaseService)`
*Line: 15*

**Docstring:**
```
用户服务类，处理用户相关的业务逻辑
```

**Public Methods (3):**
- `def get_user(user_id: int) -> Optional[User]`
  - *获取用户信息*
- `async def create_user(name: str, email: str) -> User`
  - *创建新用户*
- `def update_user(user_id: int, **kwargs) -> bool`

**Properties (1):**
- `@property user_count -> int`

#### 🔧 Public Functions (2)
- `async def startup_event() -> None`
  - *Line: 120*
  - *应用启动事件处理*
```

## 🎨 生成的 Markdown 结构

生成的 Markdown 文档结构清晰，包含：

```markdown
# markdown content namespace: 项目概述

项目描述...

## 📋 Core Source Files Metadata (Entry Points)
核心文件的 AST 元数据（不含源码）

---

# markdown content namespace: 项目根目录文件

## File Tree
```
├── README.md
├── setup.py
└── pyproject.toml
```

## Included Files
- `README.md`
- `setup.py`
- `pyproject.toml`

---

--- **start of file: README.md** ---
（文件内容）
--- **end of file: README.md** ---

---

# markdown content namespace: 源代码

## File Tree
（文件树）

## Included Files
（文件列表）

--- **start of file: src/main.py** ---

### 📄 Python File Metadata: `src/main.py`
（AST 元数据）

```python
（完整源码）
```

--- **end of file: src/main.py** ---
```

## 🔧 高级用法

### 1. 预览模式（Dry Run）

```python
(
    AiMdGenerator("output.md")
    .set_project_propery("my_project", r"D:\codes\my_project")
    .merge_from_dir(
        relative_dir_name="src",
        as_title="源代码",
        dry_run=True,  # 只预览，不实际生成
    )
)
```

### 2. 只提取元数据，不包含源码

```python
(
    AiMdGenerator("output.md")
    .set_project_propery("my_project", r"D:\codes\my_project")
    .merge_from_files_with_metadata(
        relative_file_name_list=["src/main.py"],
        as_title="核心代码架构",
        include_ast_metadata=True,  # 包含元数据
        include_file_text=False,    # 不包含源码
    )
)
```

### 3. 支持的文件类型

`AiMdGenerator` 支持多种编程语言的语法高亮：

```python
suffix__lang_map = {
    ".py": "python",
    ".java": "java",
    ".go": "go",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "javascript",
    ".tsx": "typescript",
    ".vue": "vue",
    ".php": "php",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".sql": "sql",
    ".sh": "shell",
    ".ps1": "powershell",
    ".md": "markdown",
    ".json": "json",
    ".yaml": "yaml",
    ".xml": "xml",
    ".html": "html",
    ".css": "css",
    # ... 更多
}
```

## 🎯 实际应用场景

### 1. AI 代码审查
生成完整项目上下文，让 AI 全面审查代码质量、安全漏洞、性能问题。

### 2. 技术文档生成
快速为新团队成员生成项目概览文档，配合 AI 解释代码逻辑。

### 3. 知识库构建
将项目内容导入 RAG 知识库，实现智能代码搜索和问答。

### 4. 项目迁移和重构
让 AI 理解整个项目后，提供重构建议或迁移到新框架。

### 5. 学习开源项目
下载 GitHub 项目后生成结构化文档，配合 AI 快速理解项目架构。

## 🔒 安全性

### `.gitignore` 支持

设置 `use_gitignore=True` 时，会自动遵循项目的 `.gitignore` 规则：

```python
.merge_from_dir(
    relative_dir_name="src",
    use_gitignore=True,  # 自动排除 .env、*.log 等敏感文件
)
```

### 自动排除
- 自动排除以 `.` 开头的隐藏目录（如 `.git`、`.venv`）
- 支持手动排除特定目录和文件

## 📊 性能特性

- ✅ 高效的文件遍历和过滤
- ✅ 智能文本文件检测
- ✅ 支持大型项目（数千个文件）
- ✅ 链式调用，代码简洁优雅

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🔗 相关链接

- **GitHub**: https://github.com/ydf0509/nb_ai_context
- **PyPI**: https://pypi.org/project/nb_ai_context/
- **Issues**: https://github.com/ydf0509/nb_ai_context/issues

## 💡 常见问题

### Q: 生成的 Markdown 文件太大怎么办？
A: 使用 `should_include_suffixes` 限制文件类型，或使用 `excluded_dir_name_list` 排除不重要的目录（如 `node_modules`、`venv`）。

### Q: 如何只生成代码结构，不包含源码？
A: 使用 `merge_from_files_with_metadata()` 方法，设置 `include_file_text=False`。

### Q: 支持哪些编程语言？
A: 所有文本文件都支持，但 Python 文件有特殊的 AST 元数据提取支持。



## 🌟 Star History

如果这个项目对你有帮助，请给个 Star ⭐️！

---

**nb_ai_context** - 让 AI 真正理解你的代码 🚀
