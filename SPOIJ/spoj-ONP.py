def getPriority(c):
    if c == '+' or c == '-':
        return 1
    elif c == '*' or c == '/':
        return 2
    elif c == '^':
        return 3
    else:
        return -1

def isOperand(c):
    return len(c) == 1 and c.islower()

def solve(exp):
    stack = []
    for i in range(len(exp)):
        char = exp[i]
        if isOperand(char):
            print(char, end='')
        elif char == '(':
            stack.append(exp[i])
        elif char == ')':
            while len(stack) != 0 and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            while len(exp) != 0 and getPriority(exp[i]) <= getPriority(stack[-1]):
                print(stack.pop(), end='')
            stack.append(exp[i])

n = int(input())

while n != 0:
    exp = input()
    solve(exp)
    print('')
    n -= 1
