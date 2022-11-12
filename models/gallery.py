from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


#representation of table in my database
class Gallery(db.Model):
    __tablename__ = 'gallerys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)

# decided not to use cascade delete, figured that just because a gallery can be closed, 
# doesn't necessary mean that artworks, customers, or artists disappear, they will manually
# just need to be given a new gallery through a PATCH or database entry.

    artists = db.relationship("Artist", backref="gallery")
    customers = db.relationship("Customer", backref="gallery")
    arts = db.relationship("Art", backref="gallery")

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class GallerySchema(ma.Schema):
    name = fields.String(required = True)
    location = fields.String(required = False)
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long')) 
    
    class Meta:
        fields = ('id', 'name', 'location', 'phone') 
        ordered = True