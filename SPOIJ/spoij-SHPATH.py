#TLE

from queue import PriorityQueue

class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight

# tính chi phí từ 1 điểm đến tất cả các điểm còn lại 
def dijsktra(graph, start):
    pq = PriorityQueue()
    pq.put(Node(start, 0))
    res = dict()
    res[start] = 0
    while not pq.empty():
        top = pq.get()
        v = top.id
        w = top.weight
        for neighbor in graph[v]:
            if neighbor not in res or w + graph[v][neighbor] < res[neighbor]:
                res[neighbor] = w + graph[v][neighbor]
                pq.put(Node(neighbor, res[neighbor]))
    return res

### main
s = int(input())            # [the number of tests <= 10]
while s != 0:
    n = int(input())            # [the number of cities <= 10000]
    cities = dict()
    graph = dict()
    cost = dict()
    for i in range(n):
        name = input()
        cities[name] = i
        p = int(input())            
        if i not in graph:
            graph[i] = dict()
        while p != 0:
            nr, c = map(int, input().split())
            graph[i][nr - 1] = c
            p -= 1

    r = int(input())
    while r != 0:
        c1, c2 = input().split()
        i1, i2 = cities[c1], cities[c2]
        if i1 not in cost:
            # Nếu đỉnh này chưa được xử lý thì tính toán
            # sau đó dictionary cost sẽ lưu trữ dữ liệu chi phí được tính để sử dụng về sau
            cost[i1] = dijsktra(graph, i1)
        print(cost[i1][i2])
        r -= 1
    if input().isspace():
        continue
    s -= 1