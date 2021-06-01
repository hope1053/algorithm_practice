from collections import deque
import heapq

def solution(jobs):
    JOBS_COUNT, TIME, COST = len(jobs), 0, 1
    
    candidate, current_time, total_time = list(), 0, 0
    
    jobs = deque(sorted(jobs))
    
    while jobs or candidate:
        if not candidate:
            time, cost = jobs.popleft()
            current_time = time + cost
            total_time += cost
        else:
            cost, time = heapq.heappop(candidate)
            current_time += cost
            total_time += current_time - time
        
        while jobs and jobs[0][TIME] <= current_time:
            heapq.heappush(candidate, jobs.popleft()[::-1])
            
    return total_time // JOBS_COUNT