bilet = int(input("Введите колличество билетов:"))
x = bilet
cost = 0

while bilet != 0:
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        cost = cost + 0
        print(cost)
        bilet = bilet - 1

    elif age > 18 and age <= 25:
        cost = cost + 990
        print(cost)
        bilet = bilet - 1

    elif age >= 26 and age <= 100:
        cost = cost + 1390
        print(cost)
        bilet = bilet - 1
    else:
        print("Неверный возраст")


if x >= 3:
    cost = cost * 0.9
    print("Цена с учетом скидки:", cost)
else:
    print("Цена:", cost)
