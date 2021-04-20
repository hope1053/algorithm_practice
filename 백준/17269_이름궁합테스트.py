N, M = map(int, input().split())
A, B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

min_num = min(N, M)
name = ''

for i in range(min_num):
    name += A[i] + B[i]
name += A[min_num:] + B[min_num:]

lst = [alp[ord(i)-ord('A')] for i in name]

for i in range(M+N-2):
    for j in range(M+N-i-1):
        lst[j] += lst[j+1]

print("{}%".format(lst[0]%10 * 10 + lst[1]%10))