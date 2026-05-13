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