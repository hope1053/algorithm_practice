# first try
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

# second try
def solution_2(n,a,b):
    count = 1
    
    while abs(a-b) != 1 or a // 2 == b // 2:
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1
        count += 1
        
    return count