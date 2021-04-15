# 1st try
def solution(n):
    answer = 0
    temp = []
    while True:
        n, left = divmod(n, 3)
        temp.append(left)
        if n == 0:
            break

    for idx, value in enumerate(reversed(temp)):
            answer += value * 3**idx
    return answer

# 2nd try
def solution(n):
    arr = list()
    a, b = n, 3
    while a != 0:
        a, b = divmod(a,3)
        arr.append(b)
    answer = 0
    for idx, value in enumerate(arr):
        answer += 3**(len(arr)-idx-1) * value
        
    return answer

# 3rd try
def solution(n):
    a, b = divmod(n, 3)
    answer = str(b)
    while a > 0:
        a, b = divmod(a, 3)
        answer += str(b)
    return int(answer, 3)