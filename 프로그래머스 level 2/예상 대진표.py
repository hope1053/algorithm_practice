def solution(n,a,b):
    def return_num(i):
        if i % 2 == 0:
            return i // 2
        else:
            return i // 2 + 1

    count = 1
    A, B = a, b
    while abs(A-B) != 1 or A//2 == B//2:
        A = return_num(A)
        B = return_num(B)
        count += 1
    return count