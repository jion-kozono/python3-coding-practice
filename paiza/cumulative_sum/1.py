A = [1,5,9,7,5,3,2,5,8,4]

# a_2 から a_7 までの和 (a_2 + a_3 + ... + a_7) を、累積和を使うことで求めてください。

cumulative_sum = [0] * 11
for i in range(len(A)):
    cumulative_sum[i+1] = A[i] + cumulative_sum[i]

print(cumulative_sum[8] - cumulative_sum[2])
