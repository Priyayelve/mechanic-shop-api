from flask import Blueprint, request
from app.extensions import db
from app.models import ServiceTicket, Mechanic
from app.blueprints.service_ticket.schemas import service_ticket_schema, service_tickets_schema

service_ticket_bp = Blueprint('service_ticket_bp', __name__)

@service_ticket_bp.route('/', methods=['POST'])
def create_service_ticket():
    data = request.json

    new_ticket = ServiceTicket(
        description=data['description']
    )

    db.session.add(new_ticket)
    db.session.commit()

    return service_ticket_schema.jsonify(new_ticket)

@service_ticket_bp.route('/', methods=['GET'])
def get_service_tickets():
    tickets = ServiceTicket.query.all()
    return service_tickets_schema.jsonify(tickets)

@service_ticket_bp.route('/<int:ticket_id>/assign-mechanic/<int:mechanic_id>', methods=['PUT'])
def assign_mechanic(ticket_id, mechanic_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)

    ticket.mechanics.append(mechanic)

    db.session.commit()

    return service_ticket_schema.jsonify(ticket)

@service_ticket_bp.route('/<int:ticket_id>/remove-mechanic/<int:mechanic_id>', methods=['PUT'])
def remove_mechanic(ticket_id, mechanic_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)

    ticket.mechanics.remove(mechanic)

    db.session.commit()

    return service_ticket_schema.jsonify(ticket)