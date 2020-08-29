# https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: list, target: int) -> int:
        i_head = 0
        i_tail = len(nums)
        first = nums[i_head]
        while i_tail - i_head > 1:
            mid = (i_tail - i_head) // 2 + i_head
            val = nums[mid]
            if val == target: 
                return mid
            elif val < target:
                if target < first:
                    return self.bin_search(nums[mid + 1:i_tail], target, anchor=mid + 1)
                elif val > first:
                    i_head = mid
                else:
                    i_tail = mid 
            else: # val > target
                if target >= first:
                    return self.bin_search(nums[i_head:mid], target, anchor=i_head)
                elif val < first:
                    i_tail = mid
                else:
                    i_head = mid
        i_last = (i_tail - i_head) // 2 + i_head
        return i_last if nums[i_last] == target else -1
            
    def bin_search(self, sublist: list, target: int, anchor: int = 0) -> int:
        n = len(sublist)
        if n == 0:
            return -1
        mid = n // 2
        val = sublist[mid]
        if target == val:
            return mid + anchor
        elif val < target:
            return self.bin_search(sublist[mid + 1:], target, anchor=mid+1+anchor)
        else:
            return self.bin_search(sublist[:mid], target, anchor=anchor)
