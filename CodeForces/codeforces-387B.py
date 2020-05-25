def solve (n, m, a, b):
    count = 0
    i = j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            count += 1
            j += 1
            i += 1
        else:
            j += 1
    return n - count
            
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve(n, m, a, b))

if __name__ == '__main__':
    main()
