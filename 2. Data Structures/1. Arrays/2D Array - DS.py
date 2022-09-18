# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=false



# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]]

def hourglassSum(arr):
    # Write your code here
    sums = []
    
    for i in range(3):
        n = 0
        for j in range(3):
            print(arr[j][n:n+3])
            n += 1

hourglassSum(arr)