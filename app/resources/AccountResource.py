from flask import request

from app.Model.Model import Staff, Account
from app.resources.BaseResource import BaseResource


class AccountQuery(BaseResource):
    def get(self, accountId):
        accounts = Account.objects(bookNum=accountId)
        print accounts[0].bookName
        return self.make_data(accounts[0].bookName)

    pass


class AccountRegister(BaseResource):
    def post(self):
        data = request.json
        operate = int(data['operate'])
        del data['operate']
        res = self.db.do_sql(operate, ['run', 'account', data])
        response = self.make_data(res)
        return response

    pass
