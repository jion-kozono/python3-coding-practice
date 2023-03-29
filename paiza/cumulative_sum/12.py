N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# 数列 a の a_2 から a_7 までの和を、累積和を使うことで求め、一行で出力してください。
cumulative_sum = [0] * (N+1)
for i in range(N):
    if A[i] % 2 == 0:
        cumulative_sum[i+1] = cumulative_sum[i] + 1
    else:
        cumulative_sum[i+1] = cumulative_sum[i]

print(cumulative_sum[Y+1] - cumulative_sum[X])
