import itertools
class MemberStore():
	Members = []
	last_id = 1

	def get_all(self):
		return MemberStore.Members
	
	def add(self,member):
		member.id = MemberStore.last_id
		MemberStore.Members.append(member)
		MemberStore.last_id += 1
	
	def get_by_id(self,id):  
		result = None
		for e in self.get_all():
			if e.id == id :
				result = e 
			break
		return result		

	def get_by_name(self,member_name):
		return (member for member in self.get_all() if member.name == member_name)		
		
	
	def delete(self,id):
		member_id = self.get_all()
		member_id.remove(self.get_by_id(id))
		MemberStore.last_id -= 1

	def entity_exist(self,member):
		for e in self.get_all():
			if str(e) == str(member):
				return True
		return 	False

	def update(self, member):
		result = member
		all_members = self.get_all()
		for index, user in enumerate(all_members):
			if user.id == member.id:
				all_members[index] = member
				break

	def get_members_with_post(self,all_posts):
		all_members = self.get_all()
		for member , post in itertools.product(all_members,all_posts):
			if member.id == post.member_id:
				member.posts.append(post)
		for member in all_members:
			yield member	

		
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

	

