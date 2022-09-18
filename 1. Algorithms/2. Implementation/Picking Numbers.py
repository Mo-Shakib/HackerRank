# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=false

# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a = sorted(a)
    subarray = []
    lengths = []
    prev = a[0]
    subarray.append(prev)
    for i in a[1:]:
        if abs(i - prev) <= 1:
            subarray.append(i)
        else:
            prev = i
            lengths.append(len(subarray))
            subarray.clear()
            subarray.append(prev)
    
    return max(lengths)
    





print(pickingNumbers([4,6,5,3,3,1]))