# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=false

# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
import string

def designerPdfViewer(h, word):
    # Write your code here
    heights = {}
    letters = [*string.ascii_lowercase[:26]]
    for i in range(26):
        heights[letters[i]] = h[i]
    
    max_height = []

    for i in word:
        max_height.append(heights[i])
    
    return int(max(max_height)*len(word))
