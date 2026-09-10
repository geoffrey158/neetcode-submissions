class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return indexes of numbers that add up to target
        #smaller first 
        hashmap = {}

        for n in range(len(nums)):
            complement = target - nums[n] 

            if complement in hashmap:
                return [hashmap[complement],n]
            #store index 
            hashmap[nums[n]] = n 
        return None 