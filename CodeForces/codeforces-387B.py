def solve (n, m, a, b):
    count = 0
    i = j = 0
    # for i in range(n):
    #     while j < m:
    #         if a[i] <= b[j]:
    #             j += 1
    #             count +=1
    #             break
    #         j += 1
    #     if j == m:
    #         break

    while i < n and j < m:
        if a[i] <= b[j]:
            count += 1
            j += 1
            i += 1
        else:
            j += 1
    return n - count
            
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solve(n, m, a, b))
