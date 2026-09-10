class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #key = idx 
        #value = num in idx 

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                #return answer with smaller idx first
                #hashmap[complement] first bc needs to be added to hashmap first
                return [hashmap[complement],i] 
            hashmap[nums[i]] = i 
        