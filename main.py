#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:32
# software-version: python 3.6


from flask import Flask
from flask_restful import Api
from resourceClass import Insert, Query, Update, Delete


app = Flask(__name__)
api = Api(app)

api.add_resource(Insert, '/insert')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')
api.add_resource(Query, '/query')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8002')


