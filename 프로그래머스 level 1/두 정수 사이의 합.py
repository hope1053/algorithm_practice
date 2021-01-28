def solution(a, b):
    table = []
    if a == b:
        return a
    elif a < b:
        table = [i for i in range(a,b+1)]
        return sum(table)
    else:
        table = [i for i in range(b,a+1)]
        return sum(table)
