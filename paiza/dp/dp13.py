# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_boss

n, x, a, y, b, z, c = map(int, input().split())

INF = 10 ** 6

dp = [INF] * (n+z)
dp[0] = 0

for i in range(1, n+z):
    if i >= x:
        dp[i] = min(dp[i], dp[i-x]+a)
    if i >= y:
        dp[i] = min(dp[i], dp[i-y]+b)
    if i >= z:
        dp[i] = min(dp[i], dp[i-z]+c)

print(min(dp[n:]))
