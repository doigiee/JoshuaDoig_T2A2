from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date
from models.customer import Customer, CustomerSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')

@customers_bp.route('/')
#@jwt_required()
def get_all_customers():
    # return 'get all'
    stmt = db.select(Customer)
    customers = db.session.scalars(stmt)
    return CustomerSchema(many=True).dump(customers)

@customers_bp.route('/<int:id>/')
def one_customer(id):
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    return CustomerSchema().dump(customer)

    # return 'all_customers route'w

    # if not authorize():
    # return {'error': 'You must be an admin'}, 401
