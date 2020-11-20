import sys
sys.setrecursionlimit(4000)

def expo(a,n):
  if n ==1:
    return a
  elif n == 0:
    return 1
  else:
    return a * expo(a,n-1)