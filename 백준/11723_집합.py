import sys

M = int(input())
S = set()

for _ in range(M):
    order = sys.stdin.readline().split()
    if order[0] == "add":
        num = int(order[1])
        S.add(num)
    elif order[0] == "remove":
        num = int(order[1])
        if num in S:
            S.remove(num)
    elif order[0] == "check":
        num = int(order[1])
        if num in S:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        num = int(order[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif order[0] == "all":
        S = {num for num in range(1, 21)}
    elif order[0] == "empty":
        S = set()
