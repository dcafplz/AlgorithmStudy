# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(low, high):
            if high - low < 2:
                return
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid, high)
            merge(low, mid, high)

        def merge(low, mid, high):
            temp = []
            l, h = low, mid

            while l < mid and h < high:
                if nums[l] < nums[h]:
                    temp.append(nums[l])
                    l += 1
                else:
                    temp.append(nums[h])
                    h += 1

            while l < mid:
                temp.append(nums[l])
                l += 1
            while h < high:
                temp.append(nums[h])
                h += 1

            for i in range(low, high):
                nums[i] = temp[i - low]
                
        sort(0, len(nums))
        return nums
