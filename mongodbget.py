from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from random import randint
# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/local")
db=client.business
fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)
ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)
result = db.reviews.delete_many({'like': 1})
print('Number of  deleted : ' + str(result.deleted_count))
UpdatedDocument = db.reviews.find_one({'like': 1})
print('The deleted document:')
pprint(UpdatedDocument)
