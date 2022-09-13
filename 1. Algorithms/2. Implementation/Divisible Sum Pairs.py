# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=next-challenge&h_v=zen

# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    res = 0
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                print(ar[i], ar[j])
                res += 1
    return res