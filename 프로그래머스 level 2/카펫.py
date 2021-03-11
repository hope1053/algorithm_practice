def solution(brown, yellow):
    a, b = 0,0
    total = int((brown + yellow) ** 0.5)
    for i in range(3, total):
        if total % i == 0:
            a, b = i, total // i
            if a + b == (brown + 4)//2:
                answer = [a,b]
                answer.sort(reverse = True)
                return answer