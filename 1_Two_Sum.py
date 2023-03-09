class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in premap: 
                return [premap[r], i]
            premap[n] = i
        return
