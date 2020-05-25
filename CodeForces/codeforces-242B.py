#https://codeforces.com/problemset/problem/242/B

def main():
    n = int(input())
    a = 1000000001
    b = i1 = i2 = -1

    for i in range(n):
        x, y = map(int, input().split())
        if x < a:
            a = x
            i1 = i
        elif x == a and y >= b:
            i1 = i2 = i
            b = y
        if y > b:
            b = y
            i2 = i
        elif y == b and x <= a:
            a = x
            i1 = i2 = i
    if i1 == i2:
        print(i1 + 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()
