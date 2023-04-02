import bisect,collections,copy,heapq,itertools,math,string
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())

N = I()
A = LS()

st = []

for i in range(N):
    if A[i] == "+" or A[i] == "-":
        num1 = st.pop()
        num2 = st.pop()
        if A[i] == "+":
            st.append(num1 + num2)
        else:
            st.append(num2 - num1)
    else:
        st.append(int(A[i]))
print(st[-1])
