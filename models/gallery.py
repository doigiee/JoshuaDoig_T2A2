from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

class Gallery(db.Model):
    __tablename__ = 'gallerys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    phone = db.Column(db.Text)
    
    # arts_id = db.Column(db.Integer, db.ForeignKey('arts.id'), nullable=False)

    # art = db.relationship("Art", backref="gallerys")

class GallerySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location', 'phone', 'arts') 
        ordered = True


# sqlalchemy.exc.InvalidRequestError: Mapper 'mapped class Gallery->gallerys' has no property 'arts'

# sqlalchemy.exc.AmbiguousForeignKeysError: Could not determine join condition between parent/child tables on
# 		relationship Art.gallery - there are multiple foreign key paths linking the tables. Specify the 'foreign_keys'
# 		argument, providing a list of those columns which should be counted as containing a foreign key reference to the
# 		parent table.