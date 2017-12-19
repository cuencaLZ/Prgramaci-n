"""Get the number n to return the sequence from n to 1. The number n can be negative and also large number. (See the range as the following)"""

def seq_to_one(n):
    if n>=1:
        x=list(range(1, n+1))
        x.reverse()
        return x
    else:
        x=list(range(n, 2))
        return x
        