from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

#representation of table in my database
class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)

#foreign key(s)
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=True)
    artists = db.relationship('Art', backref='artists', cascade='all, delete')

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class ArtistSchema(ma.Schema):
    name = fields.String(required = False, validate=And(
        Length(min=2, error='Your title needs to be at least 2 characters long'), 
        Regexp('^[a-zA-Z0-9 ]+$', error= 'Letters, numbers and spaces are the only accepted inputs for a title'))) 
    location = fields.String(required = False, validate=Length(min=2, error='location must be at least 2 numbers long'))
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long'))
#foreign key(s)
    gallery_id = fields.Integer(required = False) 
    
    class Meta:
        fields = ('id', 'name', 'location', 'phone', 'gallery_id') 
        ordered = True

