from flask import Flask, render_template, request
from main import load_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        title = request.form["title"]
        amount = request.form["amount"]
        print(title, amount)

    return render_template("add_expense.html")

@app.route("/view-expenses")
def view_expenses():
    expenses = load_data()
    return render_template("view_expenses.html", expenses=expenses)

if __name__ == "__main__":
    app.run(debug=True)