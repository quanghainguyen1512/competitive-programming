#https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3359 

def getMass(atom):
    if atom == 'H':
        return 1
    elif atom == 'C':
        return 12
    elif atom == 'O':
        return 16
    else:
        return 0

def solve(formula):
    stack = []
    for i in range(len(formula)):
        char = formula[i]
        if char == '(':
            stack.append(-1)
        elif char == ')':
            temp = 0
            while stack[-1] != -1:
                temp += stack.pop()
            stack[-1] = temp
        elif char.isnumeric():
            stack.append(stack.pop() * int(char))
        else:
            stack.append(getMass(char))
    return sum(stack)

def main():
    a = input()
    print(solve(a))

if __name__ == '__main__':
    main()