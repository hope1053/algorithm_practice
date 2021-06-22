def movable(next_x, next_y, visited, L):
    return 0 <= next_x < L and 0 <= next_y < L and not visited[next_x][next_y]

def solution(answer):
    L = int(input())
    current_x, current_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    if current_x == goal_x and current_y == goal_y:
        answer.append(0)
        return

    visited = [[False] * L for _ in range(L)]
    count = 0

    current_pos = [(current_x, current_y)]
    visited[current_x][current_y] = True

    while current_pos:
        next_pos = list()
        DELTAS = [(-2,1), (-1,2), (1,2), (2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

        for current_x, current_y in current_pos:
            for dx, dy in DELTAS:
                next_x, next_y = current_x + dx, current_y + dy
                if movable(next_x, next_y, visited, L):
                    next_pos.append((next_x, next_y))
                    visited[next_x][next_y] = True
        count += 1
        if (goal_x, goal_y) in next_pos:
            answer.append(count)
            break
        else:
            current_pos = next_pos

answer = list()
test_num = int(input())

for _ in range(test_num):
    solution(answer)

for num in answer:
    print(num)