# 1st try
def solution(n, computers):
    count = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and computers[i][j] == 1:
                count += 1
                dfs(i, j, computers, visited, n)
                
    return count

def dfs(i, j, computers, visited, n):
    will_visit = list()
    will_visit.append((i,j))
    
    while will_visit:
        x, y = will_visit.pop()
        visited[x][y] = True
        for idx in range(n):
            if not visited[y][idx] and computers[y][idx] == 1:
                will_visit.append((y, idx))

# 2nd try