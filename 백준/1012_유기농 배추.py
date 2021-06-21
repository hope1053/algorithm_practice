from collections import deque
t = int(input())

def solution(w, h, k):
    arr = [[0] * w for _ in range(h)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    section = 0
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                section += 1
                visited[i][j] = True
                search(arr, visited, i, j, w, h)

    print(section)

def search(arr, visited, i, j, w, h):
    queue = deque()
    queue.append((i, j))
    
    while queue:
        current_x, current_y = queue.popleft()
        DELTAS = [(0,1), (0,-1), (1,0), (-1,0)]

        for dx, dy in DELTAS:
            next_x, next_y = current_x + dx, current_y + dy
            if movable(next_x, next_y, w, h, visited, arr):
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

def movable(next_x, next_y, w, h, visited, arr):
    return 0 <= next_x < h and 0<= next_y < w and arr[next_x][next_y] == 1 and not visited[next_x][next_y]

for _ in range(t):
    w, h, k = map(int, input().split())
    solution(w, h, k)