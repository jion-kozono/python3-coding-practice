# https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_step0

n = int(input())

# dp = [0] * (n+1)
# dp[0] = 1
# for i in range(1, n+1):
#     if i >= 1:
#         dp[i] = dp[i] + dp[i-1]
#     if i >= 2:
#         dp[i] = dp[i] + dp[i-2]

# print(dp[n])

n = int(input())

dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
