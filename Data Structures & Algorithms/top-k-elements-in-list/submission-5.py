class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort, frequency is used as the key 
        freq = [[] for i in range(len(nums)+1)]
        
        #keep track how many times each number shows up 
        hashmap = {}
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        for num,count in hashmap.items():
            freq[count].append(num)

        res = [] #return value 

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]: 
                res.append(num)
                if len(res) == k:
                    return res

