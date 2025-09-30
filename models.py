from mongoengine import *

connect('cookieTest')

class User(Document):
    userid = StringField()
    username = StringField()
    password = StringField()
    content = StringField()

