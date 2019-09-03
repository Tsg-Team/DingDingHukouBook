#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/9/4 0:53
# software-version: python 3.6


class Lock(object):
    # 锁住当前流程
    def __call__(self, *args, **kwargs):

        def realfunc(*args, **kwargs):
            try:
                self._func(*args, **kwargs)
            except Exception as e:
                error = '[出现错误： %s]' % e
                print error
                return error
        return realfunc

    def __init__(self, func):
        self._func = func

