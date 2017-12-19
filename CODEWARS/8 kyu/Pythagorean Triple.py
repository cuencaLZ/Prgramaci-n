"""Given an array of 3 integers a, b and c, determine if they form a pythagorean triple.

A pythagorean triple is formed when:

c2 = a2 + b2
where c is the largest value of a, b, c.

For example: a = 3, b = 4, c = 5 forms a pythagorean triple, because 52 = 32 + 42

Return Values
1 if a, b and c form a pythagorean triple
0 if a, b and c do not form a pythagorean triple
For Python: return True or False"""

def pythagorean_triple(integers):
      c=integers[2]
      b=integers[1]
      a=integers[0]
      if c>b and c>a:
          return c**2==b**2+a**2
      if b>c and b>a:
          return b**2==c**2+a**2
      if a>b and a>c:
          return a**2==b**2+c**2
          