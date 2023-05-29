import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

mycol = mydb["customers"]

print(mydb.list_collection_names())
#
# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")

# mydict = { "name": "John", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)
#
# mydict = { "name": "Peter", "address": "Lowstreet 27" }
#
# x = mycol.insert_one(mydict)
#
# print(x.inserted_id)
#
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
#
# print(x.inserted_ids)

# x = mycol.find_one()

# print(x)
# print("printing all the customers")
# for x in mycol.find():
#     print(x)
print('55')
myquery = {"name":"Ben"}

mydoc = mycol.find_one(myquery,{'address':0})
print(mydoc["_id"])
print('59')
print(mydoc)
for x in mydoc:
    print(x)
print(mydoc['name'])
print("printing what you wanted")
print(type(mydoc))
