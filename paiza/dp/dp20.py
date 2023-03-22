# https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_step2

n, x = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [n + 1] * (x + 1)
dp[0] = 0

for val in a:
    for j in range(x, val - 1, -1):
        if dp[j - val] != n + 1:
            dp[j] = min(dp[j], dp[j - val] + 1)

if dp[x] == n + 1:
    print(-1)
else:
    print(dp[x])

# n, x = map(int, input().split())
# A = [int(input()) for i in range(n)]
# # n * x の２次元配列を作成
# dp = [[10**9]*(x + 1) for _ in range(n)]

# # 0列目はすべて0
# dp[0][0] = 0

# if A[0] <= x:
#     dp[0][A[0]] = 1

# for i in range(1,n):
#     for j in range(x + 1):
#         if A[i] <= j:
#             dp[i][j] = min(dp[i - 1][j - A[i]]+1, dp[i -1][j])
#         else:
#             dp[i][j] = dp[i - 1][j]
# if dp[n-1][x] == 10**9:
#     print(-1)
# else:
#     print(dp[n-1][x])
