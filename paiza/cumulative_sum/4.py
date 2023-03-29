n,x,y = map(int,input().split())
A = list(map(int, input().split()))

# 数列 a の a_2 から a_7 までの和を、累積和を使うことで求め、一行で出力してください。
cumulative_sum = [0] * (n+1)
for i in range(n):
    cumulative_sum[i+1] = A[i] + cumulative_sum[i]

print(cumulative_sum[y+1] - cumulative_sum[x])
