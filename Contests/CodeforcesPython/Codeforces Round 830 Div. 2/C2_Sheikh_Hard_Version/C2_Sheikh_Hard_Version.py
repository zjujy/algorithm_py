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
    n, q = mint()
    nums = ints()

    right = [n - 1] * n
    pres = [0] * (n + 1)
    xor = [0] * (n + 1)
    before = 0
    for i, a in enumerate(nums):
        pres[i+1] = pres[i] + a
        xor[i+1] = xor[i] ^ a
        if a > 0:
            right[before] = i
            before = i
    for i in range(1, n):
        if nums[i] == 0: right[i] = right[i - 1]
 
    def cal(l, r) -> int:
        return pres[r] - pres[l] - (xor[r] ^ xor[l])
 
    for _ in range(q):
        L, R = mint()
        ans = cal(L - 1, R)
        if ans == 0:
            print(L, L)
            continue

        ansl, ansr = L, R
 
        now = L - 1
 
        for i in range(min(65, R - L)):
            if cal(now, R) != ans:
                break
            
            r = R
            l = now + 1

            while l < r:
                mid = (l + r) >> 1

                if cal(now, mid) == ans:
                    r = mid
                else:
                    l = mid + 1
                    
            if r - now - 1 < ansr - ansl:
                ansl, ansr = now + 1, r
 
            now = right[now]
            if now == R - 1:
                break
 
        print(ansl, ansr)

for _ in range(sint()):
    solve()
