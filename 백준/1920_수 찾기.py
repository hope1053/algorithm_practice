N, A = int(input()), {i: 1 for i in map(int, input().split())}
M, B = int(input()), list(map(int, input().split()))

for i in B:
    print(A.get(i, 0))
