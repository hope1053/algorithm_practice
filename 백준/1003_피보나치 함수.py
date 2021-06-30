test_num = int(input())
answer = list()

for _ in range(test_num):
    count_zero, count_one = 0, 0
    n = int(input())
    cache = [(0,0)] * (n+2)
    cache[0] = (1,0)
    cache[1] = (0,1)
    if n < 2:
        answer.append(cache[n])
    else:
        for i in range(2, n+1):
            cache[i] = (cache[i-1][0] + cache[i-2][0], cache[i-1][1] + cache[i-2][1])
        answer.append(cache[n])

for num1, num2 in answer:
    print(num1, num2, end = " ")
    print()