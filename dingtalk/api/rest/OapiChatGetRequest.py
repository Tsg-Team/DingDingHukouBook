'''
Created by auto_sdk on 2019.03.11
'''
from dingtalk.api.base import RestApi
class OapiChatGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.chatid = None

	def getHttpMethod(self):
		return 'GET'

	def getapiname(self):
		return 'dingtalk.oapi.chat.get'
