from flask import Blueprint, request, jsonify
from extensions import db
from models.product import Product

product_bp = Blueprint('products', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():

    data = request.get_json()

    product = Product(
        name=data['name'],
        price=data['price'],
        stock=data['stock']
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product added successfully"
    })

@product_bp.route('/products', methods=['GET'])
def get_products():

    page = request.args.get('page', 1, type=int)

    per_page = request.args.get('per_page', 5, type=int)

    pagination = Product.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    products = []

    for product in pagination.items:

        products.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "category": product.category,
            "stock": product.stock
        })

    return jsonify({
        "page": page,
        "total_pages": pagination.pages,
        "total_products": pagination.total,
        "products": products
    })