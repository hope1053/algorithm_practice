import heapq
from collections import defaultdict

def solution(n, vertexes):
    node_dict = defaultdict(list)
    
    for vertex in vertexes:
        node_dict[vertex[0]].append(vertex[1])
        node_dict[vertex[1]].append(vertex[0])
        
    # 다익스트라 알고리즘
    distances = {node: float('inf') for node in node_dict}
    distances[1] = 0
    queue = list()
    heapq.heappush(queue, [distances[1], 1])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
            
        for node in node_dict[current_node]:
            distance = current_distance + 1
            
            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(queue, [distance, node])
                
    max_distances = [distance for distance in distances.values() if distance == max(distances.values())]
    return len(max_distances)