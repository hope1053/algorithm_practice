from itertools import permutations
from collections import defaultdict, deque
import heapq

def solution(board, r, c):
    global card_num, pos_dict, copied_board, answer
    copied_board = board[:]
    answer = list()
    pos_dict = defaultdict(list)
    SIZE = 4
    for i in range(SIZE):
        for j in range(SIZE):
            board_num = board[i][j]
            if board_num != 0:
                pos_dict[board_num].append((i, j))
                
    card_num = len(pos_dict)
    delete_order = list(permutations([num for num in range(1, card_num+1)]))
    
    for order in delete_order:
        get_ready(r, c, order, 0, 0)

    return heapq.heappop(answer)

def get_ready(r, c, order, card_idx, move_count):
    global card_num, pos_dict, copied_board, answer
    if card_idx == card_num:
        heapq.heappush(answer, move_count)
        return
    current_card = order[card_idx]
    first_card_pos = pos_dict[current_card][0]
    second_card_pos = pos_dict[current_card][1]
    
    first_move = bfs(r, c, first_card_pos[0], first_card_pos[1])
    second_move = bfs(first_card_pos[0], first_card_pos[1], second_card_pos[0], second_card_pos[1])
    
    delete_card(current_card)
    get_ready(second_card_pos[0], second_card_pos[1], order, card_idx + 1, move_count + first_move + second_move)
    restore_card(current_card)
    
    first_move = bfs(r, c, second_card_pos[0], second_card_pos[1])
    second_move = bfs(second_card_pos[0], second_card_pos[1], first_card_pos[0], first_card_pos[1])
    
    delete_card(current_card)
    get_ready(first_card_pos[0], first_card_pos[1], order, card_idx + 1, move_count + first_move + second_move)
    restore_card(current_card)
    
def delete_card(current_card):
    global pos_dict, copied_board
    for x, y in pos_dict[current_card]:
        copied_board[x][y] = 0
        
def restore_card(current_card):
    global pos_dict, copied_board
    for x, y in pos_dict[current_card]:
        copied_board[x][y] = current_card
        
def bfs(current_x, current_y, next_x, next_y):
    global copied_board

    if current_x == next_x and current_y == next_y:
        return 1

    visited = [[False] * 4 for _ in range(4)]
    visited[current_x][current_y] = True
    table = [[0] * 4 for _ in range(4)]
    need_visit = deque([(current_x, current_y)])
    DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while need_visit:
        x, y = need_visit.popleft()
        for dx, dy in DELTAS:
            move_to_x, move_to_y = x + dx, y + dy
            if visitable(move_to_x, move_to_y, visited):
                table[move_to_x][move_to_y] = table[x][y] + 1
                visited[move_to_x][move_to_y] = True
                if move_to_x == next_x and move_to_y == next_y:
                    return table[move_to_x][move_to_y] + 1
                need_visit.append((move_to_x, move_to_y))
            
            move_to_x, move_to_y = ctrl_move(x, y, dx, dy)
            if not visited[move_to_x][move_to_y]:
                table[move_to_x][move_to_y] = table[x][y] + 1
                visited[move_to_x][move_to_y] = True
                if move_to_x == next_x and move_to_y == next_y:
                    return table[move_to_x][move_to_y] + 1
                need_visit.append((move_to_x, move_to_y))
            
def visitable(move_to_x, move_to_y, visited):
    return 0 <= move_to_x < 4 and 0 <= move_to_y < 4 and not visited[move_to_x][move_to_y]

def ctrl_move(x, y, dx, dy):
    global copied_board
    while True:
        next_x, next_y = x + dx, y + dy
        if next_x < 0 or next_x >= 4 or next_y < 0 or next_y >= 4:
            return x, y
        else:
            if copied_board[next_x][next_y] != 0:
                return next_x, next_y
            x, y = next_x, next_y