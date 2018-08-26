# ý tưởng: sắp xếp mảng c tăng dần, sau đó dùng biến i để duyệt xuôi và ngược lại
# mỗi lượt duyệt tính toán thời gian, sau đó so sánh 2 thời gian và in ra kết quả nhỏ hơn
# độ phức tạp: O(n)

n, x = map(int, input().split())
c = list(map(int, input().split()))

c.sort()
t1 = t2 = 0
i = 0
x_ = x
while i < n:
    t1 += c[i] * x
    if x > 1:
        x -= 1
    i += 1

while i != 0:
    i -= 1
    t2 += c[i] * x_
    if x_ > 1:
        x_ -= 1

print(min(t1, t2))