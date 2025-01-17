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
    lens = ints()
    nums = []
    for _ in range(3):
        nums.append(ints())
        nums[-1].sort(reverse = True)
        
    ans = math.inf
    
    idx = [0] * 3
    while all(idx[i] < lens[i] for i in range(3)):
        ans = min(ans, sum((nums[i][idx[i]] - nums[j][idx[j]]) * (nums[i][idx[i]] - nums[j][idx[j]]) for i in range(3) for j in range(i + 1, 3)))
        mn = min(nums[i][idx[i]] for i in range(3))
        mx = -1
        # 需要先判断是否存在最小值不变的情况下，减小最大值和中间值，使得计算结果更小，并且需要优先减小最大值
        for i in range(3):
            if idx[i] == lens[i] - 1 or nums[i][idx[i] + 1] < mn: continue
            if mx == -1 or nums[i][idx[i]] > nums[mx][idx[mx]]:
                mx = i

        if mx != -1:
            idx[mx] += 1
            continue
        
        # 否则贪心的将最大值变小，注意，此时可能会得到一个更小的最小值
        for i in range(3):
            if idx[i] == lens[i] - 1: continue
            if mx == -1 or nums[i][idx[i]] > nums[mx][idx[mx]]:
                mx = i
        
        # 最大值以及中间值均无法变小，将最小值变小无意义，此时直接退出循环
        if mx == -1 or nums[mx][idx[mx]] == min(nums[i][idx[i]] for i in range(3)): break
        
        idx[mx] += 1
    print(ans)

for _ in range(int(input())):
    solve()