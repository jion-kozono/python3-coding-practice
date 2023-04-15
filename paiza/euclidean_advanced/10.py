# https://paiza.jp/works/mondai/reviews/show/bd586e383ac84b9c3abb1250f2335f4e
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, a, c = map(int, input().split())
min_move = gcd(a, c)
none = True
for b in range(1, 1001):
    tmp = gcd(min_move, b)
    if n % tmp != 0:
        print(b)
        none = False
if none:
    print(-1)
