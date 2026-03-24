

"""
把所有一层级下的md文件合并成一个md文件
D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files
"""
from nb_path import NbPath

def merge_all_md():
    """
    合并指定目录下所有第一层级的 .md 文件到一个单独的 .md 文件中。
    """
    # 1. 定义源目录和输出文件路径
    # 使用 NBPath 来处理路径，它能很好地处理 Windows 风格的反斜杠
    source_dir = NbPath(r'D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files')
    output_file:NbPath = source_dir.parent / 'all_proj_merged_all_md_files.md' # 在同目录下创建输出文件，以 zz_ 开头方便排序和查找

    print(f"源目录: {source_dir}")
    print(f"输出文件: {output_file}")

    # 2. 检查源目录是否存在
    if not source_dir.is_dir():
        print(f"错误: 目录 '{source_dir}' 不存在。")
        return

    # 3. 查找所有第一层级的 .md 文件
    # 使用 .glob('*.md') 来匹配当前目录下的 md 文件
    # 使用 sorted() 确保合并顺序是可预测的（按字母顺序）
    md_files = sorted(list(source_dir.glob('*.md')))

    if not md_files:
        print("未在该目录下找到任何 .md 文件。")
        return

    # 4. 准备合并内容
    all_contents = []
    print(f"\n找到 {len(md_files)} 个 .md 文件准备合并...")

    for md_file in md_files:
        # 关键：跳过输出文件本身，防止在重复运行时将自己也合并进去
        if md_file.resolve() == output_file.resolve():
            print(f"  - 跳过输出文件自身: {md_file.name}")
            continue
        if md_file.name in ['funboost_all_docs_and_codes.md','funboost_all_codes.md','boost_spider_all_docs_and_codes_no_md.md']:
            continue

        print(f"  - 正在读取: {md_file.name}")
        try:
            # 读取文件内容
            content = md_file.read_text(encoding='utf-8')
            
            # 创建一个分隔符，包含文件名，方便追溯来源
            separator = f"\n\n---\n\n# Merged from: {md_file.name}\n\n"
            
            # 将分隔符和文件内容一起添加到列表中
            all_contents.append(separator + content)
        except Exception as e:
            print(f"    错误: 读取文件 {md_file.name} 失败: {e}")

    # 5. 将所有内容写入输出文件
    if all_contents:
        # 将列表中的所有元素连接成一个大字符串
        # 注意：第一个文件前也会有一个分隔符，这通常是期望的行为，因为它清晰地标记了内容的开始
        final_content = "".join(all_contents)
        
        # 使用 NBPath.write_text() 写入文件
        output_file.write_text(final_content, encoding='utf-8')
        
        print(f"\n成功！所有 .md 文件已合并到: {output_file}")
        output_file.copy_to(source_dir.parent / 'all_proj_merged_all_md_files.txt')
    else:
        print("\n没有内容被合并。")

# --- 主程序入口 ---
if __name__ == '__main__':
    # 调用函数开始合并
    merge_all_md()


