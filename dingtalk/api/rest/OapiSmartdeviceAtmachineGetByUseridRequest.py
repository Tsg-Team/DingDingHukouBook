'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiSmartdeviceAtmachineGetByUseridRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.param = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartdevice.atmachine.get_by_userid'
