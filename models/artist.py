from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

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
    name = fields.String(required = False) 
    location = fields.String(required = False)
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long'))
#foreign key(s)
    gallery_id = fields.Integer(required = False) 
    
    class Meta:
        fields = ('id', 'name', 'location', 'phone', 'gallery_id') 
        ordered = True

