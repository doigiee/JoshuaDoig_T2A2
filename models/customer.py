from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, OneOf,Regexp


#representation of table in my database
class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)

#foreign key(s)
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=True)

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class CustomerSchema(ma.Schema):
    name = fields.String(required = False, validate= Regexp('^[a-zA-Z. &:;]+$', error='Please enter a valid title for your art.'))
    phone = fields.String(required = True, validate=Length(min=9, error='phone number entries must be at least 9 numbers long'))
    address = fields.String(required = False) 
#foreign key(s)
    gallery_id = fields.Integer(required = False) 
    
    class Meta:
        fields = ('id', 'name', 'phone', 'address', 'gallerys') 
        ordered = True

