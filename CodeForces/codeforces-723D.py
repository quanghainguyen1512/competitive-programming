# khi làm và submit thì em bị lỗi ở test case 26 như link sau
# link submission: http://codeforces.com/contest/723/submission/40685958
# tuy nhiên, ý tưởng và triển khai khá giống với bài sửa trên lớp của anh Phúc
# sau khi chạy thử test case bị lỗi trên laptop, python báo lỗi đệ quy hàm visitOcean quá nhiều lần
# hiện tại em không biết tối ưu như thế nào, mong anh/chị TA giúp đỡ
import sys

sys.setrecursionlimit(1000000)

class Lake:
    def __init__(self, x, y, cnt):
        self.x = x
        self.y = y
        self.countCell = cnt
    def __lt__(self, other):
        if self.countCell < other.countCell:
            return True
        return False

def visitOcean(i, j):
    if i < 0 or i == n or j < 0 or j == m or map[i][j] == '*' or visited[i][j]:
        return
    visited[i][j] = True
    visitOcean(i + 1, j)
    visitOcean(i - 1, j)
    visitOcean(i, j - 1)
    visitOcean(i, j + 1)

def countCellsInLake(i, j):
    if visited[i][j] or i < 0 or i == n or j < 0 or j == m or map[i][j] == '*':
        return 0
    visited[i][j] = True
    return 1 + countCellsInLake(i + 1, j) + countCellsInLake(i - 1, j) + countCellsInLake(i, j + 1) + countCellsInLake(i, j - 1)

def fillLake(i, j):
    if i < 0 or i == n or j < 0 or j == m or map[i][j] == '*' or visited[i][j]:
        return
    map[i] = map[i][:j] + '*' + map[i][j + 1:m]
    visited[i][j] = True
    fillLake(i + 1, j)
    fillLake(i - 1, j)
    fillLake(i, j - 1)
    fillLake(i, j + 1)

####### main
n, m, k = map(int, input().split())
visited = [[False for i in range(m)] for j in range(n)]
map = []
lakes = []
cellToDel = 0

for i in range(n):
    line = input()
    map.append(line)

for i in range(m):
    if not visited[0][i] and map[0][i] == '.':
        visitOcean(0, i)
    if not visited[n - 1][i] and map[n - 1][i] == '.':
        visitOcean(n - 1, i)

for i in range(n):
    if not visited[i][0] and map[i][0] == '.':
        visitOcean(i, 0)
    if not visited[i][m - 1] and map[i][m - 1] == '.':
        visitOcean(i, m - 1)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and map[i][j] == '.':
            count = countCellsInLake(i, j)
            lakes.append(Lake(i, j, count))

lakes.sort()
visited = [[False for i in range(m)] for j in range(n)]
for i in range(len(lakes) - k):
    cellToDel += lakes[i].countCell
    fillLake(lakes[i].x, lakes[i].y)

print(cellToDel)
for i in range(n):
    print(map[i])
