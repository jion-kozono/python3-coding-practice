n = int(input())

a = 2
fermat = 1
for i in range(n-1):
    fermat*=a
    fermat%=n

is_prime = True
if n % a == 0:
    is_prime = False

if fermat % n != 1:
    is_prime = False

print("YES" if is_prime else "NO")
