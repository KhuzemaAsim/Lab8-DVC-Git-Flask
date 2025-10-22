from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "House Price App - baseline"

@app.route("/login")
def login():
    return "Login Page"

@app.route("/dashboard")
def dashboard():
    return "Dashboard Page"

@app.route("/api/data")
def api_data():
    return {"message": "API Response"}


if __name__ == "__main__":
    app.run(debug=True)
