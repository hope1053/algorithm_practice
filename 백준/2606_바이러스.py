from collections import defaultdict

N = int(input())
computer_dict = defaultdict(list)

for _ in range(int(input())):
    first, second = map(int, input().split())
    computer_dict[first].append(second)
    computer_dict[second].append(first)

visited = [False] * (N + 1)

queue = [1]
while queue:
    current_node = queue.pop()
    if not visited[current_node]:
        visited[current_node] = True
        queue.extend(computer_dict[current_node])

print(len([1 for computer in visited if computer]) - 1)