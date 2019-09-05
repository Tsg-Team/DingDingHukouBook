from mongoengine import *

connect('run', host='119.29.187.65', port=27017)

class Staff(EmbeddedDocument):
    userId = StringField()
    name = StringField()
    avatar = StringField()


class Account(Document):
    bookNum = StringField()
    bookName = StringField()
    bookStatus = StringField()
    borrowStatus = IntField()
    department = StringField()
    status = StringField()
    bookRemark = StringField()
    staffs = ListField(EmbeddedDocumentField('Staff'))
