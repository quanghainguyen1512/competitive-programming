# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=734

parent = []
ranks = []
def makeSet(n):
    global parent, ranks                      # for python 3.5
    parent = []
    ranks = []
    for i in range(n):
        parent.append(i)
        ranks.append(0)

def findSet(u):
    if parent[u] != u:
        # return findSet(parent[u])
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] +=1

def main():
    t = int(input())
    input()
    while t != 0:
        SUCCESSFULL_ANSWER, UNCCESSSFULL_ANSWER = 0, 0
        computers = int(input())
        makeSet(computers)
        while True:
            line = input().split()
            if len(line) == 0:
                break
            cmd = line[0]
            i, j = int(line[1]), int(line[2])
            i -= 1
            j -= 1
            if cmd == 'c':
                unionSet(i, j)
            elif cmd == 'q':
                if findSet(i) == findSet(j):
                    SUCCESSFULL_ANSWER += 1
                else:
                    UNCCESSSFULL_ANSWER += 1
        t -= 1
        print(SUCCESSFULL_ANSWER, ',', UNCCESSSFULL_ANSWER, sep='')

if __name__ == '__main__':
    main()