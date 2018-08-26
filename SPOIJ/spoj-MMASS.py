import queue as qu
case = 0
while True:    
    p, c = map(int, input().split())
    if p == 0 and c == 0: 
        break
    p = min(p, c)
    case += 1
    print('Case {}:'.format(case))
    q = qu.deque(range(1, p + 1))
    while c != 0:
        command = input().split()
        if command[0] == 'N':
            nexPer = q.popleft()
            print(nexPer)
            q.append(nexPer)
        else:
            emPer = int(command[1])
            if q.__contains__(emPer):
                q.remove(emPer)
            q.appendleft(emPer)
        c -= 1