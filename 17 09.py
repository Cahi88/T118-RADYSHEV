money = int(input("какой у вас бюджет?"))
drink_price = int(input("сколько стоит сок?"))
bun_price = int(input("сколько стоит булочка?"))
people = int(input("сколько студентов?"))
def lunch_balance(money, drink_price, bun_price,people=1):
    return money - (bun_price+drink_price)*people
if people < 1:
    people = 1
if lunch_balance(money, drink_price, bun_price,people) > 0:
    print(f"остаеться {lunch_balance(money, drink_price, bun_price,people)} тенге")
elif lunch_balance(money, drink_price, bun_price) < 0:
    print(f"у вас не хватает {-lunch_balance(money, drink_price, bun_price,people)}")
else:
    print("вам хватает ровно!")


