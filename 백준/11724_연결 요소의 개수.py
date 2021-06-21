from collections import defaultdict, deque
n, m = map(int, input().split())

def solution(n, m):
    connected = [False] * (n+1)
    graph = defaultdict(list)

    for _ in range(m):
        first_node, second_node = map(int, input().split())
        graph[first_node].append(second_node)
        graph[second_node].append(first_node)

    connected_compo = 0
    for key in range(1, n+1):
        if not connected[key]:
            connected_compo += 1
            search(connected, graph, key)

    print(connected_compo)

def search(connected, graph, key):
    queue = deque()
    queue.append(key)

    while queue:
        current_node = queue.popleft()
        if not connected[current_node]:
            connected[current_node] = True
            queue.extend(graph[current_node])

solution(n, m)