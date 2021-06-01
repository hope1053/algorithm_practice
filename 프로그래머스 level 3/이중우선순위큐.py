import heapq

def solution(operations):
    queue = list()
    
    for order in operations:
        if order[0] == 'I':
            heapq.heappush(queue, int(order.split(' ')[-1]))
        else:
            if len(queue) == 0:
                continue
            if order.split(' ')[-1] == '1':
                tmp_queue = change_heap(queue)
                heapq.heappop(tmp_queue)
                queue = change_heap(tmp_queue)
            else:
                # 최솟값 삭제
                heapq.heappop(queue)
                
    if len(queue) == 0:
        return [0,0]
    tmp_queue = change_heap(queue)
    max_num = -tmp_queue[0]
    queue = change_heap(tmp_queue)
    min_num = queue[0]
    return [max_num, min_num]
                
def change_heap(queue):
    tmp_queue = list()
    for num in queue:
        heapq.heappush(tmp_queue, -num)
        
    return tmp_queue