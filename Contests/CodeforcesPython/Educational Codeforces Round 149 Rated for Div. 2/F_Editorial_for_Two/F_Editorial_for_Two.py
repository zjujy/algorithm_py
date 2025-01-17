import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = mint()
    nums = ints()

    def check(x) -> bool:
        left = [0] * (n + 1)
        h = []
        s = 0
        for i, a in enumerate(nums):
            if s + a <= x:
                s += a
                heappush(h, -a)
            elif h and -h[0] > a:
                s += a
                s += heappushpop(h, -a)
            left[i + 1] = len(h)
        
        h = []
        s = 0
        for i in range(n - 1, -1, -1):
            a = nums[i]
            if s + a <= x:
                s += a
                heappush(h, -a)
            elif h and -h[0] > a:
                s += a
                s += heappushpop(h, -a)
            if len(h) + left[i] >= k:
                return True
        return False

    pres = list(accumulate(sorted(nums), initial = 0))
    l, r = pres[(k + 1) // 2], pres[k] - pres[k // 2]
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)

for _ in range(int(input())):
    solve()