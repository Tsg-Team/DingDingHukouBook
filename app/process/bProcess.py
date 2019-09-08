#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/9/4 0:38
# software-version: python 3.6


import datetime

from app.db.DataBase import DBOperate
from app.decorator.decorator import Lock


@Lock
def borrow_account(operate=4, data=None):
    # 借阅户口本流程
    if not data:
        data = ['run', 'borrow', {'test': 'test'}]
    print 'Start time: %s' % datetime.datetime.now()
    # time.sleep(1)
    db = DBOperate()
    # res = db.do_sql(4, ['run', 'account', {'bookStatus': '正常'}])
    res = db.do_sql(operate, data)
    print 'End time: %s' % datetime.datetime.now()
    return res


if __name__ == '__main__':
    b1, b2 = [borrow_account(), borrow_account()]
    print b1
    print b2

