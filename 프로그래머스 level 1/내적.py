# 1st try
def solution(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
                
    answer = sum
    return answer

# 2nd try
def second_solution(a, b):
    return sum([x[0]*x[1] for x in list(zip(a,b))])