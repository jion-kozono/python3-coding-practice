N = int(input())

T, xA, Bx, BxA = 0, 0, 0, 0
for i in range(N):
    s = input()
    # 最初に各文字列内のABの個数を求める
    T += s.count("AB")
    # 最後にAと最初にBがつくもののペアを見つけて、その個数を足す
    if s[0] == "B" and s[-1] == "A":
        BxA+=1
    elif s[0] == "B":
        Bx+=1
    elif s[-1] == "A":
        xA+=1

if Bx == 0 and xA == 0:
    print(T + max(BxA -1, 0))
else:
    print(T + BxA + min(Bx, xA))
