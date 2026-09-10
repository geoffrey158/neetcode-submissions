class Solution(object):
    def topKFrequent(self, nums, k):

        #hashmap to count occurence of this value 
        count = {}

        #bucket sort but reversed a little 
        #index = frequency of element based on size of nums, 0 - len(nums)+1 
        #value = list of values that occur that many times 
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            #increase the count of the n value, if n doesnt exist yet we put a default value of 0
            count[n] = 1 + count.get(n,0)
            
        for n,c in count.items():
            freq[c].append(n)
        
        res = [] #result output 

        #start from highest frequence to low frequence of occurence
        #so start backwards from freq list 
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n) #appends the value that happens most often to list
                if len(res) == k: #if the size of the result output is the same as k we return the resulting list
                    return res

        #Time Complexity: O(n)
        #Space Complexity: O()




        