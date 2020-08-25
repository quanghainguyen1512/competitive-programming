from queue import PriorityQueue

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        pq = PriorityQueue()
        lst = list(map(int, input().split()))
        for i in lst:
            pq.put(i)
        cost = 0
        while not pq.empty():
            # print(pq.queue)
            top = pq.get()
            if pq.empty():
                break
            top += pq.get()
            cost += top
            pq.put(top)
        print(cost)

if __name__ == '__main__':
    main()
