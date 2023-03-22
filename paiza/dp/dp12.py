# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step2

n, x, a, y, b = map(int, input().split())

INF = 10 ** 6

dp = [INF] * (n+y)
dp[0] = 0

for i in range(1, n+y):
    if i >= x:
        dp[i] = min(dp[i], dp[i-x]+a)
    if i >= y:
        dp[i] = min(dp[i], dp[i-y]+b)

print(min(dp[n:]))
