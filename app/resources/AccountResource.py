#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


import json

from flask import request

from app.Model.Model import Staff, Account
from app.resources.BaseResource import BaseResource


class AccountByUser(BaseResource):
    def get(self):
        userId = request.args.get('userId')
        querySql = {}
        if (userId):
            staffs = {
                '$elemMatch': {
                    'userId': userId
                }
            }
            querySql['staffs'] = staffs
            accounts = Account.objects(__raw__=querySql)
            result = []
            for account in accounts:
                result.append(account)
            return self.make_data(result, "success", "success")
        else:
            return self.make_data([], "failed", "failed")

    pass


class AccountByBookNum(BaseResource):
    def get(self, bookNum):
        accounts = Account.objects(bookNum=bookNum)
        return self.make_data(accounts[0], "success", "success")

    pass


class AccountRegister(BaseResource):
    def post(self):
        data = request.json
        account = Account(**data)
        account.save()
        return self.make_data(account, '录入成功', 'success')

    pass
