'''
Created by auto_sdk on 2019.07.09
'''
from dingtalk.api.base import RestApi
class OapiServiceaccountListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.pageSize = None
		self.pageStart = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.serviceaccount.list'
