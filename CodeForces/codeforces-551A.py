# ý tưởng: tạo một mảng sorted_a là bản sao của a đồng thời đã được sắp xếp không tăng
# duyệt mảng a, sử dụng hàm index để lấy vị trí xuất hiện đầu tiên của mỗi giá trị của mảng a
# trong mảng sorted_a cộng thêm 1 sẽ được kết quả hợp lệ
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    sorted_a = a.copy()
    sorted_a.sort(reverse=True)
    i = 0
    while i < n:
        print(sorted_a.index(a[i]) + 1, end = ' ')
        i += 1
