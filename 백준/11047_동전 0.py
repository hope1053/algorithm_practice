import sys
N, K = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
count = 0
while K > 0:
    if coins[-1] > K:
        coins.pop()
    else:
        count += K // coins[-1]
        K = K % coins[-1]
        coins.pop()

print(count)