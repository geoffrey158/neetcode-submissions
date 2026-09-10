class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0 
        count = len(nums) #keeps track of the number of values that are not val 
        notdup = 0 
        for n in nums:

            if n == val:
                count -= 1 
            else:
                nums[notdup] = n
                notdup += 1 


        

        return count