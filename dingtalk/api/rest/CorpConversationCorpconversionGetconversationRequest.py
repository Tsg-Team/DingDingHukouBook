'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class CorpConversationCorpconversionGetconversationRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.open_conversation_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.corp.conversation.corpconversion.getconversation'
