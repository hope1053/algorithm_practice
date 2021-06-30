import heapq, sys
N = int(sys.stdin.readline())
queue = list()
for _ in range(N):
    input_val = int(sys.stdin.readline())
    if not queue and input_val == 0:
        print(0)
    elif queue and input_val == 0:
        print(heapq.heappop(queue))
    else:
        heapq.heappush(queue, input_val)