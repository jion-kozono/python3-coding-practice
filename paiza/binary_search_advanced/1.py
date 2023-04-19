import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()

# 薬品を x 回使った場合、得られる情報は最大で 2^x 通りとなります。
# したがって、N 通りある候補から感染者を必ず特定するためには、薬品の使用回数 x が N ≦ 2^x を満たす必要があります。
# 二分探索の考え方を応用し、感染していないことがまだ確定していない人のうち約半数に対する検査を繰り返すことにします。
# もし検査した集団が陽性ならば、残りの半分はもう検査しなくてよく、逆に陰性ならば、その集団はもう検査しなくてよいです。
# このようにして集団を半々にしていくことで、x 回以内に感染者を必ず特定することができます。(簡単な証明としては、上の不等式を変形することで N / 2x ≦ 1 が成り立ちます。)
# よって、この不等式を満たす x のうち最小の値が答えになります。

num = 1
ans = 0

while num < N :
    num *= 2
    ans += 1

print(ans)
