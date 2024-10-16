class Calculator:
    #functions for basic operations
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0: # returns an error incase of division by 0
            return "Error: Division by zero"
        return num1 / num2
