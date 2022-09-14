# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Write your code here

def migratoryBirds(arr):    
    birds = {}
    for i in arr:
        if i not in birds:
            birds[i] = [i]
        else:
            birds[i] = birds[i] + [i]
    
    arr = sorted([*set(arr)])
    max_ = arr[0]
    for i in arr:
        if len(birds[i]) > len(birds[max_]):
            max_ = i
    return max_