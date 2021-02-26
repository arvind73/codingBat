Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

def diff21(n):
  if n<21:
    return abs(n-21)
  elif n==21:
    return 0
  else:
    return abs(n-21)*2
