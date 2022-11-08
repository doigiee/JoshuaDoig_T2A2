from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date
from models.art import Art, ArtSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

arts_bp = Blueprint('arts', __name__, url_prefix='/arts')

@arts_bp.route('/')
#@jwt_required()
def get_all_arts():
    stmt = db.select(Art).order_by(Art.title.desc())
    arts = db.session.scalars(stmt)
    return ArtSchema(many=True).dump(arts)

@arts_bp.route('/<int:id>/')
def one_art(id):
    stmt = db.select(Art).filter_by(id=id)
    art = db.session.scalar(stmt)
    return ArtSchema().dump(art)
