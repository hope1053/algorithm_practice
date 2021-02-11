def solution(numbers):
    answer = []
    for idx, item in enumerate(numbers):
        value = idx
        while value + 1 < len(numbers):
            answer.append(item + numbers[value+1])
            value += 1
    return sorted(set(answer))