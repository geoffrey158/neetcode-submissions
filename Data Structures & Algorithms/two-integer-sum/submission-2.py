class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the indices 
        res = [] 
        
        hashmap = {} #use hashmap to store value and index
        for n in range(len(nums)):
            
            complement = target - nums[n]

            if complement in hashmap:
                return [hashmap[complement],n]

            hashmap[nums[n]] = n

        
