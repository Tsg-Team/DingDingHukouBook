#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6


from flask import request
from flask_restful import reqparse

import appConfig
import dingtalk.api
from app.resources.BaseResource import BaseResource

parser = reqparse.RequestParser()
parser.add_argument('header', type=str)
appConfig = appConfig.configs.get('appConfig')


class Login(BaseResource):
    def post(self):
        requestData = request.json
        token = getAssessToken()
        userInfo = getUseInfo(token, requestData['authCode'])
        return self.make_data(userInfo)


def getAssessToken():

    request = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    request.appkey = appConfig.get('appKey')
    request.appsecret = appConfig.get('appSecret')
    response = request.getResponse()
    return response['access_token']


def getUseInfo(accessToken, authCode):
    request = dingtalk.api.OapiSsoGetuserinfoRequest("https://oapi.dingtalk.com/user/getuserinfo")
    request.code = authCode
    request.access_token = accessToken
    response = request.getResponse()
    return response
