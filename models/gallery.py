from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

#representation of table in my database
class Gallery(db.Model):
    __tablename__ = 'gallerys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)
    
    # arts_id = db.Column(db.Integer, db.ForeignKey('arts.id'), nullable=False)

    # art = db.relationship("Art", backref="gallerys")


    # art = db.relationship("Gallery", backref="gallerys")
    # artist = db.relationship("Artist", backref="gallerys")
    # customer = db.relationship("Customer", backref="gallerys")

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class GallerySchema(ma.Schema):
    name = fields.String(required = True)
    location = fields.String(required = False)
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long')) 
    
    class Meta:
        fields = ('id', 'name', 'location', 'phone') 
        ordered = True