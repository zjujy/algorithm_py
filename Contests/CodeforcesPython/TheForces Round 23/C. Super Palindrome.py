import sys

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

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
# from types import GeneratorType
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
    n = sint()
    s = input()
    ans = 0
    eq = ne = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            if ne >= 3:
                x = ne - 2
                ans += (x + 1) // 2 * (x + 2 - (x & 1)) // 2
            ne = 1
            eq += 1
        else:
            if eq >= 3:
                ans += (eq - 2) * (eq - 1) // 2
            eq = 1
            ne += 1
    if ne >= 3:
        x = ne - 2
        ans += (x + 1) // 2 * (x + 2 - (x & 1)) // 2
    if eq >= 3:
        ans += (eq - 2) * (eq - 1) // 2
    eq = 1
    
    print(ans)

for _ in range(int(input())):
    solve()