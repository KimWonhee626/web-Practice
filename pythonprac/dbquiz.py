from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix = db.movies.find_one({'title':'매트릭스'}, {'_id':False})
matrix_star = matrix['star']

same_star = list(db.movies.find({'star':matrix_star}, {'_id':False}))

for target in same_star:
    print(target['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
