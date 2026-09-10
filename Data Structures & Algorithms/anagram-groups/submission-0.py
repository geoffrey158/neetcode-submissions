class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Utilize a defaultdict to store lists of anagrams based on their sorted representation
        ans = defaultdict(list)
        
        # Step 2: Iterate through each word in the input list
        for word in strs:
            # Step 3: Sort the characters of each word to obtain a canonical representation
            sorted_word = ''.join(sorted(word))
            
            # Step 4: Append the original word to the list associated with its sorted form in the defaultdict
            ans[sorted_word].append(word)

        # Step 5: Return the values (anagram groups) of the defaultdict
        return list(ans.values())