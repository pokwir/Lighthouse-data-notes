from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return "Yayyy, you found my math app!"

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
    return jsonify(result=int(num1) + int(num2))

@app.route('/subtract', methods=['POST', 'GET'])
def subtract():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
    return jsonify(result=int(num1) - int(num2))

@app.route('/multiply', methods=['POST', 'GET'])
def multiply():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
    return jsonify(result=int(num1) * int(num2))

@app.route('/divide', methods=['POST', 'GET'])
def divide():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
    else:
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
    return jsonify(result=int(num1) / int(num2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)