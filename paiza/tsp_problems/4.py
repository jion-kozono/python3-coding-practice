from math import sqrt, pow


def dist(a, b):
    return sqrt(pow(a[0] - b[0], 2.0) + pow(a[1] - b[1], 2.0))


tour = []
tour_length = 2 ** 30


def calc_length(n, p):
    global points
    length = 0
    for i in range(n):
        length += dist(points[p[i] - 1], points[p[(i + 1) % n] - 1])
    return length


def update_tour(n, p):
    global tour, tour_length
    tmp_length = calc_length(n, p)
    if tmp_length < tour_length:
        tour_length = tmp_length
        tour = p.copy()


def permutations(n, p):
    if len(p) == n:
        update_tour(n, p)
        return
    for i in range(1, n + 1):
        if i in p:
            continue
        p.append(i)
        permutations(n, p)
        del p[-1]


n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]

permutations(n, [])
print(f"{tour_length:.12f}")
print(" ".join(map(str, tour)))
