from flask import request, jsonify
from . import inventory_bp

inventory = []

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@inventory_bp.route('/', methods=['POST'])
def add_inventory():

    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data['name'],
        "quantity": data['quantity']
    }

    inventory.append(new_item)

    return jsonify(new_item), 200