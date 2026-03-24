#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将所有深层级文件夹下的md文件
D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_md_files

复制到这个目录下，并把md后缀改为txt
D:\codes\nb_ai_context\markdown_gen_files_git_ignore\ai_txt_files

使用 NbPath包
"""

from nb_path import NbPath
import chardet
def copy_md_to_txt(only_md_file:NbPath=None):
    # 定义源目录和目标目录
    source_dir: NbPath = NbPath(__file__).parent / "ai_md_files"
    target_dir: NbPath = NbPath(__file__).parent / "ai_txt_files"
    
    # 确保目标目录存在
    target_dir.ensure_parent().mkdir(exist_ok=True)
    
    # 递归查找所有.md文件
    md_files = source_dir.rglob_files("*.md")
    
    print(f"找到 {len(md_files)} 个.md文件")
    
    # 复制每个文件并更改扩展名
    for md_file in md_files:  
        # if 'nb_time'  not in md_file.name:  
        #     continue
        # 构造目标文件路径，保持相对路径结构
        if only_md_file:
            if only_md_file != md_file:
                continue
        relative_path = md_file.relative_to(source_dir)
        txt_file = (target_dir / relative_path).with_suffix(".txt")

        txt_file.ensure_parent().write_text_with_utf8_bom(md_file.read_text())

        print(f"txt_file {txt_file} chardet_detect: {txt_file.chardet_detect()}")
        print(f"已复制: {md_file} -> {txt_file}")
        
    
    print("完成!")
if __name__ == "__main__":
    copy_md_to_txt()