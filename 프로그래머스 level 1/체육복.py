def solution(n, lost, reserve):
    student = [1] * n
    for i in lost:
        student[i-1] -= 1
    for j in reserve:
        student[j-1] += 1
    print(student)

    for idx, value in enumerate(student):
        if value == 1 or value == 0:
            pass
        else:
            if idx == 0 and student[idx+1] == 0:
                student[idx] -= 1
                student[idx+1] = 1
            elif idx == n-1 and student[idx-1] == 0:
                student[idx] -= 1
                student[idx-1] = 1
            elif 0 < idx < n-1:
                if student[idx-1] == 0:
                    student[idx] -= 1
                    student[idx-1] = 1
                elif student[idx+1] == 0:
                    student[idx] -= 1
                    student[idx+1] = 1
    print(student)

    return n - student.count(0)
