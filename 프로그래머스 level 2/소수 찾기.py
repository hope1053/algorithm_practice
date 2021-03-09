from itertools import permutations
def solution(numbers):
    return(prime_list(all_nums(numbers)))

def all_nums(numbers):
    num = [i for i in numbers]  
    arr = list()
    for i in range(len(num)):
        for j in list(permutations(num, i+1)):
            arr.append(j)
    all_num = list(set([int(''.join(i)) for i in arr]))
    return all_num

def prime_list(all_num):
    case = [0 for _ in range(len(all_num))]
    for idx,value in enumerate(all_num):
        m = int(value**0.5)
        if value in [0,1]:
            case[idx] = 1
            continue
        for j in range(2, m+1):
            if value % j == 0:
                case[idx] = 1
                break
    return case.count(0)