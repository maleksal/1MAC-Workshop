import models
import stores

def create_member():
	member1 = models.Members("Malek",19)
	member2 = models.Members("Ahmad",15)
	print(member1)
	print(member2)
	return member1 , member2

def adding_to_store(store,members):	
	for member in members:
		store.add(member)

def get_all(store):
	for members in store.Members:
		return members	

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

#---------------------------
members_inc = create_member()
member1,member2 = members_inc
store = stores.MemberStore()

adding_to_store(store,members_inc)
get_by_id(store,member1)
get_by_name(store,"Malek")
print get_all(store)

update_member(store,member2)
delete_member_by_id(store,2)

#-------- post ---------------


