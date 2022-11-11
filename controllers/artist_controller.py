from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date
from models.artist import Artist, ArtistSchema
from controllers.user_controller import authorize
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

@artists_bp.route('/create', methods=['POST'])
@jwt_required()
def create_artist():
    data = ArtistSchema().load(request.json)

    artist = Artist()
    artist.name = data['name'],
    artist.location = data['location'],
    artist.phone = data['phone'],
    artist.gallery_id = data['gallery_id']

    # Add and commit artist to database
    db.session.add(artist)
    db.session.commit()
    # let user know result
    return ArtistSchema().dumps(artist), 201

#input the id to let the server know which artist to delete
@artists_bp.route("/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def artist_delete(id):
    authorize()
    stmt = db.select(Artist).filter_by(id=id)
    artist = db.session.scalar(stmt)
    if artist:
        db.session.delete(artist)
        db.session.commit()
        return {'message': f"Artist '{id}' was successfully deleted."}
    else:
        return {'error': f'Artist was not found with id {id} in our database.'}, 404
