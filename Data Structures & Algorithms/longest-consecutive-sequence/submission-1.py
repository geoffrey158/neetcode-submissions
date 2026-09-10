class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #must be of O(n) time 
        #if we short the algorith first, that is O(nlogn)

        #brute force

        if not nums:
            return 0 
        res = 0
        nums.sort()

        curr = nums[0]
        streak = 0 
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1 
            streak += 1
            curr += 1
            res = max(res, streak)
        return res