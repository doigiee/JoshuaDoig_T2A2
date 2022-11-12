from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp


#representation of table in my database
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

#representation for flask CRUD methods
# Marshmallow used for validation requirements
class UserSchema(ma.Schema):
    name = fields.String(required = False)
    email = fields.String(required = True, validate = Regexp("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", error="Only vaild emails will be accepted, please try again."))
    password = fields.String(required = True, validate= Regexp("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", error='Try another password, special characters are permitted.'))
    is_admin = fields.String(required = True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'is_admin') #, 'customers', 'artists')
        password = ma.String(validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)