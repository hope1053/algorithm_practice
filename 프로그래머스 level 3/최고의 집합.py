def solution(n, s):
    answer = []
    if s < n:
        answer.append(-1)
    else:
        a, b =  divmod(s, n)
        answer = [a] * n
        if b > 0:
            for idx in range(len(answer)):
                answer[idx] += 1
                b -= 1
                if b == 0:
                    break
        
    return sorted(answer)