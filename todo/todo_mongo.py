import mongoengine as me
me.connect('mongo_test', host='localhost', port=27017)

class Post(me.Document):
    title = me.StringField(required=True, max_length=200)
    content = me.StringField()