# 8. Handle division by zero using try and except
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Answer =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
