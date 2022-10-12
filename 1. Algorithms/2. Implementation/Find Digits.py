# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=false

#  Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    count = 0
    for i in list(str(n)):
        try:
            if n % int(i) == 0:
                count += 1
        except ZeroDivisionError:
            pass
    return count