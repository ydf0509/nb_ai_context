
# 🤖 AI 上下文阅读协议 (由 nb_ai_context 生成)

> **此文档生成时间**：2026-06-16 14:54:29
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
  Ingest file or directory into knowledge base (chunking + embedding + indexing). Auto-creates collection if not exists.
  Supports any text file: code, docs, law, articles, manuals, etc. Python files get extra class/function scope enrichment.
  Note: Typically called by users via scripts for batch ingestion, not by AI during conversations.
  `````

- `def nbrag_search(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Knowledge base name, i.e. 知识库名字 (use nbrag_stats to see available names)'), top_k: int = Field(default=5, description='Number of results to return'), use_rerank: bool = Field(default=True, description='Enable reranker for better accuracy (recommended)'), use_bm25: bool = Field(default=True, description='Enable BM25 keyword matching + RRF fusion (recommended for precise names)'), filter_filename: str = Field(default='', description="Filter by filename (e.g. 'core.py'). BM25 auto-disabled when set")) -> str` `mcp.tool()`
  - *Line: 74*
  - **Docstring:**
  `````
  Search knowledge base (知识库) for relevant content. Works for code, docs, law, articles, or any imported text.
  
  IMPORTANT: If you don't know the collection_name, call nbrag_stats() first to see all available knowledge bases.
  collection_name = knowledge base name = 知识库名字 (e.g. user says "查funboost知识库" → collection_name="funboost").
  
  **PREFER nbrag_search_and_fetch** when the user asks 'how to do X', 'show me examples of X',
  or any knowledge/usage question — it auto-fetches complete file context and avoids fragmented chunks.
  **Use nbrag_search** only when you need fine-grained control (disable BM25/rerank) or metadata-only lookup.
  
  TIP: Don't pass the user's raw long question directly. Rewrite it into focused search terms.
  e.g. user asks "试用期干了5个月不转正，1年合同合法吗" → query="试用期 最长期限 1年合同"
  Then do a second search: query="违法约定试用期 赔偿" to find penalty clauses.
  
  Result format: [1/5] filename chunk:X/Y line:N-M scope:xxx doc_id:xxx dist:0.1234 score:0.9876
  Key fields for follow-up: file_path (for nbrag_get_raw_file), doc_id + chunk_index (for nbrag_get_adjacent_chunks).
  
  After search, use these follow-up tools to dig deeper:
    - nbrag_grep(keyword, collection_name) → exact keyword/regex search (code names, legal terms, article numbers)
    - nbrag_find_definition(symbol, collection_name) → complete class/function definition (Python .py files ONLY)
    - nbrag_get_raw_file(file_path, collection_name) → full file content without chunk overlap
    - nbrag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result
  
  If first search misses, try different keywords or use nbrag_grep for exact term matching.
  `````

- `def nbrag_search_and_fetch(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), top_k: int = Field(default=5, description='Number of search results to return'), fetch_top_n_raw: int = Field(default=3, description='Auto-fetch raw source for top N results (0 to skip)'), context_lines: int = Field(default=100, description='Lines of context around matched chunk'), filter_filename: str = Field(default='', description="Filter by filename (e.g. 'core.py')")) -> str` `mcp.tool()`
  - *Line: 166*
  - **Docstring:**
  `````
  Search + auto-fetch raw file content for top results in one call (saves a round-trip).
  
  **PREFER this over nbrag_search** when:
  - User asks 'how to do X', 'show me examples of X', 'what is X usage', or any knowledge/usage question.
  - You need both a quick answer AND the full source code backing it.
  - You want to avoid fragmented chunks and get complete file context immediately.
  
  **Use nbrag_search** only when:
  - You need fine-grained control (disable BM25, different chunk counts).
  - You only want metadata/summary, not full source.
  
  Always uses BM25+rerank for best quality.
  Same doc_id in multiple results is fetched only once with merged line range.
  `````

- `def nbrag_grep(keyword: str = Field(description="Keyword or regex (e.g. 'UserService', '侵权责任', 'Article 42', 'MAX_RETRIES')"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), max_results: int = Field(default=10, description='Maximum number of matches to return'), case_sensitive: bool = Field(default=False, description='Case-sensitive matching'), filter_filename: str = Field(default='', description="Filter by filename (e.g. 'booster.py')"), context_lines: int = Field(default=10, description='Context lines before/after each match (use 20+ for class headers)')) -> str` `mcp.tool()`
  - *Line: 292*
  - **Docstring:**
  `````
  Keyword/regex exact search in cached raw files. Complements nbrag_search (semantic search).
  
  Use cases where nbrag_search falls short:
    - Code: class/function names ('UserService'), constants ('MAX_RETRIES'), imports ('from myproject')
    - Law/docs: article numbers ('第四十二条'), exact legal terms ('侵权责任'), section titles
    - General: specific dates, proper nouns, technical terms, exact phrases
  
  Tip: use context_lines=15 to see surrounding context around the match.
  Typical workflow: nbrag_search (find direction) → nbrag_grep (pinpoint exact terms) → nbrag_get_raw_file (full context)
  `````

- `def nbrag_find_definition(symbol: str = Field(description="Symbol name (e.g. 'UserService', 'get_by_id', 'MyClass.__init__')"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), max_results: int = Field(default=5, description='Maximum number of definitions to return')) -> str` `mcp.tool()`
  - *Line: 331*
  - **Docstring:**
  `````
  Find complete class/function/method definition by symbol name.
  Python .py files: AST parsing for exact boundaries + methods summary. Non-Python: regex fallback (limited).
  IMPORTANT: Only works on imported .py files. Code snippets inside .md/.txt docs cannot be AST-parsed.
  For non-.py content, use nbrag_grep to search for keywords instead.
  `````

- `def nbrag_get_file_chunks(file_path: str = Field(description='Full path or filename (from nbrag_search results)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), start_chunk: int = Field(default=0, description='Start chunk index (0-based) for pagination'), max_chunks: int = Field(default=10, description='Max chunks to return')) -> str` `mcp.tool()`
  - *Line: 371*
  - **Docstring:**
  `````
  Paginated view of file chunks with scope and line metadata.
  Note: chunks have overlap. For clean source code without overlap, use nbrag_get_raw_file instead.
  `````

- `def nbrag_get_raw_file(file_path: str = Field(description='Full path or filename (from nbrag_search results)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), line_start: int = Field(default=-1, description='Start line (1-based), -1 for beginning'), line_end: int = Field(default=-1, description='End line (inclusive), -1 for end of file')) -> str` `mcp.tool()`
  - *Line: 391*
  - **Docstring:**
  `````
  Get cached raw file content without chunk overlap. Recommended for viewing full source code.
  Supports line_start/line_end for extracting specific line ranges.
  Only available for files imported with raw cache (re-import older files if needed).
  `````

- `def nbrag_get_adjacent_chunks(doc_id: str = Field(description='Document ID (from nbrag_search/nbrag_grep results)'), chunk_index: int = Field(description="Target chunk index (the X from 'chunk:X/Y' in results)"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), window: int = Field(default=3, description='Returns chunk_index ± window chunks')) -> str` `mcp.tool()`
  - *Line: 459*
  - **Docstring:**
  `````
  Get adjacent chunks around a specific chunk index, for expanding context of a search result.
  Requires doc_id and chunk_index from nbrag_search results (not file_path).
  Example: doc_id="abc123", chunk_index=3, window=2 → returns chunks 1-5
  `````

- `def nbrag_get_chunks_by_lines(doc_id: str = Field(description='Document ID (from nbrag_search/nbrag_grep results)'), line_start: int = Field(description="Start line (1-based, from 'line:N-M' in results)"), line_end: int = Field(description="End line (inclusive, from 'line:N-M' in results)"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)')) -> str` `mcp.tool()`
  - *Line: 476*
  - **Docstring:**
  `````
  Get all chunks covering a line range, with scope metadata.
  vs nbrag_get_raw_file: this returns chunks (with scope but has overlap),
  nbrag_get_raw_file returns raw code (no overlap but no scope).
  Example: doc_id="abc123", line_start=80, line_end=200
  `````

- `def nbrag_list(collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), limit: int = Field(default=100, description='Max docs to return (default 100, max 500)'), offset: int = Field(default=0, description='Skip first N docs (default 0). Use with limit for pagination')) -> str` `mcp.tool()`
  - *Line: 519*
  - **Docstring:**
  `````
  List documents in a knowledge base (filename, path, chunk count, doc_id).
  Returns paginated results by default (limit=100). Use offset for next page.
  Use returned doc_id with nbrag_delete to remove documents.
  `````

- `def nbrag_delete(doc_id: str = Field(description='Document ID to delete (from nbrag_list results)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)')) -> str` `mcp.tool()`
  - *Line: 555*
  - *Delete a document's vectors and cached files from the collection. Get doc_id from nbrag_list.*

- `def nbrag_stats() -> str` `mcp.tool()`
  - *Line: 569*
  - **Docstring:**
  `````
  Get all available knowledge bases (知识库) and their stats. CALL THIS FIRST if you don't know the collection_name.
  Returns: all collection names, doc count, chunk count, embedding/rerank model, storage path.
  Glossary: collection_name = knowledge base name = 知识库名字 (e.g. "funboost", "law_docs").
  After getting collection names, use nbrag_search to search within a specific knowledge base.
  `````

- `def main()`
  - *Line: 600*
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
- `import re`
- `import json`
- `import hashlib`
- `import httpx`
- `import chromadb`
- `import bm25s`
- `from nbrag.config import get_config`
- `from nbrag.chunker import chunk_text`
- `from nbrag.chunker import enrich_chunks`
- `from nbrag.chunker import collect_files`
- `from nbrag.chunker import DEFAULT_CHUNK_SIZE`
- `from nbrag.chunker import DEFAULT_CHUNK_OVERLAP`
- `from nbrag.loggers import logger`
- `import gc`
- `import shutil`
- `import ast as _ast`
- `import warnings as _warnings`
- `from nbrag.chunker import _extract_signature`
- `import shutil`
- `import time as _time`
- `import time as _time`
- `import time as _time`
- `import shutil`
- `import time as _time`
- `from concurrent.futures import ThreadPoolExecutor`
- `from concurrent.futures import as_completed`
- `import re`
- `import re`
- `import re`
- `import re`
- `import ast as _ast`
- `import warnings as _warnings`
- `from nbrag.chunker import _extract_signature`

#### 🔧 Public Functions (24)

- `def build_bm25_index(collection_name, documents, chunk_ids)`
  - *Line: 137*
  - *构建 BM25 索引并持久化到磁盘。*

- `def invalidate_bm25_cache(collection_name = None)`
  - *Line: 203*
  - *清除 BM25 索引缓存（导入/删除 collection 后调用）。*

- `def build_symbol_index(collection_name)`
  - *Line: 230*
  - **Docstring:**
  `````
  扫描 raw_files 中所有 .py 文件的 AST，构建 symbol 索引并持久化到磁盘。
  
  索引结构: {simple_name: [{doc_id, filename, source, type, qualified, line_start, line_end, sig, methods}, ...]}
  simple_name 是不含限定前缀的名字（如 "search"），qualified 是完整路径（如 "MyClass.search"）。
  `````

- `def invalidate_symbol_cache(collection_name = None)`
  - *Line: 326*
  - *清除 Symbol 索引缓存（导入/删除后调用）。*

- `def invalidate_doc_id_cache(collection_name = None)`
  - *Line: 398*
  - *清除 doc_id 映射缓存（导入/删除 collection 后调用）。*

- `def get_collection(name = 'default')`
  - *Line: 418*
  - *获取或创建一个 ChromaDB collection（写操作用）。*

- `def delete_collection(name)`
  - *Line: 433*
  - *删除整个 collection（清空该知识库）。*

- `def list_collections()`
  - *Line: 441*
  - *列出所有 collection。*

- `def embed(texts, max_retries = 10, sleep_interval = 0.0, verbose = False)`
  - *Line: 455*
  - *调用 Embedding API，自动分批，失败自动重试。*

- `def rerank(query, documents, top_n = 5, max_retries = 3)`
  - *Line: 504*
  - *调用 Rerank API，返回 (indices, scores)。scores 是 cross-encoder 的真实相关性分数。*

- `def prepare_file_no_embed(file_path, chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP)`
  - *Line: 604*
  - *阶段 1a：读取 + 切分 + Enrichment（无 Embedding，无 DB 操作，可并行）。*

- `def batch_embed_prepared(prepared_list, sleep_interval = 0.0, verbose = False)`
  - *Line: 640*
  - **Docstring:**
  `````
  阶段 1b：批量调用 Embedding API，跨文件合并 chunks 减少 API 调用。
  
  Args:
      prepared_list: 来自 prepare_file_no_embed 的结果列表
      sleep_interval: API 调用之间的间隔（秒）
      verbose: 是否输出详细日志
  
  Returns:
      更新后的 prepared_list，每个 ok 的结果会新增 "embeddings" 字段
  `````

- `def check_file_cache(file_path, collection_name = 'default')`
  - *Line: 689*
  - *检查文件是否已缓存且未修改。*

- `def ingest_file(file_path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, sleep_interval = 0.0, use_cache = True, verbose = False)`
  - *Line: 853*
  - *导入单个文件到知识库，返回结果 dict（串行版本，兼容旧调用）。*

- `def ingest_path(path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None, sleep_interval = 0.0, use_cache = True, verbose = False)`
  - *Line: 886*
  - *导入文件或目录到知识库。返回 (results_list, errors_list, skipped_count)。*

- `def batch_ingest(paths, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None, delete_first = False, on_progress = None, verbose = False, max_workers = 1, sleep_interval = 0.01, use_cache = True)`
  - *Line: 921*
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
      delete_first: 是否先清空旧数据再导入（适用于全量重建）。优先级高于 use_cache。
      on_progress: 可选回调 fn(current, total, file_path, result)，用于自定义进度展示。
      verbose: 是否打印详细日志。
      max_workers: Embedding 并发线程数。
                   1 = 串行（默认，兼容旧行为）；
                   2-4 = 并行读取+Embedding，串行写入 ChromaDB。
                   不建议超过 4，避免触发 Embedding API 频率限制。
      use_cache: 是否启用文件缓存检查（基于 mtime）。默认 True，未修改的文件会被跳过。
  `````

- `def search(query, collection_name = 'default', top_k = 5, use_rerank = True, use_bm25 = True, filter_filename = None)`
  - *Line: 1169*
  - **Docstring:**
  `````
  混合检索：Vector + BM25 → RRF 融合 → Reranker 精排。
  
  返回 (documents, metadatas, distances, rerank_used, total, rerank_scores)。
  rerank_scores: Reranker 的真实相关性分数列表（未 rerank 时为空列表）。
  `````

- `def get_file_chunks(file_identifier, collection_name = 'default', start_chunk = 0, max_chunks = 5, raw = False, line_start = -1, line_end = -1)`
  - *Line: 1250*
  - *按文件路径或文件名获取知识库中该文件的内容。*

- `def get_context_chunks(doc_id, collection_name = 'default', chunk_index = None, window = 2, line_start = None, line_end = None)`
  - *Line: 1370*
  - *获取指定文档的上下文 chunks。*

- `def grep_knowledge(keyword, collection_name = 'default', max_results = 10, case_sensitive = False, filter_filename = None, context_lines = 5)`
  - *Line: 1431*
  - *在知识库的原始缓存文件中进行关键词/正则搜索。*

- `def find_symbol_definition(symbol, collection_name = 'default', max_results = 5)`
  - *Line: 1497*
  - **Docstring:**
  `````
  在知识库中查找符号（类/函数/方法）的完整定义。
  
  优先使用预构建的 Symbol 索引（O(1) 查表 + 仅读取匹配文件），
  索引不存在时回退到全量 AST 扫描（兼容旧数据）。
  `````

- `def list_documents(collection_name = 'default', offset = 0, limit = None)`
  - *Line: 1715*
  - *列出知识库中已导入的文档。支持 offset/limit 分页。*

- `def delete_document(doc_id, collection_name = 'default')`
  - *Line: 1748*
  - *删除指定文档的所有向量数据及缓存文件。返回 (deleted_count, filename)。*

- `def get_stats()`
  - *Line: 1770*
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

- `bm25s`
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

**让 AI 基于真实内容回答，消除幻觉** — 把代码、文档、法律条文、技术手册等任何文本导入 nbrag，AI Agent 就能基于真实内容回答问题，不再凭训练数据"编"。

nbrag 是一个 Agentic RAG MCP Server：AI Agent 通过 12 个 MCP 工具自主多轮检索，支持接入 Cursor、Claude Code/Desktop、OpenCode、Cherry Studio、Open WebUI、Dify、Cline 等任何 MCP 兼容的 AI 产品。

### 典型场景

- **三方库/框架**：LangChain 版本迭代太快 AI 容易把 API 搞混，导入最新源码后彻底解决；冷门框架（如 funboost）AI 预训练不足，导入后秒变专家
- **私有项目**：公司内部 SDK、wiki、设计文档——Context7 等公开服务永远不可能收录的内容
- **专业知识**：法律法规全文、医学指南、行业标准——任何需要 AI 精准引用而非"大概记得"的领域

## 为什么不用 Context7？

Context7 是优秀的 MCP 文档服务（56K+ stars），但它是"预制菜"——只能查它已收录的公开库文档片段。

| | Context7 | **nbrag** |
|---|---------|-----------|
| 数据来源 | Upstash 预索引的 GitHub 文档 | **用户自己导入任何文件** |
| 内容深度 | 教程级代码片段 | **源码级**（每个函数、每行注释） |
| 私有库/内部框架 | 不支持 | **完全支持** |
| 更新时效 | 取决于 Context7 爬取频率 | **导入即可用** |
| 检索管线 | 向量搜索 + 重排序 | **BM25 + Vector + RRF + Reranker 四级管线** |
| 离线/自部署 | 依赖 context7.com 云服务 | **本地 ChromaDB + 可配置 API** |
| 工具数量 | 2 个 | **12 个互补工具**（搜索 + grep + AST 定位 + 原文读取） |

**两者互补**：Context7 适合快速查主流库用法，nbrag 适合深入理解源码、使用私有库、或追求最高检索质量。

## 为什么不是 Naive RAG？

| | Naive RAG | **Agentic RAG (本项目)** |
|---|-----------|----------------------|
| 检索触发 | 每次提问自动检索 top-5 注入 | AI 自主决定是否检索、用哪个工具 |
| 检索轮次 | 1 次 | 多轮（实测 m 次搜索 + n 次文件读取） |
| 查询构造 | 用户原文 | AI 重写查询、组合多种检索策略 |
| 工具种类 | 仅语义搜索 | 混合检索（Vector + BM25 → RRF 融合）+ grep + AST 符号定位 + 原文读取 |
| 分析深度 | 浅层描述 | 完整的跨文件调用链图 |
| 准确度 | 浅层匹配，容易遗漏 | **显著优于 Naive RAG**，跨文件关联更完整 |

核心观点：**检索不是管道，是 Agent 的一种能力。**

### 为什么不在 nbrag 内部做 Query Rewrite？

nbrag 刻意**不在内部做查询改写**（虽然技术上可以加），因为 AI Agent 本身就是最好的 query rewriter：

```
用户: "公司让我试用期干了5个月不转正，签1年合同，合法吗？能要什么赔偿？"
         ↓
    AI Agent（理解问题 → 拆解 → 重写查询）
         ↓
  第1轮: nbrag_search("试用期 最长期限 1年合同")        → 命中第19条
  第2轮: nbrag_search("违法约定试用期 赔偿标准")        → 命中第83条
  第3轮: nbrag_grep("第十九条")                          → 精确定位原文
  第4轮: nbrag_get_raw_file(...)                         → 读完整法条上下文
         ↓
    AI 综合 4 轮结果，给用户完整回答
```

AI 理解上下文、对话历史和领域知识，它改写查询的效果远好于任何规则引擎或小模型。所以 nbrag 的设计原则是：**把"智能"留给 AI，把"工具"做好给 AI 用。**

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
    "nbrag": {
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
    "nbrag": {
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
    "nbrag": {
      "type": "http",  //可以省略,因为有url，就能自动推断是http模式
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

AI 会自动调用 `nbrag_add_document` 导入，再用 `nbrag_search` + `nbrag_grep` 等工具多轮检索回答你的问题。

#### 方式 B: 手动脚本导入（推荐大批量）

手动导入更灵活——可以精确指定目录、过滤文件后缀、控制 chunk 参数：

```python
from nbrag.core import batch_ingest

# 示例 1：导入 Python 项目源码
batch_ingest(
    paths=["D:/codes/my_project/src", "D:/codes/my_project/docs"],
    collection_name="my_project",
    file_extensions=[".py", ".md"],
    delete_first=True,
    verbose=True,
)

# 示例 2：导入法律法规文本
batch_ingest(
    paths=["D:/docs/civil_code"],
    collection_name="civil_code",
    file_extensions=[".md", ".txt"],
    delete_first=True,
    verbose=True,
)
```

参见 `scripts/` 目录下的示例：
- `scripts/ingest_project.py` — 通用项目导入模板
- `scripts/ingest_ex1/` — 《中华人民共和国民法典》全文导入示例
- `scripts/ingest_ex2_marriage_law/` — 婚姻家庭法司法解释导入示例

## 12 个工具

| 类别 | 工具 | 功能 |
|------|------|------|
| **导入** | `nbrag_add_document` | 导入文件/目录（支持代码、文档、法律条文、技术手册等任何文本） |
| **混合检索** | `nbrag_search` | Vector + BM25 → RRF 融合 → Rerank 精排 |
| **混合检索** | `nbrag_search_and_fetch` | 混合搜索 + 自动取原文（省一次 round-trip） |
| **精确检索** | `nbrag_grep` | 关键词/正则搜索（法条编号、API 名、专业术语等精确匹配） |
| **精确检索** | `nbrag_find_definition` | AST 定位 class/function 完整定义（仅 `.py` 文件） |
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

**代码场景**（Python 源码、框架 API）：
```
1. nbrag_search → 混合检索，找到相关文件和大致位置
2. nbrag_grep → 精确定位类名/方法名/常量（行级精度）
3. nbrag_find_definition → 获取完整的类/函数定义（仅 .py 文件）
4. nbrag_get_raw_file → 读取完整源码验证细节
5. 跨文件追踪：发现未知符号时重复 2-4 步
```

**通用知识场景**（法律条文、医学指南、技术手册等）：
```
1. nbrag_search → 语义搜索，找到相关章节/条款
2. nbrag_grep → 精确匹配条文编号、专业术语、关键词
3. nbrag_get_raw_file → 读取完整原文确认上下文
4. nbrag_get_adjacent_chunks → 扩展上下文，查看前后条款
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

### 为什么三存储？

- **ChromaDB**：存向量 chunks（有 overlap），用于语义搜索
- **raw_files/**：存原始文件快照（无 overlap），用于精确行号读取
- **bm25_index/**：BM25 稀疏索引（bm25s 持久化），用于关键词检索 + RRF 融合

AI 经常需要看完整源码，如果只有 chunks 会有 overlap 重复，浪费 token 还容易困惑。
BM25 索引和 Vector 索引并行查询，通过 RRF 融合后再 Rerank，比纯语义搜索在精确关键词查询上 recall 更高。

### 为什么 BM25 + RRF 混合检索？

纯向量搜索有系统性盲区：搜 `"BrokerEnum"` 这种精确类名，向量距离不一定最近；搜 `"REDIS_BULK_PUSH"` 这种常量名，语义空间中锚点弱。BM25 补上了精确关键词匹配这一环。

两路结果通过 **RRF (Reciprocal Rank Fusion)** 融合——只看排名不看分数（BM25 分数无界，cosine 分数 [-1,1]，直接加权不可比），两路共识文档排名最高，k=60 是 2009 年 SIGIR 论文的标准值，无需调参。

分词器针对代码做了特殊处理：拆 camelCase (`getUserById` → `get user by id`)、拆 snake_case、去 chunk header。对于非代码文本（法律、医学等），BM25 同样有效——中文分词和关键词匹配天然适用于任何自然语言文本。

### 为什么 AST scope 注入？

**仅对 `.py` 文件生效。** 每个 Python chunk 的 embedding 前注入 `[File: path] [Scope: MyClass.my_method] [Sig: def my_method(self, x)]`。
这样搜索 "process 方法" 时更容易命中 `class DataProcessor` 下的 `def process(self, data)`，而不是随机匹配到别的 "process" 字符串。

非 Python 文件（`.md`、`.txt` 等）只注入 `[File: path]` 头部，不做 AST 解析。这些文件依赖语义搜索 + BM25 关键词匹配 + grep 精确查找。

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
| BM25 | bm25s（100-500x faster than rank_bm25，支持持久化） |
| 融合 | RRF (Reciprocal Rank Fusion, k=60) |
| 分块 | LangChain TextSplitter + 自研 AST 增强（Python）/ 通用分块（其他文本） |
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
dynamic = ["version"]
description = "Agentic RAG MCP Server — 12 tools for AI-driven multi-round code retrieval that outperforms naive single-shot RAG"
readme = "README.md"
license = {text = "MIT"}
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
    "bm25s[full]>=0.2.0",
]

[project.urls]
Homepage = "https://github.com/ydf0509/nbrag"
Repository = "https://github.com/ydf0509/nbrag"

[project.scripts]
nbrag = "nbrag.server:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.version]
path = "nbrag/__init__.py"

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
*Line: 20*

**Class Variables (3):**
- `api_key: str = ''`
- `base_url: str = 'https://api.siliconflow.cn/v1'`
- `model: str = 'BAAI/bge-m3'`

##### 📌 `class RerankConfig`
*Line: 27*

**Class Variables (1):**
- `model: str = 'BAAI/bge-reranker-v2-m3'`

##### 📌 `class StorageConfig`
*Line: 32*

**Class Variables (2):**
- `db_path: str = _DEFAULT_DB_PATH`
- `raw_files_path: str = ''`

##### 📌 `class ChunkingConfig`
*Line: 38*

**Class Variables (2):**
- `chunk_size: int = 1500`
- `chunk_overlap: int = 200`

##### 📌 `class RagConfig`
*Line: 44*

**Class Variables (4):**
- `embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)`
- `rerank: RerankConfig = field(default_factory=RerankConfig)`
- `storage: StorageConfig = field(default_factory=StorageConfig)`
- `chunking: ChunkingConfig = field(default_factory=ChunkingConfig)`

#### 🔧 Public Functions (2)

- `def load_config(cli_args = None) -> RagConfig`
  - *Line: 95*
  - *加载配置：CLI > 环境变量 > YAML > 默认值。*

- `def get_config() -> RagConfig`
  - *Line: 170*
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


# 项目根目录（config.py 位于 <PROJECT_ROOT>/nbrag/config.py）
# 用 __file__ 推导绝对路径，确保不论从哪里启动脚本，db_path 都指向同一个固定位置
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DEFAULT_DB_PATH = os.path.join(_PROJECT_ROOT, "rag_db")


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
    db_path: str = _DEFAULT_DB_PATH
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
        or _DEFAULT_DB_PATH
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
- `import re`
- `import json`
- `import hashlib`
- `import httpx`
- `import chromadb`
- `import bm25s`
- `from nbrag.config import get_config`
- `from nbrag.chunker import chunk_text`
- `from nbrag.chunker import enrich_chunks`
- `from nbrag.chunker import collect_files`
- `from nbrag.chunker import DEFAULT_CHUNK_SIZE`
- `from nbrag.chunker import DEFAULT_CHUNK_OVERLAP`
- `from nbrag.loggers import logger`
- `import gc`
- `import shutil`
- `import ast as _ast`
- `import warnings as _warnings`
- `from nbrag.chunker import _extract_signature`
- `import shutil`
- `import time as _time`
- `import time as _time`
- `import time as _time`
- `import shutil`
- `import time as _time`
- `from concurrent.futures import ThreadPoolExecutor`
- `from concurrent.futures import as_completed`
- `import re`
- `import re`
- `import re`
- `import re`
- `import ast as _ast`
- `import warnings as _warnings`
- `from nbrag.chunker import _extract_signature`

#### 🔧 Public Functions (24)

- `def build_bm25_index(collection_name, documents, chunk_ids)`
  - *Line: 137*
  - *构建 BM25 索引并持久化到磁盘。*

- `def invalidate_bm25_cache(collection_name = None)`
  - *Line: 203*
  - *清除 BM25 索引缓存（导入/删除 collection 后调用）。*

- `def build_symbol_index(collection_name)`
  - *Line: 230*
  - **Docstring:**
  `````
  扫描 raw_files 中所有 .py 文件的 AST，构建 symbol 索引并持久化到磁盘。
  
  索引结构: {simple_name: [{doc_id, filename, source, type, qualified, line_start, line_end, sig, methods}, ...]}
  simple_name 是不含限定前缀的名字（如 "search"），qualified 是完整路径（如 "MyClass.search"）。
  `````

- `def invalidate_symbol_cache(collection_name = None)`
  - *Line: 326*
  - *清除 Symbol 索引缓存（导入/删除后调用）。*

- `def invalidate_doc_id_cache(collection_name = None)`
  - *Line: 398*
  - *清除 doc_id 映射缓存（导入/删除 collection 后调用）。*

- `def get_collection(name = 'default')`
  - *Line: 418*
  - *获取或创建一个 ChromaDB collection（写操作用）。*

- `def delete_collection(name)`
  - *Line: 433*
  - *删除整个 collection（清空该知识库）。*

- `def list_collections()`
  - *Line: 441*
  - *列出所有 collection。*

- `def embed(texts, max_retries = 10, sleep_interval = 0.0, verbose = False)`
  - *Line: 455*
  - *调用 Embedding API，自动分批，失败自动重试。*

- `def rerank(query, documents, top_n = 5, max_retries = 3)`
  - *Line: 504*
  - *调用 Rerank API，返回 (indices, scores)。scores 是 cross-encoder 的真实相关性分数。*

- `def prepare_file_no_embed(file_path, chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP)`
  - *Line: 604*
  - *阶段 1a：读取 + 切分 + Enrichment（无 Embedding，无 DB 操作，可并行）。*

- `def batch_embed_prepared(prepared_list, sleep_interval = 0.0, verbose = False)`
  - *Line: 640*
  - **Docstring:**
  `````
  阶段 1b：批量调用 Embedding API，跨文件合并 chunks 减少 API 调用。
  
  Args:
      prepared_list: 来自 prepare_file_no_embed 的结果列表
      sleep_interval: API 调用之间的间隔（秒）
      verbose: 是否输出详细日志
  
  Returns:
      更新后的 prepared_list，每个 ok 的结果会新增 "embeddings" 字段
  `````

- `def check_file_cache(file_path, collection_name = 'default')`
  - *Line: 689*
  - *检查文件是否已缓存且未修改。*

- `def ingest_file(file_path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, sleep_interval = 0.0, use_cache = True, verbose = False)`
  - *Line: 853*
  - *导入单个文件到知识库，返回结果 dict（串行版本，兼容旧调用）。*

- `def ingest_path(path, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None, sleep_interval = 0.0, use_cache = True, verbose = False)`
  - *Line: 886*
  - *导入文件或目录到知识库。返回 (results_list, errors_list, skipped_count)。*

- `def batch_ingest(paths, collection_name = 'default', chunk_size = DEFAULT_CHUNK_SIZE, chunk_overlap = DEFAULT_CHUNK_OVERLAP, file_extensions = None, delete_first = False, on_progress = None, verbose = False, max_workers = 1, sleep_interval = 0.01, use_cache = True)`
  - *Line: 921*
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
      delete_first: 是否先清空旧数据再导入（适用于全量重建）。优先级高于 use_cache。
      on_progress: 可选回调 fn(current, total, file_path, result)，用于自定义进度展示。
      verbose: 是否打印详细日志。
      max_workers: Embedding 并发线程数。
                   1 = 串行（默认，兼容旧行为）；
                   2-4 = 并行读取+Embedding，串行写入 ChromaDB。
                   不建议超过 4，避免触发 Embedding API 频率限制。
      use_cache: 是否启用文件缓存检查（基于 mtime）。默认 True，未修改的文件会被跳过。
  `````

- `def search(query, collection_name = 'default', top_k = 5, use_rerank = True, use_bm25 = True, filter_filename = None)`
  - *Line: 1169*
  - **Docstring:**
  `````
  混合检索：Vector + BM25 → RRF 融合 → Reranker 精排。
  
  返回 (documents, metadatas, distances, rerank_used, total, rerank_scores)。
  rerank_scores: Reranker 的真实相关性分数列表（未 rerank 时为空列表）。
  `````

- `def get_file_chunks(file_identifier, collection_name = 'default', start_chunk = 0, max_chunks = 5, raw = False, line_start = -1, line_end = -1)`
  - *Line: 1250*
  - *按文件路径或文件名获取知识库中该文件的内容。*

- `def get_context_chunks(doc_id, collection_name = 'default', chunk_index = None, window = 2, line_start = None, line_end = None)`
  - *Line: 1370*
  - *获取指定文档的上下文 chunks。*

- `def grep_knowledge(keyword, collection_name = 'default', max_results = 10, case_sensitive = False, filter_filename = None, context_lines = 5)`
  - *Line: 1431*
  - *在知识库的原始缓存文件中进行关键词/正则搜索。*

- `def find_symbol_definition(symbol, collection_name = 'default', max_results = 5)`
  - *Line: 1497*
  - **Docstring:**
  `````
  在知识库中查找符号（类/函数/方法）的完整定义。
  
  优先使用预构建的 Symbol 索引（O(1) 查表 + 仅读取匹配文件），
  索引不存在时回退到全量 AST 扫描（兼容旧数据）。
  `````

- `def list_documents(collection_name = 'default', offset = 0, limit = None)`
  - *Line: 1715*
  - *列出知识库中已导入的文档。支持 offset/limit 分页。*

- `def delete_document(doc_id, collection_name = 'default')`
  - *Line: 1748*
  - *删除指定文档的所有向量数据及缓存文件。返回 (deleted_count, filename)。*

- `def get_stats()`
  - *Line: 1770*
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
import re
import json
import hashlib


import httpx
import chromadb
import bm25s
from nbrag.config import get_config
from nbrag.chunker import (
    chunk_text, enrich_chunks, collect_files,
    DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP,
)
from nbrag.loggers import logger

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

_bm25_cache = {}  # collection_name -> (bm25s.BM25, chunk_ids_list)

_CHROMA_GET_BATCH = 500  # SQLite 默认 999 参数限制，预留余量


def _batch_get(col, include, ids=None, where=None):
    """
    分页获取 ChromaDB collection 数据，避免 SQLite 'too many SQL variables' 错误。

    SQLite 默认最多 999 个 SQL 参数；Chromadb 在通过 `col.get(include=["metadatas"])`
    全量读取大集合时会对每条记录使用占位符参数，超过限制即报错。本函数将大查询
    拆成 ≤ 500 的批次后聚合。

    调用方约定:
      - 提供了 `ids` 时按 ids 分批（适用于 BM25 召回后的补充读取）。
      - 只提供 `where` 时走单查询（单 doc_id/单 source 的过滤结果不会超过 999）。
      - 什么都不提供时先拿 id 列表再分批取 include 内容。
    """
    # 少量 ids 或有 where 过滤器时，直接查询即可，结果集不会过大
    if where is not None:
        kwargs = {"include": list(include)}
        if ids is not None:
            kwargs["ids"] = list(ids)
        kwargs["where"] = where
        return col.get(**kwargs)

    if ids is not None:
        ids_list = list(ids)
        if len(ids_list) <= _CHROMA_GET_BATCH:
            return col.get(ids=ids_list, include=list(include))
        result = {"ids": [], "documents": [], "metadatas": []}
        for i in range(0, len(ids_list), _CHROMA_GET_BATCH):
            batch = col.get(ids=ids_list[i:i + _CHROMA_GET_BATCH], include=list(include))
            for key in result:
                if key in batch and batch[key] is not None:
                    result[key].extend(batch[key])
        return result

    # 全量查询：先拿 id（只查 id 不涉及 metadata 表，安全），再分批拿数据
    id_only = col.get(include=[])
    all_ids = id_only.get("ids", [])
    if not all_ids:
        return {"ids": [], "documents": [], "metadatas": []}
    if len(all_ids) <= _CHROMA_GET_BATCH:
        return col.get(include=list(include))
    result = {"ids": [], "documents": [], "metadatas": []}
    for i in range(0, len(all_ids), _CHROMA_GET_BATCH):
        batch = col.get(ids=all_ids[i:i + _CHROMA_GET_BATCH], include=list(include))
        for key in result:
            if key in batch and batch[key] is not None:
                result[key].extend(batch[key])
    return result


# ─── BM25 混合检索 ─────────────────────────────────────────

_CAMEL_SPLIT_RE = re.compile(r'([a-z])([A-Z])')
_CAMEL_UPPER_RE = re.compile(r'([A-Z]+)([A-Z][a-z])')
_HEADER_RE = re.compile(r'^#\s*\[File:.*$', re.MULTILINE)


def _preprocess_for_bm25(text):
    """预处理文本供 BM25 分词：去 chunk header、拆 camelCase/snake_case、小写化。"""
    text = _HEADER_RE.sub('', text)
    text = _CAMEL_SPLIT_RE.sub(r'\1 \2', text)
    text = _CAMEL_UPPER_RE.sub(r'\1 \2', text)
    text = text.replace('_', ' ')
    return text.lower()


def _bm25_index_dir(collection_name):
    return os.path.join(_cfg().storage.db_path, "bm25_index", collection_name)


def build_bm25_index(collection_name, documents, chunk_ids):
    """构建 BM25 索引并持久化到磁盘。"""
    if not documents:
        return
    preprocessed = [_preprocess_for_bm25(doc) for doc in documents]
    corpus_tokens = bm25s.tokenize(preprocessed)

    retriever = bm25s.BM25()
    retriever.index(corpus_tokens)

    index_dir = _bm25_index_dir(collection_name)
    os.makedirs(index_dir, exist_ok=True)
    retriever.save(index_dir)
    with open(os.path.join(index_dir, "chunk_ids.json"), "w") as f:
        json.dump(chunk_ids, f)

    _bm25_cache[collection_name] = (retriever, chunk_ids)


def _load_bm25_index(collection_name):
    """从磁盘加载 BM25 索引到内存缓存。"""
    if collection_name in _bm25_cache:
        return _bm25_cache[collection_name]

    index_dir = _bm25_index_dir(collection_name)
    if not os.path.isdir(index_dir):
        return None, None

    ids_path = os.path.join(index_dir, "chunk_ids.json")
    if not os.path.isfile(ids_path):
        return None, None

    try:
        retriever = bm25s.BM25.load(index_dir, mmap=False)
        with open(ids_path, "r") as f:
            chunk_ids = json.load(f)
        _bm25_cache[collection_name] = (retriever, chunk_ids)
        return retriever, chunk_ids
    except Exception:
        return None, None


def _bm25_search(query, collection_name, top_k):
    """BM25 检索，返回 (ids_list, scores_list)。"""
    retriever, chunk_ids = _load_bm25_index(collection_name)
    if retriever is None:
        return [], []

    query_tokens = bm25s.tokenize(_preprocess_for_bm25(query))
    n = min(top_k, len(chunk_ids))
    results, scores = retriever.retrieve(query_tokens, k=n)

    ids = [chunk_ids[idx] for idx in results[0]]
    return ids, scores[0].tolist()


def _rrf_fusion(vec_ids, bm25_ids, k=60):
    """Reciprocal Rank Fusion — 合并两路检索结果，返回按 RRF 分数排序的 id 列表。"""
    scores = {}
    for rank, doc_id in enumerate(vec_ids):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    for rank, doc_id in enumerate(bm25_ids):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    return [doc_id for doc_id, _ in sorted(scores.items(), key=lambda x: x[1], reverse=True)]


def invalidate_bm25_cache(collection_name=None):
    """清除 BM25 索引缓存（导入/删除 collection 后调用）。"""
    import gc
    import shutil
    if collection_name:
        _bm25_cache.pop(collection_name, None)
        gc.collect()
        index_dir = _bm25_index_dir(collection_name)
        if os.path.isdir(index_dir):
            shutil.rmtree(index_dir, ignore_errors=True)
    else:
        _bm25_cache.clear()
        gc.collect()
        bm25_root = os.path.join(_cfg().storage.db_path, "bm25_index")
        if os.path.isdir(bm25_root):
            shutil.rmtree(bm25_root, ignore_errors=True)


# ─── Symbol 索引（加速 find_definition）──────────────────

_symbol_cache = {}  # collection_name -> {simple_name: [entries]}


def _symbol_index_dir(collection_name):
    return os.path.join(_cfg().storage.db_path, "symbol_index", collection_name)


def build_symbol_index(collection_name):
    """扫描 raw_files 中所有 .py 文件的 AST，构建 symbol 索引并持久化到磁盘。

    索引结构: {simple_name: [{doc_id, filename, source, type, qualified, line_start, line_end, sig, methods}, ...]}
    simple_name 是不含限定前缀的名字（如 "search"），qualified 是完整路径（如 "MyClass.search"）。
    """
    import ast as _ast
    import warnings as _warnings
    from nbrag.chunker import _extract_signature

    raw_dir = os.path.join(_raw_files_dir(), collection_name)
    if not os.path.isdir(raw_dir):
        return

    doc_id_to_info = _get_doc_id_map(collection_name)
    index = {}  # simple_name -> [entry, ...]

    for fname in os.listdir(raw_dir):
        if not fname.lower().endswith(".py"):
            continue
        doc_id = os.path.splitext(fname)[0]
        info = doc_id_to_info.get(doc_id, {})
        fpath = os.path.join(raw_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            continue
        try:
            with _warnings.catch_warnings():
                _warnings.simplefilter("ignore", SyntaxWarning)
                tree = _ast.parse(content)
        except SyntaxError:
            continue

        def _walk(node, parent_chain=""):
            for child in _ast.iter_child_nodes(node):
                if not isinstance(child, (_ast.ClassDef, _ast.FunctionDef, _ast.AsyncFunctionDef)):
                    continue
                name = child.name
                qualified = f"{parent_chain}.{name}" if parent_chain else name
                start = child.lineno
                end = child.end_lineno if hasattr(child, 'end_lineno') and child.end_lineno else start
                sym_type = "class" if isinstance(child, _ast.ClassDef) else "function"
                sig = _extract_signature(child)

                methods = []
                if isinstance(child, _ast.ClassDef):
                    for sub in _ast.iter_child_nodes(child):
                        if isinstance(sub, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
                            methods.append(_extract_signature(sub))

                entry = {
                    "doc_id": doc_id,
                    "filename": info.get("filename", fname),
                    "source": info.get("source", fpath),
                    "type": sym_type,
                    "qualified": qualified,
                    "line_start": start,
                    "line_end": end,
                    "sig": sig,
                    "methods": methods,
                }
                index.setdefault(name, []).append(entry)
                _walk(child, qualified)

        _walk(tree)

    index_dir = _symbol_index_dir(collection_name)
    os.makedirs(index_dir, exist_ok=True)
    with open(os.path.join(index_dir, "symbols.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)

    _symbol_cache[collection_name] = index
    return index


def _load_symbol_index(collection_name):
    """从磁盘加载 Symbol 索引到内存缓存。"""
    if collection_name in _symbol_cache:
        return _symbol_cache[collection_name]

    index_dir = _symbol_index_dir(collection_name)
    symbols_path = os.path.join(index_dir, "symbols.json")
    if not os.path.isfile(symbols_path):
        return None

    try:
        with open(symbols_path, "r", encoding="utf-8") as f:
            index = json.load(f)
        _symbol_cache[collection_name] = index
        return index
    except Exception:
        return None


def invalidate_symbol_cache(collection_name=None):
    """清除 Symbol 索引缓存（导入/删除后调用）。"""
    import shutil
    if collection_name:
        _symbol_cache.pop(collection_name, None)
        index_dir = _symbol_index_dir(collection_name)
        if os.path.isdir(index_dir):
            shutil.rmtree(index_dir, ignore_errors=True)
    else:
        _symbol_cache.clear()
        symbol_root = os.path.join(_cfg().storage.db_path, "symbol_index")
        if os.path.isdir(symbol_root):
            shutil.rmtree(symbol_root, ignore_errors=True)


def _query_symbol_index(symbol, index):
    """在 Symbol 索引中查找匹配项，返回 entry 列表。

    匹配逻辑与原 find_symbol_definition 一致：
      name == symbol  OR  qualified == symbol  OR  qualified.endswith('.{symbol}')
    """
    results = []
    seen = set()
    lookup_key = symbol.rsplit(".", 1)[-1]

    for entry in index.get(lookup_key, []):
        name = entry["qualified"].rsplit(".", 1)[-1]
        qualified = entry["qualified"]
        if name == symbol or qualified == symbol or qualified.endswith(f".{symbol}"):
            key = (entry["doc_id"], entry["line_start"])
            if key not in seen:
                seen.add(key)
                results.append(entry)

    if "." in symbol:
        first_part = symbol.split(".")[0]
        for entry in index.get(first_part, []):
            qualified = entry["qualified"]
            if qualified == symbol or qualified.endswith(f".{symbol}"):
                key = (entry["doc_id"], entry["line_start"])
                if key not in seen:
                    seen.add(key)
                    results.append(entry)

    return results


def _get_doc_id_map(collection_name):
    """获取 collection 的 doc_id → {filename, source} 映射（带 600s 内存缓存）。"""
    import time as _time
    now = _time.time()
    if (collection_name in _doc_id_cache
            and now - _doc_id_cache_ts.get(collection_name, 0) < 600):
        return _doc_id_cache[collection_name]

    col = _get_existing_collection(collection_name)
    if col is None:
        return {}
    all_meta = _batch_get(col, include=["metadatas"])
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
    invalidate_bm25_cache(name)
    invalidate_symbol_cache(name)


def list_collections():
    """列出所有 collection。"""
    return _get_chroma().list_collections()


_http_client = None

def _get_http_client():
    global _http_client
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.Client(timeout=120)
    return _http_client


def embed(texts, max_retries=10, sleep_interval=0.0, verbose=False):
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
    total_chunks = len(texts)
    num_batches = (total_chunks + EMBEDDING_BATCH_SIZE - 1) // EMBEDDING_BATCH_SIZE
    
    for batch_idx, i in enumerate(range(0, total_chunks, EMBEDDING_BATCH_SIZE)):
        if i > 0 and sleep_interval > 0:
            _time.sleep(sleep_interval)
        batch = texts[i:i + EMBEDDING_BATCH_SIZE]
        if verbose:
            processed = min(i + EMBEDDING_BATCH_SIZE, total_chunks)
            print(f"  [embed {batch_idx + 1:>4}/{num_batches}] {processed}/{total_chunks} chunks")
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
            except Exception as e:
                logger.error(f"Embedding API error: {e} , attempt :{attempt}")
                if attempt < max_retries - 1:
                    _time.sleep(2 ** attempt)
                else:
                    raise
    return all_embeddings


def rerank(query, documents, top_n=5, max_retries=3):
    """调用 Rerank API，返回 (indices, scores)。scores 是 cross-encoder 的真实相关性分数。"""
    import time as _time
    cfg = _cfg()
    if not cfg.embedding.api_key or not cfg.rerank.model:
        n = min(top_n, len(documents))
        return list(range(n)), [0.0] * n

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
            indices = [r["index"] for r in data["results"]]
            scores = [r.get("relevance_score", 0.0) for r in data["results"]]
            return indices, scores
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

def prepare_file_no_embed(file_path, chunk_size=DEFAULT_CHUNK_SIZE,
                          chunk_overlap=DEFAULT_CHUNK_OVERLAP):
    """阶段 1a：读取 + 切分 + Enrichment（无 Embedding，无 DB 操作，可并行）。"""
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        return {"ok": False, "error": f"Cannot read {file_path}: {e}"}

    if not text.strip():
        return {"ok": False, "skipped": True, "reason": f"Empty file: {os.path.basename(file_path)}"}

    file_ext = os.path.splitext(file_path)[1]
    abs_path = _normalize_path(file_path)
    file_mtime = os.path.getmtime(file_path)
    raw_chunks = chunk_text(text, chunk_size, chunk_overlap, file_ext=file_ext)
    if not raw_chunks:
        return {"ok": False, "skipped": True, "reason": f"No chunks after split: {os.path.basename(file_path)}"}

    enriched_chunks, line_ranges, scopes = enrich_chunks(
        raw_chunks, text, file_path=abs_path, file_ext=file_ext,
    )

    filename = os.path.basename(file_path)
    doc_id = hashlib.md5(abs_path.encode()).hexdigest()[:12]

    return {
        "ok": True, "filename": filename, "file_ext": file_ext,
        "text": text, "abs_path": abs_path, "doc_id": doc_id,
        "enriched_chunks": enriched_chunks,
        "line_ranges": line_ranges, "scopes": scopes,
        "chars": len(text), "chunks": len(enriched_chunks),
        "file_mtime": file_mtime,
    }


def batch_embed_prepared(prepared_list, sleep_interval=0.0, verbose=False):
    """阶段 1b：批量调用 Embedding API，跨文件合并 chunks 减少 API 调用。

    Args:
        prepared_list: 来自 prepare_file_no_embed 的结果列表
        sleep_interval: API 调用之间的间隔（秒）
        verbose: 是否输出详细日志

    Returns:
        更新后的 prepared_list，每个 ok 的结果会新增 "embeddings" 字段
    """
    all_chunks = []
    chunk_refs = []

    for file_idx, p in enumerate(prepared_list):
        if not p.get("ok"):
            continue
        for chunk_idx, chunk in enumerate(p["enriched_chunks"]):
            all_chunks.append(chunk)
            chunk_refs.append((file_idx, chunk_idx))

    if not all_chunks:
        return prepared_list

    all_embeddings = embed(all_chunks, sleep_interval=sleep_interval, verbose=verbose)

    for ref_idx, (file_idx, chunk_idx) in enumerate(chunk_refs):
        p = prepared_list[file_idx]
        if "embeddings" not in p:
            p["embeddings"] = [None] * len(p["enriched_chunks"])
        p["embeddings"][chunk_idx] = all_embeddings[ref_idx]

    return prepared_list


def _prepare_file(file_path, chunk_size=DEFAULT_CHUNK_SIZE,
                  chunk_overlap=DEFAULT_CHUNK_OVERLAP,
                  sleep_interval=0.0):
    """阶段 1：读取 + 切分 + Embedding（无 DB 操作，可并行）。

    保持兼容性：内部调用 prepare_file_no_embed + embed。
    """
    prepared = prepare_file_no_embed(file_path, chunk_size, chunk_overlap)
    if not prepared["ok"]:
        return prepared
    prepared["embeddings"] = embed(prepared["enriched_chunks"], sleep_interval=sleep_interval)
    return prepared


def check_file_cache(file_path, collection_name="default"):
    """检查文件是否已缓存且未修改。"""
    abs_path = _normalize_path(file_path)
    doc_id = hashlib.md5(abs_path.encode()).hexdigest()[:12]
    try:
        file_mtime = os.path.getmtime(file_path)
    except Exception:
        return False, None

    try:
        col = get_collection(collection_name)
        result = col.get(
            where={"doc_id": doc_id},
            include=["metadatas"]
        )
        if result and result["metadatas"]:
            stored_mtime = result["metadatas"][0].get("file_mtime")
            if stored_mtime is not None and abs(stored_mtime - file_mtime) < 1e-6:
                # 额外检查 raw 缓存文件是否真实存在于磁盘上
                file_ext = os.path.splitext(file_path)[1]
                raw_path = _raw_file_path(collection_name, doc_id, file_ext)
                if os.path.exists(raw_path):
                    return True, doc_id
    except Exception:
        pass
    return False, doc_id


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
    file_mtime = prepared.get("file_mtime")

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
            "file_mtime": file_mtime,
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


def _batch_write_to_db(prepared_list, collection_name,
                       results, errors, skipped,
                       on_progress, verbose, total_file_count):
    """批量写入 ChromaDB（delete_first=True 专用，跳过逐文件查旧/删旧）。

    先缓存原始文件，收集所有 chunks，然后一次性 upsert 到 ChromaDB。
    相比逐文件 _write_to_db，减少了 N 次 col.get + N 次 col.delete 的 SQLite 开销。
    """
    col = get_collection(collection_name)
    all_ids = []
    all_documents = []
    all_embeddings = []
    all_metadatas = []

    for i, p in enumerate(prepared_list):
        fp = p.get("_fp", "?")
        if not p.get("ok"):
            if p.get("skipped"):
                skipped.append(p.get("reason", ""))
            elif p.get("error"):
                errors.append(p.get("error", "unknown error"))
            continue

        try:
            _cache_raw_file(p["text"], collection_name, p["doc_id"], p["file_ext"])
        except Exception as e:
            errors.append(f"{p['filename']}: cache_raw_file failed: {e}")
            continue

        doc_id = p["doc_id"]
        enriched_chunks = p["enriched_chunks"]
        embeddings = p["embeddings"]
        line_ranges = p["line_ranges"]
        scopes = p["scopes"]
        file_mtime = p.get("file_mtime")

        for ci in range(len(enriched_chunks)):
            all_ids.append(f"{doc_id}_c{ci}")
            all_documents.append(enriched_chunks[ci])
            all_embeddings.append(embeddings[ci])
            all_metadatas.append({
                "source": p["abs_path"],
                "filename": p["filename"],
                "doc_id": doc_id,
                "chunk_index": ci,
                "total_chunks": len(enriched_chunks),
                "line_start": line_ranges[ci][0],
                "line_end": line_ranges[ci][1],
                "scope": scopes[ci],
                "file_mtime": file_mtime,
            })

        r = {"ok": True, "filename": p["filename"],
             "chars": p["chars"], "chunks": p["chunks"], "doc_id": doc_id}
        results.append(r)

        if on_progress:
            on_progress(i + 1, total_file_count, fp, r)
        elif verbose:
            print(f"  [prepare-write {i + 1:>4}/{len(prepared_list)}] {p['filename']} ({p['chunks']} chunks)")

    if not all_ids:
        return

    if verbose:
        print(f"\n[rag] Batch upsert {len(all_ids)} chunks to ChromaDB...")

    for start in range(0, len(all_ids), CHROMA_UPSERT_BATCH):
        end = start + CHROMA_UPSERT_BATCH
        col.upsert(
            ids=all_ids[start:end],
            documents=all_documents[start:end],
            embeddings=all_embeddings[start:end],
            metadatas=all_metadatas[start:end],
        )
        if verbose:
            print(f"  [batch-upsert] {min(end, len(all_ids))}/{len(all_ids)} chunks written")


def ingest_file(file_path, collection_name="default",
                chunk_size=DEFAULT_CHUNK_SIZE,
                chunk_overlap=DEFAULT_CHUNK_OVERLAP,
                sleep_interval=0.0,
                use_cache=True,
                verbose=False):
    """导入单个文件到知识库，返回结果 dict（串行版本，兼容旧调用）。"""
    if use_cache:
        is_cached, _ = check_file_cache(file_path, collection_name)
        if is_cached:
            abs_path = _normalize_path(file_path)
            doc_id = hashlib.md5(abs_path.encode()).hexdigest()[:12]
            if verbose:
                name = os.path.basename(file_path)
                print(f"  [cache] {name} (skipped, unchanged)")
            return {
                "ok": True,
                "filename": os.path.basename(file_path),
                "chars": 0,
                "chunks": 0,
                "doc_id": doc_id,
                "_cached": True,
            }
    prepared = _prepare_file(file_path, chunk_size, chunk_overlap, sleep_interval=sleep_interval)
    if not prepared["ok"]:
        return prepared
    result = _write_to_db(prepared, collection_name)
    if result["ok"]:
        _bm25_cache.pop(collection_name, None)
        _symbol_cache.pop(collection_name, None)
    return result


def ingest_path(path, collection_name="default",
                chunk_size=DEFAULT_CHUNK_SIZE,
                chunk_overlap=DEFAULT_CHUNK_OVERLAP,
                file_extensions=None,
                sleep_interval=0.0,
                use_cache=True,
                verbose=False):
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
            r = ingest_file(fp, collection_name, chunk_size, chunk_overlap, sleep_interval=sleep_interval, use_cache=use_cache, verbose=verbose)
        except Exception as e:
            r = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}"}
        if r["ok"]:
            if not r.get("_cached"):
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
                 verbose=False, max_workers=1,
                 sleep_interval=0.01,
                 use_cache=True,
                 ):
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
        delete_first: 是否先清空旧数据再导入（适用于全量重建）。优先级高于 use_cache。
        on_progress: 可选回调 fn(current, total, file_path, result)，用于自定义进度展示。
        verbose: 是否打印详细日志。
        max_workers: Embedding 并发线程数。
                     1 = 串行（默认，兼容旧行为）；
                     2-4 = 并行读取+Embedding，串行写入 ChromaDB。
                     不建议超过 4，避免触发 Embedding API 频率限制。
        use_cache: 是否启用文件缓存检查（基于 mtime）。默认 True，未修改的文件会被跳过。
    """
    import time as _time
    from concurrent.futures import ThreadPoolExecutor, as_completed

    if isinstance(paths, str):
        paths = [paths]

    t0 = _time.time()

    if delete_first:
        deleted_col = False
        raw_files_deleted = False
        try:
            delete_collection(collection_name)
            deleted_col = True
        except Exception:
            pass
        try:
            _delete_raw_files_collection(collection_name)
            raw_files_deleted = True
        except Exception:
            pass
        if verbose:
            print(f"[rag] Deleted old collection: {collection_name}"
                  f" (collection={'ok' if deleted_col else 'not found'}, raw_files={'ok' if raw_files_deleted else 'not found'})")

    all_files = []
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.exists(p):
            found = collect_files(p, file_extensions=file_extensions)
            if verbose:
                ext_info = f" (filter: {file_extensions})" if file_extensions else ""
                print(f"[rag] {p} -> {len(found)} files{ext_info}")
            all_files.extend(found)

    # 缓存检查
    files_to_process = []
    cached_count = 0
    if use_cache and not delete_first:
        for fp in all_files:
            is_cached, _ = check_file_cache(fp, collection_name)
            if is_cached:
                cached_count += 1
                if verbose:
                    name = os.path.basename(fp)
                    print(f"  [cache] {name} (skipped, unchanged)")
            else:
                files_to_process.append(fp)
    else:
        files_to_process = all_files

    if verbose:
        mode_str = f"parallel(workers={max_workers})" if max_workers > 1 else "sequential"
        cache_note = f", cache: {cached_count} skipped" if cached_count > 0 else ""
        print(f"[rag] Total {len(all_files)} files ({len(files_to_process)} to process{cache_note}), mode: {mode_str}, starting...\n")

    results = []
    errors = []
    skipped = []
    total_chars = 0
    total_chunks = 0
    large_files = []

    for fp in files_to_process:
        file_size = os.path.getsize(fp)
        if file_size > 100 * 1024:
            large_files.append((fp, file_size))
            if verbose:
                print(f"  [large] {fp} ({file_size / 1024:.1f} KB)")

    if max_workers <= 1:
        prepared_list = []
        for i, fp in enumerate(files_to_process):
            try:
                p = prepare_file_no_embed(fp, chunk_size, chunk_overlap)
            except Exception as e:
                p = {"ok": False, "error": f"{os.path.basename(fp)}: {type(e).__name__}: {e}", "_fp": fp}
            p["_fp"] = fp
            p["_idx"] = i
            prepared_list.append(p)
            if verbose:
                name = os.path.basename(fp)
                if p["ok"]:
                    print(f"  [prepare {i + 1:>4}/{len(files_to_process)}] {name} ({p['chunks']} chunks)")
                elif p.get("skipped"):
                    print(f"  [prepare {i + 1:>4}/{len(files_to_process)}] - {name}  (skipped)")
    else:
        prepared_list = [None] * len(files_to_process)
        done_count = 0
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            future_to_idx = {}
            for i, fp in enumerate(files_to_process):
                fut = pool.submit(prepare_file_no_embed, fp, chunk_size, chunk_overlap)
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
                        print(f"  [prepare {done_count:>4}/{len(files_to_process)}] {name} ({p['chunks']} chunks)")
                    elif p.get("skipped"):
                        print(f"  [prepare {done_count:>4}/{len(files_to_process)}] - {name}  (skipped)")

    if verbose and files_to_process:
        prepare_elapsed = _time.time() - t0
        total_chunks_to_embed = sum(p["chunks"] for p in prepared_list if p.get("ok"))
        print(f"\n[rag] Prepare done in {prepare_elapsed:.1f}s, batch embedding {total_chunks_to_embed} chunks...\n")

    if files_to_process:
        prepared_list = batch_embed_prepared(prepared_list, sleep_interval=sleep_interval, verbose=verbose)

        if verbose:
            embed_elapsed = _time.time() - t0
            print(f"\n[rag] Embedding done in {embed_elapsed:.1f}s, writing to ChromaDB...\n")

        if delete_first:
            _batch_write_to_db(
                prepared_list, collection_name,
                results, errors, skipped,
                on_progress, verbose, len(all_files),
            )
            total_chars = sum(r["chars"] for r in results)
            total_chunks = sum(r["chunks"] for r in results)
        else:
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
    else:
        # 没有文件需要处理，直接返回成功
        if verbose:
            print("\n[rag] No files to process (all cached).\n")

    # ── 构建 BM25 索引 ──
    if results:
        if verbose:
            print("\n[rag] Building BM25 index...")
        try:
            col = get_collection(collection_name)
            all_data = _batch_get(col, include=["documents"])
            build_bm25_index(collection_name, all_data["documents"], all_data["ids"])
            if verbose:
                print(f"[rag] BM25 index built ({len(all_data['ids'])} chunks)")
        except Exception as e:
            if verbose:
                print(f"[rag] BM25 index build failed (non-fatal): {e}")

    # ── 构建 Symbol 索引 ──
    if results:
        if verbose:
            print("[rag] Building Symbol index...")
        try:
            sym_index = build_symbol_index(collection_name)
            if verbose:
                sym_count = sum(len(v) for v in (sym_index or {}).values())
                print(f"[rag] Symbol index built ({sym_count} symbols)")
        except Exception as e:
            if verbose:
                print(f"[rag] Symbol index build failed (non-fatal): {e}")

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
           use_bm25=True, filter_filename=None):
    """混合检索：Vector + BM25 → RRF 融合 → Reranker 精排。

    返回 (documents, metadatas, distances, rerank_used, total, rerank_scores)。
    rerank_scores: Reranker 的真实相关性分数列表（未 rerank 时为空列表）。
    """
    col = _get_existing_collection(collection_name)
    if col is None:
        return [], [], [], False, 0, []
    total = col.count()

    if total == 0:
        return [], [], [], False, 0, []

    # ── Vector Search ──
    query_vec = embed([query])[0]
    recall_k = min(top_k * 4, total) if (use_rerank or use_bm25) else min(top_k, total)

    where_filter = {"filename": filter_filename} if filter_filename else None
    vec_results = col.query(
        query_embeddings=[query_vec],
        n_results=recall_k,
        where=where_filter,
        include=["documents", "metadatas", "distances"],
    )
    vec_ids = vec_results["ids"][0]
    vec_docs = vec_results["documents"][0]
    vec_metas = vec_results["metadatas"][0]
    vec_dists = vec_results["distances"][0]

    # ── BM25 + RRF ──
    if use_bm25 and not filter_filename:
        bm25_ids, _ = _bm25_search(query, collection_name, recall_k)
        if bm25_ids:
            fused_ids = _rrf_fusion(vec_ids, bm25_ids)

            id_to_data = {vid: (vec_docs[i], vec_metas[i], vec_dists[i])
                          for i, vid in enumerate(vec_ids)}

            bm25_only = [bid for bid in fused_ids if bid not in id_to_data]
            if bm25_only:
                max_vec_dist = max(vec_dists) if vec_dists else 1.0
                try:
                    extra = _batch_get(col, ids=bm25_only, include=["documents", "metadatas"])
                    for i, eid in enumerate(extra["ids"]):
                        id_to_data[eid] = (extra["documents"][i], extra["metadatas"][i], max_vec_dist)
                except Exception:
                    pass

            documents = [id_to_data[cid][0] for cid in fused_ids if cid in id_to_data]
            metadatas = [id_to_data[cid][1] for cid in fused_ids if cid in id_to_data]
            distances = [id_to_data[cid][2] for cid in fused_ids if cid in id_to_data]
        else:
            documents, metadatas, distances = vec_docs, vec_metas, vec_dists
    else:
        documents, metadatas, distances = vec_docs, vec_metas, vec_dists

    # ── Reranker ──
    cfg = _cfg()
    rerank_used = False
    rerank_scores = []
    if use_rerank and cfg.rerank.model and len(documents) > top_k:
        try:
            reranked_idx, rerank_scores = rerank(query, documents, top_n=top_k)
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

    return documents, metadatas, distances, rerank_used, total, rerank_scores


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
        #检查 collection 是否存在且有数据，但 raw cache 缺失
        try:
            col = _get_existing_collection(collection_name)
            if col is not None and col.count() > 0:
                return [{"error": "raw_cache_missing",
                         "message": f"Raw cache not found for collection '{collection_name}'. "
                                    f"ChromaDB has {col.count()} chunks but no raw files. "
                                    f"Please re-import with nbrag_add_document to rebuild raw cache."}]
        except Exception:
            pass
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
    """在知识库中查找符号（类/函数/方法）的完整定义。

    优先使用预构建的 Symbol 索引（O(1) 查表 + 仅读取匹配文件），
    索引不存在时回退到全量 AST 扫描（兼容旧数据）。
    """
    import re

    raw_dir = os.path.join(_raw_files_dir(), collection_name)
    if not os.path.isdir(raw_dir):
        try:
            col = _get_existing_collection(collection_name)
            if col is not None and col.count() > 0:
                return [{"error": "raw_cache_missing",
                         "message": f"Raw cache not found for collection '{collection_name}'. "
                                    f"ChromaDB has {col.count()} chunks but no raw files. "
                                    f"Please re-import with nbrag_add_document to rebuild raw cache."}]
        except Exception:
            pass
        return []

    index = _load_symbol_index(collection_name)
    if index is not None:
        return _find_definition_via_index(symbol, collection_name, index, raw_dir, max_results)

    return _find_definition_full_scan(symbol, collection_name, raw_dir, max_results)


def _find_definition_via_index(symbol, collection_name, index, raw_dir, max_results):
    """通过 Symbol 索引查找定义（快速路径）。"""
    import re
    entries = _query_symbol_index(symbol, index)
    results = []

    for entry in entries[:max_results]:
        doc_id = entry["doc_id"]
        ext_candidates = [".py"]
        content = None
        for ext in ext_candidates:
            rpath = _raw_file_path(collection_name, doc_id, ext)
            if os.path.isfile(rpath):
                try:
                    with open(rpath, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                except OSError:
                    pass
                break
        if content is None:
            content_from_raw, _ = _read_raw_file(collection_name, doc_id)
            content = content_from_raw

        if content is None:
            definition = f"(source file not found, doc_id={doc_id})"
        else:
            file_lines = content.splitlines()
            ls, le = entry["line_start"], entry["line_end"]
            definition = "\n".join(file_lines[ls - 1:le])

        methods_summary = ""
        if entry.get("methods"):
            methods_summary = "\n".join(f"  {s}" for s in entry["methods"])

        results.append({
            "filename": entry["filename"],
            "source": entry["source"],
            "doc_id": doc_id,
            "symbol_type": entry["type"],
            "qualified_name": entry["qualified"],
            "line_start": entry["line_start"],
            "line_end": entry["line_end"],
            "definition": definition,
            "methods_summary": methods_summary,
        })

    if len(results) < max_results:
        doc_id_to_info = _get_doc_id_map(collection_name)
        all_files = os.listdir(raw_dir)
        other_files = [f for f in all_files if not f.lower().endswith(".py")]
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


def _find_definition_full_scan(symbol, collection_name, raw_dir, max_results):
    """全量 AST 扫描查找定义（回退路径，兼容无索引的旧数据）。"""
    import re
    import ast as _ast
    import warnings as _warnings

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


def list_documents(collection_name="default", offset=0, limit=None):
    """列出知识库中已导入的文档。支持 offset/limit 分页。"""
    col = _get_existing_collection(collection_name)
    if col is None:
        return {}
    total = col.count()
    if total == 0:
        return {}

    all_data = _batch_get(col, include=["metadatas"])
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

    # 按 doc_id 排序确保分页结果稳定
    sorted_items = sorted(docs.items(), key=lambda x: x[0])
    if offset:
        sorted_items = sorted_items[offset:]
    if limit is not None:
        sorted_items = sorted_items[:limit]
    return dict(sorted_items)


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
    invalidate_bm25_cache(collection_name)
    invalidate_symbol_cache(collection_name)
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
                all_meta = _batch_get(col, include=["metadatas"])
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
  Ingest file or directory into knowledge base (chunking + embedding + indexing). Auto-creates collection if not exists.
  Supports any text file: code, docs, law, articles, manuals, etc. Python files get extra class/function scope enrichment.
  Note: Typically called by users via scripts for batch ingestion, not by AI during conversations.
  `````

- `def nbrag_search(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Knowledge base name, i.e. 知识库名字 (use nbrag_stats to see available names)'), top_k: int = Field(default=5, description='Number of results to return'), use_rerank: bool = Field(default=True, description='Enable reranker for better accuracy (recommended)'), use_bm25: bool = Field(default=True, description='Enable BM25 keyword matching + RRF fusion (recommended for precise names)'), filter_filename: str = Field(default='', description="Filter by filename (e.g. 'core.py'). BM25 auto-disabled when set")) -> str` `mcp.tool()`
  - *Line: 74*
  - **Docstring:**
  `````
  Search knowledge base (知识库) for relevant content. Works for code, docs, law, articles, or any imported text.
  
  IMPORTANT: If you don't know the collection_name, call nbrag_stats() first to see all available knowledge bases.
  collection_name = knowledge base name = 知识库名字 (e.g. user says "查funboost知识库" → collection_name="funboost").
  
  **PREFER nbrag_search_and_fetch** when the user asks 'how to do X', 'show me examples of X',
  or any knowledge/usage question — it auto-fetches complete file context and avoids fragmented chunks.
  **Use nbrag_search** only when you need fine-grained control (disable BM25/rerank) or metadata-only lookup.
  
  TIP: Don't pass the user's raw long question directly. Rewrite it into focused search terms.
  e.g. user asks "试用期干了5个月不转正，1年合同合法吗" → query="试用期 最长期限 1年合同"
  Then do a second search: query="违法约定试用期 赔偿" to find penalty clauses.
  
  Result format: [1/5] filename chunk:X/Y line:N-M scope:xxx doc_id:xxx dist:0.1234 score:0.9876
  Key fields for follow-up: file_path (for nbrag_get_raw_file), doc_id + chunk_index (for nbrag_get_adjacent_chunks).
  
  After search, use these follow-up tools to dig deeper:
    - nbrag_grep(keyword, collection_name) → exact keyword/regex search (code names, legal terms, article numbers)
    - nbrag_find_definition(symbol, collection_name) → complete class/function definition (Python .py files ONLY)
    - nbrag_get_raw_file(file_path, collection_name) → full file content without chunk overlap
    - nbrag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result
  
  If first search misses, try different keywords or use nbrag_grep for exact term matching.
  `````

- `def nbrag_search_and_fetch(query: str = Field(description='Search query (natural language question or keywords)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), top_k: int = Field(default=5, description='Number of search results to return'), fetch_top_n_raw: int = Field(default=3, description='Auto-fetch raw source for top N results (0 to skip)'), context_lines: int = Field(default=100, description='Lines of context around matched chunk'), filter_filename: str = Field(default='', description="Filter by filename (e.g. 'core.py')")) -> str` `mcp.tool()`
  - *Line: 166*
  - **Docstring:**
  `````
  Search + auto-fetch raw file content for top results in one call (saves a round-trip).
  
  **PREFER this over nbrag_search** when:
  - User asks 'how to do X', 'show me examples of X', 'what is X usage', or any knowledge/usage question.
  - You need both a quick answer AND the full source code backing it.
  - You want to avoid fragmented chunks and get complete file context immediately.
  
  **Use nbrag_search** only when:
  - You need fine-grained control (disable BM25, different chunk counts).
  - You only want metadata/summary, not full source.
  
  Always uses BM25+rerank for best quality.
  Same doc_id in multiple results is fetched only once with merged line range.
  `````

- `def nbrag_grep(keyword: str = Field(description="Keyword or regex (e.g. 'UserService', '侵权责任', 'Article 42', 'MAX_RETRIES')"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), max_results: int = Field(default=10, description='Maximum number of matches to return'), case_sensitive: bool = Field(default=False, description='Case-sensitive matching'), filter_filename: str = Field(default='', description="Filter by filename (e.g. 'booster.py')"), context_lines: int = Field(default=10, description='Context lines before/after each match (use 20+ for class headers)')) -> str` `mcp.tool()`
  - *Line: 292*
  - **Docstring:**
  `````
  Keyword/regex exact search in cached raw files. Complements nbrag_search (semantic search).
  
  Use cases where nbrag_search falls short:
    - Code: class/function names ('UserService'), constants ('MAX_RETRIES'), imports ('from myproject')
    - Law/docs: article numbers ('第四十二条'), exact legal terms ('侵权责任'), section titles
    - General: specific dates, proper nouns, technical terms, exact phrases
  
  Tip: use context_lines=15 to see surrounding context around the match.
  Typical workflow: nbrag_search (find direction) → nbrag_grep (pinpoint exact terms) → nbrag_get_raw_file (full context)
  `````

- `def nbrag_find_definition(symbol: str = Field(description="Symbol name (e.g. 'UserService', 'get_by_id', 'MyClass.__init__')"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), max_results: int = Field(default=5, description='Maximum number of definitions to return')) -> str` `mcp.tool()`
  - *Line: 331*
  - **Docstring:**
  `````
  Find complete class/function/method definition by symbol name.
  Python .py files: AST parsing for exact boundaries + methods summary. Non-Python: regex fallback (limited).
  IMPORTANT: Only works on imported .py files. Code snippets inside .md/.txt docs cannot be AST-parsed.
  For non-.py content, use nbrag_grep to search for keywords instead.
  `````

- `def nbrag_get_file_chunks(file_path: str = Field(description='Full path or filename (from nbrag_search results)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), start_chunk: int = Field(default=0, description='Start chunk index (0-based) for pagination'), max_chunks: int = Field(default=10, description='Max chunks to return')) -> str` `mcp.tool()`
  - *Line: 371*
  - **Docstring:**
  `````
  Paginated view of file chunks with scope and line metadata.
  Note: chunks have overlap. For clean source code without overlap, use nbrag_get_raw_file instead.
  `````

- `def nbrag_get_raw_file(file_path: str = Field(description='Full path or filename (from nbrag_search results)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), line_start: int = Field(default=-1, description='Start line (1-based), -1 for beginning'), line_end: int = Field(default=-1, description='End line (inclusive), -1 for end of file')) -> str` `mcp.tool()`
  - *Line: 391*
  - **Docstring:**
  `````
  Get cached raw file content without chunk overlap. Recommended for viewing full source code.
  Supports line_start/line_end for extracting specific line ranges.
  Only available for files imported with raw cache (re-import older files if needed).
  `````

- `def nbrag_get_adjacent_chunks(doc_id: str = Field(description='Document ID (from nbrag_search/nbrag_grep results)'), chunk_index: int = Field(description="Target chunk index (the X from 'chunk:X/Y' in results)"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), window: int = Field(default=3, description='Returns chunk_index ± window chunks')) -> str` `mcp.tool()`
  - *Line: 459*
  - **Docstring:**
  `````
  Get adjacent chunks around a specific chunk index, for expanding context of a search result.
  Requires doc_id and chunk_index from nbrag_search results (not file_path).
  Example: doc_id="abc123", chunk_index=3, window=2 → returns chunks 1-5
  `````

- `def nbrag_get_chunks_by_lines(doc_id: str = Field(description='Document ID (from nbrag_search/nbrag_grep results)'), line_start: int = Field(description="Start line (1-based, from 'line:N-M' in results)"), line_end: int = Field(description="End line (inclusive, from 'line:N-M' in results)"), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)')) -> str` `mcp.tool()`
  - *Line: 476*
  - **Docstring:**
  `````
  Get all chunks covering a line range, with scope metadata.
  vs nbrag_get_raw_file: this returns chunks (with scope but has overlap),
  nbrag_get_raw_file returns raw code (no overlap but no scope).
  Example: doc_id="abc123", line_start=80, line_end=200
  `````

- `def nbrag_list(collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)'), limit: int = Field(default=100, description='Max docs to return (default 100, max 500)'), offset: int = Field(default=0, description='Skip first N docs (default 0). Use with limit for pagination')) -> str` `mcp.tool()`
  - *Line: 519*
  - **Docstring:**
  `````
  List documents in a knowledge base (filename, path, chunk count, doc_id).
  Returns paginated results by default (limit=100). Use offset for next page.
  Use returned doc_id with nbrag_delete to remove documents.
  `````

- `def nbrag_delete(doc_id: str = Field(description='Document ID to delete (from nbrag_list results)'), collection_name: str = Field(description='Knowledge base name (use nbrag_stats to see available names)')) -> str` `mcp.tool()`
  - *Line: 555*
  - *Delete a document's vectors and cached files from the collection. Get doc_id from nbrag_list.*

- `def nbrag_stats() -> str` `mcp.tool()`
  - *Line: 569*
  - **Docstring:**
  `````
  Get all available knowledge bases (知识库) and their stats. CALL THIS FIRST if you don't know the collection_name.
  Returns: all collection names, doc count, chunk count, embedding/rerank model, storage path.
  Glossary: collection_name = knowledge base name = 知识库名字 (e.g. "funboost", "law_docs").
  After getting collection names, use nbrag_search to search within a specific knowledge base.
  `````

- `def main()`
  - *Line: 600*
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
    """Ingest file or directory into knowledge base (chunking + embedding + indexing). Auto-creates collection if not exists.
    Supports any text file: code, docs, law, articles, manuals, etc. Python files get extra class/function scope enrichment.
    Note: Typically called by users via scripts for batch ingestion, not by AI during conversations."""
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
    collection_name: str = Field(description="Knowledge base name, i.e. 知识库名字 (use nbrag_stats to see available names)"),
    top_k: int = Field(default=5, description="Number of results to return"),
    use_rerank: bool = Field(default=True, description="Enable reranker for better accuracy (recommended)"),
    use_bm25: bool = Field(default=True, description="Enable BM25 keyword matching + RRF fusion (recommended for precise names)"),
    filter_filename: str = Field(default="", description="Filter by filename (e.g. 'core.py'). BM25 auto-disabled when set"),
) -> str:
    """Search knowledge base (知识库) for relevant content. Works for code, docs, law, articles, or any imported text.

    IMPORTANT: If you don't know the collection_name, call nbrag_stats() first to see all available knowledge bases.
    collection_name = knowledge base name = 知识库名字 (e.g. user says "查funboost知识库" → collection_name="funboost").

    **PREFER nbrag_search_and_fetch** when the user asks 'how to do X', 'show me examples of X',
    or any knowledge/usage question — it auto-fetches complete file context and avoids fragmented chunks.
    **Use nbrag_search** only when you need fine-grained control (disable BM25/rerank) or metadata-only lookup.

    TIP: Don't pass the user's raw long question directly. Rewrite it into focused search terms.
    e.g. user asks "试用期干了5个月不转正，1年合同合法吗" → query="试用期 最长期限 1年合同"
    Then do a second search: query="违法约定试用期 赔偿" to find penalty clauses.

    Result format: [1/5] filename chunk:X/Y line:N-M scope:xxx doc_id:xxx dist:0.1234 score:0.9876
    Key fields for follow-up: file_path (for nbrag_get_raw_file), doc_id + chunk_index (for nbrag_get_adjacent_chunks).

    After search, use these follow-up tools to dig deeper:
      - nbrag_grep(keyword, collection_name) → exact keyword/regex search (code names, legal terms, article numbers)
      - nbrag_find_definition(symbol, collection_name) → complete class/function definition (Python .py files ONLY)
      - nbrag_get_raw_file(file_path, collection_name) → full file content without chunk overlap
      - nbrag_get_adjacent_chunks(doc_id, chunk_index, collection_name) → expand context around a result

    If first search misses, try different keywords or use nbrag_grep for exact term matching."""
    cfg = get_config()
    fname_filter = filter_filename if filter_filename else None
    documents, metadatas, distances, rerank_used, total, rerank_scores = search(
        query, collection_name, top_k, use_rerank,
        use_bm25=use_bm25,
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
    bm25_str = "on" if (use_bm25 and not fname_filter) else "off"
    header = f"[{collection_name}] {total} chunks | hybrid(bm25+vector): {bm25_str} | rerank: {rerank_str}"
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
        if rerank_scores and i < len(rerank_scores):
            meta_parts.append(f"score:{rerank_scores[i]:.4f}")

        lines.append(f"[{i + 1}/{len(documents)}] {meta.get('filename', '?')} {' '.join(meta_parts)}")
        lines.append(f"file_path: {src}")
        preview = doc[:preview_limit] + ("..." if len(doc) > preview_limit else "")
        lines.append(preview)
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_search_and_fetch(
    query: str = Field(description="Search query (natural language question or keywords)"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
    top_k: int = Field(default=5, description="Number of search results to return"),
    fetch_top_n_raw: int = Field(default=3, description="Auto-fetch raw source for top N results (0 to skip)"),
    context_lines: int = Field(default=100, description="Lines of context around matched chunk"),
    filter_filename: str = Field(default="", description="Filter by filename (e.g. 'core.py')"),
) -> str:
    """Search + auto-fetch raw file content for top results in one call (saves a round-trip).

    **PREFER this over nbrag_search** when:
    - User asks 'how to do X', 'show me examples of X', 'what is X usage', or any knowledge/usage question.
    - You need both a quick answer AND the full source code backing it.
    - You want to avoid fragmented chunks and get complete file context immediately.

    **Use nbrag_search** only when:
    - You need fine-grained control (disable BM25, different chunk counts).
    - You only want metadata/summary, not full source.

    Always uses BM25+rerank for best quality.
    Same doc_id in multiple results is fetched only once with merged line range."""
    cfg = get_config()
    fname_filter = filter_filename if filter_filename else None
    documents, metadatas, distances, rerank_used, total, rerank_scores = search(
        query, collection_name, top_k, True, use_bm25=True, filter_filename=fname_filter,
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
        if rerank_scores and i < len(rerank_scores):
            meta_parts.append(f"score:{rerank_scores[i]:.4f}")

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
    keyword: str = Field(description="Keyword or regex (e.g. 'UserService', '侵权责任', 'Article 42', 'MAX_RETRIES')"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
    max_results: int = Field(default=10, description="Maximum number of matches to return"),
    case_sensitive: bool = Field(default=False, description="Case-sensitive matching"),
    filter_filename: str = Field(default="", description="Filter by filename (e.g. 'booster.py')"),
    context_lines: int = Field(default=10, description="Context lines before/after each match (use 20+ for class headers)"),
) -> str:
    """Keyword/regex exact search in cached raw files. Complements nbrag_search (semantic search).

    Use cases where nbrag_search falls short:
      - Code: class/function names ('UserService'), constants ('MAX_RETRIES'), imports ('from myproject')
      - Law/docs: article numbers ('第四十二条'), exact legal terms ('侵权责任'), section titles
      - General: specific dates, proper nouns, technical terms, exact phrases

    Tip: use context_lines=15 to see surrounding context around the match.
    Typical workflow: nbrag_search (find direction) → nbrag_grep (pinpoint exact terms) → nbrag_get_raw_file (full context)"""
    fname_filter = filter_filename if filter_filename else None
    results = grep_knowledge(
        keyword, collection_name, max_results, case_sensitive,
        filter_filename=fname_filter, context_lines=context_lines,
    )

    if not results:
        return f"No matches for '{keyword}' (collection: {collection_name})"
    if len(results) == 1 and isinstance(results[0], dict) and results[0].get("error") == "raw_cache_missing":
        return results[0]["message"]

    lines = [f"grep: '{keyword}' | collection_name: {collection_name} | {len(results)} match(es)", ""]
    for i, r in enumerate(results):
        lines.append(f"[{i + 1}/{len(results)}] {r['filename']} line:{r['line_number']} doc_id:{r['doc_id']}")
        lines.append(f"file_path: {r['source']}")
        lines.append(r["context"])
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def nbrag_find_definition(
    symbol: str = Field(description="Symbol name (e.g. 'UserService', 'get_by_id', 'MyClass.__init__')"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
    max_results: int = Field(default=5, description="Maximum number of definitions to return"),
) -> str:
    """Find complete class/function/method definition by symbol name.
    Python .py files: AST parsing for exact boundaries + methods summary. Non-Python: regex fallback (limited).
    IMPORTANT: Only works on imported .py files. Code snippets inside .md/.txt docs cannot be AST-parsed.
    For non-.py content, use nbrag_grep to search for keywords instead."""
    results = find_symbol_definition(symbol, collection_name, max_results)

    if not results:
        return f"No definition found for '{symbol}' (collection: {collection_name}). Try nbrag_grep for a broader search."
    if len(results) == 1 and isinstance(results[0], dict) and results[0].get("error") == "raw_cache_missing":
        return results[0]["message"]

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
    file_path: str = Field(description="Full path or filename (from nbrag_search results)"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
    start_chunk: int = Field(default=0, description="Start chunk index (0-based) for pagination"),
    max_chunks: int = Field(default=10, description="Max chunks to return"),
) -> str:
    """Paginated view of file chunks with scope and line metadata.
    Note: chunks have overlap. For clean source code without overlap, use nbrag_get_raw_file instead."""
    result = get_file_chunks(
        file_path, collection_name, start_chunk, max_chunks,
        raw=False,
    )

    if not result.get("found"):
        return result.get("error", f"File not found: '{file_path}'")

    return _format_chunks_result(result)


@mcp.tool()
def nbrag_get_raw_file(
    file_path: str = Field(description="Full path or filename (from nbrag_search results)"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
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
    doc_id: str = Field(description="Document ID (from nbrag_search/nbrag_grep results)"),
    chunk_index: int = Field(description="Target chunk index (the X from 'chunk:X/Y' in results)"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
    window: int = Field(default=3, description="Returns chunk_index ± window chunks"),
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
    doc_id: str = Field(description="Document ID (from nbrag_search/nbrag_grep results)"),
    line_start: int = Field(description="Start line (1-based, from 'line:N-M' in results)"),
    line_end: int = Field(description="End line (inclusive, from 'line:N-M' in results)"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
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
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
    limit: int = Field(default=100, description="Max docs to return (default 100, max 500)"),
    offset: int = Field(default=0, description="Skip first N docs (default 0). Use with limit for pagination"),
) -> str:
    """List documents in a knowledge base (filename, path, chunk count, doc_id).
    Returns paginated results by default (limit=100). Use offset for next page.
    Use returned doc_id with nbrag_delete to remove documents."""
    limit = max(1, min(limit, 500))
    docs = list_documents(collection_name, offset=offset, limit=limit)

    if not docs:
        if offset > 0:
            return f"collection '{collection_name}': no more docs after offset {offset}."
        return f"collection '{collection_name}' is empty."

    # 从 stats 获取总文档数（已缓存计数）
    all_stats = get_stats()
    total_docs = all_stats["collections"].get(collection_name, {}).get("doc_count", 0)
    total_chunks = sum(info["chunk_count"] for info in docs.values())
    shown = len(docs)
    has_more = offset + shown < total_docs

    header = (f"[{collection_name}] {total_docs} total docs, showing {offset + 1}-{offset + shown}"
              f" | {total_chunks} chunks in current page")
    if has_more:
        header += (f"\n  (more available: use offset={offset + limit} for next page, "
                   f"{total_docs - offset - shown} remaining)")
    lines = [header + "\n"]
    for did, info in docs.items():
        lines.append(f"  {info['filename']} | file_path: {info['source']} | {info['chunk_count']} chunks | doc_id:{did}")

    return "\n".join(lines)


@mcp.tool()
def nbrag_delete(
    doc_id: str = Field(description="Document ID to delete (from nbrag_list results)"),
    collection_name: str = Field(description="Knowledge base name (use nbrag_stats to see available names)"),
) -> str:
    """Delete a document's vectors and cached files from the collection. Get doc_id from nbrag_list."""
    deleted, filename = delete_document(doc_id, collection_name)

    if deleted == 0:
        return f"Error: doc_id '{doc_id}' not found. Use nbrag_list to see available doc_ids."

    return f"Deleted: {filename} | {deleted} chunks | doc_id:{doc_id}"


@mcp.tool()
def nbrag_stats() -> str:
    """Get all available knowledge bases (知识库) and their stats. CALL THIS FIRST if you don't know the collection_name.
    Returns: all collection names, doc count, chunk count, embedding/rerank model, storage path.
    Glossary: collection_name = knowledge base name = 知识库名字 (e.g. "funboost", "law_docs").
    After getting collection names, use nbrag_search to search within a specific knowledge base."""
    cfg = get_config()
    stats = get_stats()

    lines = [
        "RAG Stats",
        f"embed: {stats['embedding_model']} | rerank: {stats['rerank_model']}",
        f"data_dir: {stats['data_dir']}",
        f"chunk: size={cfg.chunking.chunk_size} overlap={cfg.chunking.chunk_overlap} (current config) | collections: {stats['collection_count']}",
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

__version__ = "0.6.0"

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
version: "1.2.0"
description: >-
  当用户的问题涉及已导入 nbrag 知识库的内容时使用此 Skill。
  前提：相关知识必须已经通过 nbrag_add_document 导入并向量化，先用 nbrag_stats 确认知识库存在。
  通过多轮检索基于真实内容回答，避免幻觉。适用于代码、文档、法律、历史等任何已导入的知识领域。
  触发词：知识库、搜索、查定义、某某库怎么用、查法条、查询已导入的内容。
---

# nbrag 知识库检索工作流

nbrag 提供 12 个 MCP 工具，核心分三类：**发现 → 检索 → 深入**。

> **注意**：本文档中的函数名是 nbrag MCP 自身的函数名。当 nbrag 被接入其他 Agent 框架时，
> 函数名会带前缀（如变成 mcp__xxx__nbrag_search），AI 应以实际接收到的 function 名称为准。

## 快速决策：用哪个工具？

**核心原则：默认用 `nbrag_search_and_fetch`，它是打包好的最佳实践，省 token、省 round-trip。**

| 用户问的是什么 | 工具 | 备注 |
|---|---|---|
| 知识/用法/示例问题（"create_agent怎么用" / "离婚财产怎么分"） | **`nbrag_search_and_fetch`** | 默认首选，一步到位 |
| 需要精细控制（禁用 BM25、指定 chunk 数、按文件名过滤） | `nbrag_search` | 仅高级场景 |
| 精确符号名（"UserService 在哪定义"） | `nbrag_find_definition` | Python .py 最佳，非 .py 回退 regex |
| 精确字符串/术语/条文编号（"ThreadPool" / "第一千零七十七条"） | `nbrag_grep` | 正则匹配，返回上下文 |

**搜索上限**：10 轮不同策略和关键词都没找到 → 告知用户"知识库中可能没有相关内容"，不要无限重试。

## 文件类型与功能支持

| 导入类型 | `nbrag_search` | `nbrag_grep` | `nbrag_find_definition` | AST scope |
|---|---|---|---|---|
| `.py` 源码 | ✅ | ✅ | ✅ AST 精确解析 | ✅ |
| `.md` / `.txt` 等 | ✅ | ✅ | ⚠️ regex 回退 | ❌ |

## 检索策略

### 策略 A（默认首选）：一站式检索

```
nbrag_search_and_fetch(query="...", collection_name="xxx")
```

- 语义搜索 + 自动抓取匹配文件的原文，**一次调用获得完整上下文，避免碎片化 chunk**
- 小文件抓全文，大文件抓匹配位置附近 N 行（默认 ±100 行）
- `fetch_top_n_raw=3` 控制抓几个文件原文（设 0 跳过抓取）
- 同一文件多次命中只抓一次（合并行范围）
- 结果格式：`[1/5] file_path dist:0.1234` → 搜索排名 → 原文内容
- 不支持 `filter_filename`

### 策略 B：精细搜索

```
nbrag_search(query="...", collection_name="xxx", top_k=5)
```

- Vector + BM25 → RRF 融合 → Rerank 精排
- 可选：`use_bm25=False`、`use_rerank=False`、`filter_filename="core.py"`（精确匹配文件名）
- 返回 chunk preview，可能被截断（加 `...`）
- 关键字段：`chunk:X/Y`、`line:N-M`、`scope`（仅 Python）、`doc_id`、`file_path`、`dist`
- **大多数场景用策略 A 就够了，策略 B 仅用于需要精细控制的场景**

### 策略 C：精确匹配

```
nbrag_grep(keyword="UserService", collection_name="xxx")
```

- 搜索 raw cache 文件的原始内容（非向量库），适合精确字符串
- `context_lines=10` 控制上下文（默认 10，匹配行前后各 N 行）
- 可选 `case_sensitive=True`、`filter_filename="core.py"`
- `>>>` 标记匹配行

### 策略 D：符号定义

```
nbrag_find_definition(symbol="get_by_id", collection_name="xxx")
```

- Python：AST 精确解析，返回 class/function 完整定义 + 方法签名列表
- 非 Python：regex 回退，每个文件最多 1 处匹配，约 24 行上下文
- `max_results=5`（默认）

## 深入：获取更多上下文

| 工具 | 场景 | 关键参数 |
|------|------|---------|
| `nbrag_get_raw_file` | 看完整文件（无 overlap） | `file_path`, `line_start`, `line_end` |
| `nbrag_get_adjacent_chunks` | 扩展搜索结果的上下文 | `doc_id`, `chunk_index`, `window=3` |
| `nbrag_get_chunks_by_lines` | 按行号取 chunk | `doc_id`, `line_start`, `line_end` |
| `nbrag_get_file_chunks` | 分页浏览（有 scope） | `file_path`, `start_chunk=0`, `max_chunks=10` |

## 推荐调用流程

```
nbrag_stats()                         # 1. 确定知识库名
    ↓
nbrag_search_and_fetch()              # 2. 默认首选（一步拿到搜索+原文）
    ↓                                #   如需精细控制：nbrag_search()
nbrag_grep() / nbrag_find_definition() # 3. 精确定位符号/术语
    ↓
nbrag_get_raw_file() / nbrag_get_adjacent_chunks()  # 4. 扩展上下文
    ↓
跨文件追踪：遇到未知符号 → 重复 2-4
```

## 多轮检索策略

**核心原则**：不要把用户问题原封不动丢给搜索，主动拆解改写。

**示例**：用户问 "公司让我试用期干了5个月不转正，签的1年合同，合法吗？"
- 第1轮: `nbrag_search_and_fetch("试用期 最长期限 1年合同")` → 找到试用期上限
- 第2轮: `nbrag_search_and_fetch("违法约定试用期 赔偿")` → 找到赔偿标准
- 第3轮: `nbrag_grep("第十九条")` → 精确定位法条原文

搜索不理想时的策略：换关键词 → 换工具（语义→grep）→ 缩小文件范围 → 跨 collection

## 常见问题速查

| 症状 | 原因 | 解决 |
|------|------|------|
| collection 不存在 | 未导入或名称错误 | `nbrag_stats()` 确认名称 |
| 搜索返回空 | 无匹配或 raw cache 缺失 | 换关键词 / 重导入 |
| `nbrag_grep` / `nbrag_find_definition` 静默无结果 | raw cache 缺失或无匹配 | 用 `nbrag_stats` 确认 |
| `nbrag_find_definition` 对 .md 无效 | AST 仅解析 .py | 改用 `nbrag_grep` |

**详细错误信息**：各工具的报错信息在 MCP 工具描述中已注明，AI 应根据返回的错误信息判断原因。

## 能力边界

- ❌ 只检索已导入内容，不生成新内容
- ❌ 不导入文档（由用户手动操作）
- ❌ 不修改文件，只读取和搜索
- ✅ 超出知识库范围的，如实告知

## AI 不需要调用的工具

- `nbrag_add_document` — 用户手动导入
- `nbrag_delete` — 用户手动操作
- `nbrag_list` — 除非用户明确要求列出文档
`````

--- **end of file: nbrag/skills/nbrag-workflow/SKILL.md** (project: nbrag) --- 

---

# markdown content namespace: nbrag scripts 


## nbrag File Tree (relative dir: `scripts`)


`````

└── scripts
    ├── ingest_ex1
    │   ├── ingest_civil_code.py
    │   └── prepare_civil_code.py
    ├── ingest_ex2_marriage_law
    │   ├── ingest_marriage_law.py
    │   └── prepare_marriage_law.py
    ├── ingest_ex3_worker_rights
    │   └── ingest_worker_rights.py
    ├── ingest_funboost.py
    ├── ingest_funboost_one_md.py
    ├── ingest_langchain_ai_codes_and_docs.py
    ├── ingest_langchain_ai_docs.py
    ├── ingest_project.py
    ├── inguest_licai
    │   └── ingest_licai.py
    ├── nb_log_config.py
    ├── query_langchain.py
    ├── start_http_rag_mcp.py
    ├── start_local_rag_mcp.py
    ├── test_find_def.py
    ├── test_raw_get.py
    └── trigger_bug.py

`````

---


## nbrag (relative dir: `scripts`)  Included Files (total: 18 files)


- `scripts/ingest_funboost.py`

- `scripts/ingest_funboost_one_md.py`

- `scripts/ingest_langchain_ai_codes_and_docs.py`

- `scripts/ingest_langchain_ai_docs.py`

- `scripts/ingest_project.py`

- `scripts/nb_log_config.py`

- `scripts/query_langchain.py`

- `scripts/start_http_rag_mcp.py`

- `scripts/start_local_rag_mcp.py`

- `scripts/test_find_def.py`

- `scripts/test_raw_get.py`

- `scripts/trigger_bug.py`

- `scripts/ingest_ex1/ingest_civil_code.py`

- `scripts/ingest_ex1/prepare_civil_code.py`

- `scripts/ingest_ex2_marriage_law/ingest_marriage_law.py`

- `scripts/ingest_ex2_marriage_law/prepare_marriage_law.py`

- `scripts/ingest_ex3_worker_rights/ingest_worker_rights.py`

- `scripts/inguest_licai/ingest_licai.py`


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
    max_workers = 1,
    delete_first=True,
    verbose=True,
    sleep_interval=0.1,
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
    max_workers = 1,
    delete_first=True,
    verbose=True,
    chunk_size=1500,
    chunk_overlap=200,
    sleep_interval=0.1, 
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
    max_workers = 1,
    delete_first=True,
    verbose=True,
    chunk_size=1000,
    chunk_overlap=200,
    sleep_interval=0.1, 
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


--- **start of file: scripts/nb_log_config.py** (project: nbrag) --- 

`````python
# coding=utf8
"""
This file nb_log_config.py is auto-generated into the root directory of the Python project (at sys.path[1]).
Variables defined here will override the values in nb_log_config_default. This serves as the default configuration for nb_log.
Users do not need to modify the config file inside the nb_log package installation directory.

The final configuration is determined by the parameters passed to get_logger_and_add_handlers().
If a parameter is None, the value defined here will be used.
"""

"""
To disable colored log output, set DEFAULUT_USE_COLOR_HANDLER = False
To disable block background colors in console, set DISPLAY_BACKGROUD_COLOR_IN_CONSOLE = False
To suppress the PyCharm color settings hint, set WARNING_PYCHARM_COLOR_SETINGS = False
To change the log format template, set FORMATTER_KIND (7 built-in templates available, or add custom ones)
LOG_PATH sets the directory for log file storage.
"""
import sys
# noinspection PyUnresolvedReferences
import logging
import os
# noinspection PyUnresolvedReferences
from pathlib import Path  # noqa
import socket
from pythonjsonlogger.jsonlogger import JsonFormatter

def judge_has_set_pythonpath() -> bool:
    """
    Judge whether PYTHONPATH is set.
    :return:
    """
    try:
        sys_path1_parent2 = Path(sys.path[1]).parents[2]
        if sys_path1_parent2 == Path(sys.executable).parents[2]:
            return False
        else:
            return True
    except IndexError:
        return True

def aut_get_proj_name() -> str:
    """
    Automatically determine the project name from the sys.path[1] directory.
    :return:
    """
    if judge_has_set_pythonpath() is False:
        """
         # For example /home/ydfwsl/miniconda3/lib/python37.zip, this usually happens because PYTHONPATH is not set to the project root directory.
         1. PyCharm IDE automatically adds the opened project root directory to PYTHONPATH.

         2. In VSCode, users should set the following in settings.json:
              {
                "python.analysis.extraPaths": ["${workspaceFolder}"],
                "terminal.integrated.env.windows": { "PYTHONPATH": "${workspaceFolder};${env:PYTHONPATH}" },
                "terminal.integrated.env.osx": { "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}" },
                "terminal.integrated.env.linux": { "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}" }
              }

         3. If manually starting Python scripts in cmd, PowerShell, or Linux, you need to manually set PYTHONPATH to the project root directory.
            Simply cd into the project root directory first, then execute the corresponding command:
            CMD: set PYTHONPATH=%cd%
            PowerShell: $env:PYTHONPATH = $PWD.Path
            Linux/macOS: export PYTHONPATH=$PWD

        """
        return 'no_proj_name'
    else:
        return Path(sys.path[1]).name 

# PRINT_WRTIE_FILE_NAME is an advanced feature unique to nb_log, beyond the scope of typical logging packages.
# Controls whether print output is automatically written to a file. Set to None to disable. A new file is created daily (e.g. 2023-06-30.my_proj.print) in LOG_PATH.
# If you set the environment variable PRINT_WRTIE_FILE_NAME (e.g. export PRINT_WRTIE_FILE_NAME="my_proj.print"), it takes priority over the value in nb_log_config.py.
PRINT_WRTIE_FILE_NAME = os.environ.get("PRINT_WRTIE_FILE_NAME") or aut_get_proj_name() + '.print'

# SYS_STD_FILE_NAME is an advanced feature unique to nb_log, beyond the scope of typical logging packages.
# All stdout output (including print and StreamHandler logs) is written to this file. Set to None to disable. A new file is created daily (e.g. 2023-06-30.my_proj.std) in LOG_PATH.
# If you set the environment variable SYS_STD_FILE_NAME (e.g. export SYS_STD_FILE_NAME="my_proj.std"), it takes priority over the value in nb_log_config.py.
# This is similar to nohup redirecting all screen output to a nohup.out file - a unique feature of nb_log that logging and loguru don't offer.
# While different logger namespaces may write to dozens of separate log files, SYS_STD_FILE_NAME consolidates all project logs into a single file.
SYS_STD_FILE_NAME = os.environ.get("SYS_STD_FILE_NAME") or aut_get_proj_name() + '.std'

USE_BULK_STDOUT_ON_WINDOWS = False  # Whether to batch stdout every 0.1s on Windows (Windows I/O performance is poor)

DEFAULUT_USE_COLOR_HANDLER = True  # Whether to use colored log output by default.
DEFAULUT_IS_USE_LOGURU_STREAM_HANDLER = False  # Whether to use loguru's console handler instead of nb_log's ColorHandler by default.
DISPLAY_BACKGROUD_COLOR_IN_CONSOLE = True  # Whether to display block background colors in console logs. Set to False to disable background colors.
AUTO_PATCH_PRINT = True  # Whether to auto-patch print with monkey patch. When patched, print output is colorized and clickable for navigation.

# The following settings control startup hints in the console. Before disabling them, make sure you understand what each hint is for.
SHOW_PYCHARM_COLOR_SETINGS = True  # Set to False to suppress the PyCharm console color optimization hint at startup.
SHOW_NB_LOG_LOGO = True  # Set to False to suppress the nb_log ASCII logo at startup.
SHOW_IMPORT_NB_LOG_CONFIG_PATH = True  # Whether to print the path of the loaded nb_log_config.py file. See https://github.com/ydf0509/pythonpathdemo for PYTHONPATH details.

WHITE_COLOR_CODE = 37  # Different PyCharm versions/themes use different codes for white (37 or 97). Adjust based on your PyCharm console color settings.

DEFAULT_ADD_MULTIPROCESSING_SAFE_ROATING_FILE_HANDLER = False  # Whether to automatically write logs to a file even when log_filename is not specified (auto-generates namespace.log).
AUTO_WRITE_ERROR_LEVEL_TO_SEPARATE_FILE = False  # Automatically write ERROR level and above to a separate file, with filename auto-generated from log_filename.
LOG_FILE_SIZE = 1000  # Max size per log file in MB. Files are rotated when this size is exceeded.
LOG_FILE_BACKUP_COUNT = 10  # Max number of backup files to keep per log file. Older backups are deleted.

LOG_PATH = os.getenv("LOG_PATH")  # Priority: read from environment variable first (e.g. export LOG_PATH='/your/log/dir/')
if not LOG_PATH:
    LOG_PATH = '/pythonlogs'  # Default log directory, located at the root of the drive where the project resides.
    # LOG_PATH = Path(__file__).absolute().parent / Path("pythonlogs")   # This would create a pythonlogs folder in the project root.
    if os.name == 'posix':  # Non-root Linux/Mac users don't have write access to /pythonlogs, so default to ~/pythonlogs instead.
        home_path = os.environ.get("HOME", '/')  # Gets the current user's home directory on Linux/Mac
        LOG_PATH = Path(home_path) / Path('pythonlogs')  # Linux/Mac permissions are strict; non-root users can't write to /pythonlogs.
# print('LOG_PATH:',LOG_PATH)

LOG_FILE_HANDLER_TYPE = 6  # 1 2 3 4 5 6 7   # nb_log file rotation - all options are multi-process safe.
"""
LOG_FILE_HANDLER_TYPE can be set to one of the following values:
1 - Multi-process safe size-based rotation with batch writing to reduce file lock operations.
    In tests with 10 processes, performance is 100x better than type 5 on Windows, 5x better on Linux.
2 - Multi-process safe daily rotation. A new log file is created each day with a date suffix.
3 - Single file without rotation (no rotation means no multi-process safety concerns).
4 - WatchedFileHandler (Linux only). Relies on external logrotate for file rotation. Multi-process safe.
5 - Third-party concurrent_log_handler.ConcurrentRotatingFileHandler for size-based rotation.
    Uses file locks (fcntl on Linux, win32con on Windows). Performance on Windows is very poor.
    For size-based rotation, type 1 is recommended over type 5.
6 - BothDayAndSizeRotatingFileHandler. Custom implementation that rotates by both time and size.
    Files are rotated whenever either the size or time threshold is reached.
7 - LoguruFileHandler. Uses the well-known loguru package's file handler for writing logs.
"""

LOG_LEVEL_FILTER = logging.DEBUG  # Default log level when not specified in get_logger(). Logs below this level are ignored (e.g. if set to INFO, debug logs are suppressed).
# It is strongly discouraged to raise this globally to INFO. Use logger namespaces to adjust levels for verbose loggers individually.
# See https://nb-log-doc.readthedocs.io/zh_CN/latest/articles/c9.html#id2 for details on logger namespace usage.

ROOT_LOGGER_LEVEL = logging.INFO  # Log level for the root logger namespace. If INFO, all unhandled loggers will capture INFO and above.
ROOT_LOGGER_FILENAME = 'root.log'  # Filename for root logger logs. Set to None to disable file logging for root.
ROOT_LOGGER_FILENAME_ERROR = 'root.error.log'  # Separate filename for ERROR level and above from root logger. Set to None to disable.

# Filter console output by keywords. If a message contains any string in this list, it will be suppressed.
# This applies to both print and logger console output. Useful for filtering verbose prints from third-party packages.
# Avoid adding too many entries as it may slightly affect performance.
FILTER_WORDS_PRINT = []  # e.g. FILTER_WORDS_PRINT = ['noisy_module', 'verbose_warning'] to suppress messages containing these strings.


def get_host_ip():
    ip = ''
    host_name = ''
    # noinspection PyBroadException
    try:
        sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sc.connect(('8.8.8.8', 80))
        ip = sc.getsockname()[0]
        host_name = socket.gethostname()
        sc.close()
    except Exception:
        pass
    return ip, host_name


computer_ip, computer_name = get_host_ip()


class JsonFormatterJumpAble(JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        # log_record['jump_click']   = f"""File '{record.__dict__.get('pathname')}', line {record.__dict__.get('lineno')}"""
        log_record[f"{record.__dict__.get('pathname')}:{record.__dict__.get('lineno')}"] = ''  # Add a clickable jump-to-source field.
        log_record['ip'] = computer_ip
        log_record['host_name'] = computer_name
        super().add_fields(log_record, record, message_dict)
        if 'for_segmentation_color' in log_record:
            del log_record['for_segmentation_color']


DING_TALK_TOKEN = '3dd0eexxxxxadab014bd604XXXXXXXXXXXX'  # DingTalk alert bot token

EMAIL_HOST = ('smtp.sohu.com', 465)
EMAIL_FROMADDR = 'aaa0509@sohu.com'  # 'matafyhotel-techl@matafy.com',
EMAIL_TOADDRS = ('cccc.cheng@silknets.com', 'yan@dingtalk.com',)
EMAIL_CREDENTIALS = ('aaa0509@sohu.com', 'abcdefg')

ELASTIC_HOST = '127.0.0.1'
ELASTIC_PORT = 9200

KAFKA_BOOTSTRAP_SERVERS = ['192.168.199.202:9092']
ALWAYS_ADD_KAFKA_HANDLER_IN_TEST_ENVIRONENT = False

MONGO_URL = 'mongodb://myUserAdmin:mimamiama@127.0.0.1:27016/admin'

RUN_ENV = 'test'

FORMATTER_DICT = {
    1: logging.Formatter(
        'Time[%(asctime)s] - Logger[%(name)s] - File[%(filename)s] - Line[%(lineno)d] - Level[%(levelname)s] - Message[%(message)s]',
        "%Y-%m-%d %H:%M:%S"),
    2: logging.Formatter(
        '%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),
    3: logging.Formatter(
        '%(asctime)s - %(name)s - [ File "%(pathname)s", line %(lineno)d, in %(funcName)s ] - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),  # Traceback-style template with clickable file path
    4: logging.Formatter(
        '%(asctime)s - %(name)s - "%(filename)s" - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s -               File "%(pathname)s", line %(lineno)d ',
        "%Y-%m-%d %H:%M:%S"),  # Also supports clickable log navigation
    5: logging.Formatter(
        '%(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),  # Recommended template
    6: logging.Formatter('%(name)s - %(asctime)-15s - %(filename)s - %(lineno)d - %(levelname)s: %(message)s',
                         "%Y-%m-%d %H:%M:%S"),
    7: logging.Formatter('%(asctime)s - %(name)s - "%(filename)s:%(lineno)d" - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"),  # Short filename with line number

    8: JsonFormatterJumpAble('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s %(lineno)d  %(process)d %(thread)d', "%Y-%m-%d %H:%M:%S.%f",
                             json_ensure_ascii=False),  # JSON format, ideal for ELK stack ingestion and analysis.

    9: logging.Formatter(
        '[p%(process)d_t%(thread)d] %(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s',
        "%Y-%m-%d %H:%M:%S"),  # Enhanced template 5 with process and thread info.
    10: logging.Formatter(
        '[p%(process)d_t%(thread)d] %(asctime)s - %(name)s - "%(filename)s:%(lineno)d" - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"),  # Enhanced template 7 with process and thread info.
    11: logging.Formatter(
        f'%(asctime)s-({computer_ip},{computer_name})-[p%(process)d_t%(thread)d] - %(name)s - "%(filename)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"),  # Enhanced template 7 with process, thread, IP, and hostname.
}

FORMATTER_KIND = 5  # Default formatter template index when not specified in get_logger()

`````

--- **end of file: scripts/nb_log_config.py** (project: nbrag) --- 

---


--- **start of file: scripts/query_langchain.py** (project: nbrag) --- 

`````python
"""通过 nbrag 查询 create_deep_agent 用法。"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_load_config
from nbrag.config import load_config
from nbrag.core import search, find_symbol_definition, get_raw_file

load_config()

COL = "langchain_ai_codes_and_docs"

# 步骤 1: 语义搜索
print("=" * 60)
print("步骤 1: 语义搜索 'create_deep_agent 用法'")
print("=" * 60)
results = search("create_deep_agent 用法 参数 示例", collection_name=COL, top_k=5)
for i, r in enumerate(results.get("results", []), 1):
    meta = r.get("metadata", {})
    print(f"\n[{i}] {meta.get('filename', '?')} chunk:{meta.get('chunk_index', '?')}/{meta.get('total_chunks', '?')}")
    print(f"    scope: {meta.get('scope', '?')}  lines: {meta.get('line_start', '?')}-{meta.get('line_end', '?')}")
    print(f"    doc_id: {meta.get('doc_id', '?')}")
    doc = r.get("document", "")
    print(f"    内容预览: {doc[:200]}...")

# 步骤 2: 查找符号定义
print("\n" + "=" * 60)
print("步骤 2: 查找 create_deep_agent 完整定义")
print("=" * 60)
defs = find_symbol_definition("create_deep_agent", collection_name=COL, max_results=1)
for d in defs:
    print(f"\n文件: {d.get('filename')}")
    print(f"符号: {d.get('qualified_name')} ({d.get('symbol_type')})")
    print(f"行号: {d.get('line_start')}-{d.get('line_end')}")
    print(f"定义:\n{d.get('definition', '')[:500]}...")

# 步骤 3: 获取完整源码
if defs:
    d = defs[0]
    print("\n" + "=" * 60)
    print(f"步骤 3: 获取 {d.get('filename')} 完整源码 (行 {d.get('line_start')}-{d.get('line_end')})")
    print("=" * 60)
    raw = get_raw_file(d["doc_id"], collection_name=COL, line_start=d["line_start"], line_end=d["line_end"])
    if raw.get("found"):
        print(raw.get("content", "")[:800])
    else:
        print(f"  未找到: {raw.get('error')}")

`````

--- **end of file: scripts/query_langchain.py** (project: nbrag) --- 

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

"""
 D:/ProgramData/Miniconda3/envs/py312/python.exe d:/codes/nbrag/scripts/start_http_rag_mcp.py

"""
`````

--- **end of file: scripts/start_http_rag_mcp.py** (project: nbrag) --- 

---


--- **start of file: scripts/start_local_rag_mcp.py** (project: nbrag) --- 

`````python
# """
# 启动 nbrag STDIO MCP Server（用于 Claude Code 等 stdio MCP 客户端）。

# 完全自包含脚本，不依赖环境变量传递。
# """

# import os
# import sys

# # nb_log banner 会直接 print 到 stdout，污染 MCP stdio 协议。
# # 在导入任何可能触发 nb_log 的模块前，将 stdout 重定向到 stderr
# _clean_stdout = sys.stdout
# sys.stdout = sys.stderr

# # 确保 PYTHONPATH 包含项目根目录
# _project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.insert(0, _project_root)
# os.environ.setdefault("PYTHONPATH", _project_root)

# # 确保 nltk 能找到数据目录
# _nltk_data = os.path.expanduser("~/nltk_data")
# if os.path.isdir(_nltk_data):
#     os.environ.setdefault("NLTK_DATA", _nltk_data)

# import my_load_config
# from nbrag.config import load_config
# from nbrag.server import mcp

# # nbrag 已完成导入，恢复 stdout 用于 MCP JSON-RPC 通信
# sys.stdout = _clean_stdout

# load_config()

# print("[nbrag] STDIO MCP server started", file=sys.stderr)

# mcp.run(transport="stdio")

`````

--- **end of file: scripts/start_local_rag_mcp.py** (project: nbrag) --- 

---


--- **start of file: scripts/test_find_def.py** (project: nbrag) --- 

`````python
"""测试 find_symbol_definition 在当前代码下是否还会报错。"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_load_config
from nbrag.config import load_config
from nbrag.core import find_symbol_definition

load_config()

print("调用 find_symbol_definition('create_deep_agent', 'langchain_ai_codes_and_docs', max_results=1)...")
try:
    result = find_symbol_definition("create_deep_agent", "langchain_ai_codes_and_docs", max_results=1)
    print(f"成功: {len(result)} 个结果")
    if result:
        r = result[0]
        print(f"  filename: {r.get('filename')}")
        print(f"  symbol_type: {r.get('symbol_type')}")
        print(f"  qualified_name: {r.get('qualified_name')}")
        print(f"  line_start: {r.get('line_start')}")
        print(f"  definition (前100字): {r.get('definition', '')[:100]}")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

`````

--- **end of file: scripts/test_find_def.py** (project: nbrag) --- 

---


--- **start of file: scripts/test_raw_get.py** (project: nbrag) --- 

`````python
"""用原始 col.get() 直接测试，不经过 _batch_get。"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_load_config
from nbrag.config import load_config
from nbrag.core import _get_existing_collection

load_config()

col = _get_existing_collection("langchain_ai_codes_and_docs")
if col is None:
    print("collection 不存在")
    sys.exit(1)

count = col.count()
print(f"collection 文档数: {count}")

# 直接调用原始 col.get()
print("\n直接调用 col.get(include=['metadatas'])...")
try:
    result = col.get(include=["metadatas"])
    print(f"成功: {len(result['metadatas'])} 条")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

print("\n直接调用 col.get(include=['documents', 'metadatas'])...")
try:
    result = col.get(include=["documents", "metadatas"])
    print(f"成功: {len(result['ids'])} 条")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

`````

--- **end of file: scripts/test_raw_get.py** (project: nbrag) --- 

---


--- **start of file: scripts/trigger_bug.py** (project: nbrag) --- 

`````python
"""直接调用 nbrag 核心函数触发 too many SQL variables bug。"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_load_config
from nbrag.config import load_config
from nbrag.core import find_symbol_definition, _get_doc_id_map, list_documents, get_stats

load_config()

# 先测试 _get_doc_id_map（全量查询，最容易触发）
print("=" * 60)
print("测试 1: _get_doc_id_map (全量 metadatas 查询)")
print("=" * 60)
try:
    result = _get_doc_id_map("langchain_ai_codes_and_docs")
    print(f"成功: {len(result)} 个文档")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

# 测试 list_documents
print("\n" + "=" * 60)
print("测试 2: list_documents (全量 metadatas 查询)")
print("=" * 60)
try:
    result = list_documents("langchain_ai_codes_and_docs")
    print(f"成功: {len(result)} 个文档")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

# 测试 get_stats
print("\n" + "=" * 60)
print("测试 3: get_stats (全量 metadatas 查询)")
print("=" * 60)
try:
    result = get_stats()
    print(f"成功: {len(result.get('collections', {}))} 个知识库")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

# 测试 find_symbol_definition
print("\n" + "=" * 60)
print("测试 4: find_symbol_definition (调用 _get_doc_id_map)")
print("=" * 60)
try:
    result = find_symbol_definition("create_deep_agent", "langchain_ai_codes_and_docs", max_results=1)
    print(f"成功: {len(result)} 个结果")
except Exception as e:
    print(f"失败: {type(e).__name__}: {e}")

print("\n全部测试完成")

`````

--- **end of file: scripts/trigger_bug.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_ex1/ingest_civil_code.py** (project: nbrag) --- 

`````python
"""
导入《中华人民共和国民法典》全文到 civil_code 知识库。
7 个分编 + 1 个全文，约 224K 字符。

用法:
    cd D:/codes/nbrag
    python scripts/ingest_ex1/ingest_civil_code.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import my_load_config
from nbrag.core import batch_ingest

batch_ingest(
    paths=["D:/codes/nbrag/scripts/ingest_ex1"],
    collection_name="civil_code",
    file_extensions=[".md"],
    max_workers=1,
    delete_first=True,
    verbose=True,
    sleep_interval=1,
)

`````

--- **end of file: scripts/ingest_ex1/ingest_civil_code.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_ex1/prepare_civil_code.py** (project: nbrag) --- 

`````python
"""
清洗《中华人民共和国民法典》全文，按"编"拆分为独立文件，供 nbrag ingest 测试。
"""
import re
from pathlib import Path

RAW_FILE = Path(r"C:\Users\ydf19\.cursor\projects\d-codes-ai-proj\agent-tools\5584ca14-6ddd-4bb8-b565-890d6b6f6f16.txt")
OUTPUT_DIR = Path(__file__).parent

raw = RAW_FILE.read_text(encoding="utf-8")

lines = raw.splitlines()
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if "第一编 总则" in line and start_idx is None:
        if i > 0 and "目 录" not in lines[i - 2]:
            start_idx = i
    if line.strip().startswith("附件："):
        end_idx = i
        break

if start_idx is None:
    for i, line in enumerate(lines):
        if re.match(r"第一条\s", line):
            start_idx = i
            break

if end_idx is None:
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith("第一千二百六十条"):
            end_idx = i + 1
            break

body_lines = lines[start_idx:end_idx]
body = "\n".join(body_lines)

header = """中华人民共和国民法典
（2020年5月28日第十三届全国人民代表大会第三次会议通过）
自2021年1月1日起施行。

"""

split_pattern = re.compile(r"^(第[一二三四五六七]编\s+\S+)$")
parts = []
current_title = "前言"
current_lines = []

for line in body_lines:
    m = split_pattern.match(line.strip())
    if m and not current_lines:
        current_title = m.group(1)
        current_lines = [line]
    elif m:
        parts.append((current_title, current_lines))
        current_title = m.group(1)
        current_lines = [line]
    else:
        current_lines.append(line)

if current_lines:
    parts.append((current_title, current_lines))

part_names = {
    "第一编 总则": "01_总则.md",
    "第二编 物权": "02_物权.md",
    "第三编 合同": "03_合同.md",
    "第四编 人格权": "04_人格权.md",
    "第五编 婚姻家庭": "05_婚姻家庭.md",
    "第六编 继承": "06_继承.md",
    "第七编 侵权责任": "07_侵权责任.md",
}

saved = []
for title, plines in parts:
    fname = part_names.get(title, f"99_{title}.md")
    content = header + f"# {title}\n\n" + "\n".join(plines) + "\n"
    out = OUTPUT_DIR / fname
    out.write_text(content, encoding="utf-8")
    saved.append((fname, len(plines), len(content)))
    print(f"  {fname}: {len(plines)} lines, {len(content)} chars")

full_out = OUTPUT_DIR / "民法典_全文.md"
full_content = header + body + "\n"
full_out.write_text(full_content, encoding="utf-8")
print(f"\n  民法典_全文.md: {len(body_lines)} lines, {len(full_content)} chars")
print(f"\nTotal: {len(saved)} parts + 1 full text saved to {OUTPUT_DIR}")

`````

--- **end of file: scripts/ingest_ex1/prepare_civil_code.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_ex2_marriage_law/ingest_marriage_law.py** (project: nbrag) --- 

`````python
"""
导入婚姻家庭法相关法律文本到 marriage_law 知识库。
包含：
  - 民法典 第五编 婚姻家庭
  - 婚姻家庭编司法解释（一）—— 91条，2021年施行
  - 婚姻家庭编司法解释（二）—— 23条，2025年施行
  - 解释（二）新闻发布会背景介绍
  - 解释（二）记者问答与典型案例

用法:
    cd D:/codes/nbrag
    python scripts/ingest_ex2_marriage_law/ingest_marriage_law.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import my_load_config
from nbrag.core import batch_ingest

batch_ingest(
    paths=["D:/codes/nbrag/scripts/ingest_ex2_marriage_law"],
    collection_name="marriage_law",
    file_extensions=[".md"],
    max_workers=1,
    delete_first=True,
    verbose=True,
    sleep_interval=1,
)

`````

--- **end of file: scripts/ingest_ex2_marriage_law/ingest_marriage_law.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_ex2_marriage_law/prepare_marriage_law.py** (project: nbrag) --- 

`````python
"""
清洗婚姻家庭相关法律文本，保存到当前目录，供 nbrag ingest 测试。
包含：
  1. 民法典 第五编 婚姻家庭（已在 ingest_ex1 中，此处复用）
  2. 婚姻家庭编司法解释（一）—— 91条，2021年施行
  3. 婚姻家庭编司法解释（二）—— 23条，2025年施行
  4. 解释（二）新闻发布会背景介绍 + 典型案例 + 记者问答
"""
import re
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent

# === 解释（一） ===
raw1 = Path(r"C:\Users\ydf19\.cursor\projects\d-codes-ai-proj\agent-tools\59d059a2-7b7e-4095-837b-859f4e84a866.txt").read_text(encoding="utf-8")
lines1 = raw1.splitlines()

start1 = None
end1 = None
for i, line in enumerate(lines1):
    if "为正确审理婚姻家庭纠纷案件" in line and start1 is None:
        start1 = i
    if "第九十一条" in line and "本解释自" in line:
        end1 = i + 1
        break

body1 = "\n".join(lines1[start1:end1]) if start1 and end1 else ""

header1 = """# 最高人民法院关于适用《中华人民共和国民法典》婚姻家庭编的解释（一）

法释〔2020〕22号
2020年12月25日审判委员会第1825次会议通过，自2021年1月1日起施行。

"""

out1 = OUTPUT_DIR / "司法解释_一_婚姻家庭编.md"
out1.write_text(header1 + body1 + "\n", encoding="utf-8")
print(f"  {out1.name}: {len(body1)} chars")

# === 解释（二）：正文 + 发布背景 + 典型案例 + 记者问答 ===
raw2 = Path(r"C:\Users\ydf19\.cursor\projects\d-codes-ai-proj\agent-tools\e0c6efff-1207-488d-a611-b6a6f3012eda.txt").read_text(encoding="utf-8")
lines2 = raw2.splitlines()

# 发布会背景介绍（解释正文之前的内容）
bg_start = None
bg_end = None
for i, line in enumerate(lines2):
    if "一、《解释（二）》的制定背景" in line and bg_start is None:
        bg_start = i
    if line.strip().startswith("法释〔2025〕1号"):
        bg_end = i
        break

if bg_start and bg_end:
    bg_body = "\n".join(lines2[bg_start:bg_end])
    header_bg = """# 婚姻家庭编司法解释（二）—— 新闻发布会介绍

最高人民法院 2025年1月15日

"""
    out_bg = OUTPUT_DIR / "解释二_发布会背景介绍.md"
    out_bg.write_text(header_bg + bg_body + "\n", encoding="utf-8")
    print(f"  {out_bg.name}: {len(bg_body)} chars")

# 解释（二）正文
start2 = None
end2 = None
for i, line in enumerate(lines2):
    if "为正确审理婚姻家庭纠纷案件" in line and i > 50 and start2 is None:
        start2 = i
    if "第二十三条" in line and "本解释自" in line:
        end2 = i + 1
        break

body2 = "\n".join(lines2[start2:end2]) if start2 and end2 else ""

header2 = """# 最高人民法院关于适用《中华人民共和国民法典》婚姻家庭编的解释（二）

法释〔2025〕1号
2024年11月25日审判委员会第1933次会议通过，自2025年2月1日起施行。

"""

out2 = OUTPUT_DIR / "司法解释_二_婚姻家庭编.md"
out2.write_text(header2 + body2 + "\n", encoding="utf-8")
print(f"  {out2.name}: {len(body2)} chars")

# 记者问答和典型案例
qa_start = None
for i, line in enumerate(lines2):
    if "答记者问" in line and i > end2:
        qa_start = i
        break

if qa_start:
    qa_end = len(lines2)
    for i in range(len(lines2) - 1, qa_start, -1):
        stripped = lines2[i].strip()
        if stripped and not any(kw in stripped for kw in ["版权", "法律法规", "©", "备案", "ICP", "导航", "友情链接", "深圳"]):
            qa_end = i + 1
            break

    qa_body = "\n".join(lines2[qa_start:qa_end])
    header_qa = """# 婚姻家庭编司法解释（二）—— 记者问答与典型案例

最高人民法院 2025年1月15日

"""
    out_qa = OUTPUT_DIR / "解释二_记者问答与典型案例.md"
    out_qa.write_text(header_qa + qa_body + "\n", encoding="utf-8")
    print(f"  {out_qa.name}: {len(qa_body)} chars")

# === 复制 民法典 第五编 婚姻家庭 ===
src_marriage = Path(r"D:\codes\nbrag\scripts\ingest_ex1\05_婚姻家庭.md")
if src_marriage.exists():
    dst_marriage = OUTPUT_DIR / "民法典_第五编_婚姻家庭.md"
    dst_marriage.write_text(src_marriage.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"  {dst_marriage.name}: copied from ingest_ex1")

print(f"\nDone! Files saved to {OUTPUT_DIR}")

`````

--- **end of file: scripts/ingest_ex2_marriage_law/prepare_marriage_law.py** (project: nbrag) --- 

---


--- **start of file: scripts/ingest_ex3_worker_rights/ingest_worker_rights.py** (project: nbrag) --- 

`````python
"""
导入"打工人法律百科"知识库 — 18 部劳动/社保/税务法律法规。

涵盖：劳动法、劳动合同法、社会保险法、个人所得税法、工伤/失业/公积金、
      带薪年休假、工资支付、女职工保护、职业病防治、劳动争议仲裁等。

用法:
    cd D:/codes/nbrag
    D:/ProgramData/miniconda3/envs/py312/python.exe scripts/ingest_ex3_worker_rights/ingest_worker_rights.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import my_load_config
from nbrag.core import batch_ingest

batch_ingest(
    paths=["D:/codes/nbrag/scripts/ingest_ex3_worker_rights"],
    collection_name="worker_rights",
    file_extensions=[".md"],
    max_workers=1,
    delete_first=True,
    verbose=True,
    sleep_interval=1,
)

`````

--- **end of file: scripts/ingest_ex3_worker_rights/ingest_worker_rights.py** (project: nbrag) --- 

---


--- **start of file: scripts/inguest_licai/ingest_licai.py** (project: nbrag) --- 

`````python
"""把 inguest_licai 目录下的 PDF 转成 .md 文本，再批量导入 nbrag 知识库 finance_reports。

流程：
    1. 扫描 PDF 文件
    2. 用 pdfplumber 逐页提取文字（含表格按行拼接）
    3. 写到同名 .md 文件（同目录）
    4. 调 batch_ingest 导入 nbrag

用法：
    D:/ProgramData/miniconda3/envs/py312/python.exe d:/codes/nbrag/scripts/inguest_licai/ingest_licai.py
"""

import os
import sys
from pathlib import Path

# 项目根加入 sys.path（容忍任意 cwd 启动）
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import my_load_config  # noqa: F401  加载 NBRAG_API_KEY
import pdfplumber
from nbrag.core import batch_ingest


PDF_DIR = Path(__file__).resolve().parent
COLLECTION_NAME = "finance_reports"


def pdf_to_markdown(pdf_path: Path, md_path: Path) -> int:
    """把 PDF 转成 .md，返回总页数。"""
    lines = [f"# {pdf_path.stem}\n", f"> Source: {pdf_path.name}\n"]
    with pdfplumber.open(pdf_path) as pdf:
        n_pages = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            lines.append(f"\n## Page {i}\n")
            text = page.extract_text() or ""
            if text.strip():
                lines.append(text.strip())
                lines.append("")
            for tbl_idx, tbl in enumerate(page.extract_tables() or []):
                if not tbl:
                    continue
                lines.append(f"\n### Page {i} Table {tbl_idx + 1}\n")
                for row in tbl:
                    cells = [(c or "").strip().replace("\n", " ") for c in row]
                    lines.append("| " + " | ".join(cells) + " |")
                lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return n_pages


def convert_all_pdfs() -> list[Path]:
    """把目录下所有 PDF 转成 .md，返回 .md 路径列表。"""
    md_paths = []
    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        md = pdf.with_suffix(".md")
        if md.exists() and md.stat().st_mtime >= pdf.stat().st_mtime:
            print(f"[skip] {md.name} 已是最新")
        else:
            print(f"[conv] {pdf.name} -> {md.name} ...")
            n = pdf_to_markdown(pdf, md)
            print(f"       完成，{n} 页")
        md_paths.append(md)
    return md_paths


def main():
    md_paths = convert_all_pdfs()
    if not md_paths:
        print("没找到 PDF")
        return

    print(f"\n开始导入 {len(md_paths)} 个 .md 到 nbrag collection={COLLECTION_NAME}")
    batch_ingest(
        paths=[str(p) for p in md_paths],
        collection_name=COLLECTION_NAME,
        file_extensions=[".md"],
        max_workers=1,
        delete_first=True,
        verbose=True,
        sleep_interval=0.1,
    )
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()

`````

--- **end of file: scripts/inguest_licai/ingest_licai.py** (project: nbrag) --- 

---

