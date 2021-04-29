def numCount(arr):
    count = 1
    mx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mx:
            count += 1
            mx = arr[i]
        else:
            continue
    return count

n = int(input())
trophy = list()
for _ in range(n):
    trophy.append(int(input()))

print(numCount(trophy))
trophy.reverse()
print(numCount(trophy))