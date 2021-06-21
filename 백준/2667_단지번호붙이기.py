from collections import deque

n = int(input())
arr = list()

for _ in range(n):
    arr.append(list(map(int, input())))

def solution(arr):
    visited = [[False] * n for _ in range(n)]
    answer = list()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, n, arr, visited, answer)

    answer.sort()
    print(len(answer))
    for num in answer:
        print(num)

def dfs(i, j, n, arr, visited, answer):
    connected_num = 1
    queue = deque()
    queue.append((i, j))

    while queue:
        current_x, current_y = queue.popleft()
        DELTAS = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in DELTAS:
            next_x, next_y = current_x + dx, current_y + dy
            if movable(next_x, next_y, n, arr, visited):
                connected_num += 1
                visited[next_x][next_y] = True
                queue.append((next_x, next_y))
    answer.append(connected_num)

def movable(next_x, next_y, n, arr, visited):
    return 0 <= next_x < n and 0 <= next_y < n and arr[next_x][next_y] == 1 and not visited[next_x][next_y]

solution(arr)