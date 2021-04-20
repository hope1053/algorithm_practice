n = int(input())
answer = list()
for _ in range(n):
    answer.append(list(map(int, input().split(' '))))

answer.sort(key = lambda x:(x[0],x[1]))

for i in answer:
    print(i[0], i[1])