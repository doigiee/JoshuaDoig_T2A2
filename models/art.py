from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

VALID_TYPES = ['John Smithers', 'Sandra Bullocks', 'Jimmy Barnes', 'Matthew Finley', 'Chris Hemsrunt', 'Sammy Tammy', 'Jacob Googels']
# VALID_GALLERIES_ID = [1, 2, 3]
# VALID_ARTISTS_ID = [1, 2, 3, 4, 5, 6, 7]

class Art(db.Model):
    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    creator = db.Column(db.Text)
    dimensions = db.Column(db.Text)
    color_pallet = db.Column(db.Text)
    kilograms = db.Column(db.Text)
    price = db.Column(db.Text)
    medium = db.Column(db.Text)
    created = db.Column(db.Date)
    descriptions = db.Column(db.Text)

    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=False)
    artist_id= db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    # gallery = db.relationship("Gallery", back_populates="arts")
    # artist = db.relationship("Artist", back_populates="arts")


class ArtSchema(ma.Schema):
    title = fields.String(required = False, validate= Regexp('^[a-zA-Z. &:;]+$', error='Please enter a valid title for your art.'))
    creator = fields.String(required = False, validate=OneOf(VALID_TYPES, error= "The creator must be one of our registered artists: 'John Smithers', 'Sandra Bullocks', 'Jimmy Barnes', 'Matthew Finley', 'Chris Hemsrunt', 'Sammy Tammy', 'Jacob Googels'."))
    dimensions = fields.String(required = False) 
    color_pallet = fields.String(required = False)
    kilograms = fields.String(required = False)
    price = fields.String(required = True)
    medium = fields.String(required = False)
    created = fields.String(required = False)
    descriptions = fields.String(required = True, validate=Length(min=1, error="description must be at least 1 character in length"))
    gallery_id = fields.Integer(required = True) #validate=OneOf(VALID_GALLERIES_ID, error= "The gallery_id must be one of our registered galleries: '1', '2', or '3'"))
    artist_id = fields.Integer(required = True) #validate=OneOf(VALID_ARTISTS_ID, error= "The artist_id must be a registered number: '1', '2', '3', '4', '5', '6' or '7'."))
    
    class Meta:
        fields = ('id', 'title', 'creator', 'dimensions', 'color_pallet', 'kilograms', 'price', 'medium', 'created', 'descriptions', 'gallery_id', 'artist_id') 
        ordered = True

    