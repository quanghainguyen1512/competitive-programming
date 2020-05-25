#https://codeforces.com/problemset/problem/439/B
#O(n)

def main():
    n, x = map(int, input().split())
    c = list(map(int, input().split()))

    c.sort()
    t1 = t2 = 0
    i = 0
    x_ = x
    while i < n:
        t1 += c[i] * x
        if x > 1:
            x -= 1
        i += 1

    while i != 0:
        i -= 1
        t2 += c[i] * x_
        if x_ > 1:
            x_ -= 1

    print(min(t1, t2))

if __name__ == '__main__':
    main()