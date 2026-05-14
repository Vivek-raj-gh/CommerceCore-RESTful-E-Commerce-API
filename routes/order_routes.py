from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order

order_bp = Blueprint('orders', __name__)

@order_bp.route('/orders', methods=['POST'])
def place_order():
    """
    Place New Order
    ---
    tags:
      - 📦 Orders

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

            total_amount:
              type: number
              example: 4999

    responses:
      200:
        description: Order placed successfully
    """

    data = request.get_json()

    order = Order(
        user_id=data['user_id'],
        total_amount=data['total_amount']
    )

    db.session.add(order)

    db.session.commit()

    return jsonify({
        "message": "Order placed successfully"
    })

@order_bp.route('/orders/<int:user_id>', methods=['GET'])
def get_orders(user_id):
    """
    Get User Orders
    ---
    tags:
      - 📦 Orders

    parameters:

      - name: user_id
        in: path
        type: integer
        required: true
        example: 1

    responses:
      200:
        description: Returns user orders
    """

    orders = Order.query.filter_by(
        user_id=user_id
    ).all()

    result = []

    for order in orders:

        result.append({
            "id": order.id,
            "total_amount": order.total_amount
        })

    return jsonify(result)