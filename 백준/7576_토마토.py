def movable(next_x, next_y, w, h, ripped, tomato_box):
    return 0 <= next_x < h and 0 <= next_y < w and tomato_box[next_x][next_y] == 0 and not ripped[next_x][next_y]
    
w, h = map(int, input().split())

ripe_tomato = list()
no_tomato = list()
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

ripped = [[False] * w for _ in range(h)]

for x, y in ripe_tomato + no_tomato:
    ripped[x][y] = True

while ripe_tomato:
    DELTAS = [(0,1), (0,-1), (1,0), (-1,0)]
    new_tomato = list()
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