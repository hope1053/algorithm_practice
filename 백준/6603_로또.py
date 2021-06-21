from itertools import combinations

while True:
    input_arr = list(map(int, input().split()))
    if input_arr[0] == 0:
        break

    k = input_arr[0]
    s = input_arr[1:]

    combi_list = list(combinations(s, 6))
    
    for combi in combi_list:
        for num in combi:
            print(num, end = ' ')
        print()

    print()