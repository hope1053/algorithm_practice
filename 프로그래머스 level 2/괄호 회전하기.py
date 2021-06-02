def solution(brackets):
    LEN = len(brackets)
    answer = 0
    
    for i in range(LEN):
        rotated_bracket = brackets[i:] + brackets[:i]
        if check_bracket(rotated_bracket):
            answer += 1
            
    return answer
    
def check_bracket(brackets):
    bracket_dict = {']':'[', ')':'(', '}':'{'}
    stack = list()
    
    for bracket in brackets:
        if bracket not in bracket_dict:
            stack.append(bracket)
        else:
            if not stack:
                return False
            if stack[-1] == bracket_dict[bracket]:
                stack.pop()
    
    return len(stack) == 0