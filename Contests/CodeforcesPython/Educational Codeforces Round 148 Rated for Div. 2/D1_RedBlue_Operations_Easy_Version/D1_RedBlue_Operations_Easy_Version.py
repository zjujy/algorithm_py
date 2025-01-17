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
    n, q = mint()
    arr = ints()
    krr = ints()

    arr.sort()
    ans = [0] * q

    for i in range(q):
        k = krr[i]
        tmp = arr.copy()
        for j in range(n):
            tmp[j] += k
            k -= 1
            if k == 0: break

        if k & 1:
            k += 1
            tmp[-1] -= k
        
        neg = k // 2
        s, res = 0, math.inf
        for a in tmp:
            s += a
            res = min(res, a)
        
        neg -= s - res * n
        if neg > 0:
            res -= (neg + n - 1) // n
        
        ans[i] = res

    print(*ans)

# for _ in range(int(input())):
solve()