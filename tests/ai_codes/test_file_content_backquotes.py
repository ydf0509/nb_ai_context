"""测试 FILE_CONTENT_BACKQUOTES 变量的使用"""
import sys
import os

# 添加父目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from nb_ai_context.ai_md_generator import AiMdGenerator, FILE_CONTENT_BACKQUOTES

def test_file_content_backquotes():
    """测试 FILE_CONTENT_BACKQUOTES 是否正确定义"""
    print(f"FILE_CONTENT_BACKQUOTES 的值: {repr(FILE_CONTENT_BACKQUOTES)}")
    assert FILE_CONTENT_BACKQUOTES == "```", "FILE_CONTENT_BACKQUOTES 的值应该是三个反引号"
    print("✅ FILE_CONTENT_BACKQUOTES 定义正确")

def test_markdown_generation():
    """测试生成的 Markdown 是否使用了 FILE_CONTENT_BACKQUOTES"""
    # 创建一个测试文件
    test_file = "tests/ai_codes/temp_test.py"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write('def test_func():\n    """测试函数"""\n    return "hello"\n')
    
    try:
        # 生成 Markdown
        output_md = "tests/ai_docs/test_backquotes_output.md"
        generator = AiMdGenerator(output_md)
        generator.set_project_propery(
            project_name="test_project",
            project_root=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        )
        generator.clear_text()
        generator.merge_from_files(
            relative_file_name_list=["tests/ai_codes/temp_test.py"],
            as_title="Test Files"
        )
        
        # 读取生成的 Markdown
        with open(output_md, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 验证是否包含反引号（应该是通过 FILE_CONTENT_BACKQUOTES 变量生成的）
        assert "```" in content, "生成的 Markdown 应该包含代码块"
        print("✅ Markdown 生成成功，包含代码块")
        
        # 清理测试文件
        os.remove(test_file)
        print("✅ 测试完成")
        
    except Exception as e:
        # 清理测试文件
        if os.path.exists(test_file):
            os.remove(test_file)
        raise e

if __name__ == "__main__":
    print("开始测试 FILE_CONTENT_BACKQUOTES...")
    test_file_content_backquotes()
    test_markdown_generation()
    print("\n🎉 所有测试通过！")

