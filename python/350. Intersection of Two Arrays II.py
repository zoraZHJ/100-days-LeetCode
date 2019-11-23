class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        res = []
        for num in nums1:
            if num not in dict1:
                dict1.update({num: 1})
            else:
                count = dict1[num] + 1
                dict1.update({num: count})
        for num in nums2:
            if num in dict1 and dict1[num] > 0:
                count = dict1[num] - 1
                dict1.update({num: count})
                res.append(num)
        return res