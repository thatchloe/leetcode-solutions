class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        re = -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                re = i
                break
        return re
