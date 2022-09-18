# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=false

# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    if k >= max(height):
        return 0
    return int(max(height) - k)
