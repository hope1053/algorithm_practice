def solution(number, k):
    arr = list(number)
    table, left = list(), list()
    idx = 0

    for idx, value in enumerate(arr):
        if len(table) == 0:
            table.append(value)
            continue
        while len(table) > 0 and table[-1] < value:
            left.append(table[-1])
            del table[-1]
            if len(left) == k:
                break
        table.append(value)
        if len(left) == k:
            table.extend(arr[idx+1:])
            break

    if len(table) > len(arr) - k:
        for i in range(len(table)-len(arr)+k):
            del table[table.index(min(table))]
    return ''.join(table)

