names = ["alex", "ben", "cam", "dick", "ellen", "feather"]
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

# WRONG: passed_students = {passed_student:student_scores for (student, students_scores) in student_scores() if student_scores > 70}
# SYNTAX: passed_students = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
