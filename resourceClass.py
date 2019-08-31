#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse
from DataBase import DBOperate


parser = reqparse.RequestParser()
parser.add_argument('header', type=str)


class Insert(Resource):

    def post(self):
        db = DBOperate()
        data = request.json
        res = db.do_sql(1, ['run', 'account', data])
        response = make_data(res)
        return response


class Query(Resource):

    def post(self):
        data = request.json
        response = make_data(data)
        return response


def make_data(data):
    data = {
        'data': data,
        'msg': 'success'
    }
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response