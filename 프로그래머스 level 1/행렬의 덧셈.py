def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        c = []
        a = arr1[i]
        b = arr2[i]
        for j in range(len(a)):
            c.insert(j, a[j]+b[j])
        answer.insert(i, c)
    return answer