from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

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

    # gallery = db.relationship("Gallery", backref="arts")
    # artist = db.relationship("Artist", backref="arts")


class ArtSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'creator', 'dimensions', 'color_pallet', 'kilograms', 'price', 'medium', 'created', 'descriptions', 'gallery', 'artist') 
        ordered = True

    