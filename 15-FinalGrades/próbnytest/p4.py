def f(subjects):
    best_subject = ''
    best_avg = 0
    for subject, grade in subjects.items():
        average = sum(grade)/len(grade)
        if average>best_avg:
            best_avg = average
            best_subject = subject
    return best_subject
print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))