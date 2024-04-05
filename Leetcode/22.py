class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(openP, closedP):
            if len(stack) == n * 2:
                ans.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closedP)
                stack.pop()

            if closedP < openP:
                stack.append(")")
                backtrack(openP, closedP + 1)
                stack.pop()
    
        backtrack(0, 0)
        return ans

