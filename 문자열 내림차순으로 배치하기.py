def solution(s):
    a = list(s)
    for idx, value in enumerate(a):
        a[idx] = ord(value)
    for idx, value in enumerate(sorted(a, reverse = True)):
        a[idx] = chr(value)

    return ''.join(a)