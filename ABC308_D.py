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
2 3
sns
euk
2 2
ab
cd
5 7
skunsek
nukesnu
ukeseku
nsnnesn
uekukku
"""

def bfs(G,s):
  inf=10**30
  D=[inf]*len(G)
  D[s]=0
  dq=deque()
  dq.append(s)
  while dq:
    x=dq.popleft()
    for y in G[x]:
      if D[y]>D[x]+1:
        D[y]=D[x]+1
        dq.append(y)
  return D

def solve(test):
  H,W=map(int, input().split())
  S=[input() for _ in range(H)]
  a='snuke'
  s=[-1]*26
  for i in range(5):
    s[ord(a[i])-ord('a')]=i
  G=[[] for _ in range(H*W)]
  for i in range(H):
    for j in range(W):
      for k in range(4):
        ni=i+[-1,0,1,0][k]
        nj=j+[0,1,0,-1][k]
        if 0<=ni<H and 0<=nj<W and (s[ord(S[i][j])-ord('a')]+1)%5==s[ord(S[ni][nj])-ord('a')]:
          G[i*W+j].append(ni*W+nj)
  D=bfs(G,0)
  ans='Yes' if D[H*W-1]<10**30 else 'No'
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