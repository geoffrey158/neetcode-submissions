class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for n in range(len(nums)+1)]

        hashmap = {} 

        res = []#return value
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        for idx,count in hashmap.items():
            freq[count].append(idx)

        for i in range(len(freq)-1,0,-1):

            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
        