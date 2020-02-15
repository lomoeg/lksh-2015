s1 = input()
s = s1.split()
stack = []
operation = '+-*'
for i in range(len(s)):
    result = 0
    if s[i] not in operation:
        stack.append(int(s[i]))
    else:
        if s[i] == '+':
            result = int(stack.pop()) + int(stack.pop())
        elif s[i] == '-':
            result = (int(stack.pop()) - int(stack.pop())) * -1
        else:
            result = int(stack.pop()) * int(stack.pop())
        stack.append(result)

print(*stack)