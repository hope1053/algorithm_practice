import numpy

def solution(n, words):
    n_words = numpy.array(words)
    for i in range(1, len(words)):
        arr = numpy.where(n_words == words[i])[0]
        if len(arr) > 1:
            return [int(arr[1]) % n + 1, int(arr[1]) // n + 1]
        if words[i][0] != words[i-1][-1]:
            return [i % n + 1, i // n + 1]
    return [0,0]