#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/8/31 23:43
# software-version: python 3.6
import json
import time

from flask import request
import threading

from app.Model.Model import Staff, Account
from app.resources.BaseResource import BaseResource

lock = threading.Lock()

class Borrow(BaseResource):

    def post(self):
        requestData = request.json
        if(not lock.locked()):
            lock.acquire()
            result = {
                "error":""
            }
            try:
                time.sleep(3)
                accounts = Account.objects(bookNum=requestData['bookNum'])
            except Exception as e:
                error = '[出现错误： %s]' % e
                print error
                result["error"] = error
            finally:
                lock.release()
                if(result["error"]):
                    return self.make_data({}, result["error"], 'success')
                else:
                    return self.make_data({}, '申请成功', 'success')
        else:
            return self.make_data({}, '他人正在借请稍后重试', 'faild')

    pass
