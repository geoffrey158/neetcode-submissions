class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #return the minimum element in thte array 
        #array could be rotated 
        #array is sorted in ascending order 
        
        #binary search 
        left = 0
        right = len(nums) - 1 
        res = nums[0] 

        while left <= right: 
            mid = left + right-left//2 
            res = min(res,nums[mid])
            #check if the mid element to last element of array to see if it's been rotated 
            if nums[mid] > nums[right]:# it means the array has been rotated 
                left = mid + 1 
            else: #it means the array has not been rotated
                right = mid - 1 

        return res 

        