'''
Created by auto_sdk on 2019.06.28
'''
from dingtalk.api.base import RestApi
class OapiProcessWorkrecordCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.process.workrecord.create'
