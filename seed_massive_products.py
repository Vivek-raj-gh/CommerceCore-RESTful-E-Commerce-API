import random

from faker import Faker

from app import app
from extensions import db
from models.product import Product

fake = Faker()

categories = [
    "Electronics",
    "Fashion",
    "Books",
    "Gaming",
    "Home",
    "Sports",
    "Beauty",
    "Groceries"
]

with app.app_context():

    for _ in range(1000):

        product = Product(

            name=fake.unique.catch_phrase(),

            description=fake.text(max_nb_chars=200),

            category=random.choice(categories),

            image_url="https://picsum.photos/200",

            price=round(random.uniform(100, 100000), 2),

            stock=random.randint(1, 500)
        )

        db.session.add(product)

    db.session.commit()

    print("1000 products inserted successfully!")