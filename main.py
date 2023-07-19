from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route("/")

def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/planet")

def planet():
    # request is used to get the url of the planets
    name = request.args.get("name")
    # next 
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()