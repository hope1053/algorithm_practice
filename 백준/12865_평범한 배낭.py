n, k = map(int, input().split(' '))
items = list()
value = 0
for _ in range(n):
    item = list(map(int, input().split(' ')))
    items.append((item[0], item[1]))
items.sort(key = lambda x:x[1]/x[0])

for item in items:
    if k > item[0]:
        k -= item[0]
        value += item[1]

print(value)