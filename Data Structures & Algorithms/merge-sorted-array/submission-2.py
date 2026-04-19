class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = m - 1
        R = len(nums1) - 1

        for i in range(n - 1, -1, -1):
            
            while L >= 0 and nums1[L] > nums2[i]:
                nums1[R] = nums1[L]
                nums1[L] = 0
                R -= 1 
                L -= 1
            nums1[R] = nums2[i]
            R -= 1