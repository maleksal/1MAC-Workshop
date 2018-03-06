from datetime import datetime
class Members():
	def __init__(self,username,age):
		self.name = username
		self.age = age
		self.id =0
		self.posts = []
	def __str__(self):
		return ("Name:{}, Age: {}".format(self.name,self.age))

class Post():
	def __init__(self,title,content,member_id = 0):
		self.title = title 
		self.content = content
		self.id =0
		self.datetime = datetime.now()
		self.member_id= member_id
	def __str__(self):
		return ("Title: {} , Content: {} , Date: {}".format(self.title,self.content,self.datetime))