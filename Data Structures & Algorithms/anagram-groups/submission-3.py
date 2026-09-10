class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        #iterate through every word in the list 
        for word in strs:
            count = [0]*26 #keeps track of all the letters in a word 
            #iterate through every character in the word 
            for c in word:    
                count[ord(c)-ord('a')] += 1 
            
            res[tuple(count)].append(word)

        return list(res.values())

