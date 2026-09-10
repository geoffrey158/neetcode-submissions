class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0 
        count = 0 
        notdup = 0 
        for n in nums:

            if n == val:
                count += 1
            else:
                nums[notdup] = n
                notdup += 1 


        

        return len(nums) - count 