from collections import defaultdict
import heapq

def get_distance(user, users, friend_dic, answer):
    distance_graph = {friend: float('Inf') for friend in range(1, users+1)}
    distance_graph[user] = 0
    queue = list()
    heapq.heappush(queue, [distance_graph[user], user])

    while queue:
        current_distance, current_user = heapq.heappop(queue)
        if current_distance > distance_graph[current_user]:
            continue
        
        for user_cand in friend_dic[current_user]:
            distance = current_distance + 1
            if distance < distance_graph[user_cand]:
                distance_graph[user_cand] = distance
                heapq.heappush(queue, [distance, user_cand])

    answer.append(sum(distance_graph.values()))

users, friend_num = map(int, input().split())
friend_dic = defaultdict(list)
for _ in range(friend_num):
    first, second = map(int, input().split())
    friend_dic[first].append(second)
    friend_dic[second].append(first)
answer = list()

for num in range(1, users + 1):
    get_distance(num, users, friend_dic, answer)

min_list = [idx+1 for idx, value in enumerate(answer) if value == min(answer)]

print(min_list[0])