# https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step1

INF = 10 ** 8
n, a, b = map(int, input().split())
dp = [INF] * (n+4)
dp[0] = 0

for i in range(2, n+4):
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2]+a)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5]+b)

# n個以上購入時の最安値
print(min(dp[n:]))
