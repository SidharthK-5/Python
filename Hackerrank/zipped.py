"""
Given N no. of students and X no. of subjects for each
Print the average marks of each student in each subject
"""

num_students, num_subjects = map(int, input().split())
student_marks = [list(map(float, input().split())) for _ in range(num_subjects)]
zipped_marks = list(zip(*student_marks))
print(*[sum(student) / len(student) for student in zipped_marks], sep="\n")
