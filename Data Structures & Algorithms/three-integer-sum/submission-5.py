class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] > 0:
                break

            if i>0 and nums[i] == nums[i-1]:
                continue

            a = nums[i]
            left = i + 1 
            right = len(nums) - 1
            
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