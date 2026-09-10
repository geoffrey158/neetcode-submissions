class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0 

        left = 0 
        res = 0 #return value, keep tracking of largest consecutive 1s 

        for right in range(len(nums)):
            
            #if the right pointer is not 1 
            if nums[right] != 1:
                left = right+1
                
            
            res = max(res,right-left+1)

        return res 

            