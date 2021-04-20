n = int(input())

for _ in range(n):
    left_stack = list()
    right_stack = list()

    tmp_pw = list(input())
    for key in tmp_pw:
        if key == '-':
            if left_stack:
                left_stack.pop()
        elif key == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif key == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        else:
            left_stack.append(key)
    left_stack.extend(reversed(right_stack))

    print(''.join(left_stack))