class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        left = 0
        right = len(heights)-1

        while left <= right:
            w = right - left
            h = min(heights[left] , heights[right])
            currWater = w*h
            maxWater = max(currWater, maxWater)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxWater