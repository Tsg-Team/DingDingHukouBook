'''
Created by auto_sdk on 2018.08.07
'''
from dingtalk.api.base import RestApi
class OapiUserGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.userid = None

	def getHttpMethod(self):
		return 'GET'

	def getapiname(self):
		return 'dingtalk.oapi.user.get'
