def solve(n, t, a):
    time = 0
    res = 0
    j = 0
    for i in range(n):
        if time + a[i] <= t:
            time += a[i]
        else:
            time += a[i]
            while time > t:
                time -= a[j]
                j += 1
        res = max(res, i - j + 1)
    return res

n, t = map(int, input().split())
a = list(map(int, input().split()))

print(solve(n, t, a))

# O(n)