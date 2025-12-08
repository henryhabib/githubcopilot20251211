from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import csv
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))  # 'income' or 'expense'
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

# Routes
@app.route('/')
def dashboard():
    # ...existing code for fetching and summarizing data...
    return render_template('dashboard.html')

def categorize_transaction(transaction_type, amount, description):
    """
    Categorizes a transaction based on logic.
    """
    if transaction_type == 'income':
        if amount > 5000:
            return 'High Income'
        elif 'bonus' in description.lower():
            return 'Bonus'
        else:
            return 'Regular Income'
    elif transaction_type == 'expense':
        if 'rent' in description.lower():
            return 'Housing'
        elif 'grocery' in description.lower() or 'food' in description.lower():
            return 'Food'
        elif amount > 1000:
            return 'Large Expense'
        else:
            return 'Miscellaneous'
    return 'Uncategorized'

def calculate_tax(income: list[float]):
    """
    Calculates tax based on income brackets.
    """
    if income <= 10000:
        return income * 0.1
    elif income <= 30000:
        return income * 0.2
    else:
        return income * 0.3

def calculate_discount(price, discount_rate):
    """
    Calculates the discounted price.
    """
    return price * (discount_rate / 100)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction_type = request.form['type']
        category = categorize_transaction(
            transaction_type,
            float(request.form['amount']),
            request.form.get('description', '')
        )
        # ...existing code for adding transactions...
        return redirect(url_for('dashboard'))
    return render_template('add_transaction.html')

@app.route('/export')
def export_csv():
    # Export transactions as CSV
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Type', 'Category', 'Amount', 'Date'])
    for transaction in Transaction.query.all():
        writer.writerow([transaction.id, transaction.type, transaction.category, transaction.amount, transaction.date])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='transactions.csv')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
