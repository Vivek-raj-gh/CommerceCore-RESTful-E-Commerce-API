from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order

order_bp = Blueprint('orders', __name__)

@order_bp.route('/orders', methods=['POST'])
def place_order():

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