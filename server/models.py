# server/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = "plants"

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    # Constructor (optional, but good for clarity)
    def __init__(self, name, image=None, price=None):
        self.name = name
        self.image = image
        self.price = price

    # Serialization method for JSON output
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price
        }
