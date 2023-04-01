N = int(input())

# バケットサイズ
M = 101

exist = [0] * M

for i in range(N):
    d = int(input())

    # update bucket
    exist[d] = 1

print(sum(exist))

# 以下はsetを使う方法
S = set(input() for i in range(N))
print(len(S))
