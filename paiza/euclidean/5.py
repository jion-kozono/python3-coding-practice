# https://paiza.jp/works/mondai/euclidean_primer/euclidean_primer__extgcd?language_uid=python3
a, b = map(int, input().split())

def extGCD(a, b):
    if b:
        d, y, x = extGCD(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

a, x, y =extGCD(a,b)
print(x,y)
