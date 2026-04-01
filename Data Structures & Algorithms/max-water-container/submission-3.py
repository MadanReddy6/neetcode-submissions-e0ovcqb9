class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0
        left = 0
        right = len(heights)-1

        while left < right:

            h = min(heights[left] , heights[right])
            w = right - left
            currentWater = h * w

            maxWater = max(currentWater, maxWater)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxWater