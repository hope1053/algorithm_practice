def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

n = int(input())

for _ in range(n):
    parent = dict()
    number = dict()
    num = int(input())
    for _ in range(num):
        x, y = input().split(' ')
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x,y)
        print(number[find(x)])