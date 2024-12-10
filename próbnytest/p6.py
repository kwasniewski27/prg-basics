import json
def f(years, course, average_grade):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    total = 0
    for student in data:
        if student['age'] >= years:
            for line in student['studies']['courses']:
                if course == line['name']:
                    avg = sum(line['grades'])/len(line['grades'])
                    if avg >= average_grade:
                        total += 1
    return total
print(f(21, "statistics", 4))