N, K, R = map(int, input().split())

class Node:
    def __init__(self):
        self.left = -1
        self.right = -1

tree = [Node() for _ in range(N)]

for _ in range(N - 1):
    a, b, lr = input().split()
    a = int(a) - 1
    b = int(b) - 1
    if lr == "L":
        tree[a].left = b
    elif lr == "R":
        tree[a].right = b

for _ in range(K):
    v, lr = input().split()
    v = int(v) - 1
    if lr == "L":
        if tree[v].left != -1:
            print(tree[v].left + 1)
        else:
            print()
    elif lr == "R":
        if tree[v].right != -1:
            print(tree[v].right + 1)
        else:
            print()
