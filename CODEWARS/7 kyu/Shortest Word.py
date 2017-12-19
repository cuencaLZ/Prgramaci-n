"""x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""

def find_short(s):
      a= s.split()
      a.sort(cmp=None, key=len, reverse=False)
      y=a[0]
      return len (y)