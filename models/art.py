from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

VALID_TYPES = ['John Smithers', 'Sandra Bullocks', 'Jimmy Barnes', 'Matthew Finley', 'Chris Hemsrunt', 'Sammy Tammy', 'Jacob Googels']
#will need to come in and manually change this when adding more galleries or artists. its okay for now, works though for large-scale will need to optimise.
# VALID_GALLERY = [1, 2, 3]
# VALID_ARTISTS = [1, 2, 3, 4, 5, 6, 7]

#representation of table in my database
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

#foreign key(s)
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=True)
    artist_id= db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=True)

    # gallery = db.relationship("Gallery", backref="art", cascade='all, delete')
    # artist = db.relationship("Artist", back_populates="arts")

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class ArtSchema(ma.Schema):
    title = fields.String(required = False)
    creator = fields.String(required = False, validate=OneOf(VALID_TYPES, error= "The creator must be one of our registered artists: 'John Smithers', 'Sandra Bullocks', 'Jimmy Barnes', 'Matthew Finley', 'Chris Hemsrunt', 'Sammy Tammy', 'Jacob Googels'."))
    dimensions = fields.String(required = False) 
    color_pallet = fields.String(required = False)
    kilograms = fields.String(required = False)
    price = fields.String(required = True)
    medium = fields.String(required = False)
    created = fields.String(required = False)
    descriptions = fields.String(required = True, validate=Length(min=2, error="description must be at least 2 characters in length"))
#foreign key(s)
    #error = "your artist id doesnt exist"),#
    gallery_id = fields.Integer(required = False)# validate=OneOf(VALID_GALLERY, error= "The gallery_id must be one of our registered galleries: eg. '1', '2','3', etc"))
    artist_id = fields.Integer(required = False)# validate=OneOf(VALID_ARTISTS, error= "The artist_id must be a registered number: eg. '1', '2', '3', '4', '5', '6', '7', etc."))
    # gallery_id = fields.Integer(required = True, validate=Regexp('0123456789', error= "The gallery_id must be one of our registered galleries: eg. '1', '2', or '3'"))
    # artist_id = fields.Integer(required = True, validate=Regexp('0123456789', error= "The artist_id must be a registered number: eg. '1', '2', '3', '4', '5', '6' or '7'."))
class Meta:
    fields = ('id', 'title', 'creator', 'dimensions', 'color_pallet', 'kilograms', 'price', 'medium', 'created', 'descriptions', 'gallery_id', 'artist_id') 
    ordered = True

    