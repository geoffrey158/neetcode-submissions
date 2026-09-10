class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-1):
            #if the first element is greater than 0 
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue 

            a = nums[i]
            left = i + 1
            right = len(nums)-1

            while left < right:

                totalSum = a + nums[left] + nums[right]
                if totalSum == 0:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values for the second number
                    while nums[left] == nums[left - 1] and left < right: #
                        left += 1
                    # Skip duplicate values for the third number
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif totalSum > 0:
                    right -= 1
                else:
                    left += 1
            
        return res 