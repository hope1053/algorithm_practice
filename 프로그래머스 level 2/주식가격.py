# 1st try
def solution(prices):
    arr = list()

    for index in range(len(prices)):
        if index == len(prices) - 1:
            break
        index2 = index + 1
        while prices[index] <= prices[index2]:
            index2 += 1
            if index2 >= len(prices):
                index2 -= 1
                break
        arr.append(index2 - index)
    arr.append(0)
    return arr

# 2nd try
from collections import deque
def solution(prices):
    answer = list()
    # prices를 deque로 만들어주어서 왼쪽부터 데이터를 뽑아낼 수 있도록 만들어준다
    prices = deque(prices)
    
    # 계속해서 popleft를 사용해서 데이터를 추출할 것이기 때문에 만약에 queue가 비었다면 break 할 수 있도록 설정
    while prices:
        # 현재 값을 popleft로 받아오고 time = 0 으로 설정
        current, time = prices.popleft(), 0
        # popleft를 한 뒤 남은 가격들과 비교를 해서 만약 현재 가격이 더 작다면 time을 더해주고 만약에 현재 가격이 더 커지는 순간이 온다면 break를 한다.
        for num in prices:
            time += 1
            if current > num:
                break
        answer.append(time)
    
    return answer