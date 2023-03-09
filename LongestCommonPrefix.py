class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       if not strs:
           return ''
       prefix = min(strs, key=len)
       for i in range(len(prefix)):
           for s in strs:
               if prefix[i] != s[i]:
                   return prefix[:i]
       return prefix
