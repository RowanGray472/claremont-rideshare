from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(10), nullable=False)
    place = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.time}', '{self.place}', '{self.date}')"

# Create the database and table
with app.app_context():
    db.create_all()

# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Simple validation (replace with proper auth in real apps)
        if username == "admin" and password == "password":
            return redirect(url_for("welcome", username=username))
        else:
            return "Invalid credentials. Try again!"
    
    return render_template("login.html")

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for('welcome'))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        date = request.form.get("date")
        time = request.form.get("time")
        place = request.form.get("place")
        username = request.args.get("username", "Guest")

        # Save data to the database
        new_user = User(username=username, time=time, place=place, date=date)
        db.session.add(new_user)
        db.session.commit()

        print(f"Data saved: {username}, {time}, {place}")
        return redirect(url_for('welcome', username=username))

    username = request.args.get("username", "Guest")
    users = User.query.all()  # Optional: Fetch all users to display
    return render_template("welcome.html", username=username, users=users)

if __name__ == "__main__":
    app.run(debug=True)

