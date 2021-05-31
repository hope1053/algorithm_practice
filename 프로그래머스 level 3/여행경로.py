from collections import defaultdict, deque

def solution(tickets):
    ticket_dict = defaultdict(list)
    for departure, arrival in tickets:
        ticket_dict[departure].append(arrival)
        
    for key, value in ticket_dict.items():
        ticket_dict[key].sort()
        ticket_dict[key] = deque(value)
        
    return dfs(ticket_dict)

def dfs(ticket_dict):
    stack = ["ICN"]
    answer = list()
    
    while stack:
        current_city = stack[-1]
        if current_city not in ticket_dict or len(ticket_dict[current_city]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(ticket_dict[current_city].popleft())

    return answer[::-1]