import typing
import os
import fnmatch
import ast

from nb_path import NbPath

class AiMdGenerator(NbPath):
    """
    An extremely powerful context generator born for AI collaboration.

    This class is designed to revolutionize how developers interact with Large Language
    Models (LLMs). It intelligently merges multiple project source files into a single,
    well-structured, and context-rich Markdown file, providing the AI with a perfect
    and comprehensive project snapshot.

    The benefits for large AI models are immense:
    1.  **Provides a God's-eye View**: Through a file manifest, clear file boundaries,
        and relative paths, the AI can easily construct the project's overall
        architecture and understand file dependencies and relationships, rather than
        fumbling in the dark.
    2.  **Ensures Information Integrity and Accuracy**: The AI receives complete,
        unabridged source file content, avoiding the chaos, omissions, or context
        loss caused by manual copy-pasting. This enables it to provide more precise
        analysis and suggestions.
    3.  **Enhances Security**: The built-in `use_gitignore` feature is a critical
        security barrier. It automatically ignores files containing sensitive
        information (like API keys or database passwords) such as `.env` or local
        configs, allowing you to share code without fear of accidental leaks.

    Its core methods, `merge_from_files` and `merge_from_dir`, offer extreme
    flexibility. Combined with the elegant chainable calls of `nb_path`, creating a
    high-quality AI context is transformed from a tedious, error-prone manual task
    into a single, delightful line of code.

    Example:
        >>> # Imagine you want an AI to review your entire project
        >>> project_name = "my_project"
        >>> project_summary = '''
        ... This is an excellent Python project that demonstrates best practices.
        ... It includes comprehensive documentation and well-structured code.
        ... '''
        >>> 
        >>> (
        ...     AiMdGenerator("project_context_for_ai.md")
        ...     .set_project_propery(project_name=project_name, project_root="/path/to/your/project")
        ...     .clear_text()  # Clear the old file
        ...     .add_project_summary(
        ...         project_summary=project_summary,
        ...         # Extract metadata (without full source) from core files first
        ...         most_core_source_code_file_list=[
        ...             "src/main.py",
        ...             "src/api.py",
        ...             "src/models.py",
        ...         ]
        ...     )
        ...     .auto_merge_from_python_project_some_files()  # Auto-include README, setup.py, etc.
        ...     .merge_from_dir(
        ...         relative_dir_name="src", # The main source code directory
        ...         as_title="Project Source Code",
        ...         use_gitignore=True,  # Automatically use .gitignore rules
        ...         should_include_suffixes=[".py", ".md"], # Only include specified file types
        ...         include_ast_metadata=True,  # Include AST metadata for Python files
        ...     )
        ...     .merge_from_dir(
        ...         relative_dir_name="tests", # The tests directory
        ...         as_title="Project Tests",
        ...         use_gitignore=True,
        ...         should_include_suffixes=[".py"],
        ...         excluded_dir_name_list=["tests/temp_files"],
        ...         include_ast_metadata=True,
        ...     )
        ... )
    """

    """cn description
    一个极其强大的、为 AI 协作而生的上下文生成器。

    此类旨在彻底改变开发者与大语言模型（LLM）的交互方式。它能够智能地将多个项目源文件
    合并成一个结构清晰、上下文丰富的单一 Markdown 文件，从而为 AI 提供一个完美、全面的项目快照。

    对 AI 大模型的好处是巨大的：
    1.  **提供上帝视角**：通过文件清单、清晰的文件边界和相对路径，AI 能够轻松构建出项目的
        整体架构，理解文件间的依赖和引用关系，而不是盲人摸象。
    2.  **确保信息的完整与准确**：AI 得到的是未经删减的、完整的源文件内容，避免了因手动
        复制粘贴导致的格式混乱、内容遗漏或上下文缺失，从而能给出更精准的分析和建议。
    3.  **提升安全性**：内置的 `use_gitignore` 功能是一道关键的安全屏障。它能自动忽略
        `.env`、本地配置等包含敏感信息（如 API 密钥、数据库密码）的文件，让你在分享代码
        时无需担心意外泄露秘密。

    其核心方法 `merge_from_files` 和 `merge_from_dir` 提供了极高的灵活性，结合 `nb_path`
    优雅的链式调用，使得创建一个高质量的 AI 上下文从繁琐、易错的手工劳动，变成了一行
    赏心悦目的代码。

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
            str_list.append("\n## 📋 Core Source Files Metadata (Entry Points)\n\n")
            str_list.append("以下是项目最核心的入口文件的结构化元数据，帮助快速理解项目架构：\n\n")
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
        return self

    def _generate_markdown_header(self, as_title: str, file_text_list: list) -> list:
        """生成包含文件树和文件列表的 Markdown 头部"""
        str_list = [f"# markdown content namespace: {as_title} \n\n"]

        # 1. 生成文件树
        str_list.append("## File Tree\n\n")
        str_list.append("```\n")
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
        str_list.append("\n```\n\n---\n\n")

        # 2. 生成文件列表
        str_list.append("## Included Files\n\n")
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
            str_list.append(f"--- **start of file: {relative_file_name_posix}** --- \n")
            # 3. Handle .md files separately to ensure their content is rendered correctly.
            #    Other file types are wrapped in code blocks.
            if suffix == ".md":
                str_list.append(text + "\n")
            else:
                lang = self.suffix__lang_map.get(suffix, "text")
                str_list.append(f"``{lang}\n{text}\n```\n")

            str_list.append(f"--- **end of file: {relative_file_name_posix}** --- \n")
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
            lines.append("```")
            lines.append(metadata["module_docstring"])
            lines.append("```\n")

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
                    lines.append("```")
                    lines.extend(docstring_lines)
                    lines.append("```\n")

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
                        lines.append("  ```")
                        for doc_line in init_method["docstring"].split("\n"):
                            lines.append(f"  {doc_line}")
                        lines.append("  ```")
                    
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
                                # 多行文档字符串，用代码块格式显示
                                lines.append("  - **Docstring:**")
                                lines.append("  ```")
                                for doc_line in docstring_lines:
                                    lines.append(f"  {doc_line}")
                                lines.append("  ```")
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
                            # 多行文档字符串，用代码块格式显示
                            lines.append("  - **Docstring:**")
                            lines.append("  ```")
                            for doc_line in docstring_lines:
                                lines.append(f"  {doc_line}")
                            lines.append("  ```")
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
            str_list.append(f"--- **start of file: {relative_file_name_posix}** --- \n")
            
            # 对于 Python 文件，添加 AST 元数据
            if suffix == ".py" and include_ast_metadata:
                metadata = self._parse_python_file_ast(file)
                metadata_md = self._format_py_metadata_as_markdown(metadata, relative_file_name_posix)
                str_list.append(metadata_md)
            
            # 添加完整的文件内容
            if suffix == ".md":
                str_list.append(text + "\n")
            else:
                lang = self.suffix__lang_map.get(suffix, "text")
                str_list.append(f"```{lang}\n{text}\n```\n")

            str_list.append(f"--- **end of file: {relative_file_name_posix}** --- \n")
            str_list.append("---\n\n")

        self.append_text('\n'.join(str_list))
        self.ensure_utf8_bom()
        return self
