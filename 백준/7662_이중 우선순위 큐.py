import heapq
N = int(input())

for _ in range(N):
    heap_list = list()
    for _ in range(int(input())):
        order = input().split()
        if order[0] == 'I':
            heapq.heappush(heap_list, int(order[-1]))
        elif order[0] == 'D' and order[-1] == '-1':
            if len(heap_list) == 0:
                continue
            else: heapq.heappop(heap_list)
        else:
            if len(heap_list) == 0:
                continue
            else:
                max_heap = list()
                for value in heap_list:
                    heapq.heappush(max_heap, -value)
                heapq.heappop(max_heap)
                empty_list = list()
                for value in max_heap:
                    heapq.heappush(empty_list, -value)
                heap_list = empty_list
                # 최대힙으로 변환한 다음에 최댓값 제거하고 다시 최소힙으로 돌려놔야함
    if len(heap_list) == 0:
        print("EMPTY")
    else:
        print(max(empty_list), min(empty_list))
