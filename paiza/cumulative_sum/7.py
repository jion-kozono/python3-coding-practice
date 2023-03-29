N = int(input())
A = list(map(int, input().split()))

# 数列 a の a_2 から a_7 までの和を、累積和を使うことで求め、一行で出力してください。
cumulative_sum = [0] * (N+1)
for i in range(N):
    cumulative_sum[i+1] = A[i] + cumulative_sum[i]

ans = 0
for i in range(N-2):
    ans = max(ans, cumulative_sum[i+3] - cumulative_sum[i])
print(ans)
