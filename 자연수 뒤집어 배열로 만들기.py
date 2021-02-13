def solution(n):
    answer = list(str(n))
    answer.reverse()
    return [int(x) for x in answer]