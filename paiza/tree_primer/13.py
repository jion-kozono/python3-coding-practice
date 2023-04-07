N, K, R = map(int, input().split())

class Node:
    def __init__(self):
        self.children = []

tree = [Node() for _ in range(N)]

for _ in range(N - 1):
    a, b= input().split()
    a = int(a) - 1
    tree[a].children.append(b)

for _ in range(K):
    v, l = input().split()
    v = int(v) - 1
    l = int(l) - 1
    print(tree[v].children[l])
