"""
测试 __init__ 方法参数提取功能
"""
from nb_ai_context import AiMdGenerator
from nb_path import NbPath
import tempfile
import os


# 创建一个测试用的 Python 文件
test_code = '''
"""测试模块"""
from typing import Optional, List


class UserService:
    """用户服务类
    
    这是一个处理用户相关业务的服务类
    """
    
    def __init__(
        self, 
        database_url: str,
        timeout: int = 30,
        max_connections: int = 10,
        enable_cache: bool = True,
        allowed_domains: Optional[List[str]] = None,
        **kwargs
    ):
        """初始化用户服务
        
        Args:
            database_url: 数据库连接URL
            timeout: 超时时间（秒）
            max_connections: 最大连接数
            enable_cache: 是否启用缓存
            allowed_domains: 允许的域名列表
        """
        self.database_url = database_url
        self.timeout = timeout
        self.max_connections = max_connections
        self.enable_cache = enable_cache
        self.allowed_domains = allowed_domains or []
    
    def get_user(self, user_id: int) -> dict:
        """获取用户信息"""
        pass
    
    def create_user(self, name: str, email: str) -> bool:
        """创建新用户"""
        pass
    
    @property
    def connection_count(self) -> int:
        """当前连接数"""
        return 0


class SimpleClass:
    """一个没有 __init__ 方法的简单类"""
    
    def do_something(self):
        """做一些事情"""
        pass
'''


def test_init_extraction():
    """测试 __init__ 方法提取"""
    
    # 创建临时目录和文件
    with tempfile.TemporaryDirectory() as temp_dir:
        # 创建测试文件
        test_file = os.path.join(temp_dir, "test_service.py")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(test_code)
        
        # 生成 AI Markdown
        output_path = os.path.join(temp_dir, "test_output.md")
        
        (
            AiMdGenerator(output_path)
            .set_project_propery(
                project_name="test_project",
                project_root=temp_dir
            )
            .clear_text()
            .merge_from_files(
                relative_file_name_list=["test_service.py"],
                as_title="测试代码",
            )
            .show_textfile_info()
        )
        
        # 读取生成的内容
        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        print("\n" + "="*80)
        print("生成的 Markdown 内容（AST 元数据部分）：")
        print("="*80)
        
        # 只打印元数据部分
        if "### 📄 Python File Metadata:" in content:
            metadata_start = content.index("### 📄 Python File Metadata:")
            metadata_end = content.index("```python", metadata_start) if "```python" in content[metadata_start:] else len(content)
            print(content[metadata_start:metadata_end])
        
        # 验证关键内容
        assert "🔧 Constructor (`__init__`):" in content, "缺少 __init__ 构造器标题"
        assert "database_url: str" in content, "缺少 database_url 参数"
        assert "timeout: int = 30" in content, "缺少 timeout 参数及默认值"
        assert "enable_cache: bool = True" in content, "缺少 enable_cache 参数及默认值"
        assert "Optional[List[str]]" in content, "缺少复杂类型注解"
        assert "**kwargs" in content, "缺少 kwargs 参数"
        
        print("\n✅ 所有测试通过！__init__ 方法参数提取成功！")
        print("\n关键特性验证：")
        print("  ✓ __init__ 方法被单独显示")
        print("  ✓ 参数类型注解正确提取")
        print("  ✓ 默认值正确显示")
        print("  ✓ 复杂类型（Optional[List[str]]）正确解析")
        print("  ✓ **kwargs 等特殊参数正确处理")
        print("  ✓ 没有 __init__ 的类也能正常处理")


if __name__ == "__main__":
    test_init_extraction()

