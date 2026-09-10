class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = [0] * (len(nums)*2)

        for n in range(len(nums)):

            res[n] = nums[n]
            res[n+len(nums)] = nums[n]


        return res 