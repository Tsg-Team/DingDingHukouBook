#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse
from DataBase import DBOperate
from BaseResource import BaseResource



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
        res = self.db.do_sql(operate, ['run', 'borrow', data])
        response = self.make_data(res)
        return response

