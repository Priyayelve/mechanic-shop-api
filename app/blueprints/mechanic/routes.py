from flask import Blueprint, request
from app.extensions import db
from app.models import Mechanic
from app.blueprints.mechanic.schemas import mechanic_schema, mechanics_schema

mechanic_bp = Blueprint('mechanic_bp', __name__)

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():
    data = request.json

    new_mechanic = Mechanic(
        name=data['name'],
        specialty=data['specialty']
    )

    db.session.add(new_mechanic)
    db.session.commit()

    return mechanic_schema.jsonify(new_mechanic)

@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(mechanics)

@mechanic_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    data = request.json

    mechanic.name = data.get('name', mechanic.name)
    mechanic.specialty = data.get('specialty', mechanic.specialty)

    db.session.commit()

    return mechanic_schema.jsonify(mechanic)

@mechanic_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)

    db.session.delete(mechanic)
    db.session.commit()

    return {"message": "Mechanic deleted successfully"}