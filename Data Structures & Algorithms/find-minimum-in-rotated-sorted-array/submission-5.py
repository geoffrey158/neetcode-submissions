class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')#return value

        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            res = min(res,nums[mid])
            #check to see if array is rotated
            
            if nums[mid] < nums[left]: #array is rotated                    
                right = mid - 1 
            elif nums[mid] > nums[left] and nums[mid] < nums[right]: #array is not rotated
                right = mid - 1 
            else:
                left = mid + 1 
    

        return res 