from  mongoengine import Document, StringField, BooleanField, IntField, connect
from settings import uri, db_name_second_part
from faker import Faker
from  random import  randint

fake = Faker()

connect(db=db_name_second_part, host=uri)

class User(Document):
    fullname = StringField(max_length=70)
    email = StringField(max_length=110)
    age = IntField()
    worded_place = StringField(max_length=100)
    logic_field = BooleanField(default=False)
    meta = {
        'collection': 'users'
    }

class Generator:

    def generator(self, users:int):
        for _ in range(users):
            user = User(fullname=fake.name(),
                        email=fake.email(),
                        age=randint(18, 90),
                        worded_place=fake.company(),
                        )
            user.save()

    def __call__(self, users:int):
        if not isinstance(users, int):
            print('Incorrect data type')
            return
        else:
            self.generator(users)

if __name__ == '__main__':
    generate = Generator()
    generate(int(input('Enter the number of records: ')))
