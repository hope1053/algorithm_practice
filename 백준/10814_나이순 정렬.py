n = int(input())
answer = list()

for i in range(n):
    data = input().split(' ')
    answer.append([[int(data[0]), data[1]], i])

answer.sort(key = lambda x:(x[0][0], x[1]))

for i in answer:
    print(i[0][0], i[0][1])