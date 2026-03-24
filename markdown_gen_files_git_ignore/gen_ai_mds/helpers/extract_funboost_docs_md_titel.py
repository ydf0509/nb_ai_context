import os
import re
from pathlib import Path
from typing import Dict, List


def extract_headings_above_level4(folder_path: str) -> Dict[str, List[tuple]]:
    """
    提取指定文件夹下所有markdown文件中4级及以上的标题（# 到 ####，即1-4级）
    
    Args:
        folder_path: 文件夹路径
        
    Returns:
        字典，key为文件名，value为标题列表，每个元素为(行号, 标题级别, 标题内容)的元组
    """
    result = {}
    folder = Path(folder_path)
    
    if not folder.exists():
        return result
    
    pattern = re.compile(r'^(#{1,4})\s+(.+)$')
    code_block_pattern = re.compile(r'^```')
    
    for md_file in folder.glob('*.md'):
        headings = []
        in_code_block = False
        
        with open(md_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                if code_block_pattern.match(line):
                    in_code_block = not in_code_block
                    continue
                
                if in_code_block:
                    continue
                
                match = pattern.match(line)
                if match:
                    level = len(match.group(1))
                    title = match.group(2).strip()
                    headings.append((line_num, level, title))
        
        if headings:
            result[md_file.name] = headings
    
    return result


def collect_headings(folder_path: str) -> List[str]:
    """
    收集指定文件夹下所有markdown文件中4级及以上的标题到列表
    
    Returns:
        包含所有输出内容的列表
    """
    output_list = []
    headings_dict = extract_headings_above_level4(folder_path)
    
    if not headings_dict:
        output_list.append("未找到任何4级及以上的标题")
        return output_list
    
    for filename, headings in headings_dict.items():
        output_list.append(f"\n{'='*60}")
        output_list.append(f"文件: {filename}")
        output_list.append(f"{'='*60}")
        for line_num, level, title in headings:
            indent = "  " * (level - 4)
            output_list.append(f"  行{line_num}: {'#' * level} {title}")
    
    return output_list


def get_funboost_docs_md_titles() -> List[str]:
    """
    获取指定文件夹下所有markdown文件中4级及以上的标题
    
    Returns:
        包含所有标题的列表
    """
    folder = r'd:\codes\funboost_docs\source\articles'
    result_list = collect_headings(folder)
    
    # 打印查看结果
    # for line in result_list:
    #     print(line)
        
    print(f"\n\n总共收集了 {len(result_list)} 行输出")
    # 合并成一个大字符串（如果需要）
    big_string = '\n'.join(result_list)
    return big_string


if __name__ == '__main__':
    titles = get_funboost_docs_md_titles()
    print(titles)
    
    
    
