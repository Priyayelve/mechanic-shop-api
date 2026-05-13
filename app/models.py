from app.extensions import db

service_mechanics = db.Table(
    'service_mechanics',
    db.Column('service_ticket_id', db.Integer, db.ForeignKey('service_ticket.id')),
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'))
)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    specialty = db.Column(db.String(100))

class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    mechanics = db.relationship(
        'Mechanic',
        secondary=service_mechanics,
        backref='service_tickets'
    )