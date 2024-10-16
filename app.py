from flask import Flask,render_template
from calculator import Calculator

app = Flask(__name__)

@app.route('/')
def index():

    # Retrieve and convert user inputs to float
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']  # Get the selected operation
    # calculator.add(num1, num2) #testing
    print(num1 + num2)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)