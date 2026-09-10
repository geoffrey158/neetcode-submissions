class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #same amount of characters between two strings and same amount of characters
        #initial condition
        if len(s) != len(t):
            return False 

        #hashmap 
        hashmapS = {}
        hashmapT = {}

        #doesn't matter which len to use here b/c of intial condition 
        #we know they have the same # of characters
        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get(s[i],0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i],0)

        return hashmapS == hashmapT 

