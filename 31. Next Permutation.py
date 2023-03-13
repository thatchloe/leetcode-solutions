def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Step 1
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Step 2
        if i < 0:
            nums.reverse()
            return
        
        # Step 3
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Step 4
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5
        nums[i+1:] = reversed(nums[i+1:])
