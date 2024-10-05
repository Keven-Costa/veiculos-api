import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///default.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return {'vehicles': [{ 'id': v.id, 'make': v.make, 'model': v.model, 'year': v.year } for v in vehicles]}

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    new_vehicle = Vehicle(**request.json)
    db.session.add(new_vehicle)
    db.session.commit()
    return {'id': new_vehicle.id}, 201

@app.route('/vehicles/<int:id>', methods=['PUT'])
def update_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return {'error': 'Vehicle not found'}, 404
    for key, value in request.json.items():
        setattr(vehicle, key, value)
    db.session.commit()
    return {'message': 'Vehicle updated'}

@app.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return {'error': 'Vehicle not found'}, 404
    db.session.delete(vehicle)
    db.session.commit()
    return {'message': 'Vehicle deleted'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
