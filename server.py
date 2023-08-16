from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.json
        first_number = data['first']
        second_number = data['second']
        result = first_number + second_number
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.json
        first_number = data['first']
        second_number = data['second']
        result = first_number - second_number
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

