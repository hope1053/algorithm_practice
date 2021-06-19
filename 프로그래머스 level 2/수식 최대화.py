#1st_try
from itertools import permutations
import re
def solution(expression):
    code = set(re.findall('\D', expression))
    all_code = list(permutations(code))
    cand = []
    
    for item in all_code:
        temp = re.compile('(\D)').split('' + expression)
        for i in item:
            while i in temp:
                index = temp.index(i)
                temp = temp[:index-1] + [str(eval(''.join(temp[index-1:index+2])))] + temp[index+2:]
        cand.append(abs(int(temp[0])))
    return max(cand)

#2nd_try
import re
from itertools import permutations

def second_solution(expression):
    value_cand = list()
    operators = set(re.findall('(\D)', expression))
    operator_cands = list(permutations(operators))
    
    split_expression = re.compile('(\D)').split(expression)
    
    for cand in operator_cands:
        expression_c = split_expression[:]
        for operator in cand:
            while operator in expression_c:
                idx = expression_c.index(operator)
                expression_c = expression_c[:idx - 1] + [str(eval(''.join(expression_c[idx-1:idx + 2])))] + expression_c[idx + 2:]
        value_cand.append(abs(int(expression_c[0])))
        
    return max(value_cand)