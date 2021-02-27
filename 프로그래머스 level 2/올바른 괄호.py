def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0