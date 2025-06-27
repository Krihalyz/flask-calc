from flask import Flask, render_template, request
from adder import add_numbers, substract_numbers, multiply_numbers, divide_numbers

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <title>Flask Calculator</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            width: 300px;
        }
        input[type="text"], button {
            width: 100%;
            padding: 8px;
            margin: 5px 0 10px 0;
            box-sizing: border-box;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background-color: #0056b3;
        }
        h2 {
            text-align: center;
        }
        .result {
            background-color: #f0f0f0;
            padding: 10px;
            text-align: center;
            border-radius: 4px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Simple Web Calculator</h2>
        <form method="post">
            <input name="a" type="text" placeholder="First number" required>
            <input name="b" type="text" placeholder="Second number" required>
            <input name="op" type="text" placeholder="Operator (+, -, *, /)" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result %}
        <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""
history = []

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = ""
    if request.method == "POST":
        if "clear" in request.form:
            history.clear()
        else:
            try:
                expression = request.form["expression"]
                # Evaluate safely:
                result = str(eval(expression, {"__builtins__": None}, {}))
                # store it:
                history.append(f"{expression} = {result}")
            except Exception as e:
                result = f"Error: {e}"
    return render_template("calculator.html", result=result, history=history)

if __name__ == "__main__":
    app.run(debug=True)