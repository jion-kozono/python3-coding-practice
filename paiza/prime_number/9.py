def GCD(x, y):
        return GCD(y,x%y) if x % y else y

from math import gcd
n = int(input())


ans = int(input())
for i in range(1, n):
    a = int(input())
    ans = gcd(ans, a)
print(ans)
