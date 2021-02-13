def solution(n, m):
    table = []
    for i in range(1, min(n, m) + 1):
        if n%i==0 and m%i==0:
            table.append(i)
    a = max(table)

    if min(n, m) == a:
        b = max(n, m)
    else:
        b = a * (n / a) * (m / a)
    return [a,b]
