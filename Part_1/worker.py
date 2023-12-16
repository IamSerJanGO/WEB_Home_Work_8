import argparse

from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from models import User, Quote
from settings import uri

# uri = "mongodb+srv://1000remons1000:uRjDhccw8EqUbyur@cluster0.opdn5du.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client.home_work_db

class Getter:
    def get_quotes_name(self, user_name):
        auothor = db.authors.find_one({ 'fullname': user_name })
        id_auothor = auothor.get('_id')
        qoutes_list = db.qoutes.find({'author': id_auothor})
        for value in qoutes_list:
            print(value.get('quote'))


    def get_quotes_tag(self, tag):
        obj = db.qoutes.find({'tags': {'$in': [tag]}})
        for elemen in obj:
            print(elemen.get('quote'))

    def get_quotes_many_tag(self, tags):
        obj_list = []
        for tag in tags:
            objs = db.qoutes.find({'tags': {'$in': [tag]}})
            for obj in objs:
                if obj not in obj_list:
                    obj_list.append(obj)
        for element in obj_list:
            print(element.get('quote'))




get_worker = Getter()

while True:
    print('Enter your command')
    user_command = input('-').split(':')
    if user_command[0] == 'eexit':
        break
    if len(user_command) < 2:
        print('Invalid command')
        continue

    if user_command[0] == 'name':
        author_name = user_command[1].strip()
        get_worker.get_quotes(author_name)
    elif user_command[0] == 'tag':
        tag = user_command[1].strip()
        get_worker.get_quotes_tag(tag)
    elif user_command[0] == 'tags':
        tags = user_command[1].strip().split(',')
        get_worker.get_quotes_many_tag(tags)







