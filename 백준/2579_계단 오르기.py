# DP 풀이
num = int(input())
cases = [0] + [int(input()) for _ in range(num)]
if num == 1:
    print(cases[1])
else:
    dp = [0] * (num + 1)
    dp[1] = cases[1]
    dp[2] = cases[1] + cases[2]

    for i in range(3, num+1):
        dp[i] = max(cases[i] + cases[i-1] + dp[i-3], cases[i] + dp[i-2])

    print(dp[num])