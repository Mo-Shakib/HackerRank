# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    beautifuldays = 0
    for day in range(i, j+1):
        if abs(day-int(str(day)[::-1])) % k == 0:
            beautifuldays += 1
    return beautifuldays
