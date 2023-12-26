import sys

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
    cnt = 0
    for _ in range(n):
        x, y = mint()
        if x > 0:
            cnt |= 1
        elif x < 0:
            cnt |= 2
        if y > 0:
            cnt |= 4
        elif y < 0:
            cnt |= 8
    print("NO" if cnt == 15 else "YES")


for _ in range(int(input())):
    solve()
