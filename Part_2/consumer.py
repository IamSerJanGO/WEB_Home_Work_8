import pika
from pymongo.mongo_client import MongoClient
from settings import uri, db_name_second_part
from bson import ObjectId

client = MongoClient(uri)
db = client.home_work_2


def take_user(user_id):
    db.users.update_one({'_id': ObjectId(user_id.decode())}, {'$set': {'logic_field': True}})

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare('send_users')

    def collbak(ch, method, properties, body):
        take_user(body)
        print(f"Processed message: {body.decode()}")

    channel.basic_consume(queue='send_users', on_message_callback=collbak)
    channel.start_consuming()

main()



