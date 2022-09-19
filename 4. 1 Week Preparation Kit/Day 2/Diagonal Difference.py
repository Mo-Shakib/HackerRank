# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

def diagonalDifference(arr):
    length = len(arr)
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)-1

    for i in range(length):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][n]
        n -= 1            
    return abs(left_diagonal - right_diagonal)