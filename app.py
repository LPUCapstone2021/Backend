from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from engine import recommended_cars
from db import car_details

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/cars', methods=['GET'])
@cross_origin()
def cars():
    ids = [id for id in request.args.values()]
    if ids:
        return jsonify({
            "status": "success",
            "method": "GET",
            "data": car_details(ids)
        })
    else:
        return jsonify({
            "status": "failure",
            "message": "Error, check server logs"
        })

@app.route('/form', methods=['POST'])
@cross_origin()
def form():
    features = request.json.get('features')
    preferences = request.json.get('preferences')
    if features and preferences:
        return jsonify({
            "status": "success",
            "method": "POST",
            "data": recommended_cars(features, preferences)
        })
    else:
        return jsonify({
            "status": "failure",
            "message": "Error, check server logs"
        })

@app.route('/')
@cross_origin()
def root():
    return 'CarsAndCars'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)