from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

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
#decided not to perfectly follow plan of ERD though did implement some constraints and messages in terms of input-able data and constraints
class ArtSchema(ma.Schema):
    title = fields.String(required = False)
    creator = fields.String(required = False)
    dimensions = fields.String(required = False) 
    color_pallet = fields.String(required = False)
    kilograms = fields.String(required = False)
    price = fields.String(required = True)
    medium = fields.String(required = False)
    created = fields.String(required = False)
    descriptions = fields.String(required = True, validate=Length(min=2, error="description must be at least 2 characters in length"))
#foreign key(s)
    #error = "your artist id doesnt exist"),#
    gallery_id = fields.Integer(required = False)
    artist_id = fields.Integer(required = False)
    
class Meta:
    fields = ('id', 'title', 'creator', 'dimensions', 'color_pallet', 'kilograms', 'price', 'medium', 'created', 'descriptions', 'gallery_id', 'artist_id') 
    ordered = True


# "OneOf" 
# example though not used in final production

# maybe not the best thing, as if a new artwork is created it can only be one of these listed registered artists, basically ruling out the use of creating new artists,
# though as it's showing I can use 'Oneof' I'll leave this here as a demonstration, though in final production would probably advise omitting this use of 'Oneof'. 
# it just means for the meantime the dev would need to come in here and insert all new registered artists upon reviewing that they are infact an artist they wish to register.
#VALID_TYPES = ['John Smithers', 'Sandra Bullocks', 'Jimmy Barnes', 'Matthew Finley', 'Chris Hemsrunt', 'Sammy Tammy', 'Jacob Googels']
#validate=OneOf(VALID_TYPES, error= "The creator must be one of our registered artists: 'John Smithers', 'Sandra Bullocks', 'Jimmy Barnes', 'Matthew Finley', 'Chris Hemsrunt', 'Sammy Tammy', 'Jacob Googels'."))

    