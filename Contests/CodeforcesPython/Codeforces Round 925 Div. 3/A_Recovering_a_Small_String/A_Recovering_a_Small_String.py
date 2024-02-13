import sys
from string import ascii_lowercase

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    ans = []
    for i in range(3):
        c = max(1, n - 26 * (2 - i))
        n -= c
        ans.append(ascii_lowercase[c - 1])
    print("".join(ans))


for _ in range(int(input())):
    solve()
