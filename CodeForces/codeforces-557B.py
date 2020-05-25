#https://codeforces.com/problemset/problem/557/B

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n]
    g = a[0]
    res = 0
    if b >= 2 * g:
        res = g * n * 3
    else:
        res = b / 2 * n * 3

    if res > w:
        res = w
    print(res)
    
if __name__ == '__main__':
    main()
