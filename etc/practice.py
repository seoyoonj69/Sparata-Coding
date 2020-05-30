from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

db.movies.update_one({'star':9.39},{'$set':{'star':0}})