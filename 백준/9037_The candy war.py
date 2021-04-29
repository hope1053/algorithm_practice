t = int(input())

for _ in range(t):
    turn = 0
    n = int(input())
    candies = list(map(int, input().split(' ')))

    while len(set(candies)) != 1:
        for idx, value in enumerate(candies):
            if value % 2 == 1:
                candies[idx] = value + 1
        if len(set(candies)) == 1:
            break
        tmp_candy = [candy // 2 for candy in candies]
        candies = [sum(candy) for candy in list(zip(tmp_candy, ([tmp_candy[-1]] + tmp_candy[:-1])))]
        turn += 1

    print(turn)
