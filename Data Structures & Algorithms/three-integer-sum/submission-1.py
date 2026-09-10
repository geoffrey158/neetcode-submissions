class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = [] 
        nums.sort()

        #iterate through nums 
        #i = idx
        #a = value
        for i, a in enumerate(nums):
            if a > 0:
                break

            #don't want to use same value in the same position
            #checks for duplicates 
            if i > 0 and a==nums[i-1]:
                continue

            #after finding a value, do the same thing as twosum 
            left = i+1 
            right = len(nums) - 1 

            while left<right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1 
                elif threeSum < 0:
                    left += 1 
                else: #threesum is 0 
                    ans.append([a, nums[left],nums[right]])
                    left += 1
                    #checks for duplicates 
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                
        return ans 

        #Time Complexity: O(n^2)
        #Space Complexity: O(1) or O(n) extra space depending on the sorting algorithm. 
        #O(m) space for the output list.