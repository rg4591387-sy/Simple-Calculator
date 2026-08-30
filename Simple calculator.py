# Simple Calculator

num1 = eval(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = eval(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero")

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Cannot perform modulo by zero")

else:
    print("Invalid operator")
