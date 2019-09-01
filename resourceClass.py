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
db = DBOperate()


class Account(Resource):

    def post(self):
        data = request.json
        operate = data['operate']
        del data['operate']
        res = db.do_sql(operate, ['run', 'account', data])
        response = make_data(res)
        return response


class Borrow(Resource):

    def post(self):
        data = request.json
        operate = data['operate']
        res = db.do_sql(operate, ['run', 'account', data])
        response = make_data(res)
        return response


def make_data(data):
    data = {
        'data': data,
        'msg': 'success',
        'status': ''
    }
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = "true"
    return response
