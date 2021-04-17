# 1st try
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

# 2nd try
def solution(brown, yellow):
    # 1과 yellow 사이에서 yellow의 약수를 구하고
    # 약수와 yellow를 약수로 나눈 값의 곱이 전체 넓이와 동일하면 배열에 담아 return
    # brown = a*b - (a-2)*(b-2), yellow = (a-2)*(b-2), brown + yellow = a*b 활용
    for i in range(1, yellow+1):
        if yellow % i == 0:
            a = i + 2
            b = yellow//i + 2
            if a * b == brown + yellow:
                return [max(a,b), min(a,b)]