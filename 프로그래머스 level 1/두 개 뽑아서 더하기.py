def solution(numbers):
    answer = []
    for idx, item in enumerate(numbers):
        while idx + 1 < len(numbers):
            answer.append(item + numbers[idx+1])
            idx += 1
    return sorted(set(answer))