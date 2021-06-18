#1st_try
def solution(answers):

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    score = [0, 0, 0]
    winner = []

    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            score[0] += 1
        if answers[i] == student2[i % 8]:
            score[1] += 1
        if answers[i] == student3[i % 10]:
            score[2] += 1

    for i in range(3):
        if score[i] == max(score):
            winner.append(i + 1)

    return winner

#2nd_try
def second_solution(answers):
    answer = list()
    num_answer = [get_answer(answers, [1,2,3,4,5]), get_answer(answers, [2,1,2,3,2,4,2,5]), get_answer(answers, [3,3,1,1,2,2,4,4,5,5])]
    
    for idx, value in enumerate(num_answer):
        if value == max(num_answer):
            answer.append(idx+1)
            
    return answer
    
    
def get_answer(answers, arr):
    answer_cand = arr * (len(answers) // len(arr)) + arr[:(len(answers) % len(arr))]
    result_arr = [True for answer, cand in list(zip(answers, answer_cand)) if answer == cand]
    return len(result_arr)