class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "-" and stack:
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == "+" and stack:
                stack.append(stack.pop() + stack.pop())
            elif i == "*" and stack:
                stack.append(stack.pop() * stack.pop())
            elif i == "/" and stack:
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        
        return stack[0]

        