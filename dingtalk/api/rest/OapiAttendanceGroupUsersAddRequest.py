'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiAttendanceGroupUsersAddRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.group_key = None
		self.op_userid = None
		self.user_id_list = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.attendance.group.users.add'
