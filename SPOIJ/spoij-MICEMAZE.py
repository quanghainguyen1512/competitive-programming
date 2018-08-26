n = int(input())
e = int(input())
t = int(input())
m = int(input())
graph = [[0 for i in range(n)] for i in range(n)]
while m != 0:
    a, b, w = map(int, input().split())
    m -= 1