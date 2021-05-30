def solution(m, n, puddles):
    school_map = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                continue
            if i == 1 and j == 1:
                school_map[i][j] = 1
            else:
                school_map[i][j] = (school_map[i-1][j] + school_map[i][j-1]) % 1_000_000_007
            
    return school_map[-1][-1]