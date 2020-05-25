#https://codeforces.com/problemset/problem/551/A

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(1)
    else:
        sorted_a = a.copy()
        sorted_a.sort(reverse=True)
        i = 0
        while i < n:
            print(sorted_a.index(a[i]) + 1, end = ' ')
            i += 1
    
if __name__ == '__main__':
    main()

