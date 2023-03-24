n = int(input())

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0: # 偶数はあらかじめ除く
        return False

    for i in range(3, int(n**0.5) + 1, 2): #奇数だけを判定
        if n % i == 0:
            return False
    return True

print("YES" if is_prime(n) else "NO")
