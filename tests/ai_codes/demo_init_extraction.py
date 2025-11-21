"""
演示 __init__ 方法参数提取功能的示例代码
"""
from typing import Optional, List, Dict


class DatabaseConnection:
    """数据库连接类
    
    管理数据库连接池和查询操作
    """
    
    def __init__(
        self,
        host: str,
        port: int = 3306,
        username: str = "root",
        password: str = "",
        database: Optional[str] = None,
        charset: str = "utf8mb4",
        pool_size: int = 10,
        timeout: float = 30.0,
        ssl_config: Optional[Dict[str, str]] = None,
        auto_commit: bool = True,
        *args,
        **kwargs
    ):
        """初始化数据库连接
        
        Args:
            host: 数据库主机地址
            port: 数据库端口号，默认 3306
            username: 用户名，默认 root
            password: 密码
            database: 数据库名称（可选）
            charset: 字符集，默认 utf8mb4
            pool_size: 连接池大小
            timeout: 连接超时时间（秒）
            ssl_config: SSL 配置字典
            auto_commit: 是否自动提交事务
            *args: 额外的位置参数
            **kwargs: 额外的关键字参数
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset
        self.pool_size = pool_size
        self.timeout = timeout
        self.ssl_config = ssl_config or {}
        self.auto_commit = auto_commit
    
    def connect(self) -> bool:
        """建立数据库连接"""
        return True
    
    def execute(self, query: str, params: Optional[tuple] = None) -> List[Dict]:
        """执行 SQL 查询"""
        return []
    
    def close(self):
        """关闭数据库连接"""
        pass
    
    @property
    def is_connected(self) -> bool:
        """检查是否已连接"""
        return True


class SimpleLogger:
    """简单的日志类（没有 __init__ 参数）"""
    
    def log(self, message: str):
        """记录日志"""
        print(message)
    
    def error(self, message: str):
        """记录错误"""
        print(f"ERROR: {message}")


# 使用 AiMdGenerator 生成这个文件的 AST 元数据
if __name__ == "__main__":
    from nb_ai_context import AiMdGenerator
    from nb_path import NbPath
    
    # 获取当前文件路径
    current_file = NbPath(__file__)
    project_root = current_file.parent.parent.parent  # 回到项目根目录
    
    output_path = current_file.parent.parent / "ai_docs" / "demo_init_extraction_output.md"
    output_path.ensure_parent()
    
    print(f"当前文件: {current_file}")
    print(f"项目根目录: {project_root}")
    print(f"输出路径: {output_path}")
    
    # 生成 Markdown
    (
        AiMdGenerator(str(output_path))
        .set_project_propery(
            project_name="demo",
            project_root=str(project_root)
        )
        .clear_text()
        .merge_from_files(
            relative_file_name_list=[str(current_file.relative_to(project_root))],
            as_title="演示 __init__ 提取功能",
        )
        .show_textfile_info()
    )
    
    print(f"\n✅ 已生成 Markdown 文件: {output_path}")
    print(f"\n请查看文件内容，可以看到：")
    print("  1. DatabaseConnection 类的 __init__ 方法被单独突出显示")
    print("  2. 所有参数（包括类型、默认值）都被详细列出")
    print("  3. 支持复杂类型如 Optional[Dict[str, str]]")
    print("  4. 支持 *args 和 **kwargs")
    print("  5. SimpleLogger 类（没有自定义 __init__）也能正常处理")
    
    # 读取并显示部分内容
    content = output_path.read_text(encoding="utf-8")
    
    # 查找并显示 __init__ 部分
    if "🔧 Constructor (`__init__`):" in content:
        print("\n" + "="*80)
        print("生成的 __init__ 元数据预览：")
        print("="*80)
        
        start_idx = content.index("🔧 Constructor (`__init__`):")
        # 找到下一个 ** 开头的部分（Public Methods 或 Properties）
        end_markers = ["**Public Methods", "**Properties", "**Class Variables"]
        end_idx = len(content)
        for marker in end_markers:
            if marker in content[start_idx:]:
                potential_end = start_idx + content[start_idx:].index(marker)
                if potential_end < end_idx:
                    end_idx = potential_end
        
        print(content[start_idx:end_idx])
    else:
        print("\n⚠️ 未找到 __init__ 构造器信息")

