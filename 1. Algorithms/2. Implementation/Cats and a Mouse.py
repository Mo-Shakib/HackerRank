# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true

def catAndMouse(x, y, z):
    # cat A -> x
    # cat B -> y
    # mouse C -> z

    if abs(x - z) < abs(y-z):
        return 'Cat A'
    elif abs(x - z) > abs(y-z):
        return 'Cat B'
    if abs(x - z) == abs(y-z):
        return 'Mouse C'
        