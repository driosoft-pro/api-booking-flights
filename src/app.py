from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
db = SQLAlchemy(app)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    airline = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    flight = db.relationship('Flight', backref=db.backref('reservations', lazy=True))

@app.route('/flights', methods=['POST'])
def create_flight():
    data = request.get_json()
    flight = Flight(**data)
    db.session.add(flight)
    db.session.commit()
    return jsonify(flight), 201

@app.route('/flights', methods=['GET'])
def get_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure_date = request.args.get('departure_date')
    flights = Flight.query.filter_by(origin=origin, destination=destination).all()
    return jsonify(flights), 200

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    reservation = Reservation(**data)
    db.session.add(reservation)
    db.session.commit()
    return jsonify(reservation), 201

@app.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify(reservations), 200

@app.route('/statistics', methods=['GET'])
def get_statistics():
    airlines = db.session.query(Flight.airline, db.func.count(Reservation.id)).\
        join(Reservation).\
        group_by(Flight.airline).\
        order_by(db.func.count(Reservation.id).desc()).all()
    num_airlines = len(Flight.query.distinct(Flight.airline).all())
    return jsonify({'airlines': airlines, 'num_airlines': num_airlines}), 200

if __name__ == '__main__':
    db.create_all()
    app.run()
