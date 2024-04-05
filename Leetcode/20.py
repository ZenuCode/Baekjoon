class Solution:
    def isValid(self, s: str) -> bool:
        que = []

        if len(s) < 2:
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                que.append(i)
            else:
                if que:
                    compare = que.pop()
                    if i == ")" and compare != "(":
                        return False
                    elif i == "]" and compare != "[":
                        return False
                    elif i == "}" and compare != "{":
                        return False
                else:
                    return False
        
        if que: return False
        else: return True
