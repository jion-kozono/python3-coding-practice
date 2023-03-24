# n = int(input())

# ans = 0

# for i in range(1, int(n**0.5)+1):
#     if n % i != 0:
#         continue
#     ans += 1

#     if i != n//i:
#         ans+=1
# print(ans)

import collections

def prime_factorize(n):
    prime_factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i

    if n != 1:
        prime_factors.append(n)
    return prime_factors

n = int(input())
pf = prime_factorize(n)
pf_count = collections.Counter(pf)

ans = 1
for v in pf_count.values():
    ans *= (v+1)
print(ans)
