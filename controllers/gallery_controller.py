from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date
from models.gallery import Gallery, GallerySchema
from controllers.user_controller import authorize
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, JWTManager, create_access_token, jwt_required

gallerys_bp = Blueprint('gallerys', __name__, url_prefix='/gallerys')

# to see all galleries
@gallerys_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_gallerys():
    stmt = db.select(Gallery)#.order_by(Gallery.id())
    gallerys = db.session.scalars(stmt)
    return GallerySchema(many=True).dump(gallerys)

# to see a specified gallery
@gallerys_bp.route('/<int:id>/', methods=["GET"])
@jwt_required()
def one_gallery(id):
    stmt = db.select(Gallery)#.filter_by(id=id)
    gallery = db.session.scalar(stmt)
    return GallerySchema().dump(gallery)
    # return 'all_galleries route'

#route to create a new gallery, only can be accessed by admin with a JWT token
@gallerys_bp.route('/create', methods=['POST'])
@jwt_required()
def create_gallery():
    authorize()
    data = GallerySchema().load(request.json)
    
    #variable storing the class
    gallery = Gallery()
    gallery.name = data['name'],
    gallery.location = data['location'],
    gallery.phone = data['phone']

    # Add and commit gallery to database
    db.session.add(gallery)
    db.session.commit()
    # let admin know the result
    return GallerySchema().dumps(gallery), 201

#input the id to let the server know which gallery to delete
@gallerys_bp.route("/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def gallery_delete(id):
    authorize()
    stmt = db.select(Gallery).filter_by(id=id)
    gallery = db.session.scalar(stmt)
    if gallery:
        db.session.delete(gallery)
        db.session.commit()
        return {'message': f"Gallery '{gallery.id}' was successfully deleted."}
    else:
        return {'error': f'Gallery was not found with id {id} in our database.'}, 404
