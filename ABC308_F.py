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
3 3
4 3 1
4 4 2
2 3 1
10 5
9 7 1 5 2 2 5 5 7 6
7 2 7 8 2
3 2 4 1 2
"""

#multiset
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')
class SortedMultiset(Generic[T]):
  BUCKET_RATIO = 50
  REBUILD_RATIO = 170
 
  def _build(self, a=None) -> None:
      "Evenly divide `a` into buckets."
      if a is None: a = list(self)
      size = self.size = len(a)
      bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
      self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
 
  def __init__(self, a: Iterable[T] = []) -> None:
      "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
      a = list(a)
      if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
          a = sorted(a)
      self._build(a)
 
  def __iter__(self) -> Iterator[T]:
      for i in self.a:
          for j in i: yield j
 
  def __reversed__(self) -> Iterator[T]:
      for i in reversed(self.a):
          for j in reversed(i): yield j
 
  def __len__(self) -> int:
      return self.size
 
  def __repr__(self) -> str:
      return "SortedMultiset" + str(self.a)
 
  def __str__(self) -> str:
      s = str(list(self))
      return "{" + s[1 : len(s) - 1] + "}"
 
  def _find_bucket(self, x: T) -> List[T]:
      "Find the bucket which should contain x. self must not be empty."
      for a in self.a:
          if x <= a[-1]: return a
      return a
 
  def __contains__(self, x: T) -> bool:
      if self.size == 0: return False
      a = self._find_bucket(x)
      i = bisect_left(a, x)
      return i != len(a) and a[i] == x
 
  def count(self, x: T) -> int:
      "Count the number of x."
      return self.index_right(x) - self.index(x)
 
  def add(self, x: T) -> None:
      "Add an element. / O(√N)"
      if self.size == 0:
          self.a = [[x]]
          self.size = 1
          return
      a = self._find_bucket(x)
      insort(a, x)
      self.size += 1
      if len(a) > len(self.a) * self.REBUILD_RATIO:
          self._build()
 
  def discard(self, x: T) -> bool:
      "Remove an element and return True if removed. / O(√N)"
      if self.size == 0: return False
      a = self._find_bucket(x)
      i = bisect_left(a, x)
      if i == len(a) or a[i] != x: return False
      a.pop(i)
      self.size -= 1
      if len(a) == 0: self._build()
      return True
 
  def lt(self, x: T) -> Union[T, None]:
      "Find the largest element < x, or None if it doesn't exist."
      for a in reversed(self.a):
          if a[0] < x:
              return a[bisect_left(a, x) - 1]
 
  def le(self, x: T) -> Union[T, None]:
      "Find the largest element <= x, or None if it doesn't exist."
      for a in reversed(self.a):
          if a[0] <= x:
              return a[bisect_right(a, x) - 1]
 
  def gt(self, x: T) -> Union[T, None]:
      "Find the smallest element > x, or None if it doesn't exist."
      for a in self.a:
          if a[-1] > x:
              return a[bisect_right(a, x)]
 
  def ge(self, x: T) -> Union[T, None]:
      "Find the smallest element >= x, or None if it doesn't exist."
      for a in self.a:
          if a[-1] >= x:
              return a[bisect_left(a, x)]
 
  def __getitem__(self, x: int) -> T:
      "Return the x-th element, or IndexError if it doesn't exist."
      if x < 0: x += self.size
      if x < 0: raise IndexError
      for a in self.a:
          if x < len(a): return a[x]
          x -= len(a)
      raise IndexError
 
  def index(self, x: T) -> int:
      "Count the number of elements < x."
      ans = 0
      for a in self.a:
          if a[-1] >= x:
              return ans + bisect_left(a, x)
          ans += len(a)
      return ans
 
  def index_right(self, x: T) -> int:
      "Count the number of elements <= x."
      ans = 0
      for a in self.a:
          if a[-1] > x:
              return ans + bisect_right(a, x)
          ans += len(a)
      return ans

def solve(test):
  N,M=map(int, input().split())
  P=sorted(list(map(int, input().split())))
  L=list(map(int, input().split()))
  D=list(map(int, input().split()))
  ms=SortedMultiset(P)
  X=sorted([(D[i],L[i]) for i in range(M)], reverse=True)
  ans=sum(P)
  for i in range(M):
    d,l=X[i]
    x=ms.ge(l)
    if x==None:
      continue
    else:
      ms.discard(x)
      ans-=d
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