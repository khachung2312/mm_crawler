from mongoengine import Document, StringField, IntField, DateTimeField

class TinDangXe(Document):
    url = StringField(unique=True)
    title = StringField(required=True)

