from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError


#representation of table in my database
class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)

#foreign key(s)
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=False)

    # gallery = db.relationship("Gallery", backref="artists")

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class ArtistSchema(ma.Schema):
    name = fields.String(required = False, validate= Regexp("^""([a-z])(?=.*"" [A-Z])?=.*(?=.*(?=.*\d)[])@$!%*?&[A-Za-z\d@$#$^()!%*?&]{8,}$", error='Please enter a valid title for your art.'))
    location = fields.String(required = False)
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long'))
#foreign key(s)
    gallery_id = fields.Integer(required = True) #validate=OneOf(VALID_GALLERIES_ID, error= "The gallery_id must be one of our registered galleries: '1', '2', or '3'"))
    artist_id = fields.Integer(required = True) #validate=OneOf(VALID_ARTISTS_ID, error= "The artist_id must be a registered number: '1', '2', '3', '4', '5', '6' or '7'."))
    
    class Meta:
        fields = ('id', 'name', 'location', 'phone', 'gallery') 
        ordered = True

