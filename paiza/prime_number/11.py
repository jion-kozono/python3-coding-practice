def eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n+1):
        if not is_prime[i]: continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return is_prime

n = int(input())
is_prime = eratosthenes(n)
max_multi = 0
ans = [-1,-1]
for i in range(2, n//2+1):
    j = n-i
    if is_prime[i] and is_prime[j]:
        if i*j > max_multi:
            max_multi = i*j
            ans = [i, j]
print(ans[0])
print(ans[1])
