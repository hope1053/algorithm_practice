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