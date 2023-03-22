S = input()
N = len(S)

dp = [False] * (N+1)

dp[0] = True
for i in range(N+1):
    if i >= 5 and dp[i-5] and S[i-5:i] == "erase":
        dp[i] = True
    if i >= 6 and dp[i-6] and S[i-6:i] == "eraser":
        dp[i] = True
    if i >= 5 and dp[i-5] and S[i-5:i] == "dream":
        dp[i] = True
    if i >= 7 and dp[i-7] and S[i-7:i] == "dreamer":
        dp[i] = True

print("Yes" if dp[N] else "No")
