"""
Given N students, each student has name, ID, and MARKS.
Task is to find the average marks of the students.
The program should have less than 4 lines of code.
"""

N, column_headers = int(input()), input().split()
test_cases = [input().split() for _ in range(N)]
idx = [
    header_idx for header_idx, header in enumerate(column_headers) if header == "MARKS"
][0]
print(sum([int(test_case[idx]) for test_case in test_cases]) / N)
