# https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-one/challenges

def findMedian(arr):
    arr = sorted(arr)
    median = 0
    if len(arr) % 2 == 0:
        x = int(len(arr)//2)
        median = (arr[x] + arr[x-1])/2
    else:
        x = len(arr)//2 
        median = arr[x]
    return median