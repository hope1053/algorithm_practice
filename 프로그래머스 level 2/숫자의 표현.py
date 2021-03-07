def solution(n):
    count = 0
    piv = 1
    while piv <= n:
        answer = 0
        for i in range(piv, n+1):
            answer += i
            if answer == n:
                count += 1
                break
            elif answer > n:
                break
        piv += 1
        
    return count