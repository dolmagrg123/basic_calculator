class Calculator:
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def division(num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    
    print(add(1,2))
    print(subtract(5,6))
    print(multiply(1,5))
    print(division(2,0))
    print(division(2,2))
    

