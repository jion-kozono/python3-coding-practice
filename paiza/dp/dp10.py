# https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_boss

n, a, b = map(int, input().split())
# recurrence formula: dp[n] = min(dp[n-1]+a, dp[n-2]+b)
dp = [0] * (n+1)
dp[0] = 0
dp[1] = a

for i in range(2, n+1):
    dp[i] = min(dp[i-1]+a, dp[i-2]+b)

print(dp[n])
