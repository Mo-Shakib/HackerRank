# https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=false

# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    if len(s) > n:
        return s[:n].count('a')
    return s.count('a') * (n // len(s)) + s[:n%len(s)].count('a')
