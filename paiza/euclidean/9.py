N = int(input())
A, cal, B = input().split()
A, B = map(int, [A, B])

A %= N
B %= N

if cal == "+":
    print((A+B) % N)
elif cal == "-":
    print((A-B + N) % N)
elif cal == "*":
    print(A*B % N)
else:
    print(A**B % N)
