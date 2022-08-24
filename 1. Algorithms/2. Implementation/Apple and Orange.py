# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=false


# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

# Write your code here
def countApplesAndOranges(s, t, a, b, apples, oranges):
    totalApple = 0
    totalOrange = 0

    for i in apples:
        if s <= (a + i) <= t:
            totalApple += 1
    print(totalApple)
    for j in oranges:
        if s <= (b + j) <= t:
            totalOrange += 1
    print(totalOrange)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
