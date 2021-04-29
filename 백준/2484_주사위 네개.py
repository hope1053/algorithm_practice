N = int(input())
prices = list()
for _ in range(N):
    dices = list(map(int, input().split(' ')))
    
    if len(set(dices)) == 1:
        price = 50000 + dices[0] * 5000
    elif len(set(dices)) == 2:
        for dice in set(dices):
            if dices.count(dice) == 3:
                price = 10000 + dice * 1000
            elif dices.count(dice) == 2:
                price = 2000 + 500 * sum(set(dices))
    elif len(set(dices)) == 3:
        for dice in set(dices):
            if dices.count(dice) == 2:
                price = 1000 + dice * 100
    else:
        price = max(dices) * 100

    prices.append(price)
print(max(prices))