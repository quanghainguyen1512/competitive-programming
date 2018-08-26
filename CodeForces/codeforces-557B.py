# ý tưởng: sắp xếp mảng a, sau đó so sánh vị trí 0 và n có giá trị lần lượt là b và g
# nếu b >= 2 * g thì nữ uống nhiều nhất đúng bằng lượng g và nam là 2 * g
# ngược lại thì nữ sẽ uống lượng nhiều nhất là b / 2 và nam là b
# tính toán tổng lượng nước và trả về biến res
# cuối cùng so sánh biến res với lượng nước tối đa ban đầu w

n, w = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = a[n]
g = a[0]
res = 0
if b >= 2 * g:
    res = g * n * 3
else:
    res = b / 2 * n * 3

if res > w:
    res = w
print(res)