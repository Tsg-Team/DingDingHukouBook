'''
Created by auto_sdk on 2019.06.24
'''
from dingtalk.api.base import RestApi
class OapiProcessWorkrecordTaskgroupCancelRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.process.workrecord.taskgroup.cancel'
