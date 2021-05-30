from collections import defaultdict

def solution(n, s, a, b, fares):
    fare_arr = make_map(n, fares)
    min_fare = float('Inf')
    for k in range(n):
        min_fare = min(fare_arr[s-1][k] + fare_arr[k][a-1] + fare_arr[k][b-1], min_fare)
    return min_fare


def make_map(n, fares):
    fare_arr = [[float('Inf')] * n for _ in range(n)]
    
    for fare in fares:
        fare_arr[fare[0]-1][fare[1]-1] = fare[-1]
        fare_arr[fare[1]-1][fare[0]-1] = fare[-1]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                fare_arr[i][j] = 0
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                fare_arr[i][j] = min(fare_arr[i][k] + fare_arr[k][j], fare_arr[i][j])
    return fare_arr