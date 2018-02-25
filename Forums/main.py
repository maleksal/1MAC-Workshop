import models
import stores 

member1 = models.Members("Malek",19)
member2 = models.Members("Ahmad",15)

store = stores.MemberStore()
store.add(member1)
store.add(member2)

print store.get_all()
print store.get_by_id(1)
print store.get_by_id(2)

print store.entity_exist(member1)
print store.entity_exist(member2)

store.delete(1)
store.update(member2)
print store.get_all()
#--------------
post1 = models.Post("welcome","Today i will talk about security")
post2 = models.Post("Hello","it is raining today!")
post3 = models.Post("Hi","How are u today!")

post_store = stores.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print post_store.get_all()

print post_store.get_by_id(1)
print post_store.get_by_id(2)
print post_store.get_by_id(3)

post_store.delete_post(1)
print post_store.get_all()



