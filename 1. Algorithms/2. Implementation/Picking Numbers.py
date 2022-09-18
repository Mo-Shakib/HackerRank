# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=false

# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a = sorted(a)
    
    subarray = 1
    lengths = []
    prev = a[0]

    for i in a[1:]:
        if abs(i - prev) <= 1:
            subarray += 1
        else:
            prev = i
            lengths.append(subarray)
            subarray = 1
    
    if len(lengths) != 0:
        return max(lengths)
    
    return subarray