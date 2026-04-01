class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = nums[0]

        for i in range(len(nums)):
            low = min(low , nums[i])

        return low