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
    """
    Get Products with Pagination
    ---
    tags:
      - 🛍️ Products

    parameters:

      - name: page
        in: query
        type: integer
        required: false
        default: 1

      - name: per_page
        in: query
        type: integer
        required: false
        default: 10

    responses:
      200:
        description: Paginated product list
    """

    page = request.args.get('page', 1, type=int)

    per_page = request.args.get('per_page', 10, type=int)

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
            "stock": product.stock
        })

    return jsonify({

        "page": page,

        "per_page": per_page,

        "total_products": pagination.total,

        "total_pages": pagination.pages,

        "has_next": pagination.has_next,

        "has_prev": pagination.has_prev,

        "products": products
    })