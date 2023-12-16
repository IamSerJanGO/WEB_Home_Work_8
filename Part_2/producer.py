import pika

from pymongo.mongo_client import MongoClient
from settings import uri
from  models import  Generator

generate_data = Generator()
generate_data(int(input('Enter the number of records: ')))

client = MongoClient(uri)
db = client.home_work_2

users = db.users.find({'logic_field': False})

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connecion = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connecion.channel()

    channel.queue_declare('send_users')

    count = 1
    for user in users:
        channel.basic_publish(exchange='', routing_key='send_users', body=str(user.get('_id')).encode())
        print(f'The task {count} has been sent to the queue')
        count += 1

    channel.close()

main()
