def solution(n):
    answer = []
    while n > 3:
        if n % 3 == 0:
            answer.append(4)
            n = n//3 - 1
        else:
            answer.append(n%3)
            n = n//3
    if n == 3:
        answer.append(4)
    else:
        answer.append(n)

    return ''.join([str(_) for _ in reversed(answer)])
