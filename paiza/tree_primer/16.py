from collections import defaultdict

N, R = map(int, input().split())

location = defaultdict(int)
binary_tree = [-1] * 1000000

location[R] = 0
binary_tree[0] = R

for _ in range(N - 1):
    a, b, LR = input().split()
    a = int(a)
    b = int(b)
    if LR == "L":
        location[b] = 2 * location[a] + 1
    else:
        location[b] = 2 * location[a] + 2
    binary_tree[location[b]] = b


v = int(input())
now = 0
while binary_tree[now] != -1:
    if v < binary_tree[now]:
        now = 2 * now + 1
    else:
        now = 2 * now + 2

print(binary_tree[(now - 1) // 2]) #親は逆の計算

if now % 2 == 0:
    print("R")
else:
    print("L")
