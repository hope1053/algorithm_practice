import sys
n = int(sys.stdin.readline())
answer = [0] * (10**4+1) 

for _ in range(n):
    data = int(sys.stdin.readline())
    answer[data] += 1

for i in range(10**4+1):
    if answer[i] != 0:
        for _ in range(answer[i]):
            print(i, end='\n')

