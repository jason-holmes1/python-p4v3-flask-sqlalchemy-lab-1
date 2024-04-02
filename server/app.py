# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
#? Add a route to get all earthquakes
@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    #? Query the database for the earthquake with the given id
    earthquake = Earthquake.query.get(id)
    #? If earthquake is found, return the earthquake as JSON
    if earthquake:
        response = {
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        }
        #? Return the response with a 200 status code
        return make_response(response, 200)
    else:
        #? If earthquake is not found, return a message with a 404 status code
        return {'message': f'Earthquake {id} not found.'}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
    
def get_earthquakes(magnitude):
    # Query the database for earthquakes with magnitude greater than or equal to the input
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Prepare the data for JSON
    data = []
    for quake in quakes:
        data.append({
            "id": quake.id,
            "location": quake.location,
            "magnitude": quake.magnitude,
            "year": quake.year
        })

    # Return a JSON response
    return jsonify({
        "count": len(data),
        "quakes": data
    })