from flask import Flask, render_template, request, jsonify
from data import db

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)
