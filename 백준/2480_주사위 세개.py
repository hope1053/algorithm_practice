dices = list(map(int, input().split(' ')))

if len(set(dices)) == 1:
    price = 10000 + dices[0] * 1000
elif len(set(dices)) == 2:
    for dice in dices:
        if dices.count(dice) == 2:
            price = 1000 + dice * 100
else:
    price = max(dices) * 100

print(price)