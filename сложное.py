def add(a, b):
    return a+b
def subtract(a, b):
        return a-b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return("делить на 0 нельзя")
    return a / b
print(add(3,4))
print(subtract(7,7))
print(multiply(6,7))
print(divide(0,15))