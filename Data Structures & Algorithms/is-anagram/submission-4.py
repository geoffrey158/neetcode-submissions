class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hashmapS = {} 
        hashmapT = {} 

        for n in range(len(s)):
            hashmapS[s[n]] = 1 + hashmapS.get(s[n],0)
            hashmapT[t[n]] = 1 + hashmapT.get(t[n],0)
        
        return hashmapS == hashmapT 