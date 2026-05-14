from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt

from flasgger import Swagger

from flask_cors import CORS

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    swagger_template = {

        "swagger": "2.0",
    
        "info": {
            "title": "CommerceCore REST API",
            "description": "RESTful E-Commerce API Documentation",
            "version": "1.0"
        },
    
        "tags": [
        
            {
                "name": "🔐 Authentication",
            },
    
            {
                "name": "🛍️ Products",                
            },
    
            {
                "name": "📦 Orders",
            },
    
            {
                "name": "🛒 Cart",
            }
        ]
    }
    
    Swagger(app, template=swagger_template)
    
    from routes.auth_routes import auth_bp
    from routes.product_routes import product_bp
    from routes.order_routes import order_bp
    from routes.cart_routes import cart_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(cart_bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)