def solution(n, nodes):
    min_cost = 0
    bridge = 0
    
    nodes.sort(key = lambda x:x[-1])
    
    parent = [node for node in range(n)]
    
    for node in nodes:
        first_node, second_node, cost = node
        if find(parent, first_node) != find(parent, second_node):
            parent[find(parent, first_node)] = find(parent, second_node)
            bridge += 1
            min_cost += cost
            if bridge == n-1:
                return min_cost
            
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]