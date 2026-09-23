total = 10000

def lunch_total(price, quantity):
    total = price * quantity
    return total

result = lunch_total(1200, 3)

print(result)
print(total)

print(lunch_total(1200, 3))
print(lunch_total(1200, 0))
print(lunch_total(0, 2))