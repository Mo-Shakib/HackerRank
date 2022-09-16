# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=next-challenge&h_v=legacy

# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

# Write your code here
def dayOfProgrammer(year):
    if year > 1917:
        if year == 1918:
            return '26.09.1918'

        if (year % 400 == 0):
            return f'12.09.{year}'
        
        elif (year % 4 == 0 and year % 100 != 0):
            return f'12.09.{year}'
    
    elif year < 1917:
        if year % 4 == 0:
            return f'12.09.{year}'
    
    return f'13.09.{year}'