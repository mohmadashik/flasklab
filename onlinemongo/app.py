# from flask import Flask ,jsonify
from pymongo import MongoClient
# from bson import ObjectId
import pymongo

# app = Flask(__name__)
# client = MongoClient("mongodb+srv://root:ashik123@cluster0.mjskf0e.mongodb.net/?retryWrites=true&w=majority")

# client = pymongo.MongoClient("mongodb+srv://root:ashik123@cluster0.mjskf0e.mongodb.net/?retryWrites=true&w=majority")
# client = MongoClient("mongodb+srv://root:<password>@cluster0.mjskf0e.mongodb.net/?retryWrites=true&w=majority")

client = pymongo.MongoClient("mongodb://ashik:ashik123@ac-emlkjtg-shard-00-00.izcbjtm.mongodb.net:27017,ac-emlkjtg-shard-00-01.izcbjtm.mongodb.net:27017,ac-emlkjtg-shard-00-02.izcbjtm.mongodb.net:27017/?ssl=true&replicaSet=atlas-ccxt8h-shard-0&authSource=admin&retryWrites=true&w=majority")

# db = client['example']
db = client.moviesdb
movie = db.movie
print('hi')
print('this is books',movie)
result = movie.find_one({'movie':"doctor"})
# result = book.find()

print(result)

# @app.route('/')
# def index():
#     return 'index page'
# @app.route('/books')
# def all_books():
#     books = db['books']
#     print(books)
#     data = books.find_one({"_id":ObjectId("63e48cb1072e86fe71490e1f")})
#     print(data)
#     # return jsonify({"data":data})
# all_books()

# if __name__ == "__main__":
#     app.run(debug=True,port=2023)