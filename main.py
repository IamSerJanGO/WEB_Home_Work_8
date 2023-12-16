from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://1000remons1000:uRjDhccw8EqUbyur@cluster0.opdn5du.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.test
#
# # Send a ping to confirm a successful connection
# db.cats.insert_many([
#     {
#         'name': 'Lama',
#         'age': 2,
#         'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
#     },
#     {
#         'name': 'Liza',
#         'age': 4,
#         'features': ['ходить в лоток', 'дає себе гладити', 'білий'],
#     },
# ])
#
# import redis
# from redis_lru import RedisLRU
#
# client = redis.StrictRedis(host="localhost", port=6379, password=None)
# cache = RedisLRU(client)
#
#
# @cache
# def f(x):
#     print(f"Function call f({x})")
#     return x
#
#
# if __name__ == '__main__':
#     print(f"Result f(3): {f(3)}")
#     print(f"Result f(3): {f(4)}")
import pika


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello_world')
    # data =input('enter daa: ')
    channel.basic_publish(exchange='', routing_key='hello_world', body=input('enter daa: ').encode())
    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    main()