from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from engine import recommended_cars

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/form', methods=['POST'])
@cross_origin()
def form():
    form = request.json
    features, preferences = form.get('features'), form.get('preferences')
    if form:
        response = jsonify({
            "status": "success",
            "method": "POST",
            "data": recommended_cars(features, preferences)
        })
    else:
        response = jsonify({
            "status": "failure",
            "message": "Error, check server logs"
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
@cross_origin()
def root():
    return 'CarsAndCars'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)