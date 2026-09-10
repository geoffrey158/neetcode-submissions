class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create an array ans of length 2n 

        ans = [0] * (2*len(nums))

        for n in range(len(nums)):
            ans[n] = nums[n]
            ans[n+len(nums)] = nums[n]
        

        return ans

        #time complexity: O(n)
        #space complexity: O(n) for the output array 
        
        