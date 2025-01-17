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
    n, m = mint()
    s = []
    ans = 26 * m
    for i in range(n):
        s.append(list(map(ord, input())))
        for j in range(i):
            ans = min(ans, sum(abs(x - y) for x, y in zip(s[i], s[j])))
    print(ans)

for _ in range(int(input())):
    solve()