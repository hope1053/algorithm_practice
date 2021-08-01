def solution(lines):
    START, FINISH = 0, 1
    if len(lines) == 1:
        return 1
    
    recorded_list = list()
    
    for line in lines:
        date, end_time, duration = line.split()
        duration = float(duration[:-1])
        hour, minute, second = map(float, end_time.split(":"))
        end_second = 60**2 * hour + 60 * minute + second
        start_second = end_second - duration + 0.001
        recorded_list.append((int(start_second * 1000), int(end_second * 1000)))
    
    max_count = 0
    
    for i in range(len(recorded_list)):
        count = 1
        for start, finish in recorded_list[:i] + recorded_list[i+1:]:
            if recorded_list[i][FINISH] <= start < recorded_list[i][FINISH] + 1000 or recorded_list[i][FINISH] <= finish < recorded_list[i][FINISH] + 1000 or (start < recorded_list[i][FINISH] and recorded_list[i][FINISH] + 999 <= finish):
                count += 1
        max_count = max(count, max_count)
        
    return max_count