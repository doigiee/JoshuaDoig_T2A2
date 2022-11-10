from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date
from models.artist import Artist, ArtistSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, JWTManager, create_access_token, jwt_required

artists_bp = Blueprint('artists', __name__, url_prefix='/artists')

@artists_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_artists():
    stmt = db.select(Artist)#.order_by(Artist.id())
    artists = db.session.scalars(stmt)
    return ArtistSchema(many=True).dump(artists)

@artists_bp.route('/<int:id>/', methods=["GET"])
@jwt_required()
def one_artist(id):
    stmt = db.select(Artist).filter_by(id=id)
    artist = db.session.scalar(stmt)
    return ArtistSchema().dump(artist)
    # return 'all_artists route'

    # if not authorize():
    # return {'error': 'You must be an admin'}, 401
