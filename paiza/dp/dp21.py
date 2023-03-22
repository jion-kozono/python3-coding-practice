# https://paiza.jp/works/mondai/dp_primer/dp_primer_partial_sums_boss

n, x = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [False] * (x + 1)
dp[0] = True

for val in a:
    for j in range(val, x + 1):
        if dp[j - val]:
            dp[j] = True

if dp[x]:
    print("yes")
else:
    print("no")

# # 個数制限なし部分和問題
# n, x = map(int, input().split())
# A = [int(input()) for i in range(n)]
# # n * x の２次元配列を作成
# dp = [[0]*(x + 1) for _ in range(n+1)]

# # 重さ0, 0個目のおもりについて
# dp[0][0] = 1

# for i in range(1, n+1):
#     for j in range(x + 1):
#         ref = dp[i - 1][j]  # ref = reference(参照)の意味
#         if A[i-1] > j: # コスト不足のとき
#             dp[i][j] = ref
#         else:
#             ref_back = dp[i-1][j - A[i-1]]
#             ref_back_i = dp[i][j - A[i-1]]
#             # 間違い: dp[i][j] = min(ref,ref_back,ref_back_i) 正しくは下
#             # dp[i][j] = ref or ref_back or ref_back_i これでも通るが下の方が必要最小限
#             dp[i][j] = ref or ref_back_i

# print("yes" if dp[n][x] else "no")
