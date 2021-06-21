from collections import deque
n, k = map(int, input().split())

def solution(n, k):
    current_pos = deque([[n, 0]])
    visited = set()

    if n == k:
        print(0)
        return

    while current_pos:
        current_p, current_t = current_pos.popleft()
        current_t += 1
        next_p = [current_p - 1, current_p + 1, current_p * 2]
        for pos in next_p:
            if pos == k:
                print(current_t)
                return
            if pos in visited or pos < 0 or pos > 100000:
                continue
            else:
                current_pos.append([pos, current_t])
                visited.add(current_p)

solution(n, k)