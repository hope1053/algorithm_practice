from itertools import combinations
from collections import Counter
def solution(orders, course):
    result = list()
    for num in course:
        candidate = list()
        for name in orders:
            for cand in combinations(name, num):
                temp = ''.join(sorted(cand))
                candidate.append(temp)
        sorted_candidate = Counter(candidate).most_common()
        result += [menu for menu, cnt in sorted_candidate if cnt >= 2 and cnt == sorted_candidate[0][1]]
        
    return sorted(result)