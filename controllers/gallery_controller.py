from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date
from models.gallery import Gallery, GallerySchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

gallerys_bp = Blueprint('gallerys', __name__, url_prefix='/gallerys')

@gallerys_bp.route('/', methods=["GET"])
# @jwt_required()
def get_all_gallerys():
    stmt = db.select(Gallery)#.order_by(Gallery.id())
    gallerys = db.session.scalars(stmt)
    return GallerySchema(many=True).dump(gallerys)

@gallerys_bp.route('/<int:id>/', methods=["GET"])
def one_gallery(id):
    stmt = db.select(Gallery)#.filter_by(id=id)
    gallery = db.session.scalar(stmt)
    return GallerySchema().dump(gallery)
    # return 'all_galleries route'
