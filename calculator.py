from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    try:
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        operator = data["operator"]

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operator"}), 400

        return jsonify({"result": result})
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"}), 400

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    try:
        value = float(data["value"])
        conversion = data["conversion"]

        if conversion == "km-miles":
            result = value * 0.621371
        elif conversion == "celsius-fahrenheit":
            result = (value * 9 / 5) + 32
        elif conversion == "usd-inr":
            result = value * 83.50
        elif conversion == "inr-usd":
            result = value / 83.50
        else:
            return jsonify({"error": "Invalid conversion"}), 400

        return jsonify({"result": round(result, 2)})
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
