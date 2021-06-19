from collections import defaultdict

N, M, start_node = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    first_node, second_node = map(int, input().split())
    graph[first_node].append(second_node)
    graph[second_node].append(first_node)

# print(graph)

# DFS
visited = list()
need_visit = list()

need_visit.append(start_node)

while need_visit:
    node = need_visit.pop()
    if node not in visited:
        visited.append(node)
        need_visit.extend(sorted(graph[node], reverse=True))

for node in visited:
    print(node, end=' ')
print()
# BFS
visited = list()
need_visit = list()

need_visit.append(start_node)

while need_visit:
    node = need_visit.pop(0)
    if node not in visited:
        visited.append(node)
        need_visit.extend(sorted(graph[node]))

for node in visited:
    print(node, end=' ')
