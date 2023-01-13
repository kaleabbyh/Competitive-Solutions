"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list):
    m = [round(i) for i in student_scores]
    return m


def count_failed_students(student_scores: list):
    count = 0
    for i in student_scores:
        if i <= 40:
            count += 1
    return count


def above_threshold(student_scores: list, threshold):

    m = []
    for i in student_scores:
        if i >= threshold:
            m.append(i)
    return m


def letter_grades(highest):

    gap = int((highest-40)/4)
    a = [41+gap*i for i in range(4)]
    return a


def student_ranking(student_scores: list, student_names: list):
    m = []
    for i in range(len(student_names)):
        m.append(f'{i+1}. {student_names[i]}: {str(student_scores[i])}')
    return m


def perfect_score(student_info: list):

    for i, j in student_info:
        if j == 100:
            return [i, j]

    return []
