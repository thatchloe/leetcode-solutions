class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        for i in range(n2-1, -1, -1):
            carry = 0
            for j in range(n1-1, -1, -1):
                curr = int(num2[i]) * int(num1[j]) + carry
                carry, res[i+j+1] = divmod(curr + res[i+j+1], 10)
            res[i] += carry
        while res and res[0] == 0:
            res.pop(0)
        return ''.join(map(str, res)) if res else '0'
