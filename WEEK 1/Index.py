#Creating a Basic Calculator Program
#Assign values to the variables

x = 20
y = 30
op = '+' # Choose one operator: '+', '-', '*', '/'

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    result = x / y
else:
    result = "Invalid operator"

print(f"{x} {op} {y} = {result}")

