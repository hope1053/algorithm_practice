N = int(input())
spot_arr = [list(input()) for _ in range(N)]
answer = list()
def comp(x, y, N):
    init_spot = spot_arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if init_spot != spot_arr[i][j]:
                half_N = N // 2
                answer.append('(')
                comp(x, y, half_N)
                comp(x, y+half_N, half_N)
                comp(x+half_N, y, half_N)
                comp(x+half_N, y+half_N, half_N)
                answer.append(')')
                return
    answer.append(init_spot)

comp(0,0, N)
print(''.join(answer))