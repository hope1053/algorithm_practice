import heapq
def solution(N, road, K):
    nodes = {}
    distances = {node : float('inf') if node !=1 else 0 for node in range(1,N+1)}
    for n1, n2, dis in road:
            nodes[n1] = nodes.get(n1, []) + [(n2, dis)]
            nodes[n2] = nodes.get(n2, []) + [(n1, dis)]
    queue = []
    heapq.heappush(queue, [0,1])

    while queue:
        current_dis, current_node = heapq.heappop(queue)
        if distances[current_node] < current_dis:
            continue
        for item in nodes[current_node]:
            distance = current_dis + item[1]
            
            if distance < distances[item[0]]:
                distances[item[0]] = distance
                heapq.heappush(queue, [distance, item[0]])
    count = 0        
    for value in distances.values():
        if value <= K:
            count += 1
    return count