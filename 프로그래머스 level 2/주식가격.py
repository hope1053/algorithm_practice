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
