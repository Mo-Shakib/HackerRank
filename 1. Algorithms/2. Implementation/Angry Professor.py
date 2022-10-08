# https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=false

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a

def angryProfessor(k, a):
    # Write your code here
    n = 0
    for arrive in a:
        if arrive <= 0:
            n += 1
    if k <= n:
        return 'NO'
    return 'YES'

