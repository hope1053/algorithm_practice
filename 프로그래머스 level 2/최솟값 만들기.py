def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    LEN = len(A)
    sum = 0
    
    for i in range(LEN):
        sum += A[i] * B[i]
        
    return sum