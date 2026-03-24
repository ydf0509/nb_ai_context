# markdown content namespace: nb_print readme 


## File Tree


```

└── README.md

```

---


## Included Files


- `README.md`


---


### code file start: README.md 

# nb_print

**一次导入，自动改变所有print效果，可在控制台输出内容中点击跳转打开实际print的地方**

[![pypi](https://img.shields.io/pypi/v/nb-print.svg)](https://pypi.org/project/nb-print)
[![versions](https://img.shields.io/pypi/pyversions/nb-print.svg)](https://pypi.org/project/very-nb-print)
[![license](https://img.shields.io/pypi/l/nb-print.svg)](https://pypi.org/project/very-nb-print)

**`nb_print`：让你的 `print()` "活" 起来，一键跳转到代码位置。**

在大型项目或遗留代码中进行调试时，你是否曾被满屏的 `print` 输出所困扰，苦苦寻找 "这行输出究竟是哪里打印的？，什么时候打印的" `nb_print` 正是为解决这一痛点而生。

在调试项目和三方库时候，你也可以加print，替代断点debug。

它通过极简的方式，增强了 Python 内置的 `print` 函数，让你的每一次打印输出都附带源码位置的超链接和打印的时间。

---

## ✨ 核心功能

- **🚀 无感植入**: 只需在项目入口 `import nb_print` 一次，无需修改任何现有 `print` 代码，即可全局生效。
- **🖱️ 点击跳转**: 在 PyCharm, VSCode 等现代 IDE 的控制台中，点击输出前缀即可直接跳转到发起 `print` 的确切代码行。
- **🎨 智能美化**: 打印内容自动有色块和颜色。
- **🎯 解决痛点**: 彻底告别大海捞针式的 `print` 调试，极大提升开发和排错效率。
- **自带时间**： 自动添加是什么时间打印的

## 📦 pip安装

```bash
pip install very-nb-print
```

注意是安装 very-nb-print ，因为 nb_print 名字因为和其他包相似度高，不被pypi允许

## 🚀 使用方法

在你的项目主入口文件（例如 `main.py` 或 `app.py`）的顶部，加入一行导入语句即可。

```python
print('导入nb_print之前，这行print是原始的')

import nb_print

print('导入nb_print之后，这行print自动强化了')
```

**控制台打印是这样**
```shell
导入nb_print之前，这行print是原始的
2025-06-26 14:00:41  "d:/codes/nb_print/tests/nb_print_demo.py:5" -<module>-[print]-  导入nb_print之后，这行print自动强化了
```

**控制台图片效果**
![alt text](image.png)

## 🛠️ 工作原理

`nb_print` 的实现非常轻量，其核心原理是 **"猴子补丁" (Monkey Patching)**。

当 `import nb_print` 时，它会用一个自定义的函数替换掉 Python `builtins` 模块中的原生 `print` 函数。


## 🤝 贡献

欢迎通过提交 Issues 和 Pull Requests 来贡献代码、报告问题或提出功能建议。

## 📄 许可证

本项目基于 MIT License 开源。

**code file end: README.md**

---

# markdown content namespace: nb_print codes 


## File Tree


```

└── nb_print
    └── __init__.py

```

---


## Included Files


- `nb_print/__init__.py`


---


### code file start: nb_print/__init__.py 

```python
# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2022/5/9 19:02
"""
不直接给print打补丁，自己重新赋值。

"""
import multiprocessing
import os
import sys
import time
import traceback


print_raw = print


def stdout_write(msg: str):
    if sys.stdout:
        sys.stdout.write(msg)
        sys.stdout.flush()


def stderr_write(msg: str):
    '''打包exe运行或者做成windwos services 这些情况下情况下,sys.stderr是None,None.write会报错'''
    if sys.stderr:
        sys.stderr.write(msg)
        sys.stderr.flush()
    else:
        stdout_write(msg)


WORD_COLOR = 37

def _print_with_file_line(*args, sep=' ', end='\n', file=None, flush=True, sys_getframe_n=2):
    args = (str(arg) for arg in args)  # REMIND 防止是数字不能被join
    args_str = sep.join(args) + end
    # stdout_write(f'56:{file}')
    if file == sys.stderr:
        stderr_write(args_str)  # 如 threading 模块第926行，打印线程错误，希望保持原始的红色错误方式，不希望转成蓝色。
    elif file in [sys.stdout, None]:
        # 获取被调用函数在被调用时所处代码行数
        fra = sys._getframe(sys_getframe_n)
        line = fra.f_lineno
        file_name = fra.f_code.co_filename
        fun = fra.f_code.co_name
        now_str= time.strftime("%Y-%m-%d %H:%M:%S")
        # mtime = time.gmtime()
        # now_str = f'{mtime.tm_year}-{mtime.tm_mon}-{mtime.tm_mday} {mtime.tm_hour}:{mtime.tm_min}:{mtime.tm_sec}'
        # sys.stdout.write(f'"{__file__}:{sys._getframe().f_lineno}"    {x}\n')
        # if nb_log_config_default.DEFAULUT_USE_COLOR_HANDLER:
        #     if nb_log_config_default.DISPLAY_BACKGROUD_COLOR_IN_CONSOLE:
        #         stdout_write(f'\033[0;34m{now_str}  "{file_name}:{line}" -{fun}-[print]-  \033[0;{WORD_COLOR};44m{args_str[:-1]}\033[0m \033[0m\n')  # 36  93 96 94
        #     else:
        #         stdout_write(
        #             f'\033[0;{WORD_COLOR};34m{now_str}  "{file_name}:{line}" -{fun}-[print]-  {args_str[:-1]}  \033[0m\n')  # 36  93 96 94
        #     # sys.stdout.write(f'\033[0;30;44m"{file_name}:{line}"  {time.strftime("%H:%M:%S")}  {"".join(args)}\033[0m\n')
        # else:
        #     stdout_write(
        #         f'{now_str}  "{file_name}:{line}"  -{fun}-[print]- {args_str} ')
        stdout_write(f'\033[0;34m{now_str}  "{file_name}:{line}" -{fun}-[print]-  \033[0;{WORD_COLOR};44m{args_str[:-1]}\033[0m \033[0m\n')  # 36  93 96 94
        
    else:  # 例如traceback模块的print_exception函数 file的入参是   <_io.StringIO object at 0x00000264F2F065E8>，必须把内容重定向到这个对象里面，否则exception日志记录不了错误堆栈。
        print_raw(args_str, sep=sep, end=end, file=file)



# noinspection PyProtectedMember,PyUnusedLocal,PyIncorrectDocstring,DuplicatedCode
def nb_print(*args, sep=' ', end='\n', file=None, flush=True):
    """
    超流弊的print补丁
    :param x:
    :return:
    """
    _print_with_file_line(*args, sep=sep, end=end, file=file, flush=flush, sys_getframe_n=2)


# noinspection PyPep8,PyUnusedLocal
def print_exception(etype, value, tb, limit=None, file=None, chain=True):
    """
    避免每行有两个可跳转的，导致第二个可跳转的不被ide识别。
    主要是针对print_exception，logging.exception里面会调用这个函数。

    # traceback.print_exception = print_exception  # file类型为 <_io.StringIO object at 0x00000264F2F065E8> 单独判断sys.stderr sys.stdout 以外的情况了，解决了，不需要用到p rint_exception。

    :param etype:
    :param value:
    :param tb:
    :param limit:
    :param file:
    :param chain:
    :return:
    """
    if file is None:
        file = sys.stderr
    for line in traceback.TracebackException(
        type(value), value, tb, limit=limit).format(chain=chain):
        # print(line, file=file, end="")
        if file != sys.stderr:
            stderr_write(f'{line} \n')
        else:
            stdout_write(f'{line} \n')


# print = nb_print

def patch_print():
    """
    Python有几个namespace，分别是

    locals

    globals

    builtin

    其中定义在函数内声明的变量属于locals，而模块内定义的函数属于globals。


    https://codeday.me/bug/20180929/266673.html   python – 为什么__builtins__既是模块又是dict

    :return:
    """
    if os.environ.get('has_patch_print'):
        return
    os.environ['has_patch_print'] = '1'

    try:
        __builtins__.print = nb_print
    except AttributeError:
        """
        <class 'AttributeError'>
        'dict' object has no attribute 'print'
        """
        # noinspection PyUnresolvedReferences
        __builtins__['print'] = nb_print
    # traceback.print_exception = print_exception  # file类型为 <_io.StringIO object at 0x00000264F2F065E8> 单独判断，解决了，不要加这个。


# def common_print(*args, sep=' ', end='\n', file=None):
#     args = (str(arg) for arg in args)
#     args = (str(arg) for arg in args)  # REMIND 防止是数字不能被join
#     if file == sys.stderr:
#         stderr_write(sep.join(args) + end)  # 如 threading 模块第926行，打印线程错误，希望保持原始的红色错误方式，不希望转成蓝色。
#     else:
#         stdout_write(sep.join(args) + end)


def reverse_patch_print():
    """
    提供一个反猴子补丁，恢复print原状
    :return:
    """
    # try:
    #     __builtins__.print = common_print
    # except AttributeError:
    #     __builtins__['print'] = common_print

    try:
        __builtins__.print = print_raw
    except AttributeError:
        __builtins__['print'] = print_raw


def is_main_process():
    return multiprocessing.process.current_process().name == 'MainProcess'


# noinspection DuplicatedCode
def only_print_on_main_process(*args, sep=' ', end='\n', file=None, flush=True):
    # 获取被调用函数在被调用时所处代码行数
    if is_main_process():
        _print_with_file_line(*args, sep=sep, end=end, file=file, flush=flush, sys_getframe_n=2)



patch_print()


if __name__ == '__main__':
    print('before patch')
    patch_print()
    print(0)
    nb_print(123, 'abc')
    print(456, 'def')
    print('http://www.baidu.com')

    reverse_patch_print()
    print_raw('hi')

    import logging

    try:
        1 / 0
    except Exception as e:
        traceback.print_exception()

```

**code file end: nb_print/__init__.py**

---

