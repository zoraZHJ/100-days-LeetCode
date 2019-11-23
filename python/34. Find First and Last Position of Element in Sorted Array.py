class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        not_found = [-1, -1]
        len_nums = len(nums)
        if len_nums == 0:
            return not_found
        i = 0
        j = len_nums - 1
        if target < nums[i] or nums[j] < target:
            return not_found
        
        start_first = 0
        start_last = -1
        end_first = -1
        end_last = len_nums - 1
        
        start = -1
        end = -1

        while i <= j:
            mid = (i + j)//2

            if nums[i] == target:
                start_last = i
            if nums[j] == target:
                end_first = j

            if nums[mid] < target:
                i = mid + 1
                start_first = i
            elif nums[mid] > target:
                j = mid - 1
                end_last = j
            elif nums[mid] == target:
                if start_last == -1:
                    start_last = mid
                if end_first == -1:
                    end_first = mid
                break
        if start_last == -1 and end_first == -1:
            return not_found
        
        
        while start_first <= start_last:
            mid = (start_first + start_last) // 2
            if nums[mid] == target:
                if mid == 0 or (mid!=0 and nums[mid-1] != target):
                    start = mid
                    break
                elif nums[mid-1] == target:
                    start_last = mid - 1
            elif nums[mid] < target:
                start_first = mid + 1
            elif nums[mid] > target:
                start_last = mid - 1

        while end_first <= end_last:
            mid = (end_first + end_last) // 2
            if nums[mid] == target:
                if mid == end_last or (mid != (len_nums - 1) and nums[mid+1] != target):
                    end = mid
                    break
                elif nums[mid+1] == target:
                    end_first = mid + 1
            elif nums[mid] < target:
                end_first = mid + 1
            elif nums[mid] > target:
                end_last = mid - 1

        return [start, end]

