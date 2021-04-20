N, lst = input(), list(map(int,input().split()))

answer = [lst[0]]

for i in range(1, int(N)):
    answer.append(lst[i]*(i+1) - sum(answer))

for i in answer: print(i, end=' ')