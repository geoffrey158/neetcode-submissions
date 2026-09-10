class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #base case
        if len(s1) > len(s2):
            return False

        #count all characters in S1 
        hashmapS1 = {}
        for c in range(len(s1)):
            hashmapS1[s1[c]] = 1 + hashmapS1.get(s1[c],0)
        
        #window has to be length of s1 
        hashmapS2 = {} 
        left = 0
        for right in range(len(s2)):
            #if character is in string
            hashmapS2[s2[right]] = 1 + hashmapS2.get(s2[right],0)
            
            if right-left+1> len(s1):
                hashmapS2[s2[left]] -= 1
                
                if hashmapS2[s2[left]] == 0: 
                    del hashmapS2[s2[left]]
                left += 1 
            if hashmapS1 == hashmapS2:
                return True
        return False
