#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/9/4 0:53
# software-version: python 3.6


import time
import threading


class CallableObject(object):

    # flask路由注册不能有同名函数，所以利用可调用对象来作为装饰器
    # 且修改对应对象的__name__字段，以避免函数或对象重名
    def __init__(self, func):
        self.func = func
        time.sleep(0.001)
        self.__name__ = str(time.time()).replace('.', '')

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class Lock(object):

    def __init__(self, func, *args, **kwargs):
        self.func = func

    # 锁住当前流程
    def __call__(self, *args, **kwargs):

        def realfunc(*args, **kwargs):
            # code
            lock = threading.Lock()
            lock.acquire()
            try:
                res = self.func(*args, **kwargs)
            except Exception as e:
                error = '[出现错误： %s]' % e
                print error
                res = error
            finally:
                lock.release()
            return res
        return realfunc()

