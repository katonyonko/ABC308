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
4
1 1 0 2
MEEX
3
0 0 0
XXX
15
1 1 2 0 0 2 0 2 0 0 0 0 0 2 2
EXMMXXXEMEXEXMM
"""

def index(i,j,k): return i*4*8+j*8+k

def solve(test):
  N=int(input())
  A=list(map(int, input().split()))
  S=input()
  dp=[0]*(N+1)*4*8
  dp[0]=1
  for i in range(N):
    for j in range(4):
      for k in range(8):
        dp[index(i+1,j,k)]+=dp[index(i,j,k)]
    for j in range(4):
      for k in range(8):
        if dp[index(i,j,k)]==0: continue
        if S[i]=="M" and j==0:
          # print(i+1,j+1,k|(1<<A[i]),index(i+1,j+1,k|(1<<A[i])),dp[index(i,j,k)])
          dp[index(i+1,j+1,k|(1<<A[i]))]+=dp[index(i,j,k)]
        elif S[i]=="E" and j==1:
          dp[index(i+1,j+1,k|(1<<A[i]))]+=dp[index(i,j,k)]
        elif S[i]=="X" and j==2:
          dp[index(i+1,j+1,k|(1<<A[i]))]+=dp[index(i,j,k)]
  x=[0,1,0,2,0,1,0,3]
  ans=sum([x[k]*dp[index(N,3,k)] for k in range(8)])
  if test==0:
    print(ans)
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