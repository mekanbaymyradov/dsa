def main(line):
    pairs = {
        ')':'(',
        ']':'[',
        '}':'{',
    }
    stack = []

    for i in line:
        if i in '([{':
            stack.append(i)
        else:
            if not stack or stack[-1] != pairs[i]:
                print('no')
                return
            stack.pop()
        
    if not stack:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    n = input().strip()
    main(n)