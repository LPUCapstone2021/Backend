from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/form', methods=['POST'])
def form():
    data = request.json
    return jsonify({
        "Message": data
    })

@app.route('/')
def root():
    return 'CarsAndCars'

if __name__ == '__main__':
    app.run(threaded=True, port=5000)