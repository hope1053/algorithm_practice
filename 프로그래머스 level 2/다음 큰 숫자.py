def solution(n):
    count = format(n, 'b').count('1')
    while True:
        n += 1
        if format(n, 'b').count('1') == count:
            return mn