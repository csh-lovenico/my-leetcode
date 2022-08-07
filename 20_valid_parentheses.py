s = "()"

stack = []
result = False

for i in range(len(s)):
    if s[i] == "(" or s[i] == "{" or s[i] == "[":
        stack.append(s[i])
    elif s[i] == ")":
        if len(stack) == 0:
            result = False
            break
        stack_top = stack.pop()
        if stack_top != "(":
            result = False
            break
    elif s[i] == "}":
        if len(stack) == 0:
            result = False
            break
        stack_top = stack.pop()
        if stack_top != "{":
            result = False
            break
    elif s[i] == "]":
        if len(stack) == 0:
            result = False
            break
        stack_top = stack.pop()
        if stack_top != "[":
            result = False
            break

    if len(stack) != 0:
        result = False
