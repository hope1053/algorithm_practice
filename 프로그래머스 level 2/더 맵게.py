import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    search = True
    count = 0

    while search:
        hot_1, hot_2, = heapq.heappop(scoville), heapq.heappop(scoville)
        new_hot = hot_1 + 2 * hot_2
        heapq.heappush(scoville, new_hot)
        count += 1
        if scoville[0] >= K:
            search = False
        if len(scoville) ==  1 and scoville[0] < K:
            return -1

    return count
