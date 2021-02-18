def solution(n):
    answer = 0
    temp = []
    while True:
        n, left = divmod(n, 3)
        temp.append(left)
        if n == 0:
            break

    for idx, value in enumerate(reversed(temp)):
            answer += value * 3**idx
    return answer