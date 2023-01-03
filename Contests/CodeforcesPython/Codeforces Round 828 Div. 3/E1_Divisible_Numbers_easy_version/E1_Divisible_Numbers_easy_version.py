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
    a, b, c, d = map(int, input().split())

    ab = a * b
    for i in range(a + 1, c + 1):
        k = math.lcm(i, ab) // i
        r = (b + k - 1) // k
        if r * k == b:
            r += 1
        if r * k <= d:
            print(i, r * k)
            return
    print(-1, -1)

    # x1 = x2 = y1 = y2 = 0
    
    # for i in range(a + 1, c + 1):
    #     if not x1 and i % a == 0:
    #         x1 = i
    #     if not y1 and i % b == 0:
    #         y1 = i
    #     if x1 and y1:
    #         break
    # for i in range(b + 1, d + 1):
    #     if not x2 and i % a == 0:
    #         x2 = i
    #     if not y2 and i % b == 0:
    #         y2 = i
    #     if x2 and y2:
    #         break
        
    # if x1 and y2:
    #     print(x1, y2)
    # elif x2 and y1:
    #     print(x2, y1)
    # else:
    #     print(-1)

t = int(input())
for _ in range(t):
    solve()