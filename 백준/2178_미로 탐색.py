from collections import deque

H, W = map(int, input().split())

table = list()
for _ in range(H):
    tmp_arr = list(map(int, input()))
    table.append(tmp_arr)

def solution(table, W, H):
    visited = [[False] * W for _ in range(H)]
    DELTAS = [(0,1), (0, -1), (1,0), (-1,0)]
    will_visit = deque([(0, 0, 1)])

    while will_visit:
        pos = will_visit.popleft()
        current_x, current_y, current_move = pos[0], pos[1], pos[2]
        visited[current_x][current_y] = True
        if current_x == H-1 and current_y == W-1:
            print(current_move)
            break
            
        for dx, dy in DELTAS:
            next_x, next_y, next_move = current_x + dx, current_y + dy, current_move + 1
            if movable(next_x, next_y, visited, table):
                visited[next_x][next_y] = True
                will_visit.append((next_x, next_y, next_move))

def movable(next_x, next_y, visited, table):
    return 0 <= next_x < H and 0 <= next_y < W and not visited[next_x][next_y] and table[next_x][next_y] == 1

solution(table, W, H)