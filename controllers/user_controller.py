from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required



users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=["GET"])
@jwt_required()
def get_all_users():
    stmt = db.select(User)#.order_by(User.id())
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

@users_bp.route('/register/', methods=['POST'])
def user_register():
    try:
        # Create a new user model from user information
        user = User(
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            name = request.json.get('name')
        )
        # Add and then commit the user to the database
        db.session.add(user)
        db.session.commit()
        # Respond to client
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Sorry, please try again, that email is current unavailable or in use'}, 409


@users_bp.route('/login/', methods=['POST'])
def user_login():
    # user found by email
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    # When user exists and password entered is correct
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        # return UserSchema(exclude=['password']).dump(user)
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email or password'}, 401
    
# for admins with priveleges to authorize
def authorize():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)