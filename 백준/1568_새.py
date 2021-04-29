n = int(input())
time = 0

num = 1
while n > 0:
    if n >= num:
        time += 1
        n -= num
        num += 1
    else:
        num = 1

print(time)
