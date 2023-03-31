# この数列において、総和が 15 以下の区間のうち、最大の長さを求めてください。
# https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__syakutori_length_step1

# n, k = map(int, input().split())
n, k = 10, 15
a = list(map(int, input().split()))
max_section = 0 # 最大の区間の長さ
elements_sum = 0 # 区間内の要素の和を格納する変数
right = 0

# ① left を固定し、条件を満たす間 right を 1 ずつ進めていき、right がそれ以上進めなくなったとき、
#    right - left とすることでそれまでの条件を満たす区間の数を求めることができる
# ② right がこれ以上右に進めなくなったとき、left を 1 進め、また ① に戻る
# ③ ただし、left == right となったときは、right を 1 進める

for left in range(n):
    while right < n:
        if elements_sum + a[right] <= k:
            elements_sum += a[right]
            right += 1
        else:
            break #②

    max_section = max(max_section, right - left)

    if right == left:
        right += 1
    else:
        elements_sum -= a[left]

print(max_section)
