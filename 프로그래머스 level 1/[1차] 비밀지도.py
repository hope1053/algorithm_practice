# 1st_try
def solution(n, arr1, arr2):
    arr3 = [""] * n
    arr4 = [""] * n
    arr5 = [""] * n

    for i in range(n):
        arr1[i] = format(arr1[i], "b")
        arr2[i] = format(arr2[i], "b")
    for j in range(n):
        if len(arr1[j]) < n:
            for k in range(n-len(arr1[j])):
                arr1[j] = '0' + arr1[j]
        if len(arr2[j]) < n:
            for k in range(n-len(arr2[j])):
                arr2[j] = '0' + arr2[j]

    for a in range(n):
        for b in range(n):            
            if arr1[a][b] == '0':
                arr3[a] += " "
            else:
                arr3[a] += "#"
            if arr2[a][b] == '0':
                arr4[a] += " "
            else:
                arr4[a] += "#"

    for a in range(n):
        for b in range(n):   
            if arr3[a][b]=="#" or arr4[a][b]=="#":
                arr5[a] += "#"
            else:
                arr5[a] += " "
    return arr5

# 2nd_try
def second_solution(n, arr1, arr2):
    answer = list()
    secret_map = list()
    for i in range(n):
        secret_map.append(bin(arr1[i] | arr2[i])[2:])
        
    for key in secret_map:
        key = key.rjust(n, "0")
        key = key.replace("1", "#")
        key = key.replace("0", " ")
        answer.append(key)
        
    return answer