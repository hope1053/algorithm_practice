def solution(n):
    word = str(n)
    sum = 0
    for i in range(len(word)):
        sum += int(word[i])
    return sum
