count_students = int(input())
students = {}

for _ in range(count_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for data in students.items():
    average_grade = sum(data[1]) / len(data[1])
    grades = [f"{grade:.2f}" for grade in data[1]]
    print(f"{data[0]} -> {' '.join(grades)} (avg: {average_grade:.2f})")
