#https://codeforces.com/problemset/problem/572/A
 
def main():
    n1, n2 = map(int, input().split())
    k, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = 'NO'

    if a[k - 1] < b[n2 - m]:
        result = 'YES'

    print(result)

if __name__ == '__main__':
    main()
