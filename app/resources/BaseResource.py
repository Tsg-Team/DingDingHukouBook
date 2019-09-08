#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6
import json
from json import JSONEncoder

from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from mongoengine.base import BaseDocument

from app.db.DataBase import DBOperate

class MongoEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseDocument):
            data = o.to_mongo()
            # might not be present if EmbeddedDocument
            o_id = data.pop('_id', None)
            if o_id:
                data['id'] = str(o_id.__str__())
            data.pop('_cls', None)
            return data
        else:
            return JSONEncoder.default(self, o)

class BaseResource(Resource):
    db = DBOperate()
    def make_data(self, data, msg, status):
        resData = {
            'data': data,
            'msg': msg,
            'status': status
        }
        response = make_response(json.dumps(resData, cls=MongoEncoder))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Credentials'] = "true"
        return response

