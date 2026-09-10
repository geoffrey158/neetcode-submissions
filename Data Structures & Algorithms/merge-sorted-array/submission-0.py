class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        n1 = m - 1 #tracker for nums1
        n2 = n - 1 #tracker for nums2

        while n2 >= 0:
            if n1 >= 0 and nums1[n1] > nums2[n2]:
                nums1[last] = nums1[n1]
                n1 -= 1
            else:
                nums1[last] = nums2[n2]
                n2 -= 1
                
            last -= 1