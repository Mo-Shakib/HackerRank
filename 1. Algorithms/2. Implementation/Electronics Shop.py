# https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=next-challenge&h_v=zen

def getMoneySpent(keyboards, drives, b):
    prices = []
    for i in keyboards:
        for j in drives:
            if (i + j) <= b:
                prices.append(i+j)
    if len(prices) == 0:
        return -1
    return max(prices)
