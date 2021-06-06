def solution(n, results):
    result_arr = [[0] * n for _ in range(n)]
    WIN, LOSE = 1, -1
    
    for winner, loser in results:
        result_arr[winner-1][loser-1], result_arr[loser-1][winner-1] = WIN, LOSE
        
    for player in range(n):
        win_list = [play_num for play_num, value in enumerate(result_arr[player]) if value == WIN]
        while win_list:
            next_player = win_list.pop()
            for play_num, value in enumerate(result_arr[next_player]):
                if value == WIN and result_arr[player][play_num] == 0:
                    result_arr[player][play_num], result_arr[play_num][player] = WIN, LOSE
                    win_list.append(play_num)
                    
    return len([result for result in result_arr if result.count(0) == 1])