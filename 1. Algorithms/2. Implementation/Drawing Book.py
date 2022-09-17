# https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=false

# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

import math

# Write your code here
def pageCount(n, p):
    if n % 2 == 1 and (p == (n - 1)):
        return 0
    return int(min(math.ceil(abs(1 - p)/2),math.ceil(abs(n - p)/2)))