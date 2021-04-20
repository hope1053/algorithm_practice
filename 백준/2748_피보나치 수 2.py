# DP 풀이

n = int(input())

cache = [0 for i in range(n+1)]
cache[0] = 0
cache[1] = 1

for num in range(2, n+1):
    cache[num] = cache[num-1] + cache[num-2]

print(cache[-1])