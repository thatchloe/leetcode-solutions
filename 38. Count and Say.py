class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        
        return self.make_count(self.countAndSay(n-1))
        
    @staticmethod
    def make_count(n: str) -> str:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(n))
