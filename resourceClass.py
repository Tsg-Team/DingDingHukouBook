#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse
from DataBase import DBOperate
from BaseResource import BaseResource


class Insert(BaseResource):

    def post(self):
        data = request.json
        res = self.db.do_sql(1, ['run', 'account', data])
        response = self.make_data(res)
        return response


class Update(BaseResource):

    def post(self):
        data = request.json
        response = self.make_data(data)
        return response


class Delete(BaseResource):

    def post(self):
        data = request.json
        response = self.make_data(data)
        return response


class Query(BaseResource):

    def post(self):
        data = request.json
        res = self.db.do_sql(4, ['run', 'account', data])
        response = self.make_data(res)
        return response
