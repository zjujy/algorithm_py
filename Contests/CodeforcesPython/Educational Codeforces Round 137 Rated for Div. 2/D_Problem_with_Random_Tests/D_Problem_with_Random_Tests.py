import math
import collections
import random
from heapq import heapify, heappush, heappop
from functools import reduce
from bisect import bisect, bisect_left

# Sample Inputs/Output 
# region fastio
import sys, os
from io import BytesIO, IOBase
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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    s = input()
    
    cnt = s.count("1")
    if cnt == n:
        print(s)
        return
    if cnt == 0:
        print(0)
        return
    
    s = s.lstrip("0")
    if cnt == len(s):
        print(s)
        return

    k = s.find("0")

    v = [True] * (k + 1)
    cnt = k
    ans = list(s)
    for i, c in enumerate(ans):
        if c == "0" and cnt:
            chk = False
            for j in range(1, k + 1):
                if not v[j]:
                    continue
                # print(j, ans[i-j])
                if s[i-j] == "1":
                    ans[i] = "1"
                    chk = True
            if chk:
                for j in range(1, k + 1):
                    if not v[j]:
                        continue
                    if s[i-j] == "0":
                        v[j] = False
                        cnt -= 1
    # print(v)
    print("".join(ans).lstrip("0"))

# t = int(input())
# for _ in range(t):
solve()