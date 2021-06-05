def solution(key, lock):
    M, N = len(key), len(lock)
    total_arr = [[0] * (2 * M + N) for _ in range(2 * M + N)]
    # 가운데에 자물쇠 배치
    for i in range(N):
        for j in range(N):
            total_arr[M+i][M+j] = lock[i][j]
    
    # 4번 모두 회전시키기
    for _ in range(4):
        key = rotate(key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                attach(x, y, M, key, total_arr)
                if check(N, M, total_arr):
                    return True
                detach(x, y, M, key, total_arr)
                continue
    return False
            
def rotate(key):
    return list(zip(*key[::-1]))

def check(N, M, total_arr):
    for i in range(N):
        for j in range(N):
            if total_arr[M+i][M+j] != 1:
                return False
    return True

def attach(x, y, M, key, total_arr):
    for i in range(M):
        for j in range(M):
            total_arr[x+i][y+j] += key[i][j]
    
def detach(x, y, M, key, total_arr):
    for i in range(M):
        for j in range(M):
            total_arr[x+i][y+j] -= key[i][j]