import io
import sys
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
3
1 3
3 1
2 2
2
1 3
2 6
4
999999999 1000000000
333333333 999999999
1000000000 999999997
999999998 1000000000
"""

from functools import cmp_to_key
def cmp(a, b):
  if (a[0]+a[1])*b[0] == (b[0]+b[1])*a[0]: return 0
  return -1 if (a[0]+a[1])*b[0] < (b[0]+b[1])*a[0] else 1

def solve(test):
  N=int(input())
  A=[list(map(int, input().split())) for _ in range(N)]
  A=[(A[i][0],A[i][1],i) for i in range(N)]
  A.sort(key=cmp_to_key(cmp))
  ans=[A[i][2]+1 for i in range(N)]
  if test==0:
    print(*ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)