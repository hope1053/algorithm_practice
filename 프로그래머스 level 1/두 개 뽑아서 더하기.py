# 1st try
def solution(numbers):
    answer = []
    for idx, item in enumerate(numbers):
        while idx + 1 < len(numbers):
            answer.append(item + numbers[idx+1])
            idx += 1
    return sorted(set(answer))

# 2nd try
from itertools import combinations
def solution(numbers):
    arr = [sum(x) for x in list(combinations(numbers, 2))]
    return list(sorted(set(arr)))

# 3rd try
from itertools import combinations
def solution(numbers):
    return list(sorted(set([sum(x) for x in list(combinations(numbers, 2))])))