from flask import Flask, render_template, request, jsonify
from data import db
from collections import defaultdict  # NEW

app = Flask(__name__)
app.config['DATABASE'] = 'data/database'

# Initialize the database
with app.app_context():
    db.init_app(app)
    db.get_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    # Get all form fields from Emma’s frontend
    rm1 = data.get('rm1', '')
    rm2 = data.get('rm2', '')
    rm3 = data.get('rm3', '')
    rm4 = data.get('rm4', '')
    rent = data.get('rent', '')
    groceries = data.get('groceries', '')

    # Basic validation
    if not all([rm1, rm2, rm3, rm4, rent, groceries]):
        return jsonify({'error': 'All fields are required.'}), 400

    try:
        rent = float(rent)
        groceries = float(groceries)
    except ValueError:
        return jsonify({'error': 'Rent and groceries must be numbers.'}), 400

    # Combine names and costs into entries
    conn = db.get_db()
    cursor = conn.cursor()
    tracker_id = 1
    roommate_id = 1  # placeholder; replace with logic if needed

    # Rent entry
    if rent > 0:
        cursor.execute(
            'INSERT INTO expense (amount, description, tracker_id, roommate_id) VALUES (?, ?, ?, ?)',
            (rent, 'Rent', tracker_id, roommate_id)
        )

    # Groceries entry
    if groceries > 0:
        cursor.execute(
            'INSERT INTO expense (amount, description, tracker_id, roommate_id) VALUES (?, ?, ?, ?)',
            (groceries, 'Groceries', tracker_id, roommate_id)
        )

    conn.commit()
    return jsonify({'status': 'Expenses added successfully'}), 200

@app.route('/get_expenses', methods=['GET'])
def get_expenses():
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, description FROM expense')
    expenses = cursor.fetchall()

    result = []
    for row in expenses:
        result.append({
            'id': row['id'],
            'description': row['description'],
            'amount': row['amount']
        })

    return jsonify(result)

# NEW: Simple class for in-memory use only
class Roommate:
    def __init__(self, key, name):
        self.key = key
        self.name = name

@app.route('/get_balances', methods=['GET'])
def get_balances():
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT amount, description FROM expense')
    expenses = cursor.fetchall()

    rm1 = request.args.get('rm1', 'Roommate 1').strip()
    rm2 = request.args.get('rm2', 'Roommate 2').strip()
    rm3 = request.args.get('rm3', 'Roommate 3').strip()
    rm4 = request.args.get('rm4', 'Roommate 4').strip()

    roommates = [
        Roommate('rm1', rm1),
        Roommate('rm2', rm2),
        Roommate('rm3', rm3),
        Roommate('rm4', rm4)
    ]

    payer = roommates[0]  # default payer = first roommate
    debts = defaultdict(float)

    for row in expenses:
        amount = row['amount']
        split = amount / len(roommates)
        for rm in roommates:
            if rm.name != payer.name:
                debts[f'{rm.name} owes {payer.name}'] += split

    return jsonify({k: round(v, 2) for k, v in debts.items()})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
