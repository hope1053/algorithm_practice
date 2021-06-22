def movable(next_x, next_y, w, h, ripped, tomato_box):
    return 0 <= next_x < h and 0 <= next_y < w and tomato_box[next_x][next_y] == 0 and not ripped[next_x][next_y]
    
w, h = map(int, input().split())

# 익은 토마토 index 리스트
ripe_tomato = list()
# 토마토가 없는 위치 index 리스트
no_tomato = list()
# 전체 토마토 박스 리스트
tomato_box = list()

for i in range(h):
    tmp_arr = list(map(int, input().split()))
    tomato_box.append(tmp_arr)
    for idx, value in enumerate(tmp_arr):
        if value == 0:
            continue
        elif value == 1:
            ripe_tomato.append((i, idx))
        else:
            no_tomato.append((i, idx))

day = -1

# 처음부터 모든 토마토가 익어있는지 확인
if w * h == len(ripe_tomato) + len(no_tomato):
    print(0)
    exit(0)

# 익은 상태 계속 체크할 수 있는 리스트
ripped = [[False] * w for _ in range(h)]

for x, y in ripe_tomato + no_tomato:
    ripped[x][y] = True

while ripe_tomato:
    new_tomato = list()
    DELTAS = [(0,1), (0,-1), (1,0), (-1,0)]
    for current_x, current_y in ripe_tomato:
        for dx, dy in DELTAS:
            next_x, next_y = current_x + dx, current_y + dy
            if movable(next_x, next_y, w, h, ripped, tomato_box):
                ripped[next_x][next_y] = True
                new_tomato.append((next_x, next_y))
    ripe_tomato = new_tomato
    day += 1

if any(False in row for row in ripped):
    print(-1)
    exit(0)

print(day)