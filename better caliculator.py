num1 = float(input("Enter first number:"))
num2 = float(input("Enter Second number:"))
op = input("Enter operator:")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")
