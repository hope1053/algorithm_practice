# DP 풀이

n = int(input())

cache = [0] * (n+1)

for num in range(2, n+1):
    cache[num] = cache[num-1] + 1
    # 6의 배수의 경우 2,3 모두 다 나뉠 수 있기 때문에 elif가 아닌 각자의 경우로 처리해줘야함
    if num % 2 == 0:
        cache[num] = min(cache[num//2] + 1, cache[num])
    if num % 3 == 0:
        cache[num] = min(cache[num//3] + 1, cache[num])

print(cache[-1])