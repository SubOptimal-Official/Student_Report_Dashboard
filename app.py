from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# --------------------
# App Configuration
# --------------------
app = Flask(__name__)
app.secret_key = "student_report_secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --------------------
# Database Models
# --------------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)

# --------------------
# Routes
# --------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Authentication logic will go here later
        return redirect(url_for("login"))

    return render_template("login.html")

# --------------------
# App Entry Point
# --------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
