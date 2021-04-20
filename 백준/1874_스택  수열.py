n = int(input())

stack = list()
answer = list()
count = 1

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == data:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))