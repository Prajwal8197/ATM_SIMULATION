from flask import Flask, render_template, request, redirect, url_for
from models import User, ATM

app = Flask(__name__)

@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    name = request.form["name"]
    face = request.form["face"]
    fingerprint = request.form["fingerprint"]

    # Check if the user exists
    user = User.query.filter_by(name=name).first()
    if user is None:
        return render_template("login.html", error="User not found")

    # Check if the user's face and fingerprint match
    if not ATM.is_face_match(name, face):
        return render_template("login.html", error="Incorrect face")

    if not ATM.is_fingerprint_match(name, fingerprint):
        return render_template("login.html", error="Incorrect fingerprint")

    # Login the user
    session["user"] = user.id
    return redirect(url_for("home"))

@app.route("/home")
def home():
    if not session.get("user"):
        return redirect(url_for("login"))

    user = User.query.get(session["user"])
    return render_template("home.html", user=user)

@app.route("/check_balance")
def check_balance():
    if not session.get("user"):
        return redirect(url_for("login"))

    user = User.query.get(session["user"])
    balance = user.balance
    return render_template("check_balance.html", balance=balance)

@app.route("/withdraw_cash", methods=["POST"])
def withdraw_cash():
    if not session.get("user"):
        return redirect(url_for("login"))

    user = User.query.get(session["user"])
    amount = request.form["amount"]

    # Check if the user has enough funds
    if amount > user.balance:
        return render_template("withdraw_cash.html", error="Insufficient funds")

    # Withdraw the cash
    user.balance -= amount
    user.save()
    return render_template("withdraw_cash.html", success="Cash withdrawn")

@app.route("/deposit_cash", methods=["POST"])
def deposit_cash():
    if not session.get("user"):
        return redirect(url_for("login"))

    user = User.query.get(session["user"])
    amount = request.form["amount"]

    # Deposit the cash
    user.balance += amount
    user.save()
    return render_template("deposit_cash.html", success="Cash deposited")

@app.route("/transfer_money", methods=["POST"])
def transfer_money():
    if not session.get("user"):
        return redirect(url_for("login"))

    user = User.query.get(session["user"])
    from_name = request.form["from_name"]
    to_name = request.form["to_name"]
    amount = request.form["amount"]

    # Check if the user has enough funds
    if amount > user.balance:
        return render_template("transfer_money.html", error="Insufficient funds")

    # Transfer the money
    from_user = User.query.filter_by(name=from_name).first()
    to_user = User.query.filter_by(name=to_name).first()

    from_user.balance -= amount
    to_user.balance += amount
    from_user.save()
    to_user.save()
    return render_template("transfer_money.html", success="Money transferred")
