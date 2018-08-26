# Ở đây em không sử dụng list để lưu trữ các segment mà thực hiện so sánh ngay khi nhập dữ liệu
# với ý tưởng lưu vị trí có phần tử nhỏ nhất và có phần tử lớn nhất
# nếu 2 vị trí đó trùng nhau thì ta có một segment bao hết tất cả các segment khác

n = int(input())
a = 1000000001
b = i1 = i2 = -1

for i in range(n):
    x, y = map(int, input().split())
    if x < a:
        a = x
        i1 = i
    elif x == a and y >= b:
        i1 = i2 = i
        b = y
    if y > b:
        b = y
        i2 = i
    elif y == b and x <= a:
        a = x
        i1 = i2 = i
if i1 == i2:
    print(i1 + 1)
else:
    print(-1)
