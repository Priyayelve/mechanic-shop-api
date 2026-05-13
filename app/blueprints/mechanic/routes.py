from flask import request, jsonify
from . import mechanic_bp

mechanics = []

@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    return jsonify(mechanics)

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():

    data = request.get_json()

    new_mechanic = {
        "id": len(mechanics) + 1,
        "name": data['name'],
        "specialty": data['specialty']
    }

    mechanics.append(new_mechanic)

    return jsonify(new_mechanic), 200