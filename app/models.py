from app import db
import datetime

db.connect('goodwood')


class LineItem(db.Document):
    line_number = db.StringField()
    item = db.StringField()
    created = db.DateTimeField(default=datetime.datetime.utcnow)  # utc to keep it universal

    meta = {
        'indexes': [
            ('line_number', '-created')
        ]
    }

    def __repr__(self):
        return '<Line %r>' % self.line_number


class Cvi(db.Document):
    contractor = db.StringField()
    employer = db.StringField()
    project = db.StringField()
    cvi_number = db.IntField()
    cvi_line_item = db.ListField(db.ReferenceField(LineItem))
    date = db.DateField(default=datetime.datetime.now)

    meta = {'allow_inheritance': True}

    def __repr__(self):
        return '<Cvi %r>' % self.project
