# markdown content namespace: db_libs readme 


## File Tree


```

└── README.md

```

---


## Included Files


- `README.md`


---


### code file start: README.md 

# db_libs
## 安装 pip innstall db_libs

各种数据库的封装。只封装生成连接的部分，十分克制,很少去添加一些新的方法然后去调用原生类的方法。

因为原生类已经很好用了，主要是控制一下用户无限实例化连接类，造成反复创建连接就可以了。

```
redis_lib和mongo_lib在redis和pymongo的基础上进行封装。
由于原生的包已经足够好用了，并不需要重新写几百个方法进行过度封装。
仅仅是加了享元模式，使得在相同入参情况下无限实例化相关客户端类的时候不会反复重新连接。
封装方式采用的非常规方式，使用的是继承方式，而非通常情况下的使用组合来进行封装。
继承方式封装的比组合模式封装的好处更多。



mysql_lib使用连接池，兼容在多线程环境运行。使调用时候少关注cursor commit close 等。

sqla_lib 是反射已存在的表，也是使用连接池，兼容多线程环境运行。能够支持orm和原生sql语句两种执行方式。

```

```python
# 组合模式封装的代码一般是如下这种例子。
"""
这种方式封装是组合，精确点是23种设计模式的代理模式。
代理模式说的是定义很多方法，来调用self.r所具有的方法。


另外对于无限实例化，还使用了享元模式。
封装数据库切记不要使用单例模式，如果入参传了不同的主机ip或者不同的db，而仍然返回之前的连接对象，那就大错特错了。

"""
# 使用组合模式封装的redis，没有继承模式的好用。
import redis

class RedisClient:

    params__reids_map = {}

    def __init__(self,host,db,port,password):
        if (host,db,port,password) not in self.__class__.params__reids_map:
            self.r = redis.Redis(host,db,port,password)
            self.__class__.params__reids_map[(host,db,port,password)] = self.r
        else:
            self.r = self.__class__.params__reids_map[(host,db,port,password)]
    
    def my_set(self,key,value):
        print('额外的扩展')
        self.r.set(name=key,value=value)
    
    def my_get(self,name):
        # 这个封装简直是多次一举，在redis实例化时候，
        # 将Redis类的构造方法的入参 decode_responses设置为True，就可以避免几百个方法需要反复decode了。
        return self.r.get(name).decode()

```

#### 例如网上的一种封装，重新封装几百个方法，我不喜欢这样封装工具类。
```python
import redis

class MyRedis():
    def __init__(self,ip,password,port=6379,db=1):#构造函数
        try:
            self.r = redis.Redis(host=ip,password=password,port=port,db=db)  #连接redis固定方法,这里的值必须固定写死
        except Exception as e:
            print('redis连接失败，错误信息%s'%e)
    def str_get(self,k):
        res = self.r.get(k)   #会从服务器传对应的值过来，性能慢
        if res:
            return res.decode()   #从redis里面拿到的是bytes类型的数据，需要转换一下

    def str_set(self,k,v,time=None): #time默认失效时间
        self.r.set(k,v,time)

    def delete(self,k):
        tag = self.r.exists(k)
        #判断这个key是否存在,相对于get到这个key他只是传回一个存在火灾不存在的信息，
        # 而不用将整个k值传过来（如果k里面存的东西比较多，那么传输很耗时）
        if tag:
            self.r.delete(k)
        else:
            print('这个key不存在')

    def hash_get(self,name,k):  #哈希类型存储的是多层字典（嵌套字典）
        res = self.r.hget(name,k)
        if res:
            return res.decode()  #因为get不到值得话也不会报错所以需要判断一下

    def hash_set(self,name,k,v): #哈希类型的是多层
        self.r.hset(name,k,v)   #set也不会报错

    def hash_getall(self,name):
        res = self.r.hgetall(name)   #得到的是字典类型的，里面的k,v都是bytes类型的
        data={}
        if res:
            for k,v in res.items(): #循环取出字典里面的k,v，在进行decode
                k = k.decode()
                v = v.decode()
                data[k]=v
        return data

    def hash_del(self,name,k):
        res = self.r.hdel(name,k)
        if res:
            print('删除成功')
            return 1
        else:
            print('删除失败，该key不存在')
            return 0

    @property   #属性方法，
                # 使用的时候和变量一个用法就好比实例，A=MyRedis(), A.clean_redis使用，
                # 如果不加这个@property,使用时A=MyRedis(), A.clean_redis()   后面需要加这个函数的括号
    def clean_redis(self):
        self.r.flushdb()   #清空 redis
        print('清空redis成功！')
        return 0



a = MyRedis('118.0000','HK0000*')

print(a.str_get('duan'))

```


## sqla_lib使用如下，可以orm操作已存在的数据库。
```python

if __name__ == '__main__':
    """
    例如 ihome_area2的表结果如下。
    
    create table ihome_area2
(
    create_time datetime    null,
    update_time datetime    null,
    id          int auto_increment
        primary key,
    name        varchar(32) not null
);

    """

    enginex = create_engine(
        'mysql+pymysql://root:123456@127.0.0.1:3306/aj?charset=utf8',
        max_overflow=10,  # 超过连接池大小外最多创建的连接
        pool_size=50,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=3600,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        echo=True)
    sqla_helper = SqlaReflectHelper(enginex)
    Ihome_area2 = sqla_helper.base_classes.ihome_area2  # ihome_area2是表名。


    def f1():
        with sqla_helper.session as ss:
            ss  # type: _SessionContext

            print(ss)

            print(ss.query(sqlalchemy.func.count(Ihome_area2.id)).scalar())

            # 使用orm方式插入
            ss.add(Ihome_area2(create_time=datetime.now(), update_time=datetime.now(), name='testname'))

            print(ss.query(sqlalchemy.func.count(Ihome_area2.id)).scalar())

            # 使用占位符语法插入，此种可以防止sql注入
            ss.execute(f'''INSERT INTO ihome_area2 (create_time, update_time, name) VALUES (:v1,:v2,:v3)''', params={'v1': '2020-06-14 19:15:14', 'v2': '2020-06-14 19:15:14', 'v3': 'testname00'})

            # 直接自己拼接完整字符串，不使用三方包占位符的后面的参数，此种会引起sql注入，不推荐。
            cur = ss.execute(f'''INSERT INTO ihome_area2 (create_time, update_time, name) VALUES ('2020-06-14 19:15:14','2020-06-14 19:15:14', 'testname')''', )

            # 这样也可以打印执行的语句
            # noinspection PyProtectedMember
            print(cur._saved_cursor._executed)

        # 使用最原生的语句，直接调用了pymysql的cursor对象。
        conny = sqla_helper.engine.raw_connection()
        cury = conny.cursor(DictCursor)  # type: DictCursor
        print(cury)
        cury.execute('SELECT * FROM ihome_area2 LIMIT 3')
        result = cury.fetchall()
        print(result)
        conny.commit()
        cury.close()
        conny.close()


    def f2():
        ss = sqla_helper.get_session_factory()()
        print(ss)
        print(ss.query(sqlalchemy.func.count(sqla_helper.base_classes.ihome_area.id)).scalar())
        ss.add(sqla_helper.base_classes.ihome_area(create_time=datetime.now(), update_time=datetime.now(), name='testname'))
        ss.commit()
        print(ss.query(sqlalchemy.func.count(sqla_helper.base_classes.ihome_area.id)).scalar())
        ss.close()


    with decorator_libs.TimerContextManager():
        t_pool = BoundedThreadPoolExecutor(10)  # 封装mysql，切记一定要测试多线程下的情况。
        for _ in range(500):
            # f1()
            t_pool.submit(f1)
        t_pool.shutdown()


```

![](https://visitor-badge.glitch.me/badge?page_id=db_libs)

**code file end: README.md**

---

# markdown content namespace: db_libs codes 


## File Tree


```

└── db_libs
    ├── __init__.py
    ├── dataset_lib.py
    ├── mongo_fork_safe.py
    ├── mongo_lib.py
    ├── mysql_lib.py
    ├── records.py
    ├── redis_lib.py
    ├── scripts
    │   ├── generate_create_table_statement_by_dict.py
    │   └── sqlmodel.py
    └── sqla_lib.py

```

---


## Included Files


- `db_libs/dataset_lib.py`

- `db_libs/mongo_fork_safe.py`

- `db_libs/mongo_lib.py`

- `db_libs/mysql_lib.py`

- `db_libs/records.py`

- `db_libs/redis_lib.py`

- `db_libs/sqla_lib.py`

- `db_libs/__init__.py`

- `db_libs/scripts/generate_create_table_statement_by_dict.py`

- `db_libs/scripts/sqlmodel.py`


---


### code file start: db_libs/dataset_lib.py 

```python

import os
import dataset
import threading

pid__db_map = {}
_lock = threading.Lock()

def get_db(connect_url) -> dataset.Database:
    """封装一个函数，判断pid"""
    pid = os.getpid()
    key = (pid, connect_url,)
    if key not in pid__db_map:
        with _lock:
            if key not in pid__db_map:
                pid__db_map[key] =  dataset.connect(connect_url)
    return pid__db_map[key]


def get_table(connect_url, table_name) -> dataset.Table:
    """封装一个函数，判断pid"""
    db = get_db(connect_url)
    return db[table_name]
```

**code file end: db_libs/dataset_lib.py**

---


### code file start: db_libs/mongo_fork_safe.py 

```python
import os
from multiprocessing import Process
from pymongo.collection import Collection
from pymongo import MongoClient

"""
此模块封装的pymongo是在linux上子进程安全的。使用方式见 db_libs/mongo_fork_safe.py
在win上无所谓都正常。

在linux上 MongoClient 实例化即使传参 connect=False，如果在父进程中已经操作了mongo，在子进程中仍然报错。
因为在父进程中只要操作了mongo，就会去连接mongo服务，connect=False就被破坏了。

只有下面这种每次操作mongo，都不使用Collection类型的全局变量/实例属性 ,每次都动态 get_col() ,每一次操作mongo前都判断pid的方式才进程安全
"""

pid__col_map = {}


def get_col(db: str, col: str, mongo_connect_url='mongodb://127.0.0.1') -> Collection:
    """封装一个函数，判断pid"""
    pid = os.getpid()
    key = (pid, mongo_connect_url, db, col)
    if key not in pid__col_map:
        pid__col_map[key] = MongoClient(mongo_connect_url,connect=False).get_database(db).get_collection(col)
    return pid__col_map[key]

```

**code file end: db_libs/mongo_fork_safe.py**

---


### code file start: db_libs/mongo_lib.py 

```python
# coding=utf8
"""
@author:Administrator
@file: mongo_lib.py
@time: 2020/06
"""

import pymongo
import decorator_libs  # pip install decorator_libs


@decorator_libs.flyweight
class MongoClientFlyWeight(pymongo.MongoClient):
    def my_fun(self):
        print('扩展示例')
        self.database_names()


@decorator_libs.lru_cache()
def get_col(mongo_connect_url, database_name, col_name):
    """
    缓存更进一步，节省执行的代码行数。操作更快。
    :param mongo_connect_url:
    :param database_name:
    :param col_name:
    :return:
    """
    return MongoClientFlyWeight(mongo_connect_url).get_database(database_name).get_collection(col_name)


if __name__ == '__main__':
    """
    测试无限实例化。
    使不使用享元模式，时间差距很大，相隔30多倍。
    """
    # with decorator_libs.TimerContextManager():
    #     pass
    #     for i in range(1000):
    #         pymongo.MongoClient().get_database('testdb').get_collection('test_col').insert({"a": i})

    with decorator_libs.TimerContextManager():
        for i in range(100000):
            MongoClientFlyWeight().get_database('testdb').get_collection('test_col')#.insert({"a": i})

    with decorator_libs.TimerContextManager():
        for i in range(100000):
            get_col('mongodb://127.0.0.1', 'testdb', 'test_col')#.insert({"a": i})

```

**code file end: db_libs/mongo_lib.py**

---


### code file start: db_libs/mysql_lib.py 

```python
# coding=utf8
"""
@author:Administrator
@file: mysql_lib.py
@time: 2020/06
"""
"""
最好的封装mysql的方式，是自定义cursor，扩展功能，然后指定为自己的Cursor类型。
这种方式需要能看懂源码。

"""
import datetime
import nb_log
import pymysql
import pymysql.cursors
from dbutils.pooled_db  import PooledDB  # pip install DBUtils
import decorator_libs


class _Row(dict):
    """A dict that allows for object-like property access syntax."""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


class ObjectCusor(pymysql.cursors.DictCursor, ):
    """
    比字典式的cursor，返回结果除了能用 ["xx"]来获取字段的值以外，还可以使用 .xx的方式获取字段的值。

    将sql内容打印出来
    """
    dict_type = _Row
    logger_object_cursor = nb_log.LogManager('db_libs.ObjectCusor').get_logger_and_add_handlers(log_filename='ObjectCusor.log')

    def mogrify(self, query, args=None):
        query_str = super().mogrify(query, args)
        self.logger_object_cursor.debug(query_str)
        return query_str

    def get_one(self, query, args):
        """
        可以在此类添加很多方法，或者继承此类，在CursorContext中指定cursor_class就可以。
        扩展方法示例，举个例子。
        :param query:
        :param args:
        :return:
        """
        print('假设你需要封装获取一条记录的方法，只想用一个方法来完成,不想手动调用execute和fetchone 两个方法，你可以这么封装')
        self.execute(query, args)
        return self.fetchone()


class CursorContext:
    def __init__(self, conn_pool: PooledDB, cursor_class=ObjectCusor, ):
        """
        :param conn_pool: 连接池
        """
        self.conn = conn_pool.connection()  # type: pymysql.Connection
        self.cursor = self.conn.cursor(cursor_class)  # type: ObjectCusor                #pymysql.cursors.Cursor

    def __enter__(self) -> ObjectCusor:
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return False


if __name__ == '__main__':
    # pymysql.connections.Connection
    pool = PooledDB(
        creator=pymysql,  # 使用链接数据库的模块
        maxconnections=50,  # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=5,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
        maxcached=10,  # 链接池中最多闲置的链接，0和None不限制
        maxshared=0,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
        maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
        setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
        ping=0,
        # ping MySQL服务端，检查是否服务可用。
        # 如：0 = None = never,
        # 1 = default = whenever it is requested,
        # 2 = when a cursor is created,
        # 4 = when a query is executed,
        # 7 = always
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='sqlachemy_queues',
        charset='utf8',
        # cursorclass=pymysql.cursors.DictCursor, # 固定使用自定义的 ObjectCusor，包含了DictCursor的所有功能。
    )

    """
    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    cur = conn.cursor()
    sql = "select * from queue_test58 limit 10"
    r = cur.execute(sql)
    r = cur.fetchall()
    print(r)
    cur.close()
    conn.close()
    """
    # nb_log.LogManager().get_logger_and_add_handlers()
    with CursorContext(pool, ) as cursor:
        cursor.execute("select * from sqlachemy_queues.queue_test58 limit 3")
        for row in cursor.fetchall():
            print(row['status'])  # 两种方式都可以获取表中的status字段的值。
            print(row.status)
        cursor.execute('INSERT INTO sqlachemy_queues.queue_test58(body,publish_timestamp,status) VALUES (%s,%s, %s)',
                       args=('bodytest', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'teststatus'))
        print(cursor.rowcount, cursor.lastrowid)
        # 可以调用自定义的方法。
        print(cursor.get_one('select * from sqlachemy_queues.queue_test58 where body=%s', args=('bodytest',)))

    with CursorContext(pool) as cursor:
        cursor.executemany('INSERT INTO sqlachemy_queues.queue_test58(body,publish_timestamp,status) VALUES (%s,%s, %s)',
                           args=[('bodytest', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'teststatus')] * 10)
        print(cursor.rowcount, cursor.lastrowid)


    def test_threads():
        """测试多线程"""
        with CursorContext(pool, ) as cursorx:
            cursorx.execute('INSERT INTO sqlachemy_queues.queue_test58(body,publish_timestamp,status) VALUES (%s,%s, %s)',
                            args=('bodytest', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'teststatus'))


    from threadpool_executor_shrink_able import ThreadPoolExecutorShrinkAble

    thread_pool = ThreadPoolExecutorShrinkAble(10)
    with decorator_libs.TimerContextManager():
        for _ in range(3000):
            thread_pool.submit(test_threads)
        thread_pool.shutdown()

```

**code file end: db_libs/mysql_lib.py**

---


### code file start: db_libs/records.py 

```python

from records import *
```

**code file end: db_libs/records.py**

---


### code file start: db_libs/redis_lib.py 

```python
# coding=utf8
"""
@author:Administrator
@file: redis_lib.py
@time: 2020/06
"""
import redis2  # pip install redis2
import redis3  # pip install redis3
import decorator_libs  # pip install decorator_libs

"""
将Redis类的构造方法的入参 decode_responses设置为True，将会减少很多手动decode的麻烦。

"""


@decorator_libs.flyweight
class RedisV2(redis2.Redis):
    """
    通常封装的redis工具类，一般是控制单例、享元模式等，使其在实例化时候不会无限重新校验账号密码进行连接。
    通常如果要封装redis，一般使用的是组合的方式，并不会使用到继承官方Redis类，此封装将打破这一常规使用继承，同时使用了享元模式装饰器，确保不会无限重新连接。

    此类由于是继承关联方Reids类，所以可以直接使用一切Redis类的方法，同时在此类可以添加自己的一些方法。
    我不建议直接覆盖父类的方法名，我希望确保原生的Redis方法名是原汁原味的，如果要扩展，我希望是添加一些不同的方法名。
    """

    def my_set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """
        此方法是举个例子
        这样此类技能照常使用原生Redis类的方法，又能添加自己的一些方法。
        :param name:
        :param value:
        :param ex:
        :param px:
        :param nx:
        :param xx:
        :return:
        """
        print('添加自己的一些逻辑')
        self.set(name, value, ex, px, nx, xx)


@decorator_libs.lru_cache()
def redis2_from_url(url, db=None, **kwargs):
    return redis2.from_url(url, db, **kwargs)


@decorator_libs.flyweight
class RedisV3(redis3.Redis):
    """
    redis2 和 redis3这两个包有很多不同之处，redis2是redis包的2.10.6的不同命名空间的备份版本。
    redis3 是redis包的3.xx 的不同命名空间的备份版本。
    之所以这样做，是为了可以确保在同一个项目中，同时使用redis的2.xx和3.xx。
    通常，同一个项目要使用一个包的两个版本是不可能的，因为是在同一个解释器下运行，无法使用所谓的python虚拟环境来隔离使用不同版本。

    redis2和redsi3有许多方法，虽然方法名一样，但入参位置，入参名称，入参类型不一样。
    例如你老项目想使用celery4.4版本，会被安装上redis 3.xx版本，如果你的项目已经多处使用了redis 2.xx的方法，运行起来会产生很多错误。
    如果坚持使用celery4.4版本，同时又不想去修改项目中大量的redis 2.xx的使用地方，那么你的redis工具类可以改成依赖redis2这个包，而不是去依赖redis包的2.xx版本,这样第三方包依赖何种redis版本都不会影响到你。

    此类是为了redsi3.

    """


@decorator_libs.lru_cache()
def redis3_from_url(url, db=None, **kwargs):
    return redis3.from_url(url, db, **kwargs)


if __name__ == '__main__':
    """
    测试10000次写入，都采用无限实例化的方式。
    使用没有加入享元模式的Redis类操作10000次时间远远大于RedisV2操作时间。
    """
    with decorator_libs.TimerContextManager():
        for _ in range(100):
            redis2.Redis(password='123456').set('test1', 1)

    with decorator_libs.TimerContextManager():
        for _ in range(100):
            RedisV2(password='123456').set('test1', 1)

```

**code file end: db_libs/redis_lib.py**

---


### code file start: db_libs/sqla_lib.py 

```python
# coding=utf8
"""
@author:Administrator
@file: sqla_lib.py
@time: 2020/06
"""
from datetime import datetime
import decorator_libs
import nb_log

import sqlalchemy
# from pymysql import PY2
from pymysql.cursors import Cursor, DictCursor
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.scoping import ScopedSession
from threadpool_executor_shrink_able import ThreadPoolExecutorShrinkAble

# sqlachemy的日志还是非最终完全sql语句，这里可以显示完全最终语句。
logger_show_pymysql_execute_sql = nb_log.LogManager('show_pymysql_execute_sql').get_logger_and_add_handlers(
    log_filename='show_pymysql_execute_sql.log')


def _my_mogrify(self, query, args=None):
    """
    Returns the exact string that is sent to the database by calling the
    execute() method.

    This method follows the extension to the DB API 2.0 followed by Psycopg.
    """
    conn = self._get_db()
    # if PY2:  # Use bytes on Python 2 always
    #     query = self._ensure_bytes(query, encoding=conn.encoding)

    if args is not None:
        query = query % self._escape_args(args, conn)
    logger_show_pymysql_execute_sql.debug(query)
    return query


Cursor.mogrify = _my_mogrify


class _SessionContext(Session):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()
        return False


class SqlaReflectHelper(nb_log.LoggerMixin):
    """
    反射数据库中已存在的表
    """

    def __init__(self, sqla_engine: Engine):
        nb_log.LogManager('sqlalchemy.engine.base.Engine').remove_all_handlers()
        if sqla_engine.echo:
            # 将日志自动记录到硬盘根目录的/pythonlogs/sqla_execute.log。原来的日志模板不好看，换成这个。
            nb_log.LogManager('sqlalchemy.engine.base.Engine').get_logger_and_add_handlers(10, log_filename='sqla_execute.log')
        else:
            nb_log.LogManager('sqlalchemy.engine.base.Engine').get_logger_and_add_handlers(30, log_filename='sqla_execute.log')
        self.engine = sqla_engine
        Base = automap_base()
        Base.prepare(self.engine, reflect=True)
        self.base_classes = Base.classes
        self.base_classes_keys = Base.classes.keys()
        self.logger.debug(self.base_classes_keys)
        self.show_tables_and_columns()
        self.session_factory_of_scoped = None

    def show_tables_and_columns(self):
        for table_name in self.base_classes_keys:
            self.logger.debug(table_name)
            model = getattr(self.base_classes, table_name)
            self.logger.debug(model.__table__.columns.keys())

    def get_session_factory(self):
        return sessionmaker(bind=self.engine)

    def get_session_factory_of_scoped(self) -> ScopedSession:
        session_factory = sessionmaker(bind=self.engine, class_=_SessionContext)  # 改成了自定义的Session类
        return ScopedSession(session_factory)

    @property
    def session(self):
        if not self.session_factory_of_scoped:
            self.session_factory_of_scoped = self.get_session_factory_of_scoped()
        return self.session_factory_of_scoped()


if __name__ == '__main__':
    """
    例如 ihome_area2的表结果如下。
    
    create table ihome_area2
(
    create_time datetime    null,
    update_time datetime    null,
    id          int auto_increment
        primary key,
    name        varchar(32) not null
);

    """

    enginex = create_engine(
        'mysql+pymysql://root:123456@127.0.0.1:3306/aj?charset=utf8',
        max_overflow=10,  # 超过连接池大小外最多创建的连接
        pool_size=50,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=3600,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        echo=True)
    sqla_helper = SqlaReflectHelper(enginex)
    Ihome_area2 = sqla_helper.base_classes.ihome_area2  # ihome_area2是表名。


    def f1():
        with sqla_helper.session as ss:
            ss  # type: _SessionContext

            print(ss)

            print(ss.query(sqlalchemy.func.count(Ihome_area2.id)).scalar())

            # 使用orm方式插入
            ss.add(Ihome_area2(create_time=datetime.now(), update_time=datetime.now(), name='testname'))

            print(ss.query(sqlalchemy.func.count(Ihome_area2.id)).scalar())



            # 使用占位符语法插入，此种可以防止sql注入
            ss.execute(text('''INSERT INTO ihome_area2 (create_time, update_time, name) VALUES (:v1,:v2,:v3)'''), params={'v1': '2020-06-14 19:15:14', 'v2': '2020-06-14 19:15:14', 'v3': 'testname00'})

            # 直接自己拼接完整字符串，不使用三方包占位符的后面的参数，此种会引起sql注入，不推荐。
            cur = ss.execute(f'''INSERT INTO ihome_area2 (create_time, update_time, name) VALUES ('2020-06-14 19:15:14','2020-06-14 19:15:14', 'testname')''', )

            # 这样也可以打印执行的语句
            # noinspection PyProtectedMember
            print(cur._saved_cursor._executed)

        # 使用engine多对操作.
        enginex.execute('SELECT * FROM ihome_area2')

        # 使用最原生的语句，直接调用了pymysql的cursor对象。
        conny = sqla_helper.engine.raw_connection()
        cury = conny.cursor(DictCursor)  # type: DictCursor
        print(cury)
        cury.execute('SELECT * FROM ihome_area2 LIMIT 3')
        result = cury.fetchall()
        print(result)
        conny.commit()
        cury.close()
        conny.close()


    def f2():
        ss = sqla_helper.get_session_factory()()
        print(ss)
        print(ss.query(sqlalchemy.func.count(sqla_helper.base_classes.ihome_area.id)).scalar())
        ss.add(sqla_helper.base_classes.ihome_area(create_time=datetime.now(), update_time=datetime.now(), name='testname'))
        ss.commit()
        print(ss.query(sqlalchemy.func.count(sqla_helper.base_classes.ihome_area.id)).scalar())
        ss.close()


    with decorator_libs.TimerContextManager():
        t_pool = ThreadPoolExecutorShrinkAble(10)  # 封装mysql，切记一定要测试多线程下的情况。
        for _ in range(500):
            # f1()
            t_pool.submit(f1)
        t_pool.shutdown()



```

**code file end: db_libs/sqla_lib.py**

---


### code file start: db_libs/__init__.py 

```python
# coding=utf8
"""
@author:Administrator
@file: __init__.py
@time: 2020/06
"""

# from torndb_for_python3 import Connection as TorndbConnection
# import records   # 这也是兼容多种sql数据库的。
# import dataset  # 方便保存字典
```

**code file end: db_libs/__init__.py**

---


### code file start: db_libs/scripts/generate_create_table_statement_by_dict.py 

```python
def generate_create_table_statement(data,table_name):
    columns = []
    for key, value in data.items():
        if isinstance(value, bool):
            columns.append(f"{key} BOOLEAN")
        elif isinstance(value, int):
            columns.append(f"{key} BIGINT(20)")
        elif isinstance(value, float):
            columns.append(f"{key} FLOAT")
        elif isinstance(value, str):
            columns.append(f"{key} VARCHAR(255)")
        elif isinstance(value, dict):
            columns.append(f"{key} JSON")
        else:
            columns.append(f"{key} VARCHAR(255)")

    columns_str = ', '.join(columns)
    create_table_statement = f"CREATE TABLE {table_name} ({columns_str})"

    return create_table_statement

if __name__ == '__main__':
    # 给定的字典数据
    data = {
        "_id": "test_user_custom_result:4b42c7f2-7dda-4201-9cdc-dc61789ff72c",
        "function": "f",
        "host_name": "LAPTOP-7V78BBO2",
        "host_process": "LAPTOP-7V78BBO2 - 49552",
        "insert_minutes": "2024-02-18 16:32",
        "insert_time": "2024-02-18 16:32:20",
        "insert_time_str": "2024-02-18 16:32:20",
        "msg_dict": {
            "extra": {
                "publish_time": 1708245138.8229,
                "publish_time_format": "2024-02-18 16:32:18",
                "task_id": "test_user_custom_result:4b42c7f2-7dda-4201-9cdc-dc61789ff72c"
            },
            "x": 29
        },
        "params": {
            "x": 29
        },
        "params_str": '{"x": 29}',
        "process_id": 49552,
        "publish_time": 1708245138.8229,
        "publish_time_str": "2024-02-18 16:32:18",
        "queue_name": "test_user_custom",
        "result": 290,
        "run_times": 1,
        "script_name": "test_user_custom_record_process_info_func.py",
        "script_name_long": "D:\\codes\\funboost\\test_frame\\test_user_custom_record_process_info_func\\test_user_custom_record_process_info_func.py",
        "success": True,
        "task_id": "test_user_custom_result:4b42c7f2-7dda-4201-9cdc-dc61789ff72c",
        "thread_id": 25580,
        "time_cost": 0.003,
        "time_end": 1708245140.4220266,
        "time_start": 1708245140.4190009,
        "total_thread": 8,
        "utime": "2024-02-18 08:32:20",
    }

    # 生成建表语句
    create_table_statement = generate_create_table_statement(data,table_name = "your_table_namexx")

    # 打印建表语句
    print(create_table_statement)
```

**code file end: db_libs/scripts/generate_create_table_statement_by_dict.py**

---


### code file start: db_libs/scripts/sqlmodel.py 

```python


from sqlmodel import create_engine, Session

"""
SQLModel 是一个基于 Python 的 SQL 数据库访问工具，
它提供了一种声明式的方式来定义数据库模型，并且能够自动创建数据库表格、执行查询操作和数据持久化。SQLModel 基于 SQLAlchemy 库构建而成，它简化了 SQLAlchemy 的使用方式，使得开发者能够更加方便地与 SQL 数据库交互。
"""
```

**code file end: db_libs/scripts/sqlmodel.py**

---

