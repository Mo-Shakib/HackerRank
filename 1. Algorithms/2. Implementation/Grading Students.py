# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=false


import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
    
def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        elif ((math.ceil(i/5) * 5) - i) <= 2:
            new_grades.append(math.ceil(i/5) * 5)
        elif ((math.ceil(i/5) * 5) - i) > 2:
            new_grades.append(i)
    return new_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
