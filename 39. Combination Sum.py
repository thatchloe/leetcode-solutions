class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if sum(path) > target:
            return 
        if sum(path) == target:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target, path+[nums[i]], ret)
