#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


from flask import request

from app.resources.BaseResource import BaseResource
from app.process.bProcess import borrow_account


class Account(BaseResource):

    def post(self):
        data = request.json
        operate = int(data['operate'])
        del data['operate']
        res = self.db.do_sql(operate, ['run', 'account', data])
        response = self.make_data(res)
        return response


class Borrow(BaseResource):

    def post(self):
        data = request.json
        operate = data['operate']
        res = borrow_account(operate, ['run', 'borrow',  data])
        response = self.make_data(res)
        return response

