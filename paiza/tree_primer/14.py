from collections import defaultdict

N, K, R = map(int, input().split())

binary_tree = defaultdict(int)
location = defaultdict(int)

binary_tree[0] = R
location[R] = 0

for i in range(N - 1):
    a, b, lr = input().split()
    a = int(a)
    b = int(b)

    if lr == "L":
        location[b] = 2 * location[a] + 1
    else:
        location[b] = 2 * location[a] + 2

    binary_tree[location[b]] = b

for i in range(K):
    v, lr = input().split()
    v = int(v)
    if lr == "L":
        print(binary_tree[location[v] * 2 + 1])
    else:
        print(binary_tree[location[v] * 2 + 2])
