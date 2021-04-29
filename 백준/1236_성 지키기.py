width, height = map(int, input().split(' '))

security = list()
for _ in range(width):
    security.append(list(input()))

w, h = 0, 0

for idx in range(width):
    if security[idx].count('X') == 0:
        w += 1

for i in range(height):
    tmp = list()
    for j in range(width): 
        tmp.append(security[j][i])
    if tmp.count('X') == 0:
        h += 1

print(max(w, h))