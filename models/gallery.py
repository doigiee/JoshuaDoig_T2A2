from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp


#representation of table in my database
class Gallery(db.Model):
    __tablename__ = 'gallerys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)

# made it so that if a gallery is deleted, all associated, artists, artworks and customers are deleted.
#Thus this could represent a closure sort of situation.

    artists = db.relationship("Artist", backref="gallery", cascade='all, delete')
    customers = db.relationship("Customer", backref="gallery", cascade='all, delete')
    arts = db.relationship("Art", backref="gallery", cascade='all, delete')
    

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class GallerySchema(ma.Schema):
    name = fields.String(required = True, validate=And(
        Length(min=2, error='Your title needs to be at least 2 characters long'), 
        Regexp('^[a-zA-Z0-9 ]+$', error= 'Letters, numbers and spaces are the only accepted inputs for a title')))
    location = fields.String(required = False, validate=Length(min=2, error='addresses must be at least 2 characters long'))
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long')) 
    
    class Meta:
        fields = ('id', 'name', 'location', 'phone') 
        ordered = True