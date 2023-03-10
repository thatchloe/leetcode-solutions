class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_pa = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in map_pa:
                stack.append(c)
            elif not stack or map_pa[stack.pop()] != c:
                return False
        return stack == []
