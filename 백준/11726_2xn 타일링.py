N = int(input())
if N <= 1:
    print(1)
    exit(0)

cache = [0] * (N+1)
cache[1], cache[2] = 1, 2
for i in range(3, N+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 10007

print(cache[N])