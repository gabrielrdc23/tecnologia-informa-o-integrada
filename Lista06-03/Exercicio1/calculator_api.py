from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator', methods=['GET'])
def calculate():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

    result = 0
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Divisão por zero não é permitida'})

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
