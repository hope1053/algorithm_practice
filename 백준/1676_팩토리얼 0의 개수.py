N = int(input())

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

factorial_n = str(factorial(N))[::-1]
answer = 0
idx = 0
while factorial_n[idx] == '0':
    answer += 1
    idx += 1
print(answer)