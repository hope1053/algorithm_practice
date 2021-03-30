from itertools import combinations
from bisect import bisect_left
def make_combi(arr):
    case = list()
    for j in range(5):
        for k in list(combinations(range(4),j)):
            temp = list(arr)
            if len(k) != 0:
                for idx in k:
                    temp[idx] = '-'
            case.append(''.join(temp[:-1]))
    return case

def solution(info, query):
    result = list()
    table = {}
    for i in info:
        tmp = i.split()
        cases = make_combi(tmp)
        for case in cases:
            if case not in table.keys():
                table[case] = [int(tmp[-1])]
            else:
                table[case].append(int(tmp[-1]))
                
    for key in table.keys():
        table[key].sort()

    for check in query:
        seperate_q = check.split()
        tmp = ''.join([check.split()[x] for x in range(0,8,2)])
        if tmp in table.keys():
            result.append(len(table[tmp]) - bisect_left(table[tmp], int(seperate_q[-1]), lo=0, hi=len(table[tmp])))
        else:
            result.append(0)
    return result