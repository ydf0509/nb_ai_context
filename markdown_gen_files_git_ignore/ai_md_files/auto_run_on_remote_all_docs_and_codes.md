# markdown content namespace: auto_run_on_remote readme 


## File Tree


```

└── README.md

```

---


## Included Files


- `README.md`


---


### code file start: README.md 

# 1 安装

pip install auto_run_on_remote

# 2 auto_run_on_remote 介绍

```
全名字含义应该是 auto_run_current_python_script_on_remote_server

在本机运行脚本自动在远程机器上运行。

自动上传文件夹 自动创建文件夹 自动远程机器上运行python脚本。
原理是 run_current_script_on_remote() 函数中自动利用 sys._getframe(1).f_code.co_filename 获取当前文件位置，所以不用传参告诉函数当前脚本的位置。

比pycahrm专业版复杂的配置调用远程python解释器更方便，因为pycahrm专业版如果设置了远程解释器启动脚本时候很卡，
启动ide界面更卡，因为ide会去读远程解释器的所有安装的python包，真的是太卡了。
而这个在远程运行启动速度就很快，丝毫不会造成ide卡顿。
还有就是破解最新版pycahrm麻烦老失效，用社区版就好了
```

# 3 用法如下
```
在项目的任意目录层级下的脚本中运行 run_current_script_on_remote(),则脚本会自动运行在远程机器。
当第一次运行脚本时候，会自动在你当项目的根目录生成 auto_run_on_remote_config.py 配置文件，然后，你自己按需修改其中的值。
以后运行run_current_script_on_remote()会自动读取到 auto_run_on_remote_config.py  中的配置。
```

```python
import time
import sys

from auto_run_on_remote import run_current_script_on_remote


run_current_script_on_remote()
# 以下的代码的print都不是在当前机器打印的，是在远程机器上打印的。

for i in range(10):
    print(f'嘻嘻 {i},通过文件路径和python解释器路径，可以发现这句话是在远程机器打印出来的, {__file__} ,{sys.executable} ')
    time.sleep(1)

```



代码运行截图，我本机是win10，可以看到代码是运行在linux的。
[![hXvZff.png](https://z3.ax1x.com/2021/09/10/hXvZff.png)](https://imgtu.com/i/hXvZff)


# 4 配置文件 auto_run_on_remote_config.py 介绍
```python
"""
这个配置文件是自动生成到你的项目根目录的。
"""

import sys

# 项目根目录文件夹，这个一般不需要改，会根据PYTHONPATH智能获取。
# pycahrm自动添加了项目根目录到第一个PYTHONPATH，如果是cmd命令启动这先设置PYTHONPATH环境变量。
# windows设置  set PYTHONPATH=你当前python项目根目录,然后敲击你的python运行命令
# linux设置    export PYTHONPATH=你当前python项目根目录,然后敲击你的python运行命令
PYTHON_PROJ_DIR_LOCAL = sys.path[1]

# 这是远程机器的账号密码配置。把这个配置文件加到gitignore就不会泄漏了。
HOST = '192.168.6.133'
PORT = 22
USER = 'ydf'
PASSWORD = '123456'

PYTHON_INTERPRETER = 'python3'  # 如果你安装了四五个python环境，可以直接指定远程解释器的绝对路径  例如 /opt/minicondadir/ens/env35/python

FORBID_DEPLOY_FROM_LINUX = True # 一般生产机器是linux，是否禁止从linux部署到别的机器，这样可以防止你从生产环境远程到测试环境，配置后，即使生产环境的代码有远程部署，也不会执行远程部署而是直接运行。

# 上传文件夹的配置，具体可以看paramiko_util.py里面的代码。
PATH_PATTERN_EXLUDED_TUPLE = ('/.git/', '/.idea/', '/dist/', '/build/')  # 路径中如果有这些就自动过滤不上传
FILE_SUFFIX_TUPLE_EXLUDED = ('.pyc', '.log', '.gz')  # 这些后缀的文件不上传
ONLY_UPLOAD_WITHIN_THE_LAST_MODIFY_TIME = 3650 * 24 * 60 * 60  # 只有在这个时间之内修改的文件才上传。如果项目比较大，可以第一次完整上传，之后再把这个时间改小。
FILE_VOLUME_LIMIT = 1000 * 1000  # 大于这个体积的文件不上传，单位b。
SFTP_LOG_LEVEL = 20  # 文件夹上传时候的日志级别。10 logging.DEBUG ,20 logging.INFO 30 logging.WaRNING,如果要看为什么某个文件上传失败，可以设置debug级别。

EXTRA_SHELL_STR = ''  # 远程执行命令之前，可以自定义执行的shell语句，一般例如可以设置啥环境变量什么的。


```


**code file end: README.md**

---

# markdown content namespace: auto_run_on_remote codes 


## File Tree


```

└── auto_run_on_remote
    ├── __init__.py
    ├── paramiko_util.py
    ├── remote_config.py
    ├── run_script_on_remote_server.py
    └── set_config.py

```

---


## Included Files


- `auto_run_on_remote/paramiko_util.py`

- `auto_run_on_remote/remote_config.py`

- `auto_run_on_remote/run_script_on_remote_server.py`

- `auto_run_on_remote/set_config.py`

- `auto_run_on_remote/__init__.py`


---


### code file start: auto_run_on_remote/paramiko_util.py 

```python
import os
import re
import sys
import time
from nb_log import LoggerMixin, LoggerLevelSetterMixin
import paramiko


class ParamikoFolderUploader(LoggerMixin, LoggerLevelSetterMixin):
    """
    paramoki 实现的文件夹上传
    """

    def __init__(self, host, port, user, password, local_dir: str, remote_dir: str,
                 path_pattern_exluded_tuple=('/.git/', '/.idea/',),
                 file_suffix_tuple_exluded=('.pyc', '.log', '.gz'),
                 only_upload_within_the_last_modify_time=3650 * 24 * 60 * 60,
                 file_volume_limit=1000 * 1000, sftp_log_level=10):
        """

        :param host:
        :param port:
        :param user:
        :param password:
        :param local_dir:
        :param remote_dir:
        :param path_pattern_exluded_tuple: 命中了这些正则的直接排除
        :param file_suffix_tuple_exluded: 这些结尾的文件排除
        :param only_upload_within_the_last_modify_time: 仅仅上传最近多少天修改的文件
        :param file_volume_limit: 大于这个体积的不上传，单位b。
        :param sftp_log_level:日志级别
        """
        self._host = host
        self._port = port
        self._user = user
        self._password = password

        self._local_dir = str(local_dir).replace('\\', '/')
        if not self._local_dir.endswith('/'):
            self._local_dir += '/'
        self._remote_dir = str(remote_dir).replace('\\', '/')
        if not self._remote_dir.endswith('/'):
            self._remote_dir += '/'
        self._path_pattern_exluded_tuple = path_pattern_exluded_tuple
        self._file_suffix_tuple_exluded = file_suffix_tuple_exluded
        self._only_upload_within_the_last_modify_time = only_upload_within_the_last_modify_time
        self._file_volume_limit = file_volume_limit

        t = paramiko.Transport((host, port))
        t.connect(username=user, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(t)

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=user, password=password, compress=True)
        self.ssh = ssh

        self.set_log_level(sftp_log_level)

        self._has_upload_file_cnt = 0
        self._has_filter_file_cnt = 0
        self._has_upload_file_volume = 0
        self._has_filter_file_volume = 0

    def _judge_need_filter_a_file(self, filename: str):
        ext = filename.split('.')[-1]
        if '.' + ext in self._file_suffix_tuple_exluded:
            return True
        for path_pattern_exluded in self._path_pattern_exluded_tuple:
            # print(path_pattern_exluded,filename)
            if re.search(path_pattern_exluded, filename):
                return True
        file_st_mtime = os.stat(filename).st_mtime
        volume = os.path.getsize(filename)
        if time.time() - file_st_mtime > self._only_upload_within_the_last_modify_time:
            return True
        if volume > self._file_volume_limit:
            return True
        return False

    def _make_dir(self, dirc, final_dir):
        """
        sftp.mkdir 不能直接越级创建深层级文件夹。
        :param dirc:
        :param final_dir:
        :return:
        """
        # print(dir,final_dir)
        try:
            self.sftp.mkdir(dirc)
            if dirc != final_dir:
                self._make_dir(final_dir, final_dir)
        except (FileNotFoundError,):
            parrent_dir = os.path.split(dirc)[0]
            self._make_dir(parrent_dir, final_dir)

    def upload(self):
        for parent, dirnames, filenames in os.walk(self._local_dir):
            for filename in filenames:
                file_full_name = os.path.join(parent, filename).replace('\\', '/')
                volume = os.path.getsize(file_full_name)
                if not self._judge_need_filter_a_file(file_full_name):
                    remote_full_file_name = re.sub(f'^{self._local_dir}', self._remote_dir, file_full_name)
                    try:
                        self.logger.debug(f'本地：{file_full_name}   远程： {remote_full_file_name}')
                        self.sftp.put(file_full_name, remote_full_file_name)

                        self._has_upload_file_cnt +=1
                        self._has_upload_file_volume += volume
                    except (FileNotFoundError,) as e:
                        # self.logger.warning(remote_full_file_name)
                        self._make_dir(os.path.split(remote_full_file_name)[0], os.path.split(remote_full_file_name)[0])
                        self.sftp.put(file_full_name, remote_full_file_name)
                else:
                    self.logger.debug(f'根据过滤规则，不上传这个文件 {file_full_name}')
                    self._has_filter_file_cnt +=1
                    self._has_filter_file_volume +=volume
        self.logger.warning(f'''
         总共上传文件数量: {self._has_upload_file_cnt} 个  ,  总共上传文件体积: {self._has_upload_file_volume/1000000} M ,  
         总共过滤文件数量: {self._has_filter_file_cnt} 个  ,  总共过滤文件体积: {self._has_filter_file_volume/1000000} M   
''')


if __name__ == '__main__':
    uploader = ParamikoFolderUploader('192.168.6.133', 22, 'ydf', '372148', sys.path[1], '/home/ydf/codes/dssf/')
    uploader.upload()

```

**code file end: auto_run_on_remote/paramiko_util.py**

---


### code file start: auto_run_on_remote/remote_config.py 

```python
"""
这个配置文件是自动生成到你的项目根目录的。
"""

import sys

# 项目根目录文件夹，这个一般不需要改，会根据PYTHONPATH智能获取。
# pycahrm自动添加了项目根目录到第一个PYTHONPATH，如果是cmd命令启动这先设置PYTHONPATH环境变量。
# windows设置  set PYTHONPATH=你当前python项目根目录,然后敲击你的python运行命令
# linux设置    export PYTHONPATH=你当前python项目根目录,然后敲击你的python运行命令


PYTHON_PROJ_DIR_LOCAL = sys.path[1]

# 这是远程机器的账号密码配置。把这个配置文件加到gitignore就不会泄漏了。
HOST = '192.168.6.133'
PORT = 22
USER = 'ydf'
PASSWORD = '123456'

PYTHON_INTERPRETER = 'python3'  # 如果你安装了四五个python环境，可以直接指定远程解释器的绝对路径  例如 /opt/minicondadir/ens/env35/python

FORBID_DEPLOY_FROM_LINUX = True # 一般生产机器是linux，是否禁止从linux部署到别的机器，这样可以防止你从生产环境远程到测试环境，配置后，即使生产环境的代码有远程部署，也不会执行远程部署而是直接运行。

# 上传文件夹的配置，具体可以看paramiko_util.py里面的代码。
PATH_PATTERN_EXLUDED_TUPLE = ('/.git/', '/.idea/', '/dist/', '/build/')  # 路径中如果有这些就自动过滤不上传
FILE_SUFFIX_TUPLE_EXLUDED = ('.pyc', '.log', '.gz')  # 这些后缀的文件不上传
ONLY_UPLOAD_WITHIN_THE_LAST_MODIFY_TIME = 3650 * 24 * 60 * 60  # 只有在这个时间之内修改的文件才上传。如果项目比较大，可以第一次完整上传，之后再把这个时间改小。
FILE_VOLUME_LIMIT = 1000 * 1000  # 大于这个体积的文件不上传，单位b。
SFTP_LOG_LEVEL = 20  # 文件夹上传时候的日志级别。10 logging.DEBUG ,20 logging.INFO 30 logging.WaRNING,如果要看为什么某个文件上传失败，可以设置debug级别。

EXTRA_SHELL_STR = ''  # 远程执行命令之前，可以自定义执行的shell语句，一般例如可以设置啥环境变量什么的。

```

**code file end: auto_run_on_remote/remote_config.py**

---


### code file start: auto_run_on_remote/run_script_on_remote_server.py 

```python
import sys
import re
import os
import time
import nb_log
from auto_run_on_remote.paramiko_util import ParamikoFolderUploader
from fabric2 import Connection
from auto_run_on_remote import remote_config
from auto_run_on_remote import set_config  # noqa

logger = nb_log.get_logger('run_script_on_remote_server')
python_proj_dir = remote_config.PYTHON_PROJ_DIR_LOCAL.replace('\\', '/')
if not python_proj_dir.endswith('/'):
    python_proj_dir += '/'
python_proj_dir_short = python_proj_dir.split('/')[-2]

if remote_config.USER == 'root':  # 文件夹会被自动创建，无需用户创建。
    remote_dir = f'/pycodes/{python_proj_dir_short}/'
else:
    remote_dir = f'/home/{remote_config.USER}/pycodes/{python_proj_dir_short}/'


def run_current_script_on_remote(pty=True):
    """
    :param pty: 这个指的是本机脚本结束，远程就会结束。为False则本机例如停电关机结束，远程代码还在继续运行。
    :return:
    """
    if remote_config.FORBID_DEPLOY_FROM_LINUX and os.name == 'posix':
        # 一般生产机器是linux，是否禁止从linux部署到别的机器，这样可以防止你从生产环境远程到测试环境，配置后，即使生产环境的代码有远程部署，也不会执行远程部署而是直接运行。
        return
    if int(os.getenv('is_auto_remote_run', 0)) == 1:  # 不能循环递归远程启动。
        return
    logger.warning(f'将本地文件夹代码 {python_proj_dir}  上传到远程 {remote_config.HOST} 的 {remote_dir} 文件夹。')
    t_start = time.perf_counter()
    uploader = ParamikoFolderUploader(remote_config.HOST, remote_config.PORT, remote_config.USER,
                                      remote_config.PASSWORD,
                                      python_proj_dir, remote_dir,
                                      path_pattern_exluded_tuple=remote_config.PATH_PATTERN_EXLUDED_TUPLE,
                                      file_suffix_tuple_exluded=remote_config.FILE_SUFFIX_TUPLE_EXLUDED,
                                      only_upload_within_the_last_modify_time=remote_config.ONLY_UPLOAD_WITHIN_THE_LAST_MODIFY_TIME,
                                      file_volume_limit=remote_config.FILE_VOLUME_LIMIT,
                                      sftp_log_level=remote_config.SFTP_LOG_LEVEL)

    uploader.upload()
    logger.info(
        f'上传 本地文件夹代码 {python_proj_dir}  上传到远程 {remote_config.HOST} 的 {remote_dir} 文件夹耗时 {round(time.perf_counter() - t_start, 3)} 秒')
    # conn.run(f'''export PYTHONPATH={remote_dir}:$PYTHONPATH''')
    # 获取被调用函数所在模块文件名
    # print(sys._getframe())
    local_file_name = sys._getframe(1).f_code.co_filename.replace('\\', '/')  # noqa
    # file_name = re.sub(f'^{python_proj_dir}', '', local_file_name)
    file_name = re.sub(f'^{python_proj_dir}', remote_dir, local_file_name)  # 远程文件名字。
    process_mark = f'auto_remote_run_mark__{file_name.replace("/", "__")[:-3]}'

    conn = Connection(remote_config.HOST, port=remote_config.PORT, user=remote_config.USER,
                      connect_kwargs={"password": remote_config.PASSWORD}, )
    kill_shell = f'''ps -aux|grep {process_mark}|grep -v grep|awk '{{print $2}}' |xargs kill -9'''
    logger.warning(f'{kill_shell} 命令杀死 {process_mark} 标识的进程')
    uploader.ssh.exec_command(kill_shell)
    # conn.run(kill_shell, encoding='utf-8')

    python_exec_str = f''' {remote_config.PYTHON_INTERPRETER} {file_name}  -auto_remote_process_mark {process_mark} '''
    shell_str = f'''export is_auto_remote_run=1;export PYTHONPATH={remote_dir}:$PYTHONPATH ;cd {remote_dir}; {python_exec_str}'''
    extra_shell_str2 = remote_config.EXTRA_SHELL_STR  # 内部函数对外部变量不能直接改。
    if not extra_shell_str2.endswith(';') and remote_config.EXTRA_SHELL_STR != '':
        extra_shell_str2 += ';'
    shell_str = extra_shell_str2 + shell_str
    logger.warning(f'使用语句 {shell_str} 在远程机器 {remote_config.HOST} 上启动脚本 {file_name}')
    conn.run(shell_str, encoding='utf-8', pty=pty)
    sys.exit()  # 使本机不执行代码。

```

**code file end: auto_run_on_remote/run_script_on_remote_server.py**

---


### code file start: auto_run_on_remote/set_config.py 

```python
# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2022/4/11 0011 0:56
"""

使用覆盖的方式，做配置。
"""
import sys
import importlib
from pathlib import Path
from shutil import copyfile
import nb_log  # noqa
from auto_run_on_remote import remote_config

PACKAGE_NAME = 'auto_run_on_remote'
DEFAULT_CONFIG_MODLUE = 'remote_config'
CUSTOM_CONFIG_MODULE_NAME = 'auto_run_on_remote_config'

custom_config_module_path = Path(sys.path[1]).absolute() / Path(f'{CUSTOM_CONFIG_MODULE_NAME}.py')


def use_config_form_config_module():
    """
    自动读取配置。会优先读取启动脚本的目录的distributed_frame_config.py文件。没有则读取项目根目录下的distributed_frame_config.py
    :return:
    """

    try:
        m = importlib.import_module(CUSTOM_CONFIG_MODULE_NAME)
        msg = f'{PACKAGE_NAME} 包 读取到\n "{m.__file__}:1" 文件里面的变量作为优先配置了\n'
        print(msg)
        for var_namex, var_valuex in m.__dict__.items():
            if var_namex.isupper():
                setattr(remote_config, var_namex, var_valuex)
    except ModuleNotFoundError:
        auto_creat_config_file_to_project_root_path()
        msg = f'''在你的项目根目录下生成了 \n "{custom_config_module_path}:1" 的 {PACKAGE_NAME} 包 的配置文件，快去看看并修改一些自定义配置吧'''
        print(msg)


def auto_creat_config_file_to_project_root_path():
    # print(Path(sys.path[1]).as_posix())
    # print((Path(__file__).parent.parent).absolute().as_posix())
    """
    :return:
    """
    if Path(sys.path[1]).as_posix() in Path(__file__).parent.absolute().as_posix():
        print('不希望在本项目里面创建')
        return
    # noinspection PyPep8
    """
        如果没设置PYTHONPATH，sys.path会这样，取第一个就会报错
        ['', '/data/miniconda3dir/inner/envs/mtfy/lib/python36.zip', '/data/miniconda3dir/inner/envs/mtfy/lib/python3.6', '/data/miniconda3dir/inner/envs/mtfy/lib/python3.6/lib-dynload', '/root/.local/lib/python3.6/site-packages', '/data/miniconda3dir/inner/envs/mtfy/lib/python3.6/site-packages']
        
        ['', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\python36.zip', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\DLLs', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib', 'F:\\minicondadir\\Miniconda2\\envs\\py36', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\multiprocessing_log_manager-0.2.0-py3.6.egg', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\pyinstaller-3.4-py3.6.egg', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\pywin32_ctypes-0.2.0-py3.6.egg', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\altgraph-0.16.1-py3.6.egg', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\macholib-1.11-py3.6.egg', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\pefile-2019.4.18-py3.6.egg', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\win32', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\win32\\lib', 'F:\\minicondadir\\Miniconda2\\envs\\py36\\lib\\site-packages\\Pythonwin']
    """
    if '/lib/python' in sys.path[1] or r'\lib\python' in sys.path[1] or '.zip' in sys.path[1]:
        raise EnvironmentError('''如果用pycahrm启动，默认不需要你手动亲自设置PYTHONPATH，如果你是cmd或者shell中直接敲击python xx.py 来运行，
                               报现在这个错误，你现在肯定是没有设置PYTHONPATH环境变量，不要设置永久环境变量，设置临时会话环境变量就行，
                               windows设置  set PYTHONPATH=你当前python项目根目录,然后敲击你的python运行命令    
                               linux设置    export PYTHONPATH=你当前python项目根目录,然后敲击你的python运行命令    
                               要是连PYTHONPATH这个知识点都不知道，那就要google 百度去学习PYTHONPATH作用了，非常重要非常好用，
                               不知道PYTHONPATH作用的人，在深层级文件夹作为运行起点导入外层目录的包的时候，如果把深层级文件作为python的执行文件起点，经常需要到处很low的手写 sys.path.insert硬编码，这种方式写代码太low了。
                               知道PYTHONPATH的人无论项目有多少层级的文件夹，无论是多深层级文件夹导入外层文件夹，代码里面永久都不需要出现手动硬编码操纵sys.path.append
                               ''')
    # with (Path(sys.path[1]) / Path('nb_log_config.py')).open(mode='w', encoding='utf8') as f:
    #     f.write(config_file_content)
    copyfile(Path(__file__).parent / Path(f'{DEFAULT_CONFIG_MODLUE}.py'), custom_config_module_path)


use_config_form_config_module()

```

**code file end: auto_run_on_remote/set_config.py**

---


### code file start: auto_run_on_remote/__init__.py 

```python
from auto_run_on_remote.run_script_on_remote_server import run_current_script_on_remote
```

**code file end: auto_run_on_remote/__init__.py**

---

