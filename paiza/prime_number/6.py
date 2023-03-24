def eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return is_prime

is_prime = eratosthenes(6000010)

n = int(input())
for i in range(n):
    a = int(input())
    print("pass" if is_prime[a] else "failure")
