class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1) #number of characters in s1 
        n2 = len(s2) #number of characters in s2 

        #26 length because the condition states only lower case alphabetical letters 
        countS1 = [0] * 26 #used to count the characters of s1 
        countS2 = [0] * 26 #used to count the characters of s2 
        #base case: if s2 is shorter than s1 than it has to be false
        if len(s2) < len(s1):
            return False 

        #count the characters in the first window size, based on size of s1 
        for i in range(n1):
            countS1[ord(s1[i]) - ord('a')] += 1 
            countS2[ord(s2[i]) - ord('a')] += 1 

        #iterate through s2 based on the fixed window size 
        #there is a fixed window size based on length of s1 
        for i in range(n2-n1):

            #if the lists are the same amount of characters return True 
            if countS1 == countS2:
                return True 
            
            #as we shift the window to the right
            #adjust the left side of window,remove an element 
            countS2[ord(s2[i]) - ord('a')] -= 1
            #adjust the right side of window, add an element 
            countS2[ord(s2[i+n1]) - ord('a')] += 1

        
        return countS1 == countS2