from flask import Blueprint, request, jsonify, render_template
from .calculator import add, subtract, multiply, divide

calculator_bp = Blueprint("calculator", __name__)

@calculator_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@calculator_bp.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    
    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        operation = data.get("operation")

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            if num2 == 0:
                return jsonify({"error": "Division by zero is not allowed"}), 400
            result = divide(num1, num2)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
