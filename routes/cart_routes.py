from flask import Blueprint, request, jsonify
from extensions import db
from models.cart import Cart

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    """
    Add Product to Cart
    ---
    tags:
      - 🛒 Cart

    parameters:

      - in: body
        name: body
        required: true

        schema:
          type: object

          properties:

            user_id:
              type: integer
              example: 1

            product_id:
              type: integer
              example: 5

            quantity:
              type: integer
              example: 2

    responses:
      200:
        description: Product added to cart successfully
    """

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

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    """
    Get User Cart
    ---
    tags:
      - 🛒 Cart

    parameters:

      - name: user_id
        in: path
        type: integer
        required: true
        example: 1

    responses:
      200:
        description: Returns all cart items for user
    """

    cart_items = Cart.query.filter_by(
        user_id=user_id
    ).all()

    result = []

    for item in cart_items:

        result.append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity
        })

    return jsonify(result)