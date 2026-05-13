from app import limiter
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Customer
from app.blueprints.customer.schemas import customer_schema, customers_schema

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json

    new_customer = Customer(
        name=data['name'],
        email=data['email']
    )

    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)

@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)
from app.auth import encode_token

@customer_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():

    data = request.json

    email = data['email']

    customer = Customer.query.filter_by(email=email).first()

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    token = encode_token(customer.id)

    return jsonify({
        "token": token
    }), 200
from app.auth import token_required

@customer_bp.route('/my-tickets', methods=['GET'])
@token_required
def my_tickets(customer_id):
    return jsonify({
        "message": f"Protected route accessed by customer {customer_id}"
    }), 200