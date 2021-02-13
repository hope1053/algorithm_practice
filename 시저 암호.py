def solution(s, n):
    a = list(s)
    for idx, value in enumerate(a):
        a[idx] = ord(value)
    for idx, value in enumerate(a):
        if value == 32:
            pass
        elif 65 <= value <= 90:
            a[idx] += n
            if a[idx] > 90:
                a[idx] = a[idx] - 26
        elif 97 <= value <= 122:
            a[idx] += n
            if a[idx] > 122:
                a[idx] = a[idx] - 26
    for idx, value in enumerate(a):
        a[idx] = chr(value)
    return ''.join(a)
