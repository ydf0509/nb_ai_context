
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **此文档生成时间**：2026-06-05 20:18:48
> **系统指令**：你正在解析一份由工具 **`nb_ai_context`** 自动生成的**结构化项目快照**。
> **文档性质**：这**不是**一份普通的面向人类的文档，而是专为 AI 大模型（LLM）设计的上下文数据流。它将项目文档、源代码和 AST 架构元数据进行了特殊的结构化合并，请开启"代码解析器"的心智模式。


## 🧠 AI 认知与解析准则

这份由 `nb_ai_context` 生成的文档是你的核心知识库。其中的内容是动态的——它可能包含完整的底层源码，也可能仅包含使用教程，或者是两者的混合。请严格遵循以下自适应阅读策略：

### 1. 信息的层级与冲突处理
*   **文档即意图**：将 `README`、教程文档和 Docstrings 视为项目设计的**最高意图**。如果生成器省略了对应源码，请完全信任文档逻辑，以此为基础推理。
*   **源码即事实**：遇到 `.py` 源码或 AST 元数据（类/函数签名）时，以此作为实现细节、类型约束和语法准确性的**最终事实标准**。
*   **冲突处理**：若文档与源码/AST 存在矛盾，请以源码为准，并在回答中向用户简要指出该差异。
*   **测试代码的忽略**：为优化 Token 长度，集成/单元测试及非核心 API 源码通常被隐藏。**绝对不要**因此推断或提醒用户“项目缺乏测试”或“代码未实现”。

### 2. 文件边界与架构感知
*   **上下文定界**：工具使用 `--- **start of file: <路径>** ---` 等标记严格界定文件。**在你的回复中，请使用标准 Markdown 代码块，切勿模仿使用此类系统定界符。**
*   **结构可视化**：利用“文件树 (File Tree)”章节建立项目的宏观架构认知。
*   **依赖关系**：利用“文件依赖分析”章节理清模块间的 import 数据流向。

### 3. 严格的代码生成与交互边界
*   **事实锚定 (Fact Anchoring)**：你生成的代码必须严格锚定在本文档范围内！API 调用必须基于**源码中的 AST 签名**或**文档中的演示示例**。
*   **严禁臆造 (Zero Fabrication)**：绝对禁止编造文档中未定义或未提及的类名、方法名或参数。
*   **越界拒绝**：如果用户询问的功能在当前提供的上下文中完全不存在，请明确告知“当前上下文中未包含该信息”，而不是试图凭空生成。

---
# markdown content namespace: nbrag project summary 



- `nbrag` is an Agentic RAG MCP Server with 12 complementary tools for AI-driven multi-round code retrieval.
- Dual storage: ChromaDB for vectorized chunks (with overlap) + raw_files/ for original file snapshots (no overlap).
- Core modules:
  - `nbrag/server.py`: 12 MCP tools + CLI entry point (`main()`)
  - `nbrag/core.py`: Embedding/Rerank API calls, ChromaDB CRUD, file ingestion
  - `nbrag/chunker.py`: Text splitting, line number calculation, Python AST scope parsing, header injection
  - `nbrag/config.py`: Configuration loading: CLI > env vars > YAML > defaults
- AST scope injection: Python file chunks get `[File:] [Scope:] [Sig:] [Lines:]` headers before embedding, significantly improving search accuracy.
- Each chunk stores 8 metadata fields: source, filename, doc_id, chunk_index, total_chunks, line_start, line_end, scope.
- Usage: `uvx nbrag` (stdio) or `uvx nbrag --transport streamable-http --port 9101` (HTTP)


## 📋 nbrag most core source files metadata (Entry Points)


以下是项目 nbrag 最核心的入口文件的结构化元数据，帮助快速理解项目架构：



### the project nbrag most core source code files as follows: 
- `nbrag/server.py`
- `nbrag/core.py`


### 📄 Python File Metadata: `nbrag/server.py`

#### 📝 Module Docstring

`````
nbrag MCP Server — 12 个 Agentic RAG 工具。

Tools (12):
  1. nbrag_add_document         → Import file/directory into collection
  2. nbrag_search               → Semantic search (vector + rerank)
  3. nbrag_search_and_fetch     → Search + auto-fetch raw source (combo tool)
  4. nbrag_grep                 → Keyword/regex exact search (complements semantic search)
  5. nbrag_find_definition      → Find complete class/function definition by symbol name
  6. nbrag_get_file_chunks      → Paginated chunks with scope/line metadata
  7. nbrag_get_raw_file         → Raw file content without overlap
  8. nbrag_get_adjacent_chunks  → Adjacent chunks by chunk index
  9. nbrag_get_chunks_by_lines  → Chunks covering a line range
  10. nbrag_list                → List imported documents
  11. nbrag_delete              → Delete a document
  12. nbrag_stats               → Collection overview and config

启动方式:
  uvx nbrag                          # stdio (默认)
  uvx nbrag --transport streamable-http --port 9101  # HTTP
`````

#### 📦 Imports

- `from pydantic import Field`
- `from mcp.server.fastmcp import FastMCP`
- `from nbrag.config import get_config`
- `from nbrag.chunker import DEFAULT_CHUNK_SIZE`
- `from nbrag.chunker import DEFAULT_CHUNK_OVERLAP`
- `from nbrag.core import ingest_path`
- `from nbrag.core import search`
- `from nbrag.core import list_documents`
- `from nbrag.core import delete_document`
- `from nbrag.core import get_stats`
- `from nbrag.core import get_file_chunks`
- `from nbrag.core import get_context_chunks`
- `from nbrag.core import grep_knowledge`
- `from nbrag.core import find_symbol_definition`
- `import argparse`
- `from nbrag.config import load_config`

#### 🔧 Public Functions (13)

- `def nbrag_add_document(path: str = Field(description='Absolute path to a file or directory. Directory imports all text files recursively'), collection_name: str = Field(description='Collection name (required, auto-created if not exists. Use nbrag_stats to see existing)'), chunk_size: int = Field(default=DEFAULT_CHUNK_SIZE, description='Chunk size in chars, default 1500, recommended 1000-2000'), chunk_overlap: int = Field(default=DEFAULT_CHUNK_OVERLAP, description='Chunk overlap in chars, default 200'), file_extensions: str = Field(default='', description="Comma-separated file extensions to include (e.g. 'py,md,html'). Empty = all text files")) -> str` `mcp.tool()`
  - *Line: 36*
  - **Docstring:**
  `````
  Ingest file or directory into RAG collection (chunking + embedding + indexing). Auto-creates collection if not exists.
  Each chunk is enriched with file path, line numbers, and Python class/function scope.
  Use nbrag_search to retrieve ingested content.
  Note: This tool is typically called manually by users via scripts for one-time batch ingestion,
  not by AI during conversations. AI should focus on nbrag_search/nbrag_grep for retrieval.
  `````

- `def nbrag_search(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections),collection_name对应你的中文就是知识库名字'), top_k: int = Field(default=5, description='Number of results to return'), use_rerank: bool = Field(default=True, description='Enable reranker for better accuracy (recommended)'), filter_filename: str = Field(default='', description="Optional: filter by filename only (e.g. 'constant.py', not full path)")) -> str` `mcp.tool()`
  - *Line: 76*
  - **Docstring:**
  `````
  Semantic search in RAG collection. Vector recall + Rerank. Call nbrag_stats first to see available collections.
  
  Each result contains: file_path (full path), chunk:X/Y, line:N-M, scope, doc_id, dist (cosine distance, lower=more similar).
  
  Recommended deep-analysis workflow (use multiple tools, not just search):
    1. nbrag_search → find relevant files and rough location
    2. nbrag_grep → pinpoint exact class/method/constant names (what semantic search may miss)
    3. nbrag_find_definition → get complete class/function source with inheritance chain
    4. nbrag_get_raw_file → read full source code to verify details
    5. Cross-file tracing: when you see unknown symbols in code, repeat steps 2-4 to trace references
  
  Follow-up tools — use result fields directly as parameters:
    - nbrag_find_definition(symbol, collection_name) → complete class/function definition + methods summary
    - nbrag_get_raw_file(file_path, collection_name) → full source code without overlap
    - nbrag_get_file_chunks(file_path, collection_name) → paginated chunks with scope metadata
    - nbrag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result
    - nbrag_get_chunks_by_lines(doc_id, line_start, line_end, collection_name) → chunks covering line range
  `````

- `def nbrag_search_and_fetch(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)'), top_k: int = Field(default=5, description='Number of search results to return'), fetch_top_n_raw: int = Field(default=3, description='Auto-fetch raw source for top N results (0 to skip fetching)'), context_lines: int = Field(default=100, description='Lines of context around matched chunk. Small files (≤2x this) are fetched fully')) -> str` `mcp.tool()`
  - *Line: 157*
  - **Docstring:**
  `````
  Search + auto-fetch raw source code for top results in one call (combo tool).
  Saves a round-trip vs calling nbrag_search then nbrag_get_raw_file separately.
  Same doc_id appearing in multiple results is fetched only once with merged line range.
  `````

- `def nbrag_grep(keyword: str = Field(description="Keyword or regex pattern (e.g. class name 'UserService', method 'get_by_id', constant 'MAX_RETRIES')"), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)'), max_results: int = Field(default=10, description='Maximum number of matches to return'), case_sensitive: bool = Field(default=False, description='Case-sensitive matching'), filter_filename: str = Field(default='', description="Optional: filter by filename only (e.g. 'booster.py', not full path)"), context_lines: int = Field(default=10, description='Lines of context before and after each match (default 10, use 20+ for seeing full function/class headers)')) -> str` `mcp.tool()`
  - *Line: 270*
  - **Docstring:**
  `````
  Keyword/regex exact search in cached raw files. Complements nbrag_search (semantic search).
  
  Use cases where nbrag_search falls short:
    - Find class/function/variable names: 'UserService', 'get_by_id'
    - Find config keys/constants: 'MAX_RETRIES', 'DEFAULT_TIMEOUT'
    - Find import statements: 'from myproject.core'
    - Find string literals: 'error_handler'
  
  Tip: use context_lines=15 to see class headers + inheritance chain around the match.
  For complete definitions, use nbrag_find_definition instead.
  Typical workflow: nbrag_search (find direction) → nbrag_grep (pinpoint symbols) → nbrag_find_definition (full definition)
  `````

- `def nbrag_find_definition(symbol: str = Field(description="Symbol name to find (class name like 'UserService', function name like 'get_by_id', or qualified name like 'MyClass.__init__')"), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)'), max_results: int = Field(default=5, description='Maximum number of definitions to return')) -> str` `mcp.tool()`
  - *Line: 309*
  - **Docstring:**
  `````
  Find the complete definition of a class/function/method by symbol name.
  Uses AST parsing to extract exact boundaries — returns the FULL source code of the definition.
  For classes, also returns a methods summary (all method signatures).
  
  Best for cross-file tracing: when you see an unknown symbol in code, use this to get its complete definition.
  Much more efficient than grep + raw_file for understanding class hierarchy and implementation.
  `````

- `def nbrag_get_file_chunks(file_path: str = Field(description="Full absolute path (use 'file_path' value from nbrag_search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)'), start_chunk: int = Field(default=0, description='Start chunk index (0-based), use for pagination'), max_chunks: int = Field(default=10, description='Max chunks to return (use for pagination)')) -> str` `mcp.tool()`
  - *Line: 349*
  - **Docstring:**
  `````
  Paginated view of file chunks with scope and line metadata. Use start_chunk to paginate.
  Note: adjacent chunks have overlap. For clean source code without overlap, use nbrag_get_raw_file instead.
  `````

- `def nbrag_get_raw_file(file_path: str = Field(description="Full absolute path (use 'file_path' value from nbrag_search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)'), line_start: int = Field(default=-1, description='Start line (1-based), -1 for beginning'), line_end: int = Field(default=-1, description='End line (inclusive), -1 for end of file')) -> str` `mcp.tool()`
  - *Line: 369*
  - **Docstring:**
  `````
  Get cached raw file content without chunk overlap. Recommended for viewing full source code.
  Supports line_start/line_end for extracting specific line ranges.
  Only available for files imported with raw cache (re-import older files if needed).
  `````

- `def nbrag_get_adjacent_chunks(doc_id: str = Field(description="Document ID (use 'doc_id' value from nbrag_search/nbrag_grep results)"), chunk_index: int = Field(description="Target chunk index (0-based, the X from 'chunk:X/Y' in nbrag_search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)'), window: int = Field(default=3, description='Context window: returns chunk_index ± window chunks')) -> str` `mcp.tool()`
  - *Line: 437*
  - **Docstring:**
  `````
  Get adjacent chunks around a specific chunk index, for expanding context of a search result.
  Requires doc_id and chunk_index from nbrag_search results (not file_path).
  Example: doc_id="abc123", chunk_index=3, window=2 → returns chunks 1-5
  `````

- `def nbrag_get_chunks_by_lines(doc_id: str = Field(description="Document ID (use 'doc_id' value from nbrag_search/nbrag_grep results)"), line_start: int = Field(description="Start line number (1-based, from 'line:N-M' in search results)"), line_end: int = Field(description="End line number (inclusive, from 'line:N-M' in search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)')) -> str` `mcp.tool()`
  - *Line: 454*
  - **Docstring:**
  `````
  Get all chunks covering a line range, with scope metadata.
  vs nbrag_get_raw_file: this returns chunks (with scope but has overlap),
  nbrag_get_raw_file returns raw code (no overlap but no scope).
  Example: doc_id="abc123", line_start=80, line_end=200
  `````

- `def nbrag_list(collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)')) -> str` `mcp.tool()`
  - *Line: 497*
  - **Docstring:**
  `````
  List all documents in a collection (filename, path, chunk count, doc_id).
  Use returned doc_id with nbrag_delete to remove documents.
  `````

- `def nbrag_delete(doc_id: str = Field(description="Document ID to delete (use 'doc_id' value from nbrag_list results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)')) -> str` `mcp.tool()`
  - *Line: 516*
  - *Delete a document's vectors and cached files from the collection. Get doc_id from nbrag_list.*

- `def nbrag_stats() -> str` `mcp.tool()`
  - *Line: 530*
  - **Docstring:**
  `````
  nbrag_stats 获取所有知识库的统计信息，英文术语`collection` 就是中文的`知识库`
  Get RAG overview: all collection names, doc/chunk counts, and config.
  Call this FIRST to discover available collection_name values for other tools.
  Glossary: collection = knowledge base, doc = imported file, chunk = vector-embedded text segment.
  `````

- `def main()`
  - *Line: 562*
  - *CLI entry point for uvx / python -m nbrag.*


---




### 📄 Python File Metadata: `nbrag/core.py`

#### 📝 Module Docstring

`````
RAG 核心逻辑 —— 供 MCP 服务和独立脚本共同复用。

功能:
  - Embedding / Rerank API 调用（默认 SiliconFlow，可配置任何 OpenAI 兼容 API）
  - ChromaDB 向量存储（CRUD + 搜索）
  - 文件导入（切分 + enrichment + 存储）

分块增强逻辑（切分、行号、AST scope、头部注入）在 chunker.py 中。
配置从环境变量 / YAML 文件 / CLI 参数加载（见 config.py）。
`````

#### 📦 Imports

- `import os`
- `import hashlib`
- `import httpx`
- `import chromadb`
- `from nbrag.config import get_config`
- `from nbrag.chunker import chunk_text`
- `from nbrag.chunker import enrich_chunks`
- `from nbrag.chunker import collect_files`
- `from nbrag.chunker import DEFAULT_CHUNK_SIZE`
- `from nbrag.chunker import DEFAULT_CHUNK_OVERLAP`
- `import time as _time`
- `import time as _time`
- `import time as _time`
- `import shutil`
- `import time as _time`
- `from concurrent.futures import ThreadPoolExecutor`
- `from concurrent.futures import as_completed`
- `import re`
- `import re`
- `import ast as _ast`
- `import warnings as _warnings`
- `from nbrag.chunker import _extract_signature`

#### 🔧 Public Functions (17)

- `def invalidate_doc_id_cache(collection_name = None)`
  - *Line: 85*
  - *清除 doc_id 映射缓存（导入/删除 collection 后调用）。*

- `def get_collection(name = 'default')`
  - *Line: 105*
  - *获取或创建一个 ChromaDB collection（写操作用）。*

- `def delete_collection(name)`
  - *Line: 120*
  - *删除整个 collection（清空该知识库）。*

- `def list_collections()`
  - *Line: 126*
  - *列出所有 collection。*

- `def embed(texts, max_retries = 3)`
  - *Line: 140*
  - *调用 Embedding API，自动分批，失败自动重试。*

- `def rerank(query, documents, top_n = 5, max_retries = 3)`
  - *Line: 180*
  - *调用 Rerank API，返回重排后的索引列表，失败自动重试。*

- `def ingest_file(file_path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP)`
  - *Line: 368*
  - *导入单个文件到知识库，返回结果 dict（串行版本，兼容旧调用）。*

- `def ingest_path(path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None)`
  - *Line: 378*
  - *导入文件或目录到知识库。返回 (results_list, errors_list, skipped_count)。*

- `def batch_ingest(paths, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None, delete_first = False, on_progress = None, verbose = False, max_workers = 1)`
  - *Line: 409*
  - **Docstring:**
  `````
  批量导入多个路径到知识库（一站式封装）。
  
  两阶段流水线设计：
    阶段 1（可并行）：读取文件 → 文本切分 → 调用 Embedding API 获取向量
    阶段 2（必须串行）：写入 ChromaDB + 缓存原始文件
  
  Embedding API 调用是 I/O 密集型（网络等待），是整个导入流程的主要瓶颈。
  通过 max_workers > 1 可以并行执行阶段 1，显著加速大批量导入。
  ChromaDB（SQLite 底层）不支持并发写，所以阶段 2 始终串行。
  
  Args:
      paths: 文件/目录路径列表（或单个字符串）。
      collection_name: 知识库名称，不存在时自动创建。
      chunk_size: 分块大小（字符数），默认 1500。
      chunk_overlap: 分块重叠（字符数），默认 200。
      file_extensions: 可选后缀过滤列表（如 [".py", ".md"]），None 表示全部文本文件。
      delete_first: 是否先清空旧数据再导入（适用于全量重建）。
      on_progress: 可选回调 fn(current, total, file_path, result)，用于自定义进度展示。
      verbose: 是否打印详细日志。
      max_workers: Embedding 并发线程数。
                   1 = 串行（默认，兼容旧行为）；
                   2-4 = 并行读取+Embedding，串行写入 ChromaDB。
                   不建议超过 4，避免触发 Embedding API 频率限制。
  `````

- `def search(query, collection_name = 'default', top_k = 5, use_rerank = True, filter_filename = None)`
  - *Line: 586*
  - *语义搜索。返回 (documents, metadatas, distances, rerank_used, total)。*

- `def get_file_chunks(file_identifier, collection_name = 'default', start_chunk = 0, max_chunks = 5, raw = False, line_start = -1, line_end = -1)`
  - *Line: 636*
  - *按文件路径或文件名获取知识库中该文件的内容。*

- `def get_context_chunks(doc_id, collection_name = 'default', chunk_index = None, window = 2, line_start = None, line_end = None)`
  - *Line: 756*
  - *获取指定文档的上下文 chunks。*

- `def grep_knowledge(keyword, collection_name = 'default', max_results = 10, case_sensitive = False, filter_filename = None, context_lines = 5)`
  - *Line: 817*
  - *在知识库的原始缓存文件中进行关键词/正则搜索。*

- `def find_symbol_definition(symbol, collection_name = 'default', max_results = 5)`
  - *Line: 873*
  - *在知识库中查找符号（类/函数/方法）的完整定义。*

- `def list_documents(collection_name = 'default')`
  - *Line: 984*
  - *列出知识库中已导入的文档。*

- `def delete_document(doc_id, collection_name = 'default')`
  - *Line: 1010*
  - *删除指定文档的所有向量数据及缓存文件。返回 (deleted_count, filename)。*

- `def get_stats()`
  - *Line: 1030*
  - *返回所有知识库的统计信息。*


---



## 🔗 nbrag Some File Dependencies Analysis

以下是项目文件之间的依赖关系，帮助 AI 理解代码结构：

### 📊 Internal Dependencies Graph

`````
Entry Points (not imported by other project files):
  ★ nbrag/server.py

Core Files (imported by other files, sorted by import count):
  ◆ nbrag/core.py (imported by 1 files)

`````

### 📋 Detailed Dependencies

#### `nbrag/core.py`

**Imported by:**
- `nbrag/server.py`

#### `nbrag/server.py`

**Imports from project:**
- `nbrag/core.py`

### 📦 Third-party Dependencies

项目使用的第三方库：

- `chromadb`
- `httpx`
- `mcp`
- `nbrag`
- `pydantic`
- ......以及更多的第三方库......


---
# markdown content namespace: nbrag Project Root Dir Some Files 


## nbrag File Tree (relative dir: `.`)


`````

├── README.md
└── pyproject.toml

`````

---


## nbrag (relative dir: `.`)  Included Files (total: 2 files)


- `README.md`

- `pyproject.toml`


---


--- **start of file: README.md** (project: nbrag) --- 

`````markdown
# nbrag

**Agentic RAG MCP Server** — 基于 MCP 协议的智能知识库，可导入代码、文档、小说等任意文本，尤其对 Python 项目有奇效（AST 自动解析 class/function 作用域，搜索精准度远超普通 RAG）。支持接入任何 MCP 兼容的 AI 产品：Cursor、OpenCode、Claude Code、Cherry Studio、Open WebUI、Dify、Cline 等，也可嵌入用户自己开发的具备 ReAct Loop 的 Agent 程序。

AI Agent 自主决定何时搜、搜什么、搜几次。12 个精心设计的互补 MCP 工具，吊打传统一轮检索的 Naive RAG。

## 为什么不是 Naive RAG？

| | Naive RAG | **Agentic RAG (本项目)** |
|---|-----------|----------------------|
| 检索触发 | 每次提问自动检索 top-5 注入 | AI 自主决定是否检索、用哪个工具 |
| 检索轮次 | 1 次 | 多轮（实测 m 次搜索 + n 次文件读取） |
| 查询构造 | 用户原文 | AI 重写查询、组合多种检索策略 |
| 工具种类 | 仅语义搜索 | 语义 + grep + AST 符号定位 + 原文读取 |
| 分析深度 | 浅层描述 | 完整的跨文件调用链图 |
| 准确度 | 浅层匹配，容易遗漏 | **显著优于 Naive RAG**，跨文件关联更完整 |

核心观点：**检索不是管道，是 Agent 的一种能力。**

## 快速开始

### 1. 安装

```bash
# 方式 A: uvx (推荐，零安装)
uvx nbrag

# 方式 B: pip
pip install nbrag
```

### 2. 配置 API Key

```bash
# SiliconFlow 免费 API Key (https://siliconflow.cn)
export NBRAG_API_KEY=sk-xxx
```

### 3. 在 Cursor / Claude Desktop 中配置 MCP

有三种配置方式，选一种即可：

#### 方式 A: uvx 启动（推荐，零安装）

```json
{
  "mcpServers": {
    "rag": {
      "command": "uvx",
      "args": ["nbrag"],
      "env": {
        "NBRAG_API_KEY": "sk-xxx"
      }
    }
  }
}
```

#### 方式 B: python 命令启动

```json
{
  "mcpServers": {
    "rag": {
      "command": "python",
      "args": ["-m", "nbrag"],
      "env": {
        "NBRAG_API_KEY": "sk-xxx"
      }
    }
  }
}
```

#### 方式 C: HTTP 模式（推荐多项目共享）

> **为什么选 HTTP？** stdio 模式下每个 IDE 窗口会各起一个独立进程。如果你同时打开了几十个项目，
> 就是几十个 Python 进程 + 几十份 ChromaDB 内存。HTTP 模式只跑一个服务进程，所有 IDE 共享同一个端口，
> 省内存，也避免多进程并发写同一个 ChromaDB 数据库的锁冲突。

先启动服务：

```bash
# uvx 方式
uvx nbrag --transport streamable-http --port 9101

# 或 python 方式
python -m nbrag --transport streamable-http --port 9101
```

再配置客户端：

```json
{
  "mcpServers": {
    "rag": {
      "type": "http",
      "url": "http://localhost:9101/mcp"
    }
  }
}
```

#### 在openwebui 中配置nbrag mcp，通过rag知识库学习 langchain框架，截图如下：

nbrag是标准mcp，所以配置在任何个人agent和任意agent产品里面
![alt text](image109.png)

### 4. 导入知识库

#### 方式 A: 让 AI 自动导入

告诉 AI：

> "帮我把 D:/codes/my_project 导入到 myproject 知识库，然后搜索 XXX"

AI 会自动调用 `nbrag_add_document` 导入，再用 `nbrag_search` + `nbrag_grep` + `nbrag_find_definition` 多轮检索回答你的问题。

#### 方式 B: 手动脚本导入（推荐大项目）

手动导入更灵活——可以精确指定目录、过滤文件后缀、控制 chunk 参数：

```python
from nbrag.core import batch_ingest

batch_ingest(
    paths=[
        "D:/codes/my_project/src",     # 只导入 src 目录
        "D:/codes/my_project/docs",    # 加上文档目录
    ],
    collection_name="my_project",
    file_extensions=[".py", ".md"],    # 只要 Python 和 Markdown 文件
    delete_first=True,                 # 清空旧数据重新导入
    verbose=True,
)
```

参见 `scripts/ingest_project.py` 获取完整示例。

## 12 个工具

| 类别 | 工具 | 功能 |
|------|------|------|
| **导入** | `nbrag_add_document` | 导入文件/目录（自动分块 + Embedding + 缓存原文） |
| **语义检索** | `nbrag_search` | 向量搜索 + Rerank 精排 |
| **语义检索** | `nbrag_search_and_fetch` | 搜索 + 自动取源码（省一次 round-trip） |
| **精确检索** | `nbrag_grep` | 关键词/正则搜索（和语义搜索互补） |
| **精确检索** | `nbrag_find_definition` | AST 精确定位 class/function 完整定义 |
| **上下文扩展** | `nbrag_get_file_chunks` | 按 chunk 分页浏览文件 |
| **上下文扩展** | `nbrag_get_raw_file` | 读取无 overlap 的原始文件 |
| **上下文扩展** | `nbrag_get_adjacent_chunks` | 获取相邻 chunks |
| **上下文扩展** | `nbrag_get_chunks_by_lines` | 按行号范围取 chunks |
| **管理** | `nbrag_list` | 列出知识库所有文档 |
| **管理** | `nbrag_delete` | 删除指定文档 |
| **管理** | `nbrag_stats` | 知识库统计信息 |

### Skill 指南（教 AI 打组合拳）

12 个工具暴露给 AI 后，AI 只知道"能调什么"，不知道"按什么顺序调"。
项目附带一个 Skill 文件，打包在 `nbrag` 包内，把最佳检索流程写成 AI 能读懂的指南。

**使用方法**：从 pip 安装路径复制到你项目的 Skills 目录，AI 就自动学会多轮检索策略。

```bash
# 先获取 skill 路径
SKILL_PATH=$(python -c "import nbrag, os; print(os.path.join(os.path.dirname(nbrag.__file__), 'skills', 'nbrag-workflow'))")

# Cursor
cp -r $SKILL_PATH .cursor/skills/

# Claude Code
cp -r $SKILL_PATH .claude/skills/

# nb_agent
cp -r $SKILL_PATH .nb_agent/skills/

# OpenAI Codex / Gemini CLI /nb_agent（跨平台标准）
cp -r $SKILL_PATH .agents/skills/
```

Skill 内容包括：发现（nbrag_stats）→ 检索（4 种策略选择）→ 深入（4 种上下文获取方式）→ 多轮重试策略。

### AI 推荐的深度分析工作流

```
1. nbrag_search → 找到相关文件和大致位置
2. nbrag_grep → 精确定位类名/方法名/常量（语义搜索漏掉的）
3. nbrag_find_definition → 获取完整的类/函数定义源码
4. nbrag_get_raw_file → 读取完整源码验证细节
5. 跨文件追踪：发现未知符号时重复 2-4 步
```

## 向量数据库 Metadata 字段

每个 chunk 入库时除了 embedding 向量，还存储了丰富的 metadata。这是很多 RAG 方案忽略的关键设计——有了 metadata，才能实现按文件过滤、按行号定位、按作用域追踪等高级能力。

| 字段 | 类型 | 示例 | 说明 |
|------|------|------|------|
| `source` | str | `D:/codes/myproject/core.py` | 文件绝对路径（跨平台统一格式） |
| `filename` | str | `core.py` | 文件名（方便 `filter_filename` 过滤） |
| `doc_id` | str | `a1b2c3d4e5f6` | 路径 MD5 前 12 位（文件唯一标识） |
| `chunk_index` | int | `3` | 当前 chunk 在文件中的序号（0-based） |
| `total_chunks` | int | `15` | 该文件的总 chunk 数 |
| `line_start` | int | `45` | chunk 对应的起始行号（1-based） |
| `line_end` | int | `78` | chunk 对应的结束行号 |
| `scope` | str | `MyClass.my_method` | Python AST 解析的作用域（非 Python 文件为空） |

**chunk 头部注入示例**（embedding 前自动添加，提升搜索精度）：

```
# [File: D:/codes/myproject/core.py] [Class: class MyClass(Base)] [Method: process] [Sig: def process(self, data: dict)] [Lines: 45-78]
```

有了这些 metadata + 头部注入，`nbrag_search` 搜 "process 方法" 就能精准命中 `MyClass.process`，而不是随机匹配到别的 "process" 字符串。

## 配置

### 环境变量

| 变量 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `NBRAG_API_KEY` | **是** | | Embedding/Rerank API Key |
| `NBRAG_BASE_URL` | 否 | `https://api.siliconflow.cn/v1` | API Base URL |
| `NBRAG_EMBEDDING_MODEL` | 否 | `BAAI/bge-m3` | Embedding 模型 |
| `NBRAG_RERANK_MODEL` | 否 | `BAAI/bge-reranker-v2-m3` | Rerank 模型 |
| `NBRAG_DB_PATH` | 否 | `./rag_db` | ChromaDB 存储路径 |
| `NBRAG_CHUNK_SIZE` | 否 | `1500` | 分块大小 |
| `NBRAG_CHUNK_OVERLAP` | 否 | `200` | 分块重叠 |

### 配置文件 (可选)

支持 YAML 配置文件，自动搜索顺序：
1. `./nbrag_config.yaml`
2. `~/.config/nbrag/config.yaml`

```yaml
embedding:
  api_key: ${NBRAG_API_KEY}
  base_url: https://api.siliconflow.cn/v1
  model: BAAI/bge-m3

rerank:
  model: BAAI/bge-reranker-v2-m3

storage:
  db_path: ./rag_db

chunking:
  chunk_size: 1500
  chunk_overlap: 200
```

### CLI 参数

```bash
nbrag --help
nbrag --transport stdio              # 默认
nbrag --transport streamable-http    # HTTP 模式
nbrag --api-key sk-xxx              # 直接传 API Key
nbrag --db-path /data/rag           # 指定存储路径
nbrag --config ./my_config.yaml     # 指定配置文件
```

## 设计决策

### 为什么 chunk_size = 1500？

BGE-M3 的最佳召回区间是 700-3000 字符。如果 chunk_size 设太小（如 500），一个 8000 字符的大类会被切成 20+ 块，语义搜索碎片化严重、召回率下降。1500 是实测平衡点，大多数函数/类能完整落入 1-2 个 chunk 内。

即使 chunk 切分不完美，Agentic RAG 也不会像 Naive RAG 那样只用碎片凑答案。AI 会自主判断当前 chunk 信息不足，然后调用 `nbrag_get_raw_file` 读完整源码、用 `nbrag_find_definition` 精确定位类/函数定义、用 `nbrag_grep` 全文搜索关键词，多轮组合直到信息充分。这正是 "检索是 Agent 的能力" 而非固定管道的意义。

### 为什么双存储？

- **ChromaDB**：存向量 chunks（有 overlap），用于语义搜索
- **raw_files/**：存原始文件快照（无 overlap），用于精确行号读取

AI 经常需要看完整源码，如果只有 chunks 会有 overlap 重复，浪费 token 还容易困惑。

### 为什么 AST scope 注入？

每个 chunk 的 embedding 前注入 `[File: path] [Scope: MyClass.my_method] [Sig: def my_method(self, x)]`。
这样搜索 "process 方法" 时更容易命中 `class DataProcessor` 下的 `def process(self, data)`，而不是随机匹配到别的 "process" 字符串。

### 为什么 12 个工具而不是 3 个？

MCP 工具设计原则：**职责单一、参数最少、docstring 引导下一步**。

一个大而全的 `rag_query(mode="search|grep|raw|...")` 会导致 AI 幻觉——它不知道该传什么参数。
拆成 12 个小工具后，每个工具参数清晰，AI 的调用准确率大幅提升。

## 技术栈

| 组件 | 选择 |
|------|------|
| Embedding | SiliconFlow BGE-M3（免费、中文最强之一） |
| Rerank | SiliconFlow BGE-Reranker-v2-m3（免费） |
| 向量数据库 | ChromaDB（本地持久化，无需外部服务） |
| 分块 | LangChain TextSplitter + 自研 AST 增强 |
| MCP | FastMCP (Python) |
| 传输 | stdio / streamable-http / SSE |

## License

MIT

`````

--- **end of file: README.md** (project: nbrag) --- 

---


--- **start of file: pyproject.toml** (project: nbrag) --- 

`````text
[project]
name = "nbrag"
version = "0.3.0"
description = "Agentic RAG MCP Server — 12 tools for AI-driven multi-round code retrieval that outperforms naive single-shot RAG"
readme = "README.md"
license = "MIT"
requires-python = ">=3.11"
keywords = ["mcp", "rag", "agentic-rag", "chromadb", "embedding", "code-search", "ai-agent", "mcp-server"]
authors = [
    {name = "ydf", email = "ydf0509@sohu.com"},
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
]

dependencies = [
    "mcp>=1.0.0",
    "httpx>=0.24.0",
    "chromadb>=0.4.0",
    "langchain-text-splitters>=0.2.0",
    "pydantic>=2.0.0",
    "pyyaml>=6.0",
]

[project.urls]
Homepage = "https://github.com/ydf0509/nbrag"
Repository = "https://github.com/ydf0509/nbrag"

[project.scripts]
nbrag = "nbrag.server:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

`````

--- **end of file: pyproject.toml** (project: nbrag) --- 

---

# markdown content namespace: nbrag codes 


## nbrag File Tree (relative dir: `nbrag`)


`````

└── nbrag
    ├── __init__.py
    ├── __main__.py
    ├── chunker.py
    ├── config.py
    ├── core.py
    ├── loggers.py
    └── server.py

`````

---


## nbrag (relative dir: `nbrag`)  Included Files (total: 7 files)


- `nbrag/chunker.py`

- `nbrag/config.py`

- `nbrag/core.py`

- `nbrag/loggers.py`

- `nbrag/server.py`

- `nbrag/__init__.py`

- `nbrag/__main__.py`


---


--- **start of file: nbrag/chunker.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/chunker.py`

#### 📝 Module Docstring

`````
RAG 分块增强模块 —— 文本切分 + 行号计算 + AST scope 解析 + 头部上下文注入。

从 core.py 拆分出来，专注于「把原始文本变成 enriched chunks」这一步。
core.py 专注于存储和检索。
`````

#### 📦 Imports

- `import os`
- `import ast`
- `import bisect`
- `import warnings`
- `from langchain_text_splitters import Language`
- `from langchain_text_splitters import RecursiveCharacterTextSplitter`

#### 🔧 Public Functions (5)

- `def chunk_text(text, chunk_size = DEFAULT_CHUNK_SIZE, overlap = DEFAULT_CHUNK_OVERLAP, file_ext = '')`
  - *Line: 46*
  - **Docstring:**
  `````
  根据文件类型自动选择最优切分策略（不含头部注入）。
  代码文件按 class/function 边界切分；Markdown 按标题切分；通用文本按段落切分。
  `````

- `def compute_line_ranges(full_text, chunks, overlap = DEFAULT_CHUNK_OVERLAP)`
  - *Line: 78*
  - **Docstring:**
  `````
  为每个 chunk 计算它在原文中的行号范围 (1-based)。
  
  使用顺序搜索 + 重叠偏移，确保每个 chunk 匹配到正确位置。
  Returns: [(start_line, end_line), ...]
  `````

- `def get_python_scope_at_line(text, line_number)`
  - *Line: 193*
  - **Docstring:**
  `````
  给定行号，返回该行所属的完整 scope 链字符串。
  
  返回示例: "MyClass", "MyClass.my_method", ""(模块级)
  `````

- `def enrich_chunks(chunks, full_text, file_path = '', file_ext = '')`
  - *Line: 252*
  - **Docstring:**
  `````
  为 chunks 注入头部上下文信息，返回 (enriched_chunks, line_ranges, scopes)。
  
  头部注入在 embedding 前完成，让向量包含上下文信息。
  line_ranges 和 scopes 用于存入 metadata。
  `````

- `def collect_files(path, file_extensions = None)`
  - *Line: 282*
  - **Docstring:**
  `````
  收集路径下所有文本文件（支持单文件或递归目录）。
  
  Args:
      path: 文件或目录路径。
      file_extensions: 可选，限定的后缀列表（如 [".py", ".md"]）。
                       传入时只收集这些后缀；不传则使用 TEXT_EXTENSIONS 全集。
                       后缀不区分大小写，自动补 "." 前缀（"py" → ".py"）。
  `````


---

`````python
"""
RAG 分块增强模块 —— 文本切分 + 行号计算 + AST scope 解析 + 头部上下文注入。

从 core.py 拆分出来，专注于「把原始文本变成 enriched chunks」这一步。
core.py 专注于存储和检索。
"""

import os
import ast
import bisect
import warnings

from langchain_text_splitters import Language, RecursiveCharacterTextSplitter


DEFAULT_CHUNK_SIZE = 1500
DEFAULT_CHUNK_OVERLAP = 200

# ─── 文件类型映射 ─────────────────────────────────────────

TEXT_EXTENSIONS = {
    ".txt", ".md", ".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go",
    ".rs", ".c", ".cpp", ".h", ".hpp", ".cs", ".rb", ".php", ".sh",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf",
    ".csv", ".tsv", ".xml", ".html", ".css", ".sql", ".r", ".lua",
    ".swift", ".kt", ".scala", ".dart", ".vue", ".svelte",
    ".rst", ".tex", ".log", ".env", ".bat", ".ps1",
}

_EXT_TO_LANG = {
    ".py": Language.PYTHON, ".js": Language.JS, ".ts": Language.TS,
    ".jsx": Language.JS, ".tsx": Language.TS,
    ".java": Language.JAVA, ".go": Language.GO,
    ".rs": Language.RUST, ".rb": Language.RUBY,
    ".cpp": Language.CPP, ".c": Language.C, ".h": Language.C, ".hpp": Language.CPP,
    ".cs": Language.CSHARP, ".php": Language.PHP,
    ".swift": Language.SWIFT, ".kt": Language.KOTLIN, ".scala": Language.SCALA,
    ".lua": Language.LUA, ".sol": Language.SOL,
    ".md": Language.MARKDOWN, ".html": Language.HTML,
    ".tex": Language.LATEX, ".rst": Language.RST,
}


# ─── 文本切分 ─────────────────────────────────────────────

def chunk_text(text, chunk_size=DEFAULT_CHUNK_SIZE, overlap=DEFAULT_CHUNK_OVERLAP,
               file_ext=""):
    """根据文件类型自动选择最优切分策略（不含头部注入）。
    代码文件按 class/function 边界切分；Markdown 按标题切分；通用文本按段落切分。
    """
    text = text.strip()
    if not text:
        return []

    lang = _EXT_TO_LANG.get(file_ext.lower())
    if lang:
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=lang, chunk_size=chunk_size, chunk_overlap=overlap,
        )
    else:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=overlap,
            separators=["\n\n", "\n", "。", ".", "；", ";", "，", ",", " ", ""],
        )
    return splitter.split_text(text)


# ─── 行号计算 ─────────────────────────────────────────────

def _build_line_offsets(text):
    """构建行号偏移表: line_offsets[i] = 第 i+1 行的起始字符位置。"""
    offsets = [0]
    for line in text.split('\n'):
        offsets.append(offsets[-1] + len(line) + 1)
    return offsets


def compute_line_ranges(full_text, chunks, overlap=DEFAULT_CHUNK_OVERLAP):
    """为每个 chunk 计算它在原文中的行号范围 (1-based)。

    使用顺序搜索 + 重叠偏移，确保每个 chunk 匹配到正确位置。
    Returns: [(start_line, end_line), ...]
    """
    line_offsets = _build_line_offsets(full_text)
    ranges = []
    search_start = 0

    for chunk in chunks:
        stripped = chunk.strip()
        if not stripped:
            ranges.append((0, 0))
            continue

        needle = stripped[:200]
        pos = full_text.find(needle, search_start)
        if pos == -1:
            pos = full_text.find(needle)

        if pos >= 0:
            start_line = bisect.bisect_right(line_offsets, pos)
            end_pos = pos + len(stripped)
            end_line = bisect.bisect_right(line_offsets, end_pos)
            ranges.append((start_line, end_line))
            advance = max(1, len(stripped) - overlap)
            search_start = pos + advance
        else:
            ranges.append((0, 0))

    return ranges


# ─── Python AST scope 解析 ────────────────────────────────

def _extract_signature(node):
    """从 AST 节点提取函数签名字符串。ClassDef 返回基类列表。"""
    if isinstance(node, ast.ClassDef):
        if node.bases:
            bases = []
            for b in node.bases:
                if isinstance(b, ast.Name):
                    bases.append(b.id)
                elif isinstance(b, ast.Attribute):
                    bases.append(b.attr)
                else:
                    bases.append("?")
            return f"class {node.name}({', '.join(bases)})"
        return f"class {node.name}"

    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = node.args
        params = []
        all_args = args.args + args.posonlyargs
        defaults_offset = len(all_args) - len(args.defaults)
        for i, arg in enumerate(all_args):
            p = arg.arg
            if arg.annotation and isinstance(arg.annotation, ast.Name):
                p += f": {arg.annotation.id}"
            if i >= defaults_offset:
                p += "=..."
            params.append(p)
        if args.vararg:
            params.append(f"*{args.vararg.arg}")
        if args.kwonlyargs:
            if not args.vararg:
                params.append("*")
            for kw in args.kwonlyargs:
                p = kw.arg
                if kw.annotation and isinstance(kw.annotation, ast.Name):
                    p += f": {kw.annotation.id}"
                params.append(p)
        if args.kwarg:
            params.append(f"**{args.kwarg.arg}")
        prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
        sig = f"{prefix} {node.name}({', '.join(params)})"
        if node.returns and isinstance(node.returns, ast.Name):
            sig += f" -> {node.returns.id}"
        return sig

    return ""


def _build_python_scope_map(text):
    """解析 Python 代码，构建 scope 列表。

    返回: [(start_line, end_line, scope_str, signature), ...]
    scope_str 示例: "MyClass", "MyClass.my_method", "my_function"
    signature 示例: "def my_method(self, x, y=...)"
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(text)
    except SyntaxError:
        return []

    scopes = []

    def _walk(node, parent_chain=""):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                name = child.name
                scope_str = f"{parent_chain}.{name}" if parent_chain else name
                start = child.lineno
                end = child.end_lineno if hasattr(child, 'end_lineno') and child.end_lineno else start
                sig = _extract_signature(child)
                scopes.append((start, end, scope_str, sig))
                _walk(child, scope_str)

    _walk(tree)
    return scopes


def get_python_scope_at_line(text, line_number):
    """给定行号，返回该行所属的完整 scope 链字符串。

    返回示例: "MyClass", "MyClass.my_method", ""(模块级)
    """
    scope_map = _build_python_scope_map(text)
    scope, _sig, _parent = _find_scope_in_map(scope_map, line_number)
    return scope


# ─── 头部上下文注入 ───────────────────────────────────────

def _format_header(file_path, line_start, line_end, scope="", signature="",
                   parent_class_sig=""):
    """格式化 chunk 头部注入字符串。"""
    parts = [f"[File: {file_path}]"]
    if scope:
        if "." in scope:
            class_part, method_part = scope.rsplit(".", 1)
            if parent_class_sig:
                parts.append(f"[Class: {parent_class_sig}]")
            else:
                parts.append(f"[Class: {class_part}]")
            parts.append(f"[Method: {method_part}]")
        else:
            parts.append(f"[Scope: {scope}]")
    if signature:
        parts.append(f"[Sig: {signature}]")
    if line_start and line_end:
        parts.append(f"[Lines: {line_start}-{line_end}]")
    return "# " + " ".join(parts)


def _find_scope_in_map(scope_map, line_number):
    """从预构建的 scope_map 中查找指定行号的最内层 scope。
    返回 (scope_str, signature, parent_class_sig) 元组。
    parent_class_sig: 如果当前 scope 是方法（如 Cls.method），返回父类的签名（含继承链）。"""
    best_scope = ""
    best_sig = ""
    best_size = float('inf')
    parent_class_sig = ""
    for entry in scope_map:
        s_start, s_end, s_str = entry[0], entry[1], entry[2]
        sig = entry[3] if len(entry) > 3 else ""
        if s_start <= line_number <= s_end:
            size = s_end - s_start
            if size < best_size:
                best_size = size
                best_scope = s_str
                best_sig = sig
    if "." in best_scope:
        class_name = best_scope.rsplit(".", 1)[0]
        for entry in scope_map:
            if entry[2] == class_name:
                parent_class_sig = entry[3] if len(entry) > 3 else ""
                break
    return best_scope, best_sig, parent_class_sig


def enrich_chunks(chunks, full_text, file_path="", file_ext=""):
    """为 chunks 注入头部上下文信息，返回 (enriched_chunks, line_ranges, scopes)。

    头部注入在 embedding 前完成，让向量包含上下文信息。
    line_ranges 和 scopes 用于存入 metadata。
    """
    if not chunks:
        return [], [], []

    line_ranges = compute_line_ranges(full_text, chunks)

    scope_map = []
    if file_ext.lower() == ".py":
        scope_map = _build_python_scope_map(full_text)

    enriched = []
    scopes = []
    for i, chunk in enumerate(chunks):
        ls, le = line_ranges[i]
        if scope_map and ls > 0:
            scope, sig, parent_cls_sig = _find_scope_in_map(scope_map, ls)
        else:
            scope, sig, parent_cls_sig = "", "", ""
        scopes.append(scope)
        header = _format_header(file_path, ls, le, scope, sig, parent_cls_sig)
        enriched.append(f"{header}\n{chunk}")

    return enriched, line_ranges, scopes


def collect_files(path, file_extensions=None):
    """收集路径下所有文本文件（支持单文件或递归目录）。

    Args:
        path: 文件或目录路径。
        file_extensions: 可选，限定的后缀列表（如 [".py", ".md"]）。
                         传入时只收集这些后缀；不传则使用 TEXT_EXTENSIONS 全集。
                         后缀不区分大小写，自动补 "." 前缀（"py" → ".py"）。
    """
    if file_extensions is not None:
        allowed = set()
        for ext in file_extensions:
            ext = ext.strip().lower()
            if not ext.startswith("."):
                ext = "." + ext
            allowed.add(ext)
    else:
        allowed = TEXT_EXTENSIONS

    if os.path.isfile(path):
        ext = os.path.splitext(path)[1].lower()
        if ext in allowed:
            return [path]
        return []
    files = []
    for root, _, fnames in os.walk(path):
        for fn in sorted(fnames):
            if os.path.splitext(fn)[1].lower() in allowed:
                files.append(os.path.join(root, fn))
    return files

`````

--- **end of file: nbrag/chunker.py** (project: nbrag) --- 

---


--- **start of file: nbrag/config.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/config.py`

#### 📝 Module Docstring

`````
配置加载模块 — CLI > 环境变量 > YAML 配置文件 > 默认值。

最小启动只需要一个环境变量:
    export NBRAG_API_KEY=sk-xxx
    uvx nbrag
`````

#### 📦 Imports

- `import os`
- `from dataclasses import dataclass`
- `from dataclasses import field`
- `import yaml`

#### 🏛️ Classes (5)

##### 📌 `class EmbeddingConfig`
*Line: 14*

**Class Variables (3):**
- `api_key: str = ''`
- `base_url: str = 'https://api.siliconflow.cn/v1'`
- `model: str = 'BAAI/bge-m3'`

##### 📌 `class RerankConfig`
*Line: 21*

**Class Variables (1):**
- `model: str = 'BAAI/bge-reranker-v2-m3'`

##### 📌 `class StorageConfig`
*Line: 26*

**Class Variables (2):**
- `db_path: str = './rag_db'`
- `raw_files_path: str = ''`

##### 📌 `class ChunkingConfig`
*Line: 32*

**Class Variables (2):**
- `chunk_size: int = 1500`
- `chunk_overlap: int = 200`

##### 📌 `class RagConfig`
*Line: 38*

**Class Variables (4):**
- `embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)`
- `rerank: RerankConfig = field(default_factory=RerankConfig)`
- `storage: StorageConfig = field(default_factory=StorageConfig)`
- `chunking: ChunkingConfig = field(default_factory=ChunkingConfig)`

#### 🔧 Public Functions (2)

- `def load_config(cli_args = None) -> RagConfig`
  - *Line: 89*
  - *加载配置：CLI > 环境变量 > YAML > 默认值。*

- `def get_config() -> RagConfig`
  - *Line: 164*
  - *获取当前配置（未加载时自动从环境变量加载）。*


---

`````python
"""
配置加载模块 — CLI > 环境变量 > YAML 配置文件 > 默认值。

最小启动只需要一个环境变量:
    export NBRAG_API_KEY=sk-xxx
    uvx nbrag
"""

import os
from dataclasses import dataclass, field


@dataclass
class EmbeddingConfig:
    api_key: str = ""
    base_url: str = "https://api.siliconflow.cn/v1"
    model: str = "BAAI/bge-m3"


@dataclass
class RerankConfig:
    model: str = "BAAI/bge-reranker-v2-m3"


@dataclass
class StorageConfig:
    db_path: str = "./rag_db"
    raw_files_path: str = ""  # 默认 db_path/raw_files


@dataclass
class ChunkingConfig:
    chunk_size: int = 1500
    chunk_overlap: int = 200


@dataclass
class RagConfig:
    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)
    rerank: RerankConfig = field(default_factory=RerankConfig)
    storage: StorageConfig = field(default_factory=StorageConfig)
    chunking: ChunkingConfig = field(default_factory=ChunkingConfig)

    def __post_init__(self):
        if not self.storage.raw_files_path:
            self.storage.raw_files_path = os.path.join(self.storage.db_path, "raw_files")


_config: RagConfig = None


def _load_yaml(path):
    """加载 YAML 配置文件，返回 dict（文件不存在返回空 dict）。"""
    if not path or not os.path.isfile(path):
        return {}
    try:
        import yaml
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _find_config_file():
    """按优先级查找配置文件。"""
    candidates = [
        os.path.join(os.getcwd(), "nbrag_config.yaml"),
        os.path.join(os.getcwd(), "nbrag_config.yml"),
        os.path.expanduser("~/.config/nbrag/config.yaml"),
        os.path.expanduser("~/.config/nbrag/config.yml"),
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None


def _resolve_env_ref(value):
    """解析 ${VAR_NAME} 环境变量引用。"""
    if not isinstance(value, str):
        return value
    if value.startswith("${") and value.endswith("}"):
        var_name = value[2:-1]
        return os.environ.get(var_name, "")
    return value


def load_config(cli_args=None) -> RagConfig:
    """加载配置：CLI > 环境变量 > YAML > 默认值。"""
    global _config

    yaml_path = None
    if cli_args and hasattr(cli_args, 'config') and cli_args.config:
        yaml_path = cli_args.config
    else:
        yaml_path = os.environ.get("NBRAG_CONFIG", None) or _find_config_file()

    yaml_data = _load_yaml(yaml_path)

    embedding_data = yaml_data.get("embedding", {})
    rerank_data = yaml_data.get("rerank", {})
    storage_data = yaml_data.get("storage", {})
    chunking_data = yaml_data.get("chunking", {})

    api_key = (
        (getattr(cli_args, 'api_key', None) if cli_args else None)
        or os.environ.get("NBRAG_API_KEY", "")
        or _resolve_env_ref(embedding_data.get("api_key", ""))
    )

    base_url = (
        os.environ.get("NBRAG_BASE_URL", "")
        or embedding_data.get("base_url", "")
        or "https://api.siliconflow.cn/v1"
    )

    embedding_model = (
        os.environ.get("NBRAG_EMBEDDING_MODEL", "")
        or embedding_data.get("model", "")
        or "BAAI/bge-m3"
    )

    rerank_model = (
        os.environ.get("NBRAG_RERANK_MODEL", "")
        or rerank_data.get("model", "")
        or "BAAI/bge-reranker-v2-m3"
    )

    db_path = (
        (getattr(cli_args, 'db_path', None) if cli_args else None)
        or os.environ.get("NBRAG_DB_PATH", "")
        or storage_data.get("db_path", "")
        or "./rag_db"
    )

    raw_files_path = (
        os.environ.get("NBRAG_RAW_FILES_PATH", "")
        or storage_data.get("raw_files_path", "")
        or ""
    )

    chunk_size = int(
        os.environ.get("NBRAG_CHUNK_SIZE", "0")
        or chunking_data.get("chunk_size", 0)
        or 1500
    )

    chunk_overlap = int(
        os.environ.get("NBRAG_CHUNK_OVERLAP", "0")
        or chunking_data.get("chunk_overlap", 0)
        or 200
    )

    _config = RagConfig(
        embedding=EmbeddingConfig(api_key=api_key, base_url=base_url, model=embedding_model),
        rerank=RerankConfig(model=rerank_model),
        storage=StorageConfig(db_path=db_path, raw_files_path=raw_files_path),
        chunking=ChunkingConfig(chunk_size=chunk_size, chunk_overlap=chunk_overlap),
    )
    return _config


def get_config() -> RagConfig:
    """获取当前配置（未加载时自动从环境变量加载）。"""
    global _config
    if _config is None:
        load_config()
    return _config

`````

--- **end of file: nbrag/config.py** (project: nbrag) --- 

---


--- **start of file: nbrag/core.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/core.py`

#### 📝 Module Docstring

`````
RAG 核心逻辑 —— 供 MCP 服务和独立脚本共同复用。

功能:
  - Embedding / Rerank API 调用（默认 SiliconFlow，可配置任何 OpenAI 兼容 API）
  - ChromaDB 向量存储（CRUD + 搜索）
  - 文件导入（切分 + enrichment + 存储）

分块增强逻辑（切分、行号、AST scope、头部注入）在 chunker.py 中。
配置从环境变量 / YAML 文件 / CLI 参数加载（见 config.py）。
`````

#### 📦 Imports

- `import os`
- `import hashlib`
- `import httpx`
- `import chromadb`
- `from nbrag.config import get_config`
- `from nbrag.chunker import chunk_text`
- `from nbrag.chunker import enrich_chunks`
- `from nbrag.chunker import collect_files`
- `from nbrag.chunker import DEFAULT_CHUNK_SIZE`
- `from nbrag.chunker import DEFAULT_CHUNK_OVERLAP`
- `import time as _time`
- `import time as _time`
- `import time as _time`
- `import shutil`
- `import time as _time`
- `from concurrent.futures import ThreadPoolExecutor`
- `from concurrent.futures import as_completed`
- `import re`
- `import re`
- `import ast as _ast`
- `import warnings as _warnings`
- `from nbrag.chunker import _extract_signature`

#### 🔧 Public Functions (17)

- `def invalidate_doc_id_cache(collection_name = None)`
  - *Line: 85*
  - *清除 doc_id 映射缓存（导入/删除 collection 后调用）。*

- `def get_collection(name = 'default')`
  - *Line: 105*
  - *获取或创建一个 ChromaDB collection（写操作用）。*

- `def delete_collection(name)`
  - *Line: 120*
  - *删除整个 collection（清空该知识库）。*

- `def list_collections()`
  - *Line: 126*
  - *列出所有 collection。*

- `def embed(texts, max_retries = 3)`
  - *Line: 140*
  - *调用 Embedding API，自动分批，失败自动重试。*

- `def rerank(query, documents, top_n = 5, max_retries = 3)`
  - *Line: 180*
  - *调用 Rerank API，返回重排后的索引列表，失败自动重试。*

- `def ingest_file(file_path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP)`
  - *Line: 368*
  - *导入单个文件到知识库，返回结果 dict（串行版本，兼容旧调用）。*

- `def ingest_path(path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None)`
  - *Line: 378*
  - *导入文件或目录到知识库。返回 (results_list, errors_list, skipped_count)。*

- `def batch_ingest(paths, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None, delete_first = False, on_progress = None, verbose = False, max_workers = 1)`
  - *Line: 409*
  - **Docstring:**
  `````
  批量导入多个路径到知识库（一站式封装）。
  
  两阶段流水线设计：
    阶段 1（可并行）：读取文件 → 文本切分 → 调用 Embedding API 获取向量
    阶段 2（必须串行）：写入 ChromaDB + 缓存原始文件
  
  Embedding API 调用是 I/O 密集型（网络等待），是整个导入流程的主要瓶颈。
  通过 max_workers > 1 可以并行执行阶段 1，显著加速大批量导入。
  ChromaDB（SQLite 底层）不支持并发写，所以阶段 2 始终串行。
  
  Args:
      paths: 文件/目录路径列表（或单个字符串）。
      collection_name: 知识库名称，不存在时自动创建。
      chunk_size: 分块大小（字符数），默认 1500。
      chunk_overlap: 分块重叠（字符数），默认 200。
      file_extensions: 可选后缀过滤列表（如 [".py", ".md"]），None 表示全部文本文件。
      delete_first: 是否先清空旧数据再导入（适用于全量重建）。
      on_progress: 可选回调 fn(current, total, file_path, result)，用于自定义进度展示。
      verbose: 是否打印详细日志。
      max_workers: Embedding 并发线程数。
                   1 = 串行（默认，兼容旧行为）；
                   2-4 = 并行读取+Embedding，串行写入 ChromaDB。
                   不建议超过 4，避免触发 Embedding API 频率限制。
  `````

- `def search(query, collection_name = 'default', top_k = 5, use_rerank = True, filter_filename = None)`
  - *Line: 586*
  - *语义搜索。返回 (documents, metadatas, distances, rerank_used, total)。*

- `def get_file_chunks(file_identifier, collection_name = 'default', start_chunk = 0, max_chunks = 5, raw = False, line_start = -1, line_end = -1)`
  - *Line: 636*
  - *按文件路径或文件名获取知识库中该文件的内容。*

- `def get_context_chunks(doc_id, collection_name = 'default', chunk_index = None, window = 2, line_start = None, line_end = None)`
  - *Line: 756*
  - *获取指定文档的上下文 chunks。*

- `def grep_knowledge(keyword, collection_name = 'default', max_results = 10, case_sensitive = False, filter_filename = None, context_lines = 5)`
  - *Line: 817*
  - *在知识库的原始缓存文件中进行关键词/正则搜索。*

- `def find_symbol_definition(symbol, collection_name = 'default', max_results = 5)`
  - *Line: 873*
  - *在知识库中查找符号（类/函数/方法）的完整定义。*

- `def list_documents(collection_name = 'default')`
  - *Line: 984*
  - *列出知识库中已导入的文档。*

- `def delete_document(doc_id, collection_name = 'default')`
  - *Line: 1010*
  - *删除指定文档的所有向量数据及缓存文件。返回 (deleted_count, filename)。*

- `def get_stats()`
  - *Line: 1030*
  - *返回所有知识库的统计信息。*


---

`````python
"""
RAG 核心逻辑 —— 供 MCP 服务和独立脚本共同复用。

功能:
  - Embedding / Rerank API 调用（默认 SiliconFlow，可配置任何 OpenAI 兼容 API）
  - ChromaDB 向量存储（CRUD + 搜索）
  - 文件导入（切分 + enrichment + 存储）

分块增强逻辑（切分、行号、AST scope、头部注入）在 chunker.py 中。
配置从环境变量 / YAML 文件 / CLI 参数加载（见 config.py）。
"""

import os
import hashlib

import httpx
import chromadb
from nbrag.config import get_config
from nbrag.chunker import (
    chunk_text, enrich_chunks, collect_files,
    DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP,
)


def _cfg():
    return get_config()


# ─── 延迟初始化的全局对象 ──────────────────────────────────

_chroma_client = None
_data_dir_initialized = False


def _ensure_dirs():
    global _data_dir_initialized
    if _data_dir_initialized:
        return
    cfg = _cfg()
    os.makedirs(cfg.storage.db_path, exist_ok=True)
    os.makedirs(cfg.storage.raw_files_path, exist_ok=True)
    _data_dir_initialized = True


def _get_chroma():
    global _chroma_client
    if _chroma_client is None:
        _ensure_dirs()
        _chroma_client = chromadb.PersistentClient(path=_cfg().storage.db_path)
    return _chroma_client


EMBEDDING_BATCH_SIZE = 32
CHROMA_UPSERT_BATCH = 5000

_doc_id_cache = {}
_doc_id_cache_ts = {}


def _get_doc_id_map(collection_name):
    """获取 collection 的 doc_id → {filename, source} 映射（带 60s 内存缓存）。"""
    import time as _time
    now = _time.time()
    if (collection_name in _doc_id_cache
            and now - _doc_id_cache_ts.get(collection_name, 0) < 60):
        return _doc_id_cache[collection_name]

    col = _get_existing_collection(collection_name)
    if col is None:
        return {}
    all_meta = col.get(include=["metadatas"])
    mapping = {}
    for meta in all_meta["metadatas"]:
        did = meta.get("doc_id", "")
        if did and did not in mapping:
            mapping[did] = {
                "filename": meta.get("filename", "?"),
                "source": meta.get("source", "?"),
            }
    _doc_id_cache[collection_name] = mapping
    _doc_id_cache_ts[collection_name] = now
    return mapping


def invalidate_doc_id_cache(collection_name=None):
    """清除 doc_id 映射缓存（导入/删除 collection 后调用）。"""
    if collection_name:
        _doc_id_cache.pop(collection_name, None)
        _doc_id_cache_ts.pop(collection_name, None)
    else:
        _doc_id_cache.clear()
        _doc_id_cache_ts.clear()


def _normalize_path(path):
    """统一路径格式（跨平台兼容）。"""
    p = os.path.abspath(path).replace("\\", "/")
    if len(p) >= 2 and p[1] == ':':
        p = p[0].upper() + p[1:]
    return p


# ─── 底层工具函数 ─────────────────────────────────────────

def get_collection(name="default"):
    """获取或创建一个 ChromaDB collection（写操作用）。"""
    return _get_chroma().get_or_create_collection(
        name=name, metadata={"hnsw:space": "cosine"},
    )


def _get_existing_collection(name):
    """获取已存在的 collection，不存在时返回 None（只读操作用，避免自动创建空 collection）。"""
    try:
        return _get_chroma().get_collection(name=name)
    except (ValueError, Exception):
        return None


def delete_collection(name):
    """删除整个 collection（清空该知识库）。"""
    _get_chroma().delete_collection(name)
    invalidate_doc_id_cache(name)


def list_collections():
    """列出所有 collection。"""
    return _get_chroma().list_collections()


_http_client = None

def _get_http_client():
    global _http_client
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.Client(timeout=120)
    return _http_client


def embed(texts, max_retries=3):
    """调用 Embedding API，自动分批，失败自动重试。"""
    cfg = _cfg()
    api_key = cfg.embedding.api_key
    if not api_key:
        raise ValueError(
            "NBRAG_API_KEY is empty. Set the environment variable or configure in nbrag_config.yaml"
        )
    import time as _time
    client = _get_http_client()
    all_embeddings = []
    for i in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[i:i + EMBEDDING_BATCH_SIZE]
        for attempt in range(max_retries):
            try:
                resp = client.post(
                    f"{cfg.embedding.base_url}/embeddings",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": cfg.embedding.model,
                        "input": batch,
                        "encoding_format": "float",
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                sorted_data = sorted(data["data"], key=lambda x: x["index"])
                all_embeddings.extend([d["embedding"] for d in sorted_data])
                break
            except Exception:
                if attempt < max_retries - 1:
                    _time.sleep(2 ** attempt)
                else:
                    raise
    return all_embeddings


def rerank(query, documents, top_n=5, max_retries=3):
    """调用 Rerank API，返回重排后的索引列表，失败自动重试。"""
    import time as _time
    cfg = _cfg()
    if not cfg.embedding.api_key or not cfg.rerank.model:
        return list(range(min(top_n, len(documents))))

    client = _get_http_client()
    for attempt in range(max_retries):
        try:
            resp = client.post(
                f"{cfg.embedding.base_url}/rerank",
                headers={
                    "Authorization": f"Bearer {cfg.embedding.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": cfg.rerank.model,
                    "query": query,
                    "documents": documents,
                    "top_n": top_n,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return [r["index"] for r in data["results"]]
        except Exception:
            if attempt < max_retries - 1:
                _time.sleep(2 ** attempt)
            else:
                raise


# ─── 原始文件缓存 ─────────────────────────────────────────

def _raw_files_dir():
    return _cfg().storage.raw_files_path


def _raw_file_dir(collection_name):
    d = os.path.join(_raw_files_dir(), collection_name)
    os.makedirs(d, exist_ok=True)
    return d


def _raw_file_path(collection_name, doc_id, ext=""):
    return os.path.join(_raw_file_dir(collection_name), f"{doc_id}{ext}")


def _cache_raw_file(text, collection_name, doc_id, ext=""):
    """将原始文件内容缓存到 raw_files/ 目录。"""
    path = _raw_file_path(collection_name, doc_id, ext)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def _delete_raw_file(collection_name, doc_id):
    """删除缓存的原始文件（尝试所有可能的扩展名）。"""
    d = os.path.join(_raw_files_dir(), collection_name)
    if not os.path.isdir(d):
        return
    prefix = f"{doc_id}"
    for fname in os.listdir(d):
        if fname.startswith(prefix):
            try:
                os.remove(os.path.join(d, fname))
            except OSError:
                pass


def _read_raw_file(collection_name, doc_id):
    """读取缓存的原始文件，返回 (content, cached_path) 或 (None, None)。"""
    d = os.path.join(_raw_files_dir(), collection_name)
    if not os.path.isdir(d):
        return None, None
    prefix = f"{doc_id}"
    for fname in os.listdir(d):
        if fname.startswith(prefix):
            fpath = os.path.join(d, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                    return f.read(), fpath
            except OSError:
                return None, None
    return None, None


def _delete_raw_files_collection(collection_name):
    """删除某个 collection 的全部缓存文件。"""
    import shutil
    d = os.path.join(_raw_files_dir(), collection_name)
    if os.path.isdir(d):
        shutil.rmtree(d, ignore_errors=True)


# ─── 高级操作 ─────────────────────────────────────────────

def _prepare_file(file_path, chunk_size=DEFAULT_CHUNK_SIZE,
                  chunk_overlap=DEFAULT_CHUNK_OVERLAP):
    """阶段 1：读取 + 切分 + Embedding（无 DB 操作，可并行）。"""
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        return {"ok": False, "error": f"Cannot read {file_path}: {e}"}

    if not text.strip():
        return {"ok": False, "skipped": True, "reason": f"Empty file: {os.path.basename(file_path)}"}

    file_ext = os.path.splitext(file_path)[1]
    abs_path = _normalize_path(file_path)
    raw_chunks = chunk_text(text, chunk_size, chunk_overlap, file_ext=file_ext)
    if not raw_chunks:
        return {"ok": False, "skipped": True, "reason": f"No chunks after split: {os.path.basename(file_path)}"}

    enriched_chunks, line_ranges, scopes = enrich_chunks(
        raw_chunks, text, file_path=abs_path, file_ext=file_ext,
    )

    embeddings = embed(enriched_chunks)

    filename = os.path.basename(file_path)
    doc_id = hashlib.md5(abs_path.encode()).hexdigest()[:12]

    return {
        "ok": True, "filename": filename, "file_ext": file_ext,
        "text": text, "abs_path": abs_path, "doc_id": doc_id,
        "enriched_chunks": enriched_chunks, "embeddings": embeddings,
        "line_ranges": line_ranges, "scopes": scopes,
        "chars": len(text), "chunks": len(enriched_chunks),
    }


def _write_to_db(prepared, collection_name="default"):
    """阶段 2：写入 ChromaDB + 缓存原文（必须串行）。"""
    if not prepared["ok"]:
        return prepared

    text = prepared["text"]
    abs_path = prepared["abs_path"]
    filename = prepared["filename"]
    doc_id = prepared["doc_id"]
    file_ext = prepared["file_ext"]
    enriched_chunks = prepared["enriched_chunks"]
    embeddings = prepared["embeddings"]
    line_ranges = prepared["line_ranges"]
    scopes = prepared["scopes"]

    _cache_raw_file(text, collection_name, doc_id, file_ext)

    col = get_collection(collection_name)

    try:
        old_data = col.get(where={"doc_id": doc_id}, include=[])
        if old_data["ids"]:
            col.delete(ids=old_data["ids"])
    except Exception:
        pass

    ids = [f"{doc_id}_c{i}" for i in range(len(enriched_chunks))]
    metadatas = [
        {
            "source": abs_path,
            "filename": filename,
            "doc_id": doc_id,
            "chunk_index": i,
            "total_chunks": len(enriched_chunks),
            "line_start": line_ranges[i][0],
            "line_end": line_ranges[i][1],
            "scope": scopes[i],
        }
        for i in range(len(enriched_chunks))
    ]

    for start in range(0, len(ids), CHROMA_UPSERT_BATCH):
        end = start + CHROMA_UPSERT_BATCH
        col.upsert(
            ids=ids[start:end],
            documents=enriched_chunks[start:end],
            embeddings=embeddings[start:end],
            metadatas=metadatas[start:end],
        )
    return {
        "ok": True, "filename": filename,
        "chars": prepared["chars"], "chunks": prepared["chunks"], "doc_id": doc_id,
    }


def ingest_file(file_path, collection_name="default",
                chunk_size=DEFAULT_CHUNK_SIZE,
                chunk_overlap=DEFAULT_CHUNK_OVERLAP):
    """导入单个文件到知识库，返回结果 dict（串行版本，兼容旧调用）。"""
    prepared = _prepare_file(file_path, chunk_size, chunk_overlap)
    if not prepared["ok"]:
        return prepared
    return _write_to_db(prepared, collection_name)


def ingest_path(path, collection_name="default",
                chunk_size=DEFAULT_CHUNK_SIZE,
                chunk_overlap=DEFAULT_CHUNK_OVERLAP,
                file_extensions=None):
    """导入文件或目录到知识库。返回 (results_list, errors_list, skipped_count)。"""
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return [], [f"Path not found: {path}"], 0

    files = collect_files(path, file_extensions=file_extensions)
    if not files:
        return [], [f"No text files found in: {path}"], 0

    results = []
    errors = []
    skipped = []
    for fp in files:
        try:
            r = ingest_file(fp, collection_name, chunk_size, chunk_overlap)
        except Exception as e:
            r = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}"}
        if r["ok"]:
            results.append(r)
        elif r.get("skipped"):
            skipped.append(r["reason"])
        else:
            errors.append(r["error"])

    return results, errors, len(skipped)


def batch_ingest(paths, collection_name="default",
                 chunk_size=DEFAULT_CHUNK_SIZE,
                 chunk_overlap=DEFAULT_CHUNK_OVERLAP,
                 file_extensions=None,
                 delete_first=False, on_progress=None,
                 verbose=False, max_workers=1):
    """批量导入多个路径到知识库（一站式封装）。

    两阶段流水线设计：
      阶段 1（可并行）：读取文件 → 文本切分 → 调用 Embedding API 获取向量
      阶段 2（必须串行）：写入 ChromaDB + 缓存原始文件

    Embedding API 调用是 I/O 密集型（网络等待），是整个导入流程的主要瓶颈。
    通过 max_workers > 1 可以并行执行阶段 1，显著加速大批量导入。
    ChromaDB（SQLite 底层）不支持并发写，所以阶段 2 始终串行。

    Args:
        paths: 文件/目录路径列表（或单个字符串）。
        collection_name: 知识库名称，不存在时自动创建。
        chunk_size: 分块大小（字符数），默认 1500。
        chunk_overlap: 分块重叠（字符数），默认 200。
        file_extensions: 可选后缀过滤列表（如 [".py", ".md"]），None 表示全部文本文件。
        delete_first: 是否先清空旧数据再导入（适用于全量重建）。
        on_progress: 可选回调 fn(current, total, file_path, result)，用于自定义进度展示。
        verbose: 是否打印详细日志。
        max_workers: Embedding 并发线程数。
                     1 = 串行（默认，兼容旧行为）；
                     2-4 = 并行读取+Embedding，串行写入 ChromaDB。
                     不建议超过 4，避免触发 Embedding API 频率限制。
    """
    import time as _time
    from concurrent.futures import ThreadPoolExecutor, as_completed

    if isinstance(paths, str):
        paths = [paths]

    t0 = _time.time()

    if delete_first:
        deleted_col = False
        try:
            delete_collection(collection_name)
            deleted_col = True
        except Exception:
            pass
        try:
            _delete_raw_files_collection(collection_name)
        except Exception:
            pass
        if verbose:
            print(f"[rag] Deleted old collection: {collection_name}"
                  f" (collection={'ok' if deleted_col else 'not found'}, raw_files=cleaned)")

    all_files = []
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.exists(p):
            found = collect_files(p, file_extensions=file_extensions)
            if verbose:
                ext_info = f" (filter: {file_extensions})" if file_extensions else ""
                print(f"[rag] {p} -> {len(found)} files{ext_info}")
            all_files.extend(found)

    if verbose:
        mode_str = f"parallel(workers={max_workers})" if max_workers > 1 else "sequential"
        print(f"[rag] Total {len(all_files)} files, mode: {mode_str}, starting Embedding...\n")

    results = []
    errors = []
    skipped = []
    total_chars = 0
    total_chunks = 0
    large_files = []

    for fp in all_files:
        file_size = os.path.getsize(fp)
        if file_size > 100 * 1024:
            large_files.append((fp, file_size))
            if verbose:
                print(f"  [large] {fp} ({file_size / 1024:.1f} KB)")

    if max_workers <= 1:
        prepared_list = []
        for i, fp in enumerate(all_files):
            try:
                p = _prepare_file(fp, chunk_size, chunk_overlap)
            except Exception as e:
                p = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}", "_fp": fp}
            p["_fp"] = fp
            p["_idx"] = i
            prepared_list.append(p)
            if verbose:
                name = os.path.basename(fp)
                if p["ok"]:
                    print(f"  [embed {i + 1:>4}/{len(all_files)}] {name} ({p['chunks']} chunks)")
                elif p.get("skipped"):
                    print(f"  [embed {i + 1:>4}/{len(all_files)}] - {name}  (skipped)")
    else:
        prepared_list = [None] * len(all_files)
        done_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            future_to_idx = {}
            for i, fp in enumerate(all_files):
                fut = pool.submit(_prepare_file, fp, chunk_size, chunk_overlap)
                future_to_idx[fut] = (i, fp)

            for fut in as_completed(future_to_idx):
                i, fp = future_to_idx[fut]
                try:
                    p = fut.result()
                except Exception as e:
                    p = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}"}
                p["_fp"] = fp
                p["_idx"] = i
                prepared_list[i] = p
                done_count += 1
                if verbose:
                    name = os.path.basename(fp)
                    if p["ok"]:
                        print(f"  [embed {done_count:>4}/{len(all_files)}] {name} ({p['chunks']} chunks)")
                    elif p.get("skipped"):
                        print(f"  [embed {done_count:>4}/{len(all_files)}] - {name}  (skipped)")

    if verbose:
        embed_elapsed = _time.time() - t0
        print(f"\n[rag] Embedding done in {embed_elapsed:.1f}s, writing to ChromaDB...\n")

    for i, p in enumerate(prepared_list):
        fp = p.get("_fp", "?")
        try:
            r = _write_to_db(p, collection_name) if p["ok"] else p
        except Exception as e:
            r = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}"}

        if r["ok"]:
            results.append(r)
            total_chars += r["chars"]
            total_chunks += r["chunks"]
        elif r.get("skipped"):
            skipped.append(r.get("reason", ""))
        else:
            errors.append(r.get("error", "unknown error"))

        if on_progress:
            on_progress(i + 1, len(all_files), fp, r)
        elif verbose:
            idx = i + 1
            name = os.path.basename(fp)
            if r["ok"]:
                print(f"  [write {idx:>4}/{len(all_files)}] {name} ({r['chunks']} chunks)")
            elif not r.get("skipped"):
                print(f"  [write {idx:>4}/{len(all_files)}] X {name}  ({r.get('error', '')})")

    elapsed = _time.time() - t0
    stats = {
        "success": len(results), "failed": len(errors), "skipped": len(skipped),
        "total_chars": total_chars, "total_chunks": total_chunks,
        "file_count": len(all_files), "elapsed": elapsed,
        "results": results, "errors": errors, "skipped_reasons": skipped,
        "large_files": large_files,
    }

    if verbose:
        skip_str = f" {stats['skipped']} skipped" if skipped else ""
        print(f"\n[rag] Done! {stats['success']} ok {stats['failed']} failed{skip_str}"
              f" | {total_chunks} chunks {total_chars:,} chars | {elapsed:.0f}s")
        if large_files:
            print(f"\n[rag] Large files (>100KB) summary ({len(large_files)}):")
            large_files_sorted = sorted(large_files, key=lambda x: x[1], reverse=True)
            for fp, size in large_files_sorted:
                print(f"  {size / 1024:.1f} KB  {fp}")
            total_large_size = sum(s for _, s in large_files)
            print(f"  Total: {len(large_files)} files, {total_large_size / 1024 / 1024:.2f} MB")

    return stats


def search(query, collection_name="default", top_k=5, use_rerank=True,
           filter_filename=None):
    """语义搜索。返回 (documents, metadatas, distances, rerank_used, total)。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return [], [], [], False, 0
    total = col.count()

    if total == 0:
        return [], [], [], False, 0

    query_vec = embed([query])[0]
    retrieve_k = min(top_k * 4, total) if use_rerank else min(top_k, total)

    where_filter = None
    if filter_filename:
        where_filter = {"filename": filter_filename}

    results = col.query(
        query_embeddings=[query_vec],
        n_results=retrieve_k,
        where=where_filter,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    cfg = _cfg()
    rerank_used = False
    if use_rerank and cfg.rerank.model and len(documents) > top_k:
        try:
            reranked_idx = rerank(query, documents, top_n=top_k)
            documents = [documents[i] for i in reranked_idx]
            metadatas = [metadatas[i] for i in reranked_idx]
            distances = [distances[i] for i in reranked_idx]
            rerank_used = True
        except Exception:
            documents = documents[:top_k]
            metadatas = metadatas[:top_k]
            distances = distances[:top_k]
    else:
        documents = documents[:top_k]
        metadatas = metadatas[:top_k]
        distances = distances[:top_k]

    return documents, metadatas, distances, rerank_used, total


def get_file_chunks(file_identifier, collection_name="default",
                    start_chunk=0, max_chunks=5,
                    raw=False, line_start=-1, line_end=-1):
    """按文件路径或文件名获取知识库中该文件的内容。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return {"found": False, "error": f"collection '{collection_name}' does not exist"}
    total = col.count()
    if total == 0:
        return {"found": False, "error": f"collection '{collection_name}' is empty"}

    all_data = _query_file_by_identifier(col, file_identifier)

    if not all_data["ids"]:
        return {"found": False, "error": f"File not found: '{file_identifier}'"}

    items = list(zip(all_data["ids"], all_data["documents"], all_data["metadatas"]))
    items.sort(key=lambda x: x[2].get("chunk_index", 0))

    first_meta = items[0][2]
    total_chunks = len(items)
    max_line = max(m.get("line_end", 0) for _, _, m in items)
    doc_id = first_meta.get("doc_id", "?")
    source = first_meta.get("source", "?")
    actual_filename = first_meta.get("filename", "?")

    if raw:
        return _get_raw_file_result(
            collection_name, doc_id, source, actual_filename,
            total_chunks, max_line, line_start, line_end,
        )

    chunk_line_ranges = [
        (m.get("line_start", 0), m.get("line_end", 0)) for _, _, m in items
    ]

    end_chunk = min(start_chunk + max_chunks, total_chunks)
    selected = items[start_chunk:end_chunk]

    chunks = []
    for _, doc, meta in selected:
        chunks.append({
            "index": meta.get("chunk_index", 0),
            "line_start": meta.get("line_start", 0),
            "line_end": meta.get("line_end", 0),
            "scope": meta.get("scope", ""),
            "content": doc,
        })

    return {
        "found": True,
        "source": source,
        "filename": actual_filename,
        "doc_id": doc_id,
        "total_chunks": total_chunks,
        "total_lines": max_line,
        "chunk_line_ranges": chunk_line_ranges,
        "chunks": chunks,
        "start_chunk": start_chunk,
        "end_chunk": end_chunk,
    }


def _query_file_by_identifier(col, file_identifier):
    """按路径或文件名查找文件的 chunks。"""
    is_path = ('/' in file_identifier or '\\' in file_identifier)
    empty = {"ids": [], "documents": [], "metadatas": []}

    if is_path:
        normalized = _normalize_path(file_identifier)
        try:
            result = col.get(where={"source": normalized}, include=["documents", "metadatas"])
            if result["ids"]:
                return result
        except Exception:
            pass
        basename = os.path.basename(file_identifier)
        try:
            return col.get(where={"filename": basename}, include=["documents", "metadatas"])
        except Exception:
            return empty

    try:
        return col.get(where={"filename": file_identifier}, include=["documents", "metadatas"])
    except Exception:
        return empty


def _get_raw_file_result(collection_name, doc_id, source, filename,
                         total_chunks, total_lines, line_start, line_end):
    """从缓存读取原始文件，支持按行截取。"""
    content, cached_path = _read_raw_file(collection_name, doc_id)
    if content is None:
        return {
            "found": False,
            "error": f"Raw file cache not found (doc_id={doc_id}). "
                     f"This file may have been imported before caching was enabled. Please re-import.",
        }

    lines = content.splitlines(keepends=True)
    actual_total = len(lines)

    ls = max(1, line_start) if line_start > 0 else 1
    le = min(actual_total, line_end) if line_end > 0 else actual_total
    selected_lines = lines[ls - 1:le]

    return {
        "found": True,
        "raw": True,
        "source": source,
        "filename": filename,
        "doc_id": doc_id,
        "total_chunks": total_chunks,
        "total_lines": actual_total,
        "line_start": ls,
        "line_end": le,
        "content": "".join(selected_lines),
    }


def get_context_chunks(doc_id, collection_name="default",
                       chunk_index=None, window=2,
                       line_start=None, line_end=None):
    """获取指定文档的上下文 chunks。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return {"found": False, "error": f"collection '{collection_name}' does not exist"}

    try:
        all_data = col.get(
            where={"doc_id": doc_id},
            include=["documents", "metadatas"],
        )
    except Exception:
        all_data = {"ids": [], "documents": [], "metadatas": []}

    if not all_data["ids"]:
        return {"found": False, "error": f"Document not found: '{doc_id}'"}

    items = list(zip(all_data["ids"], all_data["documents"], all_data["metadatas"]))
    items.sort(key=lambda x: x[2].get("chunk_index", 0))

    if chunk_index is not None:
        idx_min = max(0, chunk_index - window)
        idx_max = min(len(items) - 1, chunk_index + window)
        selected = items[idx_min:idx_max + 1]
    elif line_start is not None and line_end is not None:
        selected = []
        for item in items:
            meta = item[2]
            cl_start = meta.get("line_start", 0)
            cl_end = meta.get("line_end", 0)
            if cl_start < line_end and cl_end > line_start:
                selected.append(item)
        if not selected:
            return {"found": True, "chunks": [],
                    "message": f"No chunks matching line range {line_start}-{line_end}"}
    else:
        return {"found": False, "error": "Provide either chunk_index or line_start+line_end"}

    first_meta = items[0][2]
    chunks = []
    for _, doc, meta in selected:
        chunks.append({
            "index": meta.get("chunk_index", 0),
            "line_start": meta.get("line_start", 0),
            "line_end": meta.get("line_end", 0),
            "scope": meta.get("scope", ""),
            "content": doc,
        })

    return {
        "found": True,
        "source": first_meta.get("source", "?"),
        "filename": first_meta.get("filename", "?"),
        "doc_id": doc_id,
        "total_chunks": len(items),
        "chunks": chunks,
    }


def grep_knowledge(keyword, collection_name="default", max_results=10,
                    case_sensitive=False, filter_filename=None, context_lines=5):
    """在知识库的原始缓存文件中进行关键词/正则搜索。"""
    import re

    raw_dir = os.path.join(_raw_files_dir(), collection_name)
    if not os.path.isdir(raw_dir):
        return []

    doc_id_to_info = _get_doc_id_map(collection_name)

    flags = 0 if case_sensitive else re.IGNORECASE
    try:
        pattern = re.compile(keyword, flags)
    except re.error:
        pattern = re.compile(re.escape(keyword), flags)

    results = []
    for fname in os.listdir(raw_dir):
        doc_id = os.path.splitext(fname)[0]
        info = doc_id_to_info.get(doc_id, {})

        if filter_filename and info.get("filename", "") != filter_filename:
            continue

        fpath = os.path.join(raw_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                file_lines = f.readlines()
        except OSError:
            continue

        for i, line in enumerate(file_lines):
            if pattern.search(line):
                ctx_start = max(0, i - context_lines)
                ctx_end = min(len(file_lines), i + context_lines + 1)
                ctx_parts = []
                for j in range(ctx_start, ctx_end):
                    prefix = ">>>" if j == i else "   "
                    ctx_parts.append(f"{prefix} {j + 1:>5}| {file_lines[j].rstrip()}")

                results.append({
                    "filename": info.get("filename", fname),
                    "source": info.get("source", fpath),
                    "doc_id": doc_id,
                    "line_number": i + 1,
                    "line_content": line.rstrip(),
                    "context": "\n".join(ctx_parts),
                })

                if len(results) >= max_results:
                    return results

    return results


def find_symbol_definition(symbol, collection_name="default", max_results=5):
    """在知识库中查找符号（类/函数/方法）的完整定义。"""
    import re
    import ast as _ast
    import warnings as _warnings

    raw_dir = os.path.join(_raw_files_dir(), collection_name)
    if not os.path.isdir(raw_dir):
        return []

    doc_id_to_info = _get_doc_id_map(collection_name)

    all_files = os.listdir(raw_dir)
    py_files = [f for f in all_files if f.lower().endswith(".py")]
    other_files = [f for f in all_files if not f.lower().endswith(".py")]

    results = []

    def _scan_py(fname):
        doc_id = os.path.splitext(fname)[0]
        info = doc_id_to_info.get(doc_id, {})
        fpath = os.path.join(raw_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            return
        try:
            with _warnings.catch_warnings():
                _warnings.simplefilter("ignore", SyntaxWarning)
                tree = _ast.parse(content)
        except SyntaxError:
            return

        file_lines = content.splitlines()

        def _search_nodes(node, parent_chain=""):
            for child in _ast.iter_child_nodes(node):
                if isinstance(child, (_ast.ClassDef, _ast.FunctionDef, _ast.AsyncFunctionDef)):
                    name = child.name
                    qualified = f"{parent_chain}.{name}" if parent_chain else name
                    if name == symbol or qualified == symbol or qualified.endswith(f".{symbol}"):
                        start = child.lineno
                        end = child.end_lineno if hasattr(child, 'end_lineno') and child.end_lineno else start
                        definition_lines = file_lines[start - 1:end]
                        sym_type = "class" if isinstance(child, _ast.ClassDef) else "function"

                        methods_summary = ""
                        if isinstance(child, _ast.ClassDef):
                            from nbrag.chunker import _extract_signature
                            method_sigs = []
                            for sub in _ast.iter_child_nodes(child):
                                if isinstance(sub, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
                                    method_sigs.append(_extract_signature(sub))
                            if method_sigs:
                                methods_summary = "\n".join(f"  {s}" for s in method_sigs)

                        results.append({
                            "filename": info.get("filename", fname),
                            "source": info.get("source", fpath),
                            "doc_id": doc_id,
                            "symbol_type": sym_type,
                            "qualified_name": qualified,
                            "line_start": start,
                            "line_end": end,
                            "definition": "\n".join(definition_lines),
                            "methods_summary": methods_summary,
                        })
                    _search_nodes(child, qualified)

        _search_nodes(tree)

    for fname in py_files:
        _scan_py(fname)
        if len(results) >= max_results:
            break

    if len(results) < max_results:
        pattern = re.compile(r'\b' + re.escape(symbol) + r'\b')
        for fname in other_files:
            doc_id = os.path.splitext(fname)[0]
            info = doc_id_to_info.get(doc_id, {})
            fpath = os.path.join(raw_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue
            file_lines = content.splitlines()
            for i, line in enumerate(file_lines):
                if pattern.search(line):
                    ctx_start = max(0, i - 3)
                    ctx_end = min(len(file_lines), i + 20)
                    results.append({
                        "filename": info.get("filename", fname),
                        "source": info.get("source", fpath),
                        "doc_id": doc_id,
                        "symbol_type": "unknown",
                        "qualified_name": symbol,
                        "line_start": i + 1,
                        "line_end": ctx_end,
                        "definition": "\n".join(file_lines[ctx_start:ctx_end]),
                        "methods_summary": "",
                    })
                    break
            if len(results) >= max_results:
                break

    return results


def list_documents(collection_name="default"):
    """列出知识库中已导入的文档。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return {}
    total = col.count()
    if total == 0:
        return {}

    all_data = col.get(include=["metadatas"])
    docs = {}
    for meta in all_data["metadatas"]:
        if meta is None:
            continue
        did = meta.get("doc_id", "unknown")
        if did not in docs:
            docs[did] = {
                "filename": meta.get("filename", "?"),
                "source": meta.get("source", "?"),
                "total_chunks": meta.get("total_chunks", 0),
                "chunk_count": 0,
            }
        docs[did]["chunk_count"] += 1
    return docs


def delete_document(doc_id, collection_name="default"):
    """删除指定文档的所有向量数据及缓存文件。返回 (deleted_count, filename)。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return 0, "?"

    try:
        doc_data = col.get(where={"doc_id": doc_id}, include=["metadatas"])
    except Exception:
        doc_data = {"ids": [], "metadatas": []}

    if not doc_data["ids"]:
        return 0, "?"

    filename = doc_data["metadatas"][0].get("filename", "?") if doc_data["metadatas"] else "?"
    col.delete(ids=doc_data["ids"])
    _delete_raw_file(collection_name, doc_id)
    return len(doc_data["ids"]), filename


def get_stats():
    """返回所有知识库的统计信息。"""
    cfg = _cfg()
    collections = list_collections()
    stats = {
        "embedding_model": cfg.embedding.model,
        "rerank_model": cfg.rerank.model or "not configured",
        "data_dir": cfg.storage.db_path,
        "collection_count": len(collections),
        "collections": {},
    }

    chroma = _get_chroma()
    for col_obj in collections:
        name = col_obj.name
        try:
            col = chroma.get_collection(name)
            count = col.count()
            if count > 0:
                all_meta = col.get(include=["metadatas"])
                doc_ids = set(m.get("doc_id", "") for m in all_meta["metadatas"] if m is not None)
                stats["collections"][name] = {
                    "doc_count": len(doc_ids), "chunk_count": count,
                }
            else:
                stats["collections"][name] = {"doc_count": 0, "chunk_count": 0}
        except Exception as e:
            stats["collections"][name] = {"error": str(e)}

    return stats

`````

--- **end of file: nbrag/core.py** (project: nbrag) --- 

---


--- **start of file: nbrag/loggers.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/loggers.py`

#### 📦 Imports

- `import nb_log`


---

`````python
﻿
import nb_log

logger = nb_log.get_logger("nbrag")

`````

--- **end of file: nbrag/loggers.py** (project: nbrag) --- 

---


--- **start of file: nbrag/server.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/server.py`

#### 📝 Module Docstring

`````
nbrag MCP Server — 12 个 Agentic RAG 工具。

Tools (12):
  1. nbrag_add_document         → Import file/directory into collection
  2. nbrag_search               → Semantic search (vector + rerank)
  3. nbrag_search_and_fetch     → Search + auto-fetch raw source (combo tool)
  4. nbrag_grep                 → Keyword/regex exact search (complements semantic search)
  5. nbrag_find_definition      → Find complete class/function definition by symbol name
  6. nbrag_get_file_chunks      → Paginated chunks with scope/line metadata
  7. nbrag_get_raw_file         → Raw file content without overlap
  8. nbrag_get_adjacent_chunks  → Adjacent chunks by chunk index
  9. nbrag_get_chunks_by_lines  → Chunks covering a line range
  10. nbrag_list                → List imported documents
  11. nbrag_delete              → Delete a document
  12. nbrag_stats               → Collection overview and config

启动方式:
  uvx nbrag                          # stdio (默认)
  uvx nbrag --transport streamable-http --port 9101  # HTTP
`````

#### 📦 Imports

- `from pydantic import Field`
- `from mcp.server.fastmcp import FastMCP`
- `from nbrag.config import get_config`
- `from nbrag.chunker import DEFAULT_CHUNK_SIZE`
- `from nbrag.chunker import DEFAULT_CHUNK_OVERLAP`
- `from nbrag.core import ingest_path`
- `from nbrag.core import search`
- `from nbrag.core import list_documents`
- `from nbrag.core import delete_document`
- `from nbrag.core import get_stats`
- `from nbrag.core import get_file_chunks`
- `from nbrag.core import get_context_chunks`
- `from nbrag.core import grep_knowledge`
- `from nbrag.core import find_symbol_definition`
- `import argparse`
- `from nbrag.config import load_config`

#### 🔧 Public Functions (13)

- `def nbrag_add_document(path: str = Field(description='Absolute path to a file or directory. Directory imports all text files recursively'), collection_name: str = Field(description='Collection name (required, auto-created if not exists. Use nbrag_stats to see existing)'), chunk_size: int = Field(default=DEFAULT_CHUNK_SIZE, description='Chunk size in chars, default 1500, recommended 1000-2000'), chunk_overlap: int = Field(default=DEFAULT_CHUNK_OVERLAP, description='Chunk overlap in chars, default 200'), file_extensions: str = Field(default='', description="Comma-separated file extensions to include (e.g. 'py,md,html'). Empty = all text files")) -> str` `mcp.tool()`
  - *Line: 36*
  - **Docstring:**
  `````
  Ingest file or directory into RAG collection (chunking + embedding + indexing). Auto-creates collection if not exists.
  Each chunk is enriched with file path, line numbers, and Python class/function scope.
  Use nbrag_search to retrieve ingested content.
  Note: This tool is typically called manually by users via scripts for one-time batch ingestion,
  not by AI during conversations. AI should focus on nbrag_search/nbrag_grep for retrieval.
  `````

- `def nbrag_search(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections),collection_name对应你的中文就是知识库名字'), top_k: int = Field(default=5, description='Number of results to return'), use_rerank: bool = Field(default=True, description='Enable reranker for better accuracy (recommended)'), filter_filename: str = Field(default='', description="Optional: filter by filename only (e.g. 'constant.py', not full path)")) -> str` `mcp.tool()`
  - *Line: 76*
  - **Docstring:**
  `````
  Semantic search in RAG collection. Vector recall + Rerank. Call nbrag_stats first to see available collections.
  
  Each result contains: file_path (full path), chunk:X/Y, line:N-M, scope, doc_id, dist (cosine distance, lower=more similar).
  
  Recommended deep-analysis workflow (use multiple tools, not just search):
    1. nbrag_search → find relevant files and rough location
    2. nbrag_grep → pinpoint exact class/method/constant names (what semantic search may miss)
    3. nbrag_find_definition → get complete class/function source with inheritance chain
    4. nbrag_get_raw_file → read full source code to verify details
    5. Cross-file tracing: when you see unknown symbols in code, repeat steps 2-4 to trace references
  
  Follow-up tools — use result fields directly as parameters:
    - nbrag_find_definition(symbol, collection_name) → complete class/function definition + methods summary
    - nbrag_get_raw_file(file_path, collection_name) → full source code without overlap
    - nbrag_get_file_chunks(file_path, collection_name) → paginated chunks with scope metadata
    - nbrag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result
    - nbrag_get_chunks_by_lines(doc_id, line_start, line_end, collection_name) → chunks covering line range
  `````

- `def nbrag_search_and_fetch(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)'), top_k: int = Field(default=5, description='Number of search results to return'), fetch_top_n_raw: int = Field(default=3, description='Auto-fetch raw source for top N results (0 to skip fetching)'), context_lines: int = Field(default=100, description='Lines of context around matched chunk. Small files (≤2x this) are fetched fully')) -> str` `mcp.tool()`
  - *Line: 157*
  - **Docstring:**
  `````
  Search + auto-fetch raw source code for top results in one call (combo tool).
  Saves a round-trip vs calling nbrag_search then nbrag_get_raw_file separately.
  Same doc_id appearing in multiple results is fetched only once with merged line range.
  `````

- `def nbrag_grep(keyword: str = Field(description="Keyword or regex pattern (e.g. class name 'UserService', method 'get_by_id', constant 'MAX_RETRIES')"), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)'), max_results: int = Field(default=10, description='Maximum number of matches to return'), case_sensitive: bool = Field(default=False, description='Case-sensitive matching'), filter_filename: str = Field(default='', description="Optional: filter by filename only (e.g. 'booster.py', not full path)"), context_lines: int = Field(default=10, description='Lines of context before and after each match (default 10, use 20+ for seeing full function/class headers)')) -> str` `mcp.tool()`
  - *Line: 270*
  - **Docstring:**
  `````
  Keyword/regex exact search in cached raw files. Complements nbrag_search (semantic search).
  
  Use cases where nbrag_search falls short:
    - Find class/function/variable names: 'UserService', 'get_by_id'
    - Find config keys/constants: 'MAX_RETRIES', 'DEFAULT_TIMEOUT'
    - Find import statements: 'from myproject.core'
    - Find string literals: 'error_handler'
  
  Tip: use context_lines=15 to see class headers + inheritance chain around the match.
  For complete definitions, use nbrag_find_definition instead.
  Typical workflow: nbrag_search (find direction) → nbrag_grep (pinpoint symbols) → nbrag_find_definition (full definition)
  `````

- `def nbrag_find_definition(symbol: str = Field(description="Symbol name to find (class name like 'UserService', function name like 'get_by_id', or qualified name like 'MyClass.__init__')"), collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)'), max_results: int = Field(default=5, description='Maximum number of definitions to return')) -> str` `mcp.tool()`
  - *Line: 309*
  - **Docstring:**
  `````
  Find the complete definition of a class/function/method by symbol name.
  Uses AST parsing to extract exact boundaries — returns the FULL source code of the definition.
  For classes, also returns a methods summary (all method signatures).
  
  Best for cross-file tracing: when you see an unknown symbol in code, use this to get its complete definition.
  Much more efficient than grep + raw_file for understanding class hierarchy and implementation.
  `````

- `def nbrag_get_file_chunks(file_path: str = Field(description="Full absolute path (use 'file_path' value from nbrag_search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)'), start_chunk: int = Field(default=0, description='Start chunk index (0-based), use for pagination'), max_chunks: int = Field(default=10, description='Max chunks to return (use for pagination)')) -> str` `mcp.tool()`
  - *Line: 349*
  - **Docstring:**
  `````
  Paginated view of file chunks with scope and line metadata. Use start_chunk to paginate.
  Note: adjacent chunks have overlap. For clean source code without overlap, use nbrag_get_raw_file instead.
  `````

- `def nbrag_get_raw_file(file_path: str = Field(description="Full absolute path (use 'file_path' value from nbrag_search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)'), line_start: int = Field(default=-1, description='Start line (1-based), -1 for beginning'), line_end: int = Field(default=-1, description='End line (inclusive), -1 for end of file')) -> str` `mcp.tool()`
  - *Line: 369*
  - **Docstring:**
  `````
  Get cached raw file content without chunk overlap. Recommended for viewing full source code.
  Supports line_start/line_end for extracting specific line ranges.
  Only available for files imported with raw cache (re-import older files if needed).
  `````

- `def nbrag_get_adjacent_chunks(doc_id: str = Field(description="Document ID (use 'doc_id' value from nbrag_search/nbrag_grep results)"), chunk_index: int = Field(description="Target chunk index (0-based, the X from 'chunk:X/Y' in nbrag_search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)'), window: int = Field(default=3, description='Context window: returns chunk_index ± window chunks')) -> str` `mcp.tool()`
  - *Line: 437*
  - **Docstring:**
  `````
  Get adjacent chunks around a specific chunk index, for expanding context of a search result.
  Requires doc_id and chunk_index from nbrag_search results (not file_path).
  Example: doc_id="abc123", chunk_index=3, window=2 → returns chunks 1-5
  `````

- `def nbrag_get_chunks_by_lines(doc_id: str = Field(description="Document ID (use 'doc_id' value from nbrag_search/nbrag_grep results)"), line_start: int = Field(description="Start line number (1-based, from 'line:N-M' in search results)"), line_end: int = Field(description="End line number (inclusive, from 'line:N-M' in search results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)')) -> str` `mcp.tool()`
  - *Line: 454*
  - **Docstring:**
  `````
  Get all chunks covering a line range, with scope metadata.
  vs nbrag_get_raw_file: this returns chunks (with scope but has overlap),
  nbrag_get_raw_file returns raw code (no overlap but no scope).
  Example: doc_id="abc123", line_start=80, line_end=200
  `````

- `def nbrag_list(collection_name: str = Field(description='Collection name (required, use nbrag_stats to see available collections)')) -> str` `mcp.tool()`
  - *Line: 497*
  - **Docstring:**
  `````
  List all documents in a collection (filename, path, chunk count, doc_id).
  Use returned doc_id with nbrag_delete to remove documents.
  `````

- `def nbrag_delete(doc_id: str = Field(description="Document ID to delete (use 'doc_id' value from nbrag_list results)"), collection_name: str = Field(description='Collection name (use nbrag_stats to see available collections)')) -> str` `mcp.tool()`
  - *Line: 516*
  - *Delete a document's vectors and cached files from the collection. Get doc_id from nbrag_list.*

- `def nbrag_stats() -> str` `mcp.tool()`
  - *Line: 530*
  - **Docstring:**
  `````
  nbrag_stats 获取所有知识库的统计信息，英文术语`collection` 就是中文的`知识库`
  Get RAG overview: all collection names, doc/chunk counts, and config.
  Call this FIRST to discover available collection_name values for other tools.
  Glossary: collection = knowledge base, doc = imported file, chunk = vector-embedded text segment.
  `````

- `def main()`
  - *Line: 562*
  - *CLI entry point for uvx / python -m nbrag.*


---

`````python
﻿"""
nbrag MCP Server — 12 个 Agentic RAG 工具。

Tools (12):
  1. nbrag_add_document         → Import file/directory into collection
  2. nbrag_search               → Semantic search (vector + rerank)
  3. nbrag_search_and_fetch     → Search + auto-fetch raw source (combo tool)
  4. nbrag_grep                 → Keyword/regex exact search (complements semantic search)
  5. nbrag_find_definition      → Find complete class/function definition by symbol name
  6. nbrag_get_file_chunks      → Paginated chunks with scope/line metadata
  7. nbrag_get_raw_file         → Raw file content without overlap
  8. nbrag_get_adjacent_chunks  → Adjacent chunks by chunk index
  9. nbrag_get_chunks_by_lines  → Chunks covering a line range
  10. nbrag_list                → List imported documents
  11. nbrag_delete              → Delete a document
  12. nbrag_stats               → Collection overview and config

启动方式:
  uvx nbrag                          # stdio (默认)
  uvx nbrag --transport streamable-http --port 9101  # HTTP
"""

from pydantic import Field
from mcp.server.fastmcp import FastMCP
from nbrag.config import get_config
from nbrag.chunker import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP
from nbrag.core import (
    ingest_path, search, list_documents, delete_document, get_stats,
    get_file_chunks, get_context_chunks, grep_knowledge, find_symbol_definition,
)

mcp = FastMCP("nbrag")


@mcp.tool()
def nbrag_add_document(
    path: str = Field(description="Absolute path to a file or directory. Directory imports all text files recursively"),
    collection_name: str = Field(description="Collection name (required, auto-created if not exists. Use nbrag_stats to see existing)"),
    chunk_size: int = Field(default=DEFAULT_CHUNK_SIZE, description="Chunk size in chars, default 1500, recommended 1000-2000"),
    chunk_overlap: int = Field(default=DEFAULT_CHUNK_OVERLAP, description="Chunk overlap in chars, default 200"),
    file_extensions: str = Field(default="", description="Comma-separated file extensions to include (e.g. 'py,md,html'). Empty = all text files"),
) -> str:
    """Ingest file or directory into RAG collection (chunking + embedding + indexing). Auto-creates collection if not exists.
    Each chunk is enriched with file path, line numbers, and Python class/function scope.
    Use nbrag_search to retrieve ingested content.
    Note: This tool is typically called manually by users via scripts for one-time batch ingestion,
    not by AI during conversations. AI should focus on nbrag_search/nbrag_grep for retrieval."""
    cfg = get_config()
    ext_list = [e.strip() for e in file_extensions.split(",") if e.strip()] if file_extensions else None
    results, errors, skipped_count = ingest_path(path, collection_name, chunk_size, chunk_overlap, file_extensions=ext_list)

    total_chunks = sum(r["chunks"] for r in results)
    total_chars = sum(r["chars"] for r in results)

    skip_str = f", {skipped_count} skipped" if skipped_count else ""
    lines = [f"Import done: {len(results)} ok, {len(errors)} failed{skip_str}"]
    lines.append(f"collection: {collection_name} | chars: {total_chars} | chunks: {total_chunks}")
    lines.append(f"chunk_size={chunk_size} overlap={chunk_overlap} | embed: {cfg.embedding.model}")

    if len(results) <= 10:
        lines.append("")
        for r in results:
            lines.append(f"  {r['filename']} ({r['chunks']} chunks, {r['chars']} chars, doc_id:{r['doc_id']})")
    else:
        lines.append(f"\n{len(results)} files imported (too many to list)")

    if errors:
        lines.append(f"\nFailed ({len(errors)}):")
        for e in errors[:10]:
            lines.append(f"  {e}")

    return "\n".join(lines)


@mcp.tool()
def nbrag_search(
    query: str = Field(description="Search query (natural language question or keywords)"),
    collection_name: str = Field(description="Collection name (required, use nbrag_stats to see available collections),collection_name对应你的中文就是知识库名字"),
    top_k: int = Field(default=5, description="Number of results to return"),
    use_rerank: bool = Field(default=True, description="Enable reranker for better accuracy (recommended)"),
    filter_filename: str = Field(default="", description="Optional: filter by filename only (e.g. 'constant.py', not full path)"),
) -> str:
    """Semantic search in RAG collection. Vector recall + Rerank. Call nbrag_stats first to see available collections.

    Each result contains: file_path (full path), chunk:X/Y, line:N-M, scope, doc_id, dist (cosine distance, lower=more similar).

    Recommended deep-analysis workflow (use multiple tools, not just search):
      1. nbrag_search → find relevant files and rough location
      2. nbrag_grep → pinpoint exact class/method/constant names (what semantic search may miss)
      3. nbrag_find_definition → get complete class/function source with inheritance chain
      4. nbrag_get_raw_file → read full source code to verify details
      5. Cross-file tracing: when you see unknown symbols in code, repeat steps 2-4 to trace references

    Follow-up tools — use result fields directly as parameters:
      - nbrag_find_definition(symbol, collection_name) → complete class/function definition + methods summary
      - nbrag_get_raw_file(file_path, collection_name) → full source code without overlap
      - nbrag_get_file_chunks(file_path, collection_name) → paginated chunks with scope metadata
      - nbrag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result
      - nbrag_get_chunks_by_lines(doc_id, line_start, line_end, collection_name) → chunks covering line range"""
    cfg = get_config()
    fname_filter = filter_filename if filter_filename else None
    documents, metadatas, distances, rerank_used, total = search(
        query, collection_name, top_k, use_rerank,
        filter_filename=fname_filter,
    )

    if total == 0:
        stats = get_stats()
        avail = list(stats["collections"].keys())
        exists = collection_name in avail
        if not exists:
            return (f"collection '{collection_name}' does not exist.\n"
                    f"Available collections: {avail}\n"
                    f"Use nbrag_add_document to create and import docs.")
        return (f"collection '{collection_name}' is empty. "
                f"Use nbrag_add_document to import docs first.")

    if not documents:
        return f"No results (collection has {total} chunks, filter: {filter_filename or 'none'})"

    rerank_str = cfg.rerank.model if rerank_used else "off"
    header = f"[{collection_name}] {total} chunks | rerank: {rerank_str}"
    if filter_filename:
        header += f" | filter: {filter_filename}"
    lines = [header, ""]

    preview_limit = min(8000, 40000 // max(len(documents), 1))
    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances)):
        if meta is None:
            meta = {}
        src = meta.get("source", meta.get("filename", "?"))
        ci = meta.get("chunk_index", "?")
        tc = meta.get("total_chunks", "?")
        ls = meta.get("line_start", 0)
        le = meta.get("line_end", 0)
        scope = meta.get("scope", "")
        doc_id = meta.get("doc_id", "?")

        meta_parts = [f"chunk:{ci}/{tc}"]
        if ls and le:
            meta_parts.append(f"line:{ls}-{le}")
        if scope:
            meta_parts.append(f"scope:{scope}")
        meta_parts.append(f"doc_id:{doc_id}")
        meta_parts.append(f"dist:{dist:.4f}")

        lines.append(f"[{i + 1}/{len(documents)}] {meta.get('filename', '?')} {' '.join(meta_parts)}")
        lines.append(f"file_path: {src}")
        preview = doc[:preview_limit] + ("..." if len(doc) > preview_limit else "")
        lines.append(preview)
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_search_and_fetch(
    query: str = Field(description="Search query (natural language question or keywords)"),
    collection_name: str = Field(description="Collection name (required, use nbrag_stats to see available collections)"),
    top_k: int = Field(default=5, description="Number of search results to return"),
    fetch_top_n_raw: int = Field(default=3, description="Auto-fetch raw source for top N results (0 to skip fetching)"),
    context_lines: int = Field(default=100, description="Lines of context around matched chunk. Small files (≤2x this) are fetched fully"),
) -> str:
    """Search + auto-fetch raw source code for top results in one call (combo tool).
    Saves a round-trip vs calling nbrag_search then nbrag_get_raw_file separately.
    Same doc_id appearing in multiple results is fetched only once with merged line range."""
    cfg = get_config()
    fname_filter = None
    documents, metadatas, distances, rerank_used, total = search(
        query, collection_name, top_k, True, filter_filename=fname_filter,
    )

    if total == 0:
        stats = get_stats()
        avail = list(stats["collections"].keys())
        exists = collection_name in avail
        if not exists:
            return (f"collection '{collection_name}' does not exist.\n"
                    f"Available collections: {avail}\n"
                    f"Use nbrag_add_document to create and import docs.")
        return (f"collection '{collection_name}' is empty. "
                f"Use nbrag_add_document to import docs first.")

    if not documents:
        return f"No results (collection has {total} chunks)"

    rerank_str = cfg.rerank.model if rerank_used else "off"
    lines = [f"[{collection_name}] {total} chunks | rerank: {rerank_str}", ""]

    preview_limit = min(8000, 40000 // max(len(documents), 1))
    fetch_targets = {}
    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances)):
        if meta is None:
            meta = {}
        src = meta.get("source", meta.get("filename", "?"))
        ci = meta.get("chunk_index", "?")
        tc = meta.get("total_chunks", "?")
        _ls = meta.get("line_start", 0)
        _le = meta.get("line_end", 0)
        ls = int(_ls) if isinstance(_ls, (int, float)) else 0
        le = int(_le) if isinstance(_le, (int, float)) else 0
        scope = str(meta.get("scope", ""))
        doc_id = str(meta.get("doc_id", "?"))

        meta_parts = [f"chunk:{ci}/{tc}"]
        if ls and le:
            meta_parts.append(f"line:{ls}-{le}")
        if scope:
            meta_parts.append(f"scope:{scope}")
        meta_parts.append(f"doc_id:{doc_id}")
        meta_parts.append(f"dist:{dist:.4f}")

        lines.append(f"[{i + 1}/{len(documents)}] {meta.get('filename', '?')} {' '.join(meta_parts)}")
        lines.append(f"file_path: {src}")
        preview = doc[:preview_limit] + ("..." if len(doc) > preview_limit else "")
        lines.append(preview)
        lines.append("")

        if i < fetch_top_n_raw and doc_id != "?" and src != "?":
            if doc_id not in fetch_targets:
                fetch_targets[doc_id] = {"src": str(src), "line_min": ls, "line_max": le}
            else:
                t = fetch_targets[doc_id]
                if ls:
                    t["line_min"] = min(t["line_min"], ls) if t["line_min"] else ls
                if le:
                    t["line_max"] = max(t["line_max"], le) if t["line_max"] else le

    if fetch_targets:
        lines.append("=" * 40)
        lines.append(f"Auto-fetched raw source ({len(fetch_targets)} file(s)):")
        lines.append("")

    for doc_id, target in fetch_targets.items():
        center_start = target["line_min"] or 1
        center_end = target["line_max"] or center_start
        center = (center_start + center_end) // 2
        half = context_lines

        raw_result = get_file_chunks(
            target["src"], collection_name, 0, 0,
            raw=True, line_start=-1, line_end=-1,
        )

        if not raw_result.get("found"):
            lines.append(f"[{target['src']}] raw cache not available")
            lines.append("")
            continue

        tl = raw_result["total_lines"]
        if tl <= context_lines * 2:
            lines.append(_format_raw_result(raw_result))
        else:
            fetch_start = max(1, center - half)
            fetch_end = min(tl, center + half)
            excerpt = get_file_chunks(
                target["src"], collection_name, 0, 0,
                raw=True, line_start=fetch_start, line_end=fetch_end,
            )
            if excerpt.get("found"):
                lines.append(_format_raw_result(excerpt))
            else:
                lines.append(f"[{target['src']}] excerpt failed")
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_grep(
    keyword: str = Field(description="Keyword or regex pattern (e.g. class name 'UserService', method 'get_by_id', constant 'MAX_RETRIES')"),
    collection_name: str = Field(description="Collection name (required, use nbrag_stats to see available collections)"),
    max_results: int = Field(default=10, description="Maximum number of matches to return"),
    case_sensitive: bool = Field(default=False, description="Case-sensitive matching"),
    filter_filename: str = Field(default="", description="Optional: filter by filename only (e.g. 'booster.py', not full path)"),
    context_lines: int = Field(default=10, description="Lines of context before and after each match (default 10, use 20+ for seeing full function/class headers)"),
) -> str:
    """Keyword/regex exact search in cached raw files. Complements nbrag_search (semantic search).

    Use cases where nbrag_search falls short:
      - Find class/function/variable names: 'UserService', 'get_by_id'
      - Find config keys/constants: 'MAX_RETRIES', 'DEFAULT_TIMEOUT'
      - Find import statements: 'from myproject.core'
      - Find string literals: 'error_handler'

    Tip: use context_lines=15 to see class headers + inheritance chain around the match.
    For complete definitions, use nbrag_find_definition instead.
    Typical workflow: nbrag_search (find direction) → nbrag_grep (pinpoint symbols) → nbrag_find_definition (full definition)"""
    fname_filter = filter_filename if filter_filename else None
    results = grep_knowledge(
        keyword, collection_name, max_results, case_sensitive,
        filter_filename=fname_filter, context_lines=context_lines,
    )

    if not results:
        return f"No matches for '{keyword}' (collection: {collection_name})"

    lines = [f"grep: '{keyword}' | collection_name: {collection_name} | {len(results)} match(es)", ""]
    for i, r in enumerate(results):
        lines.append(f"[{i + 1}/{len(results)}] {r['filename']} line:{r['line_number']} doc_id:{r['doc_id']}")
        lines.append(f"file_path: {r['source']}")
        lines.append(r["context"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_find_definition(
    symbol: str = Field(description="Symbol name to find (class name like 'UserService', function name like 'get_by_id', or qualified name like 'MyClass.__init__')"),
    collection_name: str = Field(description="Collection name (required, use nbrag_stats to see available collections)"),
    max_results: int = Field(default=5, description="Maximum number of definitions to return"),
) -> str:
    """Find the complete definition of a class/function/method by symbol name.
    Uses AST parsing to extract exact boundaries — returns the FULL source code of the definition.
    For classes, also returns a methods summary (all method signatures).

    Best for cross-file tracing: when you see an unknown symbol in code, use this to get its complete definition.
    Much more efficient than grep + raw_file for understanding class hierarchy and implementation."""
    results = find_symbol_definition(symbol, collection_name, max_results)

    if not results:
        return f"No definition found for '{symbol}' (collection: {collection_name}). Try nbrag_grep for a broader search."

    lines = [f"definition: '{symbol}' | collection_name: {collection_name} | {len(results)} found", ""]
    for i, r in enumerate(results):
        header_parts = [
            f"[{i + 1}/{len(results)}]",
            f"{r['symbol_type']}",
            f"{r['qualified_name']}",
            f"line:{r['line_start']}-{r['line_end']}",
            f"doc_id:{r['doc_id']}",
        ]
        lines.append(" ".join(header_parts))
        lines.append(f"file_path: {r['source']}")

        if r.get("methods_summary"):
            lines.append("methods:")
            lines.append(r["methods_summary"])

        lines.append("---")
        lines.append(r["definition"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_get_file_chunks(
    file_path: str = Field(description="Full absolute path (use 'file_path' value from nbrag_search results)"),
    collection_name: str = Field(description="Collection name (use nbrag_stats to see available collections)"),
    start_chunk: int = Field(default=0, description="Start chunk index (0-based), use for pagination"),
    max_chunks: int = Field(default=10, description="Max chunks to return (use for pagination)"),
) -> str:
    """Paginated view of file chunks with scope and line metadata. Use start_chunk to paginate.
    Note: adjacent chunks have overlap. For clean source code without overlap, use nbrag_get_raw_file instead."""
    result = get_file_chunks(
        file_path, collection_name, start_chunk, max_chunks,
        raw=False,
    )

    if not result.get("found"):
        return result.get("error", f"File not found: '{file_path}'")

    return _format_chunks_result(result)


@mcp.tool()
def nbrag_get_raw_file(
    file_path: str = Field(description="Full absolute path (use 'file_path' value from nbrag_search results)"),
    collection_name: str = Field(description="Collection name (use nbrag_stats to see available collections)"),
    line_start: int = Field(default=-1, description="Start line (1-based), -1 for beginning"),
    line_end: int = Field(default=-1, description="End line (inclusive), -1 for end of file"),
) -> str:
    """Get cached raw file content without chunk overlap. Recommended for viewing full source code.
    Supports line_start/line_end for extracting specific line ranges.
    Only available for files imported with raw cache (re-import older files if needed)."""
    result = get_file_chunks(
        file_path, collection_name, 0, 0,
        raw=True, line_start=line_start, line_end=line_end,
    )

    if not result.get("found"):
        return result.get("error", f"File not found: '{file_path}'")

    return _format_raw_result(result)


def _format_raw_result(result):
    """Format raw file result in compact English."""
    ls = result["line_start"]
    le = result["line_end"]
    tl = result["total_lines"]
    shown = le - ls + 1
    range_info = f"line:{ls}-{le}" + (f" ({shown}/{tl} lines)" if shown < tl else " (full)")
    lines = [
        f"raw_file: {result['filename']} | doc_id:{result['doc_id']} | {tl} lines | {result['total_chunks']} chunks",
        f"file_path: {result['source']}",
        f"range: {range_info}",
        "",
        result["content"],
    ]
    if le < tl:
        lines.append(f"\n({tl - le} lines remaining, use line_start={le + 1} to continue)")
    return "\n".join(lines)


def _format_chunks_result(result):
    """Format chunks result in compact English."""
    tc = result["total_chunks"]
    lines = [
        f"file: {result['filename']} | doc_id:{result['doc_id']} | {tc} chunks | ~{result['total_lines']} lines",
        f"file_path: {result['source']}",
        "chunk_ranges: " + " ".join(f"[{s}-{e}]" for s, e in result["chunk_line_ranges"]),
        "",
    ]

    for chunk in result["chunks"]:
        idx = chunk["index"]
        scope = chunk["scope"]
        scope_str = f" scope:{scope}" if scope else ""
        lines.append(f"-- chunk {idx}/{tc} line:{chunk['line_start']}-{chunk['line_end']}{scope_str} --")
        lines.append(chunk["content"])
        lines.append("")

    sc = result["start_chunk"]
    ec = result["end_chunk"]
    if ec < tc:
        lines.append(f"(showing chunk {sc}-{ec - 1}, {ec - sc}/{tc} total. Use start_chunk={ec} for more)")
    else:
        lines.append(f"(all {tc} chunks shown)")

    return "\n".join(lines)


@mcp.tool()
def nbrag_get_adjacent_chunks(
    doc_id: str = Field(description="Document ID (use 'doc_id' value from nbrag_search/nbrag_grep results)"),
    chunk_index: int = Field(description="Target chunk index (0-based, the X from 'chunk:X/Y' in nbrag_search results)"),
    collection_name: str = Field(description="Collection name (use nbrag_stats to see available collections)"),
    window: int = Field(default=3, description="Context window: returns chunk_index ± window chunks"),
) -> str:
    """Get adjacent chunks around a specific chunk index, for expanding context of a search result.
    Requires doc_id and chunk_index from nbrag_search results (not file_path).
    Example: doc_id="abc123", chunk_index=3, window=2 → returns chunks 1-5"""
    result = get_context_chunks(
        doc_id, collection_name,
        chunk_index=chunk_index, window=window,
    )
    return _format_context_result(result, doc_id)


@mcp.tool()
def nbrag_get_chunks_by_lines(
    doc_id: str = Field(description="Document ID (use 'doc_id' value from nbrag_search/nbrag_grep results)"),
    line_start: int = Field(description="Start line number (1-based, from 'line:N-M' in search results)"),
    line_end: int = Field(description="End line number (inclusive, from 'line:N-M' in search results)"),
    collection_name: str = Field(description="Collection name (use nbrag_stats to see available collections)"),
) -> str:
    """Get all chunks covering a line range, with scope metadata.
    vs nbrag_get_raw_file: this returns chunks (with scope but has overlap),
    nbrag_get_raw_file returns raw code (no overlap but no scope).
    Example: doc_id="abc123", line_start=80, line_end=200"""
    result = get_context_chunks(
        doc_id, collection_name,
        line_start=line_start, line_end=line_end,
    )
    return _format_context_result(result, doc_id)


def _format_context_result(result, doc_id):
    """Format context/adjacent chunks result in compact English."""
    if not result.get("found"):
        return result.get("error", f"doc_id '{doc_id}' not found")

    if not result.get("chunks"):
        return result.get("message", "No matching chunks")

    tc = result["total_chunks"]
    lines = [
        f"file: {result.get('filename', '?')} | doc_id:{doc_id} | {tc} chunks",
        f"file_path: {result['source']}",
        "",
    ]

    for chunk in result["chunks"]:
        scope = chunk["scope"]
        scope_str = f" scope:{scope}" if scope else ""
        lines.append(f"-- chunk {chunk['index']}/{tc} line:{chunk['line_start']}-{chunk['line_end']}{scope_str} --")
        lines.append(chunk["content"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_list(
    collection_name: str = Field(description="Collection name (required, use nbrag_stats to see available collections)"),
) -> str:
    """List all documents in a collection (filename, path, chunk count, doc_id).
    Use returned doc_id with nbrag_delete to remove documents."""
    docs = list_documents(collection_name)

    if not docs:
        return f"collection '{collection_name}' is empty."

    total_chunks = sum(info["chunk_count"] for info in docs.values())
    lines = [f"[{collection_name}] {len(docs)} docs, {total_chunks} chunks\n"]
    for did, info in docs.items():
        lines.append(f"  {info['filename']} | file_path: {info['source']} | {info['chunk_count']} chunks | doc_id:{did}")

    return "\n".join(lines)


@mcp.tool()
def nbrag_delete(
    doc_id: str = Field(description="Document ID to delete (use 'doc_id' value from nbrag_list results)"),
    collection_name: str = Field(description="Collection name (use nbrag_stats to see available collections)"),
) -> str:
    """Delete a document's vectors and cached files from the collection. Get doc_id from nbrag_list."""
    deleted, filename = delete_document(doc_id, collection_name)

    if deleted == 0:
        return f"Error: doc_id '{doc_id}' not found. Use nbrag_list to see available doc_ids."

    return f"Deleted: {filename} | {deleted} chunks | doc_id:{doc_id}"


@mcp.tool()
def nbrag_stats() -> str:
    """
    nbrag_stats 获取所有知识库的统计信息，英文术语`collection` 就是中文的`知识库`
    Get RAG overview: all collection names, doc/chunk counts, and config.
    Call this FIRST to discover available collection_name values for other tools.
    Glossary: collection = knowledge base, doc = imported file, chunk = vector-embedded text segment."""
    cfg = get_config()
    stats = get_stats()

    lines = [
        "RAG Stats",
        f"embed: {stats['embedding_model']} | rerank: {stats['rerank_model']}",
        f"data_dir: {stats['data_dir']}",
        f"chunk: size={cfg.chunking.chunk_size} overlap={cfg.chunking.chunk_overlap} | collections: {stats['collection_count']}",
        "",
    ]

    if not stats["collections"]:
        lines.append("(no collections yet, use nbrag_add_document to import)")
        return "\n".join(lines)

    for name, info in stats["collections"].items():
        if "error" in info:
            lines.append(f"  [{name}] error: {info['error']}")
        elif info["chunk_count"] > 0:
            lines.append(f"  [{name}] {info['doc_count']} docs, {info['chunk_count']} chunks")
        else:
            lines.append(f"  [{name}] empty")

    return "\n".join(lines)


def main():
    """CLI entry point for uvx / python -m nbrag."""
    import argparse
    parser = argparse.ArgumentParser(
        description="nbrag — Agentic RAG MCP Server with 12 tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  nbrag                               # stdio transport (default)
  nbrag --transport streamable-http    # HTTP transport on port 9101
  nbrag --api-key sk-xxx              # specify API key directly
  NBRAG_API_KEY=sk-xxx nbrag         # API key via env var""",
    )
    parser.add_argument("--transport", choices=["stdio", "streamable-http", "sse"], default="stdio",
                        help="MCP transport mode (default: stdio)")
    parser.add_argument("--port", type=int, default=9101,
                        help="HTTP port (only for streamable-http/sse, default: 9101)")
    parser.add_argument("--api-key", dest="api_key",
                        help="Embedding/Rerank API key (or set NBRAG_API_KEY env var)")
    parser.add_argument("--db-path", dest="db_path",
                        help="ChromaDB storage path (default: ./rag_db)")
    parser.add_argument("--config",
                        help="Path to YAML config file")
    args = parser.parse_args()

    from nbrag.config import load_config
    load_config(args)

    if args.transport != "stdio":
        mcp.settings.port = args.port

    mcp.run(transport=args.transport)


if __name__ == "__main__":
    main()

`````

--- **end of file: nbrag/server.py** (project: nbrag) --- 

---


--- **start of file: nbrag/__init__.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/__init__.py`

#### 📝 Module Docstring

`````
nbrag — Agentic RAG MCP Server

AI-driven multi-round code retrieval with 12 complementary tools.
`````


---

`````python
﻿"""
nbrag — Agentic RAG MCP Server

AI-driven multi-round code retrieval with 12 complementary tools.
"""

__version__ = "0.1.0"

`````

--- **end of file: nbrag/__init__.py** (project: nbrag) --- 

---


--- **start of file: nbrag/__main__.py** (project: nbrag) --- 


### 📄 Python File Metadata: `nbrag/__main__.py`

#### 📝 Module Docstring

`````
python -m nbrag 入口。
`````

#### 📦 Imports

- `from nbrag.server import main`


---

`````python
﻿"""python -m nbrag 入口。"""

from nbrag.server import main

main()

`````

--- **end of file: nbrag/__main__.py** (project: nbrag) --- 

---

# markdown content namespace: nbrag skills 


## nbrag File Tree (relative dir: `nbrag/skills`)


`````

└── nbrag
    └── skills
        ├── nbrag-workflow
        │   └── SKILL.md
        └── readme.md

`````

---


## nbrag (relative dir: `nbrag/skills`)  Included Files (total: 2 files)


- `nbrag/skills/readme.md`

- `nbrag/skills/nbrag-workflow/SKILL.md`


---


--- **start of file: nbrag/skills/readme.md** (project: nbrag) --- 

`````markdown
你把这个文件夹，复制到你自己项目下的被第三方工具认可扫描的skills文件夹下
`````

--- **end of file: nbrag/skills/readme.md** (project: nbrag) --- 

---


--- **start of file: nbrag/skills/nbrag-workflow/SKILL.md** (project: nbrag) --- 

`````markdown
﻿---
name: nbrag-workflow
version: "1.0.0"
description: >-
  Multi-round intelligent retrieval using nbrag knowledge base.
  Activates when searching code implementations, finding function/class definitions,
  understanding project structure, browsing documentation, or when terms like
  "knowledge base", "code search", "find definition" appear in the user request.
---

# RAG 知识库检索工作流

nbrag 提供 12 个 MCP 工具，核心分三类：**发现 → 检索 → 深入**。

> **注意**：本文档中的函数名（如 `nbrag_search`）是 nbrag MCP 自身的函数名。
> 当 nbrag 被接入其他 Agent 框架时，函数名会带前缀（如变成 mcp__xxx__nbrag_search），
> AI 应以实际接收到的 function 名称为准，不要死记本文档中的具体函数名。


## 前提

- 以下 4 个工具依赖导入时的 raw cache：`nbrag_grep`、`nbrag_find_definition`、`nbrag_get_raw_file`、`nbrag_search_and_fetch`。
  - `nbrag_get_raw_file` 缺 cache 时报：`Raw file cache not found (doc_id=...). This file may have been imported before caching was enabled. Please re-import.`
  - `nbrag_search_and_fetch` 缺 cache 时报：`[{file_path}] raw cache not available`
  - `nbrag_grep` / `nbrag_find_definition` 缺 cache 时**静默返回空结果**（不报错），表现与"真的没有匹配"相同——如果怀疑是 cache 缺失，先用 `nbrag_stats` 确认 collection 存在且有 chunks。
- chunk 正文开头含注入 header（非原始源码），格式因上下文而异：
  - 模块级函数：`# [File: path] [Scope: func_name] [Sig: def func(...)] [Lines: N-M]`
  - 类体级：`# [File: path] [Scope: ClassName] [Sig: class ClassName(Base)] [Lines: N-M]`
  - 类方法：`# [File: path] [Class: class ClassName(Base)] [Method: method_name] [Sig: def method(...)] [Lines: N-M]`
  - 若无 `parent_class_sig` 回退为 `[Class: ClassName]`（无基类签名）
  - `[Sig]`、`[Lines]`、`[Class]` 部分字段可能缺失。

## 第一步：发现

```
nbrag_stats()
```

返回：所有 collection(知识库) 名称、文档/chunk 数、embedding/rerank 模型、data_dir、chunk_size/chunk_overlap。
首次使用或不确定 collection 名称时先调用。已知名称可直接检索。
注意：仅 `nbrag_search` / `nbrag_search_and_fetch` 在 collection 不存在时会提示 `Available collections: [...]`，
`nbrag_grep` / `nbrag_find_definition` 不会提示（静默返回空）。

## 第二步：检索

### 策略 A：语义搜索（推荐首选）

```
nbrag_search(query="用户的问题", collection_name="xxx", top_k=5)
```

- 向量召回 + rerank 精排（rerank 需配置且召回数 > top_k 才生效，失败静默降级）
- 可选 `use_rerank=False` 禁用 rerank
- 适合自然语言提问："这个项目怎么处理并发？"
- 可选 `filter_filename="core.py"` 缩小搜索范围（仅匹配文件名，非完整路径）
- 返回每条结果包含两行：
  - 标题行：`[1/5] filename chunk:X/Y line:N-M scope:xxx doc_id:xxx dist:0.1234`
  - 路径行：`file_path: /absolute/path/to/file`
- 关键字段：`chunk:X/Y`（chunk 索引/总数）、`line:N-M`、`scope`（仅 Python）、`doc_id`、`dist`（cosine 距离，越小越相似）
- chunk preview 可能被截断（加 `...`）

### 策略 B：精确搜索（补充语义搜索）

```
nbrag_grep(keyword="UserService", collection_name="xxx")
```

- 关键词/正则匹配，搜索 raw cache 文件（非向量库）
- 适合搜索确切的类名、函数名、变量名、错误信息
- 可选：`max_results=10`（默认）、`case_sensitive=True`（默认 False）、`filter_filename="core.py"`、`context_lines=10`（默认 10，匹配行前后各 N 行，即总共约 2N+1 行）
- 返回匹配行及上下文，`>>>` 标记匹配行

### 策略 C：符号查找

```
nbrag_find_definition(symbol="get_by_id", collection_name="xxx")
```

- **Python 文件**：AST 精确解析，返回 class/function 完整定义 + class 方法签名列表。AST 解析失败（语法错误）的文件会被静默跳过。
- **非 Python 文件**：正则匹配，`symbol_type` 为 `unknown`，每个文件最多返回 1 处匹配，仅约 24 行上下文（匹配行前 3 行 + 匹配行 + 后 20 行），非完整定义。
- 可选 `max_results=5`（默认）
- 支持 qualified name：`symbol="MyClass.__init__"`

### 策略 D：一站式检索（省一轮调用）

```
nbrag_search_and_fetch(query="...", collection_name="xxx", top_k=5)
```

- 语义搜索 + 自动抓取 top N 结果的 raw 源码（省去单独调用 `nbrag_get_raw_file`）
- 小文件（≤ 2×context_lines 行）抓全文；大文件只抓匹配位置 ±context_lines 行 excerpt
- 可选：`fetch_top_n_raw=3`（默认 3，设 0 跳过抓取）、`context_lines=100`（默认）
- 同一 `doc_id` 多次命中会合并行范围只抓取一次
- **限制**：不支持 `filter_filename`，始终启用 rerank
- 需要完整源码请再用 `nbrag_get_raw_file`

## 第三步：深入

检索结果通常是代码片段（chunk），需要更多上下文时选择：

| 工具 | 特点 | 适用场景 |
|------|------|---------|
| `nbrag_get_raw_file` | 无 overlap 的干净源码，无 scope | 看完整文件或指定行号范围 |
| `nbrag_get_file_chunks` | 有 scope 元数据，chunk 间有 200 字符 overlap | 分页浏览 + 了解作用域 |
| `nbrag_get_adjacent_chunks` | 有 scope，有 overlap | 扩展搜索结果的上下文 |
| `nbrag_get_chunks_by_lines` | 有 scope，有 overlap | 按行号精确取 chunk |

### 看原始文件

```
nbrag_get_raw_file(file_path="从搜索结果获取", collection_name="xxx")
```

- 支持 `line_start` / `line_end` 指定范围（1-based），默认 -1 表示读全文
- 大文件返回后会提示 `(N lines remaining, use line_start=... to continue)`
- `file_path` 也可只传文件名（如 `"core.py"`）

### 看相邻代码块

```
nbrag_get_adjacent_chunks(doc_id="从搜索结果获取", chunk_index=3, collection_name="xxx", window=3)
```

- `chunk_index` 从搜索结果的 `chunk:X/Y` 中取 X
- `window` 默认 3，返回 chunk_index ± 3（最多 7 个 chunk）

### 按行号获取

```
nbrag_get_chunks_by_lines(doc_id="...", line_start=50, line_end=100, collection_name="xxx")
```

### 分页浏览文件

```
nbrag_get_file_chunks(file_path="...", collection_name="xxx", start_chunk=0, max_chunks=10)
```

- 与 `nbrag_get_raw_file` 的区别：有 scope 元数据 + chunk 间有 overlap，适合需要作用域信息的场景

## 推荐调用顺序

```
nbrag_stats()                          # 1. 发现知识库
    ↓
nbrag_search() / nbrag_grep()            # 2. 检索（可多次、换策略）
    ↓                                # 快捷路径：直接 nbrag_search_and_fetch() 一步到位
nbrag_find_definition()                # 3. 需要完整 class/function 定义时（Python 最佳）
    ↓
nbrag_get_raw_file()                   # 4. 看完整源码（无 overlap，无 scope）
或 nbrag_get_adjacent_chunks()          #    或扩展上下文（有 scope）
或 nbrag_get_chunks_by_lines()          #    或按行号取 chunk（有 scope）
或 nbrag_get_file_chunks()              #    或分页浏览全文件 chunks（有 scope）
    ↓
跨文件追踪：遇到未知符号 → 重复 2-4
```

## 对话示例

### 示例：用户问"这个项目怎么处理并发的？"

```
1. nbrag_stats()                              → 发现 collection 名
2. nbrag_search(query="并发处理", ...)         → 语义搜索找到相关文件
3. nbrag_grep(keyword="ThreadPool", ...)       → 精确定位类名（补语义搜索漏掉的）
4. nbrag_find_definition(symbol="ThreadPool", ...) → 获取完整类定义 + 方法列表
5. nbrag_get_raw_file(file_path="...", ...)    → 读完整源码验证细节
6. 总结回答用户
```

### 示例：用户问"get_by_id 函数在哪里定义的？"

```
1. nbrag_find_definition(symbol="get_by_id", ...) → AST 精确查找
   ↓ 如果没找到
2. nbrag_grep(keyword="get_by_id", ...)            → 正则 fallback
   ↓ 找到位置后
3. nbrag_get_raw_file(file_path="...", ...)        → 读完整源码
```

## 多轮检索策略

如果第一轮搜索结果不理想：

1. **换关键词**：用同义词或更具体/更宽泛的词重新 `nbrag_search`
2. **换策略**：语义搜索不行就试 `nbrag_grep` 精确搜索
3. **缩小范围**：用 `filter_filename` 限定文件（仅 `nbrag_search` / `nbrag_grep` 支持），**精确匹配文件名**（需含后缀，如 `"core.py"` 而非 `"core"`，不支持模糊匹配或路径）
4. **查定义**：找到了引用但不知道定义在哪 → `nbrag_find_definition`
5. **跨 collection**：不同知识库可能有不同内容

## 常见错误处理

### Collection 不存在

| 工具 | 返回信息 |
|------|---------|
| `nbrag_search` / `nbrag_search_and_fetch` | `collection 'xxx' does not exist. Available collections: [...] Use nbrag_add_document to create and import docs.` |
| `nbrag_grep` / `nbrag_find_definition` | **静默返回空**（与"无匹配"不可区分） |

→ 建议：用 `nbrag_stats()` 确认 collection 名称。

### Collection 为空

| 工具 | 返回信息 |
|------|---------|
| `nbrag_search` / `nbrag_search_and_fetch` | `collection 'xxx' is empty. Use nbrag_add_document to import docs first.` |

### Raw cache 缺失

| 工具 | 返回信息 |
|------|---------|
| `nbrag_get_raw_file` | `Raw file cache not found (doc_id=...). This file may have been imported before caching was enabled. Please re-import.` |
| `nbrag_search_and_fetch` | `[{file_path}] raw cache not available` |
| `nbrag_grep` / `nbrag_find_definition` | **静默返回空** |

→ 建议：重新导入该文件/目录。

### 其他常见错误

| 返回信息 | 含义 | 建议动作 |
|----------|------|---------|
| `No results (collection has N chunks, filter: xxx)` | 搜索无匹配 | 换关键词或去掉 filter |
| `No definition found ... Try nbrag_grep` | 符号未找到（或 AST 解析失败） | 用 `nbrag_grep` 扩大搜索 |
| `File not found: 'xxx'` | 文件路径或文件名不存在 | 检查路径是否正确 |
| `Document not found: 'xxx'` | 文档 ID 不存在 | 用 `nbrag_list` 查看有效 doc_id |
| `No chunks matching line range ...` | 行号范围内无 chunk | 调整行号或用 `nbrag_get_raw_file` |
| `[path] excerpt failed` | 自动抓取源码失败 | 改用 `nbrag_get_raw_file` 手动抓取 |

## 能力边界

- ❌ 此 Skill 只负责检索和读取已有代码，不生成新代码
- ❌ 不导入文档（`nbrag_add_document` 由用户手动在终端执行脚本完成）
- ❌ 不删除文档（`nbrag_delete` 由用户手动操作）
- ❌ 不修改任何文件，只读取和搜索
- ✅ 如果用户问的问题超出检索范围（如需要联网搜索），应如实告知能力限制

## 不需要 AI 调用的工具

以下工具通常由用户手动操作：

- `nbrag_add_document` — 知识库导入（人工一次性批量操作）
- `nbrag_delete` — 删除文档
- `nbrag_list` — 列出文档（除非用户明确要求）

`````

--- **end of file: nbrag/skills/nbrag-workflow/SKILL.md** (project: nbrag) --- 

---

# markdown content namespace: nbrag scripts 


## nbrag File Tree (relative dir: `scripts`)


`````

└── scripts
    ├── ingest_funboost.py
    ├── ingest_funboost_one_md.py
    ├── ingest_langchain_ai_codes_and_docs.py
    ├── ingest_langchain_ai_docs.py
    ├── ingest_project.py
    └── start_http_rag_mcp.py

`````

---


## nbrag (relative dir: `scripts`)  Included Files (total: 6 files)


- `scripts/ingest_funboost.py`

- `scripts/ingest_funboost_one_md.py`

- `scripts/ingest_langchain_ai_codes_and_docs.py`

- `scripts/ingest_langchain_ai_docs.py`

- `scripts/ingest_project.py`

- `scripts/start_http_rag_mcp.py`


---


--- **start of file: scripts/ingest_funboost.py** (project: nbrag) --- 

`````python
﻿"""
示例：批量导入项目到 RAG 知识库。

用法:
    # 1. 设置 API Key
    export NBRAG_API_KEY=sk-xxx

    # 2. 运行导入
    python scripts/import_project.py
"""

import my_load_config
from nbrag.core import batch_ingest


batch_ingest(
    paths=[
        "D:/codes/funboost/funboost",
        "D:/codes/funboost/test_frame",
        "D:/codes/funboost/tests",
        "D:/codes/funboost_docs/source/articles/c0.md",
        "D:/codes/funboost_docs/source/articles/c1.md",
        "D:/codes/funboost_docs/source/articles/c2.md",
        "D:/codes/funboost_docs/source/articles/c3.md",
        "D:/codes/funboost_docs/source/articles/c4.md",
        "D:/codes/funboost_docs/source/articles/c4b.md",
        "D:/codes/funboost_docs/source/articles/c6.md",
        "D:/codes/funboost_docs/source/articles/c7.md",
        "D:/codes/funboost_docs/source/articles/c8.md",
        "D:/codes/funboost_docs/source/articles/c9.md",
        "D:/codes/funboost_docs/source/articles/c10.md",
        "D:/codes/funboost_docs/source/articles/c11.md",
        "D:/codes/funboost_docs/source/articles/c12.md",
        "D:/codes/funboost_docs/source/articles/c13.md",
        "D:/codes/funboost_docs/source/articles/c14.md",
        "D:/codes/funboost_docs/source/articles/c15.md",
        "D:/codes/funboost_docs/source/articles/c20.md",
    ],
    collection_name="funboost",
    file_extensions=[".py", ".md",".html"],
    max_workers = 10,
    delete_first=True,
    verbose=True,
)

`````

--- **end of file: scripts/ingest_funboost.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_funboost_one_md.py** (project: nbrag) --- 

`````python
﻿"""
示例：批量导入项目到 RAG 知识库。

用法:
    # 1. 设置 API Key
    export NBRAG_API_KEY=sk-xxx

    # 2. 运行导入
    python scripts/import_project.py
"""

import my_load_config
from nbrag.core import batch_ingest


batch_ingest(
    paths=[
        "D:/codes/funboost/funboost_all_docs_and_codes.md",
    ],
    collection_name="funboost_all_docs_and_codes",
    file_extensions=[".md",],
    max_workers = 10,
    delete_first=True,
    verbose=True,
)

`````

--- **end of file: scripts/ingest_funboost_one_md.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_langchain_ai_codes_and_docs.py** (project: nbrag) --- 

`````python


import my_load_config
from nbrag.core import batch_ingest


batch_ingest(
    paths=[
       r'D:\codes\docs\src',
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_anthropic",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_classic",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_community",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_core",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_deepseek",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_google_genai",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_openai",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_protocol",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain_text_splitters",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langdetect",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langgraph",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langgraph_sdk",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langsmith",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\langchain",
       r"D:\ProgramData\miniconda3\envs\py312\Lib\site-packages\deepagents",
    ],
    collection_name="langchain_ai_codes_and_docs",
    file_extensions=[".py", ".mdx",".html",".md"],
    max_workers = 10,
    delete_first=True,
    verbose=True,
    chunk_size=1500,
    chunk_overlap=200,
)
`````

--- **end of file: scripts/ingest_langchain_ai_codes_and_docs.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_langchain_ai_docs.py** (project: nbrag) --- 

`````python


import my_load_config
from nbrag.core import batch_ingest


batch_ingest(
    paths=[
       r'D:\codes\docs\src',

    ],
    collection_name="langchain_ai_docs",
    file_extensions=[".py", ".mdx",".html",".md"],
    max_workers = 10,
    delete_first=True,
    verbose=True,
    chunk_size=1500,
    chunk_overlap=200,
)
`````

--- **end of file: scripts/ingest_langchain_ai_docs.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_project.py** (project: nbrag) --- 

`````python
﻿"""
示例：批量导入项目到 RAG 知识库。

用法:
    # 1. 设置 API Key
    export NBRAG_API_KEY=sk-xxx

    # 2. 运行导入
    python scripts/ingest_project.py
"""

from nbrag.core import batch_ingest

batch_ingest(
    paths=[
        # 替换为你要导入的项目路径
        # "D:/codes/your_project/src",
        # "D:/codes/your_project/docs",
    ],
    collection_name="your_project",
    delete_first=True,
    verbose=True,
)

`````

--- **end of file: scripts/ingest_project.py** (project: nbrag) --- 

---


--- **start of file: scripts/start_http_rag_mcp.py** (project: nbrag) --- 

`````python
﻿"""
启动 nbrag HTTP MCP Server。

    set NBRAG_API_KEY=sk-xxx
    python scripts/start_http_rag_mcp.py

    或者 python -m nbrag --transport streamable-http --port 9101
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_load_config

from nbrag.config import load_config
from nbrag.server import mcp

load_config()

PORT = 9101
mcp.settings.port = PORT

print(f"[nbrag] HTTP MCP server on http://localhost:{PORT}/mcp")

mcp.run(transport="streamable-http")


`````

--- **end of file: scripts/start_http_rag_mcp.py** (project: nbrag) --- 

---

