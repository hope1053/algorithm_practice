K, N = map(int, input().split())
line_list = [int(input()) for _ in range(K)]
lower, upper = 1, max(line_list)

while lower <= upper:
    middle = (lower + upper) // 2
    count = sum([line // middle for line in line_list])
    if count < N:
        upper = middle - 1
    else:
        lower = middle + 1

print(upper)