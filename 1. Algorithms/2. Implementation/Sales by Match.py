# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true



# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    unique = [*set(ar)]
    res = 0
    
    for i in unique:
        if ar.count(i) % 2 == 0:
            res += ar.count(i)//2
    
        else:
            res += ((ar.count(i)+1)//2)-1
    
    return int(res)