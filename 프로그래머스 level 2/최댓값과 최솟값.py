def solution(s):
    arr = [int(i) for i in s.split(' ')]
    answer = [min(arr), max(arr)]
    return " ".join([str(_) for _ in answer])
