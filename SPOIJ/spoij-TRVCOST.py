from queue import PriorityQueue
class Node:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost

def dijsktra(g, start):
    pq = PriorityQueue()
    pq.put(Node(start, 0))
    cost = dict()
    cost[start] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.cost
        for neighbor in g[u]:
            if neighbor not in cost or w + g[u][neighbor] < cost[neighbor]:
                cost[neighbor] = w + g[u][neighbor]
                pq.put(Node(neighbor, cost[neighbor]))
    return cost

def printRes(i, res):
    if i not in res:
        print('NO PATH')
    else:
        print(res[i])

n = int(input())
v = 0
graph = dict()
while n != 0:
    a, b, w = map(int,input().split())
    if not a in graph:
        graph[a] = dict()
    graph[a][b] = w
    if not b in graph:
        graph[b] = dict()
    graph[b][a] = w
    n -= 1
u = int(input())
q = int(input())
res = dijsktra(graph, u)
while q != 0:
    printRes(int(input()), res)
    q -= 1