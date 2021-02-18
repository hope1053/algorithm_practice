def solution(d, budget):
    d = sorted(d)
    sum = 0
    answer = 0
    for item in d:
        sum += item
        if sum > budget:
            break;
        else:
            answer += 1
    return answer