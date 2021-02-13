def solution(x, n):
    arr = []
    i = 0
    while True:
        arr.append(x + i*x)
        i += 1
        if len(arr) == n:
            break
    return arr