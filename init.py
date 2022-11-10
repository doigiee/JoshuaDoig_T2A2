#This file contains and uses the main imports needed for my app.
from flask_sqlalchemy import SQLAlchemy
#SQLAlchemy is an SQL toolkit that provides efficient and high-performing database access for relational databases or Object Relational Mapping

from flask_marshmallow import Marshmallow
#Integrates the marshmallow serialization/deserialization library with my Flask application.
#adds URL and Hyperlinks fields for my API

from flask_bcrypt import Bcrypt
#provides bcrypt hashing utilities for my application

from flask_jwt_extended import JWTManager
#used to create JSON Web Tokens, when used correctly will allow higher level of security and data protection.

#contained within variables for easier call methods and imports
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
