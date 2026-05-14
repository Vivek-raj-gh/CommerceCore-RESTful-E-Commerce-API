from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register New User
    ---
    tags:
      - 🔐 Authentication

    parameters:
      - in: body
        name: body
        required: true

        schema:
          type: object

          properties:
            username:
              type: string
              example: vivek

            password:
              type: string
              example: vivek123

    responses:
      200:
        description: User registered successfully
    """
    data = request.get_json()

    hashed_password = bcrypt.generate_password_hash(
        data['password']
    ).decode('utf-8')

    user = User(
        username=data['username'],
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    })

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    User Login
    ---
    tags:
      - 🔐 Authentication

    parameters:
      - in: body
        name: body
        required: true

        schema:
          type: object

          properties:
            username:
              type: string
              example: vivek

            password:
              type: string
              example: vivek123

    responses:
      200:
        description: JWT token generated
    """
    data = request.get_json()

    user = User.query.filter_by(
        username=data['username']
    ).first()

    if user and bcrypt.check_password_hash(
        user.password,
        data['password']
    ):

        access_token = create_access_token(
            identity=user.id
        )

        return jsonify({
            "token": access_token
        })

    return jsonify({
        "message": "Invalid credentials"
    }), 401