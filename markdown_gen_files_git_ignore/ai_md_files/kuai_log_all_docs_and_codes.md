# markdown content namespace: kuai_log readme 


## File Tree


```

└── README.md

```

---


## Included Files


- `README.md`


---


### code file start: README.md 

## 1 kuai_log

安装 pip install kuai_log

kuai_log 是最快的python日志,比loguru和logging快30倍.

kuai_log的控制台日志自动彩色.

kuai_log的文件日志多进程切割安全.

kuai_log的文件日志支持更友好的json文件写入,更适合elk采集.(例如logger.info直接记录一个字典,会自动转换)

kuai_log KuaiLogger 对象的方法名和入参在logging.Logger对象中一定存在,且参数相同,虽然不是基于logging开发,但保持了良好的兼容性

### 1.2 为什么用 kuai_log

```
用户怕了logging包的创建logger, 创建handler, handler设置formatter, logger添加handler 的方式,感觉logging复杂,导致用户想用loguru

loguru对logging包的不兼容和复杂.比如loguru记录flask框架的已有日志内容,就比较麻烦,说的是在已有logging命名空间添加handler,loguru困难.
例如loguru记录flask werkzeug 请求记录的日志 ,记录 tornado.access的 日志,麻烦.

```

## 2 性能比较

在 win11 + r7 4800h上,

单进程for for循环写入10万次控制台和文件，（具体的测试代码可以直接用 tests/compare_spped 中的代码验证）

```
loguru 写入文件和打印控制台,10万次日志耗费48秒

logging 写入文件和打印控制台,10万次日志耗费45秒

nb_log 写入文件和打印控制台,10万次日志耗费7秒

kuai_log 写入文件和打印控制台,10万次日志耗费1.7秒
```

## 3 kuai_log 写入 10万次文件和打印控制台代码:

```python
import logging
import time

from kuai_log import get_logger

logger = get_logger(name='test', level=logging.DEBUG, log_filename='t5.log',
                    log_path='/pythonlogs', is_add_file_handler=True,
                    )

t_start = time.time()
for i in range(10):
    logger.debug(i)
print(time.time() - t_start)
```

### 3.2 kuai_log的日志级别和常用的日志是一样的.debug info warning error critical 

```python
import logging
import time

from kuai_log import get_logger

logger = get_logger(name='test77', level=logging.DEBUG, log_filename='t777.log',
                    log_path='/pythonlogs', is_add_file_handler=True,
                    json_log_path='/python_logs_json', is_add_json_file_handler=True,
                    )

t_start = time.time()
for i in range(1):
    logger.debug(i)
    logger.info(i)
    logger.warning(i)
    logger.error(i)
    logger.critical(i)

print(time.time() - t_start)
```

## 4 kuai_log 用法比logging和loguru简单.

### 4.1 有些人问需要实例化生成logger,没有 from loguru import logger直接用爽?

```
因为是每个name的日志行为是独立的,用户在大项目中有很多个日志,不同的表现行为不同,
例如有的函数里面日志界别高才输出,有的模块需要日志级别低就输出,
例如有的模块的日志需要写入文件,有的模块的日志不需要写入文件,
所以用不同的name来区分日志是最好的
```

### 4.2 用户想偷懒,学习loguru直接导入就使用,想不需要手动实例化生成logger

kuai_log 自带一个已经实例化好的 k_logger 对象,你还嫌麻烦?

```python
from kuai_log import k_logger

k_logger.debug('hello')
```

## 5 kuai_log为什么快?

因为logging日志系统功能非常丰富强大,扩展性好,代码较为复杂,kuai_log没有基于logging包来封装,是完全从0写的,代码简单自然就性能好了.

kuai_log实现的文件日志多进程rotate切割安全,使用了特殊的方式,所以技能保证切割不报错又能保证性能.

nb_log是基于logging封装的,kuai_log是手写的.

## 6 kuai_log 日志截图


![a9w0Q.png](https://img.vinua.cn/images/a9w0Q.png)

**code file end: README.md**

---

# markdown content namespace: kuai_log codes 


## File Tree


```

└── kuai_log
    ├── __init__.py
    ├── _datetime.py
    ├── kuai_log_record_logging_namespace.py
    ├── logger.py
    ├── rotate_file_writter.py
    └── stream.py

```

---


## Included Files


- `kuai_log/kuai_log_record_logging_namespace.py`

- `kuai_log/logger.py`

- `kuai_log/rotate_file_writter.py`

- `kuai_log/stream.py`

- `kuai_log/_datetime.py`

- `kuai_log/__init__.py`


---


### code file start: kuai_log/kuai_log_record_logging_namespace.py 

```python



pass
```

**code file end: kuai_log/kuai_log_record_logging_namespace.py**

---


### code file start: kuai_log/logger.py 

```python
import json
import time
import typing
import copy
import datetime
# from tzlocal import get_localzone
import os
import socket
import sys
import threading
import traceback
from enum import Enum
import logging
from functools import partial
from kuai_log._datetime import aware_now
from kuai_log.stream import OsStream
from kuai_log.rotate_file_writter import OsFileWritter


class FormatterFieldEnum(Enum):
    host = 'host'

    asctime = 'asctime'
    name = 'name'
    levelname = 'levelname'
    message = 'message'

    process = 'process'
    thread = 'thread'

    pathname = 'pathname'
    filename = 'filename'
    lineno = 'lineno'
    funcName = 'funcName'
    # click_line = 'click_line'


logger_name__logger_obj_map = {}  # type: typing.Dict[str,KuaiLogger]


# noinspection PyPep8
class KuaiLogger:
    """
    不要手动调用这个类,使用get_logger函数就行了.
    """

    # 获取当前时区
    # current_timezone = get_localzone().zone
    host = socket.gethostname()

    def __init__(self, name, level=logging.DEBUG,
                 is_add_stream_handler=True, is_add_file_handler=False, is_add_json_file_handler=False,
                 log_path=None, json_log_path=None, log_filename=None,
                 max_bytes=1000 * 1000 * 1000, back_count=10,
                 formatter_template='{asctime} - {host} - "{pathname}:{lineno}" - {funcName} - {name} - {levelname} - {message}', ):

        self.name = name
        self.level = level

        self._is_add_stream_handler = is_add_stream_handler
        self._is_add_file_handler = is_add_file_handler
        self._is_add_json_file_handler = is_add_json_file_handler

        self._log_path = log_path
        self._log_filename = log_filename

        if self._is_add_file_handler:
            self._fw = OsFileWritter(log_filename, log_path, max_bytes=max_bytes, back_count=back_count)
        if self._is_add_json_file_handler:
            self._fw_json = OsFileWritter(log_filename, json_log_path, max_bytes=max_bytes, back_count=back_count)

        self._formatter_template = formatter_template
        self._need_fields = self._parse_need_filed()
        # print(self._need_fields)

    def setLevel(self, level):
        """
        Set the specified level on the underlying logger.
        """
        self.level = level

    def _parse_need_filed(self):
        need_fields = set()
        for field in FormatterFieldEnum:
            if '{' + field.value + '}' in self._formatter_template:
                need_fields.add(field.value)
        return need_fields

    def _build_format_kwargs(self, level, msg, stacklevel):
        format_kwargs = {}
        if FormatterFieldEnum.name.value in self._need_fields:
            format_kwargs[FormatterFieldEnum.name.value] = self.name
        if FormatterFieldEnum.levelname.value in self._need_fields:
            format_kwargs[FormatterFieldEnum.levelname.value] = logging._levelToName[level]  # noqa
        if FormatterFieldEnum.message.value in self._need_fields:
            format_kwargs[FormatterFieldEnum.message.value] = msg

        if (
                FormatterFieldEnum.pathname.value in self._need_fields or
                FormatterFieldEnum.filename.value in self._need_fields or
                FormatterFieldEnum.funcName.value in self._need_fields):
            fra = sys._getframe(stacklevel)  # noqa
            lineno = fra.f_lineno
            pathname = fra.f_code.co_filename  # type :str
            filename = pathname.split('/')[-1].split('\\')[-1]
            # noinspection PyPep8Naming
            funcName = fra.f_code.co_name
            if FormatterFieldEnum.pathname.value in self._need_fields:
                format_kwargs[FormatterFieldEnum.pathname.value] = pathname
            if FormatterFieldEnum.filename.value in self._need_fields:
                format_kwargs[FormatterFieldEnum.filename.value] = filename
            if FormatterFieldEnum.lineno.value in self._need_fields:
                format_kwargs[FormatterFieldEnum.lineno.value] = lineno
            if FormatterFieldEnum.funcName.value in self._need_fields:
                format_kwargs[FormatterFieldEnum.funcName.value] = funcName

        if f'{FormatterFieldEnum.process.value}' in self._need_fields:
            format_kwargs[FormatterFieldEnum.process.value] = os.getgid()
        if f'{FormatterFieldEnum.thread.value}' in self._need_fields:
            format_kwargs[FormatterFieldEnum.thread.value] = threading.get_ident()
        if FormatterFieldEnum.asctime.value in self._need_fields:
            # format_kwargs[FormatterFieldEnum.asctime.value] = datetime.datetime.now().strftime(
            #     f"%Y-%m-%d %H:%M:%S.%f {self.current_timezone}")
            format_kwargs[FormatterFieldEnum.asctime.value] = aware_now()
        if FormatterFieldEnum.host.value in self._need_fields:
            format_kwargs[FormatterFieldEnum.host.value] = self.host
        return format_kwargs

    def log(self, level, msg, args=None, exc_info=None, extra=None, stack_info=False, stacklevel=3):
        # def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):

        if self.level > level:
            return
        msg = msg%args
        format_kwargs = self._build_format_kwargs(level, msg, stacklevel)
        # print(self._formatter_template)
        # print(format_kwargs)
        format_kwargs_json = {}
        if self._is_add_json_file_handler:
            format_kwargs_json = copy.copy(format_kwargs)
            format_kwargs_json['asctime'] = str(format_kwargs_json['asctime'])
            format_kwargs_json['msg'] = {}
            if isinstance(msg, dict):
                format_kwargs_json['msg'].update(msg)
                format_kwargs_json['message'] = ''
            if extra:
                format_kwargs_json['msg'].update(extra)
            if exc_info:
                format_kwargs_json['msg'].update({'traceback': traceback.format_exc()})
        if extra:
            format_kwargs.update(extra)
        msg_format = self._formatter_template.format(**format_kwargs)
        if exc_info:
            msg_format += f'\n {traceback.format_exc()}'
        msg_color = self._add_color(msg_format, level)
        # print(msg_format)
        # print(msg)
        if self._is_add_stream_handler:
            OsStream.stdout(msg_color + '\n')
        if self._is_add_file_handler:
            self._fw.write_2_file(msg_format +'\n')
        if self._is_add_json_file_handler:
            self._fw_json.write_2_file(json.dumps(format_kwargs_json, ensure_ascii=False) + '\n')

    @staticmethod
    def _add_color(complete_msg, record_level):
        if record_level == logging.DEBUG:
            # msg_color = ('\033[0;32m%s\033[0m' % msg)  # 绿色
            # print(msg1)
            msg_color = f'\033[0;32m{complete_msg}\033[0m'  # 绿色
        elif record_level == logging.INFO:
            # msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, self.bule, msg))  # 青蓝色 36    96
            msg_color = f'\033[0;36m{complete_msg}\033[0m'
        elif record_level == logging.WARNING:
            # msg_color = ('\033[%s;%sm%s\033[0m' % (self._display_method, self.yellow, msg))
            msg_color = f'\033[0;33m{complete_msg}\033[0m'
        elif record_level == logging.ERROR:
            # msg_color = ('\033[%s;35m%s\033[0m' % (self._display_method, msg))  # 紫红色
            msg_color = f'\033[0;35m{complete_msg}\033[0m'
        elif record_level == logging.CRITICAL:
            # msg_color = ('\033[%s;31m%s\033[0m' % (self._display_method, msg))  # 血红色
            msg_color = f'\033[0;31m{complete_msg}\033[0m'
        else:
            msg_color = f'{complete_msg}'
        return msg_color

    def debug(self, msg, *args, **kwargs):
        self.log(logging.DEBUG, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs, exc_info=True)

    def critical(self, msg, *args, **kwargs):
        self.log(logging.CRITICAL, msg, *args, **kwargs)


# noinspection PyPep8
def get_logger(name, level=logging.DEBUG,
               is_add_stream_handler=True, is_add_file_handler=False, is_add_json_file_handler=False,
               log_path=None, json_log_path=None, log_filename=None,
               max_bytes=1000 * 1000 * 1000, back_count=10,
               formatter_template='{asctime} - {host} - "{pathname}:{lineno}" - {funcName} - {name} - {levelname} - {message}'):
    local_params = copy.copy(locals())
    if name in logger_name__logger_obj_map:
        print(f'已存在该命名空间 {name} 日志')
        logger = logger_name__logger_obj_map[name]
        logger.level = level
    else:
        logger = KuaiLogger(**local_params)
        logger_name__logger_obj_map[name] = logger
    raw_logger = logging.getLogger(name)
    raw_logger.setLevel(level)
    raw_logger.handlers = []
    raw_logger._log = logger.log # 这是对logging包的日志记录,转移到kuai_log来记录.
    raw_logger.log = partial(logger.log, stacklevel=2)
    return logger


if __name__ == '__main__':
    pass

```

**code file end: kuai_log/logger.py**

---


### code file start: kuai_log/rotate_file_writter.py 

```python
import atexit
import multiprocessing
import queue
import threading
import typing
from pathlib import Path
import time
import os


# from nb_log.simple_print import sprint as print  # 在此模块中不能print，print会写入文件，文件中print又写入文件，无限懵逼死循环。


def build_current_date_str():
    return time.strftime('%Y-%m-%d')


class FileWritter:
    _lock = threading.RLock()

    def __init__(self, file_name: str, log_path='/pythonlogs', max_bytes=1000 * 1000 * 1000, back_count=10):
        self._max_bytes = max_bytes
        self._back_count = back_count
        self.need_write_2_file = True if file_name else False
        if self.need_write_2_file:
            self._file_name = file_name
            self.log_path = log_path
            if not Path(self.log_path).exists():
                print(f'自动创建日志文件夹 {log_path}')
                Path(self.log_path).mkdir(exist_ok=True)
            self._open_file()
            self._last_write_ts = 0
            self._last_del_old_files_ts = 0

    @property
    def file_path(self):
        f_list = []
        for f in Path(self.log_path).glob(f'????-??-??.????.{self._file_name}'):
            f_list.append(f)
        sn_list = []
        for f in f_list:
            if f'{build_current_date_str()}.' in f.name:
                sn = f.name.split('.')[1]
                sn_list.append(sn)
        if not sn_list:
            return Path(self.log_path) / Path(f'{build_current_date_str()}.0001.{self._file_name}')
        else:
            sn_max = max(sn_list)
            if (Path(self.log_path) / Path(f'{build_current_date_str()}.{sn_max}.{self._file_name}')).stat().st_size > self._max_bytes:
                new_sn_int = int(sn_max) + 1
                new_sn_str = str(new_sn_int).zfill(4)
                return Path(self.log_path) / Path(f'{build_current_date_str()}.{new_sn_str}.{self._file_name}')
            else:
                return Path(self.log_path) / Path(f'{build_current_date_str()}.{sn_max}.{self._file_name}')

    def _open_file(self):
        self._f = open(self.file_path, encoding='utf8', mode='a')

    def _close_file(self):
        self._f.close()

    def write_2_file(self, msg):
        if self.need_write_2_file:
            with self._lock:
                now_ts = time.time()
                if now_ts - self._last_write_ts > 10:
                    self._last_write_ts = time.time()
                    self._close_file()
                    self._open_file()
                self._f.write(msg)
                self._f.flush()
                if now_ts - self._last_del_old_files_ts > 30:
                    self._last_del_old_files_ts = time.time()
                    self._delete_old_files()

    def _delete_old_files(self):
        f_list = []
        for f in Path(self.log_path).glob(f'????-??-??.????.{self._file_name}'):
            f_list.append(f)
        # f_list.sort(key=lambda f:f.stat().st_mtime,reverse=True)
        f_list.sort(key=lambda f: f.name, reverse=True)
        for f in f_list[self._back_count:]:
            try:
                # print(f'删除 {f} ') # 这里不能print， stdout写入文件，写入文件时候print，死循环
                f.unlink()
            except (FileNotFoundError, PermissionError):
                pass


class BulkFileWritter:
    _lock = threading.Lock()

    filename__queue_map = {}
    filename__options_map = {}
    filename__file_writter_map = {}

    _get_queue_lock = threading.Lock()

    _has_start_bulk_write = False

    @classmethod
    def _get_queue(cls, file_name):
        if file_name not in cls.filename__queue_map:
            cls.filename__queue_map[file_name] = queue.SimpleQueue()
        return cls.filename__queue_map[file_name]

    @classmethod
    def _get_file_writter(cls, file_name):
        if file_name not in cls.filename__file_writter_map:
            fw = FileWritter(**cls.filename__options_map[file_name])
            cls.filename__file_writter_map[file_name] = fw
        return cls.filename__file_writter_map[file_name]

    def __init__(self, file_name: typing.Optional[str], log_path='/pythonlogs', max_bytes=1000 * 1000 * 1000, back_count=10):
        self.need_write_2_file = True if file_name else False
        self._file_name_key = (log_path,file_name)
        if file_name:
            self.__class__.filename__options_map[self._file_name_key] = {
                'file_name': file_name,
                'log_path': log_path,
                'max_bytes': max_bytes,
                'back_count': back_count,
            }
            self.start_bulk_write()

    def write_2_file(self, msg):
        if self.need_write_2_file:
            with self._lock:
                self._get_queue(self._file_name_key).put(msg)

    @classmethod
    def _bulk_real_write(cls):
        with cls._lock:
            for _file_name, queue in cls.filename__queue_map.items():
                msg_str_all = ''
                while not queue.empty():
                    msg_str_all += str(queue.get())
                if msg_str_all:
                    cls._get_file_writter(_file_name).write_2_file(msg_str_all)

    @classmethod
    def _when_exit(cls):
        # print('结束')
        return cls._bulk_real_write()

    @classmethod
    def start_bulk_write(cls):
        def _bulk_write():
            while 1:
                cls._bulk_real_write()
                time.sleep(0.1)

        if not cls._has_start_bulk_write:
            cls._has_start_bulk_write = True
            threading.Thread(target=_bulk_write, daemon=True).start()


atexit.register(BulkFileWritter._when_exit)

OsFileWritter = FileWritter if os.name == 'posix' else BulkFileWritter


def tt():
    fw = OsFileWritter('test_file6.log', '/test_dir2', max_bytes=1000 * 100)
    t1 = time.time()
    for i in range(10000):
        # time.sleep(0.001)
        msg = f'yyy{str(i).zfill(5)}' * 4
        print(msg)
        fw.write_2_file(msg + '\n')
    print(time.time() - t1)


if __name__ == '__main__':
    multiprocessing.Process(target=tt).start()
    multiprocessing.Process(target=tt).start()
    # tt()

```

**code file end: kuai_log/rotate_file_writter.py**

---


### code file start: kuai_log/stream.py 

```python
import datetime
import os
import queue
import sys
import threading
import time
import atexit

from kuai_log._datetime import aware_now


class Stream:
    @classmethod
    def stdout(cls, msg):
        print(msg)

    @classmethod
    def print(cls, *args, sep=' ', end='\n', file=None, flush=True, sys_getframe_n=2):
        args = (str(arg) for arg in args)  # REMIND 防止是数字不能被join
        msg = sep.join(args) + end
        print(msg)

class BulkStream:
    q = queue.SimpleQueue()
    _lock = threading.Lock()
    _has_start_bulk_stdout = False

    @classmethod
    def _bulk_real_stdout(cls):
        with cls._lock:
            msg_str_all = ''
            while not cls.q.empty():
                msg_str_all += str(cls.q.get())
            if msg_str_all:
                sys.stdout.write(msg_str_all)

    @classmethod
    def stdout(cls, msg):
        with cls._lock:
            cls.q.put(msg)

    @classmethod
    def print(cls, *args, sep=' ', end='\n', file=None, flush=True, sys_getframe_n=2):
        args = (str(arg) for arg in args)  # REMIND 防止是数字不能被join
        msg = sep.join(args) + end
        fra = sys._getframe(1)  # noqa
        line = fra.f_lineno
        full_path = fra.f_code.co_filename  # type :str
        # file_name = full_path.split('/')[-1].split('\\')[-1]
        full_path_and_line = f'"{full_path}:{line}"'
        fun = fra.f_code.co_name
        full_msg = f'{aware_now()} - {full_path_and_line} - {fun} - [print] - {msg}'
        color_msg = f'\033[0;34m{full_msg}\033[0m'
        with cls._lock:
            cls.q.put(color_msg)

    @classmethod
    def _when_exit(cls):
        # stdout_raw('结束 stdout_raw')
        return cls._bulk_real_stdout()

    @classmethod
    def start_bulk_stdout(cls):
        def _bulk_stdout():
            while 1:
                cls._bulk_real_stdout()
                time.sleep(0.1)

        if not cls._has_start_bulk_stdout:
            cls._has_start_bulk_write = True
            threading.Thread(target=_bulk_stdout, daemon=True).start()

    @classmethod
    def patch_print(cls):
        """
        Python有几个namespace，分别是

        locals

        globals

        builtin

        其中定义在函数内声明的变量属于locals，而模块内定义的函数属于globals。


        https://codeday.me/bug/20180929/266673.html   python – 为什么__builtins__既是模块又是dict

        :return:
        """
        try:
            __builtins__.print = cls.print
        except AttributeError:
            """
            <class 'AttributeError'>
            'dict' object has no attribute 'print'
            """
            # noinspection PyUnresolvedReferences
            __builtins__['print'] = cls.print
        # traceback.print_exception = print_exception  # file类型为 <_io.StringIO object at 0x00000264F2F065E8> 单独判断，解决了，不要加这个。

OsStream = Stream


if os.name == 'nt':  # windows io性能差
    OsStream = BulkStream
    BulkStream.start_bulk_stdout()
    BulkStream.patch_print()
    atexit.register(BulkStream._when_exit)

```

**code file end: kuai_log/stream.py**

---


### code file start: kuai_log/_datetime.py 

```python

import re
import sys
from calendar import day_abbr, day_name, month_abbr, month_name
from datetime import datetime as datetime_
from datetime import timedelta, timezone
from time import localtime, strftime

tokens = r"H{1,2}|h{1,2}|m{1,2}|s{1,2}|S{1,6}|YYYY|YY|M{1,4}|D{1,4}|Z{1,2}|zz|A|X|x|E|Q|dddd|ddd|d"

pattern = re.compile(r"(?:{0})|\[(?:{0}|!UTC)\]".format(tokens))


class datetime(datetime_):  # noqa: N801
    def __format__(self, spec):
        if spec.endswith("!UTC"):
            dt = self.astimezone(timezone.utc)
            spec = spec[:-4]
        else:
            dt = self

        if not spec:
            spec = "%Y-%m-%dT%H:%M:%S.%f%z"

        if "%" in spec:
            return datetime_.__format__(dt, spec)

        year, month, day, hour, minute, second, weekday, yearday, _ = dt.timetuple()
        microsecond = dt.microsecond
        timestamp = dt.timestamp()
        tzinfo = dt.tzinfo or timezone(timedelta(seconds=0))
        offset = tzinfo.utcoffset(dt).total_seconds()
        sign = ("-", "+")[offset >= 0]
        h, m = divmod(abs(offset // 60), 60)

        rep = {
            "YYYY": "%04d" % year,
            "YY": "%02d" % (year % 100),
            "Q": "%d" % ((month - 1) // 3 + 1),
            "MMMM": month_name[month],
            "MMM": month_abbr[month],
            "MM": "%02d" % month,
            "M": "%d" % month,
            "DDDD": "%03d" % yearday,
            "DDD": "%d" % yearday,
            "DD": "%02d" % day,
            "D": "%d" % day,
            "dddd": day_name[weekday],
            "ddd": day_abbr[weekday],
            "d": "%d" % weekday,
            "E": "%d" % (weekday + 1),
            "HH": "%02d" % hour,
            "H": "%d" % hour,
            "hh": "%02d" % ((hour - 1) % 12 + 1),
            "h": "%d" % ((hour - 1) % 12 + 1),
            "mm": "%02d" % minute,
            "m": "%d" % minute,
            "ss": "%02d" % second,
            "s": "%d" % second,
            "S": "%d" % (microsecond // 100000),
            "SS": "%02d" % (microsecond // 10000),
            "SSS": "%03d" % (microsecond // 1000),
            "SSSS": "%04d" % (microsecond // 100),
            "SSSSS": "%05d" % (microsecond // 10),
            "SSSSSS": "%06d" % microsecond,
            "A": ("AM", "PM")[hour // 12],
            "Z": "%s%02d:%02d" % (sign, h, m),
            "ZZ": "%s%02d%02d" % (sign, h, m),
            "zz": tzinfo.tzname(dt) or "",
            "X": "%d" % timestamp,
            "x": "%d" % (int(timestamp) * 1000000 + microsecond),
        }
        def get(m):
            try:
                return rep[m.group(0)]
            except KeyError:
                return m.group(0)[1:-1]
        return pattern.sub(get, spec)


def aware_now():
    now = datetime_.now()
    timestamp = now.timestamp()
    local = localtime(timestamp)

    try:
        seconds = local.tm_gmtoff
        zone = local.tm_zone
    except AttributeError:
        offset = datetime_.fromtimestamp(timestamp) - datetime_.utcfromtimestamp(timestamp)
        seconds = offset.total_seconds()
        zone = strftime("%Z")

    tzinfo = timezone(timedelta(seconds=seconds), zone)

    return datetime.combine(now.date(), now.time().replace(tzinfo=tzinfo))

```

**code file end: kuai_log/_datetime.py**

---


### code file start: kuai_log/__init__.py 

```python


import logging
from .logger import get_logger

k_logger = get_logger('kuai_logger')
```

**code file end: kuai_log/__init__.py**

---

