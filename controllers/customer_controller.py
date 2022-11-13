from flask import Blueprint, request
from init import db
from models.customer import Customer, CustomerSchema
from controllers.user_controller import authorize
from flask_jwt_extended import jwt_required

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')

# to see all customers from the database by querying them
@customers_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_customers():
    stmt = db.select(Customer)
    customers = db.session.scalars(stmt)
    return CustomerSchema(many=True).dump(customers)

# to see a single customer by calling their id integer
@customers_bp.route('/<int:id>/', methods=["GET"])
@jwt_required()
def one_customer(id):
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    return CustomerSchema().dump(customer)

# to create a user
@customers_bp.route('/create', methods=['POST'])
@jwt_required()
def create_customer():
    data = CustomerSchema().load(request.json)

    customer = Customer()
    customer.name = data['name'],
    customer.phone = data['phone'],
    customer.address = data['address'],
    customer.gallery_id = data['gallery_id']

    # Add and commit customer to database
    db.session.add(customer)
    db.session.commit()
    # let user know result
    return CustomerSchema().dumps(customer), 201

# to update customer name, location, phone and gallery
@customers_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_single_customer(id):
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        customer.name = request.json.get('name') or customer.name
        customer.location = request.json.get('location') or customer.location
        customer.phone = request.json.get('phone') or customer.phone
        customer.gallery_id = request.json.get('gallery_id') or customer.gallery_id
        db.session.commit()      
        return CustomerSchema().dump(customer)
    else:
        return {'error': f'Customer was not found with the matching id of {id}, please try again.'}, 404

#input the id to let the server know which customer to delete, admin/dev only
@customers_bp.route("/delete/<int:id>", methods=["DELETE"])
@jwt_required()
def customer_delete(id):
    authorize()
    stmt = db.select(Customer).filter_by(id=id)
    customer = db.session.scalar(stmt)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return {'message': f"Customer '{id}' was successfully deleted."}
    else:
        return {'error': f'Customer was not found with id {id} in our database.'}, 404
