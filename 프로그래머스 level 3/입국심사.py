def solution(n, times):
    left, right = 1, max(times) * n
    while left < right:
        middle = (left + right) // 2
        if sum([middle // x for x in times]) < n:
            left = middle + 1
        else:
            right = middle
            
    return left