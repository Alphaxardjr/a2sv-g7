t = int(input())

for _ in range(t):
    s, k, m = map(int, input().split())

    last = (m // k) * k
    elapsed = m - last
    remaining = max(0, s - elapsed)

    print(remaining)
