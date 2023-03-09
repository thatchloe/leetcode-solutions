class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height)-1, 0
        maxi = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = max(area, w*h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area
