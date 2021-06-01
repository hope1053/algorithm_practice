import heapq

def solution(n, works):
    stress = list()
    
    if sum(works) <= n:
        return 0
    
    for work in works:
        heapq.heappush(stress, -work)
    
    while n > 0:
        max_work = heapq.heappop(stress)
        heapq.heappush(stress, max_work + 1)
        n -= 1
        
    return sum([x**2 for x in stress])