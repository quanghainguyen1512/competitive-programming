#https://codeforces.com/problemset/problem/518/A

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