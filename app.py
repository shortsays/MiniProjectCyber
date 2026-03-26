from flask import Flask, render_template, jsonify
from src.database import fetch_logs, init_db

app = Flask(__name__)

init_db()

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/logs")
def get_logs():
    logs = fetch_logs(100) 
    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True)