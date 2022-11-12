from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, OneOf, And, Regexp

VALID_COLOR_PALLETS = ('red', 'grey', 'blue', 'yellow', 'green', 'purple', 'grey', 'silver', 'white', 'black')

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
# not all fields need to be filled, sometimes artworks are untitled, thus i left them required = false
    title = fields.String(required = False, validate=And(
        Length(min=2, error='Your title needs to be at least 2 characters long'), 
        Regexp('^[a-zA-Z0-9 ]+$', error= 'Letters, numbers and spaces are the only accepted inputs for a title')))
    creator = fields.String(required = False, validate=Length(min=2, error='Your creator needs to be at least 2 characters long'))
    dimensions = fields.String(required = False, validate=Regexp('^[a-zA-Z0-9 ]+$', error= 'Letters, numbers and spaces are the only accepted inputs for dimensions')) 
    color_pallet = fields.String(required = False, validate=OneOf(VALID_COLOR_PALLETS))
    kilograms = fields.String(required = False, validate=Regexp('^[a-zA-Z0-9 ]+$', error= 'Letters, numbers and spaces are the only accepted inputs for kilograms'))
    price = fields.String(required = True, validate=Regexp('^[a-zA-Z0-9$ ]+$', error= 'Letters, numbers, spaces and $ symbol are the only accepted inputs for a price'))
    medium = fields.String(required = False, validate=Regexp('^[a-zA-Z0-9 ]+$', error= 'Letters, numbers and spaces are the only accepted inputs for a medium'))
    created = fields.String(required = False) #uses date today as to why not needed to validate
    descriptions = fields.String(required = True, validate=Length(min=2, error="description must be at least 2 characters in length"))
#foreign key(s)
    gallery_id = fields.Integer(required = False)
    artist_id = fields.Integer(required = False)
    
class Meta:
    fields = ('id', 'title', 'creator', 'dimensions', 'color_pallet', 'kilograms', 'price', 'medium', 'created', 'descriptions', 'gallery_id', 'artist_id') 
    ordered = True
    