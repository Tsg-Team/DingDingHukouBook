#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: Jola
# datetime:2019/9/1 0:11
# software-version: python 3.6


import pymongo


INSERT, UPDATE, DELETE, QUERY = 1, 2, 3, 4


class DBOperate(object):

    def __init__(self):
        self.db = pymongo.MongoClient('mongodb://localhost:27017/')

    def do_sql(self, operate, info):
        # info: {db, table, data}
        if not self.check_data(info[2]):
            return False

        self.get_obj(info[0], info[1])
        print(self.obj)
        if operate == INSERT:
            res = self._insert(info[2])
        elif operate == UPDATE:
            res = self._update(info[2])
        elif operate == DELETE:
            res = self._delete(info[2])
        elif operate == QUERY:
            res = self._query(info[2])
            if res:
                return res
        else:
            res = False
        print(res)
        if res:
            return True
        return False

    def check_data(self, data):
        if isinstance(data, dict):
            return True

    def get_obj(self, *args):
        obj = self.db
        for e in args:
            obj = obj[e]
        self.obj = obj

    def _insert(self, data):
        '''
        mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
        x = mycol.insert_one(mydict)
        https://www.runoob.com/python3/python-mongodb-insert-document.html
        '''
        res = self.obj.insert_one(data)
        print(self.obj.find())
        return res

    def _update(self, data):
        '''
        myquery = { "alexa": "10000" }
        newvalues = { "$set": { "alexa": "12345" } }
        '''
        data[1]['$set'] = data
        res = self.obj.update_one(data[0], data[1])
        return res

    def _delete(self, data):
        res = self.obj.delete_one(data)
        return res

    def _query(self, data):
        res = self.obj.find(data)
        return res


if __name__ == '__main__':
    db = DBOperate()
    db.do_sql(1, [{'test': 'text'}])
