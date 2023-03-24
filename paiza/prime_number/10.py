def GCD(x, y):
        return GCD(y,x%y) if x % y else y
# GCD * LCM = x *y
def LCM(x, y):
        return x*y//GCD(x,y)

# from math import gcd
n = int(input())

ans = int(input())
for i in range(1, n):
    a = int(input())
    ans = LCM(ans, a)
print(ans)
