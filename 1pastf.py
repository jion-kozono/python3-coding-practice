S = input()

words = []
i = 0
while i < len(S):
    # 初めてS[i]が大文字になるjを見つける
    j = i+1
    while j < len(S) and S[j].islower():
        j+=1

    words.append(S[i:j+1])

    # i を j + 1進める
    i=j+1

# 単語を大文字小文字を無視した状態で辞書順にソートする
words.sort(key=str.lower)

#単語を連結して出力する
print("".join(words))
