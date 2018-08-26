def checkLoop(x, deps):
    visited[x] = 1
    for i in deps[x]:
        if visited[i] == 0 and checkLoop(i, deps):
            return True
        elif visited[i] == 1:
            return True
    visited[x] = 2
    return False

# deps = []                                   # dependencies
visited = []
t = int(input())
while t != 0:
    # f = open('result.txt', 'a')
    n, m = map(int, input().split())
    deps = [[] for i in range(n)]
    visited = [0 for i in range(n)]
    message = 'NAO'
    while m != 0:
        a, b = map(int, input().split())
        deps[a - 1].append(b - 1)
        m -= 1
    for i in range(n):
        if visited[i] == 0 and checkLoop(i, deps):
            message = 'SIM'
            break
    # f.writelines('{}\n'.format(message))
    print(message)
    t -= 1