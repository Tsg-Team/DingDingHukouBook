'''
Created by auto_sdk on 2018.07.25
'''
from dingtalk.api.base import RestApi
class OapiUserGetAdminRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)

	def getHttpMethod(self):
		return 'GET'

	def getapiname(self):
		return 'dingtalk.oapi.user.get_admin'
