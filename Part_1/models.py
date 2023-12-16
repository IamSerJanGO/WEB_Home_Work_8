import json

from mongoengine import connect, Document, StringField, IntField, ListField, ReferenceField
from settings import db_name, uri
import argparse

parser = argparse.ArgumentParser('Loader parser')
parser.add_argument('--action', help='update_users, update_quote')
parser.add_argument('--update_users')
parser.add_argument('--update_quote')
arg = vars(parser.parse_args())

connect(db=db_name, host=uri)

class User(Document):
    fullname = StringField( max_length= 70,required=True)
    born_date= StringField(max_length=40)
    born_location = StringField(max_length=50)
    description = StringField()
    meta = {
        'collection': 'authors'
    }


class Quote(Document):
    tags = ListField()
    author = ReferenceField(User, required=True)
    quote = StringField(required=True)
    meta = {
        'collection': 'qoutes'
    }

class Loader:

    def reader_author(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            try:
                new_user = User(fullname=item.get('fullname'),
                                born_date=item.get('born_date'),
                                born_location=item.get('born_location'),
                                description=item.get('description'))
                new_user.save()
            except:
                print('Invalid format')

    def reader_quote(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            quotes_data = json.load(file)

        for quote_info in quotes_data:
            author_name = quote_info.get('author')
            author = User.objects(fullname=author_name).first()
            if not author:
                author = User(fullname=author_name)
                author.save()

            new_quote = Quote(
                tags=quote_info.get('tags'),
                author=author,
                quote=quote_info.get('quote')
            )
            new_quote.save()

if arg['action'] == 'update_users' and arg['update_users']:
    print('hi')
    loader = Loader()
    loader.reader_author(arg['update_users'])
    print('hu')

elif arg['action'] == 'update_quote' and arg['update_quote']:
    loader = Loader()
    loader.reader_quote(arg['update_quote'])

else:
    print('Invalid arguments provided.')

