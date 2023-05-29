import pymongo 
import bson 
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['example']
user = db['user']
res = user.find().sort("username",1)
# res = user.find()
for i in res:
    print(i)
# res2 = user.find_one({"email":"khdd@mail.com"})
# res = user.find()
# for i in res:
#     print(i)
# print('res2 ')
# print(res2)
# user.update_one({"email":"khddd@mail.com"},{"$pull":{"email":"khdd@mail.com"}})

