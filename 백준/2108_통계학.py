import sys
from collections import Counter

answer = list()

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균
answer.append(round(sum(num_list)/ N))
# 중앙값
num_list.sort()
answer.append(num_list[N//2])
# 최빈값
count_num = Counter(num_list).most_common()
if N >= 2:
    if count_num[0][1] != count_num[1][1]:
        answer.append(count_num[0][0])
    else:
        answer.append(count_num[1][0])
else:
    answer.append(num_list[0])
# 최대 - 최소
answer.append(num_list[-1] - num_list[0])

for num in answer:
    print(num)