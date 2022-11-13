from flask import Blueprint, request
from init import db
from models.artist import Artist, ArtistSchema
from controllers.user_controller import authorize
from flask_jwt_extended import jwt_required

#artist blueprint
artists_bp = Blueprint('artists', __name__, url_prefix='/artists')

#get all artists from requesting them from database
@artists_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_artists():
    stmt = db.select(Artist)#.order_by(Artist.id())
    artists = db.session.scalars(stmt)
    return ArtistSchema(many=True).dump(artists)

# call and request a single artist from database by calling their id 
@artists_bp.route('/<int:id>/', methods=["GET"])
@jwt_required()
def one_artist(id):
    stmt = db.select(Artist).filter_by(id=id)
    artist = db.session.scalar(stmt)
    return ArtistSchema().dump(artist)
     
#create a single artist
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

#update a single artist
@artists_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_single_artist(id):
    stmt = db.select(Artist).filter_by(id=id)
    artist = db.session.scalar(stmt)
    if artist:
        artist.name = request.json.get('name') or artist.name
        artist.location = request.json.get('location') or artist.location
        artist.phone = request.json.get('phone') or artist.phone
        artist.gallery_id = request.json.get('gallery_id') or artist.gallery_id
        db.session.commit()
        return ArtistSchema().dump(artist)
    else:
        return {'error': f'Artist was not found with the matching id of {id}, please try again.'}, 404

#input the id to let the server know which artist to delete, admin/dev only
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
