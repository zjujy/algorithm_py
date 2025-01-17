import itertools
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from collections import *
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase
from string import *

# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
        
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))
# endregion fastio

# region interactive
def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = int(input())
    arr = ints()

    if n == 1:
        print(-1)
        return

    arr.sort()
    if arr[0] == arr[-1]:
        print(1)
        print(arr[0])
        return

    ans = []

    cnt = Counter()
    diff = arr[1] - arr[0]
    cnt[diff] += 1
    tmp = -1
    for j in range(2, n):
        if arr[j] - arr[j - 1] != diff:
            tmp = arr[j - 1]
        cnt[arr[j] - arr[j - 1]] += 1

    if len(cnt.keys()) == 1:
        ans.append(arr[0] - diff)
        ans.append(arr[-1] + diff)
        if n == 2 and not (diff & 1):
            ans.append(arr[0] + diff // 2)
    elif len(cnt.keys()) == 2:
        key = sorted(cnt.keys())
        mn, mx = key[0], key[1]
        if mx == mn * 2 and cnt[mx] == 1:
            if mx == diff:
                ans.append(arr[0] + mn)
            else:
                ans.append(tmp + mn)

    ans.sort()
    print(len(ans))
    print(*ans)

# for _ in range(int(input())):
solve()