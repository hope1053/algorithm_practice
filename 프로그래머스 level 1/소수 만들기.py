import math
from itertools import combinations
def solution(nums):
    arr = [sum(x) for x in list(combinations(nums,3))]
    
    def is_prime_number(x):
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
            
    count = 0
    for num in arr:
        if is_prime_number(num):
            count += 1
            
    return count