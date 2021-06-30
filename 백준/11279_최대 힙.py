import heapq, sys

N = int(sys.stdin.readline())
tmp_list = list()

for _ in range(N):
    order = int(sys.stdin.readline())

    if not tmp_list and order == 0:
        print(0)
    elif tmp_list and order == 0:
        print(-(heapq.heappop(tmp_list)))
    else:
        heapq.heappush(tmp_list, -order)