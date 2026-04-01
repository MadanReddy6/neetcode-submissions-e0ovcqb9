class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            currProd = 1
            for j in range( len(nums)):
                if i != j:
                    currProd = currProd * nums[j]
            res[i]=currProd

        return res