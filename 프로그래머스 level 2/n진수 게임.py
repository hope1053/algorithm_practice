def solution(n, t, m, p):
    result, answer = list(), str()
    for num in range(0,t*m):
        a, b = -1, -1
        temp = list()
        while a != 0:
            a, b = divmod(num, n)
            if n > 10 and b >= 10:
                b = chr(b - 10 + ord('A'))
            temp = [b] + temp
            num = a
        result.extend(temp)
        if len(result) > t * m:
            break
    
    for idx in range(len(result)):
        if (idx + 1 - p) % m == 0:
            answer += str(result[idx])
        if len(answer) == t:
            break
            
    return answer