class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we need to return the indexes 
        #use hashmap to track of indexes 
        hashmap = {}

        for i,n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[n] = i