class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort 
        #frequency list 
        freq = [[] for i in range(len(nums)+1)] 
        #max freq = length of num array 
        hashmap = {} 

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        #value,# of occurence 
        for n,i in hashmap.items():
            freq[i].append(n)
    
        res = [] 

        for i in range(len(freq)-1,0,-1):

            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res