# https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step3

x, d_1, d_2 = map(int, input().split())
Q = int(input())

for i in range(Q):
    k = int(input())
    a = [0] * (k+1)
    a[1] = x
    for i in range(2, k+1):
        if i % 2 != 0:
            a[i] = a[i-1] + d_1
        else:
            a[i] = a[i-1] + d_2
    print(a[k])
