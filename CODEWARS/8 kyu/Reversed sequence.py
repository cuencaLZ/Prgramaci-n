"""Get the number n to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]

FUNDAMENTALS"""


def reverseseq(n):
    n=n+1
    xs=[]
    while n>1:
        n=n-1
        xs.append(n)
    else:
        return (xs)