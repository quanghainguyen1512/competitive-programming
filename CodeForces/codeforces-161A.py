#https://codeforces.com/problemset/problem/161/A

def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    i = j = 0
    while i < n and j < m:
        if b[j] > a[i] + y:
            i += 1
        elif b[j] < a[i] - x:
            j += 1
        else:
            i += 1
            j += 1
            a[count] = i
            b[count] = j
            count += 1
    print(count)
    for x in range(count):
        print(a[x], b[x], sep = ' ')

if __name__ == '__main__':
    main()
