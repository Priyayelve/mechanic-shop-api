from flask import Flask
from app.config import Config
from app.extensions import db, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from app.blueprints.customer.routes import customer_bp
    from app.blueprints.mechanic.routes import mechanic_bp
    from app.blueprints.service_ticket.routes import service_ticket_bp

    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(mechanic_bp, url_prefix="/mechanics")
    app.register_blueprint(service_ticket_bp, url_prefix="/service-tickets")

    with app.app_context():
        db.create_all()

    return app