# ý tưởng: đối xử chuỗi như một số có nhiều chữ số
# em thực hiện tăng chuỗi nhỏ hơn (là s) lên một đơn vị, nếu bằng với chuỗi t thì không tìm được
# nếu khác thì chuỗi vừa tạo chính là kết quả hợp lệ

def solve (s, t):
    index = len(s) - 1

    res = s
    res = res[:index] + chr(ord(res[index]) + 1) + res[index + 1:]
    while index != 0 and ord(res[index]) == 123:
        res = res[:index] + 'a' + res[index + 1:]
        res = res[:index - 1] + chr(ord(res[index - 1]) + 1) + res[index:]
        index -= 1
    
    if res == t:
        res = 'No such string'
    return res

def main():
    s = input()
    t = input()
    print(solve(s, t))

if __name__ == '__main__':
    main()