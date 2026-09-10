class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = [] 
        for n in range(len(nums)):

            if nums[n] > 0:
                break
            if n > 0 and nums[n-1] == nums[n]:
                continue
            
            a = nums[n]
            left = n + 1  
            right = len(nums)-1 
            
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1  
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif threeSum > 0:
                    right -= 1 
                else:
                    left += 1 
        return res 