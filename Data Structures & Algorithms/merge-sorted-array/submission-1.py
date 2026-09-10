class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1 #length of nums1 
        n1 = m - 1 #counter for nums1
        n2 = n - 1 #counter for nums2

        #merge in reverse order bc both nums1 and nums2 are sorted in ascending order
        while n2 >= 0: #decrement n until there are no elements left

            #if n1 counter is still greater than or equal to 0 
            #if the last element of nums1 is greater than nums2, we add the value to the end of nums1
            if n1 >= 0 and nums1[n1] > nums2[n2]:
                nums1[last] = nums1[n1]
                n1 -= 1 #decrement the value of n1 as we add it to the end of the list 
            else:
                nums1[last] = nums2[n2]
                n2 -= 1 #decrement the value of n2 as we add it to the end of the list 
                
            last -= 1 #decrement as we add another element to the end of the list 