N = int(input())
paint_price = list()
RGB = 3

for _ in range(N):
    paint_price.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(RGB):
        paint_price[i][j] += min(paint_price[i-1][:j] + paint_price[i-1][j+1:])

print(min(paint_price[-1]))