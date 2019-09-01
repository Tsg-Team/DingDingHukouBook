#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


from flask import make_response, jsonify, request
from flask_restful import Resource, reqparse
from DataBase import DBOperate


class BaseResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('header', type=str)
    db = DBOperate()

    def make_data(self, data):
        resData = {
            'data': data,
            'msg': 'success',
            'status': ''
        }
        response = make_response(jsonify(resData))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

