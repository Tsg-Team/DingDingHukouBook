# coding=utf-8
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
    cborrower = StringField(default="无")
    cphone = StringField(default="无")
    creason = StringField(default="无")
    nborrower = StringField(default="无")
    nphone = StringField(default="无")
    napartment = StringField(default="无")
    nreason = StringField(default="无")
    staffs = ListField(EmbeddedDocumentField('Staff'))
