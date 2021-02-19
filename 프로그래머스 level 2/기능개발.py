def solution(progresses, speeds):
    answer = []

    while len(progresses) != 0:
        while progresses[0] < 100:
            for idx, value in enumerate(progresses):
                progresses[idx] += speeds[idx]
        count = 0
        while progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            count += 1
            if len(progresses) == 0:
                break
        answer.append(count)
    return answer