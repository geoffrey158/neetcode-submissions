class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Utilize a defaultdict to store lists of anagrams based on their sorted representation
        res = defaultdict(list)
        
        # Step 2: Iterate through each word in the input list
        for word in strs:
            count = [0] * 26 #26 values since it's a-z 

            # Step 3: Iterate through each letter in the word 
            for c in word: 
                count[ord(c) - ord('a')] += 1 
            
            res[tuple(count)].append(word) 

        return list(res.values())