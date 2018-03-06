import models
import stores

def create_member():
	member1 = models.Members("Malek",19)
	member2 = models.Members("Ahmad",15)
	print("{}\n{}".format(member1,member2))
	return member1 , member2

def adding_to_store(store,members):
	for member in members:
		store.add(member)

def get_all(store):
	return store.Members

def get_by_id(store,member):
	store.get_by_id(member.id)

def get_by_name(store,name):
	return store.get_by_name(name)

def update_member(store,member):
	member_copy = models.Members(member.name,member.age)
	member_copy.id = 3
	if member_copy is not member:
		print("{0} and {1} are not matching".format(member,member_copy))
	print(member_copy)
	member_copy.name = "Malek"
	store.update(member_copy)
	print(store.get_by_id(member.id))

def delete_member_by_id(store,id):
	try:
		store.delete(id)
	except ValueError:
		print("It should be  an existence entity before deleting!")

def get_members_with_posts(member_store,post_store):
	member_with_posts = member_store.get_members_with_post(post_store.get_all())
	for members_post in member_with_posts:
		print("{} has posted: \t".format(members_post.name))
		for posts in members_post.posts:
			print("\t{}\n".format(posts))

def get_top_two(member_store,post_store):
	top_two_members = member_store.get_top_two(post_store.get_all())
	for member_post in top_two_members:
		print("{} has posted: \t".format(member_post.name))
		for posts in member_post.posts:
			print("\t{}\n".format(posts))
#-----------------------------

def create_post(members_instance):
	post1 =models.Post("hello","How are you every body",members_instance[0].id)
	post2 = models.Post("hello","How are you every body",members_instance[1].id)
	post3 = models.Post("hello","How are you every body",members_instance[0].id)
	post4 =  models.Post("hello","How are you every body",members_instance[0].id)
	post5 =  models.Post("hello","How are you every body",members_instance[1].id)
	return post1,post2,post3,post4,post5

def storing_posts(post_instances,post_store):
	for post in post_instances:
		post_store.add(post)

#---------------------------
members_inc = create_member()
member1,member2 = members_inc
M_store = stores.MemberStore()
adding_to_store(M_store,members_inc)
get_by_id(M_store,member1)
get_by_name(M_store,"Malek")
print get_all(M_store)
#update_member(store,member2)
#delete_member_by_id(store,2)
create_post(members_inc)
post_inc = create_post(members_inc)
post1,post2,post3,post4,post5 = post_inc
post_store = stores.PostStore()
storing_posts(post_inc,post_store)
#get_members_with_posts(store,post_store)
get_top_two(M_store,post_store)
#----------------------------
