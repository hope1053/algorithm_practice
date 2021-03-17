def right_function(p):
    stack = list()
    for i in p:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
    if len(stack) == 0:
        return p

def solution(p):
    stack = list()
    right_function(p)

    p_arr = list(p)
    u, v, string = list(), p_arr, str()

    if len(p) == 0:
        return ''
    else:
        for i in p:
            u.append(p_arr.pop(0))
            if u.count("(") == u.count(")"):
                break

    if right_function(u) == u:
        return ''.join(u) + solution(v)
    else:
        string += '(' + solution(v) + ')'
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ')'
            else:
                u[i] = '('
        string += ''.join(u)
    return string
