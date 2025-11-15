from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = []

@app.route('/add', methods=['POST'])
def add_expense():
    data = request.get_json()
    expenses.append(data)
    return jsonify({'message': 'Expense added', 'expenses': expenses})

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

if __name__ == '__main__':
    app.run(debug=True)
