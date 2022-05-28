class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        area = 0
        while l < r:
            width = r-l
            if area < min(height[l],height[r]) * width:
                area = min(height[l],height[r]) * width
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area