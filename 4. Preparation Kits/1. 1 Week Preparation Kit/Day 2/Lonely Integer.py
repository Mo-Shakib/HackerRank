# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

def lonelyinteger(a):
    # Write your code here
    if len(a) == 1:
        return a[0]
    
    singleElement = set()
    for i in a:
        if i in singleElement:
            singleElement.remove(i)
        else:
            singleElement.add(i)
    return [*singleElement][0]