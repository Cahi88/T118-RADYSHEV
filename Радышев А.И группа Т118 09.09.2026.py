def calculate_discount (price, discount=0):
    return price *(1- discount /100)
print(calculate_discount(5000,10))