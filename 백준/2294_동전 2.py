# DP 풀이

n, k = map(int, input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))

# n은 이제 필요 없음
# k: 만들고 싶은 가치, coin: 내가 가지고 있는 코인의 List
coin.sort()

# 만들 수 있는 최솟값을 구해야하기 때문에 정해진 최댓값보다 큰 값으로 default 설정해주기
# 그리고 각 Index의 값을 만들 수 있는 최솟값을 저장해주면 되는데 0원은 만들 수 없기 때문에 0 저장
coin_arr = [10001] * (k + 1)
coin_arr[0] = 0

# 동전 하나씩 돌면서 해당 코인으로 만들 수 있는 값과 이미 저장된 값을 비교해서 최솟값을 넣어줌
for i in range(n):
    for j in range(coin[i], k+1):
        coin_arr[j] = min(coin_arr[j], coin_arr[j-coin[i]] + 1)

# 만약 구하려고 하는 값의 최솟값이 아직 저장해뒀던 10001이면 만들 수 없다는 뜻이기 때문에 불가능하다는 뜻에서 -1 프린트하기
if coin_arr[-1] == 10001:
    print(-1)
else:
    print(coin_arr[-1])