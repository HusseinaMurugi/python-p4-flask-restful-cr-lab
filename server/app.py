# server/app.py

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# GET all plants
@app.route("/plants", methods=["GET"])
def get_plants():
    plants = Plant.query.all()
    return jsonify([p.to_dict() for p in plants]), 200

# GET plant by id
@app.route("/plants/<int:id>", methods=["GET"])
def get_plant_by_id(id):
    plant = db.session.get(Plant, id)
    if not plant:
        return {"error": "Plant not found"}, 404
    return jsonify(plant.to_dict()), 200

# POST new plant
@app.route("/plants", methods=["POST"])
def create_plant():
    data = request.get_json()
    name = data.get("name")
    image = data.get("image")
    price = data.get("price")

    if not name:
        return {"error": "Name is required"}, 400

    new_plant = Plant(name=name, image=image, price=price)
    db.session.add(new_plant)
    db.session.commit()

    return jsonify(new_plant.to_dict()), 201
