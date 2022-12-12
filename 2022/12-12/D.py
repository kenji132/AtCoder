from collections import defaultdict

N, D = map(int, input().split())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


dp = [defaultdict(int) for _ in range(N + 1)]
dp[0][1] = 1

for i in range(1, N + 1):
    for d, p in dp[i - 1].items():
        for k in range(1, 6 + 1):
            dp[i][gcd(d * k, D)] += p / 6
ans = dp[N][D]
print(ans)
