N = int(input())
DP = list()

for _ in range(N):
    DP.append(list(map(int, input().split(' '))))
    
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            DP[i][j] += DP[i-1][j]
        elif j == i:
            DP[i][j] += DP[i-1][j-1]
        else:
            DP[i][j] += max(DP[i-1][j-1], DP[i-1][j])

print(max(DP[N-1]))