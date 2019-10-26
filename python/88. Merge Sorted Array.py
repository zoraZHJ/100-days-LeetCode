class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        len_nums1 = m
        while(i<len_nums1 and j<n):
            if nums1[i] <= nums2[j]:
                i += 1
                continue
            elif nums1[i] > nums2[j]:
                for idx in range(len_nums1-1,i-1,-1):
                    nums1[idx + 1] = nums1[idx]
                nums1[i] = nums2[j]
                j += 1
                i += 1
                len_nums1 += 1
        while(j<n):
            nums1[i]= nums2[j]
            j += 1
            i += 1