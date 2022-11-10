from flask import Flask

#serialised SQLAlchemy, Marshmallow, Bcrypt, and JWT calls from init
from init import db, ma, bcrypt, jwt

#imports of my controllers and blueprints, registered at bottom of page
from controllers.artwork_controller import arts_bp
from controllers.gallery_controller import gallerys_bp
from controllers.customer_controller import customers_bp
from controllers.artist_controller import artists_bp
from controllers.user_controller import users_bp
from controllers.cli_controller import db_commands

#Raised when an invalid operation is performed
from marshmallow.exceptions import ValidationError
import os

#creating the app
def create_app():
    app = Flask(__name__)


# error messages returned as JSON not HTML, return message plus error codes
    @app.errorhandler(400)
    def incorrect_request(err):
        return {'error': str(err)}, 400
#imported from marshmallow.exceptions
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400
#not found
    @app.errorhandler(404)
    def not_found_error(err):
        return {'error': str(err)}, 404
#unauthorized
    @app.errorhandler(401)
    def unauthorized_error(err):
        return {'error': str(err)}, 401
#KeyError
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error' : f'The field {err} is required'}, 400

#application configurations, database connection, and JWT_SECRET_KEY setup
    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
#create instances of the components
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
#register blueprints
    app.register_blueprint(arts_bp) 
    app.register_blueprint(gallerys_bp)
    app.register_blueprint(customers_bp) 
    app.register_blueprint(artists_bp) 
    app.register_blueprint(users_bp)
#separated blueprints from others
    app.register_blueprint(db_commands)

    return app