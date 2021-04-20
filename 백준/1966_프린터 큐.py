from collections import deque
from operator import itemgetter

n = int(input())
answer = list()

for _ in range(n):
    printed = list()
    num, pri = map(int, input().split())
    queue = list(map(int, input().split()))
    # for idx, value in enumerate(queue):
    #     queue[idx] = (value, idx)
    queue = [(i, idx) for idx, i in enumerate(queue)]
    queue = deque(queue)

    while queue:
        if max(queue, key = itemgetter(0)) == queue[0]:
            printed.append(queue.popleft())
            if printed[-1][1] == pri:
                print(len(printed))
                break
        else:
            queue.append(queue.popleft())
