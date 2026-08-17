from flask import Flask, render_template, request, redirect, url_for
import requests

API_URL = "http://127.0.0.1:5000"   # tua API

app = Flask(__name__)

# HOME
@app.route("/")
def home():
    response = requests.get(f"{API_URL}/all")
    cafes = response.json()["cafes"]
    return render_template("index.html", cafes=cafes)

# CAFÉ
@app.route("/cafe/<int:cafe_id>")
def cafe(cafe_id):
    response = requests.get(f"{API_URL}/all")
    cafes = response.json()["cafes"]

    selected = next((c for c in cafes if c["id"] == cafe_id), None)

    return render_template("cafe.html", cafe=selected)

if __name__ == "__main__":
    app.run(debug=True, port=5001)