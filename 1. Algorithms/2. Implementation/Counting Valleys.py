# https://www.hackerrank.com/challenges/counting-valleys/problem?h_r=next-challenge&h_v=zen

def countingValleys(steps, path):
    # Write your code here
    vally = 0
    mountain = 0
    for i in path:
        if i == 'D':
            mountain -= 1
        else:
            if mountain == -1:
                vally += 1
            mountain += 1
    return vally

print(countingValleys(8, 'UDDDUDUU'))