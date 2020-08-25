from queue import PriorityQueue

class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight

def dijsktra(g, start):
    pq = PriorityQueue()
    pq.put(Node(start, 0))
    cost = dict()
    cost[start] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight
        for neighbor in g[u]:
            if neighbor not in cost or w + g[u][neighbor] < cost[neighbor]:
                cost[neighbor] = w + g[u][neighbor]
                pq.put(Node(neighbor, cost[neighbor]))
    return cost

def main():
    N = int(input())
    for i in range(1, N + 1):
        n, m, S, T = map(int, input().split())
        # graph = dict()
        graph = [[1e9 for i in range(n)] for j in range(n)]
        while m != 0:
            s, t, w = map(int,input().split())
            # if s not in graph:
            #     graph[s] = dict()
            graph[s][t] = w
            # if t not in graph:
            #     graph[t] = dict()
            graph[t][s] = w
            m -= 1

        costDict = dijsktra(graph, S)
        res = 'unreachable'
        if T in costDict:
            res = costDict[T]
        print('Case #{}: {}'.format(i, res))

if __name__ == '__main__':
    main()