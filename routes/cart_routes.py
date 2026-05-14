from flask import Blueprint, request, jsonify
from extensions import db
from models.cart import Cart

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():

    data = request.get_json()

    cart = Cart(
        user_id=data['user_id'],
        product_id=data['product_id'],
        quantity=data['quantity']
    )

    db.session.add(cart)
    db.session.commit()

    return jsonify({
        "message": "Product added to cart"
    })