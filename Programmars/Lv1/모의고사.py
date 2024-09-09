def solution(answers):
    n = len(answers)
    score = {1: 0, 2: 0, 3: 0}
    student1 = [1,2,3,4,5] * ((n // 5) + 1)
    student2 = [2,1,2,3,2,4,2,5] * ((n // 8) + 1)
    student3 = [3,3,1,1,2,2,4,4,5,5] * ((n // 10) + 1)

    for num in range(0,n):
        if answers[num] == student1[num]:
            score[1] += 1
        if answers[num] == student2[num]:
            score[2] += 1
        if answers[num] == student3[num]:
            score[3] += 1

    max_score = max(score.values())
    result = [student for student, student_score in score.items() if student_score == max_score]

    return result

solution([1,3,2,4,2])