from flask import Blueprint, request, abort
from init import db, bcrypt, ma
from datetime import date, datetime
from models.art import Art, ArtSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, JWTManager, create_access_token, jwt_required
from marshmallow import fields, validates

from models.user import User

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
    art.created = date.today() #art_fields['created'],#date.today(), #data['created'],
    art.descriptions = data['descriptions'],
    art.gallery_id = data['gallery_id'],
    art.artist_id = data['artist_id']

        # data = ArtSchema().load(request.json)

    # new_art = Art()
    # new_art.title = art_fields['title'],
    # new_art.creator = art_fields['creator'],
    # new_art.dimensions = art_fields['dimensions'],
    # new_art.color_pallet = art_fields['color_pallet'],
    # new_art.kilograms = art_fields['kilograms'],
    # new_art.price = art_fields['price'],
    # new_art.medium = art_fields['medium'],
    # new_art.created = date.today() #art_fields['created'],#date.today(), #data['created'],
    # new_art.descriptions = art_fields['descriptions'],
    # new_art.gallery_id = art_fields['gallery_id'],
    # new_art.artist_id = art_fields['artist_id']

    # Add and commit art to database
    db.session.add(art)
    db.session.commit()
    # let user know result
    return ArtSchema().dumps(art), 201

#input the id to let the server know which art to delete
@arts_bp.route("/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def arts_delete(id):
    #get the user id invoking get_jwt_identity
    user_id = get_jwt_identity()
    #Find it in the db
    user = User.query.get(user_id)
    #Make sure it is in the database
    #only allowing admin the ability to delete artworks
    if not user.is_admin:
        return abort(401, description="Invalid user")

    # find the art
    art = Art.query.filter_by(id=id).first()
    #if the art doesn't exist, return an error message
    if not Art:
        return abort(400, description= "Artwork does not exist")
    #Delete the art from the database and commit
    db.session.delete(art)
    db.session.commit()
    #return the card in the response
    return jsonify(ArtSchema.dump(art))
