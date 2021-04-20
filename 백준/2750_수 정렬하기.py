# 퀵 소트
import sys
sys.setrecursionlimit(10**9)

n = int(input())

answer = list()
for _ in range(n):
    answer.append(int(input()))

def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [x for x in data[1:] if x < pivot]
    right = [x for x in data[1:] if x >= pivot]

    return qsort(left) + [pivot] + qsort(right)

answer = qsort(answer)
for i in range(len(answer)):
    print(answer[i], end='\n')

# 선택 정렬
n = int(input())
answer = list()
for _ in range(n):
    answer.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if answer[min_index] > answer[j]:
            min_index = j
    answer[i], answer[min_index] = answer[min_index], answer[i]
    
for i in answer:
    print(i)

# 파이썬 기본 정렬 알고리즘
n = int(input())
answer = list()
for _ in range(n):
    answer.append(int(input()))

answer.sort()

for i in answer:
    print(i)