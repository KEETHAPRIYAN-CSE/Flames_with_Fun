from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flames import calculate_flames

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/flames", methods=["POST"])
def flames_api():
    data = request.json

    name1 = data.get("name1", "").strip()
    name2 = data.get("name2", "").strip()

    if not name1 or not name2:
        return jsonify({"error": "Both names required"}), 400

    result = calculate_flames(name1, name2)

    return jsonify({"relationship": result})

if __name__ == "__main__":
    app.run(debug=True)
