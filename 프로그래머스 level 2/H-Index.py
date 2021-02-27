def solution(citations):
    arr = sorted(citations)
    h_idx = arr[0]

    if len([i for i in citations if i >= len(citations)]) == len(citations):
        return len(citations)

    while True:
        if len([i for i in arr if i >= h_idx]) >= h_idx:
            h_idx += 1
        else:
            h_idx -= 1
            break

    return h_idx
