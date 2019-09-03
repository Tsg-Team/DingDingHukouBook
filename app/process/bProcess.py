#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/9/4 0:38
# software-version: python 3.6


from app.db.DataBase import DBOperate
from app.decorator.decorator import Lock


@Lock
def borrow_account():
    # 借阅户口本流程
    db = DBOperate()

    return



