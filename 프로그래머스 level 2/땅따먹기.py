def solution(land):
    LEN = len(land[0])
    for i in range(1, len(land)):
        for j in range(LEN):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            
    return max(land[-1])