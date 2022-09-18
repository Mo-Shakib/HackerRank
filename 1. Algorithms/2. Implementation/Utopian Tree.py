# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    x = 1
    for i in range(1,n+1):
        if i % 2 == 1:
            x *= 2
        else:
            x += 1
    return x
