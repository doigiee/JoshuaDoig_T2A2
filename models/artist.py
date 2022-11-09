from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)
    
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=False)

    # gallery = db.relationship("Gallery", backref="artists")

class ArtistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location', 'phone', 'gallery') 
        ordered = True

