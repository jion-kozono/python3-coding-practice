n = int(input())

def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if not is_prime[p]: continue
        for q in range(2*p, n + 1, p):
            is_prime[q] = False
    return is_prime

print("YES" if eratosthenes_sieve(n)[n] else "NO")
