# Do 2 mảng a và b là mảng không giảm nên
# em chỉ cần kiểm tra phần tử cuối cùng của đoạn k lấy từ a có nhỏ hơn phần tử đầu tiên 
# của đoạn m lấy từ mảng b hay không
 
n1, n2 = map(int, input().split())
k, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 'NO'

if a[k - 1] < b[n2 - m]:
    result = 'YES'

print(result)