class MemberStore():
	Member_database = []
	last_id = 1

	def get_all(self):
		return MemberStore.Member_database
	
	def add(self,member):
		member.id = MemberStore.last_id
		MemberStore.Member_database.append(member)
		MemberStore.last_id += 1
	
	def get_by_id(self,id):  
		if id !=0 and id < MemberStore.last_id:
			return (MemberStore.Member_database[id-1])
		return False		
	
	def delete(self,id):
		member_id = self.get_all()
		member_id.remove(self.get_by_id(id))
		MemberStore.last_id -= 1

	def entity_exist(self,member):
		for e in self.get_all():
			if str(e) == str(member):
				return ("{} exist".format(str(e)))
		return 	False

	def update(self, member):
		result = member
		all_members = self.get_all()
		for index, user in enumerate(all_members):
			if user.id == member.id:
				all_members[index] = member
				break
#-------------Post Store------------------------

class PostStore():
	Posts = []
	last_id = 1

	def get_by_id(self,id):
		if id != 0 and id < PostStore.last_id:
			return (PostStore.Posts[id-1])
		return False	
		
	def get_all(self):
		return PostStore.Posts

	def add (self,post):
		post.id = PostStore.last_id
		self.Posts.append(post)	
	  	PostStore.last_id += 1
	
	def delete_post(self,id):
		posts = self.get_all()
		posts.remove(self.get_by_id(id))
		PostStore.last_id -= 1
