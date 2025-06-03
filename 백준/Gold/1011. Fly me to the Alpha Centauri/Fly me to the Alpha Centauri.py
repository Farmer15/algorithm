import math

def max_n_given_y(x, y):
    k = y - x

    n = int((-1 + math.sqrt(1 + 4 * k)) // 2)
    r = k - n * (n + 1)

    if r == 0:
      return 2 * n
    elif r <= n + 1:
      return 2 * n + 1
    else:
      return 2 * n + 2

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    print(max_n_given_y(x, y))