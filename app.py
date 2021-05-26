from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/form', methods=['POST'])
@cross_origin()
def form():
    data = request.json
    return jsonify({
        "Message": data
    })

@app.route('/')
@cross_origin()
def root():
    return 'CarsAndCars'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)