# Runtime Beats 80.74%, Memory Beat 59.93%

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"{":"}", "(":")", "[":"]"}
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and dict.get(stack[-1], "") == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return not len(stack)
