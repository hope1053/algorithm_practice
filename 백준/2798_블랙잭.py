N, M = map(int, input().split())
num_arr = map(int, input().split())

from itertools import combinations

cases = list(combinations(num_arr, 3))
answer = list()
for case in cases:
    if sum(case) <= M:
        answer.append(sum(case))

print(max(answer))