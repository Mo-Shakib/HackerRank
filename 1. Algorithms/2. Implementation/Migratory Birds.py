# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    birds = {}
    res = 0
    for i in arr:
        if i not in birds:
            birds[i] = [i]
        else:
            birds[i] = birds[i] + [i]
    
    arr = [*set(arr)]
    max_ = i
    for i in arr:
        if len(birds[i]) > len(birds[max_]):
            max_ = i
    return max_

migratoryBirds([1, 1, 2, 2, 3])