#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/9/4 0:38
# software-version: python 3.6


from app.db.DataBase import DBOperate
from app.decorator.decorator import Lock
import threading


lock = threading.Lock()


# @Lock
def borrow_account():
    # 借阅户口本流程

    # lock.acquire()
    db = DBOperate()
    # lock.release()
    res = db.do_sql(4, ['run', 'account', {'bookStatus': 'error'}])
    print res
    return res


if __name__ == '__main__':
    b1 = borrow_account()
    b2 = borrow_account()
    print b1
    print b2

