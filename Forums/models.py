class Members():
	def __init__(self,username,age):
		self.name = username
		self.age = age

class Post():
	def __init__(self,title,content):
		self.title = title 
		self.content = content
	def __str__(self):
		return self.title +"\t"+ self.content 