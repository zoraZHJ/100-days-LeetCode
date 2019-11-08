class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num not in hash:
                hash.update({num: 1})
            else:
                return True
        return False
        