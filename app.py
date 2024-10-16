from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)  # Create a Flask application instance
calculator = Calculator()  # Instantiate the Calculator class

@app.route('/', methods=['GET', 'POST'])
def calculator_view():
    result = None  # Initialize result to None
    error_message = None  # Initialize error message to None

    if request.method == 'POST':
        try:
            # Retrieve and convert user inputs to float
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']  # Get the selected operation

            # Perform the appropriate operation based on user selection
            if operation == 'add':
                result = calculator.add(num1, num2)
            elif operation == 'subtract':
                result = calculator.subtract(num1, num2)
            elif operation == 'multiply':
                result = calculator.multiply(num1, num2)
            elif operation == 'divide':
                result = calculator.divide(num1, num2)
            else:
                raise ValueError("Invalid operation")  # Handle unexpected operations
            

        except ValueError as e:
            error_message = f"Input error: {str(e)}"
    
    return render_template('index.html', result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development

