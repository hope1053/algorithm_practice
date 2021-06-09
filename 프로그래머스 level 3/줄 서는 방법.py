from math import factorial

def solution(n, k):
    candidate = [num for num in range(1, n+1)]
    answer = list()
    
    while n >= 1:
        tmp_k = k % factorial(n-1)
        index = k // factorial(n-1)
        if tmp_k == 0:
            answer.append(candidate.pop(index - 1))
        else:
            answer.append(candidate.pop(index))
        k = tmp_k
        n -= 1
    return answer