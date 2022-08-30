# https://www.hackerrank.com/challenges/kangaroo/problem

import os

# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2

# Write your code here
def kangaroo(x1, v1, x2, v2):
    
  k1 = x1 + v1
  k2 = x2 + v2

  if k1 == k2:
    return "YES"

  elif ((k1 < k2) and (v1 < v2)) or ((k1 > k2) and (v1 > v2)):
    return 'NO'
  
  elif ((k1 > k2) and (v1 == v2)) or ((k1 < k2) and (v1 == v2)):
    return 'NO'
    
  elif (k1 < k2) and (v1 > v2):
    while k1 != k2:
      k1 += v1
      k2 += v2
      if k1 > k2:
        return "NO"
      elif k1 == k2:
        return "YES"
  
  elif (k1 > k2) and (v1 < v2):
    while k1 != k2:
      k1 += v1
      k2 += v2
      if k1 < k2:
        return "NO"
      elif k1 == k2:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
