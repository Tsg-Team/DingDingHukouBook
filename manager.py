#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:32
# software-version: python 3.6


from flask import Flask
from flask_restful import Api

from app.resources.loginResource import Login
from app.resources.resourceClass import Account, Borrow


app = Flask(__name__)
api = Api(app)

api.add_resource(Account, '/account')
api.add_resource(Borrow, '/borrow')
api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8002')


