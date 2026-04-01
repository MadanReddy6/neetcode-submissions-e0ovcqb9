class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxConsecutive = 0

        for num in nums:
            # check num is sequence starting
            if num - 1 not in numSet:
                current = num
                length = 1
                while current + 1 in numSet:
                    current += 1
                    length += 1
                maxConsecutive = max(length , maxConsecutive)
        return maxConsecutive