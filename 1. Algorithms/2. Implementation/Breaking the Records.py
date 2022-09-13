# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=zen

# Write your code here

def breakingRecords(scores):
    highScores = 0
    lowScores = 0
    max_score = scores[0]
    min_score = scores[0]
    for i in scores:
        if i > max_score:
            highScores += 1
            max_score = i
    
    for i in scores:
        if i < min_score:
            lowScores += 1
            min_score = i
    
    return highScores, lowScores
