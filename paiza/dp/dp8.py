# https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_step1

n, a, b = map(int, input().split())

dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    if i >= a: dp[i] += dp[i-a]
    if i >= b: dp[i] += dp[i-b]


print(dp[n])
