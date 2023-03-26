a, b,c = map(int, input().split())

# 整数 A,B,C が与えられるので、Ax + By = C の整数解 x , y の値を 1 行で半角スペース区切りで出力してください。
# 解の組 (x , y) のうち、x または y が 1 であるような解の組の値を出力してください。

x = y = 0
if (a % b == c):
    x = 1
    y = -(a // b)
else:
    x = -(b // a)
    y = 1
print(x, y)
