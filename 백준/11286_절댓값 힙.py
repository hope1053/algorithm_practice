import heapq, sys

N = int(sys.stdin.readline())
heap = list()

for _ in range(N):
    num = int(sys.stdin.readline())
    if not heap and num == 0:
        print(0)
    elif heap and num == 0:
        print(heapq.heappop(heap)[-1])
    elif num != 0:
        heapq.heappush(heap, (abs(num), num))