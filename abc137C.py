from collections import defaultdict

N = int(input())

# num[s] : 文字列sが何個あるか
num = defaultdict(int)
for i in range(N):
    # 入力の文字列をソートしておく
    s = "".join(sorted(input()))

    num[s] += 1

# 集計
result = 0
for s in num:
    # 文字列sがn個ある
    n = num[s]

    # nC2を足す
    result += n*(n-1)//2

print(result)
