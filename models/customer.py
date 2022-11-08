from init import db, ma
from marshmallow import fields, validates
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallerys.id'), nullable=False)

    gallery = db.relationship("Gallery", back_populates="customers")


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone', 'address', 'gallery') 
        ordered = True

