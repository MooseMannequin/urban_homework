grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()
print(students)

average_grades = float(sum(grades[0])/len(grades[0])), float(sum(grades[1])/len(grades[1])), float(sum(grades[2])/len(grades[2])), float(sum(grades[3])/len(grades[3])), float(sum(grades[4])/len(grades[4]))
print('average_grades: ', average_grades)

students_points = {students[0]: average_grades[0], students[1]: average_grades[1], students[2]: average_grades[2], students[3]: average_grades[3], students[4]: average_grades[4]}
print(students_points)