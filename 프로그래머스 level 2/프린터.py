def solution(priorities, location):
    arr = []
    count = 0
    data_queue = []
    for idx, value in enumerate(priorities):
        data_queue.append([value, idx])
    
    while len(data_queue) != 0:
        count = 0
        target = data_queue[0]
        del data_queue[0]
        for item in data_queue:
            if target[0] < item[0]:
                data_queue.append(target)
                break
            else:
                count += 1
        if count == len(data_queue):
            arr.append(target)
        if len(data_queue) == 1:
            arr.append(data_queue[0])
            del data_queue[0]

    for idx, value in enumerate(arr):
        if value[1] == location:
            return idx+1
        