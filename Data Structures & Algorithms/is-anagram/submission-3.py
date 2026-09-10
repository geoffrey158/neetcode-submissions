class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmapS = {}
        hashmapT = {}

        #we know the length of s and t are the same from here 
        for i in range(len(s)):
            
            hashmapS[s[i]] = 1 + hashmapS.get(s[i],0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i],0)


        return hashmapS == hashmapT 
        