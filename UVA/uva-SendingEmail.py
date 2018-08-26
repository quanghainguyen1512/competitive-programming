# Em sử dụng dictionary để giảm bớt thời gian truy xuất nhưng có vẻ vẫn chưa tối ưu nhất
# Thời gian của submission thành công là 2.9s gần bằng limit time (3s)
# Em nghĩ có thể sẽ tự xây dựng PriorityQueue thêm khả năng remove một phần tử bất kì
# hoặc tìm cách loại bỏ việc xét các node không liên quan tới node T nhưng vẫn chưa nghĩ ra
# anh/chị T.A có thể giúp em cải tiến thêm được không ạ? Em cảm ơn :D

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
        if u not in g:                  # điều kiện này để loại bỏ test case không có bất kì node nào kết nối với nhau
            continue
        for neighbor in g[u]:
            if neighbor not in cost or w + g[u][neighbor] < cost[neighbor]:
                # vế not in cost ở đây tương ứng việc so sánh với MAX trong phương pháp trong slide
                cost[neighbor] = w + g[u][neighbor]
                pq.put(Node(neighbor, cost[neighbor]))
    return cost

N = int(input())
for i in range(1, N + 1):
    n, m, S, T = map(int, input().split())
    graph = dict()
    while m != 0:
        s, t, w = map(int,input().split())
        if s not in graph:
            graph[s] = dict()
        graph[s][t] = w
        if t not in graph:
            graph[t] = dict()
        graph[t][s] = w
        m -= 1

    costDict = dijsktra(graph, S)
    res = ''
    if T in costDict:
        res = costDict[T]
    else:
        res = 'unreachable'
    print('Case #{}: {}'.format(i, res))