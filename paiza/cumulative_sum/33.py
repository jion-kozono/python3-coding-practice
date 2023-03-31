# https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__syakutori_count_step1

# 数列において、長さが 1 以上で総和が 15 以下の区間がいくつあるか求めてください。
a = [1, 5, 9, 1, 20, 5, 3, 6, 5, 4]
section_count = 0 # 条件を満たす区間の数を格納する変数
elements_sum = 0 # 区間内の要素の和を格納する変数
right = 0

# ① left を固定し、条件を満たす間 right を 1 ずつ進めていき、right がそれ以上進めなくなったとき、
#    right - left とすることでそれまでの条件を満たす区間の数を求めることができる
# ② right がこれ以上右に進めなくなったとき、left を 1 進め、また ① に戻る
# ③ ただし、left == right となったときは、right を 1 進める

for left in range(10):
    while right < 10:
        if elements_sum + a[right] <= 15:
            elements_sum += a[right]
            right += 1
        else:
            break #②

    section_count += right - left

    if right == left:
        right += 1
    else:
        elements_sum -= a[left]

print(section_count)
