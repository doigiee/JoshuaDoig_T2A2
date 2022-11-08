from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

class Gallery(db.Model):
    __tablename__ = 'gallerys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)
    
class GallerySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location', 'phone') 
        ordered = True

