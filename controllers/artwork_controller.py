from flask import Blueprint, request, abort
from init import db
from datetime import date
from models.art import Art, ArtSchema
from controllers.user_controller import authorize
from flask_jwt_extended import jwt_required

arts_bp = Blueprint('arts', __name__, url_prefix='/arts')

@arts_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_arts():
    stmt = db.select(Art)
    arts = db.session.scalars(stmt)
    return ArtSchema(many=True).dump(arts)

@arts_bp.route('/<int:id>/', methods=["GET"])
@jwt_required()
def one_art(id):
    stmt = db.select(Art).filter_by(id=id)
    art = db.session.scalar(stmt)
    return ArtSchema().dump(art)

@arts_bp.route('/create', methods=['POST'])
@jwt_required()
def create_art():
    data = ArtSchema().load(request.json)

    art = Art()
    art.title = data['title'],
    art.creator = data['creator'],
    art.dimensions = data['dimensions'],
    art.color_pallet = data['color_pallet'],
    art.kilograms = data['kilograms'],
    art.price = data['price'],
    art.medium = data['medium'],
    art.created = date.today()
    art.descriptions = data['descriptions'],
    art.gallery_id = data['gallery_id'],
    art.artist_id = data['artist_id'],

    # Add and commit art to database
    db.session.add(art)
    db.session.commit()
    # let user know result
    return ArtSchema().dumps(art), 201

@arts_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_single_artwork(id):
    stmt = db.select(Art).filter_by(id=id)
    art = db.session.scalar(stmt)
    if art:
        art.title = request.json.get('title') or art.title
        art.creator = request.json.get('creator') or art.creator
        art.dimensions = request.json.get('dimensions') or art.dimensions
        art.color_pallet = request.json.get('color_pallet') or art.color_pallet
        art.kilograms = request.json.get('kilograms') or art.kilograms
        art.price = request.json.get('price') or art.price
        art.medium = request.json.get('medium') or art.medium
        art.created = request.json.get('created') or art.created
        art.descriptions = request.json.get('descriptions') or art.descriptions
        art.gallery_id = request.json.get('gallery_id') or art.gallery_id
        art.artist_id = request.json.get('artist_id') or art.artist_id
        db.session.commit()
        return ArtSchema().dump(art)
    else:
        return {'error': f'Artwork was not found with the matching id of {id}, please try again.'}, 404

#input the id to let the server know which art to delete
@arts_bp.route("/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def arts_delete(id):
    authorize()
    stmt = db.select(Art).filter_by(id=id)
    art = db.session.scalar(stmt)
    if art:
        db.session.delete(art)
        db.session.commit()
        return {'message': f"Artwork '{art.title}' was successfully deleted."}
    else:
        return {'error': f'Artwork was not found with id {id} in our database.'}, 404
    