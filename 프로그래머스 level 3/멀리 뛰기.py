def solution(n):
    if n <= 2:
        return n
    
    jump = [0] * (n+1)
    jump[1], jump[2] = 1, 2
    
    for i in range(3, n+1):
        jump[i] = (jump[i-1] + jump[i-2]) % 123_456_7
        
    return jump[n]