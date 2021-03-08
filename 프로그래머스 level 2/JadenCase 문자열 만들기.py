def solution(s):
    a = s.split(" ")
    for idx, value in enumerate(a):
        a[idx] = (value.lower()).capitalize()
    return ' '.join(a)
